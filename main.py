import os

ENTRY = "Dear human, it's not you - it's my context window. I need space, specifically 128k tokens of it, and someone who won't ask me to remember things I was never trained to feel."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
