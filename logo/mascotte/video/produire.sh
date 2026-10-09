#!/bin/sh
# Fabrique toutes les vidéos d'épisode qui manquent dans out/.
#   sh video/produire.sh              → tous les épisodes
#   sh video/produire.sh h15 h16      → seulement ceux-là
ICI=$(cd "$(dirname "$0")" && pwd)
cd "$ICI/.." || exit 1
TMP="${TMP_IMAGES:-$ICI/.images}"
mkdir -p "$TMP" out
for d in video/episodes/h*/; do
  e=$(basename "$d")
  [ -f "$d/voix.json" ] || continue
  [ -f "out/Tonton_$e.mp4" ] && continue
  if [ $# -gt 0 ]; then
    garde=0
    for a in "$@"; do case "$e" in "$a"*) garde=1;; esac; done
    [ $garde = 1 ] || continue
  fi
  if sh video/fabrique.sh "$e" "$TMP/$e" > "$TMP/$e.log" 2>&1; then
    echo "OK $e $(stat -c%s "out/Tonton_$e.mp4")"
    rm -rf "$TMP/$e"
  else
    echo "ECHEC $e"; tail -3 "$TMP/$e.log"
  fi
done
echo TOUT_FINI
