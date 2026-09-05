---
name: business-model-canvas-audit
description: "Reconstruct any company's Business Model Canvas from public evidence: research pricing pages, SEC filings, funding announcements, job posts, and founder interviews, fill all nine official Strategyzer blocks, tag every cell as sourced, inferred, contested, or unknown, build a provenance ledger, flag the weakest-evidence cells as the real story, and write a newsletter-ready how-does-X-make-money narrative. Use when the user says BMC audit, business model canvas for X, how does X make money, or reconstruct and map X's business model. Never invents revenue, pricing, or user counts. Not for private financials, internal strategy sessions, or non-company entities."
---

# Business Model Canvas Audit

Reconstruct any company's Business Model Canvas from public evidence, with a provenance tag on every cell.

## When to Use This Skill

- User asks for a "BMC audit", "business model canvas for X", "reconstruct/map X's business model", or "how does X make money"
- Input is a company name, a URL, or a pasted description of a company

## Hard Rules

1. Never invent numbers. No revenue, user counts, pricing, valuation, or headcount unless a fetched source states them. If unknown, write [UNKNOWN] and name the evidence that would resolve it.
2. Every cell carries exactly one tag:
   - [SOURCED] + URL: a fetched source states it. Search snippets do not count; fetch the page.
   - [INFERRED]: no source states it, but it follows from sourced evidence. Write the inference chain in the ledger.
   - [CONTESTED]: fetched sources conflict. Cite both sides in the ledger.
   - [UNKNOWN]: no evidence, no defensible inference. Not blank; labeled.
3. No em-dashes mid-sentence in reader-facing output.

## Instructions

1. Identify the company. From a URL or pasted description, resolve the legal entity, flagship product, and market. Done when you can state all three in one sentence.
2. Read `references/bmc-blocks.md` for the 9 block definitions and per-block guiding questions. Use the official Strategyzer block names verbatim; do not rename, merge, or reorder blocks.
3. Research the public footprint. Read `references/research-checklist.md` and work every applicable source class: pricing pages, app-store listings, funding announcements, SEC filings if public, job posts, founder interviews, press. Batch searches; record every promising URL. Done when each block has candidate evidence or the checklist is exhausted.
4. Fill all 9 blocks. Per cell: 1-4 bullets, then tag it per the Hard Rules. A cell with no sourced content and no defensible inference is [UNKNOWN], never empty.
5. Build the evidence ledger: one row per cell (block, claim, tag, source URLs, note). Every [SOURCED] URL must have been fetched, not skimmed from a snippet.
6. Flag the weakest cells. Name the 2-3 cells that are [INFERRED], [UNKNOWN], or [CONTESTED], why they resist outside analysis, and what disclosure would resolve them. This is the interesting story; lead the writeup with it.
7. Produce the three deliverables using `references/output-templates.md`:
   a. Markdown canvas table, all 9 blocks, tagged
   b. Evidence ledger
   c. "How does X make money" narrative, 400-700 words, newsletter-ready: direct, punchy, technically sharp, no em-dashes mid-sentence, every factual claim sourced.
8. Offer the chain: ask whether to publish the audit as a structured research page on the user's own site (on Karo's setup, a Research Obsessions dossier via her serp-to-dossier skill). If a publishing pipeline is available and accepted, load it and pass the canvas, ledger, and narrative as inputs. Otherwise hand over the three deliverables as files.

## Example

Input: "How does Raycast make money?"

Output: a tagged 9-block canvas (Revenue Streams: "Raycast Pro subscription, $8/month billed annually [SOURCED] raycast.com/pricing"), the evidence ledger, a 500-word narrative, a weakest-cells section flagging that the free-vs-Pro user split is [UNKNOWN] and would need an official user-count disclosure, and the dossier offer.
