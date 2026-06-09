# CONTEXT_ONLY_VS_RUNTIME_GUARD

## Core distinction

Instruction context influences behavior.
Runtime guard constrains behavior.

`AGENTS.md`, `CLAUDE.md`, READMEs, prompt notes, and style docs can reshape agent choices. They are powerful, but they do not physically stop tool use. A model can still read a perfect markdown rule and then execute the dangerous command anyway.

Stronger guard surfaces are:

- hooks;
- permissions;
- sandbox rules;
- approval gates;
- wrapper scripts;
- eval scenarios that test actual runtime behavior.

## Why the distinction matters

Without this distinction, teams start trusting text as if it were enforcement. That creates the context-only safety illusion: everybody feels safer because the markdown sounds good, while the runtime path is still open.

## Operational consequences

- Keep root and runtime docs compact.
- Put critical rules near the top.
- Do not claim a context file blocks anything by itself.
- Design v0 as a readable context layer plus honest skeleton guards.
- Test stronger surfaces before treating them as real protection.
