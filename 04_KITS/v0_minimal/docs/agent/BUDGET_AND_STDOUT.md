# BUDGET_AND_STDOUT

Budget is a project resource.

Track before expensive work:

- context size
- files to read
- commands to run
- tool calls
- retries or review loops
- stdout volume

Rules:

- high-output commands must be bounded
- use scoped paths, quiet flags, head/tail, or logs
- do not run installs, builds, or wide scans without making cost visible first
- stop loops that do not target new evidence
