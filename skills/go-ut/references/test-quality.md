# Test Quality

The project's own test rules win where they conflict. Read this before the first spec.

## A good test

Verifies behavior through a public interface, so code can change entirely and the test survives. It reads like a spec: "user can checkout with valid cart" says which capability exists and survives a refactor, because it ignores internal structure. One logical assertion per test. Use the domain terms of the repo's `GLOSSARY.md` and any glossary the caller passes, and respect the repo's `docs/adr/` for the area you touch.

See [examples.md](examples.md) for good and bad tests, and [mocking.md](mocking.md) for what to mock.

## Anti-patterns

- **Implementation-coupled.** Mocks internal collaborators, calls private methods, asserts call counts or order, or verifies through a side channel such as a database query. The tell: a refactor that keeps behavior breaks the test, or the test name says how, not what.
- **Tautological.** The expected value is recomputed the way the code computes it, so it passes by construction and can never disagree with the code. Take it from a literal, a worked example, or the spec.

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
