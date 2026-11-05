---
name: dev-tdd
description: 'Drive one step or behavior test-first: confirm the seam, write a failing spec, make the smallest production change, watch it pass, repeat. Use for "do this test-first", "TDD this behavior" or "red-green this fix". Called by go-work at its seams.'
---

# TDD

Report as the caller specifies; default `Done` / `Open` / `Changed`. Write no plan docs; return results in the reply.

## Rules

- Run specs only when the request or approved plan authorizes it; a later no-tests instruction wins.
- Follow [loop.md](references/loop.md): seams, vertical slices, red before green.
- Unit specs go through `go-ut`; e2e specs through `go-e2e`, only when the user or plan asks for e2e.
- Skip the loop for changes with no unit-testable behavior, such as pure styling, and say so.

## Workflow

For each behavior of the step (a direct request is one step):

1. Confirm the seam per `loop.md`: the step's `Test` names it. With no plan, return the seam as `Open` and proceed once the user confirms it.
2. Red: call `go-ut` to write one spec for that behavior and run it. When running is authorized, the red run is required even for a one-line fix: watch it fail for the right reason before touching production code. A spec for behavior the code already has may pass at once. With no unit test setup, `go-ut` reports `no unit test setup`: write and run no specs, and continue with 3.
3. Green: write the smallest production change that matches nearby code and only what that spec requires. Call `go-ut` to run the slice's focused spec; on a failure fix the code.
4. Repeat 1 to 3 for the next behavior. When the step's specs pass, report the step done with `Done` of at most 20 words.
