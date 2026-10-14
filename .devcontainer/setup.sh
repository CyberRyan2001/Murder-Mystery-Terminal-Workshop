#!/usr/bin/env bash
# Runs once when the Codespace is created (from the repo root).
set -e

pip install --no-cache-dir -r requirements.txt


CASE="$HOME/Victor_Von_Jacobson_Case"
if [ ! -d "$CASE" ]; then
  tar -xzf case.tar.gz -C "$HOME"
fi

ROOT="$(pwd)"
for rc in "$HOME/.bashrc" "$HOME/.zshrc"; do
  cat >> "$rc" <<RC

# Murder mystery workshop: start every new terminal at the crime scene
if [ "\$PWD" = "$ROOT" ] || [ "\$PWD" = "\$HOME" ]; then cd "$CASE"; fi
echo "Welcome, detective. Type ls to look around, or cat Hints.txt if you get stuck."
RC
done

echo "Setup complete."