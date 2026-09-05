# Smoke Test Plan

Template for smoke-test-launcher Draft and Threshold modes. Every bracket filled
before launch. Thresholds do not move after results arrive.

## Hypothesis

[One falsifiable sentence: "We believe [audience] will [demand action] when offered
[what the page promises]."]

## The test

- **Format:** [fake-door / preorder / waitlist / paid-ad probe]
- **Demand action:** [the visitor's cost — email, payment, booking. A click is not a
  demand action.]
- **Why this format:** [one line tying the format to the demand risk]

## The page

- **Headline:** [the promise, in the audience's words]
- **Mechanism paragraph:** [one paragraph: why this can deliver the promise]
- **CTA:** [the demand action, worded exactly as visitors will see it]
- **Deliberately excluded:** [everything else — each exclusion strengthens the signal]

## Disclosure

[What the page tells visitors about what exists today. Preorders state delivery and
refund terms before charging.]

## Traffic

- **Source:** [where visitors come from]
- **Expected quality:** [cold / warm / organic; filtering plan for paid or incentivized
  traffic]
- **Planned volume:** [N visitors minimum]

## Signed verdict (before launch)

- **Pass:** [X]% of [N] qualified visitors complete the demand action
- **Fail / kill:** [result that ends this direction]
- **Gray zone:** [range that triggers the one pre-planned follow-up test: [follow-up
  design]]
- **Sign-off:** [who agreed to these numbers, and when]

## After the test

- **If PASS:** value test via mvp-type-selector — [one-line sketch of what it would
  be]
- **If FAIL:** [kill, or the one alternative angle worth a second smoke test]
- **If GRAY:** run the pre-planned follow-up once. A second gray is a fail.

## Rules

- One variable per test: page, audience, or message — never all three.
- Sample size below the signed minimum is reported as insufficient, not as a signal.
- Results never renegotiate thresholds. Gray is not a win.
