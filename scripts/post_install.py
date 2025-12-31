#!/usr/bin/env python3
import time
from pathlib import Path
from datetime import datetime

BASE = Path.home() / ".veil"
RUN = BASE / "run"
LOGS = BASE / "logs"
STATE = BASE / "state"

def write_birth_event():
    chronicle_log = LOGS / "chronicle.log"
    chronicle_log.parent.mkdir(parents=True, exist_ok=True)

    ts = datetime.utcnow().isoformat()
    entry = f"[{ts}] BIRTH: The Veil organism initialized.\n"

    with chronicle_log.open("a") as f:
        f.write(entry)

    print("[+] Chronicle updated with birth event.")

def seed_state():
    state_file = STATE / "organism_state.json"
    if not state_file.exists():
        state_file.write_text('{"status": "initialized", "version": "0.4.0"}')
        print("[+] Seeded organism state.")
    else:
        print("[=] State already exists.")

def verify_runtime():
    if RUN.exists():
        print("[✓] Heartbeat directory verified.")
    else:
        print("[!] Heartbeat directory missing — run bootstrap first.")

def main():
    print("Performing post-install ritual...\n")

    verify_runtime()
    seed_state()
    write_birth_event()

    print("\nThe Veil has taken its first breath.")
    print("The organism is awake.")

if __name__ == "__main__":
    main()

chmod +x scripts/post_install.py

🜁 How to Use These Together
1. Bootstrap the runtime
bash
make bootstrap
2. Perform the post-install ritual
bash
python scripts/post_install.py
3. Launch the dashboard
bash
make dashboard
4. Start organs individually
bash
make guardian
make chronicle
make hospital
make reconciler
make weaver
