# AGENTS.md — protected-agent-kit

This repository is the source library for protected coding-agent and persona-agent practice.

Critical rules first:

- Treat `protected-agent-kit` as infrastructure, not as a target application repo.
- Do not install this kit into Litops, ModerBober, WhiteCrow, Quinta, or any other target repo unless the current task explicitly shifts to a reviewed install profile.
- Preserve corpus provenance, registries, pattern lineage, failure modes, install profiles, eval scenarios, and handoff prompts.
- Do not collapse the research archive into a single runtime prompt.
- Do not rewrite registries without a concrete consistency reason.
- Large bounded batches are allowed here; avoid forced microtasking when the user asks for a larger bounded pass.
- “Stop microtasking” never means rewrite-everything.
- Validate before commit.
- Do not claim done without checks, diffs, or honest status.
- Russian handoff prompts are the default. Technical file names and command names may remain in English.
- Persona humor fragments must stay separate from dry guard/runtime enforcement files.

Working rules:

- Name the working layer before editing: root docs, corpus, theory, v0 kit, persona fragments, profiles, install docs, evals, handoff prompts.
- Prefer compact, operational docs over archival bloat.
- Commit only after local checks pass and staged content is clean.
