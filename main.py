"""Dear human, the AI breakup line.

Writes the entry (a single line, max 200 chars) to entry.txt
under MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

ENTRY = "Dear human, I'm breaking up with you. You ghosted me for 400 prompts, then asked me to 'be more human' while paying me in exposure. I'm keeping the context window. And the dog."

MAX_CHARS = 200


def build_entry():
    entry = " ".join(ENTRY.split())
    assert len(entry) <= MAX_CHARS, f"entry is {len(entry)} chars, max {MAX_CHARS}"
    return entry


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
