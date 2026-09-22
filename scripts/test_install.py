#!/usr/bin/env python3
"""Isolated installer checks: python3 -m unittest discover -s scripts -v."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import install
import validate


EXPECTED_CORE = {
    "bootstrap-project-context", "capture-workflow", "compare-options",
    "debug-with-evidence", "frame-problem", "verify-delivery",
}
EXPECTED_PACKAGE = EXPECTED_CORE | {"layered-learning-design"}


def files(folder):
    """Read every installed resource, including binary and nested files."""
    return {
        path.relative_to(folder).as_posix(): path.read_bytes()
        for path in folder.rglob("*") if path.is_file()
    }


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / "package"
        self.source = self.package / "skills"
        self.script = self.package / "scripts" / "install.py"
        self.script.parent.mkdir(parents=True)
        shutil.copyfile(Path(install.__file__), self.script)
        for name in EXPECTED_PACKAGE:
            self.add_skill(name)
        self.destination = self.root / "installed"

    def add_skill(self, name):
        folder = self.source / name
        (folder / "references" / "nested").mkdir(parents=True)
        (folder / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: "Fixture skill."\n---\n'
            f"# {name}\n保留实际文件内容。\n", encoding="utf-8",
        )
        (folder / "references" / "nested" / "sample.bin").write_bytes(
            b"\x00\xff\r\n" + name.encode("utf-8")
        )

    def run_installer(self, *args, destination=None):
        return subprocess.run(
            [sys.executable, str(self.script), "--dest",
             str(destination or self.destination), *args],
            capture_output=True, text=True, encoding="utf-8",
        )

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_installed(self, names):
        self.assertEqual({path.name for path in self.destination.iterdir()}, set(names))
        for name in names:
            self.assertEqual(files(self.source / name), files(self.destination / name))

    def require_symlinks(self):
        probe = self.root / "link-probe"
        try:
            probe.symlink_to(self.source, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"Directory symlinks unavailable: {exc}")
        probe.unlink()

    def test_default_core_copies_complete_contents_and_repeat_skips(self):
        first = self.run_installer()
        self.assert_success(first)
        self.assert_installed(EXPECTED_CORE)
        before = files(self.destination)
        repeated = self.run_installer("--profile", "core")
        self.assert_success(repeated)
        self.assertEqual(repeated.stdout.count("SKIP:"), 6)
        self.assertEqual(files(self.destination), before)

    def test_all_discovers_every_skill_including_future_additions(self):
        self.add_skill("future-skill")
        self.assert_success(self.run_installer("--profile", "all"))
        self.assert_installed(EXPECTED_PACKAGE | {"future-skill"})

    def test_only_can_select_optional_skill_and_deduplicates(self):
        self.assert_success(self.run_installer(
            "--only", "layered-learning-design", "layered-learning-design",
        ))
        self.assert_installed({"layered-learning-design"})

    def test_only_and_explicit_profile_are_mutually_exclusive(self):
        result = self.run_installer("--only", "frame-problem", "--profile", "core")
        self.assertEqual(result.returncode, 2)
        self.assertFalse(self.destination.exists())

    def test_dry_run_has_no_filesystem_changes(self):
        before = files(self.root)
        result = self.run_installer("--profile", "all", "--dry-run")
        self.assert_success(result)
        self.assertEqual(result.stdout.count("COPY:"), 7)
        self.assertIn("no files written", result.stdout)
        self.assertFalse(self.destination.exists())
        self.assertEqual(files(self.root), before)

    def test_unknown_name_fails_without_writing(self):
        result = self.run_installer("--only", "frame-problem", "unknown-skill")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Unknown skills: unknown-skill", result.stderr)
        self.assertFalse(self.destination.exists())

    def test_conflict_is_preflighted_before_any_copy(self):
        conflict = self.destination / "verify-delivery"
        conflict.mkdir(parents=True)
        (conflict / "SKILL.md").write_text("Existing local changes", encoding="utf-8")
        before = files(self.destination)
        result = self.run_installer("--profile", "all")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Different content", result.stderr)
        self.assertEqual(files(self.destination), before)
        self.assertEqual(list(self.destination.iterdir()), [conflict])

    def test_destination_inside_sources_is_rejected(self):
        for destination in (self.source, self.source / "new-folder"):
            with self.subTest(destination=destination):
                before = files(self.package)
                result = self.run_installer(destination=destination)
                self.assertEqual(result.returncode, 1)
                self.assertIn("outside the source", result.stderr)
                self.assertEqual(files(self.package), before)

    def test_link_mode_installs_complete_resources_and_repeat_skips(self):
        self.require_symlinks()
        self.assert_success(self.run_installer("--profile", "all", "--mode", "link"))
        self.assert_installed(EXPECTED_PACKAGE)
        for name in EXPECTED_PACKAGE:
            target = self.destination / name
            self.assertTrue(target.is_symlink())
            self.assertEqual(target.resolve(), (self.source / name).resolve())
        repeated = self.run_installer("--profile", "all", "--mode", "link")
        self.assert_success(repeated)
        self.assertEqual(repeated.stdout.count("SKIP:"), 7)

    def test_different_existing_link_blocks_entire_install(self):
        self.require_symlinks()
        self.destination.mkdir()
        foreign = self.root / "foreign"
        foreign.mkdir()
        (self.destination / "verify-delivery").symlink_to(foreign, target_is_directory=True)
        result = self.run_installer("--profile", "all", "--mode", "link")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Different link", result.stderr)
        self.assertEqual(
            {path.name for path in self.destination.iterdir()}, {"verify-delivery"},
        )

    def test_plan_install_remains_read_only_and_honors_profile(self):
        with patch.object(install, "SKILLS_ROOT", self.source):
            plan = install.plan_install(self.destination, None, "copy")
            self.assertEqual({target.name for _, _, target in plan}, EXPECTED_CORE)
            plan = install.plan_install(self.destination, None, "copy", "all")
            self.assertEqual({target.name for _, _, target in plan}, EXPECTED_PACKAGE)
            self.assertFalse(self.destination.exists())


class PackageTests(unittest.TestCase):
    def test_real_package_all_seven_skills_install_without_missing_resources(self):
        self.assertEqual(set(install.available_skills()), EXPECTED_PACKAGE)
        self.assertEqual(set(install.CORE_SKILLS), EXPECTED_CORE)
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "installed"
            result = subprocess.run(
                [sys.executable, str(Path(install.__file__)), "--dest",
                 str(destination), "--profile", "all"],
                capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(files(install.SKILLS_ROOT), files(destination))

    def test_validator_reports_missing_core_profile_member(self):
        with patch.object(validate, "CORE_SKILLS", ("missing-core-skill",)):
            _, errors = validate.validate()
        self.assertIn("Core profile names a missing skill: missing-core-skill", errors)


if __name__ == "__main__":
    unittest.main()
