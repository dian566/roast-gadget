"""One-Line Roast: The Gadget You Use Every Day — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = 'My phone battery dies at 4 PM like it has a union quitting time — then the app that drained it asks me to rate it five stars.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
