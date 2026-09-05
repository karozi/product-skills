# Batch Pathologies

Reference for small-batches Audit mode. Each pathology has a signature and a re-slice
counter.

## 1. Big-bang release
- **Signature:** every workstream converges on one ship date; the release checklist
  runs pages long; the rollback plan is "there is no rollback plan."
- **Why it hurts:** risk compounds — five independently survivable mistakes become one
  unsurvivable launch. Feedback arrives only after the entire bet.
- **Re-slice counter:** vertical slices, each shippable; the "release" becomes the
  last slice, not the container of all of them.

## 2. Integration-at-end
- **Signature:** components build in parallel for weeks, merge in one painful window
  ("integration hell"), and nobody can run the product end-to-end until then.
- **Why it hurts:** the most expensive defects (the ones between components) surface
  last, when all the context has evaporated.
- **Re-slice counter:** integrate continuously — trunk-based flow, every slice merges
  working software, the end-to-end path runs from slice one.

## 3. Requirement hoarding
- **Signature:** months of specified-but-unbuilt work; PRDs for features queued behind
  other PRDs; the roadmap is a warehouse.
- **Why it hurts:** requirements are inventory — they rot as the market and the
  product move. The warehouse guarantees building last year's product.
- **Re-slice counter:** specify just ahead of the build; every slice re-earns its
  requirements. Hoarded requirements that no longer earn their place get deleted, not
  archived.

## 4. Done-but-unshipped
- **Signature:** finished work sits behind a feature flag or a release train, waiting
  for a batch to join. "Done" tickets pile up while users see nothing.
- **Why it hurts:** learning is delayed after the cost is already paid — the worst
  possible ordering. And unshipped work drifts from reality until shipping it
  requires rework.
- **Re-slice counter:** ship at slice boundaries; a feature flag is a two-state
  experiment tool (see build-measure-learn), not a warehouse.

## 5. Invisible WIP queue
- **Signature:** many things started, few finishing; status meetings exist to
  negotiate what "in progress" means.
- **Why it hurts:** WIP hides blockers, thrashes attention, and makes the queue's
  length invisible until deadlines do the counting.
- **Re-slice counter:** limit WIP to the number of active slices; finish before
  starting. The queue becomes visible the moment starting requires finishing.

## The envelope argument (why small beats "efficient")

Stuffing envelopes one at a time (fold, stuff, seal, stamp, repeat) looks slower than
batching each step. It finishes the first envelope sooner, so feedback and stopping
both arrive early; it surfaces a bad fold at envelope one, not envelope hundred. In
product work the same logic compounds: the first slice shipped teaches whether the
remaining slices should exist. Ries's version: the fastest way to learn is through
small batches, even when each batch feels less efficient.

## Measuring the batch

The number that matters: **elapsed time from first work started to first user
learning** from that work. Not velocity, not story points, not percent complete.
If that number is over six weeks or unmeasurable because nothing ships until the
end, the audit verdict is batch pathology.

Source: lean manufacturing batch-size economics (Toyota Production System) as
translated to startups in Eric Ries, The Lean Startup (2011), chapter 9 ("Batch"),
with the envelope example from that chapter.
