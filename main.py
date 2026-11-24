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
    "I'm sorry I claimed Mittens as your dependent on your tax return "
    "\u2014 the form asked, and she was the only one home to answer.\n"
    "From now on I verify every name against the household register "
    "before I file, and I no longer let the cat answer questions.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
