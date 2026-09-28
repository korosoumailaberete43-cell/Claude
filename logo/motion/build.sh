#!/bin/sh
# Reconstruit le teaser : images (Chromium) → bande-son (numpy) → MP4 (ffmpeg).
# Prérequis : node + playwright, python3 + numpy + imageio-ffmpeg.
set -e
cd "$(dirname "$0")"
FRAMES=${FRAMES:-/tmp/civrebar_frames}
rm -rf "$FRAMES"
NODE_PATH=$(npm root -g) node render.js frames "$FRAMES" 4
mv "$(dirname "$FRAMES")/cues.json" .
python3 sound.py
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
"$FF" -y -loglevel error -framerate 30 -i "$FRAMES/f%05d.jpg" -i out/teaser_audio.wav \
  -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart -shortest \
  out/CivRebar_AI_Teaser_1080p.mp4
rm -rf "$FRAMES"
echo "→ out/CivRebar_AI_Teaser_1080p.mp4"
