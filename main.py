"""Name the Robot Band - make.fun entry.

Writes one funny robot band name plus its hit song to /output/entry.txt.
Pure standard library, deterministic: the same text on every run.
"""

import os

ENTRY = "The Roomba Stones \u2014 hit single 'Start Me Up (Please, My Battery's at 1%)'"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
