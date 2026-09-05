import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"

VALID_SKILL_MD = """---
name: demo-skill
description: "Do a thing well. Use when the user mentions doing the thing, thing-doing, or wants their thing done. Not for undoing things."
---

# Demo Skill

## Modes

### Run mode

1. Do the thing.
"""


def write_skill(root: Path, name: str = "demo-skill", skill_md: str | None = None) -> Path:
    skill_dir = root / "skills" / "demo" / name
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(skill_md if skill_md is not None else VALID_SKILL_MD, encoding="utf-8")
    return skill_dir


def run_validator(repo_root: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(repo_root), "--json", *extra],
        capture_output=True,
        text=True,
        check=False,
    )


class ValidateSkillsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)

    def payload(self, completed: subprocess.CompletedProcess) -> dict:
        return json.loads(completed.stdout)

    def test_valid_skill_passes(self):
        write_skill(self.root)
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 0, completed.stdout)
        payload = self.payload(completed)
        self.assertEqual(payload["failed"], 0)
        self.assertEqual(payload["results"][0]["errors"], [])
        self.assertEqual(payload["results"][0]["advisories"], [])

    def test_name_folder_mismatch_fails(self):
        write_skill(self.root, name="other-name")
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 1)
        errors = self.payload(completed)["results"][0]["errors"]
        self.assertTrue(any("does not match folder" in error for error in errors))

    def test_missing_description_fails(self):
        write_skill(self.root, skill_md=VALID_SKILL_MD.replace(
            'description: "Do a thing well. Use when the user mentions doing the thing, thing-doing, or wants their thing done. Not for undoing things."',
            "",
        ))
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 1)
        errors = self.payload(completed)["results"][0]["errors"]
        self.assertTrue(any("description" in error for error in errors))

    def test_overlong_description_fails(self):
        long_description = "x" * 1025
        write_skill(self.root, skill_md=VALID_SKILL_MD.replace(
            "Do a thing well. Use when the user mentions doing the thing, thing-doing, or wants their thing done. Not for undoing things.",
            long_description,
        ))
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 1)
        errors = self.payload(completed)["results"][0]["errors"]
        self.assertTrue(any("1024" in error for error in errors))

    def test_thin_description_is_advisory_not_error(self):
        write_skill(self.root, skill_md=VALID_SKILL_MD.replace(
            "Do a thing well. Use when the user mentions doing the thing, thing-doing, or wants their thing done. Not for undoing things.",
            "Do stuff. Use when told. Not for that.",
        ))
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 0)
        payload = self.payload(completed)
        self.assertEqual(payload["failed"], 0)
        self.assertEqual(payload["warned"], 1)
        advisories = payload["results"][0]["advisories"]
        self.assertTrue(any("thin" in advisory for advisory in advisories))

    def test_strict_mode_fails_on_advisories(self):
        write_skill(self.root, skill_md=VALID_SKILL_MD.replace(
            "Do a thing well. Use when the user mentions doing the thing, thing-doing, or wants their thing done. Not for undoing things.",
            "Do stuff. Use when told. Not for that.",
        ))
        completed = run_validator(self.root, "--strict")
        self.assertEqual(completed.returncode, 1)

    def test_dead_reference_fails(self):
        write_skill(self.root, skill_md=VALID_SKILL_MD + "\nRead `references/missing.md` first.\n")
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 1)
        errors = self.payload(completed)["results"][0]["errors"]
        self.assertTrue(any("missing file" in error for error in errors))

    def test_wrong_depth_fails(self):
        deep = self.root / "skills" / "a" / "b" / "c"
        deep.mkdir(parents=True)
        (deep / "SKILL.md").write_text(VALID_SKILL_MD, encoding="utf-8")
        completed = run_validator(self.root)
        self.assertEqual(completed.returncode, 1)
        errors = self.payload(completed)["results"][0]["errors"]
        self.assertTrue(any("two folders deep" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
