# Scope and Baseline

## Baseline order

1. User-supplied baseline.
2. `Reviewed from` SHA from the previous review of this target.
3. An evidenced Git parent, for a first review.
4. Ask when uncertain.

- Confirm the baseline resolves and the diff is not empty; otherwise stop and say so.
- If the original baseline is missing, invalid, or not an ancestor of `HEAD`, stop and ask before changing it.

## Range

- Include commits after the selected start through `HEAD`, plus staged, unstaged, and untracked source or test changes.
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
