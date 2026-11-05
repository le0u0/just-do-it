# Attachments

Cache every attachment of every fetched ticket, any type, including embedded images.

## Location

- `attachments/{ticket}/` in the directory the caller names, else the system temp directory.
- Original file names.
- Create a ticket's folder only when it has a file.
- Look there before downloading. Reuse cached files.

## Download

- **With the tracker's MCP:** use its attachment download tool with that folder as output path. Run any returned download command at once; such links often expire.
- **Without MCP:** use the tracker's REST API with an API token from the environment, writing to `<cache directory>/attachments/<ticket>/<filename>`.

## Rules

- Never print or save the token.
- Download fails or variable unset: list the file as missing, with the cause.
