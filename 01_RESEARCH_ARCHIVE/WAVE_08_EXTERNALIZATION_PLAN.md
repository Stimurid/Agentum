# WAVE_08_EXTERNALIZATION_PLAN

This wave addressed how the kit leaves the repository and enters a target project safely.

Key takeaways:

- copy, vendor-folder, and submodule installs have different coupling tradeoffs;
- environment capability audit should come before any target install;
- target install must never be automatic from `protected-agent-kit` without human review.

What this wave contributed:

- `08_INSTALL/*` as explicit install-path documentation;
- the profile-specific install guides in `05_PROFILES/*/INSTALL.md`;
- the target-install handoff prompt.

Operational consequence:

Externalization is a reviewed transfer process, not a command to spray files into nearby repos.
