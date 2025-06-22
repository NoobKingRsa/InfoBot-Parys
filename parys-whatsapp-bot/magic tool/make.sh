#!/bin/bash

cd "$(dirname "$0")"  # make sure we are in magic-tool/
cd ..

LOG_DIR="logs"
mkdir -p $LOG_DIR
TIMESTAMP=$(date +%Y-%m-%d-%H%M%S)
LOG_FILE="$LOG_DIR/${TIMESTAMP}-make.log"

echo "🔍 Step 1: Verifying services.txt..." | tee -a "$LOG_FILE"
python3 magic-tool/verify.py >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
  echo "❌ Verification failed. Fix your TXT file before continuing." | tee -a "$LOG_FILE"
  exit 1
fi

echo "💾 Step 2: Backing up existing JSON..." | tee -a "$LOG_FILE"
bash magic-tool/backup.sh >> "$LOG_FILE" 2>&1

echo "🛠️  Step 3: Rebuilding services.json from TXT..." | tee -a "$LOG_FILE"
python3 magic-tool/txt_to_json.py >> "$LOG_FILE" 2>&1

echo "✅ Done! Your bot is updated safely." | tee -a "$LOG_FILE"