# Test Quality

## A good test

- Verifies behavior through a public interface, so code can change entirely and the test survives.
- Reads like a spec ("user can checkout with valid cart"), ignoring internal structure.
- One logical assertion.

## Anti-patterns

- **Implementation-coupled:** mocks internal collaborators, calls private methods, asserts call counts or order, or verifies through a side channel such as a database query. Tell: a behavior-preserving refactor breaks it, or its name says how, not what.
- **Tautological:** the expected value is recomputed as the code computes it, so it passes by construction. Take it from a literal, worked example, or the spec.

## Spec files

Unless project rules say otherwise, put a concise coverage comment (`to-charsiu` style: plain human language, no jargon, group related behaviors into a few short bullets — never a method-by-method or input-by-input dump) directly above each new or changed top-level `describe`, for the whole unit:

```ts
/**
 * Covered:
 * - <short plain-language summary of tested behavior>
 *
 * Not Covered:
 * - <short plain-language summary of untested behavior>
 */
describe('...', () => {
```

- `Covered`: every behavior tested, old and new, in brief plain-language bullets.
- `Not Covered`: behaviors that should be tested but are not, including unchanged ones outside scope, in brief plain-language bullets. Omit when empty.
- A changed behavior is done when it has setup and a meaningful assertion for the regression and relevant missing, invalid, unloaded, and edge inputs, and the comment is accurate.
