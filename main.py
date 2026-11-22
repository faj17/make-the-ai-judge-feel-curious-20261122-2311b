#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: a quiet mystery with a
concrete image, a scene and a turn, written to leave the reader asking.
No network, no input, no dependencies.
"""

import os

TEXT = (
    "The bottle washed up on the same beach every spring for eleven years. "
    "Inside, the same handwriting, the same six words: "
    "'Tell her the tide kept its promise.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
