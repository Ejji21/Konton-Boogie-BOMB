# Konton Boogie Bomb

A fullscreen PyQt6 video player that maxes out system volume on launch.

## Requirements

- Windows 10 or later
- Python 3.10–3.12 (recommended; newer versions may work but are less tested)

## Setup

1. Clone the repo and `cd` into it.
2. Install dependencies:

```
pip install PyQt6 pycaw pyinstaller
```

## Running from source

```
python KontonBoogieBomb.py
```

Press **Alt+F11** at any time to close the window.

## Building the .exe

Make sure `KONTONBOOGIE.mp4` and `icon.ico` are in the same folder as the script, then run:

```
pyinstaller --onefile --noconsole --collect-all PyQt6 --icon=icon.ico --add-data "KONTONBOOGIE.mp4;." KontonBoogieBomb.py
```

The finished executable will be in:

```
dist/KontonBoogieBomb.exe
```

It's fully self-contained — the video and icon are bundled inside, so the `.exe` can be shared as a single file.

### Troubleshooting

If the app opens to a black screen, rebuild without `--noconsole` to see the error output:

```
pyinstaller --onefile --collect-all PyQt6 --icon=icon.ico --add-data "KONTONBOOGIE.mp4;." KontonBoogieBomb.py
```

Common fix: make sure the video filename in `--add-data` exactly matches the filename used in `resource_path(...)` inside the script.
