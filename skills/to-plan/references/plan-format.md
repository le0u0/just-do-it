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

1. **Open the toolbar with the flag off**\
   Expected: Export is hidden.\
   Actual: Export is visible.
2. **Open the toolbar with the flag on**\
   Expected: Export is visible.\
   Actual: Export is visible.
3. **Turn the flag off while the toolbar is open**\
   Expected: Export disappears immediately.\
   Actual: Export stays visible.

## Implementation pipelines

| Pipeline | Ordered steps | Requires | Shared resources |
| --- | --- | --- | --- |
| Toolbar | 1 | None | None |

## Steps

### 1. Show or hide Export with the feature flag

- **Do:** Show the Export button only when the feature flag is enabled.
- **Reuse:** `FeatureFlagService.isEnabled` (`src/app/shared/feature-flag.service.ts`).
- **Test:** Goals 1–3. Assert Export is hidden, visible, and updated when the flag changes. Run: yes.
- **Commit:** `feat: gate export with the feature flag`
- **Blocked by:** none
- <sub>**Files:** `src/toolbar.ts`, `src/toolbar.test.ts`</sub>

## Out of scope

- Share dialog.

## Testing

- Seam: toolbar actions. Catches wrong visibility; misses real flag service.
- E2E: Export button hidden when flag off.
- <sub>Prior art: `src/layout.test.ts`. E2E: `playwright/tests/toolbar.spec.ts`</sub>

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

- **Goal:** number the scenarios. Give each a short action or condition as its title, then put `Expected:` and `Actual:` on separate lines, in that order. Keep each line to at most 15 words. Name the affected screen, action, or output explicitly.
  - `Actual` records the observed or documented behavior. Write `Unverified` if evidence is missing, or `Feature unavailable` for a new capability. `Expected` records the observable acceptance criterion.
  - Include meaningful edge and error outcomes. Keep rationale, implementation, test instructions, and unchanged behavior in their applicable sections unless an unchanged behavior is itself an acceptance criterion.
  - The user confirms it; only a requirement change the user requests alters it.
  - `go-work` runs the steps until every `Expected` result in `Goal` holds.
- **Statechart (when stateful):** directly after `Goal` when the feature has UI/form states, async transitions, or status lifecycles per [statechart.md](statechart.md). Include a Mermaid `stateDiagram-v2` block and one-line invariant bullets. Omit for static changes.
- **Steps:** directly after `Goal` (or `Statechart`). Use a short title describing the user-visible outcome. Keep APIs and internal types in the implementation details. Each step has focused checks and one or more planned commit groups.
  - Group work on the same feature or function in one step, including its tests and setup. Merge dependent changes that deliver the same outcome together. Separate steps may edit the same file for different behaviors.
  - Give required shared setup its own step when multiple later steps need it and a focused check can verify it. List that setup step under `Blocked by` for each consumer.
  - Lines: `Do`, `Reuse`, `Test`, `Commit`, `Blocked by`, `Files`.
  - `Do`: at most three bullets of behavior in plain words stating what the step will handle, not low-level code edits.
  - `Reuse`: cite the actual component, function and comparable caller flow at exact paths or symbols. Explain why a plausible candidate is unsuitable when diverging. A repo rule is guidance, while existing code is a precedent to verify.
  - `Blocked by`: list each prerequisite step and the specific output needed from it, or `none`. Example: `Step 1 — document editor navigation for the E2E assertion`. A unit-test-only step blocks E2E work only if it supplies required shared setup or data.
  - `Commit`: one message per cohesive category, in the confirmed format. For multiple categories, list the scope and message of each in integration order. Keep tests with the change they verify.
  - `Files`: list exact source and test paths in backticks (use `<span title="...">` tooltips only in `dev-view/plan.html`). Mark a deleted file `delete` and list it under `Deletions` using the same format.
  - `Test`: cite the Goal numbers and state what each check asserts. One check can verify multiple goals if it asserts each outcome. Name the public seam and focused runner, or the focused verification for shared setup. Use `none: no setup` when no runner exists and setup is outside scope. Name shared state or isolation relevant to parallel execution. Write and run each behavior's failing spec first when authorized.
  - Seams, temporary contracts, access-right changes, reusable project components, relative attachment paths (`attachments/{ticket}/...`), and precedents go in `<sub>` beside `Files`, only when the developer needs them.
- **Out of scope:** excluded work, or `None.`.
- **Testing:**
  - Keep scope focused, and cover every changed component or module with behavior (including template bindings); if a changed file has no spec yet, plan a new spec beside it focused on the changed behavior. One line each on what it catches and misses; approving the plan confirms them.
  - `E2E:` the scenario in plain words (create a new e2e spec when none exists for the area). Use `none` only when there is no E2E setup (`none: no setup`), the change has no UI or user-flow impact, or the user explicitly skips E2E — never set `none` just because no prior spec exists. E2E runs once, after the last step; this line is its only scope.
  - List exact prior art and spec paths in `<sub>` (use `<span title="...">` tooltips only in `dev-view/plan.html`).
- **Decisions:** at most seven choices that change scope or design, one line each; mention the diagnosis when it drove one. State the choice alone.
- **Deletions:** every deleted file, or `None.`. Approving the plan approves exactly these.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

## Implementation pipelines

List every executable step in exactly one pipeline. Each pipeline has an ID, an outcome, owned steps in order, write scope, prerequisites and shared resources. Name the output required from each dependency. Validate references, cycles and resource conflicts before requesting approval. Group work that shares ownership and must proceed in order. Mark independent pipelines eligible for parallel work and show the grouping in the HTML. `go-flow` executes this approved structure per [scheduling](../../go-flow/references/scheduling.md#approved-pipelines).

## Changes

- `agent-view/spec.md` becomes scope only through user approval.
- Ask before changing an approved plan; drop superseded scope outright.
- After merging, removing, or reordering steps, recheck every dependency against its required output. Update step numbers and references in the plan and checklist. Carry evidence forward only for unchanged behavior it still verifies.
