# Review Checks

Apply each relevant check to every changed file type: source, templates, styles, data, translation files, specs, helpers, configuration. The project's own rules add to these.

## Checks

- **Conventions:** naming, module and dependency wiring, resource cleanup, access control; match surrounding code.
- **Async safety:** unloaded or missing data in initialization, getters, templates, create and edit modes, first render.
- **UI:** user flow, visible and disabled states, loading, empty and error rendering, scoped styles, roles, labels, stable test selectors.
- **Localization:** no hard-coded visible text, safe fallbacks, locale parity, where the project localizes.
- **Unit tests:** placement beside code, meaningful assertions, mocks only at system boundaries, critical and invalid inputs, unloaded state, regression coverage.
- **End-to-end tests:** stable locators, helper reuse, deterministic waits, response assertions, test-data ownership, requested run strategy.
- **Correctness:** runtime failures, wrong or stale data, regressions, missing behavior, unnecessary changes.

## Code smells

- Check changed lines against [smells.md](smells.md).
