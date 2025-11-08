# Final Cut Pro Lyrics Plugin

A simple Python script that generates FCPXML files to add timed lyrics as title elements to Final Cut Pro timelines.

## Overview

This project demonstrates how to programmatically add text elements to Final Cut Pro by generating FCPXML files. The main use case is adding synchronized lyrics to video projects.

## How It Works

1. **Input**: Reads `lyrics.json` containing word-level timing data
2. **Processing**: Generates FCPXML with title clips for each word, aligned to frame boundaries
3. **Output**: Creates `lyrics.fcpxml` that can be imported into Final Cut Pro

## Usage

```bash
python3 main.py
```

Then in Final Cut Pro:
1. Go to **File > Import > XML**
2. Select `lyrics.fcpxml`
3. Lyrics appear on your timeline with perfect timing

## Files

- **[main.py](main.py)** - Main script that generates FCPXML from lyrics.json
- **[objective.md](objective.md)** - Project goals and requirements
- **[RESEARCH_FINDINGS.md](RESEARCH_FINDINGS.md)** - Research on approaches for adding timeline elements to FCP

## Requirements

- Python 3
- Final Cut Pro
- A `lyrics.json` file with word-level timing data

## Key Features

- Snaps timing to 30fps frame boundaries to avoid warnings
- Uses rational number format for precise timing
- Customizable text styling (Coolvetica font, size 80, centered, bold)
- Minimal, straightforward code

## License

MIT
