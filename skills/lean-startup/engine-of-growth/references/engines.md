# The Engines, Their Metrics, and Their Traps

Reference for engine-of-growth Diagnose and Audit modes. Framework from Eric Ries,
The Lean Startup (2011), chapter 10 ("Engines of Growth"), with thresholds and traps
added for this repository.

## Sticky engine

- **Grows by:** retention exceeding churn. Acquired users stay; slow accumulation
  compounds.
- **Governing metric:** churn rate (per cohort). Equivalent view: the retention curve
  flattening — where it flattens is the user base that compounds.
- **Health signals:** churn falling across successive cohorts; retention curve
  flattening higher over time.
- **Failure signal:** acquisition outpacing churn in gross numbers while cohort churn
  stays flat — the engine looks alive only while spend does.
- **Natural fit:** products with deep individual value and habitual or high-stakes
  use — B2B tools, databases, services people build their workflow around.
- **Trap:** treating raw DAU growth as engine health. DAU without the cohort churn
  view is a vanity metric (run vanity-metric-audit).

## Viral engine

- **Grows by:** existing users recruiting new users.
- **Governing metric:** viral coefficient k = invites per user times acceptance rate.
  k above 1.0 grows without spend; below 1.0, virality accelerates paid or sticky
  growth but cannot carry it.
- **Secondary metric:** viral cycle time — days from signup to invitation. At the same
  k, shorter cycles compound dramatically faster.
- **Health signals:** k trending toward and past 1.0 with cycle time shrinking.
- **Failure signal:** engineered "viral" loops (forced invites, contact-importer
  spam) that lift signups and crush retention — k is meaningless on a churning base.
- **Natural fit:** products whose value involves other people — communication,
  collaboration, sharing, marketplaces with a side that needs inviting.
- **Trap:** virality bolted onto a single-user product. The product must be better
  because a friend is on it, or the loop is a growth tax.

## Paid engine

- **Grows by:** buying users profitably.
- **Governing metric:** LTV:CAC. Above 3 is the common health line; below 1 means
  every purchase destroys value.
- **Secondary metric:** payback period — months to recover CAC. Runway and cash flow
  set the acceptable ceiling.
- **Health signals:** LTV rising (usually via retention improving — engines
  interlock), CAC stable or falling at scale.
- **Failure signal:** CAC rising as spend scales while LTV stays flat — most ad
  auctions do this eventually; only improving retention or monetization fights back.
- **Natural fit:** products with strong monetization per user and linearly scalable
  acquisition channels.
- **Trap:** paying for growth to hit a board-projected curve while LTV:CAC sits under
  1. That is not growth, it is liquidation at retail.

## Engine-product fit

| Product pattern | Engine it feeds |
|---|---|
| Deep personal value, single user, habitual | sticky |
| Value increases with other users present | viral |
| High revenue per user, linear channels | paid |
| Weak retention, no viral loop, thin margins | none — engine problem precedes growth problem |

## Escalation rule

A governing metric structurally stuck across honest tuning (multiple iterations, flat
results) escalates to pivot-or-persevere, with engine-of-growth pivot as a named
option in the catalog.
