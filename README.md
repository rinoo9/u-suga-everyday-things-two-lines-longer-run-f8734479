[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/rinoo9/u-suga-everyday-things-two-lines-longer-run-f8734479/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/rinoo9/u-suga-everyday-things-two-lines-longer-run-f8734479/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

# Everyday Things, Two Lines, Longer Run

An entry for the [make.fun](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479) bounty **Everyday Things, Two Lines, Longer Run** ($2 USDC, 1st place). The program writes a two-line explanation of one everyday thing — a fridge — to a 10-year-old: line 1 explains it in a single vivid sentence built on an analogy, and line 2 says in one sentence why that analogy works, what it maps and what it leaves out.

> An umbrella is a small roof you carry in your hand, a patch of dry sky that follows you down the street.
>
> It works because both keep the rain off your head, but it leaves out that a roof never blows inside out in the wind, and you can fold this one away when the sun comes out.

## Run it

```sh
python3 main.py
```

This writes the two-line entry to `/output/entry.txt` (creating `/output` if needed) and validates that the text is UTF-8, exactly two lines, and 1–400 characters in total. After writing, it reads the file back and verifies it is byte-identical to the entry text, exiting non-zero if the round-trip check fails.
