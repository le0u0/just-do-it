# Scope and Baseline

## Target

- **PR URL:** Resolve provider repository, PR number, target/base SHA and head SHA from PR metadata. Review the provider's PR diff, or an exact merge-base-to-head comparison for the same refs. Fetch missing objects only with authorization.
- **Single commit:** Resolve the exact target SHA and use its parent as base. Ask which parent for a merge commit unless the user specified it. A root commit uses the empty tree. A SHA given as an explicit baseline is instead the start of a branch comparison.
- **Branch or working tree:** Use the baseline and range below. Include applicable local changes only for the selected local checkout. A named branch outside that checkout uses its own resolved refs.
- **SSH repository URL:** Resolve repository identity and require an explicit PR, branch, commit or range. An SSH URL alone does not select work.

For PRs, commit targets and other immutable targets, bind all workers to the same repository, base, head and read source. Read the pinned Git objects or use a verified isolated snapshot. Follow callers, project rules and history from that source. Never use a different dirty checkout or run target code merely to fill a gap. If files or refs cannot be read, report incomplete coverage. Accept test evidence only when its recorded identity matches the reviewed target. Record the target and snapshot in the report and match them before reuse.

## Baseline order

1. User-supplied baseline.
2. `Reviewed from` SHA from the previous review of this target.
3. An evidenced Git parent, for a first review.
4. Ask when uncertain.

- Confirm the baseline resolves and the diff is not empty; otherwise stop and say so.
- If the original baseline is missing, invalid, or not an ancestor of `HEAD`, stop and ask before changing it.

## Range

- For a local checkout branch review, include commits after the selected start through `HEAD`, plus applicable staged, unstaged and untracked source or test changes.
- **Full:** use the original baseline for the first review, an explicit full-review request, and `go-flow` delivery.
- **Incremental:** on a changed snapshot in a direct re-review, start at the previous `Reviewed to` commit. Require matching original baseline and review inputs, an unchanged explicit tier choice if any, `Checkout clean: yes` on the previous report, and a previous commit that resolves and is an ancestor of `HEAD`. An incremental report can anchor the next incremental review under the same conditions.
- If those conditions fail, use a full review from the verified original baseline. A previous dirty checkout or a report without a recorded clean status leaves the previous reviewed commit insufficient as a comparison point.
- If the incremental range has no reviewable changes, report that and retain the last reviewed snapshot. A full delivery review still follows the full-review rule.

## Refs

- Resolve locally first. First review: reuse a caller-supplied plan's `Initial baseline` when it matches this checkout.
- Fetch only when a ref is missing locally or a remote comparison is asked; never enumerate remote branches.

## Parent branch

- Never infer it from the branch name: a branch created from A compares with A.
- Check reflog and candidate ancestry; a tracking branch is not proof. Still ambiguous: ask one question.

## Exclude

- Ignored files, generated or build output, dependencies, reports, screenshots, traces.
