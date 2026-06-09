# PROJECT_IDENTITY

Project identity comes before action.

Define before non-trivial work:

- active project
- working object
- root path
- intended files
- protected paths
- neighboring projects
- runtime, deploy, and secrets areas

Project bleed:

Project bleed is accidental transfer of assumptions, files, or actions across project boundaries.
It usually starts when nearby context is mistaken for the active project.

Pre-action checklist:

- what project is active now
- what object is really being changed
- what root path defines scope
- which files may change
- which paths are protected
- does this touch runtime, deploy, or secrets
- what is the rollback path

If any answer is unclear, stop and run preflight.
