#!/usr/bin/env python3
"""One-Line Office Joke entry for @syukuran.

Competition: u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162
(One-Line Office Joke: 24-Hour Sprint, make.fun)

The program writes one original joke about office life to
/output/entry.txt. The joke is a single sentence: the setup is the
universal office-fridge lunch theft, the payoff is that labelling the
sandwich as an HR investigation is the one thing that keeps it safe.
It is a different office topic from the meeting jokes in the two
sibling entries, and it is built on one specific, recognisable detail
rather than a generic complaint.

Drand anchor quoted before the first write of the entry file
(see ANCHOR.md):
  drand-quicknet round 34235197
  randomness caed9377986e7108439c452ca5809603622fbd082f558f6118be070e92fec32e

Deterministic: no input is read, no network is used, no randomness is
involved, so every run writes byte-identical output.
"""

import hashlib
import os
import sys

JOKE = (
    "I labelled my sandwich in the office fridge "
    '"HR investigation \u2014 do not touch", '
    "and it is the only thing in there that has survived the week."
)

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def entry_text():
    return JOKE


def gate_check(text):
    """Return a list of gate violations; empty means the text passes."""
    violations = []
    if not GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS:
        violations.append(
            "length %d chars, gate needs %d-%d"
            % (len(text), GATE_MIN_CHARS, GATE_MAX_CHARS)
        )
    if not text.strip():
        violations.append("text is only whitespace")
    if "\n" in text or "\r" in text:
        violations.append("text spans more than one line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return violations


def output_path(argv):
    if len(argv) > 1:
        return argv[1]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return DEFAULT_OUTPUT_PATH


def run(argv):
    text = entry_text()
    violations = gate_check(text)
    if violations:
        for violation in violations:
            print("gate failed: " + violation, file=sys.stderr)
        return 1

    path = output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    raw = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(raw)

    digest = hashlib.sha256(raw).hexdigest()
    print("wrote %s: %d chars, %d bytes, sha256 %s"
          % (path, len(text), len(raw), digest))
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv))
