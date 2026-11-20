# Public Docs (`~/.just-do-it/{project}/public/`)

Project-level documents shared across all branches of `{project}`. None of these are pre-created empty on initial setup; each is created or updated when needed after confirming with the user.

## `glossary.md`

Tracks domain terminology, product concepts, internal abbreviations, and business rules that are not self-evident from code.

### When to read and update

1. Read `~/.just-do-it/{project}/public/glossary.md` (and repository `GLOSSARY.md` if present) at the start of `go-research`, `go-plan`, `go-work`, and `go-review`.
2. Whenever you encounter an unknown term, product concept, or ambiguous wording—or when a ticket/user word conflicts with an existing term—**never guess**.
3. Ask the user to clarify the exact meaning (and where it lives in the UI or codebase if relevant).
4. Once the user answers, create or update `~/.just-do-it/{project}/public/glossary.md` immediately:

```markdown
# Glossary

| Term | Meaning | Context / Location | Avoid |
| --- | --- | --- | --- |
| Export button | Toolbar action that downloads the current view. | `src/toolbar.ts` | Download link |
```

- Keep each meaning to one concise sentence. Update existing rows in place when refined.

## `adr/`

Holds Architecture Decision Records (`~/.just-do-it/{project}/public/adr/NNN-short-title.md`) for decisions that are hard to reverse, surprising without context, or resolve a real trade-off during `go-plan` or `go-work`.

### When to read and update

1. Read existing files in `~/.just-do-it/{project}/public/adr/` (and repository `docs/adr/` if present) during `go-plan`, `go-work`, and `go-review`.
2. When a hard-to-reverse design or architecture trade-off arises in `go-plan` or `go-work`, ask the user and confirm the choice.
3. Once confirmed, write `~/.just-do-it/{project}/public/adr/NNN-short-title.md` (numbering sequentially from `001`):

```markdown
# ADR 001: Short decision title

- **Context:** One line stating the constraint or conflict.
- **Decision:** One line stating the chosen design.
- **Why:** One line stating the trade-off and reason.
```

## `jdi-config.md`

Holds the project's confirmed settings at `~/.just-do-it/{project}/public/jdi-config.md`. Created when needed by a skill or requested through `go-setup`.

### Rules

1. If `public/jdi-config.md` exists, read and follow it. If its retry limit is missing or invalid, ask the user to confirm a non-negative integer (recommend `1`) and update the file before retrying.
2. If `public/jdi-config.md` does not exist when a test-handling skill runs:
   - Inspect `package.json`, runner config files (`vitest.config.*`, `karma.conf.*`, `jest.config.*`, `playwright.config.*`, `cypress.config.*`), and test directories.
   - Present the detected unit and E2E candidates to the user and **confirm before saving**.
   - Ask for a non-negative test retry limit; recommend `1` retry after the initial failed verification run.
   - Write `~/.just-do-it/{project}/public/jdi-config.md`:

```markdown
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
- **Authentication state:** none
- **Test data:** project fixtures
```

- If the project has no unit or E2E setup, record `Runner: none` after confirming with the user.
- The limit counts retries after the first unexpected failed verification run for the same failure, across skills and delegated workers. Expected TDD red runs do not count. After each failure, diagnose and attempt an authorized fix before retrying. When the limit is exhausted, stop the affected work, report the failure and evidence, and ask the user how to proceed. A limit of `0` stops after the first failure. Do not reset the count when delegating or changing workflow stages; carry the count and evidence to the caller. A new user instruction to continue starts a new retry allowance.
