---
name: go-plan
description: 'Grill one ticket, then write agent-view/plan.md and agent-view/checklist.md for approval. Use for "plan PROJ-123", "think through PROJ-123", "what is unclear here" or "break this into steps".'
---

# Plan

## Scope & Storage

- Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
- In `go-flow`, work in one reasoning subagent: return each question round to the caller, then resume with the user's answers. Direct use asks the user in the current thread.
- Write no production code or tests. Write planning outputs for agents to `agent-view/plan.md` and `agent-view/checklist.md` (plus `agent-view/commit-format.md` when confirmed and `agent-view/diagnose.md` when needed), and render the human-readable visual plan at `dev-view/plan.html` per [html-render.md](../go-setup/references/html-render.md) (with inline attachment images and visual statechart) so the user can inspect `dev-view/plan.html` and approve.
- Two phases: grill, then write. Complete `Grill` before `Write`, unless the user asks to skip grilling. User only wants gaps found: stop after the grill.

## Inputs

- Requirements come only from supplied context, `agent-view/research.md`, or explicitly retrieved sources. Cite supplied ticket links; a key alone says nothing.
- Read `agent-view/research.md` and `agent-view/attachments/` when present in the branch folder. For a direct ticket URL or explicit lookup with no `agent-view/research.md`, run `go-research` first.
- Read the project references per [setup.md](references/setup.md) (including `~/.just-do-it/{project}/public/glossary.md`, `public/adr/`, and `public/test-config.md` when present), existing reusable project components, and the code the ticket likely touches.

## 1. Grill

Treat the ticket as a design tree: each decision branches into the decisions that hang off it.

- Work in rounds. The **frontier** is every open decision whose prerequisites are settled.
  - Ask the whole frontier in one round, numbered, most important first.
  - A question that depends on an open one waits.
- Per question: a recommended answer and one line on why it matters. Word it so "yes" accepts.
  - Put the question and the recommendation on separate lines, never in one sentence.
- Find facts yourself in code, docs, and ticket. Ask only decisions and unknown domain terms.
- Look for: missing or conflicting requirements, unclear criteria, edge and error cases, roles, test data, dependencies, design and wording, risks to existing behavior, simpler alternatives.
- Include in the tree:
  - Checkable `Goal` bullet points (the real functional objectives that determine when the task is done, including key edge/error behaviors—never boilerplate like "tests pass") confirmed with the user.
  - Which existing components, services, or shared primitives to reuse when multiple candidates exist or reuse is unclear (never guess—ask the user).
  - Unknown terminology, product terms, or glossary clashes per [domain-docs.md](references/domain-docs.md) and [public-docs.md](../go-setup/references/public-docs.md): **never guess unknown domain terms—ask the user, then save confirmed terms to `public/glossary.md` and accepted hard-to-reverse decisions to `public/adr/`**.
  - The commit format, when the project and `agent-view/commit-format.md` have none (see Commit format).
  - Boundaries, probed with a concrete edge-case scenario.
  - State transitions & missing-transition checks for stateful UI/workflows per [statechart.md](references/statechart.md).
  - E2E scenario when E2E setup exists and UI or user flows change: read the E2E folder path from `public/test-config.md` or locate it directly. List the folder first without reading spec files, then suggest concrete scenario(s) and confirm with the user before writing the plan.
- Done when the frontier is empty and the user confirms shared understanding and the `Goal`. Then write `agent-view/plan.md` and `agent-view/checklist.md`. For a grill-only request, stop after the final round.

## Commit format

- Use the project's format (`AGENTS.md`, `CLAUDE.md`, rules, project-local skills), else `agent-view/commit-format.md`.
- Neither: ask in the grill, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`.
- Save the confirmed format to `agent-view/commit-format.md` (one line plus an example) and record it under `Decisions`.

## 2. Write

1. Read [plan-format.md](references/plan-format.md), [checklist-format.md](references/checklist-format.md), and (for stateful features) [statechart.md](references/statechart.md). Write `agent-view/plan.md` (pointing directly to relevant `attachments/{ticket}/...` files in steps and acceptance criteria) and `agent-view/checklist.md`. Record the grill's decisions under `Decisions`.
2. Bug ticket whose diagnosis would clutter the plan: also write `agent-view/diagnose.md` per [diagnose-format.md](references/diagnose-format.md).
3. Check unit and E2E setup per [setup.md](references/setup.md). Record `none: no setup` when there is no setup and adding it is outside scope.
4. Make each step concrete enough for `go-work` to run without new design decisions: owned source and test files, reusable components or `agent-view/attachments/` where relevant, dependencies including shared state, public test seams, test authorization, one-line commit message, and delivery mode. Group related changes into cohesive steps.
5. List every file a step deletes under `Deletions`; plan approval covers the listed scope and its deletions.
6. User changes the requirement: revise `Goal`, steps, and `Deletions`, and update `agent-view/plan.md` and `agent-view/checklist.md` in place.
7. Update `public/glossary.md` for any newly confirmed domain terms and write `public/adr/NNN-short-title.md` for any confirmed ADR decisions per [domain-docs.md](references/domain-docs.md).
8. Render `~/.just-do-it/{project}/{branch}/dev-view/plan.html` per [html-render.md](../go-setup/references/html-render.md), including the visual statechart diagram (when stateful) and inline image previews from `../agent-view/attachments/{ticket}/`.
9. Report `dev-view/plan.html` (alongside `agent-view/plan.md` and `agent-view/checklist.md`) so the user can review `dev-view/plan.html` in the browser and approve the plan.

## Done when

- Every `Goal` bullet maps to a step with a failing test named (or `none: no setup`). Each shared setup step has a focused verification check.
- Every step has a `Commit` line and a `Reuse` line.
- The `Goal` bullets are confirmed and checkable.
- `Open` is `None.` or lists the blocking questions.
- `agent-view/plan.md`, `agent-view/checklist.md`, and `dev-view/plan.html` (plus any updates to `public/glossary.md` or `public/adr/`) are written.
