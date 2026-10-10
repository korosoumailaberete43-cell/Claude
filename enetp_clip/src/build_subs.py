# -*- coding: utf-8 -*-
"""Construit depuis out/align.json :
   - enetp_karaoke.ass  (karaoké mot à mot pour la vidéo, décalé de INTRO s)
   - enetp_paroles_video.srt / enetp_paroles_audio.srt
   - enetp_paroles.lrc  (pour lecteurs audio)
   - paroles_minutees.txt
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(os.path.dirname(HERE), "out")
INTRO = float(sys.argv[1]) if len(sys.argv) > 1 else 5.0

TITRE      = "PITIÉ, MONSIEUR LE DIRECTEUR"
SOUS_TITRE = "Déclaration des étudiants de l'E.N.E.T.P — Kabala"
ECOLE      = "E · N · E · T · P   —   K A B A L A"
DEVISE     = "Qui Maîtrise Enseigne"

MAXCHARS = 44        # longueur max d'une ligne affichée
LEAD     = 0.45      # apparition de la ligne avant le 1er mot
TAIL_MAX = 0.80      # maintien après le dernier mot
WORD_MAX = 1.30      # durée max du remplissage d'un mot

d = json.load(open(os.path.join(OUT, "align.json"), encoding="utf-8"))
lines = d["lines"]
DUR = d["duration"]
COVER_END = INTRO + lines[0]["start"] - 0.55   # la pochette reste pendant l'intro musicale

# ---------- nettoyage des durées ----------
for li, l in enumerate(lines):
    ws = l["words"]
    for i, w in enumerate(ws):
        nxt = ws[i+1]["start"] if i+1 < len(ws) else (
              lines[li+1]["words"][0]["start"] if li+1 < len(lines) else DUR)
        w["end"] = max(w["start"] + 0.12, min(w["end"], nxt, w["start"] + WORD_MAX))
    l["start"] = ws[0]["start"]
    l["end"]   = ws[-1]["end"]

def ts_ass(t):
    t = max(t, 0); h = int(t//3600); m = int(t%3600//60); s = t%60
    return f"{h:d}:{m:02d}:{s:05.2f}"

def ts_srt(t):
    t = max(t, 0); h = int(t//3600); m = int(t%3600//60); s = int(t%60); ms = int(round((t-int(t))*1000))
    if ms == 1000: s += 1; ms = 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def wrap_words(words, maxchars):
    """-> liste de rangées, chaque rangée = liste d'index de mots"""
    rows, cur, n = [], [], 0
    for i, w in enumerate(words):
        add = len(w["w"]) + (1 if cur else 0)
        if cur and n + add > maxchars:
            rows.append(cur); cur, n = [], 0
            add = len(w["w"])
        cur.append(i); n += add
    if cur: rows.append(cur)
    return rows

def display_words(line):
    """mots d'affichage (texte original) appariés aux mots alignés"""
    import re
    raw = line["text"].replace("’", "'")
    toks = raw.split()
    al = line["words"]
    # appariement positionnel : on redécoupe le texte original en autant de blocs
    # que de mots alignés, en gardant la ponctuation collée au mot précédent.
    def strip_tok(t):
        return re.sub(r"^[«»\"\(…\.,;:!\?]+|[«»\"\)…\.,;:!\?]+$", "", t)
    out, ai = [], 0
    for t in toks:
        core = strip_tok(t)
        if core == "":                       # ponctuation isolée -> collée au précédent
            if out: out[-1]["w"] += " " + t
            continue
        out.append({"w": t, "al": al[ai] if ai < len(al) else None})
        ai += 1
    # si décalage, on répartit linéairement
    n = len(out)
    for k, o in enumerate(out):
        if o["al"] is None:
            o["al"] = al[min(int(k*len(al)/max(n,1)), len(al)-1)]
    return out

# ---------- ASS ----------
HDR = f"""[Script Info]
Title: ENETP Kabala — {TITRE}
ScriptType: v4.00+
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Karaoke,Inter,64,&H003CE1FF,&H64FFFFFF,&H00120C06,&HA0000000,-1,0,0,0,100,100,0.6,0,1,4,2,5,80,80,60,1
Style: Next,Inter,38,&H8CFFFFFF,&H8CFFFFFF,&H00120C06,&H00000000,0,0,0,0,100,100,0.4,0,1,3,1,5,80,80,60,1
Style: Section,Inter,30,&H00E8E8E8,&H00E8E8E8,&H00120C06,&H00000000,-1,0,0,0,100,100,4.0,0,1,3,1,9,60,70,50,1
Style: Mark,Inter,30,&H00F0F0F0,&H00F0F0F0,&H00120C06,&H00000000,-1,0,0,0,100,100,2.5,0,1,3,1,7,250,60,50,1
Style: Big,Inter,78,&H00FFFFFF,&H00FFFFFF,&H00120C06,&H00000000,-1,0,0,0,100,100,8.0,0,1,4,2,5,80,80,60,1
Style: Sub,Inter,40,&H00C8E6FF,&H00C8E6FF,&H00120C06,&H00000000,0,0,0,0,100,100,1.5,0,1,3,1,5,80,80,60,1
Style: Tiny,Inter,28,&H00B0B0B0,&H00B0B0B0,&H00120C06,&H00000000,0,0,0,0,100,100,3.0,0,1,2,1,5,80,80,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
def E(start, end, style, text, layer=0):
    ev.append(f"Dialogue: {layer},{ts_ass(start)},{ts_ass(end)},{style},,0,0,0,,{text}")

# --- générique d'ouverture (cover) ---
E(0.60, COVER_END, "Big",  r"{\pos(960,700)\fad(700,900)\fscx92\fscy92}" + ECOLE)
E(1.30, COVER_END, "Sub",  r"{\pos(960,775)\fad(700,900)\i1}" + DEVISE + r"{\i0}")
E(2.10, COVER_END, "Big",  r"{\pos(960,880)\fad(600,900)\fs52\c&H003CE1FF&\fsp3}" + TITRE)
E(2.70, COVER_END, "Tiny", r"{\pos(960,950)\fad(600,900)}" + SOUS_TITRE)

# --- filigrane pendant le morceau ---
E(lines[0]["start"]-0.2, DUR, "Mark", r"{\pos(250,78)\fad(800,800)\an4}ENETP · KABALA")

# --- paroles ---
srt_v, srt_a, lrc, txt = [], [], [], []
prev_section = None
for li, l in enumerate(lines):
    nxt_start = lines[li+1]["start"] if li+1 < len(lines) else DUR
    st = max(l["start"] - LEAD, (lines[li-1]["end"] if li else 0) - 0.05, 0)
    en = min(l["end"] + TAIL_MAX, nxt_start - 0.02 if li+1 < len(lines) else DUR)
    en = max(en, l["end"] + 0.12)
    dw = display_words(l)
    rows = wrap_words([{"w": o["w"]} for o in dw], MAXCHARS)

    parts = []
    cursor = st
    for ri, row in enumerate(rows):
        if ri: parts.append(r"\N")
        for k, idx in enumerate(row):
            o = dw[idx]
            ws, we = o["al"]["start"], o["al"]["end"]
            gap = max(0, int(round((ws - cursor)*100)))
            dur = max(8, int(round((we - ws)*100)))
            pre = " " if (k and ri == 0) or (k and ri) else ""
            if k:  # espace avant le mot, rempli pendant le silence
                parts.append(r"{\k%d} " % gap)
            elif gap:
                parts.append(r"{\k%d}" % gap)
            parts.append(r"{\kf%d}%s" % (dur, o["w"]))
            cursor = we
    body = "".join(parts)
    E(st, en, "Karaoke", r"{\pos(960,648)\fad(180,220)}" + body, layer=2)

    # ligne suivante en aperçu (grisée)
    if li+1 < len(lines) and lines[li+1]["start"] - l["end"] < 6:
        n = lines[li+1]
        nrows = wrap_words([{"w": w["w"]} for w in display_words(n)], MAXCHARS+8)
        ntext = r"\N".join(" ".join(display_words(n)[i]["w"] for i in row) for row in nrows)
        E(st, min(en, n["start"]-0.05) if n["start"]-0.05 > st else en, "Next",
          r"{\pos(960,800)\fad(200,150)}" + ntext, layer=1)

    # étiquette de section
    if l["section"] != prev_section:
        sec_end = l["start"] + 4.0
        for j in range(li+1, len(lines)):
            if lines[j]["section"] != l["section"]:
                sec_end = min(sec_end, lines[j]["start"]); break
        E(max(l["start"]-LEAD, 0), sec_end, "Section",
          r"{\pos(1840,80)\fad(400,400)\an6}" + l["section"].upper())
        prev_section = l["section"]

        # pause instrumentale
    if li+1 < len(lines) and lines[li+1]["start"] - l["end"] > 5.0:
        g0, g1 = en + 0.2, lines[li+1]["start"] - 0.8
        if g1 - g0 > 1.2:
            E(g0, g1, "Sub", r"{\pos(960,660)\fad(600,600)\fnDejaVu Sans\fs46\alpha&H60&}♪   ♪   ♪")

    srt_v.append((l["start"], en if li+1 < len(lines) else l["end"]+1.0, l["text"]))
    srt_a.append((l["start"], en if li+1 < len(lines) else l["end"]+1.0, l["text"]))
    lrc.append((l["start"], l["text"]))
    txt.append(f'[{int(l["start"]//60):02d}:{l["start"]%60:05.2f}] {l["text"]}')

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "enetp_karaoke.ass"), "w", encoding="utf-8").write(
    HDR + "\n".join(f"Dialogue: {e.split('Dialogue: ')[1]}" if False else e for e in
                    [x.replace("Dialogue: 0,", "Dialogue: 0,") for x in
                     [f"{l}" for l in [e for e in ev]]]) + "\n")

def shift_ass(path, off):
    pass

# décalage de l'intro appliqué aux événements de paroles : on régénère proprement
def write_ass(path, offset):
    out = [HDR]
    for e in ev:
        head, rest = e.split(",", 1)
        start, rest2 = rest.split(",", 1)
        end, rest3 = rest2.split(",", 1)
        style = rest3.split(",", 1)[0]
        def p(t):
            h, m, s = t.split(":"); return int(h)*3600+int(m)*60+float(s)
        o = 0.0 if style in ("Big", "Sub", "Tiny") else offset
        if style in ("Big", "Sub", "Tiny"):
            o = 0.0
        out.append(f"{head},{ts_ass(p(start)+o)},{ts_ass(p(end)+o)},{rest3}")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")

write_ass(os.path.join(OUT, "enetp_karaoke.ass"), INTRO)

def write_srt(path, items, off):
    with open(path, "w", encoding="utf-8") as f:
        for i, (s, e, t) in enumerate(items, 1):
            f.write(f"{i}\n{ts_srt(s+off)} --> {ts_srt(e+off)}\n{t}\n\n")

write_srt(os.path.join(OUT, "enetp_paroles_video.srt"), srt_v, INTRO)
write_srt(os.path.join(OUT, "enetp_paroles_audio.srt"), srt_a, 0.0)
with open(os.path.join(OUT, "enetp_paroles.lrc"), "w", encoding="utf-8") as f:
    f.write(f"[ti:{TITRE}]\n[ar:Étudiants de l'ENETP Kabala]\n[al:ENETP Kabala]\n\n")
    for s, t in lrc:
        f.write(f"[{int(s//60):02d}:{s%60:05.2f}]{t}\n")
open(os.path.join(OUT, "paroles_minutees.txt"), "w", encoding="utf-8").write(
    f"{TITRE}\n{SOUS_TITRE}\n\nMinutage sur le fichier audio d'origine (mp3).\n\n" + "\n".join(txt) + "\n")
print("OK :", len(ev), "événements ASS,", len(srt_v), "lignes")
