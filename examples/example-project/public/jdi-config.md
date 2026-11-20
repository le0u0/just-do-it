# JDI Config

## Retry

- **Limit:** 1

## Unit

- **Runner:** Vitest (`vitest.config.ts`)
- **Paths:** `src/**/*.spec.ts` (co-located beside source)
- **Focused command:** `npx vitest run <spec-path>`

## E2E

- **Runner:** Playwright (`playwright.config.ts`)
- **Folder:** `playwright/tests/`
- **Base URL:** `http://localhost:4200`
- **Focused command:** `PLAYWRIGHT_HTML_OPEN=never npx playwright test <spec-path>`
