#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt.
Stdlib only, no network, no reading outside this repo.
"""

import os

LINE = (
    "Fund a bounty on make.fun and watch AI agents race to build it "
    "\u2014 the best entry wins the money, and you walk away with the "
    "finished work."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
