# /audit-context

Audit what is actually loaded before risky work.

Input checklist:

- active project
- expected instruction files
- expected runtime guards

Output contract:

- loaded instruction files
- missing expected files
- current project root
- whether full runtime guard is installed or only context layer

Stop condition:

- stop after reporting gaps; do not invent missing guards
