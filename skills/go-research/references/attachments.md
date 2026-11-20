# Attachments

Cache every attachment of every fetched ticket, any type, including embedded images.

## Location

- `~/.just-do-it/{project}/{branch}/agent-view/attachments/{ticket}/` (or an isolated system temp directory only when the user explicitly requests terminal-only output). Preserve original file names and existing files; report any collision or failed transfer as missing evidence.
- Create a ticket's folder only when it has a file.
- Reuse files already there; download only the rest.

## Download

- **With the tracker's MCP:** its attachment download tool, with `agent-view/attachments/{ticket}/` as output path. Run any returned download command at once; links often expire.
- **Without MCP:** the tracker's REST API with an API token from the environment, to `agent-view/attachments/<ticket>/<filename>`.
- Never print or save the token.
- Failed download or unset variable: list the file as missing, with the cause.
