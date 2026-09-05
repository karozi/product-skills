# MVP Type Catalog

Reference for mvp-type-selector. Each type answers a different question at a different
cost. Match the type to the riskiest assumption, not to the final product vision.

## The catalog

### 1. Landing page / fake door
- **Tests:** demand and message-market fit before anything exists.
- **How:** one page, one promise, one CTA (signup, preorder, or waitlist). Drive real
  traffic; measure conversion.
- **Cost:** days, near-zero money. **First learning:** days.
- **Does not test:** whether the product can deliver on the promise.
- **Use when:** the riskiest assumption is that anyone wants this at all.
- **Kill condition example:** conversion below [X]% from [N] qualified visitors.

### 2. Concierge MVP
- **Tests:** the value hypothesis with a human delivering the service manually.
- **How:** deliver the product as a white-glove service to a handful of customers. They
  experience the outcome; you learn every step of the workflow.
- **Cost:** weeks of founder time, tiny money. **First learning:** 1–2 weeks.
- **Does not test:** scale, unit economics at volume, automation feasibility.
- **Use when:** the workflow is uncertain and you need to learn what the product must do
  by doing it yourself.
- **Bonus:** produces the exact spec for what to automate first.
- **Kill condition example:** fewer than [N] of [M] concierge customers return for a
  second session.

### 3. Wizard of Oz
- **Tests:** whether the automated experience feels valuable — before the automation
  exists.
- **How:** front end looks finished; humans do the work behind the curtain (the classic
  example: Zappos founders buying shoes at retail to fill early orders).
- **Cost:** medium build, high manual ops. **First learning:** 1–3 weeks.
- **Does not test:** whether the real system can produce results at that cost.
- **Use when:** the experience is the product and you must test the experience, not the
  plumbing.
- **Disclosure:** be honest at conversion or payment — users must not pay for what they
  believe is automation.
- **Kill condition example:** users who get the outcome still do not return within [N] days.

### 4. Piecemeal MVP
- **Tests:** end-to-end value using existing tools glued together, no custom core.
- **How:** assemble no-code tools, spreadsheets, and existing services into the full
  customer journey.
- **Cost:** low build. **First learning:** 1–2 weeks.
- **Does not test:** defensibility, technical feasibility of the real build.
- **Use when:** the value is in the orchestration, not the technology.
- **Kill condition example:** [X]% of first [N] users do not complete the core loop twice.

### 5. Single-feature MVP ("Ear of the GM")
- **Tests:** the one interaction that carries all the value.
- **How:** ship exactly one feature — the whole product is that feature done excellently.
- **Cost:** highest on this list. **First learning:** weeks.
- **Does not test:** everything else; that is the point.
- **Use when:** the core interaction must be experienced to be believed (the classic
  example: Dropbox's single-folder sync before file sharing, web UI, or mobile).
- **Kill condition example:** week-2 retention of activated users below [X]%.

### 6. Explainer video
- **Tests:** comprehension and demand for a future capability.
- **How:** a video showing the promised experience; measure signups (the classic
  example: Dropbox's 3-minute demo that multiplied the waitlist 5x overnight).
- **Cost:** days. **First learning:** days.
- **Does not test:** anything about usage or retention.
- **Use when:** the product is invisible in a screenshot and the concept needs showing.
- **Kill condition example:** signup rate below [X]% of video viewers.

## Selection heuristics

- Demand risk → landing page or explainer video.
- Value / workflow risk → concierge.
- Experience risk → Wizard of Oz.
- Orchestration risk → piecemeal.
- Core-interaction risk → single-feature.
- Never run two MVP types in parallel on the same hypothesis — the results contaminate
  each other.
- The MVP that can be killed fastest and still answer the question wins. Ties go to the
  cheaper one.

Source: MVP taxonomy synthesized from Eric Ries, The Lean Startup (2011), chapter 8
("Batch"); the Zappos and Dropbox cases in chapters 1 and 5 of the same book; and Ash
Maurya, Running Lean (2012). Format adapted for this repository.
