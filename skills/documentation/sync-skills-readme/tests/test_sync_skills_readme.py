from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import sync_skills_readme as catalog  # noqa: E402


class SyncSkillsReadmeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary_directory.name)
        (self.repo / "README.md").write_text(
            "# Example\n\nIntro written by a human.\n\n## Skills\n\nOld catalog.\n\n## Notes\n\nKeep me.\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def add_skill(
        self,
        category: str,
        name: str,
        display_name: str | None = None,
        short_description: str | None = None,
    ) -> None:
        skill_directory = self.repo / "skills" / category / name
        (skill_directory / "agents").mkdir(parents=True)
        (skill_directory / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Fallback description for {name}.\n---\n\n"
            f"# {name.replace('-', ' ').title()}\n",
            encoding="utf-8",
        )
        if display_name or short_description:
            (skill_directory / "agents" / "openai.yaml").write_text(
                "interface:\n"
                f'  display_name: "{display_name or name}"\n'
                f'  short_description: "{short_description or "Fallback summary"}"\n',
                encoding="utf-8",
            )

    def test_collects_metadata_and_sorts_categories_and_skills(self) -> None:
        self.add_skill("product-thinking", "zeta-skill", "Zeta Skill", "Handle zeta work")
        self.add_skill("documentation", "alpha-skill", "Alpha Skill", "Handle alpha work")
        self.add_skill("documentation", "beta-skill", "Beta Skill", "Handle beta work")

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertLess(rendered.index("### Documentation"), rendered.index("### Product thinking"))
        self.assertLess(rendered.index("Alpha Skill"), rendered.index("Beta Skill"))
        self.assertIn("— Handle alpha work.", rendered)

    def test_preserves_known_acronyms_in_category_headings(self) -> None:
        self.add_skill("ai-product", "alpha-skill", "Alpha Skill", "Handle alpha work")

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertIn("### AI product", rendered)

    def test_first_sync_migrates_skills_section_and_preserves_other_content(self) -> None:
        self.add_skill("documentation", "alpha-skill", "Alpha Skill", "Handle alpha work")

        self.assertEqual(catalog.sync(self.repo, write=True), 0)
        updated = (self.repo / "README.md").read_text(encoding="utf-8")

        self.assertIn(catalog.START_MARKER, updated)
        self.assertIn(catalog.END_MARKER, updated)
        self.assertNotIn("Old catalog.", updated)
        self.assertIn("Intro written by a human.", updated)
        self.assertIn("## Notes\n\nKeep me.", updated)

    def test_second_sync_is_idempotent_and_check_passes(self) -> None:
        self.add_skill("documentation", "alpha-skill", "Alpha Skill", "Handle alpha work")
        catalog.sync(self.repo, write=True)
        first = (self.repo / "README.md").read_text(encoding="utf-8")

        self.assertEqual(catalog.sync(self.repo), 0)
        self.assertEqual(first, (self.repo / "README.md").read_text(encoding="utf-8"))

    def test_check_reports_stale_without_writing(self) -> None:
        self.add_skill("documentation", "alpha-skill", "Alpha Skill", "Handle alpha work")
        original = (self.repo / "README.md").read_text(encoding="utf-8")

        self.assertEqual(catalog.sync(self.repo), 1)
        self.assertEqual(original, (self.repo / "README.md").read_text(encoding="utf-8"))

    def test_rejects_folder_and_skill_name_mismatch(self) -> None:
        self.add_skill("documentation", "alpha-skill")
        skill_file = self.repo / "skills" / "documentation" / "alpha-skill" / "SKILL.md"
        skill_file.write_text(
            skill_file.read_text(encoding="utf-8").replace("name: alpha-skill", "name: wrong-name"),
            encoding="utf-8",
        )

        with self.assertRaises(catalog.CatalogError):
            catalog.collect_skills(self.repo)

    def test_malformed_quoted_frontmatter_returns_metadata_error(self) -> None:
        self.add_skill("documentation", "alpha-skill")
        skill_file = self.repo / "skills" / "documentation" / "alpha-skill" / "SKILL.md"
        skill_file.write_text(
            "---\nname: alpha-skill\ndescription: \"unterminated\n---\n",
            encoding="utf-8",
        )

        self.assertEqual(catalog.main(["--repo-root", str(self.repo), "--check"]), 2)

    def test_rejects_unexpected_skill_depth(self) -> None:
        self.add_skill("documentation", "alpha-skill")
        unexpected = self.repo / "skills" / "documentation" / "nested" / "extra-skill"
        unexpected.mkdir(parents=True)
        (unexpected / "SKILL.md").write_text(
            "---\nname: extra-skill\ndescription: Too deep.\n---\n",
            encoding="utf-8",
        )

        with self.assertRaises(catalog.CatalogError):
            catalog.collect_skills(self.repo)

    def test_escapes_markdown_in_catalog_text(self) -> None:
        self.add_skill(
            "documentation",
            "alpha-skill",
            "Alpha [Safe] Skill",
            "Handle [safe] work",
        )

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertIn(r"[Alpha \[Safe\] Skill]", rendered)
        self.assertIn(r"Handle \[safe\] work.", rendered)

    def test_rejects_unbalanced_markers(self) -> None:
        with self.assertRaises(catalog.CatalogError):
            catalog.update_readme(
                f"# Example\n\n## Skills\n\n{catalog.START_MARKER}\n",
                "### Documentation",
            )

    def test_rejects_reversed_markers(self) -> None:
        with self.assertRaises(catalog.CatalogError):
            catalog.update_readme(
                f"# Example\n\n## Skills\n\n{catalog.END_MARKER}\n{catalog.START_MARKER}\n",
                "### Documentation",
            )

    def test_preserves_crlf_and_utf8_bom(self) -> None:
        self.add_skill("documentation", "alpha-skill", "Alpha Skill", "Handle alpha work")
        readme = self.repo / "README.md"
        original = readme.read_text(encoding="utf-8").replace("\n", "\r\n")
        readme.write_bytes(b"\xef\xbb\xbf" + original.encode("utf-8"))

        self.assertEqual(catalog.sync(self.repo, write=True), 0)
        updated = readme.read_bytes()

        self.assertTrue(updated.startswith(b"\xef\xbb\xbf"))
        self.assertNotIn(b"\n", updated.replace(b"\r\n", b""))


class GistBadgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary_directory.name)
        (self.repo / "README.md").write_text(
            "# Example\n\n## Skills\n\nOld catalog.\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _add_skill(self, category: str, name: str) -> None:
        skill_directory = self.repo / "skills" / category / name
        skill_directory.mkdir(parents=True)
        (skill_directory / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Fallback description for {name}.\n---\n\n"
            f"# {name.replace('-', ' ').title()}\n",
            encoding="utf-8",
        )

    def _write_state(self, published: dict) -> None:
        state_path = self.repo / catalog.GIST_STATE_REL_PATH
        state_path.parent.mkdir(parents=True)
        state_path.write_text(
            '{"schema": 1, "published": ' + json.dumps(published) + "}",
            encoding="utf-8",
        )

    def test_badge_rendered_for_published_skill(self) -> None:
        self._add_skill("lean-startup", "mvp-type-selector")
        self._write_state(
            {
                "lean-startup/mvp-type-selector": {
                    "gist_id": "abc123",
                    "gist_url": "https://gist.github.com/karozi/abc123",
                }
            }
        )

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertIn("[gist ↗](https://gist.github.com/karozi/abc123)", rendered)

    def test_no_badge_when_state_missing(self) -> None:
        self._add_skill("lean-startup", "mvp-type-selector")

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertNotIn("gist", rendered)

    def test_no_badge_for_unpublished_skill(self) -> None:
        self._add_skill("lean-startup", "mvp-type-selector")
        self._add_skill("lean-startup", "other-skill")
        self._write_state(
            {
                "lean-startup/other-skill": {
                    "gist_url": "https://gist.github.com/karozi/xyz",
                }
            }
        )

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertIn("[gist ↗](https://gist.github.com/karozi/xyz)", rendered)
        mvp_line = next(line for line in rendered.splitlines() if "mvp" in line.lower())
        self.assertNotIn("gist", mvp_line)

    def test_malformed_state_raises(self) -> None:
        self._add_skill("lean-startup", "mvp-type-selector")
        state_path = self.repo / catalog.GIST_STATE_REL_PATH
        state_path.parent.mkdir(parents=True)
        state_path.write_text("{not json", encoding="utf-8")

        with self.assertRaises(catalog.CatalogError):
            catalog.collect_skills(self.repo)

    def test_non_gist_urls_are_ignored(self) -> None:
        self._add_skill("lean-startup", "mvp-type-selector")
        self._write_state(
            {"lean-startup/mvp-type-selector": {"gist_url": "https://example.com/nope"}}
        )

        rendered = catalog.render_catalog(catalog.collect_skills(self.repo))

        self.assertNotIn("gist ↗", rendered)


if __name__ == "__main__":
    unittest.main()
