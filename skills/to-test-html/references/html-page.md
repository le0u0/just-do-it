# HTML Page

## Format

- One static file from [qa-template.html](qa-template.html): inline CSS and JS, no framework, build step or external request. Works offline and as a ticket attachment.
- Strings: guide data in English plus the project's other UI languages. English only: no language switch.

## Structure

1. **Header:** h1 feature name; lead line `<ticket link> QA Test`; related line if any; "Found an issue? Mark it Fail and add a note. Then export the report and attach it to the ticket."; language switch top right.
2. **Progress:** bar of marked tests, "P pass · F fail · U not marked", then Export report (primary), Reset. No import.
3. **Body:** Before you start (only when the guide has it), groups with one-line reasons, tests. A thin divider line above every group heading except the first.
4. **Test:** heading `Test N: Title`, Pass / Fail toggle, optional guide note, numbered steps, and a tinted `You should see:` box. Show the optional tester note textarea only when marked Fail; retain its contents if the status changes.
5. **Finish:** summary ("P pass, F fail, U not marked yet") and a large Export report button, alone.

## Language

- Every string, including buttons, counts, nav and Pass/Fail, exists in every language.
- One `aria-pressed` button per language, in its own name. Remember the choice; default `navigator.language`.
- Set `html lang` and the title. Hide inactive languages with CSS so print shows one.

## Export report

- Export report downloads `TICKET-qa-report-YYYY-MM-DD.pdf` directly using the bundled html2pdf.js library. The report uses the selected language.
- The report uses the full width for the feature title, then shows the ticket, date, and failed test cards with steps, expected result and tester notes. When none failed, say so. Omit summary counts and passed and unmarked test details.
- The compressed bundled library and its license notices remain inline for offline use. PDF export requires a browser with `DecompressionStream`.
- No JSON, no import. Reset asks for confirmation.

## Saving progress

- Pass/Fail and notes go to `localStorage`.
- Blocked (`file://`, preview panes): fall back to `window.name` and show one red line, only then, saying to export the report before closing.

## Navigation

- Left list: "Tests", group labels, test links with a Pass/Fail mark; sticky on desktop, a wrapped row above the content on mobile. One page: no tabs, no Previous/Next.
- Highlight follows scroll at about 30% of the viewport; last test at the bottom. A click holds it until the user scrolls. No bottom padding.

## Design

- Color: one accent on warm neutrals (project theme color, else restrained). Dark text on it, never accent body text. Green and red only for Pass and Fail.
- Type: title 28px; group heading 24px bold; test title 16px semibold; steps 16px. List: "Tests" 18px bold, group labels 16px bold dark, links 14px grey indented, current dark semibold on accent.
- System font stack with per-script fallbacks. About 75ch lines.
- Focus rings, hover and active states, 150ms transitions, `prefers-reduced-motion`. Print hides controls.
- 1280px and 390px, no horizontal scroll.
