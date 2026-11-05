# Plan Format

A spec plus its tickets: Goal, Acceptance criteria, Testing, Decisions, and Out of scope are the spec; each step is a ticket with `Blocked by` edges.

## Writing

1. Read the project references per [setup.md](setup.md) and nearby code.
2. Resolve behavior (current and expected), edge and error cases, roles, test data, dependencies, exclusions, design, wording.
3. Once expected behavior is clear, ask once for an optional screenshot.
4. Write per the [writing rules](writing-rules.md), as simple as possible, latest approved scope only. No `requirements.md`: Goal and criteria live in the plan.

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

- **Goal:** one or two checkable lines: the behavior plus the specs that must pass.
  - The user confirms it; only a requirement change the user requests alters it.
  - `go-work` keeps working until it holds. Never a vague aim.
- **Acceptance criteria:** observable results, one line each, key error and edge cases included.
- **Steps:** one independently verifiable behavior ending in one passing commit; usually two to four, one for a small ticket.
  - Merge steps touching the same file or behavior. Add one only when it can pass its spec alone.
  - Lines: `Do`, `Test`, `Commit`, `Blocked by`, `Files`.
  - `Blocked by`: earlier steps needed, or `none`.
  - `Commit`: one-line message in the confirmed format, no body.
  - `Files`: mark a deleted file `delete` and list it under `Deletions`.
  - `Test`: behaviors through a public seam, or `none: no setup`. Each spec is written first and must fail first.
  - Seams, temporary contracts, access-right changes, precedents go in `Do` or `Files`, only when the developer needs them.
- **Testing:**
  - Seams under test, highest first, as few as possible, preferably existing. One line each on what it catches and misses; approving the plan confirms them.
  - Prior art: a similar existing spec.
  - `E2E:` exact spec files and scenario, or `none`. e2e runs once, after the last step; this line is its only scope.
- **Decisions:** choices that change scope or design, one line each; mention the diagnosis when it drove one.
- **Deletions:** every deleted file, or `None.`. Approving the plan approves exactly these.
- **Out of scope:** excluded work, or `None.`.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

## Changes

- A triage document becomes scope only through user approval.
- Ask before changing an approved plan; drop superseded scope outright.
