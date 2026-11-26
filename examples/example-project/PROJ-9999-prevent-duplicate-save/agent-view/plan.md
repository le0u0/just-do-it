# Plan: PROJ-9999 Prevent duplicate profile saves

Status: example

## Goal

1. **Click Save on the profile form**\
   Expected: Send one `PUT /api/v1/profile` request, disable Save, and show `Saving...` while pending.\
   Actual: Save remains active when the request starts.
2. **Click Save again before the request completes**\
   Expected: Only the first click sends a save request.\
   Actual: Repeated clicks can send multiple requests.
3. **Save succeeds**\
   Expected: Close the edit flow and restore a clean form state.\
   Actual: Unverified.
4. **Save fails with a server or network error**\
   Expected: Show the error banner and re-enable Save for immediate retry.\
   Actual: Unverified.

## Statechart

```mermaid
stateDiagram-v2
    [*] --> Clean: Load profile form
    Clean --> Dirty: Edit display name
    Dirty --> Saving: Click Save (isSaving = true)
    Saving --> Clean: 200 OK (close edit flow)
    Saving --> SaveError: 500 / network error (isSaving = false)
    SaveError --> Saving: Click Save retry
    SaveError --> Dirty: Edit field
```

- Invariant: `Saving` ignores duplicate `onSubmit()` calls and disables Save button.
- Invariant: `SaveError` clears `isSaving` and keeps server error banner visible.

## Implementation pipelines

| Pipeline | Ordered steps | Requires | Shared resources |
| --- | --- | --- | --- |
| Profile save | 1 | None | Existing ProfileForm fixtures |

## Steps

### 1. Guard Save while pending and recover on failure

- **Do:** Ignore `onSubmit()` calls while `isSaving` is true and disable the Save button (<span title="attachments/PROJ-9999/profile-save-states.svg">Save button states</span>).
- **Do:** Clear `isSaving` on both success and failure while preserving the server error message.
- **Reuse:** `AppButtonComponent` (`[loading]="isSaving"`) and `AlertBannerComponent` for error display.
- **Test:** Repeated clicks send one request; failed save re-enables Save and shows error. Run: yes.
- **Commit:** `fix: prevent duplicate profile saves`
- **Blocked by:** none
- <sub>**Files:** <span title="src/app/profile/profile-form.component.ts">Profile form logic</span>, <span title="src/app/profile/profile-form.component.html">Profile form template</span>, <span title="src/app/profile/profile-form.component.spec.ts">ProfileForm Unit Test</span>; attachment: <span title="attachments/PROJ-9999/profile-save-states.svg">Save button states</span></sub>

## Out of scope

- Other forms outside ProfileFormComponent.

## Testing

- Seam: `ProfileFormComponent.onSubmit`. Catches duplicate calls and stuck disabled state; misses real network latency.
- E2E: Rapid double-click on Save submits once and recovers after a mocked 500 response.
- <sub>Prior art: <span title="src/app/profile/profile-form.component.spec.ts">ProfileForm Unit Test</span>. E2E: <span title="playwright/tests/profile-save.spec.ts">Profile save E2E test</span></sub>

## Decisions

- Lock Save on the client via `isSaving` per ADR 001.
- Reuse `AppButtonComponent` and `AlertBannerComponent`.
- API contract and permissions unchanged.

## Deletions

None.

## Open

None.

## Reference

<sub>Requirement source: PROJ-9999<br>Repository: /example/repo<br>Branch: PROJ-9999-prevent-duplicate-save<br>Initial baseline: a1b2c3d<br>Delivery: per-step commits</sub>
