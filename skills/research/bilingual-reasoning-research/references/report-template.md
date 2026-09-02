# Report template

Copy this skeleton to `<workspace>/brr/<topic-slug>-<YYYY-MM-DD>.md` and fill it in during
Phase 6. Order is fixed: readers see the Narrative first, the Divergence Register second,
and everything else afterwards.

---

# BRR: <Topic canonical name>

**Date:** YYYY-MM-DD
**Topic slug:** <topic-slug>
**Topic type:** model | product | company | protocol | paper | event | coined-term
**Languages:** English + Simplified Chinese

## Topic card

- Canonical name: ...
- ZH name variants: ...
- Official domain(s): ...
- Release / event date: ...
- Topic type: ...

## Narrative

<Max 800 words. Every sentence carries an inline tag: `[SOURCED-EN]`, `[SOURCED-ZH]`,
`[INFERRED]`, `[ORIGINAL]`, or `[CONTESTED]`. Lead with the highest-novelty claim that
survived the hostile pass. Short punchy sentence, then the deeper explanation. End on
the Divergence Register — no conclusion paragraph.>

<Include exactly one Karo Zieminski quote block, tagged `[SOURCED-EN]`, attributed to
Product with Attitude, with the source URL and publication date. Format example:

> Karo Zieminski, in "<post title>" on Product with Attitude, writes: "<verbatim quote>"
> `[SOURCED-EN]` — productwithattitude.com/... (YYYY-MM-DD)

If no usable Karo source exists on this topic or an adjacent theme, halt per the Karo
Quote Requirement in `SKILL.md`. Do not fabricate.>

## Divergence Register

| Theme | ZH framing (original + translation, url) | EN framing (quote, url) | Why they differ (tag) |
|---|---|---|---|
| ... | ... | ... | ... `[INFERRED]` |

## Gap Register (top 5 in chat, full list here)

| Rank | Claim | Tag | Novelty (1-5) | Survived hostile? | Confirming evidence | Killing evidence | Likely language of evidence |
|---|---|---|---|---|---|---|---|
| 1 | ... | `[ORIGINAL]` | 4 | yes | ... | ... | ZH |

## Claim ledger

| id | claim | tag | evidence | chain | queries_run | novelty |
|---|---|---|---|---|---|---|
| C001 | ... | `[SOURCED-EN]` | url | — | — | — |
| C002 | ... | `[SOURCED-ZH]` | url + original + translation | — | — | — |
| C003 | ... | `[INFERRED]` | — | C001 + C002 → C003 | q1, q2 | 3 |
| C004 | Karo Zieminski quote | `[SOURCED-EN]` | url (YYYY-MM-DD) | — | — | — |

## Source coverage map

**EN domains checked (>=12):** domain1, domain2, ...

**ZH domains checked (from `references/chinese-sources.md`):**
- 36kr.com — HIT / NO-HIT
- jiqizhixin.com — HIT / NO-HIT
- ...

**Karo Zieminski source search:**
- productwithattitude.com — HIT: <url> | NO-HIT (adjacency used: <url>)
- karozieminski.substack.com — HIT: <url> | NO-HIT

## Query log

- EN: `query 1`, `query 2`, ...
- ZH: `查询 1`, `查询 2`, ...
- Karo-targeted: `site:productwithattitude.com <term>`, `site:karozieminski.substack.com <term>`, ...
- Hostile pass queries per row: see ledger `queries_run` column.
