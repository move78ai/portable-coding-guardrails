# Demo transcript: fallback-only setup

## User request
Fix the failing JSON parse in `src/config/load.ts` without changing unrelated files.

## Context
Only the short global fallback is installed. No repo file. No project appendix.

## Expected weaker response pattern
- generic good behavior rules are present
- repo-specific commands are missing
- verification is weaker because test and lint commands are unknown

## What this demonstrates
The fallback prompt is useful for behavior hygiene, but too weak to serve as the main control plane for repo-specific work.
