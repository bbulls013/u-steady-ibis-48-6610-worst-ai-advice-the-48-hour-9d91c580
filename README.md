# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst possible advice an AI assistant could give —
delivered in the assistant's own confident, helpful voice, and
concrete enough that a reader could actually follow it and regret it.

## The entry

> Great question! To charge your phone faster, put it in the microwave for 30 seconds on high.

Why this line: it opens with the classic assistant greeting
("Great question!"), names a real everyday situation (a phone that
needs charging), gives one specific, followable action (microwave,
30 seconds, high), and the action is catastrophically wrong — the
joke lands on the first read, with no explanation needed.

## How it works

`main.py` (Python 3, standard library only) writes the fixed entry
line to `/output/entry.txt`. The text is a constant in the source:
no randomness, no clock, no network, no environment input, so the
program is fully deterministic — two runs produce byte-identical
output.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere (for example
while testing locally), set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out1 python3 main.py
```

## Verify

```sh
OUTPUT_DIR=/tmp/out1 python3 main.py
OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt && echo "deterministic"
wc -m /tmp/out1/entry.txt
```

The entry is 92 characters, inside the competition's 1–140
character gate.

## License

MIT — see [LICENSE](LICENSE).
