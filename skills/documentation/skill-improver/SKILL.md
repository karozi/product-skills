---
name: skill-improver
description: "Validate every skill in a repository and improve existing ones: structural validation of SKILL.md files on push, description linting against Anthropic's skill-creator guidance, and LLM-driven description optimization from trigger-eval results. Use when adding or editing skills, when skill CI fails, when a skill undertriggers or fires on the wrong queries, or when the user says skill-improver, validate skills, lint my skills, improve this skill, or optimize skill triggering. Not for creating a brand-new skill from scratch with no existing draft."
---

# Skill Improver

Skills decay silently: descriptions stop triggering, bodies bloat, references rot. This
skill validates every skill in the repository on push and improves weak ones — forked
from Anthropic's official skill-creator (anthropics/skills, MIT), reduced to the two
parts that matter for an existing skill collection: validation and description
optimization.

## Modes

### Validate mode (default — CI run or user asks for a skill check)

1. Run `scripts/validate_skills.py --repo-root .` for the whole repository, or
   `--skill <dir>` for one skill.
2. Report errors and advisories as written. Errors block; advisories are advisory
   unless `--strict`.
3. Fix every error directly (structural problems are mechanical: name/folder mismatch,
   missing frontmatter keys, dead references, oversize bodies). For advisories, apply
   the guidelines in `references/description-guidelines.md` and rewrite the description.
4. Re-run until clean. A skill that cannot pass without changing its behavior gets
   reported, not silently patched.

### Improve mode (a skill triggers wrongly — undertriggers or false-fires)

1. Assemble trigger-eval evidence first. Either run skill-creator's `run_eval.py`
   (upstream, anthropics/skills) or generate results in the schema defined in
   `references/eval-schema.md` by testing the skill's description against realistic
   queries: 5-10 queries that should trigger, 5 that should not.
2. Read `references/description-guidelines.md` before touching the description.
3. Run `scripts/improve_description.py --eval-results <file> --skill-path <dir> --model <model>`
   — it calls `claude -p` and returns a new description plus accumulated history.
4. Apply the new description to SKILL.md, re-run the trigger evals, and repeat while
   the score improves. Stop after two non-improving iterations — the highest-scoring
   version wins, not the latest.
5. Never change a skill's body behavior while optimizing its description. Description
   edits change triggering only.

### Repair mode (a skill works but reads badly)

1. Diagnose against the skill-creator anatomy: under 500-line body, progressive
   disclosure (frontmatter + body + bundled resources), one clear job per skill.
2. Move heavy detail from the body into `references/` files with pointers saying when
   to read them. Add a table of contents to reference files over 300 lines.
3. Re-run validation. Structure repairs must not change triggering behavior — if the
   description must change, switch to Improve mode and get eval evidence first.

## Hard Rules

- Validation errors block a merge. No exceptions, no "I'll fix it later."
- Description optimization requires eval evidence. Never rewrite a description on
  vibes — an untested description is a regression waiting for a user.
- Generalize from trigger failures to intent categories; do not enumerate specific
  queries in the description (overfitting plus bloat).
- Descriptions are imperative, intent-focused, under 1024 characters, and carry a
  "Not for" boundary.
- The improve loop keeps the highest-scoring description, not the most recent one.

## Validation Checks (what CI enforces)

Errors: missing or invalid frontmatter; unexpected frontmatter keys; missing name or
description; name not kebab-case, over 64 characters, or not matching the folder; angle
brackets or over 1024 characters in the description; body over 500 lines or without
section headings; backticked file references that do not exist; SKILL.md files not
exactly two folders deep.

Advisories (errors under `--strict`): description under 40 or over 600 characters; no
imperative trigger phrasing; no negative boundary ("Not for ...").

## Credit

Validation forked from quick_validate.py and description optimization forked from
improve_description.py in [anthropics/skills](https://github.com/anthropics/skills)
(skill-creator, MIT). Adapted and extended by
[Karo Zieminski](https://productwithattitude.com/), Product with Attitude. The upstream
MIT license is preserved in `LICENSE`.
