#!/bin/sh
# Fabrique un épisode complet : voix déjà générée → images → son → MP4.
#   sh video/fabrique.sh corrige [dossier_images]
set -e
E=$1; ICI=$(cd "$(dirname "$0")" && pwd); IMG=${2:-$ICI/episodes/$E/frames}
cd "$ICI/.."
PAGE="episode.html?e=$E" node video/render.js "$IMG" 6
python3 video/mix.py "$IMG/cues.json" "episodes/$E"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())" 2>/dev/null || echo ffmpeg)
mkdir -p out
"$FF" -y -loglevel error -framerate 30 -i "$IMG/f%05d.jpg" -i "video/episodes/$E/audio.wav" \
  -c:v libx264 -preset slow -crf 20 -maxrate 6M -bufsize 12M -pix_fmt yuv420p -profile:v high \
  -af loudnorm=I=-14:TP=-1.5 -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "out/Tonton_$E.mp4"
echo "out/Tonton_$E.mp4"
