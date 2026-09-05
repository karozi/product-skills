# Public Footprint Research Checklist

Work these source classes in order. They are ordered by evidence quality: first-party and regulatory
sources outrank press. Batch web searches in parallel; record every URL you might cite, and fetch
before tagging anything [SOURCED]. A search snippet is a lead, never a source.

## Source classes

1. Company's own site
   - /pricing, /plans, /teams, /enterprise pages: revenue model, segment hints
   - Homepage and product pages: value proposition as the company states it
   - /customers, /case-studies, /about: segments, partnerships
   - Integrations or marketplace directory: partnerships
   - Docs and changelog: key activities, release cadence
   - Footer links: community channels (customer relationships)
2. App stores (if applicable)
   - App Store / Play Store listing: in-app purchase tiers, pricing, description
   - Chrome Web Store / VS Code marketplace for extensions
3. SEC filings (if public)
   - 10-K: revenue breakdown, segments, risk factors naming competitors and dependencies
   - S-1 for recent IPOs: unit economics, customer concentration, growth metrics
   - Investor relations pages for earnings materials
4. Funding announcements
   - TechCrunch, VentureBeat, Axios, The Information funding round coverage
   - Investor blog posts (a16z, Sequoia, YC) describing the company's model
   - PitchBook or Crunchbase pages for round history (amounts are [SOURCED] if the page states them)
5. Job posts
   - Careers page, LinkedIn jobs, boards like Y Combinator's Work at a Startup
   - Roles hired reveal key activities (e.g., a fleet of enterprise AEs implies enterprise sales as a channel)
6. Founder interviews and talks
   - Podcasts, conference talks, X/Twitter threads, Reddit AMAs, Indie Hackers interviews
   - Highest-quality source for cost structure and revenue-mix reasoning; still tag claims as founder-stated
7. Press and analysis
   - Trade press, analyst notes quoted in press, Wikipedia (use only as a lead; follow its citations)
8. Community signals
   - Reddit, HN, Discord/Slack communities linked from the site: customer relationships, real segment gripes

## Search patterns that work

- "{company} pricing" and site-restricted searches of the company domain
- "{company} revenue" / "{company} how does it make money"
- "{company} funding round {year}"
- "{company} 10-K" or "{company} investor relations" for public companies
- "{company} careers" or "{company} is hiring"
- "{founder name} interview {company}"
- "{company} partnership announcement"

## Conflict protocol (for [CONTESTED])

1. Prefer the more recent source.
2. Prefer first-party over press, press over aggregators.
3. If both sides survive (e.g., pricing changed and neither source is dated), tag [CONTESTED], cite both, and note the likely explanation in the ledger.

## Stop conditions

- All 9 blocks have candidate evidence, or
- You have worked every applicable source class and re-searched the two weakest blocks once with different phrasings.

Then stop researching and tag honestly. Exhausted search plus [UNKNOWN] beats a fabricated number every time.
