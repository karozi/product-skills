# Test Card and Learning Card Templates

Templates and quality rules for generating Strategyzer testing artifacts. Follow these exactly; do not improvise the sentence stems.

Source formats: Strategyzer's Test Card makes four things explicit: what needs to be true (hypothesis), how you will test it, what you will measure, and what the success threshold is ([Strategyzer: Validate Your Ideas with the Test Card](https://www.strategyzer.com/library/validate-your-ideas-with-the-test-card), [Strategyzer: Good Ideas Are Bad For Innovators](https://www.strategyzer.com/library/good-ideas-are-bad-for-innovators)). The Learning Card captures which hypotheses you tested, what you observed, what you deduce, and how you will act ([Strategyzer: Capture Customer Insights and Actions with the Learning Card](https://www.strategyzer.com/library/capture-customer-insights-and-actions-with-the-learning-card)). Strategyzer also distinguishes evidence types and data-point counts when judging how validated a hypothesis really is ([Strategyzer: Is Your Hypothesis Really Validated?](https://www.strategyzer.com/library/business-testing-is-your-hypothesis-really-validated)).

## Test Card

One card per assumption. Exact format:

```
We believe that [hypothesis].
To verify that, we will [experiment].
We are confident if [metric] is at least [threshold].
```

Header fields above the stem (include in every card):

```
### Test Card [n]: [short name]
- Assumption: [the assumption from the ranking table]
- Type: desirability | feasibility | viability
- Evidence strength: weak | strong
- Cost: [hours and dollars, estimated]
- Time to signal: [days]
```

### Hypothesis rules

1. State a testable belief about behavior, not a feature or opinion. "Paid subscribers will click a job board link" is testable. "A job board would be valuable" is not.
2. Name the segment. Who exactly will do the thing.
3. One belief per card. If the hypothesis contains "and", split it into two cards.

### Experiment rules

1. Cheapest pattern that can still move the belief. Check `ai-experiment-patterns.md` before choosing.
2. Concrete enough to run tomorrow: channel, asset, audience size, duration.
3. Weak tests (interest signals) come first; strong tests (commitment signals) are follow-up cards triggered only when the weak test passes.

### Metric and threshold rules

1. The metric must be behavioral: clicks, replies, signups, dollars, retention. Stated intent ("would you use this?") never counts.
2. Every threshold is a number with a unit and a timeframe. Set it before running, based on a baseline or a kill-worthy minimum, and write down why that number.
3. State the kill condition too: what result invalidates the assumption and stops the line of testing.

### Quality checklist (reject the card if any fail)

- [ ] A stranger could run the experiment from the card alone
- [ ] The threshold is numeric and was not chosen after seeing results
- [ ] The metric plausibly predicts the real-world behavior (signups do not prove willingness to pay)
- [ ] The experiment is the cheapest available evidence for this belief

## Learning Card

For every completed test, before discussing next steps. Exact format:

```
We believed [x]. We observed [y]. We learned [z], so we now believe [new].
```

Fill the placeholders with: [x] the exact hypothesis from the Test Card, [y] raw numbers from the field, [z] the deduction those numbers support, [new] the updated hypothesis. Append the decision on the same card, as its own line: `Decision: iterate | persevere | pivot | kill.`

Decision must be one of: **iterate** (run a variant of the same test), **persevere** (assumption validated, move to the next card), **pivot** (change the idea based on the learning), or **kill** (stop this line of testing).

### Learning Card rules

1. Observations are raw numbers, not interpretations. Separate the two strictly.
2. If the result is ambiguous, say so and specify the next cheaper test that resolves the ambiguity. Ambiguity is a valid learning.
3. One learning per card. Never bundle multiple experiments.
4. Low data volume means weak evidence. Flag results from tiny samples instead of declaring victory ([Strategyzer: Is Your Hypothesis Really Validated?](https://www.strategyzer.com/library/business-testing-is-your-hypothesis-really-validated)).

## Worked examples

### Test Card (weak evidence, day 1)

```
### Test Card 1: Job board fake door
- Assumption: Paid subscribers want an AI agents job board section
- Type: desirability
- Evidence strength: weak
- Cost: 1 hour, $0
- Time to signal: 7 days

We believe that paid subscribers want an AI agents job board section.
To verify that, we will add a fake-door link to the next two issues and
the paid welcome email, leading to a page describing the section with an
email capture form.
We are confident if at least 5% of link clicks submit an email within 7 days.
Kill if fewer than 2% submit.
```

### Test Card (strong evidence, follow-up)

```
### Test Card 2: Job board pre-order
- Assumption: Subscribers will pay extra for the job board
- Type: viability
- Evidence strength: strong
- Cost: 4 hours, $0
- Time to signal: 14 days
- Trigger: run only if Test Card 1 passes

We believe that at least 3% of paid subscribers will pay $5/month extra
for the job board.
To verify that, we will email the fake-door signups a pre-order offer
with a Stripe payment link and a 30-day money-back guarantee.
We are confident if at least 20 pre-orders complete within 14 days.
Kill if fewer than 8.
```

### Learning Card

```
## Learning Card 1: Job board fake door

We believed that at least 5% of paid subscribers who clicked a job board
link would submit an email.
We observed 412 clicks and 41 email submissions, a 9.95% rate over 7 days.
We learned that interest in a job board exceeds the bar and the audience
is large enough to test willingness to pay.
So we now believe the job board clears the interest bar but payment is
unproven.
Decision: persevere. Run Test Card 2, the pre-order check.
```
