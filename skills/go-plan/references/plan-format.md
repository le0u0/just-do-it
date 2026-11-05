# Plan Format

The plan reads as a spec plus its tickets: Goal, Acceptance criteria, Testing, Decisions, and Out of scope are the spec; each step is a ticket with its `Blocked by` edges.

## Writing the plan

1. Read the project references per [setup.md](setup.md) and nearby code.
2. Resolve:
   - Objective, current and expected behavior, acceptance criteria.
   - Edge and error cases, roles, permissions, test data.
   - Dependencies, exclusions, temporary contracts, design, wording.
3. Once expected behavior is clear, ask once for an optional screenshot.
4. Write per the [writing rules](writing-rules.md), as simple as possible.
   - Latest approved scope only.
   - Goal and acceptance criteria live in the plan: no `requirements.md`.

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

## Sections

- **Goal**
  - One or two lines, checkable: the behavior, plus the specs that must pass.
  - The user confirms it while planning. Only a requirement change the user requests alters it.
  - `go-work` keeps working until it holds.
  - Never a vague aim such as "improve the toolbar".
- **Acceptance criteria:** observable results, one line each, key error and edge cases included.
- **Steps**
  - One step is one independently verifiable behavior that ends in one passing commit. A ticket usually has two to four; a small one has one.
  - Merge steps that touch the same file or behavior. Add a step only when it can pass its spec without the others.
  - Each step has `Do`, `Test`, `Commit`, `Blocked by`, `Files`, one line each.
  - `Blocked by`: the earlier steps this one needs, or `none`. A step is ready when all are done.
  - `Commit`: the one-line message in the confirmed commit format, no body.
  - `Files`: mark any file the step deletes `delete`, and list it under `Deletions`.
  - `Test`: the behaviors through a public seam, or `none: no setup`. Each spec is written before its code and must fail first.
  - Put test seams, temporary contracts, access-right changes, and precedents in `Do` or `Files`, only when the developer needs them.
- **Testing**
  - The seams under test, highest first, as few as possible, ideally one. Prefer existing seams.
  - Per seam, one line on what it catches and what it misses. Approving the plan confirms them.
  - Prior art: a similar existing spec.
  - `E2E:` the exact e2e spec files to write or change and the scenario, or `none`. e2e runs once, after the last step; this line is its only scope.
- **Decisions:** only choices that change scope or design, one line each. Mention the diagnosis when it drove one.
- **Deletions:** every file the plan deletes, one line each, or `None.`. Approving the plan approves exactly these; any other needs the user's approval.
- **Out of scope:** work the plan excludes, one line each, or `None.`.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

## Changes

- A triage document becomes scope only through user approval.
- Ask before changing an approved plan.
- Drop superseded scope outright.
