#!/usr/bin/env python3
"""Validate every skill in a repository on push.

Adapted from anthropics/skills skill-creator scripts/quick_validate.py (MIT), extended
for repository-wide runs: two-folder-deep layout, name/folder agreement, body checks,
local reference integrity, and advisory linting of descriptions against the
skill-creator guidance in ../references/description-guidelines.md.

Dependency-free (no PyYAML): skills in this repository use scalar-only frontmatter.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
MAX_NAME_CHARS = 64
MAX_DESCRIPTION_CHARS = 1024
SOFT_DESCRIPTION_CHARS = 900
MIN_DESCRIPTION_CHARS = 40
MAX_BODY_LINES = 500
LOCAL_REF_PATTERN = re.compile(r"`((?:references|templates|scripts|assets|agents)/[A-Za-z0-9._\-/]+)`")
BOUNDARY_CUES = ("not for", "do not use", "don't use", "never use", "avoid when", "instead use")


def parse_frontmatter(text: str, source: Path) -> tuple[dict[str, str], str]:
    """Parse scalar-only YAML frontmatter. Returns (fields, body)."""
    if not text.startswith("---"):
        raise ValueError(f"{source}: no YAML frontmatter found")
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError(f"{source}: unterminated or invalid frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line[:1].isspace():
            raise ValueError(f"{source}: nested frontmatter values are not supported; keep scalars only")
        if ":" not in line:
            raise ValueError(f"{source}: unparseable frontmatter line: {line.strip()!r}")
        key, raw = line.split(":", 1)
        key = key.strip()
        raw = raw.strip()
        if not raw:
            raise ValueError(f"{source}: empty value for frontmatter key {key!r}")
        if raw[0] == '"':
            if len(raw) < 2 or raw[-1] != '"':
                raise ValueError(f"{source}: unterminated quoted value for {key!r}")
            try:
                fields[key] = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{source}: invalid quoted value for {key!r}: {exc}") from exc
        elif raw[0] == "'":
            if len(raw) < 2 or raw[-1] != "'":
                raise ValueError(f"{source}: unterminated quoted value for {key!r}")
            fields[key] = raw[1:-1].replace("''", "'")
        else:
            fields[key] = raw
        if not isinstance(fields[key], str):
            raise ValueError(f"{source}: {key!r} must be a string")
    if not fields:
        raise ValueError(f"{source}: frontmatter is empty")
    return fields, match.group(2)


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    """Validate one skill directory. Returns (errors, advisories)."""
    errors: list[str] = []
    advisories: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return ([f"SKILL.md not found in {skill_dir}"], [])

    text = skill_md.read_text(encoding="utf-8")
    try:
        frontmatter, body = parse_frontmatter(text, skill_md)
    except ValueError as exc:
        return ([str(exc)], [])

    unexpected = sorted(set(frontmatter) - ALLOWED_PROPERTIES)
    if unexpected:
        errors.append(
            f"unexpected frontmatter key(s): {', '.join(unexpected)}; "
            f"allowed: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()

    if not name:
        errors.append("missing required frontmatter key 'name'")
    else:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"name {name!r} must be kebab-case (lowercase letters, digits, single hyphens)")
        if len(name) > MAX_NAME_CHARS:
            errors.append(f"name is {len(name)} characters; maximum is {MAX_NAME_CHARS}")
        if name != skill_dir.name:
            errors.append(f"name {name!r} does not match folder name {skill_dir.name!r}")

    if not description:
        errors.append("missing required frontmatter key 'description'")
    else:
        if "<" in description or ">" in description:
            errors.append("description cannot contain angle brackets (< or >)")
        if len(description) > MAX_DESCRIPTION_CHARS:
            errors.append(f"description is {len(description)} characters; maximum is {MAX_DESCRIPTION_CHARS}")
        if len(description) < MIN_DESCRIPTION_CHARS:
            advisories.append(
                f"description is only {len(description)} characters; thin descriptions undertrigger "
                f"(aim for 100-200 words of trigger guidance)"
            )
        if len(description) > SOFT_DESCRIPTION_CHARS:
            advisories.append(
                f"description is {len(description)} characters; stay comfortably under "
                f"{MAX_DESCRIPTION_CHARS} by generalizing intent, not enumerating queries"
            )
        lowered = description.lower()
        if not re.search(r"\buse\b", lowered):
            advisories.append("description lacks imperative trigger phrasing ('Use when ...')")
        if not any(cue in lowered for cue in BOUNDARY_CUES):
            advisories.append(
                "description lacks a negative boundary ('Not for ...'); boundaries prevent false triggers"
            )

    compatibility = frontmatter.get("compatibility", "")
    if compatibility and len(compatibility) > 500:
        errors.append(f"compatibility is {len(compatibility)} characters; maximum is 500")

    body_lines = [line for line in body.splitlines()]
    if len(body_lines) > MAX_BODY_LINES:
        errors.append(f"SKILL.md body is {len(body_lines)} lines; maximum is {MAX_BODY_LINES}")
    if not re.search(r"(?m)^##\s+\S", body):
        errors.append("SKILL.md body has no '##' section headings")

    for ref in sorted(set(LOCAL_REF_PATTERN.findall(text))):
        if not (skill_dir / ref).exists():
            errors.append(f"references missing file: {ref}")

    return errors, advisories


def collect_skill_dirs(skills_root: Path) -> tuple[list[Path], list[str]]:
    """Find skill directories exactly two folders deep under skills/."""
    errors: list[str] = []
    all_skill_files = sorted(skills_root.rglob("SKILL.md"))
    expected = sorted(skills_root.glob("*/*/SKILL.md"))
    for skill_file in all_skill_files:
        if skill_file not in expected:
            errors.append(f"SKILL.md must be exactly two folders deep: {skill_file}")
    return [p.parent for p in expected], errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root (default: cwd)")
    parser.add_argument("--skill", type=Path, default=None, help="Validate a single skill directory")
    parser.add_argument("--strict", action="store_true", help="Treat advisories as failures")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output JSON only")
    args = parser.parse_args(argv)

    if args.skill:
        skill_dirs = [args.skill.resolve()]
        layout_errors: list[str] = []
    else:
        skills_root = args.repo_root.resolve() / "skills"
        if not skills_root.is_dir():
            print(f"error: {skills_root}: skills directory not found", file=sys.stderr)
            return 2
        skill_dirs, layout_errors = collect_skill_dirs(skills_root)

    results: list[dict] = []
    failed = warned = 0
    for layout_error in layout_errors:
        results.append({"skill": "(layout)", "errors": [layout_error], "advisories": []})
        failed += 1

    for skill_dir in sorted(skill_dirs):
        errors, advisories = validate_skill(skill_dir)
        rel = skill_dir.relative_to(args.repo_root.resolve()) if skill_dir.is_relative_to(args.repo_root.resolve()) else skill_dir
        results.append({"skill": str(rel), "errors": errors, "advisories": advisories})
        if errors:
            failed += 1
        if advisories:
            warned += 1

    exit_failures = failed + (warned if args.strict else 0)

    if args.as_json:
        print(json.dumps({"results": results, "failed": failed, "warned": warned}, indent=2))
        return 1 if exit_failures else 0

    for result in results:
        if result["errors"] or result["advisories"]:
            status = "FAIL" if result["errors"] else "WARN"
            print(f"{status} {result['skill']}")
            for error in result["errors"]:
                print(f"  error: {error}")
            for advisory in result["advisories"]:
                print(f"  warning: {advisory}")
        else:
            print(f"PASS {result['skill']}")

    print(f"\n{len(results)} skills: {len(results) - failed} passed, {failed} failed, {warned} with advisories.")
    if args.strict:
        print("Strict mode: advisories count as failures.")
    return 1 if exit_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
