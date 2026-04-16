# Deployment hierarchy

## Primary rule

Use the strongest local surface available.

## Order

1. Repo-level files
2. Project-level instruction surfaces
3. Skills or Gems
4. One-shot bootstrap prompts
5. Account-global fallback

## Why this order holds

Repo-level and project-level surfaces carry the information that actually changes coding outcomes:

- test commands
- lint commands
- typecheck commands
- build commands
- protected paths
- architecture constraints
- local invariants

A tiny account-global file should not carry all of that.

## Practical interpretation

Use a repo file when the model is working inside a specific repository.

Use a project surface when repo files are unavailable or when the platform cannot see the repo directly.

Use a Skill or Gem for portable behavioral rules.

Use a one-shot bootstrap prompt for disposable sessions.

Use the account-global fallback only when nothing stronger is available.
