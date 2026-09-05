# Innovation Accounting Metrics Standards

Reference for innovation-accounting Setup, Report, and Decide modes.

## Admissible metrics

Per-cohort or rate-based only. The five buckets (defined in pirate-metrics-aarr):

| Bucket | Baseline metric | Ideal depends on |
|---|---|---|
| Acquisition | Conversion per channel | channel economics |
| Activation | % of cohort completing the key action in [N] days | the "aha" threshold |
| Retention | week-N retention per cohort (flatten point) | engine of growth type |
| Referral | invites or referrals per active user | viral cycle viability |
| Revenue | conversion to paid, per cohort | unit economics |

Unknown values are marked UNKNOWN. Never substitute an industry average for a
baseline: the baseline is what this product does, not what products like it do.

## Learning milestones

A learning milestone has four parts, all present:

1. **The experiment:** one intervention, describable in a sentence.
2. **The metric and its baseline:** the cohort number the experiment moves.
3. **The threshold:** the value that counts as learned.
4. **The decision enabled:** persevere, tune, or escalate to pivot-or-persevere.

Weak forms (rejected on sight):

- "Improve retention" — no threshold, no decision.
- "Ship the onboarding v2" — activity, not learning.
- "Validate demand" — which metric, from what baseline, past what value?

## Milestone sequencing

- Milestone 1 tests the riskiest assumption first (see mvp-type-selector for the
  vehicle).
- Later milestones test tunings, in the order of expected impact on the binding
  constraint.
- A milestone that requires another milestone's success to mean anything is a
  dependent milestone and gets sequenced explicitly, not assumed.

## The tuning ledger

Every tuning experiment is logged:

| Experiment | Metric | Baseline | Result | Learning |
|---|---|---|---|---|
| [change] | [metric] | [value] | [value] | [one falsifiable sentence] |

The Decide-mode evidence pack is this ledger plus the cohort trend. Nothing else
counts as evidence — no anecdotes, no averages, no cumulative charts.

## Failure patterns

- **Moving the best cohort** while the worst stays flat — tuning that cannot
  compound. Report the worst cohort trend.
- **Milestone inflation:** thresholds set low enough that everything passes. A
  threshold that cannot fail is decoration.
- **Orphan learnings:** experiments whose learnings never feed a decision. Each
  learning must land in a milestone or a decision, or the experiment was not run.

Source: Eric Ries, The Lean Startup (2011), chapter 10 ("Innovation Accounting"),
with metric standards adapted from cohort-analysis practice in Ash Maurya, Running
Lean (2012).
