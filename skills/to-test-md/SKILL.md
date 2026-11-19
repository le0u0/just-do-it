---
name: to-test-md
description: 'Write the manual testing guide for a finished ticket as Markdown, for a reader who knows nothing about the code. Use for "write the testing guide", "test steps" or "QA guide".'
disable-model-invocation: true
---

# Testing Guide

Write the guide as Markdown.

## Input

- The current plan from the session, a supplied path, or `plan.md` in the resolved task directory. Missing: ask for it, or for requirements and diff; use their acceptance criteria in place of the plan.
- The diff from the plan's initial baseline, or the supplied diff when there is no plan.
- Ticket key from the plan's `Requirement source`. Get its URL from the matching source in `state/triage.md` or supplied requirements; if unavailable, omit the link and report it in `Open`.

## Steps

1. Read the plan and diff, or the supplied requirements and diff. Use screen names users see: no file paths or component names.
2. Write the guide per [guide-format.md](references/guide-format.md).
3. Deliver `testing-guide-{short-description}.md` per [Output delivery](../justaway/references/storage.md#output-delivery).
4. Include `Open` with the saved path or printed guide:
   - Behaviours in the diff, plan or supplied requirements that no test covers.
   - Tests that cannot be done by hand, such as fetch failure or timing.
5. Change the test list only on the user's answer.

## Done when

- Every acceptance criterion from the plan or supplied requirements has a test, or is listed in `Open` if it cannot be tested by hand.
- Every step is 15 words or fewer.
