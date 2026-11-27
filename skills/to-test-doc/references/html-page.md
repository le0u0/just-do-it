# HTML Page (`dev-view/testing-guide.html`)

Generate a single-file, self-contained HTML QA page that testers tick through offline. Inherit the shared warm-neutral tokens, typography, and escaping rules from [html-render.md](../../go-setup/references/html-render.md) (using `--muted` instead of `--grey`, and `--surface-alt` instead of hardcoded `#f6efe3`), then apply the QA-specific layout, data schema, and offline PDF export rules below.

## 1. Layout & QA-Specific CSS

- **2-column desktop + stacked mobile (`390px`)**: `260px` sticky left `<nav>` + scrollable `<main>` (`max-width: 75ch` on `#doc`), collapsing to a single-column stacked wrapped nav below `768px` with zero horizontal scroll.
- **Left `<nav>`**: `"Tests"` `18px` bold, group labels `16px` bold, `#case-id` links `14px` indented, active link `.cur` highlighted on `var(--accent)`.
- **Respect `prefers-reduced-motion`**: disable `.bar>i` width transition when reduced motion is requested.

```css
.layout{flex:1;min-height:0;width:100%;max-width:1180px;margin:0 auto;padding:0 16px;display:grid;grid-template-columns:260px minmax(0,1fr);gap:32px}
nav,main{overflow:auto;padding:16px 0 48px}
#doc{max-width:75ch}
nav a.cur{background:var(--accent);color:var(--text);font-weight:600}
.expect{background:var(--surface-alt);border-left:3px solid var(--accent);padding:10px 12px;border-radius:0 8px 8px 0}
@media(max-width:768px){
  body{height:auto;overflow:auto}
  .layout{display:block}
  nav,main{overflow:visible;padding:12px 0}
  nav{display:flex;flex-wrap:wrap;gap:6px;border-bottom:1px solid var(--border)}
  nav .nt,nav .ng{flex:1 0 100%;margin:6px 0 2px}
  nav a{margin-left:0}
  h1{padding-right:0}
  .lang{position:static;margin-bottom:8px}
}
@media(prefers-reduced-motion:reduce){.bar>i{transition:none}}
```

## 2. Structure & Conditional Elements

1. **Header**:
   - Language segmented switch top-right (`#lang`, `aria-pressed`), hidden (`#lang[hidden]`) when `DATA.languages.length <= 1`.
   - `<h1>` feature title.
   - Lead line: validated `https?://` `<a href="{link}" target="_blank" rel="noopener noreferrer">{ticket}</a> QA Test` (render plain text `{ticket}` if `DATA.link` is missing or not `https?://`).
   - **Source `.md` link**: render `<a class="src-link" href="testing-guide.md">Markdown</a>` **only** when `dev-view/testing-guide.md` is also generated; omit otherwise (never link `../agent-view/plan.md`, so standalone ticket attachments have no dead links). Omit `.src-link` from the exported PDF.
   - `Related:` line: render **only** when `DATA.related` is non-empty, validating `https?://` on each `r.link`.
   - Hint line: *"Found an issue? Mark it Fail and add a note. Then export the report and attach it to the ticket."*
2. **Progress bar**:
   - Fill bar (`%` of marked tests), count text (`"P pass · F fail · U not marked"`), primary **Export report** button, and **Reset** button (with confirmation prompt).
   - Red `#storage-warning` banner (`hidden` by default, unhidden when `localStorage` throws).
3. **Navigation & Body**:
   - Left `<nav>`: `"Tests"`, group headings, and `#case-id` links showing `✓` (`pass`) or `✗` (`fail`) badge.
   - `<main>`: `<section class="setup">` (`Before you start`) rendered **only** when `DATA.setup` is non-empty, then purpose groups (`<h2>` with thin top divider except first, plus `<p class="why">`).
   - Each test card (`<article class="test" id="{id}">`): `<h3>Test N: Title</h3>` + `Pass` / `Fail` segmented toggle (`aria-pressed`), optional italic note, numbered `<ol class="steps">` with bold screen prefix (`<b class="sc">Screen:</b> action`), `.expect` box, and `<textarea data-note>` shown **only** when marked `Fail` (retaining text if toggled).

## 3. Bilingual Data (`const DATA`)

1. Format `const DATA = {\n  ...\n};` as **multi-line, pretty-printed JSON** at the top of `<script>` (serializing `<` as `\u003c`), so future edits only touch changed lines:
   - `ticket`, `link`, `slug`, `languages` (`["en", "zh"]` or `["en"]`), `hasMd` (boolean, `true` only when `dev-view/testing-guide.md` exists), `related`, `title: {en, zh}`, `setup: [{text: {en, zh}}]`, `groups: [{name: {en, zh}, why: {en, zh}, tests: [{id, title: {en, zh}, note, steps: [{en, zh}], expect: {en, zh}}]}]`.
   - Assign a stable unique `id` (`case-1`, UUID, etc.) per test. When updating an existing `dev-view/testing-guide.html`, read its `DATA` lines first and preserve matching `id`s for unchanged tests so saved browser `results` and `notes` survive; assign new `id`s to new or acceptance-changed tests so they start blank. Pre-ID legacy migration is retired.
2. **Translate (`zh`)**:
   - Spawn one `standard` subagent per [host mapping](../../../references/agents.md#host-mapping) with the repository path and English strings.
   - Check repo translation files (`i18n`, `locales`, `zh*.json`) first, then `~/.just-do-it/{project}/public/glossary.md` and `agent-view/{spec,plan}.md`. Unmatched terms are translated plainly and reported as `guess` under `Open`.
3. Render bilingual strings as `<span data-l="en">...</span><span data-l="zh">...</span>`, filter `LANGS = ALL_LANGS.filter(l => (DATA.languages || ["en"]).includes(l.k))`, hide `#lang` if `LANGS.length <= 1`, and toggle active language via `<style id="lcss">` (`[data-l]:not([data-l="<lang>"]){display:none}`) while persisting choice in `localStorage`.

## 4. Interaction, Persistence & Offline PDF Export

- **URL validation & conditional rendering**:

```js
const safeUrl = u => /^https?:\/\//i.test(String(u || "")) ? u : "";
const extLink = (u, label) => {
  const s = safeUrl(u);
  return s ? '<a href="' + esc(s) + '" target="_blank" rel="noopener noreferrer">' + esc(label) + '</a>' : esc(label);
};
```

- **State persistence**: save `{results, notes, lang}` under `localStorage` key `"qa-v2-" + DATA.ticket + "-" + DATA.slug`. If `localStorage` throws, fall back to `window.name` and unhide `#storage-warning`.
- **Scroll-spy active indicator**: highlight the active `#case-id` link in `<nav>` with `.cur` at ~30% viewport height (and the last test when scrolled to bottom):

```js
const scroller = () => getComputedStyle(document.body).overflow === "hidden" ? $("main") : window;
function updateCur() {
  const cards = [...document.querySelectorAll("article.test")];
  if (!cards.length) return;
  const s = scroller(), atBottom = s === window
    ? innerHeight + scrollY >= document.documentElement.scrollHeight - 4
    : s.scrollTop + s.clientHeight >= s.scrollHeight - 4;
  const cut = (s === window ? 0 : s.getBoundingClientRect().top) + innerHeight * 0.3;
  let active = atBottom ? cards[cards.length - 1].id : cards[0].id;
  if (!atBottom) for (const c of cards) { if (c.getBoundingClientRect().top <= cut) active = c.id; else break; }
  document.querySelectorAll("nav a[data-id]").forEach(a => a.classList.toggle("cur", a.dataset.id === active));
}
$("main").addEventListener("scroll", updateCur, { passive: true });
window.addEventListener("scroll", updateCur, { passive: true });
updateCur();
```

- **Offline PDF Export**:
  - Include empty placeholder tags in the HTML body:
    `<template id="pdf-license"></template>`
    `<script type="application/octet-stream" id="pdf-library"></script>`
  - Run `python3 skills/to-test-doc/scripts/embed_pdf.py <path-to-testing-guide.html>` to populate `#pdf-license` (from `assets/pdf-license.txt`) and `#pdf-library` (base64 of `assets/pdf-library.js.gz`).
  - Clicking **Export report** decompresses `#pdf-library` via `DecompressionStream("gzip")` and downloads `{ticket}-qa-report-YYYY-MM-DD.pdf` in the active language: full-width title, ticket and date, failed-test count, failed cards, highlighted expected results, and tester notes (or localized `No failed tests.` when none failed; omit passed/unmarked counts and cases). Report export errors inline (`#export-error`) so testers can retry.
