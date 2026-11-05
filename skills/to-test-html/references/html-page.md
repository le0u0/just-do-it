# HTML Page

## Format

- One static file, rendered from [qa-page-template.html](qa-page-template.html).
- Inline CSS and JS. No framework, build step or external request: it works offline and as a ticket attachment.
- Strings: the guide data in English plus the project's other UI languages, from its translation files or rules.
- English only: no language switch.

## Structure

1. **Header:**
   - h1 (feature name).
   - Lead line `<ticket link> QA Test`.
   - Related-tickets line, when the guide has one.
   - One line: "Found an issue? Export results with your concerns and attach the file to the ticket."
   - Language switch, top right.
2. **Progress:** bar with "N of M steps · P pass · F fail", then Export results (primary), Load results, Reset.
3. **Body:** Setup, then groups with their one-line reasons, then the tests.
4. **Test:** heading `Test N: Title` with a Pass / Fail toggle, optional note, checkbox steps, `Expect:` line.
5. **Finish:** summary ("P pass, F fail, U not marked yet") and a large Export results button. Nothing else.

## Language

- Every string has every language: headings, notes, steps, expect lines, buttons, dialog, counts, finish text, group reasons, nav, Pass/Fail.
- One button per language, in that language's own name, with `aria-pressed`.
- The choice is remembered. Default: `navigator.language`.
- Set `html lang` and the document title.
- Hide the inactive language with CSS (`html[lang] [lang=...]`), so print shows one language.

## Export and load

- Export results opens a native `<dialog>`:
  - Title, one summary line ("1 pass · 1 fail · 9 not marked"), a "Concerns" label, one textarea, Cancel and Export.
  - Escape and Cancel close it with no download.
  - Download only from Export, as `TICKET-qa-results-YYYY-MM-DD.json`.
- The JSON holds:
  - `ticket`, `guide`, `language`, `exportedAt`, `summary {pass, fail, notMarked}`, `concerns`.
  - `tests[{id, title, result, steps[{done, text}], expect}]` in the reader's language.
  - `state`, for Load results to restore.
- Load results accepts that file.
- Reset asks for confirmation.

## Saving progress

- Save ticks, Pass/Fail and the concerns text in `localStorage`.
- Blocked (`file://` in some browsers, preview panes): fall back to `window.name` and show one red line, only then, telling the reader to export before closing.

## Navigation

- Left list: "Tests", group labels, test links with a Pass/Fail mark.
- All tests on one page: no tabs, no Previous/Next.
- Highlight follows scroll: line at about 30% of the viewport, last test at the page bottom.
- A click sets the highlight until the user scrolls (wheel, touch, keyboard).
- No artificial bottom padding.
- Desktop: sticky. Mobile: a wrapped row above the content.

## Design

A tool the reader uses while working: product register.

- When the Impeccable skill is installed, load it first. No `PRODUCT.md` in the project: return `Open` asking whether to skip its init.
- Color:
  - One accent on warm neutrals: the project's theme color from its style tokens, else one restrained accent.
  - Dark text on the accent. The accent never colors body text.
  - Green and red only for Pass and Fail.
- Type:
  - Page title 28px. Group heading 24px bold. Test title 16px semibold. Steps 16px.
  - List: "Tests" 18px bold, group labels 16px bold dark, test links 14px regular grey and indented, current one dark semibold on the accent.
  - System font stack, with system fallbacks for each language's script. Line length about 75ch.
- Controls: custom checkboxes (accent fill, dark check), visible focus rings, hover and active states, 150ms transitions, a `prefers-reduced-motion` rule.
- Print hides the controls.
- Layout: works at 1280px and 390px, no horizontal scroll. Plain solid surfaces, ordinary borders.
