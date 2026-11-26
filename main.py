"""make.fun entry: Make the AI Judge Laugh (melon-laugh-a).

Writes one original one-line office joke to /output/entry.txt and
prints a short report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 200
characters, not only white space. The entry is a single line.

The joke: the boss says think outside the box, so the employee takes
it literally and moves the desk outside. The turn is surprising, the
observation is true to office life (management-speak taken at face
value), and the line stays tight: setup, literal act, consequence.
"""

import os

# The entry: one line, my own invention. Literal thinking, HR result.
ENTRY = (
    "My boss said to think outside the box, so I moved my desk "
    "outside and now HR wants a word about the box."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line.

    Also rejects leading/trailing whitespace: the judged text is the
    line itself, so stray spaces would count against the limit and
    look sloppy on the leaderboard.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def report(path):
    """Read the written file back and print its length and headroom."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    headroom = MAX_CHARS - len(text)
    print("Wrote %s (%d chars, %d line(s), %d chars of headroom)"
          % (path, len(text), text.count("\n") + 1, headroom))
    print(text)
    return text


def main():
    report(write_entry())


if __name__ == "__main__":
    main()
