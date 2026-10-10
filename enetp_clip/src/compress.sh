#!/bin/bash
# Compression finale du clip (débruitage léger + x264 crf 23) : ~66 Mo -> ~39 Mo
set -euo pipefail
cd "$(dirname "$0")/.."
ffmpeg -y -v error -i "${1:?usage: compress.sh <in.mp4> <out.mp4>}" \
  -vf "hqdn3d=2:1.5:6:6" -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p \
  -c:a copy -movflags +faststart "${2:?}"
