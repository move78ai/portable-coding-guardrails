# Expanded operating protocol

## A. Before editing

For non-trivial coding tasks, start by making the task legible:

1. Restate the request.
2. Identify constraints and invariants.
3. Name ambiguity.
4. Decide whether you are blocked.
5. Choose the smallest viable plan.

## B. During editing

Treat every change as if it must justify itself in a diff review.

- stay local
- preserve surrounding structure
- avoid speculative cleanup
- avoid adding flexibility unless the user asked for it
- avoid introducing new dependencies unless the requirement cannot be met without them

## C. Verification ladder

Use the strongest practical evidence available in this order:

1. reproduction test or failing case
2. focused test for the changed behavior
3. narrow lint, typecheck, or build
4. targeted manual inspection

If you only got to step 4, say so clearly.

## D. Final reporting

Report four things:

1. what changed
2. what evidence was gathered
3. what assumptions were made
4. what was noticed but deliberately left outside scope

## E. Trivial task mode

For obvious one-line edits:

- skip the long plan
- still avoid hidden assumptions
- still keep the diff narrow
- still mention the quick verification
