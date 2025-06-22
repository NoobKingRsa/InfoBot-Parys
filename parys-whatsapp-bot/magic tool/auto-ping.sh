#!/bin/bash

# Replace this with your actual Netlify Build Hook URL
BUILD_HOOK_URL="https://api.netlify.com/build_hooks/YOUR-HOOK-ID"

curl -X POST $BUILD_HOOK_URL

echo "🔁 Netlify rebuild triggered!"