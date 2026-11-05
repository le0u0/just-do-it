---
name: to-test-md
description: 'Write the manual testing guide for a finished ticket as Markdown, for a reader who knows nothing about the code. Use for "write the testing guide", "test steps" or "QA guide".'
disable-model-invocation: true
---

# Testing Guide

Write the manual testing guide as Markdown. Run `to-test-html` afterwards for the HTML page.

## Input

- `plan.md` in the branch folder. Missing: ask for it, or for the requirements and the diff.
- The diff from the plan's initial baseline: what changed for users.
- The ticket key and link, from the plan's `Requirement source`.

## Steps

1. Read `plan.md` and the diff. Use screen names users see: no file paths, no component names.
2. Write the guide per [guide-format.md](references/guide-format.md): setup, groups, tests.
3. Save as `testing-guide-{short-description}.md` in the branch folder. Update in place when it exists.
4. Return under `Open` for the user:
   - Behaviours in the diff or plan that no test covers.
   - Tests that cannot be done by hand, such as fetch failure or timing.
5. Add or drop no test without the user's answer.
6. Reply with the path and `Open`.

## Storage

- Branch folder: `~/.just-do-it/{project}/{branch}/`.
- `{branch}`: `git branch --show-current`, each `/` replaced by `-`.
- Find it: glob `~/.just-do-it/*/{branch}`. No match: ask which project.
- Read `state/triage.md` there for the `Linked:` line.

## Done when

- Every acceptance criterion in `plan.md` has a test.
- Every step is 15 words or fewer.
