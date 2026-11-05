# Verify

## Setup

- Serve the HTML's folder over local HTTP (`python3 -m http.server`): `playwright-cli` blocks `file://`.
- Open it with Playwright from the project's `node_modules`.
- No Playwright: mark every check `not verified`.
- Report only what you ran.

## Checks

1. No console errors. At 390px, no horizontal scroll.
2. Every left-list link lands with its heading in view and its own link highlighted, the last two included.
3. Switching language changes every visible string, leaving no text of another language. The choice survives a reload.
4. Tick steps, mark a Fail, open Export results, type concerns, Cancel (no download), reopen (text kept), export (file correct and in the reader's language), Reset, Load results (state restored).
5. Repeat the save test with `localStorage` blocked (`addInitScript`): the red warning shows and the same-tab fallback restores state.
6. Computed font sizes match the type scale in [html-page.md](html-page.md).
7. Reload, then open a second tab: saved state is there.

## Limits

- Safari and Firefox are `not verified` unless run.
