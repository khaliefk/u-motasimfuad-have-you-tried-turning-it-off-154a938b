#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- make.fun one-liner entry.

Writes one funny line, spoken by a hopeless tech support agent to a
desperate customer, to /output/entry.txt. The agent is cheerfully
useless: the computer has given up, and so has he, so his only plan
is the classic restart, preferably together, sitting quietly a while.

Stdlib only. No network, no files read, no arguments required.
An optional first argument (or ENTRY_OUTPUT) overrides the output path,
for local testing only; the grader runs it with no arguments.
"""

import os
import sys

ENTRY = (
    "Good news: your computer isn't broken, it's just given up, "
    "and honestly, same. Have you tried turning it off and on again, "
    "or should we both sit here a while?"
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "ENTRY_OUTPUT", DEFAULT_OUTPUT
    )
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
