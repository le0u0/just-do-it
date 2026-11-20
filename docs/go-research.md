# go-research

Research a ticket, requirements link, or tracker queue. Reads live requirements, comments, related tickets, and attachments, maps relevant repository files and folders, and writes `agent-view/research.md`.

## What you get

- Requirements and acceptance criteria from the live source, with comments and proposals distinguished from agreed requirements.
- Related tickets and cached attachments (`agent-view/attachments/{ticket}/`), open questions, and relevant repository files and folders.
- Unknown domain terms flagged for confirmation and saved to `public/glossary.md`.
- Source links and any access or evidence gaps.

If the branch folder is missing under `~/.just-do-it/*/{branch}`, `go-research` triggers `go-setup` first to confirm `{project}` with you, then writes `agent-view/research.md`.

[Skill](../skills/go-research/SKILL.md) · [Storage](../skills/go-setup/references/storage.md)
