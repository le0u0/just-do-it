# Standards and Requirements

Apply both axes in the single review pass. A change can pass one and fail the other.

## Standards

- Check changed hunks against repository instructions; cite the rule.
- Omit preferences, generic refactors, checks tooling enforces.
- Documented rule: firm finding. Smell: "possible" only.

## Requirements

- Compare expected behavior with changed control flow and outcomes: missing behavior, wrong implementation, consequential scope creep.
- Quote the requirement line for each finding.
- No requirements: skip this axis.

## Evidence

- Inspect callers, types, tests, state handling only to confirm an issue.
- A finding needs:
  1. a reachable trigger
  2. impact
  3. an exact changed location
  4. a feasible fix
- A missing test is a defect only when required or tied to a shown regression.

## Done

- Every changed hunk assessed.
- Missing evidence limits a finding; it never skips the review.
