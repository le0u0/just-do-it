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
- **Steps:** directly after `Goal`. Each step ends with a focused verification check and one planned commit. Group cohesive changes to avoid micro-commits. Use one step for work that can be verified together.
  - Group changes that need each other to deliver one behavior. Keep its specs, implementation, and setup used only for that behavior together. Plan separate steps for independently verifiable behaviors with disjoint writes so workers can run them together.
  - Give required shared setup its own step when multiple later steps need it and a focused check can verify it. List that setup step under `Blocked by` for each consumer.
  - Lines: `Do`, `Test`, `Commit`, `Blocked by`, `Files`.
  - `Do`: at most three bullets of behavior in plain words, not code edits.
  - `Blocked by`: actual prerequisites, or `none` if the step can start after plan approval. Step numbers do not imply dependencies.
  - `Commit`: one-line message in the confirmed format, no body.
  - `Files`: name owned source and test paths. Mark a deleted file `delete` and list it under `Deletions`.
  - `Test`: name the public seam and focused runner for a behavior, or the focused verification for shared setup. Use `none: no setup` when no runner exists and setup is outside scope. Name any shared state or existing isolation relevant to parallel execution. Write and run each behavior's failing spec first when authorized.
  - Seams, temporary contracts, access-right changes, reusable project components, triage image paths, and precedents go in `<sub>` beside `Files`, only when the developer needs them.
- **Acceptance criteria:** observable results, one bullet each, key error and edge cases included.
  - Group by topic under `###` headings (such as the screen, rule set, or role); every bullet sits in a headed topic group.
  - Merge overlapping bullets; aim for at most 15 in all and 5 per group.
- **Out of scope:** excluded work, or `None.`. Directly after the criteria so the boundary reads with them.
- **Testing:**
  - Keep scope focused, and cover every changed component or module with behavior (including template bindings); if a changed file has no spec yet, plan a new spec beside it focused on the changed behavior. One line each on what it catches and misses; approving the plan confirms them.
  - `E2E:` the scenario in plain words (create a new e2e spec when none exists for the area). Use `none` only when there is no E2E setup (`none: no setup`), the change has no UI or user-flow impact, or the user explicitly skips E2E — never set `none` just because no prior spec exists. e2e runs once, after the last step; this line is its only scope.
  - Prior art and exact spec files go in `<sub>`.
- **Decisions:** at most seven choices that change scope or design, one line each; mention the diagnosis when it drove one. State the choice alone.
- **Deletions:** every deleted file, or `None.`. Approving the plan approves exactly these.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

## Changes

- A triage document becomes scope only through user approval.
- Ask before changing an approved plan; drop superseded scope outright.
