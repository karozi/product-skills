# Violation Taxonomy

Read this before flagging questions in Audit mode. Severity levels: fatal (the answer is
worthless), major (weakens the answer but some signal survives), minor (stylistic drift).

## FATAL

### 1. Pitching (PITCH)
Describing the solution before or inside the question. Once you pitch, every answer is a review of
your pitch, not a fact about their life.
- Detect: solution adjectives ("our new AI-powered..."), "I'm building X, does that sound
  useful?", any "let me show you".
- Fix: strip the pitch. Ask about the last time the underlying problem occurred.

### 2. Hypothetical (HYPOTHETICAL)
"Would you", "could you", "might you", "if we built". Futures are fiction; people answer what
makes them sound agreeable.
- Detect: would/could/might + verb; "if there were a tool that..."; "imagine if...".
- Fix: "When did you last [verb]?" or "What did you do the last time [problem]?"

### 3. Opinion fishing (OPINION)
"Do you think it's a good idea?" asks for a review, not a fact. Opinions are flattery with extra
steps.
- Detect: "do you think", "how do you feel about", "is it a good idea", "what's your take on
  [the idea/product]".
- Fix: ask about the last occurrence of the problem and what they actually did.

### 4. Future intent (FUTURE)
"Will you buy it?" "Would you sign up tomorrow?" Stated intent predicts behavior at roughly
coin-flip rates.
- Detect: "will you", "are you going to", "would you sign up / switch / pay".
- Fix: "What have you already paid for to fix this?" or "What would you have to cancel to make
  room for this?"

### 5. Leading (LEADING)
The answer is embedded in the question. "Don't you hate how slow onboarding is?" has one socially
acceptable reply.
- Detect: negation questions ("don't you...", "isn't it..."), emotionally loaded adjectives
  (hate, painful, annoying) attached to the topic, "wouldn't it be better if".
- Fix: neutral phrasing. "How's onboarding going for you right now?" then let them name the
  problem.

### 6. Solution talk (SOLUTION-TALK)
Asking them to spec your product. Feature requests are free; nobody is invoiced for them.
- Detect: "what features would you want", "should it have X or Y", "what would the dashboard
  look like".
- Fix: "What do you use today, and what do you do when it fails?" Their workaround is the spec.

## MAJOR

### 7. Compliment fishing (COMPLIMENT)
Fishing for validation: "what do you like about it so far?" Extracts niceness.
- Fix: "What's the last thing [this process] made you postpone or redo?"

### 8. Generic opener (GENERIC)
"What's your biggest pain point?" invites a canned, ranked, sanitized answer.
- Fix: "Walk me through the last time you [did the core activity]. Start to finish."

### 9. Cold workflow tour (TOUR)
"Tell me about your workflow" with no anchor event. Produces an idealized diagram, not reality.
- Fix: anchor to a specific recent instance ("the last one", "the one yesterday").

## MINOR

### 10. Vague quantity (VAGUE)
"How often do you..." — "often" means three times a year to some people and thirty to others.
- Fix: "How many times last month?"

### 11. Multi-barrel (MULTI-BARREL)
Two questions in one; only the interesting half gets answered.
- Fix: split, ask in sequence.

### 12. Interviewer-talk ratio (TALK)
Not a question but a flag: if the script has more talking points than questions, the interviewer
will pitch by accident. Cut narration to one line per section.
