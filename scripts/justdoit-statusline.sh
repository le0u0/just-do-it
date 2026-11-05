#!/bin/bash
# just-do-it status line: runs the command given as arguments (your existing
# status line, e.g. caveman's), then appends [JUSTDOIT] while manager mode is on (`/justaway on`).
#
# settings.json:
#   "statusLine": { "type": "command",
#     "command": "bash ~/.claude/hooks/justdoit-statusline.sh bash ~/.claude/hooks/caveman-statusline.sh" }

CFG="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
IFS= read -r -d '' -t 1 STDIN_JSON

SESSION_ID=$(printf '%s' "$STDIN_JSON" \
  | grep -o '"session_id"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 \
  | sed -e 's/.*:[[:space:]]*"//' -e 's/"$//')
case "$SESSION_ID" in ''|*[!A-Za-z0-9_-]*) SESSION_ID="" ;; esac

OUT=""
[ "$#" -gt 0 ] && OUT=$(printf '%s' "$STDIN_JSON" | "$@" 2>/dev/null)

FLAG="$CFG/.justdoit-manager-$SESSION_ID"
if [ -n "$SESSION_ID" ] && [ ! -L "$FLAG" ] && [ "$(head -c 8 "$FLAG" 2>/dev/null)" = "on" ]; then
  BADGE=$'\033[38;5;39m[JUSTDOIT]\033[0m'
  if [ -n "$OUT" ]; then
    printf '%s %s' "$OUT" "$BADGE"
  else
    printf '%s' "$BADGE"
  fi
else
  printf '%s' "$OUT"
fi
