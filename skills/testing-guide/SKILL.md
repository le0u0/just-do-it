---
name: testing-guide
description: 'Write the manual testing guide for a finished ticket as a single HTML QA page, for a tester who knows nothing about the code. Use for "write the testing guide", "QA page" or "test steps for the tester".'
effort: medium
metadata:
  tier: standard
---

# Testing Guide

Report per [reports.md](../manager/references/reports.md). Return questions as `Open`.

1. Gather `plan.md` and the diff from the plan's initial baseline to find what changed for users. Take the ticket key and link from the plan's `Requirement source`. Use the screen names users see, with no file paths or component names.
2. Write the guide as one data file, `state/testing-guide.data.json` in the branch folder, per [guide-format.md](references/guide-format.md): setup, groups, tests. Behaviours in the diff or plan that no test covers, and tests that cannot be done by hand (fetch failure, timing), go to `Open` for the user. Add or drop no test without the user's answer.
3. Write a generator, `state/testing-guide.generate.*` in the branch folder, that renders that data into the page, and run it. The generated files are never hand-edited; a later change, such as a new line or test, goes into the data, then regenerate. With both files present, reuse them.
   - Output: `testing-guide-{short-description}.html` in the branch folder, per [html-page.md](references/html-page.md). No Markdown copy.
4. Verify the page per [verify.md](references/verify.md).
5. Reply with the path, what you verified, and what you could not verify.

Done when every acceptance criterion in `plan.md` is covered by a test, every step is 15 words or fewer, the page comes from the data file, and each check in `verify.md` is `pass`, `fail` or `not verified`.
