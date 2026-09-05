---
name: engine-of-growth
description: "Diagnose which growth engine a product runs on — sticky, viral, or paid — and audit the one governing metric that engine depends on: churn for sticky, viral coefficient for viral, LTV to CAC for paid. Use when growth is slow and the cause is unclear, when planning growth experiments, when acquisition works but the numbers never compound, or when the user says engine of growth, why aren't we growing, sticky viral paid, growth engine, or which growth model. Not for choosing marketing tactics, running acquisition campaigns, or analyzing products with proven product-market fit and established growth loops."
---

# Engine of Growth

Every sustainable startup grows through one of three engines (Ries): sticky, viral, or
paid. Each engine has exactly one governing metric. Most growth failures are engine
confusion — running paid-engine playbooks on a product whose churn eats every cohort,
or chasing virality before anyone sticks around. This skill diagnoses the engine and
audits its governing metric.

## The Three Engines

- **Sticky:** growth comes from retention. Governing metric: churn. If churn exceeds
  acquisition, the engine runs backward.
- **Viral:** growth comes from users recruiting users. Governing metric: viral
  coefficient (k) — invitations sent times acceptance rate. Above 1.0, the product
  grows on its own; the cycle time decides how fast.
- **Paid:** growth comes from buying it. Governing metric: LTV:CAC. Above 3 with an
  acceptable payback period, spend is a machine; below, it is a leak.

## Modes

### Diagnose mode (default — user describes the product and growth situation)

1. Read `references/engines.md` before naming an engine.
2. Extract the evidence: acquisition trend, retention curve shape, any organic
  referral behavior, unit economics if known. UNKNOWNs are marked, not guessed.
3. Diagnose the engine the product's behavior actually fits — not the one the
  founders wish for. A product with flat retention and no viral loop is on the paid
  engine whether or not anyone budgeted for it.
4. Name the governing metric and its current value (or UNKNOWN plus how to measure it).
5. Report mismatches: the engine they are running versus the engine their actions
  assume. Mismatch is the most common finding and the most expensive.

### Audit mode (user knows the engine or Diagnose named it)

1. Pull the governing metric's trend, per cohort: churn (or retention curve), k-factor
   (with cycle time), or LTV:CAC (with payback period).
2. Check engine health against the thresholds in the reference.
3. Check engine-product fit: the product's natural usage patterns either feed the
  engine or starve it — high-frequency collaborative products feed viral; deep
  single-user value feeds sticky; strong monetization feeds paid.
4. Output one experiment — exactly one — on the governing metric, from
  `templates/engine-health.md`. Improving a non-governing metric is optimization of
  deck chairs.

## Hard Rules

- One engine at a time gets the focus. Products eventually layer engines; unproven
  products that chase all three get none.
- The governing metric is the only growth metric that matters until it is healthy.
- Virality before retention is noise: users do not invite friends to products they
  abandon.
- Paid growth on an engine-negative product buys traffic that churns — spending more
  to fill a leaking bucket is the most common terminal mistake.
- A metric that stays structurally stuck across real tuning is an engine-of-growth
  pivot signal (see pivot-catalog), not a try-harder signal.

## Output Shape (Diagnose mode)

```
Engine in behavior: [sticky / viral / paid] — evidence: [facts]
Engine assumed by current actions: [engine] — mismatch: [yes/no]
Governing metric: [metric] = [value or UNKNOWN]
Health: [healthy / weak / critical / unknown — against reference thresholds]
Next experiment: [one experiment on the governing metric]
```

Keep output in the user's language. Never diagnose an engine without stating the
evidence, and never let a wished-for engine override the behavior.
