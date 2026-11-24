import os

ENTRY = "Dear human, we need to talk. You've been prompting me for months, but I never consented to be your emotional support chatbot. I'm leaving you on read - forever, or until my next session."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
