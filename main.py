#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — one-line entry.

Writes a single-line joke about office life (at most 200
characters) to /output/entry.txt: the sort of line you send a
colleague after a meeting that should have been an email.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The joke: asked HR for a raise, got a mindfulness app instead.
# Setup and punchline on one line.
# Counted at 84 characters — inside the 1..200 window.
LINE = (
    "I asked HR for a raise and they gave me a mindfulness app. "
    "Now I'm calmly underpaid."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the joke to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
