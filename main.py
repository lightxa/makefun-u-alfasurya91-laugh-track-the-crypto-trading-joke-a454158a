"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto and trading life to
/output/entry.txt, then self-checks the kit gate: UTF-8 text, 1 to 200
characters, a single non-blank line.

The joke is one concrete trading incident, told deadpan: a stop-loss
that triggers twelve cents early, the price bouncing back before the
coffee cools, and the broker keeping the cents as a tip. Setup, turn,
punchline at the end, nothing padded.
"""

JOKE = (
    "My stop-loss hit twelve cents early, the price bounced before "
    "my coffee cooled, and my broker kept the cents as a tip."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the joke and verify it against the kit gate."""
    line = JOKE.strip()

    # Gate self-checks, exactly as the sealed scorer applies them.
    assert line, "entry must not be empty or only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry is {len(line)} characters, cap is {MAX_CHARS}"
    )
    line.encode("utf-8")  # raises if the text is not valid UTF-8

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
