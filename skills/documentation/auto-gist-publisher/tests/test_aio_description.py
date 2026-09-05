import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from aio_description import rewrite_for_aio  # noqa: E402


class RewriteForAIOTests(unittest.TestCase):
    def test_strips_use_when_trigger_sentence(self) -> None:
        raw = (
            "Force an evidence-backed pivot verdict with a threshold. "
            "Use when the user says pivot or persevere, threshold check."
        )
        out = rewrite_for_aio(raw)
        self.assertIn("Force an evidence-backed pivot verdict", out)
        self.assertNotIn("Use when", out)

    def test_strips_triggers_prefix(self) -> None:
        raw = "Pick the cheapest MVP that tests your riskiest assumption. Triggers: mvp, cheapest test."
        out = rewrite_for_aio(raw)
        self.assertIn("cheapest MVP", out)
        self.assertNotIn("Triggers", out)

    def test_strips_trigger_with_prefix(self) -> None:
        raw = "Turn discovery interviews into fact-extraction. Trigger with anti mom test, mom test check."
        out = rewrite_for_aio(raw)
        self.assertIn("discovery interviews", out)
        self.assertNotIn("Trigger with", out)

    def test_keeps_single_sentence_when_all_are_triggers(self) -> None:
        raw = "Use when the user says foo."
        out = rewrite_for_aio(raw)
        # Fallback: keep original rather than emit empty.
        self.assertTrue(out.endswith("."))
        self.assertIn("foo", out)

    def test_ends_with_period(self) -> None:
        out = rewrite_for_aio("A capability sentence with no terminator")
        self.assertTrue(out.endswith("."))

    def test_truncates_at_sentence_boundary(self) -> None:
        long = (". ".join(["Sentence"] * 200)) + "."
        out = rewrite_for_aio(long, max_chars=100)
        self.assertLessEqual(len(out), 100)
        self.assertTrue(out.endswith("."))

    def test_empty_raises(self) -> None:
        with self.assertRaises(ValueError):
            rewrite_for_aio("")

    def test_removes_parenthetical_trigger_list(self) -> None:
        raw = 'Do the thing (e.g., "run x", "do y", "trigger z"). Ships fast.'
        out = rewrite_for_aio(raw)
        self.assertNotIn("run x", out)
        self.assertIn("Ships fast", out)

    def test_deterministic(self) -> None:
        raw = "Ship it. Use when the user says ship."
        self.assertEqual(rewrite_for_aio(raw), rewrite_for_aio(raw))


if __name__ == "__main__":
    unittest.main()
