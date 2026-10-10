#!/bin/bash
# Rendu du clip paroles ENETP Kabala
set -euo pipefail
cd "$(dirname "$0")/.."
LOGO=src/logo_enetp.jpg
AUDIO="${1:?usage: render.sh <audio.mp3>}"
OUT=${2:-out/ENETP_Kabala_clip_paroles.mp4}
INTRO=3.5
COVER_END=12.39
ADUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$AUDIO")
TOTAL=$(python3 -c "print(round($INTRO+$ADUR+0.9,3))")
[ -n "${3:-}" ] && TOTAL=$3
VFADE=$(python3 -c "print(round($INTRO+$ADUR-0.2,3))")
AFADE=$(python3 -c "print(round($ADUR+$INTRO-1.0,3))")
echo "audio=$ADUR total=$TOTAL"

# 1. fond flou (une seule fois)
ffmpeg -y -v error -i "$LOGO" -vf \
 "scale=2880:2160:flags=lanczos,crop=2560:1440,gblur=sigma=70,eq=brightness=-0.68:saturation=2.0:contrast=0.95,gblur=sigma=22" \
 -frames:v 1 out/_bg.png

# 2. clip
ffmpeg -y -stats -v warning \
 -loop 1 -framerate 30 -i out/_bg.png \
 -loop 1 -framerate 30 -i "$LOGO" \
 -loop 1 -framerate 30 -i "$LOGO" \
 -i "$AUDIO" \
 -filter_complex "
 [0:v]zoompan=z='min(zoom+0.00008,1.22)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':fps=30:s=1920x1080,
      vignette=PI/4.2,format=rgba[bg];
 [3:a]adelay=3500|3500:all=1,afade=t=in:st=${INTRO}:d=0.8,afade=t=out:st=${AFADE}:d=1.0,asplit=2[aout][awav];
 [awav]showwaves=s=1920x150:mode=cline:rate=30:scale=sqrt:colors=0xFFC83C@0.9|0x7FD8FF@0.9,
      format=rgba,colorchannelmixer=aa=0.5,pad=1920:1080:0:925:0x00000000[wav];
 [bg][wav]overlay=0:0:format=auto[bgw];
 [1:v]scale=660:-1:flags=lanczos,colorkey=0x000000:0.26:0.12,format=rgba,
      fade=t=in:st=0.25:d=1.1:alpha=1,fade=t=out:st=$(python3 -c "print(round($COVER_END-0.9,2))"):d=0.9:alpha=1[cover];
 [bgw][cover]overlay=x=(W-w)/2:y=100:enable='lte(t,${COVER_END})'[v1];
 [2:v]scale=150:-1:flags=lanczos,colorkey=0x000000:0.26:0.12,format=rgba,
      fade=t=in:st=$(python3 -c "print(round($COVER_END-0.2,2))"):d=1.0:alpha=1[mark];
 [v1][mark]overlay=x=84:y=24:enable='gte(t,$(python3 -c "print(round($COVER_END-0.3,2))"))'[v2];
 [v2]ass=out/enetp_karaoke.ass:fontsdir=/usr/share/fonts,
     fade=t=in:st=0:d=0.8,fade=t=out:st=${VFADE}:d=0.8,format=yuv420p[vout]
 " -map "[vout]" -map "[aout]" \
 -c:v libx264 -preset ${PRESET:-medium} -crf ${CRF:-19} -r 30 -pix_fmt yuv420p \
 -c:a aac -b:a 256k -ar 48000 -ac 2 \
 -movflags +faststart -t "$TOTAL" "$OUT"
echo "-> $OUT"
