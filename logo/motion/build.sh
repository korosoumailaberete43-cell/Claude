#!/bin/sh
# Reconstruit un teaser : images (Chromium) → bande-son (numpy) → MP4 (ffmpeg).
#   ./build.sh            → paysage 1920x1080 (52 s)
#   ./build.sh vertical   → vertical 1080x1920 pour TikTok / WhatsApp (81 s)
# Prérequis : node + playwright, python3 + numpy + imageio-ffmpeg.
set -e
cd "$(dirname "$0")"
if [ "$1" = "vertical" ]; then
  PAGE=teaser_v; OUT=CivRebar_AI_Teaser_vertical_1080x1920; AUDIO=teaser_vertical_audio; Q="-crf 20 -maxrate 9M -bufsize 18M"; AB=192k
else
  PAGE=teaser; OUT=CivRebar_AI_Teaser_1080p; AUDIO=teaser_audio; Q="-crf 17"; AB=256k
fi
FRAMES=${FRAMES:-/tmp/civrebar_frames_$PAGE}
rm -rf "$FRAMES"
NODE_PATH=$(npm root -g) node render.js $PAGE.html frames "$FRAMES" 4
python3 sound.py $PAGE.cues.json out/$AUDIO.wav
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
"$FF" -y -loglevel error -framerate 30 -i "$FRAMES/f%05d.jpg" -i out/$AUDIO.wav \
  -c:v libx264 -preset slow $Q -pix_fmt yuv420p -profile:v high -c:a aac -b:a $AB -movflags +faststart -shortest \
  out/$OUT.mp4
rm -rf "$FRAMES"
echo "→ out/$OUT.mp4"
