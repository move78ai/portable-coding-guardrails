# Demo scenarios

## Demo 1: narrow bug fix

Goal:
- request one bug fix in one file

Desired evidence:
- one-file or minimal-file change
- focused verification
- residual risk named explicitly

## Demo 2: ambiguous feature request

Goal:
- request a feature with two plausible interpretations

Desired evidence:
- ambiguity surfaced before editing
- lowest-risk interpretation named
- diff kept narrow

## Demo 3: fallback-only failure case

Goal:
- run the same request with only the account-global fallback in place

Desired evidence:
- weaker repo knowledge
- weaker verification specificity
- no false claim that the fallback is enough for repo-local rules

## Demo 4: appendix-powered improvement

Goal:
- run the same request after real commands and invariants are filled into the appendix

Desired evidence:
- commands referenced correctly
- protected paths respected
- final report anchored to actual repo checks
