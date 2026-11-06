# Plan Format

A spec plus its tickets: Goal, Acceptance criteria, Out of scope, Testing, Decisions are the spec; each step is a ticket with `Blocked by` edges.

## Writing

1. Once expected behavior is clear, ask once for an optional screenshot.
2. Write per the [writing rules](writing-rules.md), as simple as possible, latest approved scope only.
3. The user reads this to approve it: plain words, short, grouped. Aim for under 60 lines; cut, merge, or drop what the reader does not need to approve.

```markdown
# Plan: PROJ-123 do something

Status: draft

## Goal

Export button hidden when flag off. New and changed specs pass.

## Steps

### 1. Hide Export button

- **Do:** Show the button only when the flag is on.
- **Test:** Button absent when flag off. Run: yes.
- **Commit:** `feat: hide export button when flag off`
- **Blocked by:** none
- <sub>**Files:** `toolbar`, `toolbar.test`; check `isExportEnabled` in `buildActions`</sub>

## Acceptance criteria

### Toolbar

- Flag off: Export button hidden.
- Flag on: toolbar unchanged.

### Edge cases

- Flag changes while page is open: button follows it.

## Out of scope

- Share dialog.

## Testing

- Seam: toolbar actions. Catches wrong visibility; misses real flag service.
- E2E: Export button hidden when flag off.
- <sub>Prior art: `layout.test`. E2E: `playwright/tests/toolbar.spec.ts`</sub>

## Decisions

- Print button stays as is.

## Deletions

None.

## Open

None.

## Reference

<sub>Requirement source: PROJ-123<br>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>Initial baseline: a1b2c3d<br>Delivery: per-step commits</sub>
```

## Sections

- **Goal:** one or two checkable lines: the behavior plus the specs that must pass.
  - The user confirms it; only a requirement change the user requests alters it.
  - The manager runs the steps until it holds.
- **Steps:** directly after `Goal`, since the user reads those two first. One independently verifiable behavior ending in one passing commit; usually two to four, one for a small ticket.
  - Merge steps touching the same file or behavior. Add one only when it can pass its spec alone.
  - Lines: `Do`, `Test`, `Commit`, `Blocked by`, `Files`.
  - `Do`: at most three bullets of behavior in plain words, not code edits.
  - `Blocked by`: earlier steps needed, or `none`.
  - `Commit`: one-line message in the confirmed format, no body.
  - `Files`: mark a deleted file `delete` and list it under `Deletions`.
  - `Test`: behaviors through a public seam, or `none: no setup`. Each spec is written first and must fail first.
  - Seams, temporary contracts, access-right changes, precedents go in `<sub>` beside `Files`, only when the developer needs them.
- **Acceptance criteria:** observable results, one bullet each, key error and edge cases included.
  - Group by topic under `###` headings (such as the screen, rule set, or role); every bullet sits in a headed topic group.
  - Merge overlapping bullets; aim for at most 15 in all and 5 per group.
- **Out of scope:** excluded work, or `None.`. Directly after the criteria so the boundary reads with them.
- **Testing:**
  - Seams under test, highest first, as few as possible, preferably existing. One line each on what it catches and misses; approving the plan confirms them.
  - `E2E:` the scenario in plain words, or `none`. e2e runs once, after the last step; this line is its only scope.
  - Prior art and exact spec files go in `<sub>`.
- **Decisions:** at most seven choices that change scope or design, one line each; mention the diagnosis when it drove one. State the choice alone.
- **Deletions:** every deleted file, or `None.`. Approving the plan approves exactly these.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

## Changes

- A triage document becomes scope only through user approval.
- Ask before changing an approved plan; drop superseded scope outright.
