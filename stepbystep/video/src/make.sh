#!/usr/bin/env bash
# Rend les vidéos Step by Step Academy : node + Chromium (Playwright) pour l'image, numpy pour le son.
# usage : ./make.sh [intro_generique|intro_titre_exemple|outro ...]   (sans argument : les trois)
set -euo pipefail
cd "$(dirname "$0")"
export FFMPEG="${FFMPEG:-$(python3 -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')}"
export NODE_PATH="$(npm root -g)"
OUT=../livrables; TMP=../tmp; mkdir -p "$OUT" "$TMP"
declare -A NOMS=([intro_generique]=StepByStep_Intro_generique [intro_titre_exemple]=StepByStep_Intro_titre_exemple [outro]=StepByStep_Outro_ecran_de_fin)
for v in "${@:-intro_generique intro_titre_exemple outro}"; do for v in $v; do
  python3 build_html.py "$v" "${CFG_JSON:-"{}"}" >/dev/null
  node render.js "../build/$v.html" "$TMP/$v" 30 4 4
  python3 audio.py "$v" "$TMP/$v.wav" >/dev/null
  "$FFMPEG" -y -loglevel error -f concat -safe 0 -i "$TMP/$v.txt" -c copy "$TMP/$v.mkv"
  # grain très léger (anti-bandes dans les dégradés sombres), H.264 haute qualité, AAC 320k
  enc=(-vf "noise=alls=3:allf=t,format=yuv420p" -c:v libx264 -preset slow -crf 14 -profile:v high -tune film
       -color_primaries bt709 -color_trc bt709 -colorspace bt709 -r 30 -movflags +faststart)
  "$FFMPEG" -y -loglevel error -i "$TMP/$v.mkv" -i "$TMP/$v.wav" -map 0:v -map 1:a "${enc[@]}" -c:a aac -b:a 320k -shortest "$OUT/${NOMS[$v]}.mp4"
  "$FFMPEG" -y -loglevel error -i "$TMP/$v.mkv" "${enc[@]}" -an "$OUT/${NOMS[$v]}_sans_son.mp4"
  cp "$TMP/$v.wav" "$OUT/${NOMS[$v]}_son_seul.wav"
  rm -f "$TMP/$v".part*.mkv "$TMP/$v.txt"
  echo "✔ $v"
done; done
