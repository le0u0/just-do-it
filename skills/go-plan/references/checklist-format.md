# Checklist Format

Return the checklist after the plan, per the [writing rules](writing-rules.md).

## Rules

- Progress first, one item per step.
- Mark one current item. Several only when they share no files or state.
- Add discovered work. Delete an item only with approval.
- Untick invalidated work with a short reason.
- `Step notes`: one line per step.

```markdown
# PROJ-123 checklist

## Implementation

- [x] Step 1: clamp remaining count
- [ ] Step 2: hide empty list - current

## Step notes

- Step 1: Spec failed, then passed after clamp.

## Task files

<sub>Modified: `src/example.test`</sub>

## Evidence

<sub>Unit: expected failure, then pass; command and checkout recorded here.</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>Initial baseline: a1b2c3d<br>Current HEAD: a1b2c3d<br>Current step: 2 of 2<br>Next action: approve Step 2</sub>
```

## After the checklist is returned

- The caller records progress in it after each step, including finding IDs and dispositions.
- List unrelated existing changes separately.
- On resume: compare the saved repository, branch, baseline, and HEAD with the checkout; invalidate stale evidence; keep the user's changes; ask only when drift makes scope ambiguous.
