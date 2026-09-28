"""Logo Step by Step Academy remasterisé : même composition que l'original (repère 1280 × 1280),
redessiné en vectoriel propre. Toutes les positions viennent de mesures sur l'image d'origine."""
import math
import pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"

# ---------------------------------------------------------------- couleurs d'origine
NOIR = "#111111"
OR = "#F5C518"        # or « Excellence » (valeur officielle de la 1re charte)
VERT = "#5DB12E"      # vert de la coche, relevé sur l'original et aplati
BLANC = "#FFFFFF"

# ---------------------------------------------------------------- mesures (px de l'original)
MARCHES = [  # (x gauche, y haut) ; bord droit 1027, hauteur 67
    (731, 333), (642, 422), (536, 514), (407, 603), (260, 690)]
MARCHE_DROITE, MARCHE_H = 1027, 67

# lettres : (caractère, x0, y0, largeur, hauteur) mesurées par composantes connexes
STEP1 = [("S", 190, 781, 85, 129), ("t", 283, 797, 52, 113), ("e", 344, 812, 89, 99), ("p", 449, 812, 93, 132)]
STEP2 = [("S", 735, 781, 85, 129), ("t", 828, 797, 52, 113), ("e", 889, 812, 88, 99), ("p", 994, 813, 92, 131)]
BY = [("B", 597, 824, 38, 59), ("y", 639, 840, 39, 57)]
ACADEMY = [("A", 356, 954, 76, 87), ("C", 435, 954, 89, 87), ("A", 525, 954, 76, 87), ("D", 606, 954, 71, 87),
           ("E", 686, 954, 60, 87), ("M", 754, 954, 90, 87), ("Y", 847, 954, 72, 87)]

_fonts = {}


def _font(f):
    if f not in _fonts:
        _fonts[f] = TTFont(FONTS / f)
    return _fonts[f]


def glyph_fit(fontfile, letters, ref_char, baseline_char_bottom=None):
    """Place chaque glyphe pour que sa boîte d'encre coïncide avec la lettre d'origine.
    Échelle unique par mot (hauteur de la lettre de référence), position x par lettre (centre),
    ligne de base commune (bas de la lettre de référence)."""
    f = _font(fontfile)
    gs, cmap = f.getGlyphSet(), f.getBestCmap()

    def bounds(ch):
        bp = BoundsPen(gs)
        gs[cmap[ord(ch)]].draw(bp)
        return bp.bounds
    ref = next(l for l in letters if l[0] == ref_char)
    rb = bounds(ref_char)
    s = ref[4] / (rb[3] - rb[1])                   # échelle : hauteur d'encre
    base = ref[2] + ref[4] + rb[1] * s             # ligne de base (y SVG)
    out = []
    for ch, x0, y0, w, h in letters:
        b = bounds(ch)
        cx_font = (b[0] + b[2]) / 2
        tx = x0 + w / 2 - cx_font * s
        pen = SVGPathPen(gs)
        gs[cmap[ord(ch)]].draw(pen)
        out.append(f'<path transform="translate({tx:.2f} {base:.2f}) scale({s:.5f} {-s:.5f})" d="{pen.getCommands()}"/>')
    return "".join(out)


def toque(fill, trou):
    """Toque redessinée : plateau, calotte, cordon (creux) et gland. `trou` = couleur du fond
    n'est jamais utilisée : les creux sont de vrais vides (masque), le logo reste transparent."""
    plateau = "M145 300.5 L330 137 Q334 134 339 133.4 L572.7 93.3 L411.7 305 Z"
    calotte = ("M289 310.5 L413.5 312.3 L491 213 L529.5 268.5 "
               "C518 305 495 346 465 364 C439 381 410 389 387 389 C352 388 325 381 307.5 374 "
               "C303 354 296 331 289 310.5 Z")
    # cordon et bouton : creux véritables (règle evenodd), le logo reste transparent
    x1, y1, x2, y2, w = 363, 198, 243.5, 301, 2.6
    L = math.hypot(x2 - x1, y2 - y1); nx, ny = -(y2 - y1) / L * w, (x2 - x1) / L * w
    cordon = (f"M{x1 + nx:.2f} {y1 + ny:.2f} L{x2 + nx:.2f} {y2 + ny:.2f} "
              f"L{x2 - nx:.2f} {y2 - ny:.2f} L{x1 - nx:.2f} {y1 - ny:.2f} Z")
    cx, cy, rx, ry, t = 361.5, 195.5, 15.5, 10.5, math.radians(-18)
    pts = [(cx + rx * math.cos(k) * math.cos(t) - ry * math.sin(k) * math.sin(t),
            cy + rx * math.cos(k) * math.sin(t) + ry * math.sin(k) * math.cos(t)) for k in [i * math.pi / 24 for i in range(48)]]
    bouton = "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + " Z"
    return f"""<g fill="{fill}">
  <path d="{calotte}"/>
  <path d="{plateau} {cordon} {bouton}" fill-rule="evenodd"/>
  <path d="M229.5 302 L262 389 Q268 399 278 396 Q289 392 286 381 L249 303" fill="none" stroke="{fill}" stroke-width="4.6" stroke-linejoin="round" stroke-linecap="round"/>
</g>"""


def coche(vert):
    return f"""<g>
  <circle cx="889.5" cy="277.5" r="45" fill="none" stroke="{vert}" stroke-width="9.5"/>
  <path d="M851 284 Q855 276 863 277 L876.5 293 Q902 256 940 233 Q906 266 882 307 Q877 314 870 309 Z" fill="{vert}"/>
</g>"""


def fil(or_, fin):
    """Fil doré : part de sous la toque, tourne, redescend le long des marches et s'estompe."""
    return f"""<defs><linearGradient id="g_fil" gradientUnits="userSpaceOnUse" x1="0" y1="400" x2="0" y2="790">
  <stop offset="0" stop-color="{or_}"/><stop offset=".55" stop-color="{or_}" stop-opacity=".55"/>
  <stop offset="1" stop-color="{or_}" stop-opacity="0"/></linearGradient></defs>
<path d="M503 192.5 H1010 A70 70 0 0 1 1080 262.5 V420" fill="none" stroke="{or_}" stroke-width="13"/>
<path d="M1080 419 V790" fill="none" stroke="url(#g_fil)" stroke-width="13"/>
<path d="M1071 770 H1087 A8 8 0 0 1 1071 770 Z" fill="{fin}"/>"""


def tilde(cx, cy, col):
    return (f'<path d="M{cx - 19} {cy + 3} C{cx - 14} {cy - 7} {cx - 6} {cy - 7} {cx} {cy} C{cx + 6} {cy + 7} {cx + 14} {cy + 7} {cx + 19} {cy - 3}" '
            f'fill="none" stroke="{col}" stroke-width="3.6" stroke-linecap="round"/>')


def livre(col):
    """Livre ouvert : deux pages légèrement galbées, symétriques autour de x = 638."""
    g = "M634 1082 C620 1077 603 1075 590 1078 C589 1098 587 1116 584 1133 C600 1128 618 1129 633 1136 Z"
    d = "M642 1082 C656 1077 673 1075 686 1078 C687 1098 689 1116 692 1133 C676 1128 658 1129 643 1136 Z"
    return f'<path d="{g}" fill="{col}"/><path d="{d}" fill="{col}"/>'


def logo(fond=None, texte=BLANC, or_=OR, vert=VERT, toque_col=None, detail=True):
    """detail=False retire tildes et livre (version épurée optionnelle)."""
    toque_col = toque_col or texte
    marches = "".join(f'<rect x="{x}" y="{y}" width="{MARCHE_DROITE - x}" height="{MARCHE_H}" fill="{or_}"/>' for x, y in MARCHES)
    # polices identifiées par superposition sur l'original : Quicksand SemiBold + Comfortaa
    bold = "quicksand-latin-600-normal.woff2"
    txt = (glyph_fit(bold, STEP1, "S") + glyph_fit(bold, STEP2, "S")
           + glyph_fit("comfortaa-latin-400-normal.woff2", BY, "B")
           + glyph_fit("comfortaa-latin-300-normal.woff2", ACADEMY, "D"))
    extras = (tilde(210, 1008, texte) + tilde(1065, 1008, texte) + livre(texte)) if detail else ""
    bg = f'<rect width="1280" height="1280" fill="{fond}"/>' if fond else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 1280">{bg}
{fil(or_, texte)}
{marches}
{coche(vert)}
{toque(toque_col, fond)}
<g fill="{texte}">{txt}</g>
{extras}
</svg>"""


if __name__ == "__main__":
    import sys
    out = ROOT / "out"
    (out / "logo_remaster.svg").write_text(logo(fond="#000000"))
    (out / "logo_remaster_clair.svg").write_text(logo(fond="#FAF7F0", texte=NOIR))
    print("ok")
