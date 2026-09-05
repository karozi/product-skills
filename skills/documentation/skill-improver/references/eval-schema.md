# Trigger-Eval Results Schema

The JSON schema accepted by `scripts/improve_description.py --eval-results`. Produced
by skill-creator's `run_eval.py` (upstream) or by an agent testing a description
against realistic queries.

## Schema

```json
{
  "description": "the current description that was evaluated",
  "results": [
    {
      "query": "a user query the agent was given",
      "should_trigger": true,
      "triggers": 3,
      "runs": 5,
      "pass": true
    }
  ],
  "summary": {
    "passed": 8,
    "failed": 2,
    "total": 10
  }
}
```

## Field notes

- `should_trigger` — whether this query ought to load the skill. Mix roughly half
  true, half false; false-trigger detection is where most descriptions fail.
- `triggers` / `runs` — how many times the skill fired across repeated runs. Repeated
  runs matter: triggering is stochastic, and variance is signal (a skill that fires
  3/5 times on a should-trigger query has a flaky description).
- `pass` — `should_trigger == (triggers > runs / 2)` is the recommended rule.
- `summary.total` — must equal `len(results)`.

## History file schema (optional `--history`)

```json
[
  {
    "description": "previous description attempt",
    "passed": 7,
    "failed": 3,
    "total": 10,
    "results": ["...same result objects as above..."]
  }
]
```

History prevents the improver from repeating failed approaches and is accumulated
automatically by the script's JSON output (`history` key).
