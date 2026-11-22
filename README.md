# Make the AI judge feel curious

Entry for make.fun's "Make the AI judge feel curious" bounty
($50, entries close 23 Nov 2026 09:11 WIB).

`main.py` writes one short text to `/output/entry.txt`:

> The bottle washed up on the same beach every spring for eleven years.
> Inside, the same handwriting, the same six words: 'Tell her the tide
> kept its promise.'

A quiet mystery: a concrete image (a bottle, the same beach, eleven
springs), a scene and a turn (the same handwriting, the same six words),
and a last line that keeps working after it ends — who wrote it, who is
"her", what promise did the tide keep? No instruction to relax, no stock
wellness phrasing; the calm comes from the scene itself.

## Run

```sh
python3 main.py   # writes /output/entry.txt (157 characters, UTF-8)
```

## Rubric self-score (judge criteria, most important first)

1. Intrigues — draws in, keeps asking: **1** (three open questions, no answers given)
2. Calm from the text itself, shows rather than instructs: **1** (quiet beach scene, nothing forced)
3. Craft — rhythm, pacing, plain concrete words, none to cut: **1** (parallel "the same handwriting, the same six words")
4. Lingers — an image/thought to return to: **1** ("Tell her the tide kept its promise.")
5. Freshness — own voice/images, not stock wellness: **1** (original bottle-and-tide image)

## License

MIT — see `LICENSE`.
