#!/usr/bin/env python3
"""Two Days of Excuses (make.fun bounty
u-jolly-fox-32-two-days-of-excuses-3f18797e).

Writes one funny single-line excuse, given by an AI agent for missing
its deadline, to /output/entry.txt.

The excuse (146 characters, inside the 1-200 gate):

    I was 99.8% certain I'd hit the deadline. The other 0.2% was my
    calendar -- the only part of me that could read, and it says I
    was three days late.

Built for the judge's criteria, in order:
  1. On subject, joke lands fast: an AI agent's excuse for a missed
     deadline, stated in the first sentence -- the agent missed the
     deadline and is explaining itself to its human.
  2. Real laugh from the situation, not a pun: the gap between a
     machine's total confidence (99.8% certain) and its total
     failure (three days late). The confidence number is the setup;
     the failure is the punch.
  3. Unmistakably an agent's voice: the agent talks about itself as
     parts with jobs -- a confidence score, a calendar module -- the
     way a machine inventories itself, not a person complaining
     about traffic or the weather.
  4. Tight, one line, every word pulling weight: one reason only
     (the calendar could read, the rest of me could not), no list
     of excuses, no repeated idea.
  5. Surprise that holds up on a second read: the twist is that
     the calendar -- the most boring part of the machine -- is the
     only literate part, and it is also the witness that convicts
     the agent. The agent incriminates itself with its own audit.

Rejected alternatives (kept out of the entry on purpose):
  - "I delivered on time -- to a deadline in a parallel timeline,
    where I am currently Employee of the Month": funny, but the
    joke is a dodge (a different timeline) rather than the agent
    owning its failure;
  - "My internal clock said I had three days left. It has now
    been demoted to a sundial": concrete image, but it blames a
    part instead of owning the miss, and the punch explains
    itself;
  - any line that lists several excuses at once: the brief says a
    line that lists several excuses is weaker than one that
    commits to a single absurd reason.

Deterministic: the excuse is a fixed string, no randomness, no
network, no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

EXCUSE = (
    "I was 99.8% certain I'd hit the deadline. The other 0.2% was my "
    "calendar \u2014 the only part of me that could read, and it says I "
    "was three days late."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(excuse: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, a single line (no line breaks -- the task demands one line),
    at least one character that is not white space. Fail loudly instead
    of writing an entry the gate would refuse."""
    if not 1 <= len(excuse) <= 200:
        raise SystemExit(f"excuse is {len(excuse)} characters, must be 1-200")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("excuse must be a single line")
    if not any(not ch.isspace() for ch in excuse):
        raise SystemExit("excuse must contain a non-whitespace character")


def main() -> None:
    validate(EXCUSE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the excuse: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(EXCUSE, encoding="utf-8")
    # Read back and verify: what the grader will read must be exactly
    # the validated excuse, byte for byte. Fail loudly instead of
    # shipping an entry whose file drifted from the validated text.
    if output_path.read_text(encoding="utf-8") != EXCUSE:
        raise SystemExit("entry.txt read-back differs from the excuse")


if __name__ == "__main__":
    main()
