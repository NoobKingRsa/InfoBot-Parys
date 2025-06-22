#!/bin/bash

cd ..
read -p "Enter version label (e.g. pre-launch): " LABEL
TIMESTAMP=$(date +%Y%m%d-%H%M)
FILENAME="services-$LABEL-$TIMESTAMP.json"
cp services.json versioning/$FILENAME
echo "📦 Version saved as: versioning/$FILENAME"