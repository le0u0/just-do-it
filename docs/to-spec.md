# to-spec

Research a ticket, requirements link, or tracker queue. Reads live requirements, comments, related tickets, and attachments, maps relevant repository files and folders, and writes `agent-view/spec.md`.

## What you get

- Requirements and acceptance criteria from the live source, with comments and proposals distinguished from agreed requirements.
- Related tickets and cached attachments (`agent-view/attachments/{ticket}/`), open questions, and relevant repository files and folders.
- Unknown domain terms flagged for confirmation and saved to `public/glossary.md`.
- Source links and any access or evidence gaps.

When a required source is unavailable, `to-spec` marks the brief blocked and asks you to restore access or provide the missing requirements. Ticket planning and review wait for a complete spec.

If the branch folder is missing under `~/.just-do-it/*/{branch}`, `to-spec` triggers `go-setup` first to confirm `{project}` with you, then writes `agent-view/spec.md` (for agents) and `dev-view/spec.html` (for you, with inline downloaded attachment images).

[Skill](../skills/to-spec/SKILL.md) · [Storage](../skills/go-setup/references/storage.md)
