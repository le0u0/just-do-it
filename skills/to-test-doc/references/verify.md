# Verify

## Setup

- Serve the folder over local HTTP (`python3 -m http.server`): `playwright-cli` blocks `file://`.
- Use Playwright from the project's `node_modules`. Without it, mark every check `not verified`.
- Report only what you ran.

## Checks

1. No console errors. No horizontal scroll at 390px.
2. Each left-list link lands with its heading in view and its link highlighted, the last two included.
3. Language switch changes every visible string and leaves none of another language. The choice survives a reload.
4. Confirm notes appear only for failed tests and survive status changes. Click Export report and verify a PDF downloads directly with the ticket and date in its filename. Confirm the PDF uses the selected language and shows the failed-test count, including zero when there are no failures. Check the feature header, failed steps, expected results, and tester notes or the no-failure message. Check that it omits passed and unmarked counts and cases. Check reset.
5. Repeat the save test with `localStorage` blocked (`addInitScript`): red warning shows, same-tab fallback restores state.
6. Computed font sizes match the type scale in [html-page.md](html-page.md).
7. Reload, then open a second tab: saved state is there.
8. Regenerate after wording and test-order changes: matching test IDs keep their results and notes; new tests are unmarked. For an existing pre-ID guide, check migration from its exact old DATA hash, including a removed test.
