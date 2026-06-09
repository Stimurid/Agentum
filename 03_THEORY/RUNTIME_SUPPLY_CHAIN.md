# RUNTIME_SUPPLY_CHAIN

## What the supply chain is

An agent session is not just prompt in, answer out.
It is a chain:

- user request;
- approved instruction chain;
- repo documents and other untrusted data;
- memory surface;
- tool descriptions and executable surfaces;
- shell commands and file edits;
- outputs that may later become memory.

Each link can inject drift.

## Why it matters

If you protect only one link, the system still fails through another:

- safe prompt, dangerous tool call;
- good hook, poisoned memory;
- strong registry, fake-done output;
- careful runtime, bad target-install handoff.

## Operational consequences

- Map risk across the whole chain, not one classifier.
- Treat docs, tools, and memory as executable influence.
- Keep profiles and evals linked to specific chain breaks.
- Build proving-ground scenarios that cross multiple links.
