# Verify

Serve the generated HTML's folder over local HTTP (`python3 -m http.server`), since `playwright-cli` blocks `file://`, and open it with Playwright from the project's `node_modules`. Without it, mark every check `not verified`. Report only what you ran.

1. No console errors; at 390px no horizontal scroll.
2. Every left-list link lands with its heading in view and its own link highlighted, the last two included.
3. Switching language changes every visible string, with no text of another language left visible; the choice survives a reload.
4. Tick steps, mark a Fail, open Export results, type concerns, Cancel (no download), reopen (text kept), export (file content correct and in the reader's language), Reset, Load results (state restored).
5. Repeat the save test with `localStorage` blocked (`addInitScript`): the red warning shows and the same-tab fallback restores state.
6. Computed font sizes match the type scale in [html-page.md](html-page.md).

Also reload and open a second tab to confirm the saved state. Safari and Firefox are `not verified` unless run.
