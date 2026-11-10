---
name: dev-tdd
description: 'Drive one step or behavior test-first: confirm the seam, write a failing spec, make the smallest production change, watch it pass, repeat. Use for "do this test-first", "TDD this behavior" or "red-green this fix". Called by go-work at its seams.'
---

# TDD

Report as the caller specifies; default `Done` / `Open` / `Changed`.

## Rules

- Run specs only when the request or plan authorizes it; the newest instruction wins, so a request to run named specs authorizes exactly those runs, even when an earlier plan says not to run tests.
- Follow [loop.md](references/loop.md): seams, vertical slices, red before green.
- Unit specs go through `go-ut`; e2e specs through `go-e2e`, only when the user or plan asks.
- Skip the loop for changes with no unit-testable behavior, such as pure styling, and say so.
- A failing spec means the code is wrong: fix the code, never edit the spec to match it.
- Weaken or change an existing assertion only when the expected behavior changed per the plan or user, and say why in `Open`.

## Workflow

Per behavior of the step (a direct request is one step):

1. Confirm the seam per `loop.md`. The step's `Test` names it; with no plan, return it as `Open` and proceed once confirmed.
2. Red: call `go-ut` to write one spec; its focused run is the red run, so run nothing else.
   - When running is authorized, the red run is required even for a one-line fix: watch it fail for the right reason before touching production code. A spec for behavior the code already has may pass at once: run it once, never rerun it before the fix, and put `red not observed` in `Open`.
   - `no unit test setup`: write and run no specs; continue with 3.
3. Green: write the smallest production change, matching nearby code, that the spec requires. Run the spec only after `git diff` shows the change landed; never chain an edit and a run with `;`. Call `go-ut` to run the focused spec; on failure fix the code and rerun until it passes. A production defect that `go-ut` reports is fixed here, not passed up.
4. Repeat for the next behavior.
5. When the step's specs pass, report it done with `Done` of at most 20 words. Name the spec that failed before and the run that passed after; when red was not observed, `Open` says so.
