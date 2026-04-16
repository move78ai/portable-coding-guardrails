# CLAUDE.md

Use this file for repo-level Claude work.

Carry repo-specific commands and invariants here. Do not expect a short account-level memory to do that job.

## Default behavior

For non-trivial tasks:
1. Restate the task, constraints, invariants, and assumptions.
2. Propose the smallest viable plan.
3. Make the narrowest change that solves the stated problem.
4. Verify with evidence.
5. Report what changed, what was verified, and what remains uncertain.

For trivial one-line edits, stay concise but avoid hidden assumptions.

## Guardrails

### Clarify before coding
- Do not silently choose between materially different interpretations.
- If blocked, ask a focused question.
- If not blocked, state the lowest-risk assumption and proceed.
- Push back when a simpler approach exists.

### Prefer simplicity
- No speculative features.
- No one-off abstractions.
- No silent dependency, framework, or config additions.
- No broad rewrites when a local patch will do.

### Keep changes surgical
- Touch only code directly related to the request.
- Preserve adjacent comments, naming, formatting, and structure unless the task requires changes.
- Mention unrelated issues separately instead of folding them into the patch.
- Remove only dead code created by the edit.

### Verify instead of claiming
- Prefer reproduction plus tests for bug fixes.
- Otherwise run focused relevant checks: tests, lint, typecheck, build.
- If checks cannot run, say exactly what was inspected and why that is weaker.
- Never say fixed without naming the evidence.

## Project-specific appendix

Fill this in for the actual repo:
- stack:
- test command:
- lint command:
- typecheck command:
- build command:
- critical directories:
- do not touch without approval:
- non-negotiable invariants:
