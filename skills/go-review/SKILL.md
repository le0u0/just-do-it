---
name: go-review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and the supplied objective or bug, and return the review report in the reply. Use for "review my branch" or "review this diff".'
---

# Review

- Report as the caller specifies.
- The review report is the reply; write no file for it.

## 1. Inputs

- **Requirements:** caller-supplied text, named file path, ticket URL, or plan.
  - Take them from that source alone, never from a ticket key or branch name.
  - Keep them out of the report.
  - With none, or an unreachable ticket: note no requirement, still apply **Correctness** in [checks.md](references/checks.md).
- **Previous review:** the earlier report the caller supplied, as text or named path, if any.
- **Baseline:** [scope-baseline.md](references/scope-baseline.md).

## 2. Re-review

With a previous review for this repository and branch, return it updated in full.

- Recheck each `TODO`:
  - Fixed: move to `RESOLVED` as one `Done` line of at most 20 words plus `Status: fixed (<short SHA>)`.
  - Still present: keep its two lines, each at most 20 words.
- Find new findings only in changes after `Reviewed to`; number them after the last one.
- Update `Issue Count` (open `TODO` only), `Manual review`, `Reviewed to`.
- Leave `Tests` as the caller wrote it.
- Read the test results in the previous review. A reported failure the fix does not address is a finding; check by reading code.

## 3. Review pass

- Review code only. Run no tests. Leave `Tests` as not run on a first pass; the caller fills it.
- Read the scoped diff once, then changed functions and immediate callers as needed. Cover every changed hunk.
- Method:
  - Repository has its own review skill (`.claude/skills/`, `.agents/skills/`): use its method only, not its scope, delivery, or format.
  - Otherwise: [review-method.md](references/review-method.md).
- Always apply the relevant [checks.md](references/checks.md) and the project's rules per [project-references.md](references/project-references.md).
- Check changed code follows guidance in the comments of modified files.
- Risky hunk (changed condition, removed guard): run `git log -L` or `git blame`; flag a change that undoes earlier intent. Skip for other hunks.

## 4. Filter

- Keep findings introduced or exposed by the change, on touched lines.
- Keep only findings confirmed real and hit in practice. A guess sends the fix after a false lead.
- Omit:
  - changes that look intentional
  - issues silenced by a lint-ignore comment
  - unreachable cases
  - style preferences
  - pure renames that keep behavior
  - issues tooling enforces
- A missing contract limits one finding, never the review.
- Deduplicate by root cause.
- Keep source read-only; add no `TODO` or `FIXME` comments.

## 5. Reply

1. Pick places worth a human read for `Manual review`, per [report-format.md](references/report-format.md).
2. Reply with the whole report in that format. Write no `review.md` or `checklist.md`; the caller saves them.
3. End with the standard report: `Changed` is `none`; `Open` gives open issue count by severity.
4. Say "No actionable findings" only after reading every hunk.

- Fix nothing, start no fix job. Findings get fixed only after the user selects them, with `go-fix`.
- Suggest no follow-up skill.
