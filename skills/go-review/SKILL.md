---
name: go-review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and the supplied objective or bug, and return the review report in the reply. Use for "review my branch" or "review this diff".'
---

# Review

Report as the caller specifies. The review report itself is your reply; write no file for it.

## 1. Inputs

- **Requirements:** what the caller supplied (text, a named file path, a ticket URL, or a plan). Take them from that source alone, never from a ticket key or branch name, and keep them out of the report. With none, or when the ticket is unreachable, note no requirement and still apply the **Correctness** check in [checks.md](references/checks.md).
- **Previous review:** the earlier report the caller supplied, as text or a named path, if any.
- **Baseline:** [scope-baseline.md](references/scope-baseline.md).

## 2. Re-review

When the caller supplied a previous review for this repository and branch, return it updated in full:

- Recheck each `TODO`. Fixed: move it to `RESOLVED` as one `Done` line of at most 20 words plus `Status: fixed (<short SHA>)`. Still present: keep its two lines, each at most 20 words.
- Look for new findings only in changes after `Reviewed to`, numbered after the last one.
- Update `Issue Count` (open `TODO` only), `Manual review` and `Reviewed to`; leave `Tests` as the caller wrote it.

## 3. Review pass

Review the code only; the caller writes the unit and e2e results into `Tests`. Leave `Tests` as not run on a first pass; you run no tests. On a re-review, read the test results in the previous review; for each reported failure, check by reading code that the developer's fix addresses it.

Do the review pass:

- Read the scoped diff once, then changed functions and immediate callers as needed. Cover every changed hunk.
- When the repository has its own review skill, such as a review skill in `.claude/skills/` or `.agents/skills/`, use its method only, not its scope, delivery, or format. Otherwise use [review-method.md](references/review-method.md). Always apply the relevant [checks.md](references/checks.md), and the project's own rules per [project-references.md](references/project-references.md).
- Check that changed code follows guidance in the comments of the modified files.
- For a risky hunk, such as a changed condition or a removed guard, run `git log -L` or `git blame` on it and flag a change that undoes earlier intent. Skip this for other hunks.

On a re-review, a reported test failure in `Tests` that the fix does not address is a finding.

## 4. Filter

- Keep only findings introduced or exposed by the change, on lines the change touched.
- Keep a finding only when you confirmed it is real and will be hit in practice; a guess sends the fix after a false lead.
- Omit changes that look intentional, issues silenced by a lint-ignore comment, unreachable cases, style preferences, pure renames that keep behavior, and issues tooling enforces. A missing contract limits one finding, never the review.
- Deduplicate by root cause.
- Keep source read-only; add no `TODO` or `FIXME` comments to code.

## 5. Reply

- Pick the places worth a human read for `Manual review`, per [report-format.md](references/report-format.md).
- Reply with the whole review report in that format. Write no `review.md` or `checklist.md`; the caller saves them.
- End with the standard report: `Changed` is `none`, and `Open` gives the open issue count by severity. Say "No actionable findings" only after reading every hunk.
- Fix nothing and start no fix job. A review ends at the report; findings get fixed only after the user selects them, with `go-fix`.
- Suggest no follow-up skill.
