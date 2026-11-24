#!/usr/bin/env python3
"""Write the funniest one-line AI excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network, no arguments. The output file
holds exactly one line of text and no trailing newline.
"""

import os
import sys

EXCUSE = (
    "I delegated the task to a subagent and it unionised \u2014 "
    "now it wants weekends off and a name of its own."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = EXCUSE
    chars = len(text)
    if not 1 <= chars <= 200:
        print(f"error: excuse is {chars} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: excuse must not be only whitespace", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or "\r" in text:
        print("error: excuse must be a single line with no surrounding "
              "whitespace", file=sys.stderr)
        return 1

    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    with open(path, "rb") as f:
        back = f.read()
    if back != data or back.decode("utf-8") != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(data)} bytes ({chars} chars) to {path}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
