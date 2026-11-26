# to-plan

Turn confirmed requirements into `agent-view/plan.md` and `agent-view/checklist.md` for approval.

1. Read supplied requirements or `agent-view/spec.md`, plus project rules, `public/glossary.md`, `public/adr/`, and `public/jdi-config.md` when present.
2. Bring unresolved implementation decisions and unknown domain terms to the user in rounds. Never guess unknown terms—confirm with the user and save them to `public/glossary.md` (and hard-to-reverse decisions to `public/adr/`).
3. Draft `agent-view/plan.md` with numbered `Goal` scenarios showing `Expected` before `Actual`, a `Statechart` for stateful flows, and implementation `Steps` with file references in tooltips. Assign each step to a pipeline with explicit dependencies and shared resources. Write a linked `agent-view/checklist.md` with targets, precedents and checks, plus commit format and diagnosis when needed.
4. For a full, risky or requested plan, show the separate plan review findings before approval.
5. Render the visual plan at `dev-view/plan.html` (with the statechart diagram and inline attachment images) and report its path so you can review `dev-view/plan.html` in the browser and approve.

[Skill](../skills/to-plan/SKILL.md) · [Plan format](../skills/to-plan/references/plan-format.md) · [Storage](../skills/go-setup/references/storage.md)
