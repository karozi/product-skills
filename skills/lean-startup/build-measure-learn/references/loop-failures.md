# Loop Failure Taxonomy

Reference for build-measure-learn Retro mode. Loops fail in known ways; naming the
failure mode is the retro's whole job.

## LEARNED (the loop worked — either way)

- **Confirmed:** the threshold was met. The belief survives with evidence.
- **Refuted:** the threshold was not met. The belief dies cheaply. This is a success —
  the loop's purpose was the answer, not the hoped-for answer.

Both close with the written "now we believe" sentence and spawn the next loop.

## INCONCLUSIVE (measurement failed, not the hypothesis)

Symptoms and causes:

- **No baseline existed** — the threshold had nothing to compare against.
  Cause: Plan mode skipped the baseline step. Fix: instrument first, then re-run.
- **Sample too small** — the result is inside the noise band. Cause: no sample-size
  thinking at planning. Fix: extend or widen the loop, with a number this time.
- **Contaminated signal** — two changes shipped inside one loop, or seasonality and
  press noise moved the metric. Cause: one-variable discipline broke. Fix: re-run
  with the variable isolated.
- **Wrong metric watched** — the threshold fired on a proxy that does not connect to
  the hypothesis. Cause: the metric was chosen after the build. Fix: re-derive the
  metric from the hypothesis (often the activation-event problem; see
  pirate-metrics-aarr).

An INCONCLUSIVE loop re-runs with fixed instrumentation. Two consecutive
INCONCLUSIVEs on the same hypothesis escalate: either the hypothesis is unmeasurable
in practice or the team cannot measure it yet — both are findings.

## WASTED (no learning either way)

Symptoms and causes:

- **No hypothesis was ever stated** — the loop was a build wearing a lab coat. This
  is the most expensive failure because it feels like work.
- **Built beyond the experiment** — features shipped that no measurement watched.
  Scope creep in loop clothing (see mvp-type-selector's Audit mode).
- **The result changed no decision** — the measurement came back, and the plan was
  identical either way. The experiment never needed to run.
- **Learning never written down** — the loop happened, the answer existed in the
  room, and six weeks later nobody remembers which way it pointed. Unwritten
  learning is learning that did not happen.

## Stall patterns (Track mode)

| Stall | Meaning | Cost |
|---|---|---|
| Built but unmeasured | instrumentation debt | learning delayed, decay risk |
| Measured but undecided | decision avoidance | the answer ages while opinions harden |
| Decided but unwritten | documentation debt | re-litigation guaranteed |
| Outlived timebox twice | zombie loop | attention budget drain |

## The one-sentence test

A loop can be closed honestly if it can answer: "We used to believe [X]; we measured
[Y]; we now believe [Z]." If any clause is missing, the retro names which Plan-mode
step was skipped — because that skip, not the result, is the failure.

Source: Eric Ries, The Lean Startup (2011), chapters 3–4 ("Learn," "Experiment"),
with the failure taxonomy adapted for this repository.
