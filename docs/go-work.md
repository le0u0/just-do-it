# go-work

Implements one step of work, test-first: a request, one step of a plan, or a failure to fix. The manager runs it in the main thread once per plan step; you can call it directly.

## DO IT

- Input: a request, a failure, or one step of a plan from `go-plan`, as text or a path you name.
- Modes: direct request, failure to fix (diagnose first), plan step (one step only), specs only (calls `go-ut`).
- Calls `dev-tdd` once per step.
- Writes source and specs in the repo. Returns `Done` / `Open` / `Changed`.
- Never writes `plan.md`, `checklist.md` or `review.md`, never reviews its own work, never creates or pushes branches. Commits only per the plan or on your approval.

## USE IT

| Situation | Use |
| --- | --- |
| Build a feature, "implement step 2", fix a failure | `go-work` |
| Only unit specs | `go-ut` |
| Review the result | `go-review` |

The manager calls it once per plan step and runs the final validation itself.

## WORK IT

- It does exactly one step and stops, ending with a `Done` line.
- Specs come before production code, through `dev-tdd`.
- It asks only after three different fixes fail, or when a step needs an unlisted deletion or a change outside the plan.
- It never starts the next step; it reports `Done`, the commit SHA if any, and `Open`.

## FIT IT

```text
go-plan -> go-work (calls dev-tdd -> go-ut / go-e2e) -> go-e2e -> go-review
```

- Before it: `go-plan`. After the last step: the manager's final validation, then `go-e2e`, then `go-review`.
