---
name: go-review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and the supplied objective or bug, and return the review report in the reply. Use for "review my branch" or "review this diff".'
---

# Review

Report as the caller specifies. The report is the reply; write no file.

## 1. Inputs

- **Requirements:** caller-supplied text, path, ticket URL, or plan. Never from a ticket key or branch name. None or unreachable: note no requirement, still apply **Correctness** in [checks.md](references/checks.md).
- **Previous review:** earlier report from the caller, if any.
- **Baseline:** [scope-baseline.md](references/scope-baseline.md).

## 2. Re-review

Given a previous review, return it updated in full:

- Recheck each `TODO`. Fixed: move to `RESOLVED` as one `Done` line (at most 20 words) plus `Status: fixed (<short SHA>)`. Still present: keep its two lines.
- New findings only in changes after `Reviewed to`, numbered after the last.
- Update `Issue Count` (open `TODO` only), `Manual review`, `Reviewed to`. Leave `Tests` as written.
- A reported test failure the fix does not address is a finding; check by reading code.

## 3. Review pass

- Code only; run no tests.
- Read the scoped diff once, then changed functions and immediate callers. Cover every hunk.
- Method: the repository's own review skill (method only, not its scope, delivery, format), else [review-method.md](references/review-method.md).
- Apply the relevant [checks.md](references/checks.md) and project rules per [project-references.md](references/project-references.md).
- Check changed code follows comments in modified files.
- Risky hunk (changed condition, removed guard): `git log -L` or `git blame`; flag a change that undoes earlier intent.

## 4. Filter

- Keep findings introduced or exposed by the change, on touched lines, confirmed real and hit in practice.
- Omit: intentional-looking changes, lint-ignored issues, unreachable cases, style preferences, pure renames, tooling-enforced issues.
- A missing contract limits one finding, never the review.
- Deduplicate by root cause.

## 5. Reply

1. Pick `Manual review` places per [report-format.md](references/report-format.md).
2. End with the standard report: `Changed` is `none`; `Open` gives open issue count by severity.

- Fix nothing; findings get fixed only after the user selects them, with `go-fix`.
