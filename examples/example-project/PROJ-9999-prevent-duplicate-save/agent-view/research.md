# Research: PROJ-9999 Prevent duplicate profile saves

## Requirements

- Ignore second Save click while first `PUT /api/v1/profile` request is pending.
- Disable Save button and show `Saving...` label during request (`attachments/PROJ-9999/profile-save-states.svg`).
- Keep server error banner and re-enable Save after a failed request.

## Acceptance criteria

- Rapid double-click on Save sends exactly one `PUT /api/v1/profile` call.
- Save button disabled while `isSaving` true.
- Request failure restores Save button enabled state and displays server error message.

## Related tickets

- PROJ-9810 (relates to): Profile display name field validation.

## Open questions

None.

## Code pointers

- <sub>`src/app/profile/profile-form.component.ts` (`onSubmit`), `src/app/profile/profile-form.component.html`, `src/app/profile/profile-form.component.spec.ts`, `playwright/tests/profile-save.spec.ts`</sub>

## Reference

<sub>Source: https://example.atlassian.net/browse/PROJ-9999<br>Retrieved: 2026-11-20 15:10<br>Linked: PROJ-9810<br>Attachments: `attachments/PROJ-9999/profile-save-states.svg`</sub>
