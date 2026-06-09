# WAVE_03_FAILURES_AND_POSTMORTEMS

This wave focused on failure classes rather than attractive design claims.

Key takeaways:

- broad or foreign prompts convert to damage fast if not cracked first;
- context-only safety illusion is a real failure mode;
- fake done, silent fallback, stdout burn, and project bleed are not cosmetic problems;
- subagent authority and memory authority fail in different ways and need different guards.

What this wave contributed:

- the logic behind `FAILURE_MODE_REGISTRY.yaml`;
- the bias toward routing, not only refusal;
- the insistence that evals must simulate mixed failures, not only one clean bad command.

Operational consequence:

Postmortem language belongs in registries and evals, not as decorative fear in runtime prompts.
