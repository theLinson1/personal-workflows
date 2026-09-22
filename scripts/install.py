#!/usr/bin/env python3
"""Install local skills with Python's standard library; never overwrite a skill."""

import argparse
import hashlib
import os
from pathlib import Path
import re
import shutil
import sys

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PACKAGE_ROOT / "skills"
CORE_SKILLS = (
    "bootstrap-project-context",
    "capture-workflow",
    "compare-options",
    "debug-with-evidence",
    "frame-problem",
    "verify-delivery",
)


def is_link(path):
    return path.is_symlink() or getattr(path, "is_junction", lambda: False)()


def snapshot(folder):
    """Compare complete skill contents without following nested links."""
    if not folder.is_dir():
        raise ValueError(f"Not a skill directory: {folder}")
    result = {}
    for path in sorted(folder.rglob("*")):
        if is_link(path):
            raise ValueError(f"Nested links are not supported: {path}")
        if path.is_file():
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
    return result


def available_skills():
    result = {}
    for folder in sorted(SKILLS_ROOT.iterdir()):
        if is_link(folder):
            raise ValueError(f"Source skill must be a real directory: {folder}")
        if not folder.is_dir():
            continue
        name = folder.name
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"Invalid skill directory name: {name}")
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"---\nname: ([a-z0-9-]+)\n", text)
        if not match or match.group(1) != name:
            raise ValueError(f"Skill name does not match directory: {folder}")
        result[name] = folder
    if not result:
        raise ValueError("No skills found")
    return result


def plan_install(destination, names, mode, profile=None):
    available = available_skills()
    if names and profile is not None:
        raise ValueError("Choose --only or --profile, not both")
    if profile not in (None, "core", "all"):
        raise ValueError(f"Unknown profile: {profile}")
    selected = sorted(set(names)) if names else sorted(
        available if profile == "all" else CORE_SKILLS
    )
    unknown = set(selected) - set(available)
    if unknown:
        raise ValueError("Unknown skills: " + ", ".join(sorted(unknown)))
    destination = destination.expanduser().resolve()
    source_root = SKILLS_ROOT.resolve()
    if destination == source_root or source_root in destination.parents:
        raise ValueError("Destination must be outside the source skills directory")
    plan = []
    for name in selected:
        source = available[name]
        source_files = snapshot(source)
        target = destination / name
        if is_link(target):
            if target.resolve() == source.resolve():
                plan.append(("SKIP", source, target))
                continue
            raise ValueError(f"Different link already exists; compare it first: {target}")
        if target.exists():
            if target.is_dir() and snapshot(target) == source_files:
                plan.append(("SKIP", source, target))
                continue
            raise ValueError(
                f"Different content already exists; back it up and move it aside "
                f"before installing: {target}"
            )
        plan.append((mode.upper(), source, target))
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--only", nargs="+", metavar="SKILL")
    selection.add_argument(
        "--profile", choices=("core", "all"),
        help="core: six engineering skills (default); all: every packaged skill",
    )
    parser.add_argument("--mode", choices=("copy", "link"), default="copy")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        plan = plan_install(args.dest, args.only, args.mode, args.profile)
        for action, source, target in plan:
            print(f"{action}: {target}")
            if args.dry_run or action == "SKIP":
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if action == "LINK":
                try:
                    os.symlink(source, target, target_is_directory=True)
                except OSError as exc:
                    raise ValueError(
                        f"Cannot create link at {target}; use --mode copy if links "
                        "are unavailable. Previously installed skills are left in place."
                    ) from exc
            else:
                shutil.copytree(source, target)
        print("Dry run; no files written." if args.dry_run else "Installation complete.")
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
