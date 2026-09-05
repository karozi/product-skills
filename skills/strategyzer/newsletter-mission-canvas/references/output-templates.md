# Output templates

Render all three sections, in this order, in one markdown response. Replace bracketed placeholders. Keep every fact tag and Northstar label intact.

## Template 1: Canvas table

```markdown
# [Newsletter name] Mission Canvas

| Block | Contents |
|---|---|
| **Beneficiaries** | [Free readers: ...] [SOURCED-from-user] · [Paid subscribers: ...] [ASK] · [Sponsors/partners: ...] [INFERRED] |
| **Value Propositions** | [Per beneficiary, one line each, tagged] |
| **Channels** | [Substack: ...] · [SEO/GEO: ...] · [Social: ...] · [Community: ...] [each tagged] |
| **Reader Relationships** | [Trust mechanics per beneficiary, tagged] |
| **Mission Achievement Metrics** | [Subscriber growth: ...] · [Free-to-paid conversion: ...] · [Revenue: ...] [each tagged] |
| **Key Resources** | [Tagged list] |
| **Key Activities** | [Tagged list] |
| **Key Partnerships** | [Partner: motivation, tagged] |
| **Costs** | [Money costs] · [Time costs, hrs/week] [tagged] |
```

Rules: no empty cells; write "Unknown [ASK]" instead. Facts stay tagged even mid-cell.

## Template 2: Gap analysis

```markdown
# Gap Analysis

| Block | Exists | Missing or unproven | Severity |
|---|---|---|---|
| Beneficiaries | [What is known and working] | [What is missing, vague, or unverified] | [critical / moderate / minor / none] |
| ...all 9 rows... |
```

After the table, add one short paragraph: the single biggest gap, and why it blocks a Northstar.

## Template 3: 90-day actions

```markdown
# 90-Day Actions

| # | Action | 90-day measurable outcome | Northstar |
|---|---|---|---|
| 1 | [Verb-first action] | [Number and unit by day 90] | 2026-income |
| 2 | ... | | 2027-reach |

**Northstar totals:** [N] actions toward $10K/mo (2026-income) · [M] actions toward 100K subs by Dec 2027 (2027-reach)

## Open questions
- [Each [ASK] worth resolving, as a question to the creator]
```

Rules for actions:

1. Maximum 10 actions. Prioritize by expected impact on the labeled Northstar.
2. Every action starts with a verb and ends with a measurable 90-day outcome (a number, a rate, or a shipped artifact).
3. Exactly one Northstar label per action: `2026-income` or `2027-reach`. No unlabeled actions.
4. Actions must trace to a gap from Template 2. If an action has no gap behind it, cut it.
```
