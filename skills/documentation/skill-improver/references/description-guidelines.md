# Description Guidelines

Distilled from Anthropic's skill-creator guidance and its description-optimization
prompt. Read before writing or rewriting any skill description.

## What a description is

The description is the primary triggering mechanism. The agent sees only the name and
description when deciding whether to load a skill — the body is read only after the
decision. A description is a classifier you are writing for a model, not marketing copy.

## The rules

1. **Imperative form.** "Use when reviewing dashboards" — not "this skill audits
   dashboards."
2. **Intent over implementation.** Describe what the user is trying to achieve, not how
   the skill works internally. Modes, scripts, and file layouts are body material.
3. **Pushy on purpose.** Agents undertrigger by default. Skill-creator explicitly
   recommends erring toward "use this whenever the user mentions X, even if they don't
   say the word X."
4. **Both sides of the boundary.** State when to use it AND when not to
   ("Not for ..."). A description without a negative boundary will false-trigger on
   adjacent requests.
5. **Under 1024 characters, hard limit.** Aim for 100–200 words. Over-length
   descriptions get truncated and the truncation happens exactly where the boundary
   clause lives.
6. **No angle brackets.** `<` and `>` break the frontmatter ecosystem.
7. **Generalize, never enumerate.** If the skill fails on specific queries, do not add
   those queries to the description — describe the broader intent category they belong
   to. Enumerated trigger lists overfit and bloat.

## Structure that works

```
[What it does in one clause]. Use when [trigger contexts: situations, phrases,
adjacent phrasings the user might use instead of the skill's name]. Not for
[adjacent territory it must not fire on].
```

## Red flags

- Third-person capability list ("This skill provides ...") — no trigger semantics.
- Implementation detail ("Uses a 12-type taxonomy with severity grading") — body
  material, wasted trigger space.
- No "Not for" clause — the skill will fire on its nearest neighbors.
- Over ~600 characters — check whether enumerated examples can be generalized.
- Restating the name — the agent already knows the name.

## The improvement loop

1. Gather trigger evals: 5–10 should-trigger queries, 5 should-not-trigger queries.
2. Run the improve script (or rewrite by hand following these rules).
3. Re-evaluate. Keep the highest-scoring description across iterations, not the latest.
4. Stop after two non-improving iterations — you are overfitting the test set.

Source: anthropics/skills, skill-creator (SKILL.md writing guide and
improve_description.py prompt), MIT.
