---
name: smoke-test-launcher
description: "Design and launch demand smoke tests — fake-door pages, preorders, waitlists, and paid-ad probes — with the pass/fail threshold and minimum sample size signed before launch, then debrief results honestly. Use before building anything to test demand, when a landing page or waitlist experiment is planned, or when the user says smoke test, fake door, test demand before building, should we build it, or validate interest. Not for testing product value or usability (a smoke test measures demand, not the product) or for running full A/B experiments."
---

# Smoke Test Launcher

A smoke test asks one question: does anyone want this enough to act? It measures
demand for an offer that does not exist yet — cheaply, honestly, and with the verdict
written before launch so nobody can move the goalposts after.

## The Rule

The threshold and the sample size are signed before the page goes live. A test
"designed" after results arrive is a press release for a decision already made.

## Modes

### Draft mode (default — user has an idea to test)

1. Read `references/smoke-test-types.md` before choosing a format.
2. Extract the hypothesis: who wants what, badly enough to do what. If the user cannot
   state the action that counts as demand (signup, preorder, waitlist join, booking),
   ask once — the action IS the test.
3. Choose the format: fake-door page, preorder, waitlist, or paid-ad probe — matched
   to whether the risk is interest, willingness to pay, or message.
4. Write the page: headline (the promise in their words), one paragraph of mechanism
   (why it can deliver), the CTA (the demand action), and nothing else. Every extra
   element dilutes the signal.
5. Copy `templates/smoke-test-plan.md` and fill every bracket, including the source of
   traffic and its expected quality.

### Threshold mode (user has a page but no signed verdict criteria)

1. Set the pass threshold from the traffic source's baseline, not from optimism: [X]%
   conversion from [N] qualified visitors, with N sufficient for the number to mean
   anything.
2. Set the kill threshold and the gray zone. The gray zone triggers one pre-planned
   follow-up (a different headline or a different traffic source) — named now.
3. Set the honesty rules: what the page tells visitors about what exists today (see
   the reference's disclosure standards). Payment for undelivered products has the
   strictest rules.

### Debrief mode (user pastes results)

1. Check sample size and traffic quality first: a 20% conversion on 12 visitors is a
   rounding error, not a signal. State the confidence plainly.
2. Report against the signed threshold: PASS, FAIL, or GRAY. No new thresholds are
  accepted in Debrief mode.
3. Classify what was actually learned: demand for the problem, the message, or the
  audience — a smoke test result is about the offer as worded, not the product as
  imagined.
4. A PASS routes to mvp-type-selector for the value test. A FAIL routes to a different
   smoke test or kills the direction. A GRAY runs the pre-planned follow-up once.

## Hard Rules

- Thresholds and sample size are signed before launch and never renegotiated.
- The demand action must cost the visitor something — an email, money, or a booking.
  A click is not demand.
- Paid traffic needs quality control: bots and incentivized clicks convert differently
  and must be filtered or the threshold is fiction.
- Payment-based smoke tests disclose delivery terms before charging, full stop.
- One variable per test: offer, audience, or message — never all three at once.

## Output Shape (Debrief mode)

```
Result: [PASS / FAIL / GRAY] against signed threshold [value]
Sample: [N] qualified visitors from [source], [quality caveat]
Learned: [demand / message / audience — which one moved]
Next: [mvp-type-selector value test / follow-up test / kill]
```

Keep output in the user's language. Never call a gray result a win.
