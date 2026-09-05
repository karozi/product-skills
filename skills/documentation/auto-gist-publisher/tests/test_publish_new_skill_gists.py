import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import publish_new_skill_gists as pub  # noqa: E402


SAMPLE_FRONTMATTER = """---
name: {name}
description: "{description}"
---

# body
"""


def _write_skill(root: Path, category: str, slug: str, description: str) -> Path:
    d = root / "skills" / category / slug
    d.mkdir(parents=True, exist_ok=True)
    md = d / "SKILL.md"
    md.write_text(
        SAMPLE_FRONTMATTER.format(name=slug, description=description),
        encoding="utf-8",
    )
    return md


class DiscoveryTests(unittest.TestCase):
    def test_discovers_and_sorts_skills(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_skill(root, "research", "beta-skill", "Do research.")
            _write_skill(root, "documentation", "alpha-skill", "Document things.")
            skills = pub.discover_skills(root)
            keys = [s.key for s in skills]
            self.assertEqual(keys, ["documentation/alpha-skill", "research/beta-skill"])

    def test_missing_description_errors(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            d = root / "skills" / "x" / "y"
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text("---\nname: y\ndescription: \"\"\n---\n", encoding="utf-8")
            with self.assertRaises(pub.PublisherError):
                pub.discover_skills(root)


class GistBodyTests(unittest.TestCase):
    def _skill(self, category="lean-startup", slug="mvp-type-selector") -> pub.Skill:
        return pub.Skill(
            category=category,
            slug=slug,
            name=slug,
            description="Pick the cheapest MVP that tests your riskiest assumption. Use when the user says mvp.",
            display_name=pub._display_name(slug),
            skill_md_path=Path("/tmp/fake"),
        )

    def test_body_contains_all_required_pieces(self) -> None:
        body = pub.build_gist_body(self._skill(), rank=3, total=9)
        self.assertIn("Skill #3 of 9", body)
        self.assertIn("MVP Type Selector", body)
        self.assertIn("cheapest MVP", body)
        self.assertNotIn("Use when", body)
        self.assertIn("https://github.com/karozi/awesome-product-management-skills/tree/main/skills/lean-startup/mvp-type-selector", body)
        self.assertIn("https://karozieminski.substack.com/", body)

    def test_cta_carries_per_skill_utm(self) -> None:
        cta = pub.substack_cta("mvp-type-selector")
        self.assertIn("utm_source=github-gist", cta)
        self.assertIn("utm_medium=referral", cta)
        self.assertIn("utm_campaign=amps-skills", cta)
        self.assertIn("utm_content=mvp-type-selector", cta)
        body = pub.build_gist_body(self._skill(), rank=3, total=9)
        self.assertIn(pub.substack_cta("mvp-type-selector"), body)
        self.assertNotIn("??", body)

    def test_display_name_uppercases_specials(self) -> None:
        self.assertEqual(pub._display_name("mvp-type-selector"), "MVP Type Selector")
        self.assertEqual(pub._display_name("anti-mom-test"), "Anti Mom Test")
        self.assertEqual(pub._display_name("seo-audit"), "SEO Audit")

    def test_gist_description_format(self) -> None:
        desc = pub.build_gist_description(self._skill(), rank=5)
        self.assertTrue(desc.startswith("Skill #5:"))
        self.assertIn("MVP Type Selector", desc)


class StateAndDiffTests(unittest.TestCase):
    def test_state_roundtrip(self) -> None:
        with TemporaryDirectory() as td:
            path = Path(td) / "state.json"
            self.assertEqual(pub.load_state(path), {"schema": 1, "published": {}})
            pub.save_state(path, {"schema": 1, "published": {"a/b": {"gist_id": "x"}}})
            reloaded = pub.load_state(path)
            self.assertEqual(reloaded["published"]["a/b"]["gist_id"], "x")

    def test_dry_run_detects_new_skills_and_skips_known(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_skill(root, "documentation", "alpha", "Alpha capability.")
            _write_skill(root, "documentation", "beta", "Beta capability.")
            # Pre-seed state so alpha is already published.
            state_path = root / pub.STATE_REL_PATH
            state_path.parent.mkdir(parents=True)
            state_path.write_text(
                json.dumps(
                    {"schema": 1, "published": {"documentation/alpha": {"gist_id": "abc"}}}
                ),
                encoding="utf-8",
            )
            results = pub.run(root, write=False, dry_run=True)
            self.assertEqual(results["total"], 2)
            self.assertEqual(results["skipped"], 1)
            self.assertEqual(len(results["new"]), 1)
            self.assertEqual(results["new"][0]["skill"], "documentation/beta")
            self.assertEqual(results["new"][0]["rank"], 2)

    def test_ranks_are_alphabetical(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            _write_skill(root, "a", "one", "One.")
            _write_skill(root, "a", "two", "Two.")
            _write_skill(root, "b", "three", "Three.")
            results = pub.run(root, write=False, dry_run=True)
            ranks = {r["skill"]: r["rank"] for r in results["new"]}
            self.assertEqual(ranks, {"a/one": 1, "a/two": 2, "b/three": 3})


class FrontmatterParserTests(unittest.TestCase):
    def test_parses_quoted_description(self) -> None:
        text = '---\nname: foo\ndescription: "Line one. Use when: colon inside."\n---\nbody'
        fm = pub._parse_frontmatter(text, Path("/tmp/x"))
        self.assertEqual(fm["name"], "foo")
        self.assertEqual(fm["description"], "Line one. Use when: colon inside.")

    def test_missing_frontmatter_errors(self) -> None:
        with self.assertRaises(pub.PublisherError):
            pub._parse_frontmatter("no frontmatter here", Path("/tmp/x"))


if __name__ == "__main__":
    unittest.main()
