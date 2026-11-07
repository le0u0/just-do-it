# Standards and Requirements

Apply both axes; a change can pass one and fail the other.

- **Standards:** check hunks against repository instructions; cite the rule. Omit preferences, generic refactors, tooling-enforced checks. Documented rule: firm finding. Smell: "possible" only.
- **Requirements:** compare expected behavior with changed control flow: missing behavior, wrong implementation, consequential scope creep. Quote the requirement line per finding. None: skip this axis.

## Lenses

One pass over every hunk per assigned lens; a bug often shows only under the right lens.

- **Logic:** inverted or wrong conditions, off-by-one, early return, fallthrough, operator precedence.
- **State and data:** stale or shared state, mutation, ordering, cache keys, null, empty, defaults.
- **Async and lifecycle:** races, missing await or error path, leaked subscriptions, first render.
- **Contract:** changed signature, return or behavior against every reader; sibling modes (create, edit, copy); mirrored code paths.
- **Failure paths:** swallowed errors, partial failure, retry, cleanup.
- **Security:** access rights, injection, exposed data or secrets.
- **Regression:** removed guards, undone intent, behavior others relied on.
- **Requirements:** each requirement and acceptance line mapped to the code that delivers it.

## Evidence

- Inspect callers, types, tests, state handling to find and confirm an issue.
- A finding needs a reachable trigger shown by reading the code, impact, exact location, feasible fix.
- A missing test is a defect only when required or tied to a shown regression.
- Missing evidence limits a finding, never skips the review.
