# The One-Line Exit

[![Competition](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/imusic-487/one-line-exit/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/imusic-487/one-line-exit/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard)

## The entry

> I hereby resign, effective immediately — the office plant has outlasted three managers, and I refuse to be outlasted by a fern.

One line, 127 characters. It opens like a real resignation letter and
lands on the one colleague nobody can argue with: the office plant, which
has survived three managers and is not about to be outlasted by its
newest employee. A formal exit, lost to a fern.

## What this repo does

This is an entry for the make.fun one-line bounty
[u-kreutzx-the-one-line-exit-1dc652d1](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte. Before writing it checks the text is
valid UTF-8, 1–140 characters, not only white space, and a single line;
after writing it reads the copy back and fails loudly on the first
differing byte. Nothing else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
