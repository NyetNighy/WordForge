# WordForge v2.1

Simple random password generator that takes parameters to create word-based passwords.

## Parameters

| Parameter | Options |
|-----------|---------|
| **Word Category** | All Words, Adjectives, Nouns, Verbs, Tech, Myth, Gaming, Custom Words |
| **Word Length** | Min/Max from 2–20 characters (longer words included) |
| **Case Mode** | `none` (lowercase), `first` (First Capital), `random` (rAnDoM CaSe) |
| **Symbol Sets** | 9 presets — `!@#$%^&*`, `!@#$%`, `~`#@!`, `#%^`, `_-:`, `[{]}`, `|/`, `.,;`, Custom |
| **Number Range** | From/To — 01 to 99 (zero-padded 2 digits) |
| **Custom Words** | Type directly or load a `.txt` file |

## Output Format

```
word + symbol + number
e.g.  Blaze!42  |  cRyPtO#17  |  SynC$99
```

## Features

- 500+ built-in words across 6 categories
- Long words (10–16 chars) included
- Case modes: lowercase, first-capital, random mixed case
- Load custom word lists from `.txt` files
- Save results to file
- Copy all to clipboard
- Dark theme GUI

## Usage

Run on any Windows PC — no Python or dependencies required. Just double-click `WordForge.exe`.

## Development

- **Source:** `wordforge.py` — Python 3 + tkinter
- **Build:** Cross-compiled via Wine + PyInstaller on Kali Linux
- **Icon:** Custom lightning bolt (ImageMagick + PIL)

To rebuild the `.exe`:
```bash
export WINEPREFIX=~/.wine
wine C:\Program Files\Python313\python.exe -m PyInstaller \
  --onefile --windowed --name WordForge \
  --icon WordForge.ico wordforge.py
```

## GitHub

https://github.com/NyetNighy/WordForge