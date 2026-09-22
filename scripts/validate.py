#!/usr/bin/env python3
"""Check this package's manifests, skills, and local Markdown references."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

from install import CORE_SKILLS

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    portable = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    compatibility = json.loads(
        (root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    for field in ("name", "version", "description"):
        if not portable.get(field) or portable[field] != compatibility.get(field):
            errors.append(f"Manifests differ or omit {field}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", portable.get("version", "")):
        errors.append("Version must use major.minor.patch")
    if compatibility.get("skills") != "./skills/":
        errors.append("Compatibility manifest must refer to ./skills/")

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found")
    packaged_names = {path.parent.name for path in skills}
    for name in CORE_SKILLS:
        if name not in packaged_names:
            errors.append(f"Core profile names a missing skill: {name}")
    if len(CORE_SKILLS) != len(set(CORE_SKILLS)):
        errors.append("Core profile contains duplicate names")
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            errors.append(f"Missing frontmatter: {path.relative_to(root)}")
            continue
        frontmatter = match.group(1)
        name = re.search(r"^name: ([a-z0-9-]+)$", frontmatter, re.MULTILINE)
        description = re.search(r'^description: "(.+)"$', frontmatter, re.MULTILINE)
        if not name or name.group(1) != path.parent.name:
            errors.append(f"Name differs from folder: {path.relative_to(root)}")
        if not description:
            errors.append(f"Missing one-line quoted description: {path.relative_to(root)}")
        if "[TODO:" in text:
            errors.append(f"Unfinished scaffold: {path.relative_to(root)}")
        ui = path.parent / "agents" / "openai.yaml"
        if not ui.is_file():
            errors.append(f"Missing UI metadata: {path.parent.name}")
        elif name and "$" + name.group(1) not in ui.read_text(encoding="utf-8"):
            errors.append(f"Default prompt does not name the skill: {path.parent.name}")

    # This checks file-backed references only, not network URLs or Markdown anchors.
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.relative_to(root).parts:
            continue
        text = path.read_text(encoding="utf-8")
        for href in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", href) or href.startswith("#"):
                continue
            target = (path.parent / unquote(href.split("#", 1)[0])).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                errors.append(f"Broken or external local reference: {path.relative_to(root)} -> {href}")
    return skills, errors


def main():
    try:
        skills, errors = validate()
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: 2 manifests, {len(skills)} skills, UI metadata, local references.")
    print("Structure only; workflow effectiveness requires real task evidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
