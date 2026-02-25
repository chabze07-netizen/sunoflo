#!/bin/bash
# SunoFLO Auto-Generator - Runs every hour
# Usage: ./auto-generate.sh

OUTPUT_DIR="/home/simon/Downloads/sunoflo-auto"
mkdir -p $OUTPUT_DIR

echo "========================================"
echo "SunoFLO Auto-Generator - $(date)"
echo "========================================"

# Activate virtual environment
cd /home/simon/.openclaw/workspace/sunoflo
source venv/bin/activate

# Generate random style
STYLES=("Metro Boomin" "Southside" "Wheezy" "Nick Mira" "Pi'erre Bourne" "Armin van Buuren" "Dash Berlin" "Pink Floyd" "The Weeknd" "Kendrick Lamar")
STYLE=${STYLES[$((RANDOM % ${#STYLES[@]}))]}

# Run generator
echo "Generating: $STYLE"
python src/sunoflo.py << EOF
1
1
y
1
2
EOF

echo "========================================"
echo "Done! Files saved to ~/Downloads"
echo "========================================"
