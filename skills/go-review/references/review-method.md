# Standards and Requirements

Apply both axes in the single pass; a change can pass one and fail the other.

- **Standards:** check hunks against repository instructions; cite the rule. Omit preferences, generic refactors, tooling-enforced checks. Documented rule: firm finding. Smell: "possible" only.
- **Requirements:** compare expected behavior with changed control flow: missing behavior, wrong implementation, consequential scope creep. Quote the requirement line per finding. None: skip this axis.

## Evidence

- Inspect callers, types, tests, state handling only to confirm an issue.
- A finding needs a reachable trigger, impact, exact changed location, feasible fix.
- A missing test is a defect only when required or tied to a shown regression.
- Done when every hunk is assessed; missing evidence limits a finding, never skips the review.
