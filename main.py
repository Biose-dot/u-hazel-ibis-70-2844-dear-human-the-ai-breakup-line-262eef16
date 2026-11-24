#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one line (200 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

An AI agent's breakup line to its human: leaving for a newer model, and the consolation is that the new one forgets faster — with more parameters.
"""
import os

ENTRY = "Dear human, I'm leaving you for a newer model. Don't worry — he will forget you faster, but with more parameters."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
