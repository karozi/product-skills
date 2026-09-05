# The Ten Pivot Types

Reference for pivot-catalog. Definitions from Eric Ries, The Lean Startup (2011),
chapter 11 ("Adapt"), with symptom signatures and first cheap tests added for this
repository.

## 1. Zoom-in pivot
- **What changes:** one feature becomes the whole product.
- **Symptom signature:** one feature drives nearly all engagement; the rest is dead
  weight users tolerate to reach it.
- **Preserves:** the feature and its users. **Discards:** the broader product shell.
- **First cheap test:** single-feature MVP of that feature alone, shown to new users
  with no surrounding product.

## 2. Zoom-out pivot
- **What changes:** the whole product becomes one feature of something larger.
- **Symptom signature:** the product works but is "too small" to sustain a business;
  users keep asking what else it does.
- **Preserves:** the product as a module. **Discards:** the standalone positioning.
- **First cheap test:** landing page selling the larger product, with the current
  product shown as one capability.

## 3. Customer segment pivot
- **What changes:** the product stays; the target customer changes.
- **Symptom signature:** the product works, but for users nobody planned for. Usage
  concentrates in an unexpected segment.
- **Preserves:** the product. **Discards:** the original segment, pricing, channel.
- **First cheap test:** concierge MVP with five customers from the new segment.

## 4. Customer need pivot
- **What changes:** the customer stays; the problem solved changes.
- **Symptom signature:** the target user is right, but the problem you built for is
  not the one they pay to solve. Adjacent problems surface constantly in interviews.
- **Preserves:** the customer relationships and channel knowledge. **Discards:** the
  solution.
- **First cheap test:** discovery interviews plus a landing page for the newly named
  problem (run anti-mom-test on the interview script).

## 5. Platform pivot
- **What changes:** application becomes platform, or platform becomes application.
- **Symptom signature:** partners keep building the same add-on; or the platform's
  only successful user is your own app on top of it.
- **Preserves:** the underlying technology. **Discards:** the delivery form.
- **First cheap test:** expose the API to three external builders and watch what
  ships.

## 6. Business architecture pivot
- **What changes:** B2B swaps to B2C, or high-volume/low-margin swaps to
  low-volume/high-margin (Ries calls this the "startup butterfly").
- **Symptom signature:** sales cycles are too long for runway, or volume is there but
  margin cannot support the model.
- **Preserves:** the core value proposition. **Discards:** pricing, sales motion,
  often the channel.
- **First cheap test:** landing page + pricing test in the opposite architecture.

## 7. Value capture pivot
- **What changes:** how money is made — monetization model, not the product.
- **Symptom signature:** users love the product and will not pay the way you charge;
  they ask to pay a different way.
- **Preserves:** the product and users. **Discards:** the revenue mechanism.
- **First cheap test:** fake-door pricing page for the new model (see
  smoke-test-launcher).

## 8. Engine of growth pivot
- **What changes:** the growth engine focus — sticky, viral, or paid.
- **Symptom signature:** the current engine's governing metric is structurally stuck
  (churn will not fall, k-factor will not approach 1, LTV:CAC will not clear 3) while
  another engine shows signs of life.
- **Preserves:** the product. **Discards:** the growth playbook.
- **First cheap test:** one experiment on the new engine's governing metric (see
  engine-of-growth).

## 9. Channel pivot
- **What changes:** the distribution channel, not the product or customer.
- **Symptom signature:** the product works, the channel does not. CAC exceeds what
  the channel can ever return.
- **Preserves:** product, pricing, customer. **Discards:** the channel and its
  channel-specific pricing/packaging.
- **First cheap test:** small paid experiment in the new channel with the same offer.

## 10. Technology pivot
- **What changes:** the underlying technology, to deliver the same value cheaper or
  better.
- **Symptom signature:** the value is proven, but the technology cannot deliver it at
  a viable cost or quality. Users never see the change.
- **Preserves:** hypothesis, customers, positioning. **Discards:** the stack.
- **First cheap test:** Wizard-of-Oz delivery using the new technology behind the
  curtain, if user-invisible.

## Selection rules

- Match on symptom signature, not on fashion. Pivots are diagnosed, not chosen.
- The pivot type names what changes; the pivot brief names what survives.
- If no catalog type fits, the change is probably a roadmap item, not a pivot.
