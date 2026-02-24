# SunoFLO - FL Studio Project Generator

## What is SunoFLO?

SunoFLO is an AI-powered FL Studio project generator that creates .flp files using FL Studio's native plugins.

## Phase 1 - MVP Status

**Working Features:**
- Genre selection (Trap, Drill, R&B, Pop, House, Hip Hop)
- Producer style presets (Metro Boomin, Southside, Wheezy, Nick Mira, Pi'erre Bourne)
- BPM and Key settings per style
- Basic .flp file generation

**In Development:**
- Plugin integration (Sytrus, Harmor, FPC)
- Pattern generation
- Automation clips
- Full song structure

## Installation

```bash
# Clone the repository
cd sunoflo

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install pyflp

# Run
python src/sunoflo.py
```

## Usage

1. Select your genre
2. Choose a producer style preset
3. Enter a prompt (optional)
4. Click Generate
5. Open the .flp in FL Studio

## Project Structure

```
sunoflo/
├── src/
│   ├── sunoflo.py      # Main generator
│   ├── flp_writer.py   # FLP file creation
│   └── presets.py      # Style presets
├── presets/            # FL Studio presets
├── samples/           # Example projects
└── README.md
```

## Requirements

- Python 3.10+
- PyFLP library
- FL Studio 21.2+ (to open generated projects)

## Roadmap

### Phase 1 (Current)
- [x] Basic project generation
- [x] Style presets
- [x] FLP file output
- [ ] Plugin parameter mapping

### Phase 2
- [ ] Full plugin integration
- [ ] 7 producer styles working
- [ ] Full song structure
- [ ] Automation clips

### Phase 3
- [ ] AI integration
- [ ] Stem separation
- [ ] MIDI transcription
- [ ] Reference matching

---

**Note:** Phase 1 generates basic .flp files. Full AI generation requires API access to Suno/Udio and is planned for Phase 3.
