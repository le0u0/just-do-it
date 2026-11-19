# go-plan

Grill one ticket, then write a plan and checklist for approval.

1. Use the ticket or requirements supplied. Research missing live requirements and read relevant project rules and code.
2. Bring unresolved decisions to the user in rounds. Each question includes a recommendation and why it matters.
3. Draft the plan with observable acceptance criteria, owned paths, dependencies, TDD seams, E2E scope, commit messages, and deletions. Keep each behavior, its tests, and its own setup together. Verify shared setup once before the steps that depend on it.
4. Deliver the plan and checklist before asking for approval.

In `justaway`, one reasoning worker handles the grill and plan. The coordinator relays questions and answers, and delivers the result. Direct use asks the user in the current thread.

When saving, read `plan.md` and `checklist.md` in the task directory. When printing, both appear in the terminal.

[Plan format](../skills/go-plan/references/plan-format.md) · [Output delivery](../skills/justaway/references/storage.md#output-delivery)
