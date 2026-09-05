---
name: newsletter-mission-canvas
description: "Adapt the Strategyzer Mission Model Canvas for solo newsletter creators: fill the nine blocks with beneficiaries, value propositions, channels, reader relationships, mission achievement metrics, resources, activities, partners, and costs, tag every fact as sourced, inferred, or ask, run a per-block gap analysis, and return up to ten prioritized 90-day actions labeled by income or reach goals. Use when the user says mission canvas, newsletter mission canvas, creator mission canvas, audit my newsletter business model, or mission model canvas for my Substack. Not for corporate business model canvases, fundraising decks, or paid-ad strategy."
---

# Newsletter Mission Canvas

Adapts the Strategyzer Mission Model Canvas (Steve Blank's Business Model Canvas variant for mission-driven organizations) for a solo newsletter creator. Output is a paste-ready markdown canvas, a per-block gap analysis, and 90-day actions tagged with Northstar labels.

## When to Use This Skill

- User says "mission canvas", "newsletter mission canvas", "creator mission canvas", "mission model canvas for my Substack", or "audit my newsletter business model"
- User supplies a newsletter URL, a description, or wants to be interviewed, and asks for a business/mission model review
- User runs the skill with no input: default audit of Product with Attitude

## Instructions

1. Read `references/block-definitions.md` in full before filling any block. Do not invent block structure; the 9 blocks and their newsletter meanings are defined there.
2. Pick the input mode:
   - URL: fetch it, extract facts about audience, offer, stack, and metrics.
   - Description: parse the user's text.
   - Interview: ask at most 8 questions, one per canvas block area, then proceed.
   - No input: load `references/pwa-default-facts.md` and audit Product with Attitude.
   Completion condition: you have at least one fact or an [ASK] tag for every block.
3. Fill all 9 blocks. Tag every fact `[SOURCED-from-user]`, `[INFERRED]`, or `[ASK]`. No untagged facts allowed.
4. Run gap analysis: for each block, state what exists, what is missing or unproven, and severity (critical / moderate / minor). Completion condition: all 9 blocks have a gap verdict, including "no gap" where warranted.
5. Produce up to 10 prioritized 90-day actions. Each action gets exactly one Northstar label: `2026-income` ($10K/mo goal) or `2027-reach` (100K subs by Dec 2027). Order actions by expected impact on the labeled Northstar. Completion condition: every action has a label, an owner-sized verb, and a measurable 90-day outcome.
6. Render output with the exact templates in `references/output-templates.md`: markdown canvas table, gap analysis, actions. Completion condition: output is paste-ready, every cell tagged, Northstar totals shown.

## Example

Input (default mode, no arguments): audit Product with Attitude.

Output: a 9-block canvas where "20K+ Substack subscribers" appears tagged `[SOURCED-from-user]`, "free-to-paid funnel exists on Substack" appears tagged `[INFERRED]`, and "sponsor pipeline status" appears tagged `[ASK]`, followed by the gap analysis and a 90-day action list such as "Launch referral program: 1,000 new subs in 90 days. [2027-reach]".
