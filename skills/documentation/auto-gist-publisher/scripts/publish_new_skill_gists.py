#!/usr/bin/env python3
"""Publish a public gist for every new skill added to the repo.

Idempotent: consults `state/published.json` to decide what is new. Header-only
gist body linking back to the skill folder on GitHub. Requires `gh` CLI with
gist scope.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

# Allow importing aio_description when run from repo root or from this dir.
_SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPT_DIR))
from aio_description import rewrite_for_aio  # noqa: E402


REPO_SLUG = "karozi/awesome-product-management-skills"
REPO_TREE_BASE = f"https://github.com/{REPO_SLUG}/tree/main"
SUBSTACK_CTA = "See more AI PM resources at https://karozieminski.substack.com/"
STATE_REL_PATH = "skills/documentation/auto-gist-publisher/state/published.json"


class PublisherError(RuntimeError):
    """Raised when the publisher cannot proceed safely."""


@dataclass(frozen=True)
class Skill:
    category: str
    slug: str
    name: str
    description: str
    display_name: str
    skill_md_path: Path

    @property
    def key(self) -> str:
        return f"{self.category}/{self.slug}"

    @property
    def repo_url(self) -> str:
        return f"{REPO_TREE_BASE}/skills/{self.category}/{self.slug}"


# ---------- Frontmatter parsing (minimal, matches sync-skills-readme style) ----------

def _parse_frontmatter(text: str, source: Path) -> dict:
    if not text.startswith("---"):
        raise PublisherError(f"{source}: missing YAML frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise PublisherError(f"{source}: unterminated frontmatter")
    block = text[3:end].strip("\n")
    data: dict = {}
    current_key: str | None = None
    buffer: list[str] = []
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        # Very small parser: only supports top-level `key: value` scalars,
        # which is all we need (name, description). Nested keys (metadata:)
        # are ignored.
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if m and not line.startswith(" "):
            if current_key is not None:
                data[current_key] = "\n".join(buffer).strip()
            current_key = m.group(1)
            value = m.group(2).strip()
            buffer = [value] if value else []
        else:
            if current_key is not None:
                buffer.append(line.strip())
    if current_key is not None:
        data[current_key] = "\n".join(buffer).strip()

    # Unquote description if double-quoted.
    for key in ("name", "description"):
        v = data.get(key, "")
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            try:
                data[key] = json.loads(v)
            except json.JSONDecodeError:
                data[key] = v[1:-1]
    return data


def _display_name(slug: str) -> str:
    words = slug.replace("_", "-").split("-")
    special = {"ai", "api", "ci", "cd", "mcp", "llm", "ml", "seo", "aio", "geo", "pm", "qa", "ui", "ux", "mvp"}
    out = []
    for w in words:
        out.append(w.upper() if w.lower() in special else w.capitalize())
    return " ".join(out)


# ---------- Skill discovery ----------

def discover_skills(repo_root: Path) -> list[Skill]:
    skills_root = repo_root / "skills"
    if not skills_root.is_dir():
        raise PublisherError(f"skills directory not found: {skills_root}")
    found: list[Skill] = []
    for skill_md in sorted(skills_root.glob("*/*/SKILL.md")):
        rel = skill_md.relative_to(skills_root)
        category, slug = rel.parts[0], rel.parts[1]
        text = skill_md.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text, skill_md)
        name = fm.get("name") or slug
        description = fm.get("description", "").strip()
        if not description:
            raise PublisherError(f"{skill_md}: missing description")
        found.append(
            Skill(
                category=category,
                slug=slug,
                name=name,
                description=description,
                display_name=_display_name(slug),
                skill_md_path=skill_md,
            )
        )
    return found


# ---------- State ----------

def load_state(state_path: Path) -> dict:
    if not state_path.exists():
        return {"schema": 1, "published": {}}
    data = json.loads(state_path.read_text(encoding="utf-8"))
    data.setdefault("schema", 1)
    data.setdefault("published", {})
    return data


def save_state(state_path: Path, state: dict) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def sha256_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------- Gist formatting ----------

def build_gist_body(skill: Skill, rank: int, total: int) -> str:
    aio = rewrite_for_aio(skill.description)
    return (
        f"# Skill #{rank} of {total} in awesome-product-management-skills\n\n"
        f"## {skill.display_name}\n\n"
        f"{aio}\n\n"
        f"Read the full skill: {skill.repo_url}\n\n"
        f"---\n\n"
        f"{SUBSTACK_CTA}\n"
    )


def build_gist_description(skill: Skill, rank: int) -> str:
    return f"Skill #{rank}: {skill.display_name} — awesome-product-management-skills"


# ---------- gh gist create ----------

def create_gist(body: str, filename: str, description: str, *, dry_run: bool) -> tuple[str, str]:
    """Return (gist_url, gist_id). In dry-run, return placeholders."""
    if dry_run:
        return ("https://gist.github.com/DRY-RUN", "DRY-RUN")
    # Write to a temp file so gh uses the correct filename.
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        fpath = Path(td) / filename
        fpath.write_text(body, encoding="utf-8")
        proc = subprocess.run(
            ["gh", "gist", "create", "--public", "--desc", description, str(fpath)],
            capture_output=True,
            text=True,
            check=False,
        )
    if proc.returncode != 0:
        raise PublisherError(f"gh gist create failed: {proc.stderr.strip()}")
    url = proc.stdout.strip().splitlines()[-1].strip()
    if not url.startswith("https://gist.github.com/"):
        raise PublisherError(f"unexpected gh output: {proc.stdout!r}")
    gist_id = url.rstrip("/").split("/")[-1]
    return (url, gist_id)


# ---------- Main ----------

def run(repo_root: Path, *, write: bool, dry_run: bool) -> dict:
    state_path = repo_root / STATE_REL_PATH
    state = load_state(state_path)

    skills = discover_skills(repo_root)
    total = len(skills)
    # Alphabetical rank (by category/slug) — stable, matches how they render.
    ranked = {s.key: i + 1 for i, s in enumerate(skills)}

    new_skills = [s for s in skills if s.key not in state["published"]]
    results = {"total": total, "new": [], "skipped": len(skills) - len(new_skills)}

    for skill in new_skills:
        rank = ranked[skill.key]
        body = build_gist_body(skill, rank=rank, total=total)
        desc = build_gist_description(skill, rank=rank)
        filename = f"{skill.slug}.md"
        try:
            url, gist_id = create_gist(body, filename, desc, dry_run=dry_run or not write)
        except PublisherError as exc:
            results.setdefault("errors", []).append({"skill": skill.key, "error": str(exc)})
            continue

        state["published"][skill.key] = {
            "gist_id": gist_id,
            "gist_url": url,
            "published_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sha256": sha256_of(body),
            "rank_at_publish": rank,
            "total_at_publish": total,
        }
        results["new"].append({"skill": skill.key, "url": url, "rank": rank})

    if write and not dry_run and results["new"]:
        save_state(state_path, state)

    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root", type=Path, default=Path.cwd())
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("--write", action="store_true", help="publish new gists and update state")
    grp.add_argument("--dry-run", action="store_true", help="preview only, do not call gh")
    args = ap.parse_args(argv)

    if not args.write and not args.dry_run:
        args.dry_run = True  # default to safe

    try:
        results = run(args.repo_root.resolve(), write=args.write, dry_run=args.dry_run)
    except PublisherError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(results, indent=2))
    return 0 if not results.get("errors") else 1


if __name__ == "__main__":
    raise SystemExit(main())
