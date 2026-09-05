---
name: innovation-accounting
description: "Turn startup progress into accountable numbers with Ries's innovation accounting: establish a baseline MVP, tune cohorts toward the ideal, and make pivot-or-persevere decisions on evidence. Use when reporting progress on an unproven product, when 'we're learning a lot' needs to become a measurable statement, for investor or stakeholder updates on early-stage work, or when the user says innovation accounting, learning milestones, baseline metrics, or how do we measure progress before product-market fit. Not for products with established standard metrics like ARR or for vanity-metric cleanup (that is vanity-metric-audit)."
---

# Innovation Accounting

"We're making progress" is not a report. Innovation accounting makes early-stage
progress measurable in three steps: establish the baseline, tune toward the ideal, and
decide pivot or persevere. This skill runs all three — and refuses to let a learning
claim survive without a number attached.

## The Three Steps

1. **Baseline.** Run an MVP, measure where the engine stands today: conversion,
   retention, churn — per cohort, worst-case honest.
2. **Tune.** Iterate to move the baseline toward the ideal one experiment at a time.
   Each iteration must move a named metric or it did not happen.
3. **Decide.** When tuning stops working, the pivot-or-persevere meeting gets the
   cohort evidence. Not before, not on mood.

## Modes

### Setup mode (default — new initiative or first time measuring)

1. Establish the baseline: for the current product or MVP, list per-cohort values for
   acquisition, activation, retention, referral, and revenue (see pirate-metrics-aarr
   for bucket definitions). Where a number is unknown, mark UNKNOWN — unknown baselines
   are findings, not gaps to fill with averages.
2. Name the ideal: what each metric must reach for the engine to sustain the business.
   If the ideal cannot be stated, the hypothesis is not ready for accounting.
3. Copy `templates/learning-milestone-report.md` and define the first 3 learning
   milestones.

### Report mode (user pastes progress claims or an update draft)

1. Read `references/metrics-standards.md` first.
2. Number every claim of progress. Classify each: MILESTONE (a named metric moved by a
   named experiment), INPROGRESS (experiment running, result pending, with a date), or
   NOISE (activity without a metric attached — meetings held, features shipped that no
   metric watched).
3. Report the learning-to-activity ratio. Verdict — "Accountable" (80%+ of claims are
   milestones), "Half-accountable" (50–79%), or "Activity theater" (below 50%).
4. Convert each NOISE claim into the milestone it should have been.

### Decide mode (measurement window closed)

1. Assemble: baseline, each tuning experiment and its metric movement, current cohort
   trend.
2. Apply the rule: improvement across successive cohorts → continue tuning. Flat
   cohorts after real tuning → hand off to pivot-or-persevere with the evidence pack.
3. Output the evidence pack, not a recommendation to "keep pushing."

## Hard Rules

- A learning milestone is falsifiable and metric-bound: "If [experiment], [metric]
  will move from [baseline] past [threshold] by [date]."
- Every milestone names the decision it enables. A milestone that changes no decision
  is a hobby.
- Cumulative metrics are inadmissible at every step — route through vanity-metric-audit
  if they appear.
- The baseline is the worst honest number, not the best cohort. Tuning gets credit for
  moving the worst, not the best.

## Output Shape (Report mode)

| # | Claim | Class | Metric moved | Should have been |
|---|-------|-------|--------------|------------------|

Followed by the ratio, verdict, and rewritten milestones. Keep output in the user's
language. Never accept a learning claim whose metric is missing.
