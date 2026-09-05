---
name: vanity-metric-audit
description: "Separate actionable metrics from vanity metrics in any dashboard, metrics review, or investor update, then rebuild reporting around cohort behavior. Use when reviewing a dashboard or KPI slide, when numbers go up but decisions do not get easier, or when the user says vanity metric audit, vanity metrics check, are my metrics actionable, or rebuild my dashboard. Not for choosing analytics tools or implementing tracking."
---

# Vanity Metric Audit

Numbers that only go up are useless for decisions. This skill enforces Eric Ries's
actionable-metrics standard on any dashboard, metrics review, or update, and rebuilds
reporting around cohorts so the numbers can be argued with.

## The Three Tests

A metric earns its place on a dashboard only if it passes all three (The Lean Startup,
"Innovation Accounting"):

1. **Actionable** — it moves when the team's specific actions change it, and a change in
   it maps to a cause the team controls. Total signups fail: they go up no matter what.
2. **Accessible** — everyone in the room understands what it counts and who is counted.
   A metric nobody can explain is a metric nobody can act on.
3. **Auditable** — the number can be traced to real events. If the team distrusts the
   data, they will revert to their own opinions.

Anything that fails a test is a vanity metric: it flatters, it does not inform.

## Modes

### Audit mode (default — user pastes a dashboard, KPI list, or metrics update)

1. Read `references/vanity-metric-taxonomy.md` before classifying anything.
2. Number every metric in order.
3. Classify each: ACTIONABLE, VANITY, or MASKED (an actionable metric presented in a
   vanity form, such as retention shown as a cumulative chart — this one is fixable).
4. For each VANITY or MASKED metric: one-line why, the failure test it breaks, and the
   cohort-based replacement.
5. Score the dashboard: percentage of metrics that are actionable as presented. Verdict —
   "Decision-grade" (80%+), "Half blind" (50–79%), or "Flying blind" (below 50%).
6. End with the 3 metrics the dashboard is missing but the decision needs, and the single
   question the current dashboard cannot answer.

### Rebuild mode (user wants the replacement dashboard)

1. Confirm what decision the dashboard exists to serve; if none is stated, ask once —
   a dashboard without a decision attached is decoration by definition.
2. Copy `templates/cohort-dashboard.md` and fill every bracket.
3. Every metric must be per-cohort, per-segment, or rate-based. No cumulative totals.
4. Include the baseline, the current value, and the threshold that triggers a
   pivot-or-persevere conversation.

## Hard Rules

- Cumulative anything (total users, total downloads, total revenue since launch) is
  vanity in a decision context. Always.
- Growth percentage on a cumulative curve is vanity with extra steps.
- Averages hide cohorts; distributions decide.
- Never delete the raw numbers — downgrade them to context. The audit changes what
  drives decisions, not what gets stored.

## Output Shape (Audit mode)

| # | Metric | Class | Fails test | Replacement |
|---|--------|-------|-----------|-------------|

Followed by the score, verdict, missing metrics, and the one unanswerable question.
Keep output in the user's language. Never reclassify a metric as ACTIONABLE without
naming the decision it drives and the action that would move it.
