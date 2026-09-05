# Postmortem: [Incident title]

Template for five-whys Facilitate mode. Fill every bracket. Roles, not people.

## Summary

- **Date and duration:** [when, how long]
- **Impact:** [users affected, revenue lost, trust spent — numbers where possible]
- **Status:** [detected / mitigated / resolved — and current state]

## Timeline

| Time | Event | Source |
|---|---|---|
| [t0] | [first cause, often visible only in hindsight] | [log / diff / ticket] |
| [t1] | [symptom became visible] | [alert / report] |
| [t2] | [response began] | [channel / page] |
| [t3] | [mitigated] | [action] |

## The chain(s)

### Chain 1

1. **Symptom:** [observable fact, no interpretation]
2. **Why 1:** [because ...] — evidence: [source]
3. **Why 2:** [because ...] — evidence: [source]
4. **Why 3:** [because ...] — evidence: [source]
5. **Why 4 (root, if reached):** [because ... — a system, process, or trade-off]
   — evidence: [source]

Add whys as needed; five is a guideline. Start a second chain for independent causes.

## Root cause (per chain)

[One sentence naming the system failure that made the chain possible.]

## Proportional fix plan

| Level | Fix | Type | Owner | Date |
|---|---|---|---|---|
| Symptom | [detection / rollback / blast-radius limit] | [alert / tool] | [role] | [date] |
| Process | [gate / checklist / runbook] | [process] | [role] | [date] |
| Root | [structural change] | [system] | [role] | [date] |

## What went well

[Detection, response, mitigation worth keeping. Postmortems that only list failures
teach teams to hide the next one.]

## Rules of order

- No names in causal statements — roles and systems only.
- Every "because" is checkable; unverifiable links are marked ASSUMPTION and tested
  before fixes ship.
- The meeting ends when every fix has an owner and a date.
