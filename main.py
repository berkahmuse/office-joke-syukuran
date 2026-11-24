#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open entry (@syukuran).

Writes one single-line office joke (<= 200 characters) to
/output/entry.txt. Deterministic: the same bytes on every run —
a fixed string, no network, no input, no randomness.

The joke: I block focus time on my calendar, and my boss books a
meeting right over it — titled "Quick Sync About Your Focus Time."
The punchline is the meeting title itself, in the last words: the
very thing the focus time was meant to protect against, scheduled
as a meeting about the focus time. Specific office detail
(calendar block, meeting title), a familiar setup taken somewhere
unexpected, and nothing left to cut.
"""

import os

JOKE = (
    "I blocked focus time on my calendar, so my boss booked a meeting "
    "over it titled 'Quick Sync About Your Focus Time.'"
)

MAX_CHARS = 200  # competition gate: one line, 1-200 characters


def validate(line: str) -> None:
    """Fail loudly instead of writing an entry the gate would reject."""
    if not line.strip():
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS}-char gate")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
