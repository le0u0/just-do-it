# The Loop

The project's own test rules win where they conflict. Read this before the first spec and consult it each cycle.

## Seams

A seam is the public boundary a test observes behavior at: the interface where you see behavior without reaching inside. Tests live at seams, never against internals.

Test only at seams the user confirmed: those in the plan's `Testing` section (approved with the plan), or, with no plan, seams returned as `Open` and confirmed. You can't test everything; agreeing seams first puts effort on critical paths and complex logic, not every edge case. Give each seam one line on what it catches and what it misses. Never test at an unconfirmed seam, and never reach inside it.

## Horizontal slicing

Writing all specs, then all code, tests the imagined shape of things instead of real behavior, goes insensitive to real changes, and commits to a test structure before the implementation is understood. Work in vertical slices: one failing spec, one minimal change, repeat. Each spec is a tracer bullet that responds to what the last cycle taught.

## Cycle

- **Red before green.** Write the failing spec and run it to see it fail for the right reason, then write only the code that passes it. The red run is required even for a one-line fix; never write the spec and the fix together. No speculative code, no anticipated specs.
- **One slice at a time.** One seam, one spec, one minimal change per cycle. Never write the specs of a whole plan first.
- **No refactoring beyond the slice.** Leave other code alone; `go-review` may flag it and `go-fix` fixes it only when the user selects the finding.
