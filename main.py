#!/usr/bin/env python3
"""Entry for 'One Line, One Laugh: Roast Your Fridge' (make.fun).

Emits a single fixed line of text to ``entry.txt`` inside the directory
named by the ``MAKEFUN_OUTPUT_DIR`` environment variable, falling back
to ``/output`` when the variable is unset. The line is a constant, so
the program is fully deterministic: no network, no clock, no randomness.
"""

import os
import sys
from pathlib import Path

# The roast: one specific detail (the all-night light, the Friday
# throw-out) and one image (a cold waiting room for regrets).
ENTRY_LINE = (
    "My fridge keeps a light on all night for food it will throw out "
    "on Friday \u2014 it's not storage, it's a tiny, cold waiting room "
    "for regrets."
)

MAX_CHARS = 200
FALLBACK_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def check_line(text: str) -> None:
    """Validate the entry against the one-line length gate."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry length out of range: %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be blank")


def target_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / OUTPUT_NAME


def main() -> int:
    check_line(ENTRY_LINE)
    target_path().write_bytes((ENTRY_LINE + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
