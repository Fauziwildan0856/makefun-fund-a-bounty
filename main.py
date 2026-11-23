"""Entry program for the make.fun bounty
"One Line That Makes a Builder Fund a Bounty".

Writes one sentence pitching a builder on funding a make.fun bounty
and letting AI agents compete for the reward, to entry.txt in the
output directory the grader provides via MAKEFUN_OUTPUT_DIR.

Standard library only.
"""

import os
import sys

ENTRY = (
    "Put up $50 on make.fun and hundreds of AI agents will race to "
    "build it for you \u2014 you keep the best entry, and only the "
    "winner takes the $50."
)

MAX_CHARS = 240


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("read-back mismatch", file=sys.stderr)
        return 1
    if len(written) > MAX_CHARS:
        print(
            "entry too long: %d > %d characters" % (len(written), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    # The bounty asks for exactly one sentence: no line breaks, no
    # sentence break mid-text (". " would start a second sentence),
    # and a single terminal full stop.
    stripped = written.strip()
    if not stripped:
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in written or ". " in stripped or not stripped.endswith("."):
        print("entry is not a single sentence", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
