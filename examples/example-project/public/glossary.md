# Glossary

| Term | Meaning | Context / Location | Avoid |
| --- | --- | --- | --- |
| Profile form | Account profile form where users update their display name. | `src/app/profile/profile-form.component.ts` | Settings modal |
| Pending save lock | Client-side guard blocking duplicate `PUT /api/v1/profile` requests while in flight. | `ProfileFormComponent.isSaving` | Backend idempotency key |
