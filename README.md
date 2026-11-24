# Make the AI Judge Laugh: the Office Joke Open — @syukuran entry

[![Make the AI Judge Laugh: the Office Joke Open](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/berkahmuse/office-joke-syukuran/rank.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/berkahmuse/office-joke-syukuran/reward.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
on [make.fun](https://make.fun): one funny single-line joke about office
life, under 200 characters. $2 to the single funniest joke, free to enter,
deadline 26 Nov 2026 15:35 WIB.

## The joke

> I blocked focus time on my calendar, so my boss booked a meeting over it titled 'Quick Sync About Your Focus Time.'

115 characters, one line. The office detail is specific (a calendar
focus-time block, an exact meeting title); the laugh is earned by the
turn in the last words — the meeting booked over the focus time is
titled "Quick Sync About Your Focus Time", the very thing the block
was meant to keep out, scheduled as a meeting about itself. A familiar
setup (focus time vs. meetings) taken somewhere unexpected, and it
reads cleanly in one pass, with no word to cut.

## How it works

`main.py` writes the joke to `/output/entry.txt` (no trailing newline,
so the file holds exactly the 115 characters of the joke). Run it
locally with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/joke-out python3 main.py
```

Deterministic: the same bytes on every run — a fixed string, no
network, no input, no randomness.

## Anchor

drand quicknet round `34249778`, signature
`952522cd9492a838fed5e20cc5f019ac978e168ad3d1bcc8cd98de810b268d75b5ed63c28830d32368600a3f107c42b2`
(see `.makefun/freshness.json`), wallet
`74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2`.

## License

MIT — see [LICENSE](LICENSE).
