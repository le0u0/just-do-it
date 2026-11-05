# Verify

## Setup

- Serve the folder over local HTTP (`python3 -m http.server`): `playwright-cli` blocks `file://`.
- Use Playwright from the project's `node_modules`. Without it, mark every check `not verified`.
- Report only what you ran.

## Checks

1. No console errors. No horizontal scroll at 390px.
2. Each left-list link lands with its heading in view and its link highlighted, the last two included.
3. Language switch changes every visible string and leaves none of another language. The choice survives a reload.
4. Tick steps, mark a Fail, open Export results, type concerns, Cancel (no download), reopen (text kept), export (file correct, reader's language), Reset, Load results (state restored).
5. Repeat the save test with `localStorage` blocked (`addInitScript`): red warning shows, same-tab fallback restores state.
6. Computed font sizes match the type scale in [html-page.md](html-page.md).
7. Reload, then open a second tab: saved state is there.

Safari, Firefox: `not verified` unless run.
