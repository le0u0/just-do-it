# HTML Page (`dev-view/testing-guide.html`)

Generate a single-file, self-contained HTML QA page that testers tick through offline. Start from the [working QA example](../../../examples/example-project/PROJ-9999-prevent-duplicate-save/dev-view/testing-guide.html). Replace its `DATA` with the guide data and preserve the embedded PDF bundle and license notices.

## Format & Design

- **Single static HTML file**: inline CSS and vanilla JS, no external framework, build step, or network request. Works offline via `file://` and as a ticket attachment.
- **Theme**: warm neutrals matching [`html-render.md`](../../go-setup/references/html-render.md) (`--bg:#faf7f2`, `--surface:#fff`, `--text:#2b2622`, `--grey:#6b625a`, `--border:#ddd3c6`, `--accent:#faaa6c`, `--pass:#1f7a3d`, `--pass-bg:#e3f4e8`, `--fail:#b3261e`, `--fail-bg:#fbe5e3`).
- **Typography**: title `28px`; group heading `24px` bold; test title `16px` semibold; steps `16px`; left nav `"Tests"` `18px` bold, group labels `16px` bold, links `14px` indented, current item highlighted on `--accent`. Max content width `75ch`.
- **Responsive**: 2-column layout (`260px` sticky left nav + scrollable main panel) on desktop (`1280px`), stacked wrapped nav bar on mobile (`390px`), zero horizontal scroll. Respect `prefers-reduced-motion`.

## Structure

1. **Header**:
   - Language segmented switch top-right (`English` / `繁體中文`, `aria-pressed`, hidden when single-language).
   - `<h1>` feature title.
   - Lead line: `<a href="{link}" target="_blank" rel="noopener noreferrer">{ticket}</a> QA Test`.
   - Optional `Related:` links line.
   - Hint line: *"Found an issue? Mark it Fail and add a note. Then export the report and attach it to the ticket."*
2. **Progress bar**:
   - Fill bar (`%` of marked tests), count text (`"P pass · F fail · U not marked"`), primary **Export report** button, and **Reset** button (with confirmation prompt).
   - Red storage-fallback warning banner (shown only when `localStorage` is blocked).
3. **Navigation & Body**:
   - Left `<nav>`: `"Tests"`, group headings, and `#case-id` links showing `✓` (pass) or `✗` (fail) badge; scroll-spy highlights the active test at ~30% viewport height (and last test at bottom).
   - `<main>`: optional `Before you start` setup list, then purpose groups (`<h2>` with a thin top divider except the first, plus `<p class="why">` one-line reason).
   - Each test card (`<article class="test" id="{id}">`):
     - Header row: `<h3>Test N: Title</h3>` + `Pass` / `Fail` segmented toggle (`aria-pressed`).
     - Optional italic note.
     - Numbered `<ol class="steps">` with bold screen prefix (`<b class="sc">Screen:</b> action`).
     - Tinted `You should see:` box (`background:#f6efe3; border-left:3px solid var(--accent)`).
     - Tester note `<textarea>` shown **only** when marked `Fail` (retaining its text if toggled).

## Bilingual Data (`en` + `zh`)

1. Format the guide data as a **multi-line, pretty-printed** `const DATA = {\n  ...\n};` JSON object at the top of `<script>` (never a single minified line, so later edits only read and `edit_file` the changed lines):
   - Serialize `<` in JSON strings as `\u003c` before embedding JSON in the script element. Escape untrusted text and validate URLs when rendering into HTML.
   - `ticket`, `link`, `slug`, `languages: ["en", "zh"]`, `related`, `title: {en, zh}`, `setup: [{text: {en, zh}}]`, `groups: [{name: {en, zh}, why: {en, zh}, tests: [{id, title: {en, zh}, note, steps: [{en, zh}], expect: {en, zh}}]}]`.
   - Assign a stable unique `id` (`case-1`, UUID, etc.) per test. When updating an existing `dev-view/testing-guide.html`, read only its `DATA` lines first and edit the changed lines in place, preserving matching test `id`s so saved `localStorage` results survive updates.
2. **Translate (`zh`)**:
   - Spawn one `standard` subagent per [host mapping](../../go-flow/references/agents.md#host-mapping) with the repository path and English strings.
   - It checks the repository's translation files (`i18n`, `locales`, `zh*.json`) first, then `~/.just-do-it/{project}/public/glossary.md` and `agent-view/{research,plan}.md`. Unmatched terms are translated plainly and reported as `guess` under `Open`.
3. Every UI label and guide string renders `<span data-l="en">...</span><span data-l="zh">...</span>` and toggles active language via `[data-l]:not([data-l="<lang>"]){display:none}` while persisting language choice in `localStorage`.

## Saving progress & Exporting report

- **State persistence**: save `{results, notes}` under `localStorage` key `qa-v2-[ticket,slug]`. If `localStorage` throws (blocked in sandboxed `file://` or preview panes), fall back to `window.name` and unhide the red warning banner.
- **Export report**: clicking **Export report** directly downloads `{ticket}-qa-report-YYYY-MM-DD.pdf` in the selected language. Keep the full-width title, ticket and date, failed-test count, failed cards, highlighted expected results, and tester notes. Show a localized `No failed tests.` message when none failed. Omit passed and unmarked counts and cases.
- Keep the compressed PDF library and its license notices inline for offline export. PDF export requires `DecompressionStream`. Report export failures inline.
