# Canvas Definitions, Evidence Tags, and AI-Era Rubric

Read this before filling any cell. Terminology follows Strategyzer's Value Proposition
Canvas (from *Value Proposition Design*, Osterwalder et al.). Verified against:

- https://www.strategyzer.com/value-proposition
- https://www.strategyzer.com/library/the-value-proposition-canvas
- https://www.strategyzer.com/library/value-proposition-design-book-summary

## Canvas structure

The canvas has two sides. The Customer Profile (the circle) describes the customer.
The Value Map (the square) describes the offering. Fit is achieved when the two match.

### Customer Profile (circle, built from user voice)

- **Customer jobs**: what customers are trying to get done. Four kinds: functional
  (perform or complete a specific task), social (look good, gain power or status),
  emotional (feel good, security, aesthetics), and basic needs (communication,
  nourishment). Rank jobs: major jobs the customer would be upset to fail, then
  supporting jobs (searching, comparing, buying, disposing).
- **Customer pains**: negative emotions, undesired costs and situations, and risks
  the customer experiences or could experience before, during, and after getting
  the job done. Include what makes the customer feel bad, what current solutions
  underperform at, what they fear, and what blocks adoption.
- **Customer gains**: benefits the customer expects, desires, or would be surprised
  by: functional utility, social gains, positive emotions, and cost savings.
  Include required gains (dealbreakers), expected gains, desired gains, and
  delighters.

### Value Map (square, built from vendor voice)

- **Products & services**: the bundle of goods and services the value proposition
  relies on. Physical, digital, services, platforms. List what actually exists,
  not roadmap promises (tag promises as [SOURCED] to a changelog/roadmap URL and
  note "announced, not shipped").
- **Pain relievers**: how products and services alleviate specific customer pains.
  Each reliever must name the pain it addresses; a reliever with no matching pain
  is a feature list, not a canvas.
- **Gain creators**: how products and services produce outcomes and benefits
  customers care about. Same rule: each creator maps to a named gain.

## Evidence tag rules

Every entry in every cell gets exactly one tag. No untagged entries, ever.

- **[SOURCED](url)**: the claim appears at the linked URL, verbatim or as a tight
  paraphrase. Customer Profile entries must preserve the user's own wording in
  quotes where possible. One URL per tag; if a claim needs two URLs, split it.
- **[INFERRED]**: you synthesized it from multiple [SOURCED] items, and no single
  source states it. Add the source URLs in parentheses after the tag, e.g.
  [INFERRED] (url1, url2). If you cannot cite the underlying sources, it is not
  inferred, it is invented.
- **[ORIGINAL]**: your own analytical claim with no source. Use sparingly: mainly
  for fit-assessment arguments and AI-era scores. Product facts and user quotes
  are never [ORIGINAL].

Sanity gate before delivery: any quote attributed to a user must exist at its URL.
If a fetch failed or the page is gone, downgrade to [INFERRED] or drop the entry.

## AI-era factor rubric

Score every cell's entries for these four factors. Use Low / Medium / High with a
one-line justification. These scores are analytical, so tag them [ORIGINAL].

- **Model dependency**: how much the value in this cell depends on a third-party
  model provider (OpenAI, Anthropic, Google). High = the product is a thin wrapper
  whose value collapses if the provider ships the same feature.
- **Credit pricing**: exposure to token/credit-based costs: usage pricing, rate
  limits, metered API calls, cost surprises at scale. High = users complain about
  unpredictable spend.
- **Agent-readiness**: how well the offering works when the "user" is an agent:
  public API, headless operation, MCP support, structured output, no click-only
  flows. High = agents can adopt it without a human.
- **Vendor lock-in**: switching costs: proprietary data formats, walled gardens,
  no export, ecosystem-specific skills or configs. High = leaving hurts.

Record the four scores as a compact `model/credits/agent/lock-in` line per cell,
and collect them into a summary table at the end of the canvas.

## Fit assessment definitions (Strategyzer's three fits)

- **Problem-solution fit**: evidence that the Value Map addresses real jobs,
  pains, and gains of the Customer Profile. Look for: sourced pains that have a
  named pain reliever, and sourced gains with a named gain creator.
- **Product-market fit**: evidence the value proposition creates real value for
  customers. Look for: users saying they would be very disappointed without it,
  retention/pricing signals, organic advocacy in the sourced threads.
- **Business model fit**: evidence the value proposition can be embedded in a
  profitable, scalable business model. Look for: pricing vs. cost structure
  signals (especially credit pricing), margin pressure from model dependency,
  lock-in effects on churn.

Rate each fit: `Strong / Emerging / Unproven / Absent`, plus a one-paragraph
argument citing cell entries by name.
