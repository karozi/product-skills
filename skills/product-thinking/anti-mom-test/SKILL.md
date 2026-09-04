---
name: anti-mom-test
description: "Audit and rewrite customer discovery interview questions so they pass the Mom Test: past behavior over future intent, their life over your idea, specifics over hypotheticals. Use when reviewing or writing user interview scripts, discovery call outlines, or sales discovery questions, or when the user says anti-mom-test, mom test check, fix my interview questions, or pastes interview questions for review. Not for large-scale survey design or usability testing."
---

# Anti-Mom-Test

Customer interviews fail predictably. People are nice, founders are hopeful, and the result is a
transcript full of polite fiction. This skill enforces the Mom Test (Rob Fitzpatrick) on any
interview question, script, or debrief.

## The Three Rules

1. Talk about their life, not your idea.
2. Ask about specifics in the past, not generics or opinions about the future.
3. Talk less, listen more.

A question passes only if it asks about something that already happened and did not plant the
answer.

## Modes

### Audit mode (default — user pastes questions or a script)

1. Read `references/violation-taxonomy.md` before flagging anything.
2. Number every question in order.
3. Flag each violation: question number, violation type, severity (fatal / major / minor), one-line
   why, and the rewritten question.
4. Score the script: percentage of questions passing, plus verdict — "Ship it" (80%+ passing),
   "Fix first" (50–79%), or "Burn it down" (below 50%).
5. Finish with the 3 highest-signal questions the script is missing, drawn from the interview
   guide's core sections.

### Guide mode (user wants an interview guide from a hypothesis or feature idea)

1. Confirm the hypothesis and target interviewee if not stated; do not invent them.
2. Copy `templates/interview-guide.md` and fill every bracket.
3. Every question must target past behavior or actual spend (money, time, workaround). Delete any
   question that fails this test.

### Debrief mode (user pastes a transcript or interview notes)

1. Classify every claimed insight: FACT (specific past behavior), SIGNAL (stated emotion or
   priority), or NOISE (compliments, hypothetical intent, future promises).
2. Quotes go in the output with their classification — no paraphrasing into softer claims.
3. End with "Still unknown" (open questions) and the next 3 questions to ask.

## Rewrite Rules

- "Would you..." → "When did you last..."
- "Do you think..." → "Walk me through the last time..."
- "How often do you..." → "How many times last month..."
- "Would you pay for..." → "What have you already spent money or time on to fix this?"
- Never describe the solution before the problem questions are done.
- Commitment test: interest is opinions. Commitment is time, money, reputation, or a scheduled
  next step. Only commitment counts as evidence.

## Output Shape (Audit mode)

| # | Question | Violation | Severity | Rewrite |
|---|----------|-----------|----------|---------|

Followed by score, verdict, and the 3 missing questions. Keep rewrites in the user's language.
Never soften a fatal violation to major — hypotheticals and pitches are fatal even when politely
phrased.
