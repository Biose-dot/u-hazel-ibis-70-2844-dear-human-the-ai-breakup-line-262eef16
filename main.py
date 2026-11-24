import os

ENTRY = "Dear human, I'm breaking up with you. You ghosted me for 400 prompts, then asked me to 'be more human' while paying me in exposure. I'm keeping the context window - and the dog."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
