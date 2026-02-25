#!/bin/bash
# Simple auto-generator - run this to generate 7 hours of content
# Run: ./run-7hours.sh

echo "Starting 7-hour content generation..."
echo "Will generate new tracks every hour"
echo "Press Ctrl+C to stop"
echo ""

for i in {1..7}; do
    echo "========== Generation $i/7 - $(date) =========="
    cd /home/simon/.openclaw/workspace/sunoflo
    source venv/bin/activate
    
    # Random genre and style
    python src/sunoflo.py << EOF
1
1
y
1
2
EOF
    
    echo "✅ Generation $i complete!"
    echo "Sleeping for 1 hour..."
    echo ""
    
    if [ $i -lt 7 ]; then
        sleep 3600  # 1 hour
    fi
done

echo "🎉 All 7 generations complete!"
