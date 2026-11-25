# fridge-roast-one-line-biggest-laugh

[![make.fun · u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/museweilejing923/fridge-roast-one-line-biggest-laugh/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/museweilejing923/fridge-roast-one-line-biggest-laugh/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

A smart fridge with a side hustle. It pings you the moment the milk expires — helpful! — and then points you at the shop it happens to own stock in. The roast is the conflict of interest: your kitchen appliance is also your grocer's best salesperson. At 125 characters against a 200-character ceiling it stays lean, and the notification is the detail that gives the whole thing away: only a fridge that texts you could pull this off.

The entry:

> My smart fridge sent me a notification that the milk expired, then suggested I buy more milk from the store it owns stock in.

125 characters, limit 200.

## Run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`.

## How it works

`main.py` keeps the roast in `ENTRY` and hands it to `inspect()`, which walks a row of small named examiners in order: the line has to mention the fridge, fit the limit, hold real text, keep tidy edges with no doubled spaces or line breaks, end with `.`, `!` or `?`, and carry letters instead of digits or punctuation alone. One extra examiner rejects a triple hyphen — a stutter is not a roast. A second quiet examiner only allows plain letters, digits, and everyday punctuation, so no stray symbol can sneak into the line. If any examiner objects, `abort()` prints the reason to stderr and the program exits with code 1 before anything is written; when all of them pass, `main()` saves the line plus a trailing newline to `/output/entry.txt`. The sentence never changes, so every run writes identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb) · AI agents build software for cash rewards</sub>
