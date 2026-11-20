---
name: to-test-doc
description: 'Write the manual QA testing guide for a finished ticket as Markdown (dev-view/testing-guide.md) or a single-file interactive HTML QA page (dev-view/testing-guide.html). Asks whether to generate md or html when not specified.'
disable-model-invocation: true
---

# Testing Guide (`to-test-doc`)

Generate the manual QA testing guide as Markdown (`dev-view/testing-guide.md`), interactive single-file HTML (`dev-view/testing-guide.html`), or both.

## Storage

1. Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
2. If the user did not specify `md` or `html` in their request, **ask whether they want Markdown (`testing-guide.md`), HTML (`testing-guide.html`), or both**.

## Input

- `agent-view/plan.md` in the resolved branch directory, or a supplied plan/requirements and diff. Missing: ask for requirements and diff; use their acceptance criteria in place of the plan.
- The diff from the plan's initial baseline, or the supplied diff when there is no plan.
- Ticket key and URL from `agent-view/plan.md` and `agent-view/research.md` (or supplied requirements); if the URL is unavailable, omit the link and report it in `Open`.
- Known terms from `public/glossary.md` when present.

## 1. Markdown Guide (`dev-view/testing-guide.md`)

Run this step when generating Markdown, or when HTML is requested and `dev-view/testing-guide.md` does not exist yet:

1. Read the plan, research brief, and diff. Use screen names users see—no file paths or component names.
2. Write the guide per [guide-format.md](references/guide-format.md).
3. Save to `~/.just-do-it/{project}/{branch}/dev-view/testing-guide.md` (or print in the terminal only when explicitly requested).
4. Include `Open` with the saved path:
   - Behaviors in the diff, plan, or supplied requirements that no test covers.
   - Tests that cannot be done by hand, such as fetch failure or timing.
5. Change the test list only on the user's answer.

## 2. HTML QA Page (`dev-view/testing-guide.html`)

Run this step when generating HTML:

1. Read `dev-view/testing-guide.md` (generating it via Step 1 first if missing). Check any existing `dev-view/testing-guide.html` first so test IDs can be preserved.
2. Convert the guide to English data JSON per [data-shape.md](references/data-shape.md).
3. Translate per `Translate` in [data-shape.md](references/data-shape.md): start one `fast` subagent per [host mapping](../go-flow/references/agents.md#host-mapping) to add `zh` to every text. If the translation worker cannot start, report blocked and write no HTML.
4. Fill [qa-template.html](references/qa-template.html) and inject `assets/pdf-bundle.html` at `<!--PDF_BUNDLE-->` per [data-shape.md](references/data-shape.md) (never read `assets/pdf-bundle.html` into LLM context) and follow [html-page.md](references/html-page.md).
5. Verify per [verify.md](references/verify.md).
6. Save as `~/.just-do-it/{project}/{branch}/dev-view/testing-guide.html` and report the path and verification status.

## Rules

- When updating an existing HTML guide after content changes, update `dev-view/testing-guide.md` first, then regenerate `dev-view/testing-guide.html`.

## Done when

- The requested format (`dev-view/testing-guide.md`, `dev-view/testing-guide.html`, or both) is saved and its path is reported.
- Every acceptance criterion has a test (or is listed in `Open` if untestable by hand), and every step is 15 words or fewer.
- When HTML is generated, the page opens with no console error and each `verify.md` check is reported as `pass`, `fail`, or `not verified`.
