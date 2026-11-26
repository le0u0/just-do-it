# Verify

## Setup

- Run interactive browser checks over local HTTP (`python3 -m http.server`): `playwright-cli` blocks `file://`.
- Use Playwright from the project's `node_modules`. Without it, mark automated browser checks `not verified`.
- Run standalone offline PDF verification separately by opening `dev-view/testing-guide.html` directly via `file://` with networking disabled.
- Report only what you ran and record what each check covered.

## Checks

1. No console errors. No horizontal scroll at 390px.
2. Each left-list link lands with its heading in view and its link highlighted (`.cur`), the last two included, and scroll-spy updates `.cur` on scroll.
3. Language switch changes every visible string and leaves none of another language (and `#lang` is hidden when single-language). The choice survives a reload.
4. Confirm notes appear only for failed tests and survive status changes. Click **Export report** and verify `{ticket}-qa-report-YYYY-MM-DD.pdf` downloads directly with one click. Confirm the PDF uses the selected language and shows the failed-test count, including zero when there are no failures. Check the feature header, failed steps, expected results, and tester notes or the no-failure message. Check that it omits passed and unmarked counts and cases. Check retry after export failure and reset.
5. Repeat the save test with `localStorage` blocked (`addInitScript`): red warning shows, `window.name` same-tab fallback restores state.
6. Computed font sizes match the type scale in [html-page.md](html-page.md) and [html-render.md](../../go-setup/references/html-render.md).
7. Reload, then open a second tab: saved state is there.
8. Regenerate after wording and test-order changes: matching test IDs keep their browser results and notes; new or acceptance-changed tests get new IDs and start unmarked.
