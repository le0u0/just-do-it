# Scope and Baseline

## Baseline order

1. User-supplied baseline.
2. `Reviewed to` SHA from the caller's previous review.
3. An evidenced Git parent, for a first review.
4. Ask when uncertain.

- Confirm the baseline resolves and the diff is not empty; otherwise stop and say so.
- Saved SHA missing, invalid, or not an ancestor of `HEAD`: stop and ask. Never widen the range.

## Range

- Changes after the baseline through `HEAD`, plus staged, unstaged, untracked source or test changes.
- Full plan scope from its initial baseline only when asked.

## Refs

- Resolve locally first. First review: reuse a caller-supplied plan's `Initial baseline` when it matches this checkout.
- Fetch only when a ref is missing locally or a remote comparison is asked; never enumerate remote branches.

## Parent branch

- Never infer it from the branch name: a branch created from A compares with A.
- Check reflog and candidate ancestry; a tracking branch is not proof. Still ambiguous: ask one question.

## Exclude

- Ignored files, generated or build output, dependencies, reports, screenshots, traces.
