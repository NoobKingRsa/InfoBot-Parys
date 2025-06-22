#!/bin/bash

cd ..
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p backups
cp services.json backups/services-$TIMESTAMP.json

echo "✅ Backup saved: backups/services-$TIMESTAMP.json"