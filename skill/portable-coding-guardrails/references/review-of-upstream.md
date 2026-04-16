# Upstream review

## What the upstream package gets right

1. The core idea is sharp.
2. The guidance is lightweight.
3. The principles are easy to reuse.
4. The package is small enough to copy quickly.

## What remains weak in the upstream package

1. The default install path still leans too global.
2. Repo-local commands and invariants do not have a first-class home.
3. Cross-platform exports are missing.
4. Publication collateral is missing.
5. Proof material is missing.

## Design response in this adaptation

1. Make repo-level and project-level surfaces the primary control plane.
2. Demote the account-global file to fallback-only.
3. Add platform-ready exports.
4. Add a project appendix template for real commands and invariants.
5. Add proof and launch material for public publication.
