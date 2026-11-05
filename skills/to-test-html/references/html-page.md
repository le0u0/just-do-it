# HTML Page

## Format

- One static file from [qa-template.html](qa-template.html): inline CSS and JS, no framework, build step or external request. Works offline and as a ticket attachment.
- Strings: guide data in English plus the project's other UI languages. English only: no language switch.

## Structure

1. **Header:** h1 feature name; lead line `<ticket link> QA Test`; related line if any; "Found an issue? Export results with your concerns and attach the file to the ticket."; language switch top right.
2. **Progress:** bar "N of M steps · P pass · F fail", then Export results (primary), Load results, Reset.
3. **Body:** Setup, groups with one-line reasons, tests.
4. **Test:** heading `Test N: Title`, Pass / Fail toggle, optional note, checkbox steps, `Expect:` line.
5. **Finish:** summary ("P pass, F fail, U not marked yet") and a large Export results button, alone.

## Language

- Every string, including buttons, dialog, counts, nav and Pass/Fail, exists in every language.
- One `aria-pressed` button per language, in its own name. Remember the choice; default `navigator.language`.
- Set `html lang` and the title. Hide inactive languages with CSS so print shows one.

## Export and load

- Export results opens a native `<dialog>`: title, summary line ("1 pass · 1 fail · 9 not marked"), "Concerns" textarea, Cancel, Export.
- Escape and Cancel close with no download. Only Export downloads `TICKET-qa-results-YYYY-MM-DD.json`.
- JSON: `ticket`, `guide`, `language`, `exportedAt`, `summary {pass, fail, notMarked}`, `concerns`, `tests[{id, title, result, steps[{done, text}], expect}]` in the reader's language, and `state` for Load results.
- Load results accepts that file. Reset asks for confirmation.

## Saving progress

- Ticks, Pass/Fail and concerns go to `localStorage`.
- Blocked (`file://`, preview panes): fall back to `window.name` and show one red line, only then, saying to export before closing.

## Navigation

- Left list: "Tests", group labels, test links with a Pass/Fail mark; sticky on desktop, a wrapped row above the content on mobile. One page: no tabs, no Previous/Next.
- Highlight follows scroll at about 30% of the viewport; last test at the bottom. A click holds it until the user scrolls. No bottom padding.

## Design

- Product register. Impeccable installed: load it first; no `PRODUCT.md`: return `Open` asking whether to skip its init.
- Color: one accent on warm neutrals (project theme color, else restrained). Dark text on it, never accent body text. Green and red only for Pass and Fail.
- Type: title 28px; group heading 24px bold; test title 16px semibold; steps 16px. List: "Tests" 18px bold, group labels 16px bold dark, links 14px grey indented, current dark semibold on accent.
- System font stack with per-script fallbacks. About 75ch lines.
- Custom checkboxes (accent fill, dark check), focus rings, hover and active states, 150ms transitions, `prefers-reduced-motion`. Print hides controls.
- 1280px and 390px, no horizontal scroll.
