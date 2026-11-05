# HTML Page

One static file: inline CSS and JS, no framework, no build step, no external request, so it works offline and as a ticket attachment. Strings come from the guide data in English plus the project's other UI languages, taken from its translation files or rules. With English only, leave out the language switch.

## Structure

1. **Header:** h1 (feature name), the lead line `<ticket link> QA Test`, the related-tickets line when the guide has one, and one line: "Found an issue? Export results with your concerns and attach the file to the ticket." The language switch sits top right.
2. **Progress:** a bar with "N of M steps · P pass · F fail", then Export results (primary), Load results, Reset.
3. **Setup,** then the **groups** with their one-line reasons, then the tests.
4. **Test:** heading `Test N: Title` with a Pass / Fail toggle, the optional note, checkbox steps, the `Expect:` line.
5. **Finish:** the summary ("P pass, F fail, U not marked yet") and a large Export results button. Nothing else.

## Language

- Every string has every language: headings, notes, steps, expect lines, buttons, dialog, counts, finish text, group reasons, nav, Pass/Fail.
- One button per language, labelled in that language's own name, with `aria-pressed`. The choice is remembered; the default follows `navigator.language`. Set `html lang` and the document title.
- Hide the inactive language with CSS (`html[lang] [lang=...]`), so print shows one language.

## Export and load

- Export results opens a native `<dialog>`: title, one summary line ("1 pass · 1 fail · 9 not marked"), a "Concerns" label, one textarea, Cancel and Export. Escape and Cancel close it without a download. The download happens only from Export, as `TICKET-qa-results-YYYY-MM-DD.json`.
- The JSON holds `ticket`, `guide`, `language`, `exportedAt`, `summary {pass, fail, notMarked}`, `concerns`, `tests[{id, title, result, steps[{done, text}], expect}]` in the reader's language, and `state` for Load results to restore.
- Load results accepts that file. Reset asks for confirmation.

## Saving progress

Save ticks, Pass/Fail and the concerns text in `localStorage`. When it is blocked (`file://` in some browsers, preview panes), fall back to `window.name`, and show one red line, only in that case, telling the reader to export before closing.

## Navigation

- A left list: "Tests", group labels, test links with a Pass/Fail mark. All tests stay on one page: no tabs, no Previous/Next.
- The highlight follows scroll with a line at about 30% of the viewport, and the last test at the page bottom. A click sets the highlight until the user scrolls (wheel, touch, keyboard). No artificial bottom padding.
- Sticky on desktop; on mobile a wrapped row above the content.

## Design

A tool the reader uses while working, so product register. When the Impeccable skill is installed, load it first; with no `PRODUCT.md` in the project, return `Open` asking whether to skip its init.

- One accent on warm neutrals: the project's theme color from its style tokens, else one restrained accent. Dark text on the accent; the accent never colors body text. Green and red only for Pass and Fail.
- Type: page title 28px; group heading 24px bold; test title 16px semibold; steps 16px. In the list: "Tests" 18px bold, group labels 16px bold dark, test links 14px regular grey and indented, the current one dark semibold on the accent.
- System font stack, with system fallbacks for each language's script. Line length about 75ch.
- Custom checkboxes (accent fill, dark check), visible focus rings, hover and active states, 150ms transitions, a `prefers-reduced-motion` rule. Print hides the controls.
- Work at 1280px and 390px with no horizontal scroll. Use plain, solid surfaces and ordinary borders.
