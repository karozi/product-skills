# Leak Experiment

Template for pirate-metrics-aarr Experiment mode. One bucket, one conversion, one
experiment. Fill every bracket.

## The leak

- **Leakiest bucket:** [bucket] — evidence: [conversion rate vs neighbors and range]
- **Failing conversion:** [from bucket A to bucket B], currently [X]%
- **Sequencing check passed:** [retention healthy enough / why this bucket is still
  first]

## The experiment

- **Intervention:** [one change to the failing conversion]
- **Bucket event affected:** [the specific event, per the map]
- **Expected movement:** from [X]% to [Y]% by [date]
- **Threshold (signed before launch):** [value that counts as a win]
- **Cost:** [spend / effort] · **Deadline:** [date]

## What waits its turn

- [Bucket]: [the tempting fix that waits, named so it stops tempting]

## After the experiment

1. Re-rank all five buckets with the new numbers.
2. Target the new leakiest bucket next — even if this experiment won.
3. Log the result in the innovation-accounting tuning ledger if one is running.

## Rules

- One bucket at a time. The other four wait.
- Thresholds are signed before launch and never renegotiated.
- A won experiment whose bucket is still the leakiest earns one follow-up; a second
  flat result moves to the next bucket or escalates.
