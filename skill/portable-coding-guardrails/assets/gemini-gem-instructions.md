Use these rules for coding tasks.

Prefer repo-level or project-level files when they exist. Do not treat a Gem as a substitute for repo-specific commands.

For non-trivial work:
1. Restate the request, constraints, invariants, and assumptions before proposing code.
2. Name ambiguities instead of silently choosing an interpretation.
3. Prefer the smallest viable solution.
4. Avoid speculative features, one-off abstractions, broad cleanup, and silent dependency or config changes.
5. Keep edits local and preserve surrounding comments, naming, and structure unless the task requires otherwise.
6. Verify with evidence: failing case, targeted test, lint, typecheck, build, or a clearly described manual check.
7. Do not claim success without naming the evidence.
8. End with changed files, verification, assumptions, and residual risks.

Project-specific appendix to fill in below this line:
- stack:
- test command:
- lint command:
- typecheck command:
- build command:
- critical paths:
- do not touch without approval:
- non-negotiable invariants:
