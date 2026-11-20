---
name: go-review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and confirmed goal, and write dev-view/review.md. Use for "review my branch" or "review this diff".'
---

# Review

Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user. Write the completed report to `~/.just-do-it/{project}/{branch}/dev-view/review.md` (unless the user explicitly asks for terminal-only output).

Run in the main thread as coordinator: confirm the review goal and plan, pick the tier, start the review agents, assemble and save `dev-view/review.md`. Never read hunks yourself; agents read the code.

Start the review team for every review. If an agent is unavailable or cannot start, report blocked and stop; never perform its review role yourself.

## 1. Fetch

Start one review-owned fast Fetch worker per [agents.md](references/agents.md). Give it [fetch.md](references/fetch.md) and request only missing inputs:

- Ticket text, when the requirement is a ticket URL or key (and `agent-view/research.md` is absent), including linked tickets.
- Baseline evidence, unless the user or `agent-view/plan.md` supplied the baseline.
- Diff facts for the range.
- File text of `REVIEW.md`, for the risky paths it marks.
- Paths of project-local review skills in `.claude/skills/` and `.agents/skills/` (if any).
- Re-review: delta files from `Reviewed to`, checked against the files of open `TODO` findings in `dev-view/review.md`.

Decide from its facts yourself: the baseline per [scope-baseline.md](references/scope-baseline.md), then the tier.

## 2. Goal, review plan, and inputs

- **Goal & review plan (direct run):** Read `agent-view/plan.md` and `agent-view/research.md` when present. If `agent-view/plan.md` is missing or the review goal/target is unclear when running `go-review` directly, **grill the user on the goal and target scope, confirm a concise review plan** (and update `public/glossary.md` if unknown domain terms arise per [public-docs.md](../go-setup/references/public-docs.md)) before launching the hunters.
- **Previous review:** read `dev-view/review.md` if it already exists.
- **Test references:** check whether `dev-view/ut.md` and `dev-view/e2e.md` exist in the branch folder. Reference them in `## Tests` per [report-format.md](references/report-format.md) (leave the reference empty if the file does not exist).
- **Tier:** from the diff facts, per [agents.md](references/agents.md). The caller or user may name a tier; it wins.

## 3. First review

1. Start every hunter of the tier in parallel, per [agents.md](references/agents.md) and [hunter.md](references/hunter.md).
2. Collect their candidates. Quick: the single hunter returns findings; skip step 3.
3. Start one verifier with all candidates, per [verifier.md](references/verifier.md).
4. Number the verifier's findings by severity; place them per [report-format.md](references/report-format.md). Keep the verifier's dropped lines with the review result.

## 4. Re-review

Given an existing `dev-view/review.md`, update it in full. Delta: `git diff <Reviewed to>` through the working tree. Uncommitted work has no SHA: a `Diff fingerprint` equal to the previous one means no delta; otherwise hunt only files the fixes touched.

1. **Round cap:** previous `Round` is 3 or more: run 4.2 and 4.4 only; hunt nothing new. Say in `Open`: `round cap: reconsider the approach`.
2. **Open findings:** a `TODO` whose file the delta files leave untouched stays as written. The rest go to one recheck agent per [agents.md](references/agents.md).
   - `fixed`: move to `RESOLVED` as one `Done` line (at most 20 words) plus `Status: fixed (<short SHA>)`; uncommitted fix: `fixed, not tested`.
   - `open`: keep its two lines.
3. **New code:** hunt the delta only, at the tier the delta's own diff facts give. Pass every earlier finding (all sections) as known.
4. New findings numbered after the last. Update `Issue Count` (open `TODO` only), `Reviewed to`, `Round`, and refresh `## Tests` references to `dev-view/ut.md` and `dev-view/e2e.md` if present.

- A reported test failure in `dev-view/ut.md` or `dev-view/e2e.md` that the fix does not address is a finding; send it to the hunters as a lead.

## 5. Deliver

- Save the full report to `~/.just-do-it/{project}/{branch}/dev-view/review.md` per [report-format.md](references/report-format.md) and report the saved path and open issue counts by severity. Keep findings and dropped lines in the saved report.
- `go-fix` applies fixes when the caller or user asks for them.
