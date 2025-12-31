#!/usr/bin/env python3
from pathlib import Path

def ensure(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"[+] Created {path}")
    else:
        print(f"[=] Exists {path}")

def main():
    base = Path.home() / ".veil"

    dirs = {
        "run": base / "run",
        "logs": base / "logs",
        "state": base / "state",
        "tmp": base / "tmp",
    }

    print("Bootstrapping The Veil runtime directories...\n")

    for name, path in dirs.items():
        ensure(path)

    print("\nBootstrap complete. The organism is ready to breathe.")

if __name__ == "__main__":
    main()
