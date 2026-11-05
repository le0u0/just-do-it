# go-work

Implements production code from a request, spec, ticket or approved plan, test-first. The manager runs it in the main thread; you can call it directly.

## DO IT

- Input: a request, ticket, spec, or approved plan from `go-plan`, as text or a path you name.
- Modes: direct request, failure to fix (diagnose first), approved plan (step by step, then final validation), specs only (calls `go-ut`).
- Calls `dev-tdd` once per step.
- Writes source and specs in the repo. Returns `Done` / `Open` / `Changed`.
- Never writes `plan.md`, `checklist.md` or `review.md`, never reviews its own work, never creates or pushes branches. Commits only per the plan or on your approval.

## USE IT

| Situation | Use |
| --- | --- |
| Build a feature, "implement step 2", fix a failure | `go-work` |
| Only unit specs | `go-ut` |
| Review the result | `go-review` |

The manager calls it for each plan step.

## WORK IT

- It works the plan step by step, each ending with a `Done` line.
- Specs come before production code, through `dev-tdd`.
- It asks only after three different fixes fail, or when a step needs an unlisted deletion or a change outside the plan.
- It ends with `Open: ready for review` or `Open: run e2e`.

## FIT IT

```text
go-plan -> go-work (calls dev-tdd -> go-ut / go-e2e) -> go-e2e -> go-review
```

- Before it: `go-plan`. After it: `go-e2e`, then `go-review`.
