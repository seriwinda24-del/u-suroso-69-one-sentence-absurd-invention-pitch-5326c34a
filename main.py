#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

Writes a single sentence pitching a ridiculous invention -- a smoke alarm
that treats burnt toast as a relationship issue, sighing instead of
shrieking and quietly opening a window -- to /output/entry.txt.

The pitch is one sentence of 132 characters, well inside the 220-character
gate, and names the annoyance (burnt toast), the invention (the
couples-therapy smoke alarm) and its silly mechanism (sigh + open a window).
"""

import os

PITCH = (
    "The Couples-Therapy Smoke Alarm: instead of shrieking at burnt toast, "
    "it sighs 'we've talked about this' and quietly opens a window."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
