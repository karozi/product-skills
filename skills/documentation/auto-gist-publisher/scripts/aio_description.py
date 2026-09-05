#!/usr/bin/env python3
"""Deterministic AIO/GEO description rewriter.

Takes the raw `description:` from a SKILL.md and returns a plain-language,
keyword-rich summary suitable for a public gist header. No LLM calls — pure
text transforms so the same input always yields the same output (reproducible
across CI runs).

Transforms applied, in order:
1. Strip trigger-phrase clauses ("Use when the user says…", "Triggers: …",
   "Trigger with …") — those help the agent router but read as noise on a gist.
2. Strip parenthetical trigger lists.
3. Collapse whitespace.
4. Ensure the result ends with a period.
5. Cap at ~500 characters, cutting at the last sentence boundary that fits.
"""

from __future__ import annotations

import re


# Case-insensitive prefixes that mark a trigger-phrase clause. We drop the
# clause from that marker to the end of the sentence.
_TRIGGER_PREFIXES = (
    r"use when",
    r"triggers?[:\s]",
    r"trigger with",
    r"trigger phrases?",
    r"invoke with",
    r"invoked with",
    r"activate with",
    r"call with",
    r"load when",
)


def _split_sentences(text: str) -> list[str]:
    # Split on sentence terminators while keeping them attached.
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def _is_trigger_sentence(sentence: str) -> bool:
    lowered = sentence.lower()
    for prefix in _TRIGGER_PREFIXES:
        if re.match(prefix, lowered):
            return True
    return False


def _strip_trigger_parentheticals(text: str) -> str:
    # Remove parenthetical lists that are clearly trigger-phrase inventories.
    pattern = re.compile(
        r"\s*\((?:e\.g\.,?\s*)?['\"“”].{0,400}?['\"“”]\s*(?:,\s*['\"“”].{0,400}?['\"“”]\s*)*\)",
        re.DOTALL,
    )
    return pattern.sub("", text)


def rewrite_for_aio(raw_description: str, *, max_chars: int = 500) -> str:
    """Rewrite a raw SKILL.md description into an AIO/GEO-optimized summary.

    Never fabricates content — only removes trigger-router boilerplate and
    normalizes whitespace and punctuation.
    """
    if not raw_description or not raw_description.strip():
        raise ValueError("description is empty")

    text = _strip_trigger_parentheticals(raw_description)
    sentences = _split_sentences(text)
    kept = [s for s in sentences if not _is_trigger_sentence(s)]
    if not kept:
        # Fallback: keep original if every sentence was a trigger sentence.
        kept = sentences

    joined = " ".join(kept)
    joined = re.sub(r"\s+", " ", joined).strip()

    if not joined.endswith((".", "!", "?")):
        joined += "."

    if len(joined) <= max_chars:
        return joined

    # Cut at the last sentence boundary that fits.
    truncated = joined[:max_chars]
    last_period = max(truncated.rfind("."), truncated.rfind("!"), truncated.rfind("?"))
    if last_period >= max_chars // 2:
        return truncated[: last_period + 1].strip()
    # No clean boundary — cut at last space and add ellipsis.
    last_space = truncated.rfind(" ")
    cut = truncated[:last_space] if last_space > 0 else truncated
    return cut.rstrip(",;:") + "…"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("usage: aio_description.py '<raw description>'", file=sys.stderr)
        sys.exit(2)
    print(rewrite_for_aio(sys.argv[1]))
