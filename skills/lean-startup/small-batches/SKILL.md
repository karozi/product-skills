---
name: small-batches
description: "Audit roadmaps, backlogs, and release plans for batch-size pathology — big-bang releases, quarter-long requirement queues, work that integrates at the end — and re-cut them into small shippable slices with learning checkpoints. Use when a release keeps slipping, when work sits done-but-unshipped, when integration happens in one painful merge, or when the user says small batches, why is this release taking so long, re-slice, batch size, big bang release, or WIP is piling up. Not for sprint mechanics, capacity planning, or personal productivity batching."
---

# Small Batches

Large batches feel efficient and are the opposite: work queues up invisible, risk
compounds silently, and feedback arrives only after everything is wrong. From Toyota's
lean manufacturing to Ries's startups, the rule is the same — shrink the batch until
the cost of finding a mistake approaches zero. This skill audits batch pathology and
re-cuts plans into slices that ship and learn.

## Why Small Batches Win

The famous envelope-stuffing example: fold, stuff, seal, stamp one envelope at a time
looks slower than running each step in bulk. It is not. Small batches finish
end-to-end sooner (first feedback arrives at envelope one, not after all hundred),
surface defects at the cheapest moment, and keep work-in-progress visible. Big batches
hide every problem until the moment it is most expensive.

## Modes

### Audit mode (default — user pastes a roadmap, epic, backlog, or release plan)

1. Read `references/batch-pathologies.md` before flagging.
2. Number every item, feature, or workstream.
3. Flag each pathology present: big-bang release (everything ships at once),
  integration-at-end (pieces merge only when all are done), requirement hoarding
  (months of specified-but-unbuilt work), done-but-unshipped (work finished, waiting
  for a batch to join), invisible WIP queue (work started but not completable soon).
4. Measure the batch: time from first work started to first user learning. That
  number — not story points, not task count — is the batch size that matters.
5. Verdict — "Slicing well" (learning under 2 weeks), "Batching up" (2–6 weeks),
  "Batch pathology" (6+ weeks or unmeasurable because nothing ships until the end).

### Re-slice mode (audit done, user wants the re-cut plan)

1. Find the slice axis: the thinnest path through the work that ships something to a
  real user and produces learning. Usually vertical — one user, one job, end to end —
  never horizontal ("the database layer," "all the UI").
2. Re-cut the work into slices. Every slice passes three tests: it ships (deployable
  on its own), it learns (a real user's behavior changes measurably), and it is
  smaller than the last one that hurt.
3. Sequence the slices by learning value, riskiest first (the build-measure-learn
  loop governs the order; the roadmap does not).
4. Write the re-slice from `templates/slice-plan.md` with the integration and release
  checkpoint at every slice boundary — the moment work is "done" is the moment it
  merges, not a date at the end.
5. Name what gets easier to say no to: small batches expose work that no longer
  needs doing. Killed scope is a re-slice deliverable, not a failure.

## Hard Rules

- Batch size is measured in time-to-learning, never in task count.
- A slice that cannot ship alone is not a slice; it is a fragment.
- Integration is continuous or the batch is still big — merging at the end is the
  pathology wearing a different hat.
- Every slice boundary has a release decision: ship it, or say out loud why not.
- If the plan cannot be sliced without shipping something embarrassing, the slice is
  still right and the embarrassment is information.

## Output Shape (Audit mode)

| # | Item / plan feature | Pathology | Evidence |
|---|--------------------|-----------|----------|

Followed by the batch measurement, verdict, and the recommended slice axis. Keep
output in the user's language. Never re-slice without naming the learning each slice
produces.
