# Bucket Definitions and Standard Metrics

Reference for pirate-metrics-aarr Map and Leak-hunt modes.

## What belongs in each bucket

| Bucket | Belongs | Does NOT belong (common misfilings) |
|---|---|---|
| Acquisition | visits, signups, CAC, per-channel volume | activation events, revenue, pageviews from existing users |
| Activation | % completing the "aha" action in [N] days, time-to-aha | signup completion, any click count, first-session length as a raw number |
| Retention | week-N cohort retention, churn, curve flatten point | cumulative actives, "total users ever" |
| Referral | invites sent, acceptance rate, k-factor, share rate | press pickups, one-off shoutouts, paid referrals |
| Revenue | conversion to paid, ARPU per cohort, expansion, NRR | bookings without delivery, lifetime cumulative revenue |

## Defining the activation event

The "aha" moment is discovered, not declared:

1. Take retained users and look at what they did in their first week that churned
   users did not.
2. The action with the largest retention gap IS the activation event.
3. "Signed up" is never the activation event. Signing up is acquisition's last step.

If cohort data does not exist yet, mark activation UNKNOWN and instrument before
experimenting — a guessed activation event produces confident nonsense.

## Reference ranges (context, not targets)

Honest varies-by-product disclaimers apply; these set expectations for leak-hunting
only:

- Acquisition-to-activation: often the biggest leak; single-digit to low double-digit
  percentages are common for products that eventually work.
- Activation-to-week-1 retention: healthy products retain a meaningful fraction of
  activated users; retention dying to near zero signals an activation definition
  problem, not a retention problem.
- Referral participation: most products never exceed a minority of users inviting.
- Free-to-paid conversion: a few percent is common at scale; double digits usually
  means a strong wedge or a tiny, preselected audience.

## Sequencing rules

1. Retention before referral: you cannot virally spread a product people abandon.
2. Activation before revenue: monetizing an unactivated user measures the pricing
   page, not the product.
3. Acquisition before retention is questionable in both directions: if retention is
   broken, every acquisition dollar buys churn (see engine-of-growth — this is the
   paid-engine trap).

## The misfiling audit

When mapping, challenge every metric's bucket:

- "We have 40,000 users" — total since launch is a vanity metric, not a bucket.
- "Engagement is up" — which bucket's event, per cohort?
- "Conversion is 3%" — conversion from what to what, between which buckets?

A funnel with misfiled metrics underestimates exactly one bucket and gets optimized in
the wrong place. Fix the map before fixing the funnel.

Source: Dave McClure's "Startup Metrics for Pirates" (AARRR) as consolidated in lean
analytics practice (Alistair Croll and Benjamin Yoskovitz, Lean Analytics, 2013);
activation-event definition from the "aha moment" cohort method popularized by
Facebook's "7 friends in 10 days" pattern.
