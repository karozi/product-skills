---
name: value-prop-canvas-builder
description: "Build an evidence-backed Strategyzer Value Proposition Canvas for any product, AI tool, or feature from a URL, name, or description: research the vendor's claims for the Value Map, mine Reddit, Hacker News, G2, and forums for real user jobs, pains, and gains, tag every cell as sourced, inferred, or original, score AI-era factors like model dependency, credit pricing, and agent-readiness, and close with problem-solution, product-market, and business model fit verdicts. Use when the user says value prop canvas, VPC for X, build a value proposition canvas, or wants the pains and gains of X users mapped with citable evidence. Not for full business model audits, competitive teardowns, or fact-checking existing claims."
---

# Value Proposition Canvas Builder

Build a Strategyzer Value Proposition Canvas for any product, grounded in real evidence. Every cell carries an evidence tag. No invented quotes, no invented pains.

## When to Use

- The user names a tool/product (AI tools especially) and wants a VPC, value prop canvas, or user pains/gains research for it.
- Prepping Product with Attitude content that needs a defensible, citable canvas.

Not for: business model canvas audits, competitive dossiers, or verifying existing claims. Those route to the sibling `business-model-canvas-audit` skill or a dedicated fact-checking skill.

## Instructions

1. **Pin the target.** Extract the product name, URL (if any), and pasted description. Pick ONE specific customer segment, not "everyone." Ambiguous segment: state your assumption in the output's first line. Done when you have product + segment + starting URL or "no official site found."
2. **Research the Value Map side (vendor voice).** Fetch the official site, pricing page, and docs/changelog. Capture products & services, pain relievers, and gain creators exactly as the vendor claims them. Done when every Value Map claim traces to an official URL.
3. **Research the Customer Profile side (user voice).** Search Reddit, Hacker News, G2, Trustpilot, and niche forums for real users of this product. Pull jobs, pains, and gains in users' own words, keeping the source link for each. Done when jobs, pains, and gains each hold at least 3 [SOURCED] items from at least 2 distinct communities. If a cell stays thin after two search rounds, read `references/trigger-questions.md` and use those questions to widen the query set.
4. **Load the definitions.** Read `references/canvas-definitions.md` before filling any cell. It holds the exact Strategyzer field definitions, the evidence tag rules, and the AI-era factor rubric. Do not fill the canvas from memory.
5. **Fill the canvas.** Copy `assets/canvas-output-template.md` and fill every cell. Every entry is tagged `[SOURCED](url)`, `[INFERRED]`, or `[ORIGINAL]` per the rules in canvas-definitions.md. Score each cell for the four AI-era factors: model dependency, credit pricing, agent-readiness, vendor lock-in. Done when zero cells are untagged.
6. **Write the fit assessment.** Rate problem-solution fit, product-market fit, and business model fit (Strategyzer's three fits) with a verdict and cited cell evidence for each. One paragraph per fit, no fluff.
7. **Emit the For Machines JSON.** Fill `assets/for-machines-template.json` so the entry is ready to push to the user's machine-readable content index if one exists.
8. **Save and offer the chain.** Write the canvas, fit assessment, and JSON to a workspace file. Then, if the user has a table-publishing skill or site pipeline installed, offer to chain into it to ship the canvas as a structured page with Table JSON-LD. Otherwise offer the markdown and JSON for manual publishing.

Voice rule for all reader-facing output: direct, punchy, technically sharp, no corporate jargon, no em-dashes mid-sentence.

## Example

Input: `VPC for Cursor`

Output (excerpt of the canvas table):

| Customer Profile | Entry | Evidence | AI-era (model/credits/agent/lock-in) |
|---|---|---|---|
| Pain | "It forgets my project conventions mid-session" | [SOURCED](https://www.reddit.com/r/cursor/comments/...) | High/High/Med/Med |

Followed by the full six-cell canvas, the three fit verdicts, and the For Machines JSON entry.
