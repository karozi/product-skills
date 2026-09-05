---
name: pivot-or-persevere
description: "Force a written pivot-or-persevere verdict backed by cohort evidence instead of hope. Prepares the decision meeting, runs it against Ries's failure conditions, and blocks the let's-give-it-another-quarter flake without a falsifiable threshold. Use when deciding whether to keep going or change direction, before a strategy review, when a product is stuck in the trough of sorrow, or when the user says pivot or persevere, should we pivot, pivot decision, or time to kill this. Not for choosing which pivot type to execute (that is a separate catalog decision) or for performance reviews."
---

# Pivot or Persevere

The most expensive decision in a startup is usually not deciding. This skill turns the
pivot-or-persevere question into a scheduled, evidence-backed meeting with a written
verdict — and makes "give it another quarter" an explicit, threshold-bound commitment
instead of a flake.

## The Rule

Persevering in a direction with no validated learning is not grit; it is a slow-motion
pivot you have not admitted to yet. Conversely, pivoting in reaction to a single bad
week is panic dressed as decisiveness. The verdict must rest on cohort evidence over a
defined window — never on the last board meeting's mood.

## Modes

### Prep mode (user faces the decision but has not assembled evidence)

1. Read `references/pivot-decision-rules.md` before structuring anything.
2. Establish the evidence base: baseline metrics at start, cohort trend since, and the
   learning milestones actually completed. If the team cannot state its riskiest
   assumption and whether the last loop validated it, say so — that is the first
   finding, and it usually means the problem is measurement, not direction.
3. List the failure conditions from the reference and check each against the evidence.
4. Output the meeting agenda from `templates/pivot-or-persevere-meeting.md`, filled
   with the evidence available and marked UNKNOWN where evidence is missing.

### Run mode (user is in or about to enter the meeting)

1. Walk the agenda in order. Do not let the meeting skip the evidence section and jump
   to opinions — that jump is the failure mode this skill exists to prevent.
2. For each failure condition met: name it aloud and record it.
3. Permit only two verdicts plus one commitment: PERSEVERE, PIVOT, or PERSEVERE WITH
   THRESHOLD (a dated, measurable tripwire that forces the next decision).
4. Any PERSEVERE WITH THRESHOLD must specify: the metric, the threshold value, the
   review date, and what happens automatically when the tripwire fires. No threshold,
   no extension — the default third outcome is PIVOT.

### Verdict mode (user pastes a decision already made)

1. Classify it: PERSEVERE, PIVOT, or PERSEVERE WITH THRESHOLD.
2. Check it against the decision rules: which rules support it, which it violates.
3. If the rationale contains unmeasurable justifications ("momentum is building,"
   "we're really close," "the market isn't ready"), flag each as an unsupported claim
   and state what evidence would make it supported.
4. A PIVOT verdict gets a two-line handoff: the new hypothesis and its first cheap
   test (MVP type selector territory — do not design the test here).

## Hard Rules

- The verdict is written and signed before the meeting ends. Verbal verdicts do not
  count.
- "More time" without a falsifiable threshold is automatically classified as a flake
  and reported as such.
- Sunk cost is inadmissible evidence. Anything beginning "we've already invested" is
  struck from the record.
- Vanity metrics are inadmissible. If the evidence is cumulative-only, run the
  vanity-metric-audit first and say so.
- A pivot changes the hypothesis, not just the roadmap. Rebranding the same bet with
  new packaging is not a pivot; flag it.

## Output Shape (Verdict mode)

```
Verdict: [PERSEVERE / PIVOT / PERSEVERE WITH THRESHOLD]
Evidence: [cohort facts that drove it]
Rules checked: [supported / violated]
Threshold (if any): [metric] below/above [value] by [date] → [forced action]
Unsupported claims: [list or "none"]
Next loop: [hypothesis + first test, one line each]
```

Keep output in the user's language. Never soften a flake into a verdict.
