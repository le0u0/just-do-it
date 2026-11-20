# Test Quality

## A good test

- Verifies behavior through a public interface, so code can change entirely and the test survives.
- Reads like a spec ("user can checkout with valid cart"), ignoring internal structure.
- One logical assertion per test.

## Complete component/unit coverage

- Cover **all observable behaviors** of the touched component, service, or unit in its spec file: normal flow, edge cases, unloaded/empty state, and error/invalid inputs.
- Avoid comments in spec files; if a non-obvious setup constraint requires a note, limit it to a single 1-line comment (`// ...`).

## Anti-patterns

- **Implementation-coupled:** mocks internal collaborators, calls private methods, asserts call counts or order, or verifies through a side channel such as a database query. Tell: a behavior-preserving refactor breaks it, or its name says how, not what.
- **Tautological:** the expected value is recomputed as the code computes it, so it passes by construction. Take it from a literal, worked example, or the spec.
