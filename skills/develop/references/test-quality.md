# Test Quality

The project's own test rules win where they conflict. Every section applies on every cycle: read them before the first spec and consult them during the loop.

## A good test

Verifies behavior through a public interface, so code can change entirely and the test survives. It reads like a spec: "user can checkout with valid cart" says which capability exists and survives a refactor, because it ignores internal structure. One logical assertion per test. Use the domain terms of `~/.just-do-it/{project}/docs/glossary.md` and the repo's `GLOSSARY.md`, and respect the ADRs in `~/.just-do-it/{project}/docs/adr/` and the repo's `docs/adr/` for the area you touch.

See [examples.md](examples.md) for good and bad tests, and [mocking.md](mocking.md) for what to mock.

## Seams

A seam is the public boundary a test observes behavior at: the interface where you see behavior without reaching inside. Tests live at seams, never against internals.

Test only at seams the user confirmed: those in the plan's `Testing` section (approved with the plan), or, with no plan, seams returned as `Open` and confirmed. You can't test everything; agreeing seams first puts effort on critical paths and complex logic, not every edge case. Give each seam one line on what it catches and what it misses. Never test at an unconfirmed seam, and never reach inside it.

## Anti-patterns

- **Implementation-coupled.** Mocks internal collaborators, calls private methods, asserts call counts or order, or verifies through a side channel such as a database query. The tell: a refactor that keeps behavior breaks the test, or the test name says how, not what.
- **Tautological.** The expected value is recomputed the way the code computes it, so it passes by construction and can never disagree with the code. Take it from a literal, a worked example, or the spec.
- **Horizontal slicing.** Writing all specs, then all code, tests the imagined shape of things instead of real behavior, goes insensitive to real changes, and commits to a test structure before the implementation is understood. Work in vertical slices: one failing spec, one minimal change, repeat. Each spec is a tracer bullet that responds to what the last cycle taught.

## Spec files

Unless the project's rules say otherwise, keep a coverage comment directly above each new or changed top-level `describe`, for the whole unit:

```ts
/**
 * Covered:
 * - <behavior the spec tests>
 *
 * Not Covered:
 * - <behavior that should be tested but is not>
 */
describe('...', () => {
```

`Covered` lists every behavior tested, old and new. `Not Covered` lists behaviors that should be tested but are not, including unchanged ones outside scope; omit it when empty. A changed behavior is done when it has setup and a meaningful assertion covering the regression and relevant missing, invalid, unloaded, and edge inputs, and the comment is accurate.

## The loop

This is the one definition of the loop; workflow step 3 of `SKILL.md` runs it per behavior of a step.

- **Red before green.** Write the failing spec and run it to see it fail for the right reason, then write only the code that passes it. The red run is required even for a one-line fix; never write the spec and the fix together. No speculative code, no anticipated specs.
- **One slice at a time.** One seam, one spec, one minimal change per cycle. Never write the specs of a whole plan first.
- **No refactoring beyond the slice.** Leave other code alone; `review` may flag it and `resolve-review` fixes it only when the user selects the finding.
