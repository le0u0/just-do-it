# E2E Authoring

## Process

- Write from explored locators and steps, never from source alone.
- One scenario at a time: walk it live, then write its test.
- Adapt generated code to the closest spec: auth state, imports, helpers.
- Match the closest spec's actions too, such as Enter vs button click: a click that works while exploring can be swallowed in a run.
- Drop APIs the runner version lacks.

## Test data

- Reuse the project's data helpers.
- Give each fixture a stable identity from the domain's unique key.
- Look up before creating. Never delete and recreate.

## Files and imports

- Tests, hooks, and assertions stay in the spec.
- Reuse a fitting shared helper. Never copy its logic.
- Ticket-specific functions go in one util beside the spec, named per project convention. None: ask.
- No ticket data in shared helpers.
- Never import from another test folder or spec. Move the reusable part to shared helpers first.

## Locators

- Follow the project's locator contract.
- No contract, in order: role with name, label, visible text, test ID.
- Class selector only when no stable contract can exist. Say why.

## Waits

- Use web-first assertions or `waitFor()`.
- Never fixed sleeps, `networkidle`, or `waitForSelector`.
- After login or navigation: wait for the URL and one element on the destination.
- HTTP assertion: start the project's response helper before the action.

## Before finishing

- Each requested behavior has one observable assertion.
- Diff has no inline utilities, copied helpers, cross-test imports, or ticket data in shared helpers.
