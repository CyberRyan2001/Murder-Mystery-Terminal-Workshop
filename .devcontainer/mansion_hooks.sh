# Murder mystery workshop: reading button.txt opens the secret passage.
# setup.sh copies this to ~/.mansion_hooks.sh and loads it in every new terminal.

MANSION_VAULT="$HOME/.mansion_vault"

_mansion_check_button() {
  local f dir
  for f in "$@"; do
    case "$f" in -*) continue ;; esac
    [ "$(basename -- "$f")" = "button.txt" ] && [ -f "$f" ] || continue
    dir="$(cd "$(dirname -- "$f")" && pwd)"
    if [ -d "$dir/Secret_Passage" ]; then
      echo
      echo ">> You press it again. Nothing happens... the passage is already open."
    elif [ -d "$MANSION_VAULT/Secret_Passage" ]; then
      mv "$MANSION_VAULT/Secret_Passage" "$dir/Secret_Passage"
      echo
      echo ">> A low rumble shakes the room... the wall behind the bed slides open!"
      echo ">> A new room has appeared: Secret_Passage (type ls to see it)"
    fi
  done
}

# Run the check after any command a player might use to read a file
for _cmd in cat less more head tail; do
  eval "$_cmd() { command $_cmd \"\$@\"; local _s=\$?; _mansion_check_button \"\$@\"; return \$_s; }"
done
unset _cmd
