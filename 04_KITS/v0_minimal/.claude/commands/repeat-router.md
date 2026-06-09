# /repeat-router

Classify repetition before continuing it.

Input checklist:

- repeated action or answer
- what changed since last attempt
- current evidence gap

Output contract:

- one label: no-progress, necessary-deepening, scene-shift, stale-instruction, or recovery-needed
- next bounded action

Stop condition:

- stop if the repetition has no new evidence target
