# go-plan

Grill one ticket, then write `agent-view/plan.md` and `agent-view/checklist.md` for approval.

1. Read supplied requirements or `agent-view/research.md`, plus project rules, `public/glossary.md`, `public/adr/`, and `public/test-config.md` when present.
2. Bring unresolved decisions, goal confirmation, and any unknown domain terms ("Section B", "patient history") to the user in rounds. Never guess unknown terms—confirm with the user and save them to `public/glossary.md` (and hard-to-reverse decisions to `public/adr/`).
3. Draft `agent-view/plan.md` (pointing to `attachments/{ticket}/...` and including a `## Statechart` for stateful flows) and `agent-view/checklist.md` (plus `agent-view/commit-format.md` and `agent-view/diagnose.md` when needed) with observable acceptance criteria, owned paths, dependencies, TDD seams, E2E scope, commit messages, and deletions.
4. Render the visual plan at `dev-view/plan.html` (with the statechart diagram and inline attachment images) and report its path so you can review `dev-view/plan.html` in the browser and approve.

[Skill](../skills/go-plan/SKILL.md) · [Plan format](../skills/go-plan/references/plan-format.md) · [Storage](../skills/go-setup/references/storage.md)
