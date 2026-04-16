# Demo transcript: repo-first installation

## User request
Fix the failing JSON parse in `src/config/load.ts` without changing unrelated files.

## Repo file context
- test command: `pnpm test -- config/load.test.ts`
- lint command: `pnpm eslint src/config/load.ts`
- non-negotiable invariant: preserve current config shape and error wording unless the test requires otherwise

## Expected strong response pattern
- restates goal and invariant
- edits only `src/config/load.ts`
- runs the focused test first
- optionally runs lint on the changed file
- reports changed files, verification, assumptions, and residual risks

## What this demonstrates
The repo-level file carries the exact commands and invariants. The model does not need to guess.
