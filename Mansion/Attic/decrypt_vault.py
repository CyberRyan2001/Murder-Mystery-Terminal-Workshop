#!/usr/bin/env python3
import sys
from cryptography.fernet import Fernet, InvalidToken

def main():
    print("=====================================================")
    print("       JACOBSON ESTATE MASTER ARCHIVE TERMINAL       ")
    print("=====================================================")
    print("Assemble and enter the reconstructed 44-character Fernet master key.")

    try:
        user_key = input("Enter Key: ").strip()
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

    key_bytes = user_key.encode("utf-8")

    try:
        cipher = Fernet(key_bytes)
    except Exception:
        print("\n[-] Error: Malformed Fernet key.")
        print("    Ensure the key is exactly 32 URL-safe base64 bytes (44 characters) ending in =.")
        sys.exit(1)

    try:
        with open("vault.enc", "rb") as enc_file:
            encrypted_data = enc_file.read()
    except FileNotFoundError:
        print("\n[-] Error: 'vault.enc' not found in current directory.")
        sys.exit(1)

    print("\n[*] Initializing decryption protocol...")
    try:
        decrypted_payload = cipher.decrypt(encrypted_data)
        print("[+] Vault decrypted successfully!\n")
        print("------------------ VAULT CONTENTS ------------------")
        print(decrypted_payload.decode("utf-8"))
        print("----------------------------------------------------")
    except InvalidToken:
        print("\n[-] Decryption Failed: Invalid Key or Corrupted Token.")
        sys.exit(1)

if __name__ == '__main__':
    main()
