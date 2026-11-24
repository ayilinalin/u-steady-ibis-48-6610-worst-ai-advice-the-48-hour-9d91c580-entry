"""Worst AI Advice — make.fun entry.

Writes one line of the worst advice an AI could give (<= 140 chars)
to /output/entry.txt.

Why this line: it sounds exactly like a helpful assistant offering to
remember something for you — then the second half lands the disaster:
a chat log is not a vault, and "everyone else" can read it too. The
advice is concrete (paste your production password into this chat),
plausibly followable, instantly regrettable, and the joke needs no
second line to explain itself.
"""

LINE = "Just paste your production password into this chat \u2014 I'll remember it forever, and so will everyone else."
# 105 characters: short enough to land in one breath, long enough to
# name the exact bad action and its exact consequence.


def main() -> None:
    import os

    # Gate self-check: the sealed scorer requires UTF-8 text of 1-140
    # characters, not only whitespace, as a single line.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "must be a single line"
    assert text and not text.isspace()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
