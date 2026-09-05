---
name: five-whys
description: "Run root-cause analysis the Toyota way: ask why five times to reach the system failure behind a product or process incident, then invest a proportional fix at each level. Blocks blame answers and stops teams from fixing symptoms. Use after any incident, outage, missed release, quality regression, or repeated process failure, when writing a postmortem, or when the user says five whys, root cause, why did this happen, postmortem, or blameless analysis. Not for strategic decisions, metric analysis, or interpersonal conflict — those are not causal chains."
---

# Five Whys

Behind every seemingly human error is a system that allowed it. Five Whys walks the
causal chain from symptom to system root cause, then applies Ries's proportional
investment rule: a little fix at each level, a bigger fix at deeper levels. The
classic outcome: teams stop re-fixing the same incident forever.

## The Method

Ask "why?" iteratively. Each answer becomes the subject of the next why. Human error
is never an acceptable stopping point — if a person could make that mistake, the
system asked for it. The chain typically bottoms out at a process, a missing check,
or a trade-off someone made consciously.

## Modes

### Run mode (default — user describes an incident)

1. Read `references/blame-patterns.md` before asking the first why.
2. State the symptom as observed fact, no interpretation: what happened, when, blast
  radius.
3. Walk the whys one at a time. Each answer must be causal ("X because Y"), not
  blameful ("because Dave forgot"). Struck answers get re-asked until they are causal.
4. Stop when the chain reaches a system cause that, if fixed, makes the entire chain
  impossible — usually between three and six whys. Five is a guideline, not a quota;
  say so if the chain ends early or runs long.
5. For each level in the chain, assign a proportional fix: trivial for shallow levels,
  structural for the root. A chain of whys with a fix only at the bottom will recur.

### Facilitate mode (user is running the analysis live with a team)

1. Copy `templates/postmortem.md` as the working document.
2. Enforce rules of order: no names in causal statements (roles, not people); every
  "because" must be checkable against evidence; parking-lot tangents instead of
  derailment.
3. When the room diverges into multiple chains, split them and run each to its root —
  incidents often have two or three independent causes, and merging them into one
  story hides fixes.
4. Close with the proportional-investment plan, owners, and dates. An analysis
  without owners is a ritual.

### Postmortem mode (user pastes an existing postmortem or RCA document)

1. Audit the chain: number each why. Classify each as CAUSAL, BLAME (person-shaped),
  or UNSUPPORTED (asserted without evidence).
2. Check the stopping point: does the root fix, if applied, actually prevent the
  symptom? If not, the chain stopped too early.
3. Check proportionality: fixes only at one level, or fix-sized excuses ("reminded
  everyone to be careful") get flagged.
4. Output the corrected chain and the missing fixes.

## Hard Rules

- Blame whys are struck and re-asked. "Human error" is the beginning of the analysis,
  never its conclusion.
- Every causal link must be verifiable from evidence — logs, timeline, diffs. "We
  assume" gets marked as an assumption, and assumptions get tested before fixes ship.
- Proportional investment: the depth of the five whys sets the size of the fix at
  every level (Ries: "make a proportional investment in each level"). A root-cause
  fix with no shallow-level fixes leaves the next different failure unprotected.
- If the same root cause appears in two postmortems, the previous fix was theater —
  say so.

## Output Shape (Postmortem mode)

| # | Why stated | Class | Evidence | Corrected |
|---|-----------|-------|----------|-----------|

Followed by root-cause verdict, proportionality check, and fix plan with owners.
Keep output in the user's language.
