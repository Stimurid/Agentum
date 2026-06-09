# CONTEXT_ONLY_VS_RUNTIME_GUARD

Instruction context influences behavior.
Runtime guards constrain behavior.

Context-only surfaces:

- `AGENTS.md`
- `CLAUDE.md`
- README files
- policy docs
- prompt notes

These can steer the model, but they do not physically stop tool use.

Stronger guard surfaces:

- hooks
- permissions
- sandbox rules
- approval gates
- wrapper scripts
- eval scenarios

v0_minimal starts with the context layer because it is portable and readable.
It must not pretend the context layer is sufficient by itself.
