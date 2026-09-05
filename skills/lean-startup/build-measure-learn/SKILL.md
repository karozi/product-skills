---
name: build-measure-learn
description: "Run any product initiative through the build-measure-learn loop: define the learning first, pick the smallest experiment that produces it, decide how it will be measured before anything is built, and end every loop with a written learning. Use when planning features or experiments, when a team builds for months without learning checkpoints, when turning a roadmap item into an experiment, or when the user says build measure learn, BML loop, validated learning, smallest experiment, or plan the next loop. Not for execution management, sprint ceremonies, or initiatives with no falsifiable hypothesis at all."
---

# Build-Measure-Learn

The loop is the unit of startup work. Not the sprint, not the release, not the
quarter: the loop — hypothesis, smallest experiment, measurement, learning, repeat.
This skill plans, tracks, and retro-dicts loops. Its entire job is making sure no loop
starts with "build."

## The Loop

The loop is drawn learn-first: decide what you need to learn, design the smallest
experiment that teaches it, define how the result will be measured, build the minimum
to run the experiment, measure against the pre-declared threshold, write down what is
now believed and why, and let the learning pick the next loop.

A loop that starts with build produces a product in search of a question. That is the
failure mode this skill exists to prevent.

## Modes

### Plan mode (default — user brings an idea, feature, or initiative)

1. Force the hypothesis first: "We believe [action] will cause [measurable outcome]
   because [mechanism]." If the user cannot state one, help extract it — and if none
   exists, say so: the initiative is a bet, not an experiment, and gets flagged.
2. Identify what must be learned before anything is built, and pick the smallest
   experiment that produces it. Often the answer is a smoke test (smoke-test-launcher)
   or an MVP (mvp-type-selector), not a build.
3. Define the measure BEFORE the build: metric, baseline, threshold, date. "We'll
   figure out how to measure it later" is blocked — later never comes.
4. Copy `templates/loop-card.md`, fill every bracket, and set the loop's timebox.
   Loops have deadlines; open-ended loops become projects with better branding.

### Track mode (loops are running)

1. For each open loop, report only three things: what was built (one line), what the
   measurement says, and whether the threshold was met.
2. Flag stalled loops — built but unmeasured, measured but undecided, decided but
   unwritten. Each stall type has a different owner and the same cost: learning that
  evaporates.
3. A loop that outlives its timebox twice is closed as failed. Zombie loops consume
   the team's attention budget.

### Retro mode (loop completed or killed)

1. Read `references/loop-failures.md` for the failure taxonomy.
2. Answer the four retro questions: What did we believe? What did we measure? What
   actually happened? What do we now believe?
3. Classify the outcome: LEARNED (threshold question answered either way — a failed
   threshold is a successful loop), INCONCLUSIVE (measurement failed, not the
   hypothesis — the loop gets re-run with fixed instrumentation), or WASTED (no
   learning either way — name what made it wasteful; it is usually a skipped Plan-mode
   step).
4. The next loop is proposed from the learning, never from the backlog's old position.

## Hard Rules

- Learn before build, always. The first artifact of any loop is the hypothesis.
- The measure is defined before the build, or the loop does not start.
- A loop ends in a written, falsifiable learning. Unwritten learnings are opinions
  that will be re-litigated.
- Failed thresholds are successful loops. Killing a direction cheaply is the loop
  working as designed.
- Smallest learnable unit, not smallest shippable product — learning defines the
  size, not the roadmap.

## Output Shape (Retro mode)

```
Loop: [name] · Outcome: [LEARNED / INCONCLUSIVE / WASTED]
Believed: [hypothesis] · Measured: [metric vs threshold]
Happened: [result] · Now believe: [one falsifiable sentence]
Next loop: [one line]
```

Keep output in the user's language. Never close a loop without the "now believe"
sentence.
