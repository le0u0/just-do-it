# Plan Format

A spec plus its steps: `Goal`, `Statechart` (when stateful), `Out of scope`, `Testing`, `Decisions` are the spec; each step is a unit of work with `Blocked by` edges.

## Writing

1. Once expected behavior is clear, ask once for an optional screenshot.
2. Write per the [writing rules](writing-rules.md), as simple as possible, latest approved scope only.
3. The user reads `dev-view/plan.html` to approve it: plain words, short, grouped. Cut, merge, or drop what the reader does not need to approve.

```markdown
# Plan: PROJ-123 do something

Status: draft

## Goal

- Hide the Export button in the toolbar when the feature flag is off.
- Keep the toolbar unchanged when the feature flag is on.
- Update Export button visibility immediately if the flag changes while the page is open.

## Steps

### 1. Hide Export button when flag is off

- **Do:** Show the Export button only when the feature flag is enabled.
- **Reuse:** `FeatureFlagService.isEnabled` (`src/app/shared/feature-flag.service.ts`).
- **Test:** Button absent when flag off, present when flag on. Run: yes.
- **Commit:** `feat: hide export button when flag off`
- **Blocked by:** none
- <sub>**Files:** `toolbar`, `toolbar.test`; check `isExportEnabled` in `buildActions`</sub>

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

- **Goal:** bullet list of the **real observable product/functional objectives** that determine when the task is done, including key edge and error cases.
  - Never include boilerplate like "unit tests pass" or "E2E tests pass" in `Goal` (passing tests is a baseline workflow requirement, not a functional objective).
  - The user confirms it; only a requirement change the user requests alters it.
  - `go-work` runs the steps until every bullet in `Goal` holds.
- **Statechart (when stateful):** directly after `Goal` when the feature has UI/form states, async transitions, or status lifecycles per [statechart.md](statechart.md). Include a Mermaid `stateDiagram-v2` block and one-line invariant bullets. Omit for static changes.
- **Steps:** directly after `Goal` (or `Statechart`). Each step ends with a focused verification check and one planned commit. Group cohesive changes to avoid micro-commits. Use one step for work that can be verified together.
  - Group changes that need each other to deliver one behavior. Keep its specs, implementation, and setup used only for that behavior together. Plan separate steps for independently verifiable behaviors with disjoint writes so workers can run them together.
  - Give required shared setup its own step when multiple later steps need it and a focused check can verify it. List that setup step under `Blocked by` for each consumer.
  - Lines: `Do`, `Reuse`, `Test`, `Commit`, `Blocked by`, `Files`.
  - `Do`: at most three bullets of behavior in plain words stating what the step will handle, not low-level code edits.
  - `Reuse`: existing project components, services, or helpers the step will reuse (confirmed with the user during `Grill` if uncertain), or `none`.
  - `Blocked by`: actual prerequisites, or `none` if the step can start after plan approval. Step numbers do not imply dependencies.
  - `Commit`: one-line message in the confirmed format, no body.
  - `Files`: name owned source and test paths. Mark a deleted file `delete` and list it under `Deletions`.
  - `Test`: name the public seam and focused runner for a behavior, or the focused verification for shared setup. Use `none: no setup` when no runner exists and setup is outside scope. Name any shared state or existing isolation relevant to parallel execution. Write and run each behavior's failing spec first when authorized.
  - Seams, temporary contracts, access-right changes, reusable project components, relative attachment paths (`attachments/{ticket}/...`), and precedents go in `<sub>` beside `Files`, only when the developer needs them.
- **Out of scope:** excluded work, or `None.`.
- **Testing:**
  - Keep scope focused, and cover every changed component or module with behavior (including template bindings); if a changed file has no spec yet, plan a new spec beside it focused on the changed behavior. One line each on what it catches and misses; approving the plan confirms them.
  - `E2E:` the scenario in plain words (create a new e2e spec when none exists for the area). Use `none` only when there is no E2E setup (`none: no setup`), the change has no UI or user-flow impact, or the user explicitly skips E2E — never set `none` just because no prior spec exists. E2E runs once, after the last step; this line is its only scope.
  - Prior art and exact spec files go in `<sub>`.
- **Decisions:** at most seven choices that change scope or design, one line each; mention the diagnosis when it drove one. State the choice alone.
- **Deletions:** every deleted file, or `None.`. Approving the plan approves exactly these.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

## Changes

- `agent-view/spec.md` becomes scope only through user approval.
- Ask before changing an approved plan; drop superseded scope outright.
