# The Loop

The project's own test rules win where they conflict. Read before the first spec; consult each cycle.

## Seams

- A seam is the public boundary a test observes behavior at, without reaching inside. Tests live at seams, never against internals.
- Test only at confirmed seams: those in the plan's `Testing` section, or, with no plan, seams returned as `Open` and confirmed.
- Agreeing seams first focuses effort on critical paths and complex logic, not every edge case.
- Give each seam one line on what it catches and what it misses.
- Never test at an unconfirmed seam or reach inside one.

## Vertical slices

- Horizontal slicing (all specs, then all code) tests imagined behavior, goes insensitive to real changes, and fixes test structure before the implementation is understood.
- Work in vertical slices: one failing spec, one minimal change, repeat. Each spec is a tracer bullet shaped by the last cycle.

## Cycle

- **Red before green:** write the failing spec, run it, see it fail for the right reason, then write only the code that passes it. Required even for a one-line fix; never write spec and fix together. No speculative code or anticipated specs.
- **One slice at a time:** one seam, one spec, one minimal change. Never write a whole plan's specs first.
- **No refactoring beyond the slice:** `go-review` may flag other code; `go-fix` fixes it only when the user selects the finding.
