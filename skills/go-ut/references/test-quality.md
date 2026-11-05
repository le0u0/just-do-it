# Test Quality

The project's own test rules win where they conflict. Read before the first spec.

## A good test

- Verifies behavior through a public interface, so code can change entirely and the test survives.
- Reads like a spec ("user can checkout with valid cart"), ignoring internal structure.
- One logical assertion.
- Uses the domain terms of `GLOSSARY.md` and any glossary the caller passes; respects `docs/adr/` for the area touched.
- See [examples.md](examples.md) and [mocking.md](mocking.md).

## Anti-patterns

- **Implementation-coupled:** mocks internal collaborators, calls private methods, asserts call counts or order, or verifies through a side channel such as a database query. Tell: a behavior-preserving refactor breaks it, or its name says how, not what.
- **Tautological:** the expected value is recomputed as the code computes it, so it passes by construction. Take it from a literal, worked example, or the spec.

## Spec files

Unless project rules say otherwise, put a coverage comment directly above each new or changed top-level `describe`, for the whole unit:

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

- `Covered`: every behavior tested, old and new.
- `Not Covered`: behaviors that should be tested but are not, including unchanged ones outside scope. Omit when empty.
- A changed behavior is done when it has setup and a meaningful assertion for the regression and relevant missing, invalid, unloaded, and edge inputs, and the comment is accurate.
