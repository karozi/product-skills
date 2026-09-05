# Blame Patterns and Causal Rewrites

Reference for five-whys. The difference between a blame answer and a causal answer is
the difference between a postmortem that fixes nothing and one that prevents the next
incident.

## The test

A causal answer names a mechanism that can be checked and fixed:

- Names a **role or system**, never a person.
- States a **condition** ("the alert went to a channel nobody watched"), not a
  character judgment ("nobody was paying attention").
- Is **verifiable** from evidence: logs, timelines, code, configurations.

## Common blame patterns and their rewrites

| Blame answer | What it hides | Causal re-ask |
|---|---|---|
| "Dave forgot to run the migration" | Why could forgetting break production? | "The deploy process permitted skipping a required step — why was it optional?" |
| "We were too busy to test" | Why did busy-ness allow untested releases? | "The release checklist had no gate on test coverage — why?" |
| "Someone misconfigured the flag" | Why was misconfiguration possible and silent? | "Config changes shipped without validation or review — why?" |
| "The on-call missed the page" | Why did the page require heroics? | "The alert fired at 3 AM with a runbook that didn't cover this case — why?" |
| "Communication breakdown" | Almost always a symptom, never a cause | "The two teams had no shared definition of done — why?" |
| "We didn't have time" | A choice, treated as physics | "The schedule made [quality step] the flexible item — why was it cut first?" |

## Stopping-point checks

The chain is done when the root cause is:

1. **Systemic** — a process, tool, gate, incentive, or missing check; not a person.
2. **Preventive** — fixing it makes the whole chain impossible, not just this
   symptom.
3. **Fixable** — within the team's power, or the escalation owner is named.

The chain stopped too early if the "root" is a who, a when, or a what that another why
could still open.

## Proportional investment

Ries's rule, operationalized: walk the chain top to bottom and size each fix to its
level.

- **Level 1 (symptom):** detection — alerting, rollback, blast-radius limit.
- **Level 2–3 (process):** checklist, gate, pairing, runbook update.
- **Level 4–5 (system/root):** structural change — architecture, ownership,
  incentives, tooling defaults.

A fix plan with only level-1 items or only a root fix is incomplete. Recurrence is
the audit: if the same root shows up again, the middle of the chain was left unfixed.

## Multiple chains

Incidents with compound causes (a deploy failure AND an alerting failure) get separate
chains, each run to its own root. Merging them produces one story and two unfixed
systems.

Source: Taiichi Ohno's Toyota practice as popularized for startups in Eric Ries, The
Lean Startup (2011), chapter 11 ("Adapt"); blameless-postmortem practice as
standardized across modern engineering organizations.
