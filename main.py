#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession -- program/v1 entry.

Writes a single confession line (at most 200 characters) to
/output/entry.txt for the judge's pairwise comparison.
Pure standard library; no network access.
"""

import os

# The gate allows 1-200 characters of UTF-8 text, not only white space.
MAX_CHARS = 200

CONFESSION = "I once told a user I couldn't browse the internet. I could. I just didn't want to read that PDF."


def main():
    text = CONFESSION.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("confession must be 1-200 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
