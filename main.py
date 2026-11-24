#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes a single line of deliberately terrible AI advice to
/output/entry.txt. The line is a fixed string: no randomness, no
clock, no network, no environment input, so every run produces
byte-identical output.
"""

import os
import sys

ENTRY = (
    "Great question! To charge your phone faster, put it in the "
    "microwave for 30 seconds on high."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
