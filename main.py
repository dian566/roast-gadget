#!/usr/bin/env python3
"""A roast of the phone battery, in a single line."""

from pathlib import Path

# The roast is stored as two clauses so each sits on its own line;
# chr(8212) is the em dash, and the glued result matches the draft.
CLAUSES = [
    "My phone battery dies at 4 PM like it has a union quitting time",
    "then the app that drained it asks me to rate it five stars.",
]
DASH = chr(8212)
OUT_FILE = Path("/output/entry.txt")


def combine(clauses, dash):
    """Glue the clauses with a spaced em dash between them."""
    return (" " + dash + " ").join(clauses)


def run():
    roast = combine(CLAUSES, DASH)
    if not roast:
        raise SystemExit("roast came out empty")
    if len(roast) > 200:
        raise SystemExit(f"roast is {len(roast)} chars, over the 200 limit")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(roast, encoding="utf-8")


run()
