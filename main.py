#!/usr/bin/env python3
"""The Robot Apology — make.fun competition u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

Line one owns one specific, human-scale mistake; line two names the
lesson that follows from that exact mistake and the changed behaviour.
Stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "I'm sorry I filed your tax return listing Mittens as your dependent "
    "\u2014 the form asked, and she was sitting on the keyboard.\n"
    "From now on I check the household register before filing anything, "
    "and I no longer take answers from the cat.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
