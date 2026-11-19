# Attachments

Cache every attachment of every fetched ticket, any type, including embedded images.

## Location

- `attachments/{ticket}/` under the approved task directory when saving, else an isolated system temp directory. If research runs before the delivery decision, use temp and retain attachments only when saving is approved. Original file names.
- Create a ticket's folder only when it has a file.
- Reuse files already there; download only the rest.

## Download

- **With the tracker's MCP:** its attachment download tool, that folder as output path. Run any returned download command at once; links often expire.
- **Without MCP:** the tracker's REST API with an API token from the environment, to `<cache directory>/attachments/<ticket>/<filename>`.
- Never print or save the token.
- Failed download or unset variable: list the file as missing, with the cause.
