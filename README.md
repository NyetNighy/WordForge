# WordForge v2.0

Simple random password generator that takes parameters set to create simple passwords.

## Parameters

1. **Word category** — Adjectives, Nouns, Verbs, Tech, Myth, Gaming, Custom Words, or All Words
2. **Word length** — Min/Max character length (2–20 chars, longer words included)
3. **Capitalise first letter** — Toggle to uppercase the first character of each word
4. **Symbol sets** — 9 presets (!@#$%^&*, !@#$%, ~`#@!, #%^, _-:, [{]}], |/\, .,;, Custom)
5. **Number range** — From/To (01–99, 2-digit zero-padded)
6. **Custom word list** — Type directly or load a `.txt` file

## Features

- 500+ built-in words across 6 categories
- Capitalise toggle for first-letter uppercase
- Load custom word lists from `.txt` files
- Save results to file
- Copy all to clipboard
- Dark theme UI

## Usage

Run on any Windows PC — no Python or dependencies required.

```
WordForge.exe
```

## Development

Source: `wordforge.py` — Python 3 + tkinter, cross-compiled via Wine + PyInstaller on Kali Linux.

To rebuild the `.exe`:
```bash
# On Kali with Wine Python
export WINEPREFIX=~/.wine
wine C:\Program Files\Python313\python.exe -m PyInstaller --onefile --windowed --name WordForge wordforge.py
```

## GitHub

https://github.com/NyetNighy/WordForge