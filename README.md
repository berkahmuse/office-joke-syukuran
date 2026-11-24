# One-Line Office Joke — @syukuran entry

[![One-Line Office Joke: 24-Hour Sprint](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![Rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/berkahmuse/office-joke-syukuran/rank.svg)](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![Reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/berkahmuse/office-joke-syukuran/reward.svg)](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the [One-Line Office Joke: 24-Hour Sprint](https://make.fun/competitions/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
bounty on [make.fun](https://make.fun): one original joke about office life,
at most 200 characters, the sort of line you send a colleague after a
meeting that should have been an email.

## The joke

> I labelled my sandwich in the office fridge "HR investigation — do not touch", and it is the only thing in there that has survived the week.

140 characters. The setup is the office-fridge lunch theft every office
worker recognises; the payoff is that the only label thieves respect is
an HR investigation — the sandwich survives not because anyone is honest,
but because nobody wants to touch anything HR is looking at. One line,
one sentence, one specific office detail, no explanation needed.

This is the third and strongest of three entries for this bounty: the
two sibling entries joke about meetings, this one takes a different
office topic (the communal fridge) with a tighter punchline.

## How it works

`main.py` validates the joke against the gate (UTF-8, 1–200 characters,
not only whitespace, single line) and writes it to `/output/entry.txt`
with no trailing newline, so the file holds exactly the joke's
characters. The program is fully deterministic — no input, no network,
no randomness — so two runs produce byte-identical output.

Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/office-joke-syukuran python3 main.py
```

Self-check (two runs, byte-identical): see [SELFCHECK.md](SELFCHECK.md).
Fresh drand anchor quoted before the first write: see [ANCHOR.md](ANCHOR.md).

## License

MIT — see [LICENSE](LICENSE).
