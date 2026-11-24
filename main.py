"""The Robot Pickup Line Championship entry for make.fun: one pickup line a robot would say out loud."""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# A robot pickup line grown out of machine life: a full diagnostic finds exactly one fault — you, making its cooling fans spin.
ENTRY = "I ran a full diagnostic on myself. The only fault it found was you — standing there, making my cooling fans spin."


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must be a single line with no surrounding whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
