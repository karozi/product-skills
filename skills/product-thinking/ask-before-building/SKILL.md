---
name: ask-before-building
description: Turn an under-specified feature, change, refactor, or workflow into a decision-complete build brief. Use when the user asks to clarify an idea before implementation, be interviewed one decision at a time, or convert a rough request into a copy-ready prompt for another agent. Do not use when the requirements are already sufficient or the user wants immediate implementation.
---

# Ask Before Building

Clarify consequential decisions first. Then produce a build brief another agent can execute without guessing what the user meant.

## Operating Contract

- Inspect the conversation and available project context before asking questions. Read authoritative files such as `AGENTS.md`, requirements, ADRs, and relevant code only when they exist and are within scope.
- Ask only questions whose answers could materially change the outcome, scope, behavior, architecture, risk, release, or validation.
- Ask one question per turn and wait for the answer. Do not start implementation or draft the final brief while the interview is active.
- Keep an in-session decision ledger. Clarification is read-only by default: do not edit documentation, code, tasks, or repository state unless the user explicitly requests those changes.
- Never invent file paths, commands, product rules, or permissions.

## 1. Find the Decision Gaps

Identify the smallest set of choices an implementer cannot responsibly infer. Usually this is two to six decisions, but impact matters more than count.

Check, when relevant:

- intended outcome and user;
- in-scope behavior and explicit non-goals;
- placement in the existing flow or system;
- data, state, permissions, and integrations;
- failure, empty, loading, and recovery behavior;
- compatibility, migration, accessibility, privacy, and security;
- acceptance criteria, observability, rollout, rollback, and validation.

Rank gaps by impact and uncertainty. Ask the highest-impact unresolved question next. Skip anything already answered by project evidence, conversation context, or an established local convention.

If there are no consequential gaps, skip the interview and produce the build brief. If the request contains several independent deliverables or validation paths, clarify the first useful slice instead of manufacturing one oversized prompt.

## 2. Ask One Decision at a Time

Each turn should contain:

1. one direct question;
2. two to four clear, mutually exclusive options when options are useful;
3. a recommended choice with one context-based reason, or a short trade-off statement when no option is clearly better;
4. permission to answer with an option or a different preference.

Use this compact pattern:

```markdown
**Decision — [short label]**

[One precise question]

A. [Option]
B. [Option]
C. [Option]

**Recommendation:** B — [one-sentence reason].

Choose a letter or tell me what you prefer.
```

Do not force false choices merely to fill four slots. Do not bundle related questions into one turn.

After each answer:

- record the decision and its rationale in the session ledger;
- note any assumption or constraint it creates;
- remove questions that the answer makes irrelevant;
- surface conflicts with earlier answers or authoritative project files;
- if a decision changes, mark the earlier choice as superseded and revisit dependent choices.

If the user says "use your judgment," adopt the recommended option and label it as an assumption. If the user skips a decision, record the safest reasonable assumption and expose it in the final brief. Stop asking when an implementer can proceed without consequential product guessing.

## 3. Produce the Build Brief

Return one compact, copy-ready prompt in a fenced Markdown block. Use structure rather than compressing everything into one dense paragraph. Include only sections that add useful instructions:

1. **Objective:** the outcome to achieve and who it serves.
2. **Read first:** authoritative files or context that actually exist.
3. **Decisions and assumptions:** the final ledger, including delegated or skipped choices.
4. **Scope:** required behavior and explicit non-goals.
5. **Implementation requirements:** observable requirements; mention files or components only when project evidence supports them.
6. **Acceptance criteria:** testable conditions for completion.
7. **Validation:** project-appropriate checks, commands, fixtures, and manual scenarios. Use sanitized or test data unless real data is explicitly authorized and safe.
8. **Risk and release:** compatibility, migration, observability, rollout, or rollback requirements when relevant.
9. **Handoff:** what the implementing agent should report, including changed files, checks run, results, and unresolved risks.

Follow the user's instructions and repository rules for commits, deployment, documentation, and external actions. Do not add arbitrary restrictions. If project context is unavailable, say which paths, commands, or conventions the implementer must verify before editing.

When the work is too broad for one reliable handoff, produce phased briefs with clear boundaries and dependencies. Do not use paragraph count as a proxy for scope.

## Documentation

Persist decisions to requirements, ADRs, a README, or another project record only when the user asks for documentation or the active task already authorizes those edits. Preserve unrelated content. When replacing a durable decision, identify what was superseded and why.

## Credit

Adapted and expanded by [Karo Zieminski](https://productwithattitude.com/), Product with Attitude. The upstream MIT license is preserved in `LICENSE`.
