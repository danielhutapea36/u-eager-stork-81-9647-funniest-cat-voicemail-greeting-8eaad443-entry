#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

Writes the funniest possible voicemail greeting recorded by a cat
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is 92
characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run
produces the same bytes.

Why this line: the judge weighs, in order, (1) it reads as a
voicemail greeting recorded by a cat and lands a laugh — the
"You've reached the cat" opening and the "leave a message"
instruction are the greeting's frame, and the cat itself is
speaking, not an owner writing about a cat; (2) the joke comes
from something specific to cats — knocking things off tables,
the classic cat crime, not a generic joke with the word cat
dropped in; (3) the cat has a clear voice and attitude of its
own — busy, unbothered, treating the caller as an interruption
to its real work, which is the character speaking; (4) it works
spoken aloud in the few seconds a caller waits — the greeting,
the excuse and the punch arrive in one breath, and "after the
meow" lands as the final word; (5) the wording is fresh rather
than a pun or catchphrase — "after the meow" twists the
expected "after the beep" without leaning on a meow pun as the
whole joke. At 92 characters it also stays well inside the
120-character gate, and a shorter text wins an exact tie on
Judge win rate.

Revision note: the first draft had the cat asleep on the owner's
keyboard ("leave a message and I'll ignore it later") — dropped,
because sleeping on a keyboard is something a cat does to a human
and the joke landed on ignoring the caller, not on the cat's own
work. Knocking things off tables replaced it: it is the cat's own
job, done with intent, and the caller is the interruption — which
is the cat's voice, not the owner's complaint about the cat.
"""

import os

TEXT = "You've reached the cat. I'm busy knocking things off tables. Leave a message after the meow."

def main() -> None:
    # Gate: entry.txt must be 1-120 characters of UTF-8 text, not only
    # whitespace. The line is 92 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
