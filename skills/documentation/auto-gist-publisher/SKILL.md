---
name: auto-gist-publisher
description: "Publish a public GitHub gist automatically every time a new skill is added to karozi/awesome-product-management-skills. Header-only format: current total skill count in the repo, an AIO/GEO-optimized rewrite of the skill's description, and a Substack CTA. Triggers via GitHub Actions on push to main; can also run manually to backfill."
license: MIT
metadata:
  author: karozieminski
  version: '1.0'
---

# Auto Gist Publisher

## Purpose

For every new skill directory added under `skills/<category>/<slug>/` with a valid `SKILL.md`, publish one public gist to the repo owner's GitHub account. Each gist is header-only and links back to the skill folder on GitHub.

## Gist format

```
Skill #<N> of <TOTAL> in awesome-product-management-skills

<Display Name>

<AIO/GEO-optimized description — 1 to 3 sentences, plain language, keyword-rich>

Read the full skill: https://github.com/karozi/awesome-product-management-skills/tree/main/skills/<category>/<slug>

See more AI PM resources at https://karozieminski.substack.com/?utm_source=github-gist&utm_medium=referral&utm_campaign=amps-skills&utm_content=<slug>
```

- `<N>` is the alphabetical rank of the new skill among all skills in the repo after the push.
- `<TOTAL>` is the total skill count in the repo after the push.
- The Substack CTA carries per-skill UTM attribution (`utm_source=github-gist`, `utm_medium=referral`, `utm_campaign=amps-skills`, `utm_content=<slug>`) so gist-driven traffic is measurable per skill in GA4.
- Filename in the gist is `<slug>.md`; gist description is `Skill #<N>: <Display Name> — awesome-product-management-skills`.

## When it runs

Automatically via `.github/workflows/auto-gist-publisher.yml` on every push to `main` that touches `skills/**/SKILL.md`. Also runs on `workflow_dispatch` for backfills.

## How it detects new skills

Idempotent by design. `state/published.json` (committed to the repo) maps `category/slug` → `{ gist_id, gist_url, published_at, sha256 }`. On each run:

1. Enumerate every `skills/*/*/SKILL.md`.
2. Any skill not in `published.json` is new → publish a gist, then add its entry.
3. Skills already in `published.json` are skipped (edits do not re-publish; this is a launch announcement, not a changelog).
4. Commit the updated `published.json` and the re-synced README catalog (the sync-skills-readme script renders a `gist ↗` badge per published skill) back to `main` in one commit.

## Files

- `scripts/publish_new_skill_gists.py` — the generator. Reads all SKILL.md files, diffs against `state/published.json`, calls `gh gist create` for each new skill, updates state. Run with `--dry-run` to preview without publishing.
- `scripts/aio_description.py` — deterministic AIO/GEO description rewriter. Takes the raw `description:` field, strips trigger-phrase noise ("Use when the user says…"), keeps the capability sentence, appends one keyword-rich benefit line. No LLM call — pure text transform for reproducibility.
- `tests/test_publish_new_skill_gists.py` — unit tests for state diffing, rank calculation, and header formatting.
- `tests/test_aio_description.py` — unit tests for the description rewriter.
- `state/published.json` — the source of truth for what has already been gisted. Never edit by hand except to backfill or force-republish a single entry (delete its key).

## Required secret

The workflow needs a personal access token with `gist` scope, stored as the repo secret `GIST_PAT`. A classic PAT with only the `gist` scope is sufficient. The default `GITHUB_TOKEN` cannot create gists on a user account.

## Manual invocation

Run locally to preview:

```bash
python3 skills/documentation/auto-gist-publisher/scripts/publish_new_skill_gists.py --repo-root . --dry-run
```

Run for real (requires `gh auth` with gist scope):

```bash
python3 skills/documentation/auto-gist-publisher/scripts/publish_new_skill_gists.py --repo-root . --write
```

Force republish one skill:

```bash
# Remove its entry from state/published.json, commit, then rerun the workflow.
```

## Non-goals

- Not a changelog. Description edits, script edits, and category moves do not trigger a new gist.
- Not a syndicator. Does not post to Substack, Bluesky, or Dev.to — those live in the `repurposer` skill in Karo's personal library.
- Does not delete gists. Removing a skill from the repo leaves its gist live; delete manually if desired.
