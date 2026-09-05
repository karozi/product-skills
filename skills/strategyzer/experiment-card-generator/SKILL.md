---
name: experiment-card-generator
description: "Turn claims, assumptions, draft excerpts, or roadmap items into Strategyzer Test Cards and Learning Cards: extract every risky assumption, rank by evidence risk and test cost, write each card in the exact we-believe / to-verify / confident-if format with a numeric threshold, apply the cheapest-test-first rule so waitlists, search-query checks, and fake-door links always precede builds and paid campaigns, and output a paste-ready experiment backlog grouped by evidence strength. Use when the user says test cards, experiment cards, turn claims into experiments, how would I test this assumption, or design experiments for this draft. Not for running the experiments, analytics instrumentation, or prioritizing already-validated work."
---

# Experiment Card Generator

Turn claims, assumptions, or draft excerpts into Strategyzer testing artifacts: Test Cards, Learning Cards, and a prioritized experiment backlog.

## When to Use This Skill

Use when the user provides a draft, claim list, product idea, roadmap item, or claim ledger from a fact-check, and wants experiments, test cards, or a testing plan. Trigger phrases: "test cards", "experiment cards", "turn claims into experiments", "how would I test this assumption", "design experiments for this draft".

## Instructions

1. **Extract assumptions.** Read the input and list every risky assumption it depends on: what must be true for the idea, claim, or roadmap item to work. If the input is a claim ledger from a fact-checking skill, carry its claims over directly. Label each assumption as desirability (do they want it), feasibility (can we build it), or viability (will it pay off).
   - Done when: every load-bearing claim in the input maps to at least one assumption, and none restates a fact already evidenced.

2. **Rank by evidence risk x test cost.** Score each assumption 1 to 5 on evidence risk (how little real evidence supports it) and 1 to 5 on test cost (time and money to get a signal). Sort descending by risk, then ascending by cost. Output the ranking as a table with both scores.

3. **Read `references/test-card-templates.md`.** Follow it to generate one Test Card per ranked assumption in the exact format: "We believe that [hypothesis]. To verify that, we will [experiment]. We are confident if [success metric/threshold]." Each card must name a concrete metric with a numeric threshold, not a vibe.

4. **Apply the cheapest-test-first rule.** For every assumption, check `references/ai-experiment-patterns.md` and propose the fastest evidence before the most expensive. Never recommend a build, paid campaign, or price test when a GSC query check, waitlist, or reply test could settle it first. Any escalation from weak to strong test is written as a follow-up card.

5. **Generate Learning Cards** for any test the user reports as completed, using the format in `references/test-card-templates.md`: "We believed [x]. We observed [y]. We learned [z], so we now believe [new]." Each ends with a decision (iterate, persevere, pivot, or kill), never a neutral summary.

6. **Output the backlog.** Deliver one paste-ready markdown document, grouped by evidence strength: "Strong-evidence tests" (commitment signals: pre-orders, fake-door pricing, payment) then "Weak-evidence tests" (interest signals: waitlists, GSC queries, interviews). Within each group, order cheapest first. Include the ranking table at the top and every Test Card, ready to paste into Notion or a board. No meta commentary about the process.

## Example

Input: "I think paid subscribers would pay for an AI agents job board section."

Output (excerpt):

| Assumption | Risk | Cost | Type |
|---|---|---|---|
| Paid subscribers want an agents job board | 5 | 2 | desirability |
| They will pay extra for it | 4 | 4 | viability |

**Test Card 1**
> We believe that paid subscribers want an AI agents job board. To verify that, we will add a fake-door link in the next issue and track clicks plus emails collected. We are confident if 5% of clicks submit an email.

Weak-evidence test first (fake-door link, day 1), escalating to a strong-evidence pre-order check at $5/month on day 14.
