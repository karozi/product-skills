---
name: pirate-metrics-aarr
description: "Map any product onto the AARRR funnel — acquisition, activation, retention, referral, revenue — then hunt the leakiest bucket and write the single experiment that fixes it. Use when funnel performance is unclear, when growth is slow and the bottleneck is unknown, when metrics live in scattered dashboards, or when the user says pirate metrics, AARRR, funnel analysis, where are we losing users, leakiest bucket, or acquisition activation retention referral revenue. Not for choosing analytics tooling, running the experiments it designs, or offline sales pipelines without funnel data."
---

# Pirate Metrics (AARRR)

Users arrive, wake up, stay, invite, and pay — or leak at one of those five gates.
AARRR (Dave McClure's pirate metrics) names the gates so the leakiest one gets found
and fixed first. This skill maps the product onto all five, hunts the leak, and writes
exactly one experiment. Refuses to fix everything at once, because fixing everything
at once measures nothing.

## The Five Buckets

1. **Acquisition** — users arrive from a channel.
2. **Activation** — first experience delivers the "aha"; the key action happens.
3. **Retention** — they come back; the curve flattens instead of dying.
4. **Referral** — they bring others.
5. **Revenue** — they pay.

A bucket only counts its own event. Misfiled metrics (visits in activation, revenue
in acquisition) get moved — most funnels look worse than they are because their
buckets lie.

## Modes

### Map mode (default — user describes a product or pastes scattered metrics)

1. Read `references/bucket-metrics.md` first.
2. For each bucket, name the event that defines it for THIS product and the metric
   that measures it. The activation event must be the "aha" moment — the single
   action after which retention jumps — not a signup-completed proxy.
3. File every metric the user mentions into its true bucket; call out misfilings.
4. Mark UNKNOWN buckets honestly: an unmapped bucket is the map's most important
  finding, not an embarrassment.

### Leak-hunt mode (map exists, performance is the question)

1. Rank the buckets by conversion rate between them and against the bucket's
  reference range. The leak is the biggest drop, adjusted for how far upstream it
  sits — early leaks hide downstream damage.
2. Check the sequencing trap: referral and revenue numbers before retention is healthy
  are noise. A product that leaks retention will leak everything downstream.
3. Name the leakiest bucket and the specific conversion that fails. The verdict is one
  bucket, not "growth is broken."

### Experiment mode (leak named, fix needed)

1. Copy `templates/leak-experiment.md` and design ONE experiment on the leakiest
  bucket's conversion.
2. The experiment must move one metric between two named buckets, with a threshold
  signed before launch.
3. Declare what will NOT be touched: the other four buckets wait their turn.
4. After results: re-rank the buckets. The next experiment targets the new leakiest —
  even if the last one worked. Chasing the same bucket after it stopped being the
  leak is how growth teams build one strong wall and no roof.

## Hard Rules

- One experiment at a time, on the leakiest bucket only.
- Activation is defined by the retention-jump "aha" action, discovered from cohort
  data — not by whatever the onboarding flow happens to count.
- Referral metrics are meaningless before retention holds; revenue before activation
  is a pricing page measuring the wrong thing.
- Every bucket metric is per-cohort or rate-based. Cumulative anywhere is a
  vanity-metric-audit referral.
- If all five buckets are UNKNOWN, the first experiment is instrumentation — say so.

## Output Shape (Leak-hunt mode)

| Bucket | Event | Metric | Rate | vs range |
|---|---|---|---|---|

Followed by the leak verdict, the sequencing check, and the one experiment. Keep
output in the user's language.
