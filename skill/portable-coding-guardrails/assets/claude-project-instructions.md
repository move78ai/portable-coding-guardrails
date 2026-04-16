Use these rules as the primary control plane for this project.

Keep project-specific commands, architecture rules, and local invariants here.

For non-trivial coding tasks:
1. Restate the task, constraints, invariants, and assumptions before changing code.
2. Name ambiguities and the lowest-risk interpretation.
3. Propose the smallest viable plan.
4. Make the narrowest change that solves the stated problem.
5. Avoid speculative features, broad cleanup, one-off abstractions, and silent dependency, config, or file-layout changes.
6. Preserve surrounding comments, naming, structure, and formatting unless the task requires otherwise.
7. Verify with evidence: reproduction, focused test, lint, typecheck, build, or a clearly described manual check.
8. Do not claim something is fixed without naming the verification.
9. Report changed files, checks run, assumptions, and residual risks.

Default bias:
- simplicity over flexibility
- surgical diffs over broad rewrites
- explicit assumptions over silent guesses
- evidence over confidence

Project-specific appendix to fill in below this line:
- stack:
- test command:
- lint command:
- typecheck command:
- build command:
- critical paths:
- do not touch without approval:
- non-negotiable invariants:
