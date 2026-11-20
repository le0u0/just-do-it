# go-plan

Grill one ticket, then write `agent-view/plan.md` and `agent-view/checklist.md` for approval.

1. Read supplied requirements or `agent-view/research.md`, plus project rules, `public/glossary.md`, `public/adr/`, and `public/test-config.md` when present.
2. Bring unresolved decisions, goal confirmation, and any unknown domain terms to the user in rounds. Never guess unknown terms—confirm with the user and save them to `public/glossary.md` (and hard-to-reverse decisions to `public/adr/`).
3. Draft `agent-view/plan.md` (with `## Goal` bullets defining the real functional completion criteria, `## Statechart` for stateful flows, and `## Steps` with `Do`, `Reuse`, `Test`, `Commit`, `Blocked by`, `Files`) and `agent-view/checklist.md` (plus `agent-view/commit-format.md` and `agent-view/diagnose.md` when needed).
4. Render the visual plan at `dev-view/plan.html` (with the statechart diagram and inline attachment images) and report its path so you can review `dev-view/plan.html` in the browser and approve.

[Skill](../skills/go-plan/SKILL.md) · [Plan format](../skills/go-plan/references/plan-format.md) · [Storage](../skills/go-setup/references/storage.md)
