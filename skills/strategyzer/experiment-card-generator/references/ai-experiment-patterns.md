# AI-Product Experiment Pattern Library

Reusable experiment patterns for AI products, newsletters, and content businesses. Check this library before designing any Test Card: pick the cheapest pattern that can move the belief, and reserve strong-evidence patterns as follow-up cards.

Cheapest-first ordering across the library: GSC query validation and Reddit reply tests cost nothing but time. Waitlists and fake doors cost an hour. A/B subject lines cost one send. Pre-order and fake-door pricing tests cost real reputational capital. Churn interviews cost the most per data point because they do not scale.

## 1. GSC query validation (cost: $0, weak evidence)

Tests whether search demand exists for an idea before writing anything.

1. Open Google Search Console for the existing site; export queries and impressions for the last 90 days.
2. Look for queries that match the idea's jobs, pains, and language. Note impressions, clicks, and position.
3. No GSC history or a new topic: use search autocomplete and People Also Ask to estimate whether the query space exists, and treat it as directional only.

Good for: content ideas, course topics, new sections, AIO/GEO discoverability bets. The metric is existing impressions and CTR on matching queries. A threshold looks like "at least 500 monthly impressions on matching queries with CTR above 2%". Limitation: shows interest, never willingness to pay.

## 2. Reddit reply engagement test (cost: $0, weak evidence)

Tests whether a claim or framework resonates by publishing a fragment where the target audience already argues.

1. Find 2 or 3 subreddits where the target reader hangs out.
2. Write a reply that applies the claim to a real question. No promotion, no link drop unless the sub allows it.
3. Track upvotes, replies, and DMs over 7 days.

Good for: desirability of frameworks, pain validation, language testing before drafting. Metric: upvote ratio and substantive replies. Threshold example: "at least 10 upvotes and 3 substantive replies in one thread". Escalate to a waitlist only if the language lands.

## 3. Waitlist (cost: 1 hour, weak evidence)

Tests interest with a single call to action.

1. Build a one-page description of the idea with one email capture form.
2. Drive the cheapest traffic first: a link in the next newsletter issue, a post, a pinned reply.
3. Measure signups against reach, not raw count.

Metric: signup conversion from unique visitors. Threshold example: "at least 10% of unique visitors sign up". Known trap: emails are interest, not commitment. Never claim validation of willingness to pay from a waitlist.

## 4. Fake-door pricing page (cost: 1 to 2 hours, medium evidence)

Tests willingness to pay before building, by showing a price and a buy button that leads to a "not live yet" screen.

1. Create a page presenting the offer with a real price and a Buy button.
2. Route clicks to a page saying the product launches soon, with an optional email capture.
3. Measure click-through on the priced button.

Good for: pricing sensitivity, feature demand inside an existing product. Metric: priced-button CTR from qualified visitors. Threshold example: "at least 4% click the $20/month buy button". Caveat: clicks cost nothing, so treat a pass as permission to run a pre-order, not as proof.

## 5. Pre-order check (cost: 2 to 4 hours, strong evidence)

Tests real commitment with real money.

1. Offer the thing at a real price to a warm segment (waitlist signups, existing subscribers) with a payment link and a refund guarantee.
2. Set a fixed window, 7 to 14 days.
3. Count only completed payments.

Metric: completed purchases divided by the segment contacted. Threshold example: "at least 3% of contacted waitlist signups pre-order". This is the cheapest strong evidence available; use it before building anything billable.

## 6. A/B subject lines (cost: one send, weak-to-medium evidence)

Tests which framing of a claim earns attention, inside an existing channel.

1. Write two subject lines that differ in one dimension: specificity, curiosity, or outcome.
2. Split the send 50/50 using the email tool's A/B feature.
3. Judge on unique open rate and, better, click rate on the claim's call to action.

Metric: open rate difference and click rate on the linked action. Threshold example: "subject B wins by at least 3 percentage points opens with no click-rate loss". Good for headline claims, post framings, offer positioning. Limitation: measures attention, not belief.

## 7. Churn interviews (cost: high per data point, weak-to-strong evidence)

Tests why people leave, which survey data never reveals.

1. Pull the last 20 to 30 churned subscribers.
2. Send a short, honest email: you are trying to understand why people cancel, 15 minutes, no sales pitch. Offer nothing, or a small gift card if needed.
3. Run 20-minute calls. Ask what they expected at signup and where it broke. Never pitch.
4. Code the answers into recurring reasons until the top 3 explain most cancellations.

Metric: count of interviews plus the top 3 coded reasons covering at least 60% of answers. Good for: retention assumptions, positioning drift, which promise the product fails to keep. Runs in parallel with cheap tests because scheduling takes weeks.

## Choosing and sequencing

1. For any desirability assumption: GSC validation or Reddit reply test first, then waitlist, then fake door.
2. For any viability (willingness to pay) assumption: fake-door pricing page first, then pre-order check. Never skip to building.
3. For any messaging assumption: A/B subject lines before redesigning anything.
4. For retention assumptions: churn interviews run in the background from day one because they are slow to gather.
5. Every strong-evidence card lists the weak-evidence card that must pass first as its trigger.
