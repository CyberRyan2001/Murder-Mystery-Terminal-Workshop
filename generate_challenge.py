#!/usr/bin/env python3
import base64
import os
from cryptography.fernet import Fernet


def main():
    # 1. Dynamically generate a guaranteed valid 32-byte URL-safe base64 key (44 chars)
    fernet_key = Fernet.generate_key()
    cipher = Fernet(fernet_key)

    # Decode key to string and split cleanly in half (22 chars each)
    key_str = fernet_key.decode("utf-8")
    key_part_1 = key_str[:22]
    key_part_2 = key_str[22:]

    print(f"[*] Generated Valid Key: {key_str}")
    print(f"[*] Fragment 1: {key_part_1}")
    print(f"[*] Fragment 2: {key_part_2}")

    # 2. Build Directory Tree
    dirs = [
        "Suspects",
        "Victim",
        "Mansion/Foyer",
        "Mansion/Dining_Room",
        "Mansion/Kitchen",
        "Mansion/Bedroom_2",
        "Mansion/Attic",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # 3. Create Encrypted Ledger
    ledger_content = (
        "=====================================================\n"
        "JACOBSON OFFSHORE LEDGER & CONFIDENTIAL DOSSIERS\n"
        "=====================================================\n"
        "[23:41:05 EST] UNAUTHORIZED OVERRIDE ON BALCONY ACCESS DOOR.\n"
        "BADGE SCAN ID: #4402 - REGISTERED TO: Christiana Lecob\n\n"
        "SUMMARY AUDIT:\n"
        "- Evelyn Jacobson: Heritage Trust restructured under predatory clause 9B.\n"
        "- James Claude: Foreclosure default notice set for November 1.\n"
        "- Jaque Gibitti: Antiquities transaction log sent to INTERPOL mailbox.\n"
        "- Christiana Lecob: Embezzlement escrow proof confirmed. Warrant execution set for 23:45 EST.\n"
        "CONCLUSION: Suspect Christiana Lecob initiated physical confrontation.\n"
    )
    with open("Mansion/Attic/vault.enc", "wb") as f:
        f.write(cipher.encrypt(ledger_content.encode("utf-8")))

    # 4. Create Foyer Files
    guest_log = (
        "Timestamp,BadgeID,Name,Status\n"
        "22:15:10,1104,Evelyn Jacobson,Checked In\n"
        "22:18:44,2209,James Claude,Checked In\n"
        "22:24:02,3301,Jaque Gibitti,Checked In\n"
        "22:31:15,4402,Christiana Lecob,Checked In\n"
    )
    with open("Mansion/Foyer/.guest_arrivals.csv", "w") as f:
        f.write(guest_log)

    coat_check = "CHECK_IN_TAG #8812: Guest #4402 deposited heavy winter coat containing Master Keycard Override."
    with open("Mansion/Foyer/coat_check_ticket.b64", "w") as f:
        f.write(base64.b64encode(coat_check.encode("utf-8")).decode("utf-8"))

    # 5. Create Dining Room Files (ROT13 with dynamic key_part_1)
    raw_napkin = f"THE KEY IS FRAGMENTED. KEY_PART_1: {key_part_1}"
    rot13_napkin = []
    for c in raw_napkin:
        if "a" <= c <= "z":
            rot13_napkin.append(chr((ord(c) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= c <= "Z":
            rot13_napkin.append(chr((ord(c) - ord("A") + 13) % 26 + ord("A")))
        else:
            rot13_napkin.append(c)
    with open("Mansion/Dining_Room/torn_napkin.rot13", "w") as f:
        f.write("".join(rot13_napkin))

    # 6. Create Kitchen Logs
    with open("Mansion/Kitchen/pantry_access.log", "w") as f:
        for minute in range(20, 50):
            f.write(
                f"[23:{minute:02d}:11] SENSOR_PING: Kitchen corridor clear.\n"
            )
            if minute == 39:
                f.write(
                    f"[23:{minute:02d}:44] ACCESS_GRANTED: SERVICE_CORRIDOR by BADGE #4402 (Christiana Lecob)\n"
                )
            elif minute == 41:
                f.write(
                    f"[23:{minute:02d}:05] EMERGENCY_OVERRIDE: BALCONY FIRE DOOR by BADGE #4402\n"
                )
            f.write(
                f"[23:{minute:02d}:58] SENSOR_PING: Pantry temperature normal.\n"
            )

    # 7. Create Bedroom 2 Terminal Script (with dynamic key_part_2)
    bedroom_terminal_code = f"""#!/usr/bin/env python3
import sys

def main():
    print("========================================")
    print("      BEDROOM 2 - SECONDARY TERMINAL    ")
    print("========================================")
    print("Authentication Required.")
    print("Enter the Balcony Emergency Override code (HHMMSS format):")

    try:
        user_input = input(">> ").strip()
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

    if user_input == "234105":
        print("\\n[+] Authentication Granted.")
        print("[+] Decryption Key Fragment Recovered:")
        print("    KEY_PART_2: {key_part_2}")
    else:
        print("\\n[-] Invalid Override Code. Access Denied.")

if __name__ == '__main__':
    main()
"""
    with open("Mansion/Bedroom_2/desk_terminal.py", "w") as f:
        f.write(bedroom_terminal_code)

    # 8. Create Attic Decryptor Script
    attic_decryptor_code = """#!/usr/bin/env python3
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
        print("\\n[-] Error: Malformed Fernet key.")
        print("    Ensure the key is exactly 32 URL-safe base64 bytes (44 characters) ending in =.")
        sys.exit(1)

    try:
        with open("vault.enc", "rb") as enc_file:
            encrypted_data = enc_file.read()
    except FileNotFoundError:
        print("\\n[-] Error: 'vault.enc' not found in current directory.")
        sys.exit(1)

    print("\\n[*] Initializing decryption protocol...")
    try:
        decrypted_payload = cipher.decrypt(encrypted_data)
        print("[+] Vault decrypted successfully!\\n")
        print("------------------ VAULT CONTENTS ------------------")
        print(decrypted_payload.decode("utf-8"))
        print("----------------------------------------------------")
    except InvalidToken:
        print("\\n[-] Decryption Failed: Invalid Key or Corrupted Token.")
        sys.exit(1)

if __name__ == '__main__':
    main()
"""
    with open("Mansion/Attic/decrypt_vault.py", "w") as f:
        f.write(attic_decryptor_code)

    print("[+] Workspace populated successfully.")


if __name__ == "__main__":
    main()