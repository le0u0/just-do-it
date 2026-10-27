# Plan Format

Brainstorming belongs to `think`. The plan reads as a spec plus its tickets: Goal, Acceptance criteria, Testing, Decisions, and Out of scope are the spec; each step is a ticket with its `Blocked by` edges.

## Writing the plan

Read the [project references](../../manager/references/project-references.md) and nearby code. Resolve the objective, current and expected behavior, acceptance criteria, edge and error cases, roles, permissions, test data, dependencies, exclusions, temporary contracts, design, and wording. Once expected behavior is clear, ask once for an optional screenshot.

Write `plan.md` per the [written docs](../../manager/references/written-docs.md) rules, as simple as a [review report](../../review/references/report-format.md). Latest approved scope only. Goal and acceptance criteria live in `plan.md`, so no `requirements.md` is needed.

```markdown
# Plan: PROJ-123 do something

Status: draft

## Goal

Export button hidden when flag off. `toolbar.test` and `toolbar.spec.ts` pass.

## Acceptance criteria

- Flag off: Export button hidden in the toolbar.
- Flag on: no change.

## Steps

### 1. Gate Export button

- **Do:** Add `isExportEnabled` check in `buildActions`.
- **Test:** Spec: tab absent when flag off. Run: yes.
- **Commit:** `feat: hide export button when flag off`
- **Blocked by:** none
- <sub>**Files:** `toolbar`, `toolbar.test`</sub>

## Testing

- Seam: toolbar actions. Prior art: `layout.test`.
- E2E: `playwright/tests/toolbar.spec.ts`: export button hidden when flag off.

## Decisions

- Keep Print button as is.

## Deletions

None.

## Out of scope

- Share dialog.

## Open

None.

## Reference

<sub>Requirement source: PROJ-123<br>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>Initial baseline: a1b2c3d<br>Delivery: per-step commits</sub>
```

- **Goal:** one or two lines, checkable: the behavior, plus the specs that must pass. The user confirms it while planning, and only a requirement change the user requests alters it. `develop` keeps working until it holds. Never a vague aim such as "improve the toolbar".
- **Acceptance criteria:** observable results, one line each, key error and edge cases included.
- **Steps:** few, coarse milestones, usually two to four; a small ticket is one. Group related changes into one step, one commit, and never split similar work into separate steps or commits. Each step works on its own. Each has `Do`, `Test`, `Commit`, `Blocked by`, and `Files` in one line each. `Blocked by` lists the earlier steps this one needs, or `none`; a step is ready when all of them are done. `Commit` is the step's one-line message in the confirmed commit format, with no body. Mark any file the step deletes `delete` in `Files`, and list it under `Deletions`. `Test` names the behaviors through a public seam, or `none: no setup`; each spec is written before its code and must fail first. Put test seams, temporary contracts, access-right changes, and precedents in `Do` or `Files`, only when the developer needs them.
- **Testing:** the seams under test, highest first and as few as possible, ideally one; prefer existing seams. Give each seam one line on what it catches and what it misses; approving the plan confirms them. Name prior art: a similar existing spec. `E2E:` names the exact e2e spec files to write or change and the scenario, or `none`; e2e runs once, after the last step, and this line is its only scope.
- **Decisions:** only choices that change scope or design, one line each. Link `diagnose.md` when it drove one.
- **Deletions:** every file the plan deletes, one line each, or `None.`. Approving the plan approves exactly these deletions; any other needs the user's approval.
- **Out of scope:** work the plan excludes, one line each, or `None.`.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

A triage document becomes scope only through user approval. Ask before changing an approved plan. Drop superseded scope outright.

