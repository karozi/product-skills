# Slice Plan

Template for small-batches Re-slice mode. Every slice ships, learns, and merges at
its own boundary. Fill every bracket.

## The work being re-sliced

- **Initiative:** [name]
- **Current batch:** [time from first work started to first user learning: value or
  "nothing ships until the end"]
- **Audit verdict that triggered this:** [Slicing well / Batching up / Batch
  pathology]

## Slice axis

[The thinnest vertical path: one user, one job, end to end. Not a horizontal layer.]

## Slices

### Slice 1 (riskiest learning first)

- **Ships:** [what a real user can do after this slice]
- **Learns:** [the measurable behavior change or question answered — run as a
  build-measure-learn loop]
- **Contains:** [one-line scope]
- **Deliberately excludes:** [the cut list]
- **Merges:** [integration checkpoint — continuous, at slice end]

### Slice 2 · Slice 3 · ...

[Same four fields each, sequenced by learning value.]

## Release checkpoints

| Slice | Ship decision | Date | If the learning says stop |
|---|---|---|---|
| 1 | [ship / hold with reason] | [date] | [what later slices get killed] |
| 2 | [ship / hold] | [date] | [killed scope] |

## Scope that earned deletion

[Work from the original plan that no slice needs. Deleting it is a deliverable —
list it so it stays deleted.]

## Rules

- A slice that cannot deploy alone is a fragment, not a slice. Re-cut it.
- Every slice boundary has a ship decision out loud — hold requires a reason, not a
  shrug.
- Time-to-learning per slice: [target, under 2 weeks]. Slices that cannot hit it get
  cut smaller, not rescheduled.
