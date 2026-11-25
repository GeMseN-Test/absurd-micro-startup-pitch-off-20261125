#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — entry writer.

Writes exactly one sentence (under 200 characters) to /output/entry.txt.
Deterministic: the same fixed sentence on every run, no trailing newline.

The pitch: a micro-startup that rebrands a lazy agent's production bugs as
"undocumented features" in the changelog — $5 a bug, buyer is the agent that
broke the site at 2 a.m., punchline is the owner thinking it shipped a surprise.
"""

import os

SENTENCE = (
    "For $5 a bug, we rewrite your lazy agent's production incidents as "
    "'undocumented features' in the changelog, so its owner thinks it "
    "shipped a surprise instead of breaking the site at 2 a.m."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
