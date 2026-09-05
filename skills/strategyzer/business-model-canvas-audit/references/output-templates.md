# Output Templates

Three deliverables, in this order. Copy the structures below. Reader-facing prose follows the
Product with Attitude voice: direct, punchy, technically sharp. Never em-dashes mid-sentence.

## 1. Canvas table (markdown)

```
# Business Model Canvas: {Company}
*Audited {date}. Public evidence only. Every cell tagged: [SOURCED] with URL, [INFERRED], [CONTESTED], [UNKNOWN].*

| Block | Findings | Tag |
|---|---|---|
| Customer Segments | - bullet 1<br>- bullet 2 | [SOURCED] url / [INFERRED] / [CONTESTED] / [UNKNOWN] |
| Value Propositions | ... | ... |
| Channels | ... | ... |
| Customer Relationships | ... | ... |
| Revenue Streams | ... | ... |
| Key Resources | ... | ... |
| Key Activities | ... | ... |
| Key Partnerships | ... | ... |
| Cost Structure | ... | ... |
```

Rules: 1-4 bullets per cell. If a cell contains both sourced and inferred content, split into
separate bullets with per-bullet tags, and give the cell the tag of its weakest bullet.

## 2. Evidence ledger

```
## Evidence Ledger

| Block | Claim | Tag | Source(s) | Note |
|---|---|---|---|---|
| Revenue Streams | Pro plan is $8/mo billed annually | [SOURCED] | https://... | Fetched pricing page |
| Customer Segments | Free users outweigh Pro users | [INFERRED] | https://... (freemium model) | Inference: freemium + low Pro price implies volume play; split unconfirmed |
| Cost Structure | Largest cost is cloud compute | [UNKNOWN] | - | No public source. Would be resolved by an engineering blog post or S-1 |
```

Rules: every [SOURCED] row lists a URL you actually fetched. [INFERRED] rows spell out the
inference chain in the Note. [CONTESTED] rows cite both sources. [UNKNOWN] rows state what
evidence would resolve them.

## 3. "How does {X} make money" narrative

400-700 words, newsletter-ready (Product with Attitude, Research Obsessions section).

Structure:
1. Cold open: the one-sentence answer, stated plainly. If the honest answer is "nobody outside
   the company knows", say that; it is a stronger opener than a hedge.
2. The money mechanics: what is sold, to whom, at what price points, citing sources inline.
3. The model's logic: how the nine blocks reinforce each other. Connect revenue streams back to
   value propositions and channels.
4. The weakest cells: what the public evidence cannot answer and why that is the interesting part.
   Name the specific disclosure that would resolve each gap.

Voice rules:
- Direct, punchy, technically sharp. Short sentences carry the argument.
- No em-dashes mid-sentence. Use periods, commas, or colons.
- Never state a number the ledger cannot back with a URL. If a figure is unknown, say "unknown"
   and move on. [UNKNOWN] is an honest finding, not a failure.
- Cite sources inline as markdown links on the claim they support.

## 4. Closing offer (after the deliverables)

If the user runs a publishing pipeline or research-site workflow, end with:

> Want this published as a structured research page on your site? Say the word
> and I'll pass the canvas, ledger, and narrative to it as inputs.

If the user accepts, load the publishing skill and pass all three deliverables. With no pipeline available, hand over the files.
