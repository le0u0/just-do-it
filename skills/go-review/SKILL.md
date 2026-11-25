---
name: go-review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and confirmed goal, write agent-view/review.md (linking agent-view/ut.md and agent-view/e2e.md), and render dev-view/review.html. Use for "review my branch" or "review this diff".'
---

# Review

Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user. Write the agent markdown report to `agent-view/review.md` and render the human-readable page at `dev-view/review.html` (unless the user explicitly asks for `.md` only or terminal-only output).

Run in the main thread as coordinator: confirm the review goal and plan, pick the tier, start the review agents, assemble `agent-view/review.md` and `dev-view/review.html`. Never read hunks yourself; agents read the code.

Review only. Leave source and tests untouched. Deliver the report and stop without invoking `go-fix`. The `go-flow` coordinator owns any authorized automatic fix loop.

For a ticket review, require a matching ready spec or complete inline requirements before gathering review inputs. This applies to a ticket key or URL in the request or plan and a blocked brief for the active ticket. Otherwise invoke [to-spec](../to-spec/SKILL.md) and follow its [blocked-spec procedure](../to-spec/SKILL.md#blocked-spec) if the requirements are unavailable.

Read any previous review of this target. Select full or incremental coverage per [scope and baseline](references/scope-baseline.md#range). In the flow's intermediate fix loop, `go-fix` owns focused checks.

Start the review team for each new pass. If a required agent cannot start, report blocked and stop; never perform its review role yourself.

## 1. Fetch

Start one review-owned fast Fetch worker per [agents.md](references/agents.md). Give it [fetch.md](references/fetch.md) and request only missing inputs:

- Baseline evidence, unless the user or `agent-view/plan.md` supplied the baseline.
- Diff facts for the applicable range. For a possible incremental review, include the previous reviewed commit's ancestry.
- Current checkout snapshot and clean status per [fetch.md](references/fetch.md).
- File text of `REVIEW.md`, for the risky paths it marks.
- Paths of project-local review skills in `.claude/skills/` and `.agents/skills/` (if any).

Decide from its facts yourself: the original baseline, then the selected comparison range and tier.

## 2. Goal, review plan, and inputs

- **Goal & review plan (direct run):** Read `agent-view/plan.md` and `agent-view/spec.md` when present. If `agent-view/plan.md` is missing or the review goal/target is unclear when running `go-review` directly, **grill the user on the goal and target scope, confirm a concise review plan** (and update `public/glossary.md` if unknown domain terms arise per [public-docs.md](../go-setup/references/public-docs.md)) before launching the hunters.
- **Test references:** compare each available UT/E2E report's snapshot to the reviewed checkout snapshot. Label mismatched or missing snapshots `stale`. Only matching reports can support a pass or fail for the reviewed version.
- **Tier:** Standard or Deep from the selected diff facts, per [agents.md](references/agents.md). An explicit request may select either supported tier.
- **Reuse matching coverage:** before dispatching hunters, verify that baseline, snapshot, and review inputs match a report with recorded coverage. Use its recorded tier for the same snapshot unless the user selected another tier. A full review request requires `Coverage: full`. Reuse the findings, refresh test and acceptance evidence, and keep the round number and coverage. An explicit fresh review requests a new pass.
- **Round cap:** before a new full pass, require explicit user authorization when the existing `Round` is 3 or more. Keep its original snapshot until a new full pass completes.

## 3. Review the selected diff

1. Start every hunter of the tier in parallel, per [agents.md](references/agents.md) and [hunter.md](references/hunter.md).
2. Collect their candidates.
3. Start one verifier with all candidates, per [verifier.md](references/verifier.md).
4. Sort the verifier's findings by severity and number only `TODO` entries per [report-format.md](references/report-format.md). Keep the verifier's dropped lines with the review result.
5. Before saving, check that the checkout snapshot still matches the one dispatched to the hunters. If collection fails or the snapshot changed, report the interruption and keep the previous review. Record the successful pass's range and coverage. Increment `Round` only after a stable full pass.

## 4. Re-review

Given an existing `agent-view/review.md`, preserve the original baseline and reconcile findings before delivery. For an incremental pass, hunters review changes since the last reviewed commit and trace their effects into relevant callers.

1. **Open findings:** recheck each prior `TODO` against the current code per [agents.md](references/agents.md). Keep the numbers of items still in `TODO`. Move confirmed fixes and their evidence to `RESOLVED` without a number.
2. **New or recurring findings:** match the newly verified findings to the previous report by defect, not by number. Merge duplicates and preserve explicit user dispositions when the trigger and impact are unchanged. Assign the next unused `TODO` number to new or reopened findings.

- A reported test failure in `agent-view/ut.md` or `agent-view/e2e.md` that the fix does not address is a finding; send it to the hunters as a lead.

## 5. Deliver

- For a ticket review, map each approved `Expected` result or equivalent outcome in an earlier plan to its current evidence and verdict per [report-format.md](references/report-format.md#fields). Report missing coverage even if every test ran successfully.
- Save `agent-view/review.md` per [report-format.md](references/report-format.md) and render the interactive human-readable page at `dev-view/review.html` per [html-render.md](../go-setup/references/html-render.md). Report the saved path and open issue counts by severity.
