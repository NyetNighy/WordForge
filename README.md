# WordForge v2.1

Simple random password generator that takes parameters to create word-based passwords.

## Parameters

| Parameter | Options |
|-----------|---------|
| **Word Category** | All Words, Adjectives, Nouns, Verbs, Tech, Myth, Gaming, Custom Words |
| **Word Length** | Min/Max from 2–20 characters (longer words included) |
| **Case Mode** | `none` (lowercase), `first` (First Capital), `random` (rAnDoM CaSe) |
| **Symbol Sets** | 9 presets — `!@#$%^&*`, `!@#$%`, `` ~`#@! ``, `#%^`, `_-:`, `[{]}`, `|/`, `.,;`, Custom |
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

### Windows (no Python required)

Download the latest **WordForge.exe** (or installer) from the [Releases](https://github.com/NyetNighy/WordForge/releases) page and double-click it.

### From source

```bash
python3 wordforge.py
```

Requires Python 3 with tkinter (included on most Windows installs; on Linux install `python3-tk`).

## Development

- **Source:** `wordforge.py` — Python 3 + tkinter (stdlib only)
- **Build:** Cross-compiled via Wine + PyInstaller on Kali Linux

To rebuild the `.exe`:

```bash
export WINEPREFIX=~/.wine
wine C:\\Program\ Files\\Python313\\python.exe -m PyInstaller \
  --onefile --windowed --name WordForge \
  --icon WordForge.ico wordforge.py
```

Upload the resulting binary to a [GitHub Release](https://github.com/NyetNighy/WordForge/releases/new) instead of committing it to the repository.

## License

MIT — see [LICENSE](LICENSE).

## GitHub

https://github.com/NyetNighy/WordForge
