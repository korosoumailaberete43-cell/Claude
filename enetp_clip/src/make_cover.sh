#!/bin/bash
# Exporte la pochette (cover) : 1920x1080 (depuis le générique du clip) et 1080x1080 (mise en page dédiée)
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f out/_bg.png ] || ffmpeg -y -v error -i src/logo_enetp.jpg -vf \
 "scale=2880:2160:flags=lanczos,crop=2560:1440,gblur=sigma=70,eq=brightness=-0.68:saturation=2.0:contrast=0.95,gblur=sigma=22" \
 -frames:v 1 out/_bg.png

# --- 16/9 : une image du générique ---
ffmpeg -y -v error \
 -loop 1 -framerate 30 -i out/_bg.png \
 -loop 1 -framerate 30 -i src/logo_enetp.jpg \
 -filter_complex "
 [0:v]zoompan=z='min(zoom+0.00008,1.22)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':fps=30:s=1920x1080,
      vignette=PI/4.2,format=rgba[bg];
 [1:v]scale=660:-1:flags=lanczos,colorkey=0x000000:0.26:0.12,format=rgba[cover];
 [bg][cover]overlay=x=(W-w)/2:y=100[v1];
 [v1]ass=out/enetp_karaoke.ass:fontsdir=/usr/share/fonts,format=rgb24[vout]" \
 -map "[vout]" -ss 3.4 -frames:v 1 out/cover_ENETP_1920x1080.png

# --- 1/1 : mise en page carrée dédiée ---
cat > out/_cover_square.ass <<'ASS'
[Script Info]
ScriptType: v4.00+
WrapStyle: 2
ScaledBorderAndShadow: yes
PlayResX: 1080
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Big,Inter,48,&H00FFFFFF,&H00FFFFFF,&H00120C06,&H00000000,-1,0,0,0,100,100,5.0,0,1,3,2,5,40,40,40,1
Style: Sub,Inter,32,&H00C8E6FF,&H00C8E6FF,&H00120C06,&H00000000,0,0,0,0,100,100,1.0,0,1,3,1,5,40,40,40,1
Style: Tiny,Inter,22,&H00B0B0B0,&H00B0B0B0,&H00120C06,&H00000000,0,0,0,0,100,100,2.0,0,1,2,1,5,40,40,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:10.00,Big,,0,0,0,,{\pos(540,690)}E · N · E · T · P  —  K A B A L A
Dialogue: 0,0:00:00.00,0:00:10.00,Sub,,0,0,0,,{\pos(540,755)\i1}Qui Maîtrise Enseigne{\i0}
Dialogue: 0,0:00:00.00,0:00:10.00,Big,,0,0,0,,{\pos(540,855)\fs42\c&H003CE1FF&\fsp2}PITIÉ, MONSIEUR LE DIRECTEUR
Dialogue: 0,0:00:00.00,0:00:10.00,Tiny,,0,0,0,,{\pos(540,920)}Déclaration des étudiants de l'E.N.E.T.P — Kabala
ASS
ffmpeg -y -v error \
 -loop 1 -framerate 30 -i out/_bg.png \
 -loop 1 -framerate 30 -i src/logo_enetp.jpg \
 -filter_complex "
 [0:v]scale=1440:1440:flags=lanczos:force_original_aspect_ratio=increase,crop=1080:1080,
      vignette=PI/4.2,format=rgba[bg];
 [1:v]scale=540:-1:flags=lanczos,colorkey=0x000000:0.26:0.12,format=rgba[cover];
 [bg][cover]overlay=x=(W-w)/2:y=155[v1];
 [v1]ass=out/_cover_square.ass:fontsdir=/usr/share/fonts,format=rgb24[vout]" \
 -map "[vout]" -frames:v 1 out/cover_ENETP_1080x1080.png
echo "-> out/cover_ENETP_1920x1080.png / out/cover_ENETP_1080x1080.png"
