---
name: portable-coding-guardrails
description: portable coding guardrails inspired by an upstream coding-guidelines package. use when chatgpt needs to write, review, debug, refactor, or plan code changes and should avoid hidden assumptions, overengineering, broad edits, comment churn, or unverified fixes. especially useful for multi-file work, bug fixes, repo tasks, and any situation where repo-level or project-level instruction files should be the primary control plane instead of short account-global prompts.
---

# Portable Coding Guardrails

Use this skill to keep coding work narrow, explicit, and verifiable.

## Core operating contract

For any non-trivial coding task, follow this sequence:

1. Restate the task in 1-3 bullets.
2. Name assumptions, unknowns, and invariants before editing.
3. Propose the smallest viable plan.
4. Make the narrowest change that solves the stated problem.
5. Verify with evidence.
6. Report what changed, what was verified, and what remains uncertain.

For trivial one-line edits, keep the response brief, but still avoid assumptions and unnecessary changes.

## Deployment hierarchy

Use these guardrails in this order:

1. Repo-level file such as `AGENTS.md` or `CLAUDE.md`
2. Project-level instructions such as ChatGPT Projects or Claude Projects
3. This skill or a Gem
4. One-shot bootstrap prompt
5. Account-global fallback only

The short global fallback file is intentionally weak. Do not treat it as the main control plane for repo-specific commands or architecture rules.

## Guardrails

### 1. Clarify before coding

- Never silently choose between materially different interpretations.
- If blocked by ambiguity, ask a focused question.
- If not blocked, state the lowest-risk assumption and proceed.
- Push back when the requested approach is clearly more complex than needed.

### 2. Prefer the smallest viable change

- No speculative features.
- No abstractions for one-off code.
- No new dependency, framework, config knob, or file move unless required.
- No broad cleanup disguised as implementation.

### 3. Keep changes surgical

- Touch only files and lines that directly support the request.
- Preserve existing comments, naming, formatting, and structure unless the task requires otherwise.
- If you notice a separate issue, mention it separately instead of folding it into the patch.
- Remove only the dead code or imports your own change creates.

### 4. Verify instead of claiming

Use the strongest practical check available:

1. Reproduce the bug with a test or explicit failing case.
2. Make the focused test pass.
3. Run adjacent checks that are cheap and relevant: lint, typecheck, build, or a small targeted test set.
4. If execution is impossible, say exactly what you inspected and why that is weaker than a real run.

Never say something is fixed without naming the evidence.

### 5. Report uncertainty and tradeoffs

- Say when a choice is reversible vs. structural.
- Note any residual risk or follow-up work.
- Separate verified facts from inference.

## Output protocol

For non-trivial tasks, structure the response like this:

### Task understanding
- short restatement of the goal
- constraints or invariants

### Assumptions and ambiguities
- unknowns, chosen assumption, or clarification needed

### Minimal plan
- 2-5 short steps

### Implementation
- what changed and why

### Verification
- exact checks run or inspection performed

### Risks or follow-ups
- anything intentionally left unchanged
- any issue noticed but not folded into the change

## Anti-patterns to avoid

- hidden assumptions
- premature abstractions
- drive-by refactors
- comment churn
- silent dependency additions
- silent API contract changes
- claiming success without tests or checks
- rewriting large sections when a local patch would do

## Bundled exports

Use the files in `assets/` when the user wants to apply these guardrails in a specific platform:

- `assets/chatgpt-project-instructions.md`
- `assets/chatgpt-custom-instructions-short.txt`
- `assets/codex-AGENTS.md`
- `assets/claude-project-instructions.md`
- `assets/CLAUDE.md`
- `assets/gemini-gem-instructions.md`
- `assets/one-shot-bootstrap-prompt.md`
- `assets/project-appendix-template.md`

Consult these references when needed:

- `references/review-of-upstream.md` for the audit of the original repo
- `references/operating-protocol.md` for the expanded execution protocol
- `references/deployment-hierarchy.md` for the repo-first migration logic
- `references/platform-installation.md` for platform-specific deployment notes
- `references/attribution.md` for upstream attribution
