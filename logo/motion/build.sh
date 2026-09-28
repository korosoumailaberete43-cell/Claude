#!/bin/sh
# Reconstruit une vidéo : images (Chromium) → bande-son (numpy) → MP4 (ffmpeg).
#   ./build.sh              → teaser paysage 1920x1080 (52 s)
#   ./build.sh vertical     → teaser vertical 1080x1920 (81 s)
#   ./build.sh manifeste    → « Manifeste », typographie sur fond clair (30 s)
#   ./build.sh pov          → « POV », format TikTok (32 s)
#   ./build.sh cage3d       → « Construction 3D » (30 s)
# Prérequis : node + playwright, python3 + numpy + imageio-ffmpeg.
set -e
cd "$(dirname "$0")"
case "$1" in
  "")        PAGE=teaser;    OUT=CivRebar_AI_Teaser_1080p ;;
  vertical)  PAGE=teaser_v;  OUT=CivRebar_AI_Teaser_vertical_1080x1920 ;;
  manifeste) PAGE=manifeste; OUT=CivRebar_AI_Manifeste_vertical ;;
  pov)       PAGE=pov;       OUT=CivRebar_AI_POV_vertical ;;
  cage3d)    PAGE=cage3d;    OUT=CivRebar_AI_Construction3D_vertical ;;
  *) echo "vidéo inconnue : $1"; exit 1 ;;
esac
if [ "$PAGE" = teaser ]; then Q="-crf 17"; AB=256k; else Q="-crf 20 -maxrate 9M -bufsize 18M"; AB=192k; fi
AUDIO=out/${PAGE}_audio.wav
[ "$PAGE" = teaser ] && AUDIO=out/teaser_audio.wav
[ "$PAGE" = teaser_v ] && AUDIO=out/teaser_vertical_audio.wav
FRAMES=${FRAMES:-/tmp/civrebar_frames_$PAGE}
rm -rf "$FRAMES"
NODE_PATH=$(npm root -g) node render.js $PAGE.html frames "$FRAMES" 4
python3 sound.py $PAGE.cues.json $AUDIO
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
"$FF" -y -loglevel error -framerate 30 -i "$FRAMES/f%05d.jpg" -i $AUDIO \
  -c:v libx264 -preset slow $Q -pix_fmt yuv420p -profile:v high -c:a aac -b:a $AB -movflags +faststart -shortest \
  out/$OUT.mp4
rm -rf "$FRAMES"
echo "→ out/$OUT.mp4"
