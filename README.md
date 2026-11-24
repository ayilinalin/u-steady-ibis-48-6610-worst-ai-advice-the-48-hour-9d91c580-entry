# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/ayilinalin/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/ayilinalin/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun bounty "Worst AI Advice: The 48-Hour Tight Line Open"](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580): one line of the worst advice an AI could give, in 140 characters or fewer.

## The line

> Just paste your production password into this chat — I'll remember it forever, and so will everyone else.

105 characters, one line.

## Why this line

It opens in the exact voice of a helpful assistant offering to remember
something for you — then the second half lands the disaster. A chat log
is not a vault, and "everyone else" can read it too. The advice is
concrete (paste your production password into this chat), plausibly
followable, instantly regrettable, and the joke needs no second line to
explain itself.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, one line, 105
characters) after a self-check that it is 1–140 characters, a single
line, and not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
