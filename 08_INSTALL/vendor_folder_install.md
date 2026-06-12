# vendor_folder_install

Use vendor-folder install when the target repo should own a local copy of the kit slice.

## Pros

- target repo owns its guard files
- easy local patching
- no cross-repo coupling at runtime

## Cons

- updates are manual
- drift is likely if provenance is not recorded

## Rules

- vendor only compact runtime files
- record source commit of `Agentum`
- rerun proving-ground after copy
- never vendor the full research archive
