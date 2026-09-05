# Vanity Metric Taxonomy

Classification reference for vanity-metric-audit. Read fully before flagging metrics.

## Classification

- **ACTIONABLE** — passes all three tests (actionable, accessible, auditable) as presented.
- **VANITY** — cannot support a decision in any presentation; cumulative by nature.
- **MASKED** — an actionable underlying metric shown in a vanity form. Fix the
  presentation, keep the metric.

## Classic vanity metrics

| Metric | Why it lies | Cohort replacement |
|---|---|---|
| Total registered users | Goes up even if every new user churns | Weekly signups per cohort, with week-4 retention per cohort |
| Cumulative downloads / installs | Dead users still count | Installs per cohort + active installs (DAU/MAU by cohort) |
| Cumulative revenue since launch | Hides slowdown and churn | Monthly recurring revenue, net revenue retention per cohort |
| Total pageviews / sessions | Bots and bounces count too | Activation rate per acquisition channel |
| Follower / subscriber count (raw) | Audience is not engagement | Referral or reply rate per 1,000 followers |
| Press mentions / awards | Zero causal link to learning or revenue | Inbound signups attributed to coverage, per campaign |
| "X% growth" on a cumulative curve | Growth on a big base looks small; on a small base looks huge | Absolute and per-cohort rates side by side |
| Average revenue per user (blended) | Early high-value users mask later cohorts | ARPU per signup cohort |
| DAU as one number | No baseline, no cohort split | DAU split by cohort week; retention curve |
| NPS as one number | Aggregates contradicting segments | NPS per segment, tied to behavior |

## Detection patterns

- **Cumulative form**: any "total since launch" framing in a decision document.
- **No denominator**: counts without rates (signups vs signup conversion).
- **No split**: one number where cohort, segment, or channel differences decide.
- **Uncontrolled input**: metric moves from external noise (press, seasonality) as much
  as from team action.
- **Celebration framing**: metric appears in "wins" sections but never in decisions.
  If removing it would change no decision, it is vanity in that context.

## Masked-metric fixes

- Cumulative chart of an actionable metric → per-period cohort table.
- Blended average → per-cohort or per-segment breakdown.
- Raw count → rate with denominator stated.
- One-time spike left in the series → annotate and separate baseline from spike.

## Innovation accounting tie-in

Actionable metrics feed the three steps of innovation accounting: (1) establish the
baseline with an MVP, (2) tune toward the ideal, (3) decide pivot or persevere. A
dashboard that cannot support step 3 is reporting theater.

Source: Eric Ries, The Lean Startup (2011), chapters 7 ("Measure") and 10 ("Innovation
Accounting"). Format adapted for this repository.
