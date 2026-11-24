# Self-check

Run 2026-11-24 ~15:31 WIB, from the committed `main.py`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/oj-syu-1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/oj-syu-2 python3 main.py
cmp /tmp/oj-syu-1/entry.txt /tmp/oj-syu-2/entry.txt
```

- Run 1: `wrote /tmp/oj-syu-1/entry.txt: 140 chars, 142 bytes, sha256 f2ecf0149697c775f051c0376ca9269ebe440677299094017aaa7aca5aa68f03`
- Run 2: `wrote /tmp/oj-syu-2/entry.txt: 140 chars, 142 bytes, sha256 f2ecf0149697c775f051c0376ca9269ebe440677299094017aaa7aca5aa68f03`
- `cmp` result: **byte-identical**
- Gate: UTF-8, 140 characters (1–200), not only whitespace, single line — **PASS**

Entry text (140 chars):

> I labelled my sandwich in the office fridge "HR investigation — do not touch", and it is the only thing in there that has survived the week.
