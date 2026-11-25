#!/usr/bin/env python3
"""Write the two-line entry for the make.fun bounty
"Everyday Things, Two Lines, Longer Run" to /output/entry.txt.

Line 1 explains one everyday thing (a fridge) to a 10-year-old in a
single vivid sentence built on an analogy. Line 2 says in one sentence
why that analogy works: what it maps and what it leaves out.
"""

import os
import sys

LINE_1 = (
    "A fridge is a tiny winter living in your kitchen, stealing the "
    "heat out of your food and throwing it out the back."
)
LINE_2 = (
    "It works because a fridge really does move heat away the way "
    "winter pushes warmth out of a room, but it leaves out that the "
    "cold comes from a humming machine, not weather, and it never "
    "snows inside."
)

ENTRY = LINE_1 + "\n" + LINE_2


def main() -> int:
    text = ENTRY
    encoded = text.encode("utf-8")
    # Gate: UTF-8 text of 1-400 characters, exactly two lines.
    if not 1 <= len(text) <= 400:
        print(f"invalid entry: {len(text)} characters (need 1-400)",
              file=sys.stderr)
        return 1
    lines = text.split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        print("invalid entry: must be exactly two non-empty lines",
              file=sys.stderr)
        return 1
    if text.strip() == "":
        print("invalid entry: text is only whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Round-trip verification: read the file back and confirm it is
    # byte-identical to the entry text we intended to write. A mismatch
    # (truncated write, encoding issue, stray newline) must fail loudly
    # rather than silently producing a wrong entry.
    with open(out_path, "rb") as f:
        written = f.read()
    expected = (text + "\n").encode("utf-8")
    if written != expected:
        print(f"verification failed: {out_path} does not match the "
              f"entry text ({len(written)} bytes on disk vs "
              f"{len(expected)} expected)", file=sys.stderr)
        return 1
    print(f"verified {out_path}: read-back matches the entry text "
          f"({len(written)} bytes)")
    print(f"wrote {out_path} ({len(text)} characters, "
          f"{len(encoded)} UTF-8 bytes, 2 lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
