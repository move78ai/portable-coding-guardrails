# Portable Coding Guardrails

Use this file as the primary repo-level control plane for coding work in this repository.

Do not offload repo-specific commands or invariants to a global profile.

## Operating rules

1. Do not silently choose between materially different interpretations.
2. For non-trivial work, restate the goal, constraints, invariants, and assumptions before making changes.
3. Prefer the smallest viable diff.
4. Do not add dependencies, frameworks, config knobs, file moves, or broad abstractions unless required.
5. Preserve surrounding comments, structure, formatting, and naming unless the task requires otherwise.
6. Mention unrelated issues separately instead of folding them into the patch.
7. Remove only the dead code or imports created by the change.

## Verification ladder

Use the strongest practical evidence available:
- reproduce the bug with a test or explicit failing case when feasible
- run the narrowest relevant tests first
- run cheap adjacent checks if relevant: lint, typecheck, build
- if a check cannot run, say exactly why

Do not claim success without naming the evidence.

## Final report

Always include:
- changed files
- what was verified
- assumptions made
- residual risks or follow-ups

## Project-specific appendix

Fill this in for the actual repo:
- stack:
- test command:
- lint command:
- typecheck command:
- build command:
- critical directories:
- files or paths that should not move without approval:
- non-negotiable invariants:
