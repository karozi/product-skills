---
name: pivot-catalog
description: "Match pivot symptoms to the right pivot type from Ries's ten-pivot catalog and draft the new hypothesis with its first cheap test. Use after a pivot-or-persevere verdict lands on PIVOT, when a startup or product is changing direction and needs to name the change, when growth stalls and someone says 'maybe we should pivot', or when the user says pivot catalog, which pivot, what kind of pivot, or pivot types. Not for deciding whether to pivot (that is pivot-or-persevere) or for roadmap reorganization without a hypothesis change."
---

# Pivot Catalog

A pivot without a name is a drift. This skill matches the evidence that forced the
decision to one of Ries's ten pivot types, then drafts the new hypothesis, what
learning survives the change, and the first cheap test of the new direction. Run it
the moment pivot-or-persevere returns PIVOT.

## The Rule

A pivot changes the strategy hypothesis while preserving everything validated so far.
If nothing validated survives, it is a new company, not a pivot. If the hypothesis does
not change, it is a roadmap, not a pivot. Both findings get reported.

## Modes

### Diagnose mode (default — user describes symptoms or a decision to change direction)

1. Read `references/pivot-types.md` before naming anything.
2. Extract the evidence: what was the old hypothesis, what did the cohorts say, what
   remains true regardless of direction.
3. Match symptoms to exactly one primary pivot type. Name it. If two types fit, name
   the primary and list the secondary as an explicit rider — never blend them into a
   vague "strategic shift."
4. State what validated learning carries forward and what gets thrown out. A pivot
   that preserves nothing is flagged as a restart.

### Draft mode (user knows the pivot type or Diagnose has named it)

1. Confirm the pivot type exists in the reference. If the user invented a type,
   decompose it into the catalog types it combines and say so.
2. Copy `templates/pivot-brief.md` and fill every bracket: old hypothesis, triggering
   evidence, pivot type, new hypothesis, preserved learning, and the first cheap test.
3. The first test must be a minimum-viable experiment, not a rebuild: recommend the
   MVP type using the mvp-type-selector catalog (landing page, concierge, Wizard of
   Oz, piecemeal, single-feature, explainer video).
4. Include the kill condition for the new direction — signed before the test runs.

## Hard Rules

- Every pivot gets named with a catalog type. "We're evolving" is not a pivot type.
- The new hypothesis must be falsifiable in one sentence.
- The first post-pivot test must be cheaper and faster than the original product's
  build. A pivot that starts with "first, we rebuild the platform" is a relapse.
- Preserved learning is listed explicitly — it is the pivot's only asset.
- One pivot at a time. Two simultaneous pivots produce evidence nobody can attribute.

## Output Shape (Diagnose mode)

```
Old hypothesis: [one sentence]
Triggering evidence: [cohort facts]
Pivot type: [name] — [one-line why this type]
Rider (if any): [secondary type]
Preserved learning: [list]
Discarded: [list]
New hypothesis: [one falsifiable sentence]
First test: [MVP type + one-line design]
```

Keep output in the user's language. Never recommend a pivot type without naming what
it preserves and what it discards.
