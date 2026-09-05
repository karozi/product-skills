# Smoke Test Types

Reference for smoke-test-launcher. Each format answers a different demand question at
a different honesty level.

## 1. Fake-door page
- **Tests:** whether people will act on an offer that does not exist yet.
- **How:** a page describing the product with a working CTA (signup, request access).
  Behind the door: "coming soon" or a waitlist confirmation.
- **Cost:** days. **Best for:** pre-build demand checks on new concepts.
- **Disclosure:** the door itself is the test; the confirmation page should say what
  is real ("we're building this; join the list") without burying it.
- **Classic pattern:** the Zappos-originated family of tests — take the order, learn
  from the order, then decide what to build.

## 2. Preorder smoke test
- **Tests:** willingness to pay, the strongest demand signal available pre-build.
- **How:** a page selling the product with a delivery date, charging or
  pre-authorizing payment.
- **Cost:** days plus payment infrastructure. **Best for:** products with clear,
  describable value.
- **Disclosure:** strictest standard — delivery terms, refund terms, and that the
  product is not yet built, all before the charge. Never hold money on undisclosed
  terms.
- **Threshold note:** preorder conversion is far lower than waitlist conversion;
  thresholds differ by an order of magnitude.

## 3. Waitlist test
- **Tests:** interest, cheaply and at scale.
- **How:** the classic launch-page pattern — headline, mechanism paragraph, email
  capture, often with a referral incentive (the Dropbox pattern).
- **Cost:** hours. **Best for:** fast signal on message-market fit before any build.
- **Weakness:** an email is the weakest demand currency. High waitlist conversion
  with low later activation is the standard failure pattern — treat waitlist results
  as directional only.
- **Referral incentive variant:** position boosts for referrals also test virality
  cheaply.

## 4. Paid-ad probe
- **Tests:** whether the message pulls real, targeted traffic — the closest thing to
  a demand test with zero page-building.
- **How:** small budget across ad variants; measure click-through and conversion to
  the landing action.
- **Cost:** the ad budget, capped. **Best for:** testing messages against each other
  and validating traffic quality before scaling spend.
- **Quality control:** filter bots and incentivized clicks; report the filtered
  volume. Unfiltered paid results are fiction.
- **Threshold note:** CTR alone is not demand — the action after the click is.

## Choosing

- Risk is "does anyone care" → waitlist or fake-door.
- Risk is "will they pay" → preorder.
- Risk is "which message" → paid-ad probe.
- One variable per test. Changing page and audience simultaneously produces a result
  nobody can attribute.

## Traffic sources and their baselines

| Source | Quality | Typical honest baseline |
|---|---|---|
| Cold paid (targeted) | medium | waitlist conversions in single-digit percentages |
| Warm list / newsletter | high | several times cold rates |
| Community / social organic | variable | filter for intent; report source mix |
| Untargeted or incentivized | low | thresholds are meaningless without filtering |

Baselines vary by market and offer; the table sets expectations, not excuses. Sign
the threshold from your own traffic source's history when available, and say which
source the number assumed.

Source: fake-door and preorder practice as synthesized from Eric Ries, The Lean
Startup (2011) (the Zappos and Dropbox cases) and Ash Maurya, Running Lean (2012),
with disclosure standards adapted from consumer-protection norms for preorders.
