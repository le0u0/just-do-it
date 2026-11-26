---
name: to-test-doc
description: 'Write the manual QA testing guide for a finished ticket as a single-file interactive HTML QA page (dev-view/testing-guide.html) by default, or Markdown (dev-view/testing-guide.md) when requested.'
disable-model-invocation: true
---

# Testing Guide (`to-test-doc`)

Generate the manual QA testing guide. Defaults to the interactive single-file HTML QA page (`dev-view/testing-guide.html`) unless the user explicitly asks for Markdown (`dev-view/testing-guide.md`).

## Storage

1. Resolve `~/.just-do-it/{project}/{branch}/` per [storage.md](../go-setup/references/storage.md). If the branch folder does not exist under `~/.just-do-it/*/{branch}`, run `go-setup` first to confirm `{project}` with the user.
2. Output format:
   - **Default:** generate `dev-view/testing-guide.html`.
   - **User prefers `.md` (or asks for both):** generate `dev-view/testing-guide.md` (and `dev-view/testing-guide.html` if both).

## Input

- `agent-view/plan.md` in the resolved branch directory, or a supplied plan/requirements and diff. Missing: ask for requirements and diff; use their goal/criteria in place of the plan.
- The diff from the plan's initial baseline, or the supplied diff when there is no plan.
- Ticket key and URL from `agent-view/plan.md` and `agent-view/spec.md` (or supplied requirements); if the URL is unavailable, omit the link and report it in `Open`.
- Known terms from `public/glossary.md` when present.

## 1. Draft Guide Content

1. Read the plan, research brief, and diff. Use screen names users see—no file paths or component names.
2. Structure the test cases per [guide-format.md](references/guide-format.md).
3. If the user requested Markdown (`dev-view/testing-guide.md`), save it to `~/.just-do-it/{project}/{branch}/dev-view/testing-guide.md`.

## 2. HTML QA Page (`dev-view/testing-guide.html`, default)

Run this step by default (unless the user asked for `.md` only):

1. Check any existing `dev-view/testing-guide.html` first so test IDs can be preserved.
2. Translate and build the single-file HTML page per [html-page.md](references/html-page.md):
   - Format `const DATA = { ... };` as **multi-line pretty-printed JSON** at the top of `<script>` so future small updates only need to read and `edit_file` the changed lines. Set `hasMd: true` only when `dev-view/testing-guide.md` is also generated.
   - Start one `standard` subagent per [host mapping](../go-flow/references/agents.md#host-mapping) to add `zh` translations to every text. If the translation worker cannot start, report blocked and write no HTML.
   - Embed the offline PDF bundle and license notices by running `python3 skills/to-test-doc/scripts/embed_pdf.py <testing-guide.html>`.
3. Verify per [verify.md](references/verify.md).
4. Save as `~/.just-do-it/{project}/{branch}/dev-view/testing-guide.html` and report the path, verification status, and `Open` coverage gaps (behaviors no test covers or tests that cannot be done by hand).

## Done when

- `dev-view/testing-guide.html` (or `dev-view/testing-guide.md` when `.md` was requested) is saved and its path is reported.
- Each `Expected` result in `Goal` (or equivalent supplied requirement) has a test or appears in `Open` if untestable by hand. Each test step is 15 words or fewer.
- When HTML is generated, `const DATA` is multi-line for low-token partial edits, the page opens with no console error, and each `verify.md` check is reported as `pass`, `fail`, or `not verified`.
