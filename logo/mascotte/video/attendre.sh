#!/bin/sh
# Attend qu'un MP4 soit complet : ffmpeg doit pouvoir lire sa durée
# (l'atome moov est écrit en dernier, donc un fichier volumineux
#  n'est pas forcément un fichier fini).
# usage : sh video/attendre.sh out/Tonton_h29_signature.mp4
f="$1"
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
while :; do
  if [ -f "$f" ] && "$FF" -v error -i "$f" -f null - >/dev/null 2>&1; then
    echo "pret $f $("$FF" -i "$f" 2>&1 | grep -oP 'Duration: \K[^,]+')"
    exit 0
  fi
  sleep 20
done
