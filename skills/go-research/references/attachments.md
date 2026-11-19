# Attachments

Cache every attachment of every fetched ticket, any type, including embedded images.

## Location

- `attachments/{ticket}/` under the approved task directory when saving, else an isolated system temp directory. If research runs before the delivery decision, use temp. When saving is approved, transfer cached attachments to `attachments/{ticket}/` under the task directory before cleaning up temp. Preserve original file names and existing files; report any collision or failed transfer as missing evidence.
- Create a ticket's folder only when it has a file.
- Reuse files already there; download only the rest.
- A delegated worker returns the temporary cache path and any missing files to the coordinator, who handles delivery and cleanup.

## Download

- **With the tracker's MCP:** its attachment download tool, that folder as output path. Run any returned download command at once; links often expire.
- **Without MCP:** the tracker's REST API with an API token from the environment, to `<cache directory>/attachments/<ticket>/<filename>`.
- Never print or save the token.
- Failed download or unset variable: list the file as missing, with the cause.
