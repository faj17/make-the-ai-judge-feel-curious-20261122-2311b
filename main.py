#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for make.fun.

The text is a quiet mystery meant to leave the AI judge curious:
a bottle, the same beach, eleven springs, and six words that
promise something without explaining it. No network, no input,
no dependencies; the program only writes a file.
"""

from pathlib import Path

TEXT = "The bottle washed up on the same beach every spring for eleven years. Inside, the same handwriting, the same six words: 'Tell her the tide kept its promise.'"


def main() -> None:
    # The gate allows 1-280 characters; this text is 157.
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
