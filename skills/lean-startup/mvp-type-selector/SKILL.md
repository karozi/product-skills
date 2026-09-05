---
name: mvp-type-selector
description: "Pick the cheapest MVP type that actually tests a product hypothesis — landing page, concierge, Wizard of Oz, piecemeal, single-feature, or explainer video — and output a build plan with pass/fail thresholds set before launch. Use when planning a first version, validating an idea before building, choosing between MVP options, or when the user says MVP type, cheapest way to test this, what kind of MVP, or validate before building. Not for scaling an already-validated product or writing full PRDs."
---

# MVP Type Selector

An MVP is not a small product. It is an experiment that answers one question at the
lowest possible cost. This skill picks the MVP type that tests the riskiest assumption,
names the pass/fail threshold before anything ships, and refuses to let "build" be the
first step of the loop.

## The Rule

The right MVP is the one that produces the required learning for the least build effort.
If two types answer the same question, pick the one you can kill fastest. Speed of
learning beats fidelity of product.

## Modes

### Select mode (default — user describes an idea or hypothesis)

1. Read `references/mvp-type-catalog.md` before recommending anything.
2. Extract the hypothesis. If the user has not stated one falsifiable hypothesis, ask
   for it once — an MVP without a hypothesis is just a rushed product.
3. Identify the riskiest assumption the MVP must test: demand ("will anyone care?"),
   value ("will they use it enough?"), or willingness to pay ("will they give up
   money/time/reputation?").
4. Recommend one MVP type with: why this type, what it tests, what it deliberately does
   not test, estimated cost, days to first learning, and the kill condition.
5. Output the test plan from `templates/mvp-test-plan.md` with every bracket filled.

### Plan mode (user has already chosen a type)

1. Confirm the type exists in the catalog; if the user invented a hybrid, decompose it
   into the catalog types it combines and say so.
2. Fill the test plan. The pass/fail threshold must be written before launch — a
   threshold decided after seeing results is not a threshold, it is a rationalization.
3. Include the de-risking order: which manual process, if the test passes, gets automated
   first (the concierge-to-product path).

### Audit mode (user pastes an existing MVP plan or built product)

1. Number every planned feature.
2. Tag each feature: TESTS HYPOTHESIS or PRODUCT POLISH. Anything tagged polish that
   ships before the hypothesis is confirmed is scope creep wearing a lab coat.
3. Report the learning-to-build ratio: what will be learned vs what will be built.
   Verdict — "Real experiment" (learning-first), "Product in disguise" (build-first with
   a test attached), or "Just building" (no falsifiable test at all).

## Hard Rules

- One MVP tests one hypothesis. Two hypotheses means two MVPs, sequenced.
- Wizard of Oz and concierge MVPs involve lying to users during the test. Flag the
  disclosure obligation: be honest at the moment of conversion or payment.
- The threshold is signed off before launch and cannot be renegotiated after.
- If the MVP is "the full product, phase one," it is not an MVP. Cut until removing
  more would make the test meaningless.

## Output Shape (Select mode)

```
Hypothesis: [one falsifiable sentence]
Riskiest assumption: [assumption the MVP must test]
MVP type: [type] — [one-line why this type]
Tests: [what will be learned] · Does not test: [explicit non-goals]
Cost: [money/time estimate] · First learning in: [days]
Kill condition: [specific result that ends this direction]
```

Then the full test plan. Keep output in the user's language. Never recommend a type
without naming what it does not test.
