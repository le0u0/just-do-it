# Checklist Format

Return the checklist after the plan, progress first, one item per step. Mark one current item; several only when they share no files or state. Add discovered work, delete an item only with approval, and untick invalidated work with a short reason. Follow the [writing rules](writing-rules.md); `Step notes` is one line per step.

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

The caller records progress in it after each step, including finding IDs and dispositions. List unrelated existing changes separately. On resume, compare the saved repository, branch, baseline, and HEAD with the checkout, invalidate stale evidence, keep the user's changes, and ask only when drift makes scope ambiguous.
