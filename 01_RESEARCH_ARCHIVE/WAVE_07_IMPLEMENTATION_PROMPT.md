# WAVE_07_IMPLEMENTATION_PROMPT

This wave preserved the logic for asking another agent to implement the kit without causing the original failure class again.

Key takeaways:

- handoff must come after corpus preservation;
- implementation prompts need scope limits, file targets, and non-goals;
- "work in a big batch" is useful only if boundaries are explicit.

What this wave contributed:

- the handoff prompt family in `07_HANDOFF_PROMPTS`;
- the preference for Russian paste-ready operational prompts;
- the rule that handoff must request diffs and local verification, not theatrical completion.

Operational consequence:

A good implementation prompt is a bounded transfer, not an invitation to improvise empire.
