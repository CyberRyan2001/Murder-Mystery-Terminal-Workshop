#!/usr/bin/env bash
# Runs once when the Codespace is created (from the repo root).
set -e

pip install --no-cache-dir -r requirements.txt


CASE="$HOME/Victor_Von_Jacobson_Case"
if [ ! -d "$CASE" ]; then
  tar -xzf case.tar.gz -C "$HOME"
fi

# Keep the secret passage out of the mansion until a player reads button.txt
if [ -d "$CASE/.vault" ]; then
  mkdir -p "$HOME/.mansion_vault"
  mv "$CASE/.vault"/* "$HOME/.mansion_vault/"
  rmdir "$CASE/.vault"
fi
cp .devcontainer/mansion_hooks.sh "$HOME/.mansion_hooks.sh"

ROOT="$(pwd)"
for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
  cat >> "$rc" <<RC

# Murder mystery workshop: start every new terminal at the crime scene
[ -f "\$HOME/.mansion_hooks.sh" ] && . "\$HOME/.mansion_hooks.sh"
if [ "\$PWD" = "$ROOT" ] || [ "\$PWD" = "\$HOME" ]; then cd "$CASE"; fi
echo "Welcome, detective. Type ls to look around, or cat Hints.txt if you get stuck."
RC
done

echo "Setup complete."