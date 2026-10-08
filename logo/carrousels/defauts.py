"""Dessins de la série « Trouve l'erreur » : chaque défaut classique de ferraillage,
en version fautive et en version corrigée, plus un schéma « pourquoi » quand il aide.

Chaque scénario : draw(t, ok) → corps SVG (repère 1000 x 420), zone à entourer, légende de la
réponse, et éventuellement why(t) → schéma explicatif. Les règles restent énoncées comme des
principes : les valeurs réelles se calculent selon la norme et le projet.
"""
from brand import CUIVRE, SIGNAL

ALERTE = "#D64545"  # rouge fonctionnel, réservé aux erreurs de la série


# ------------------------------------------------------------ primitives
def L(x1, y1, x2, y2, c, w=3, extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" {extra}/>'


def P(pts, c, w=10, close=False):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts) + (" Z" if close else "")
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'


def R(x, y, w, h, c, sw=3, fill="none", op=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{c}" stroke-width="{sw}" opacity="{op}"/>'


def C(cx, cy, r, c):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'


def T(x, y, s, c, size=26, anchor="middle", font="Mono", weight=400):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-weight="{weight}" font-size="{size}" fill="{c}">{s}</text>'


def hatch(x, y, w, h, c, step=16):
    lines = "".join(L(x + k, y + h, x + k + h, y, c, 1.2) for k in range(-h, w, step))
    return f'<g><clipPath id="h{x}{y}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#h{x}{y})" opacity=".55">{lines}</g>{R(x, y, w, h, c, 2)}</g>'


def support(x, y, c):
    return f'<path d="M{x} {y} L{x - 30} {y + 36} L{x + 30} {y + 36} Z" fill="{c}"/>'


def dim_h(x1, x2, y, s, t):
    m = t["muted"]
    return (L(x1, y, x2, y, m, 2) + L(x1 - 6, y + 8, x1 + 6, y - 8, m, 2) + L(x2 - 6, y + 8, x2 + 6, y - 8, m, 2)
            + R((x1 + x2) / 2 - len(s) * 9, y - 20, len(s) * 18, 34, t["bg"], 0, t["bg"]) + T((x1 + x2) / 2, y + 9, s, t["ink"], 26))


def dim_v(x, y1, y2, s, t, side=1):
    m = t["muted"]
    return (L(x, y1, x, y2, m, 2) + L(x - 8, y1 + 6, x + 8, y1 - 6, m, 2) + L(x - 8, y2 + 6, x + 8, y2 - 6, m, 2)
            + T(x + side * 14, (y1 + y2) / 2 + 9, s, t["ink"], 24, "start" if side > 0 else "end"))


def arrows_down(xs, y, c, h=40):
    return "".join(L(x, y - h, x, y, c, 3) + f'<path d="M{x - 8} {y - 12} L{x} {y} L{x + 8} {y - 12}" fill="none" stroke="{c}" stroke-width="3"/>' for x in xs)


def arrows_up(xs, y, c, h=40):
    return "".join(L(x, y + h, x, y, c, 3) + f'<path d="M{x - 8} {y + 12} L{x} {y} L{x + 8} {y + 12}" fill="none" stroke="{c}" stroke-width="3"/>' for x in xs)


def stirrups(x0, x1, y0, y1, step, c):
    out, x = "", x0
    while x <= x1:
        out += L(x, y0, x, y1, c, 3, 'opacity=".85"')
        x += step
    return out


# ------------------------------------------------------------ scénarios
def s_barres_haut(t, ok):
    m, ink = t["muted"], t["ink"]
    big, small = (238, 132) if ok else (132, 238)
    b = R(40, 110, 920, 150, m) + stirrups(64, 940, 118, 252, 36, ink)
    b += P([(56, big - 30 if big > 180 else big + 30), (56, big), (944, big), (944, big - 30 if big > 180 else big + 30)], CUIVRE, 13)
    b += P([(56, small - 24 if small > 180 else small + 24), (56, small), (944, small), (944, small - 24 if small > 180 else small + 24)], CUIVRE, 6)
    b += support(90, 260, m) + support(910, 260, m)
    b += T(500, big + (44 if big > 180 else -24), "3 HA20", t["cu_s"], 26) + T(500, small + (44 if small > 180 else -24), "2 HA14", t["cu_s"], 24)
    b += dim_h(40, 960, 370, "L = 5,40 m", t)
    return b


def w_moment_pos(t):
    m, si = t["muted"], t["si"]
    return (L(60, 120, 940, 120, m, 4) + support(60, 120, m) + support(940, 120, m)
            + f'<path d="M60 120 Q500 420 940 120" fill="{si}" opacity=".16"/><path d="M60 120 Q500 420 940 120" fill="none" stroke="{si}" stroke-width="5"/>'
            + T(500, 300, "M max", si, 28) + T(500, 90, "charge répartie", m, 22) + arrows_down(range(120, 900, 80), 112, m, 30)
            + T(500, 400, "le bas de la poutre est TENDU", t["ink"], 26, weight=500))


def s_console(t, ok):
    m, ink = t["muted"], t["ink"]
    top, bot = 176, 244
    main_y, sec_y = (top, bot) if ok else (bot, top)
    b = hatch(40, 40, 100, 360, m) + R(140, 160, 780, 100, m) + stirrups(170, 900, 166, 254, 40, ink)
    anchor = [(80, main_y + (120 if main_y == top else -120)), (80, main_y), (905, main_y), (905, main_y + (30 if main_y == top else -30))]
    b += P(anchor, CUIVRE, 13)
    b += P([(110, sec_y), (905, sec_y)], CUIVRE, 6)
    b += arrows_down(range(260, 900, 110), 150, m, 36)
    b += T(90, 430, "MUR", m, 22)
    if not ok:
        b += T(620, main_y + 44, "armatures principales", t["cu_s"], 24)
    b += dim_h(140, 920, 330, "porte-à-faux 1,80 m", t)
    return b


def w_console(t):
    m, si = t["muted"], t["si"]
    return (hatch(40, 60, 100, 300, m) + L(140, 200, 920, 200, m, 3, 'stroke-dasharray="10 8"')
            + f'<path d="M140 200 Q600 215 920 300" fill="none" stroke="{si}" stroke-width="6"/>'
            + arrows_down(range(260, 900, 110), 170, m, 36)
            + T(560, 120, "← traction en HAUT →", si, 28, weight=500) + T(560, 390, "la console plonge : c'est le dessus qui s'allonge", t["ink"], 24))


def s_enrobage(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 380, 30, 240, 380
    c = 36 if ok else 0
    b = R(x0, y0, w, h, m, 4)
    b += R(x0 + c, y0 + c, w - 2 * c, h - 2 * c, ink, 5)
    r = 15
    for cx in (x0 + c + r + 6, x0 + w / 2, x0 + w - c - r - 6):
        b += C(cx, y0 + h - c - r - 6, r + 2, CUIVRE)
    for cx in (x0 + c + r + 2, x0 + w - c - r - 2):
        b += C(cx, y0 + c + r + 2, r - 3, CUIVRE)
    if ok:
        b += dim_v(x0 + w + 40, y0 + h - c, y0 + h, "c = enrobage", t)
    else:
        b += T(x0 + w + 30, y0 + h - 10, "c = 0", t["ink"], 26, "start")
    b += T(x0 - 30, y0 + h / 2, "COUPE", m, 22, "end")
    return b


def s_crochets(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 360, 30, 280, 380
    c = 30
    ax, ay = x0 + c, y0 + c
    b = R(x0, y0, w, h, m, 4)
    if ok:
        # cadre fermé, les deux extrémités repliées à 135° vers le cœur du béton
        b += P([(ax, ay), (x0 + w - c, ay), (x0 + w - c, y0 + h - c), (ax, y0 + h - c)], ink, 7, close=True)
        b += P([(ax + 8, ay), (ax + 72, ay + 64)], ink, 7) + P([(ax, ay + 8), (ax + 64, ay + 72)], ink, 7)
        b += T(x0 + w + 30, ay + 70, "crochets à 135°", t["ink"], 24, "start")
    else:
        b += P([(ax + 40, ay), (x0 + w - c, ay), (x0 + w - c, y0 + h - c), (ax, y0 + h - c), (ax, ay + 40)], ink, 7)
    for cx, cy in ((ax + 20, ay + 20), (x0 + w - c - 20, ay + 20), (ax + 20, y0 + h - c - 20), (x0 + w - c - 20, y0 + h - c - 20), (x0 + w / 2, y0 + h - c - 20)):
        b += C(cx, cy, 15, CUIVRE)
    b += T(x0 - 30, y0 + h / 2, "COUPE", m, 22, "end")
    return b


def s_recouvrement(t, ok):
    m = t["muted"]
    a, bb = (300, 700) if ok else (450, 550)
    b = R(40, 140, 920, 140, m)
    b += P([(60, 200), (bb, 200)], CUIVRE, 11) + P([(a, 222), (940, 222)], CUIVRE, 11)
    b += dim_h(a, bb, 330, "ls ≈ 50 Ø" if ok else "10 cm", t)
    b += T(160, 125, "HA16", t["cu_s"], 24) + T(840, 125, "HA16", t["cu_s"], 24)
    return b


def s_attentes(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(80, 200, 840, 50, m) + R(420, 250, 160, 160, m)
    for y in range(270, 410, 36):
        b += L(432, y, 568, y, ink, 3, 'opacity=".85"')
    top = 40 if ok else 200
    for x in (445, 555):
        b += P([(x, 410), (x, top)], CUIVRE, 11)
    b += T(700, 232, "DALLE / PLANCHER", m, 22)
    b += T(330, 350, "POTEAU", m, 22, "end")
    if ok:
        b += dim_v(620, 40, 200, "attentes ≈ ls", t)
    return b


def s_semelle(t, ok, sol=False):
    m, ink = t["muted"], t["ink"]
    b = L(20, 250, 980, 250, m, 2, 'stroke-dasharray="6 6"') + T(960, 240, "sol", m, 20, "end")
    b += R(150, 260, 700, 110, m, 4) + R(430, 40, 140, 220, m, 4)
    if sol:
        # nappe posée à même la terre (erreur) / sur béton de propreté avec cales (correct)
        b += hatch(120, 370, 760, 36, m, 14) if not ok else R(130, 370, 740, 30, m, 2, t["line"], .8)
        yb = 364 if not ok else 340
        if ok:
            b += T(500, 395, "béton de propreté", m, 20) + "".join(R(x - 12, yb + 8, 24, 22, m, 2) for x in (230, 500, 770))
    else:
        yb = 340 if ok else 280
        b += R(130, 370, 740, 30, m, 2, t["line"], .8)
    b += P([(175, yb), (825, yb)], CUIVRE, 9)
    for x in range(200, 820, 50):
        b += C(x, yb - 12, 8, CUIVRE)
    for x in (455, 545):
        b += P([(x - 60 if x < 500 else x + 60, yb - 14), (x, yb - 14), (x, 20)], CUIVRE, 9)
    return b


def w_semelle(t):
    m, si = t["muted"], t["si"]
    return (R(430, 40, 140, 200, m, 4) + R(150, 240, 700, 110, m, 4) + arrows_down([500], 230, m, 60)
            + arrows_up(range(190, 830, 70), 360, si, 50)
            + f'<path d="M150 300 Q500 360 850 300" fill="none" stroke="{si}" stroke-width="5" stroke-dasharray="12 8"/>'
            + T(500, 150, "charge du poteau", m, 22) + T(500, 440, "le sol pousse : le BAS de la semelle est tendu", t["ink"], 24))


def s_dalle(t, ok):
    m, ink = t["muted"], t["ink"]
    b = hatch(80, 40, 50, 340, m) + hatch(870, 40, 50, 340, m) + R(130, 40, 740, 340, m, 3)
    main_h = ok
    for k in range(9):
        y = 70 + k * 35
        b += L(150, y, 850, y, CUIVRE if main_h else ink, 8 if main_h else 3, 'opacity=".9"')
    for k in range(12):
        x = 170 + k * 60
        b += L(x, 55, x, 365, CUIVRE if not main_h else ink, 8 if not main_h else 3, 'opacity=".9"')
    b += T(105, 405, "MUR", m, 20) + T(895, 405, "MUR", m, 20)
    b += T(500, 412, "← portée →", t["ink"], 24)
    b += T(500, 30, "VUE DE DESSUS", m, 20)
    return b


def s_serrees(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 330, 30, 340, 380
    b = R(x0, y0, w, h, m, 4) + R(x0 + 30, y0 + 30, w - 60, h - 60, ink, 5)
    r = 17
    if ok:
        for cx in (x0 + 64, x0 + 133, x0 + 207, x0 + w - 64):
            b += C(cx, y0 + h - 64, r, CUIVRE)
        for cx in (x0 + 64, x0 + w - 64):
            b += C(cx, y0 + h - 130, r, CUIVRE)
        b += T(x0 + w + 30, y0 + h - 90, "2 lits, espacés", t["ink"], 24, "start")
    else:
        for k in range(6):
            b += C(x0 + 62 + k * 43, y0 + h - 64, r + 2, CUIVRE)
        b += T(x0 + w + 30, y0 + h - 56, "6 HA25 collés", t["ink"], 24, "start")
    for cx in (x0 + 64, x0 + w - 64):
        b += C(cx, y0 + 64, 11, CUIVRE)
    b += T(x0 - 30, y0 + h / 2, "COUPE", m, 22, "end")
    return b


def s_chapeaux(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(40, 130, 920, 130, m) + stirrups(64, 940, 138, 252, 40, ink)
    b += P([(56, 214), (56, 242), (944, 242), (944, 214)], CUIVRE, 11)
    b += P([(56, 150), (944, 150)], CUIVRE, 4)
    if ok:
        b += P([(330, 150), (670, 150)], CUIVRE, 12)
        b += dim_h(330, 670, 90, "chapeaux", t)
    b += support(80, 260, m) + support(500, 260, m) + support(920, 260, m)
    b += T(500, 340, "appui intermédiaire", m, 22)
    return b


def w_moment_continu(t):
    m, si = t["muted"], t["si"]
    return (L(60, 200, 940, 200, m, 4) + support(60, 200, m) + support(500, 200, m) + support(940, 200, m)
            + f'<path d="M60 200 Q200 330 330 220 Q420 120 500 90 Q580 120 670 220 Q800 330 940 200" fill="{si}" opacity=".14"/>'
            + f'<path d="M60 200 Q200 330 330 220 Q420 120 500 90 Q580 120 670 220 Q800 330 940 200" fill="none" stroke="{si}" stroke-width="5"/>'
            + T(500, 70, "moment négatif : le HAUT est tendu", si, 24, weight=500) + T(200, 360, "M+", si, 26) + T(800, 360, "M+", si, 26))


def s_escalier(t, ok):
    m = t["muted"]
    b = f'<path d="M40 400 L500 180 L960 180 L960 110 L470 110 L40 330 Z" fill="none" stroke="{m}" stroke-width="3"/>'
    for k in range(6):  # marches
        x = 90 + k * 68
        y = 330 - (x - 40) * (220 / 430)
        b += f'<path d="M{x} {y:.0f} L{x} {y - 34:.0f} L{x + 68} {y - 34:.0f}" fill="none" stroke="{m}" stroke-width="2" opacity=".6"/>'
    if ok:
        b += P([(60, 376), (560, 135)], CUIVRE, 10) + P([(940, 158), (390, 158)], CUIVRE, 10)
    else:
        b += P([(60, 376), (500, 160), (940, 160)], CUIVRE, 10)
    b += T(760, 150, "PALIER", m, 22) + T(210, 390, "PAILLASSE", m, 22)
    return b


def s_ancrage(t, ok):
    m, ink = t["muted"], t["ink"]
    b = hatch(40, 260, 140, 150, m) + R(40, 110, 920, 150, m) + stirrups(200, 940, 118, 252, 36, ink)
    if ok:
        b += P([(80, 170), (80, 236), (944, 236)], CUIVRE, 12)
    else:
        b += P([(195, 236), (944, 236)], CUIVRE, 12)
    b += P([(80, 132), (944, 132)], CUIVRE, 6)
    b += T(110, 440, "APPUI DE RIVE", m, 20)
    return b



# ------------------------------------------------------------ scénarios (suite) : poteaux, voiles, dalles, fondations
def _poteau(t, x0, y0, w, h):
    """Fût de poteau vu en élévation."""
    return R(x0, y0, w, h, t["muted"], 4)


def s_poteau_cadres(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 420, 20, 200, 410
    b = _poteau(t, x0, y0, w, h)
    for dx in (34, w - 34):
        b += L(x0 + dx, y0 + 14, x0 + dx, y0 + h - 14, CUIVRE, 9)
    if ok:  # cadres resserrés en tête et en pied (zones critiques)
        for zy0, zy1, pas in ((y0 + 22, y0 + 120, 22), (y0 + h - 120, y0 + h - 22, 22), (y0 + 140, y0 + h - 140, 52)):
            yy = zy0
            while yy <= zy1:
                b += L(x0 + 20, yy, x0 + w - 20, yy, ink, 5)
                yy += pas
        b += T(x0 + w + 26, y0 + 70, "zone critique", SIGNAL, 22, "start")
        b += T(x0 + w + 26, y0 + h - 50, "zone critique", SIGNAL, 22, "start")
    else:  # espacement constant sur toute la hauteur
        yy = y0 + 22
        while yy <= y0 + h - 22:
            b += L(x0 + 20, yy, x0 + w - 20, yy, ink, 5)
            yy += 52
    b += T(x0 - 30, y0 + h / 2, "POTEAU", m, 22, "end")
    return b


def s_poteau_enrobage(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 400, 50, 260, 320
    c = 34 if ok else 4
    b = R(x0, y0, w, h, m, 4) + R(x0 + c, y0 + c, w - 2 * c, h - 2 * c, ink, 5)
    for cx in (x0 + c + 20, x0 + w - c - 20):
        for cy in (y0 + c + 20, y0 + h - c - 20):
            b += C(cx, cy, 16, CUIVRE)
    b += dim_v(x0 + w + 36, y0, y0 + c, "c = enrobage" if ok else "c ≈ 0", t)
    b += T(x0 - 30, y0 + h / 2, "COUPE", m, 22, "end")
    return b


def s_poteau_recouv(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 420, 20, 200, 410
    b = _poteau(t, x0, y0, w, h) + L(x0 - 40, y0 + h - 60, x0 + w + 40, y0 + h - 60, m, 3, 'stroke-dasharray="10 8"')
    b += T(x0 + w + 50, y0 + h - 52, "plancher", m, 22, "start")
    zy = (y0 + 150) if ok else (y0 + h - 130)
    for dx in (46, w - 46):
        b += L(x0 + dx, y0 + 14, x0 + dx, zy + 110, CUIVRE, 9)
        b += L(x0 + dx + 18, zy, x0 + dx + 18, y0 + h - 14, CUIVRE, 9)
    b += dim_v(x0 - 46, zy, zy + 110, "recouvrement", t, -1)
    b += T(500, 440, "à mi-hauteur" if ok else "en pied de poteau", SIGNAL if ok else t["ink"], 24)
    return b


def s_noeud(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(430, 20, 180, 410, m, 4)                       # poteau
    b += R(610, 150, 350, 150, m, 4)                     # poutre
    for dy in (176, 274):
        b += L(620, dy, 950, dy, CUIVRE, 9)
    for dx in (466, 574):
        b += L(dx, 34, dx, 416, CUIVRE, 9)
    yy = 170
    while yy <= 290:                                      # cadres de la poutre
        b += L(625, 162, 625, 288, ink, 4)
        yy += 40
    x = 640
    while x <= 940:
        b += L(x, 162, x, 288, ink, 4)
        x += 42
    if ok:
        for yy in (176, 214, 252, 290):
            b += L(442, yy, 598, yy, ink, 6)
        b += T(230, 240, "cadres dans le nœud", SIGNAL, 26, "end", font="Sora", weight=600)
    else:
        for yy in (60, 120, 350, 400):
            b += L(442, yy, 598, yy, ink, 5)
    b += T(760, 400, "NŒUD POUTRE-POTEAU", m, 22)
    return b


def s_tremie(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(120, 40, 760, 340, m, 4)
    for x in range(160, 880, 58):
        b += L(x, 60, x, 360, ink, 3, 'opacity=".5"')
    for y in range(70, 380, 58):
        b += L(140, y, 860, y, ink, 3, 'opacity=".5"')
    b += R(420, 150, 200, 140, t["bg"], 0, t["bg"]) + R(420, 150, 200, 140, m, 4)
    b += T(520, 228, "TRÉMIE", m, 24)
    if ok:
        for a, bb in (((420, 150), (330, 70)), ((620, 150), (710, 70)), ((420, 290), (330, 370)), ((620, 290), (710, 370))):
            b += P([a, bb], CUIVRE, 9)
        b += L(400, 130, 640, 130, CUIVRE, 9) + L(400, 310, 640, 310, CUIVRE, 9)
        b += L(400, 130, 400, 310, CUIVRE, 9) + L(640, 130, 640, 310, CUIVRE, 9)
        b += T(520, 414, "chevêtre + barres en diagonale", SIGNAL, 26, font="Sora", weight=600)
    b += T(90, 220, "DALLE", m, 22, "end")
    return b


def s_linteau(t, ok):
    m, ink = t["muted"], t["ink"]
    app = 90 if ok else 18
    b = hatch(80, 180, 220, 240, m) + hatch(700, 180, 220, 240, m)      # maçonnerie
    b += R(300 - app, 140, 400 + 2 * app, 110, m, 4)                     # linteau
    for dy in (170, 222):
        b += L(300 - app + 16, dy, 700 + app - 16, dy, CUIVRE, 9)
    x = 300 - app + 24
    while x <= 700 + app - 24:
        b += L(x, 152, x, 240, ink, 4)
        x += 44
    b += dim_h(700, 700 + app, 320, "appui", t)
    b += T(500, 120, "LINTEAU", m, 22)
    return b


def s_voile(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 150, 40, 700, 340
    b = R(x0, y0, w, h, m, 4)
    nap = [y0 + 40] if not ok else [y0 + 40, y0 + h - 40]
    for y in nap:
        b += L(x0 + 20, y, x0 + w - 20, y, CUIVRE, 8)
        for x in range(x0 + 60, x0 + w - 40, 70):
            b += L(x, y0 + 24, x, y0 + h - 24, CUIVRE, 6, 'opacity=".9"')
    if ok:
        for x in range(x0 + 95, x0 + w - 60, 140):       # épingles entre les deux nappes
            b += P([(x - 18, y0 + 40), (x + 18, y0 + h - 40)], ink, 6)
        b += T(500, 414, "deux nappes reliées par des épingles", SIGNAL, 26, font="Sora", weight=600)
    else:
        b += T(500, 414, "une seule nappe", t["ink"], 24)
    b += T(120, 220, "VOILE", m, 22, "end")
    return b


def s_longrine(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(60, 170, 880, 130, m, 4)
    b += R(400, 300, 200, 110, m, 4) + T(500, 380, "POTEAU", m, 20)
    if ok:
        for dy in (196, 274):
            b += L(80, dy, 920, dy, CUIVRE, 10)
        b += L(330, 196, 670, 196, CUIVRE, 14)
        b += T(500, 140, "acier continu + renfort sur appui", SIGNAL, 26, font="Sora", weight=600)
    else:
        for dy in (196, 274):
            b += L(80, dy, 440, dy, CUIVRE, 10) + L(560, dy, 920, dy, CUIVRE, 10)
    x = 90
    while x <= 910:
        b += L(x, 182, x, 288, ink, 4)
        x += 46
    b += T(500, 440, "LONGRINE", m, 22)
    return b


def s_radier(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(100, 160, 800, 140, m, 4)
    b += R(420, 40, 160, 120, m, 4) + T(500, 110, "POTEAU", m, 20)
    princ = 186 if ok else 274
    sec = 274 if ok else 186
    b += L(120, princ, 880, princ, CUIVRE, 13) + L(120, sec, 880, sec, CUIVRE, 7)
    b += arrows_up([200, 350, 650, 800], 330, SIGNAL if ok else m, 40)
    b += T(820, 400, "poussée du sol", t["ink"], 22)
    b += T(80, 230, "RADIER", m, 22, "end")
    b += T(500, 438, "nappe principale en partie haute", SIGNAL, 24) if ok else ""
    return b


def s_souten(t, ok):
    m, ink = t["muted"], t["ink"]
    b = P([(300, 420), (300, 60), (380, 60), (380, 420)], m, 5)        # voile
    b += R(240, 420, 400, 60, m, 4)                                      # semelle
    b += hatch(380, 120, 420, 300, m)                                    # terre retenue
    face = 312 if ok else 368
    b += L(face, 80, face, 410, CUIVRE, 11)
    for y in range(110, 410, 54):
        b += L(300, y, 380, y, CUIVRE, 5, 'opacity=".8"')
    b += arrows_up([430, 530, 630], 300, m, 0)
    b += f'<path d="M420 260 L370 260" fill="none" stroke="{m}" stroke-width="4" marker-end=""/>'
    b += L(420, 260, 392, 260, m, 4) + P([(400, 252), (388, 260), (400, 268)], m, 4)
    b += T(520, 250, "poussée des terres", t["ink"], 24, "start")
    b += T(200, 240, "MUR", m, 22, "end")
    b += T(500, 40, "acier côté " + ("opposé à la terre" if ok else "terre"), SIGNAL if ok else t["ink"], 26, font="Sora", weight=600)
    return b


def s_poteau_court(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 420, 20, 200, 410
    b = _poteau(t, x0, y0, w, h)
    b += hatch(120, 230, 300, 200, m) + hatch(620, 230, 300, 200, m)     # allèges qui brident le poteau
    b += T(270, 210, "allège", m, 22) + T(770, 210, "allège", m, 22)
    for dx in (34, w - 34):
        b += L(x0 + dx, y0 + 14, x0 + dx, y0 + h - 14, CUIVRE, 9)
    pas = 22 if ok else 52
    yy = y0 + 26
    while yy <= y0 + 215:
        b += L(x0 + 20, yy, x0 + w - 20, yy, ink, 5)
        yy += pas
    yy = y0 + 235
    while yy <= y0 + h - 20:
        b += L(x0 + 20, yy, x0 + w - 20, yy, ink, 5)
        yy += 52
    b += dim_v(x0 - 46, y0 + 20, y0 + 220, "partie libre", t, -1)
    return b


def s_reprise(t, ok):
    m, ink = t["muted"], t["ink"]
    b = hatch(200, 230, 600, 190, m, 26)                                   # béton déjà coulé
    if ok:
        b += P([(200, 230), (260, 200), (320, 230), (380, 200), (440, 230), (500, 200), (560, 230), (620, 200), (680, 230), (740, 200), (800, 230)], m, 5)
        for x in range(260, 790, 90):
            b += L(x, 215, x, 90, CUIVRE, 9) + P([(x, 90), (x + 30, 110)], CUIVRE, 9)
        b += T(500, 60, "surface rugueuse + attentes", SIGNAL, 26, font="Sora", weight=600)
    else:
        b += L(200, 230, 800, 230, m, 7) + R(200, 120, 600, 110, m, 2, "none", .35)
        b += T(500, 180, "coulage suivant : rien pour accrocher", t["ink"], 24)
    b += T(500, 442, "JOINT DE REPRISE", m, 22)
    return b


def s_epingles(t, ok):
    m, ink = t["muted"], t["ink"]
    x0, y0, w, h = 230, 50, 540, 330
    c = 34
    b = R(x0, y0, w, h, m, 4) + R(x0 + c, y0 + c, w - 2 * c, h - 2 * c, ink, 5)
    xs = [x0 + c + 24 + i * (w - 2 * c - 48) / 4 for i in range(5)]
    for cx in xs:
        b += C(cx, y0 + h - c - 24, 17, CUIVRE)
    for cx in (xs[0], xs[-1]):
        b += C(cx, y0 + c + 24, 14, CUIVRE)
    if ok:
        for cx in (xs[1], xs[3]):
            b += P([(cx, y0 + h - c - 24), (cx, y0 + c + 24)], ink, 6)
            b += P([(cx - 16, y0 + c + 34), (cx, y0 + c + 24), (cx + 16, y0 + c + 34)], ink, 6)
        b += T(500, 420, "épingles sur les barres intermédiaires", SIGNAL, 26, font="Sora", weight=600)
    else:
        b += T(500, 420, "barres du milieu non tenues", t["ink"], 24)
    b += T(200, 220, "COUPE", m, 22, "end")
    return b


def s_treillis(t, ok):
    m, ink = t["muted"], t["ink"]
    rec = 170 if ok else 40
    b = R(80, 150, 460, 150, m, 3, "none")
    for y in range(170, 300, 40):
        b += L(90, y, 530, y, CUIVRE, 6)
    for x in range(110, 530, 60):
        b += L(x, 160, x, 292, CUIVRE, 5, 'opacity=".8"')
    x0 = 530 - rec
    for y in range(182, 310, 40):
        b += L(x0, y, 950, y, CUIVRE, 6)
    for x in range(x0 + 30, 950, 60):
        b += L(x, 172, x, 304, CUIVRE, 5, 'opacity=".8"')
    b += dim_h(x0, 530, 360, "recouvrement", t)
    b += T(500, 100, "PANNEAUX DE TREILLIS SOUDÉ", m, 22)
    return b


def s_porte_faux(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(120, 200, 420, 110, m, 4) + R(540, 200, 360, 110, m, 4)
    b += support(330, 310, m)
    lo = 820 if ok else 620
    b += L(540, 226, 900, 226, CUIVRE, 11)                               # chapeaux du porte-à-faux
    b += L(160, 226, 540, 226, CUIVRE, 11) if ok else ""
    b += L(360, 226, 540, 226, CUIVRE, 11) if not ok else ""
    b += dim_h(160 if ok else 360, 540, 150, "longueur des chapeaux", t)
    b += L(160, 284, 520, 284, CUIVRE, 7)
    b += arrows_down([620, 720, 820, 880], 190, m, 40)
    b += T(720, 380, "PORTE-À-FAUX", m, 22)
    b += T(330, 380, "travée", m, 22)
    return b


def s_sens_dalle(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(140, 60, 720, 300, m, 4)
    b += hatch(100, 60, 40, 300, m) + hatch(860, 60, 40, 300, m)          # appuis (petite portée)
    gros, fin = (8, 4) if ok else (4, 8)
    for y in range(100, 350, 40):                                         # barres dans le sens de la portée
        b += L(160, y, 840, y, CUIVRE, gros if ok else fin, 'opacity=".9"')
    for x in range(190, 850, 48):
        b += L(x, 80, x, 340, CUIVRE, fin if ok else gros, 'opacity=".9"')
    b += dim_h(140, 860, 400, "portée principale", t)
    b += T(500, 40, "DALLE PORTANT SUR DEUX APPUIS", m, 22)
    return b


def s_pliage(t, ok):
    m, ink = t["muted"], t["ink"]
    r = 70 if ok else 14
    b = f'<path d="M160 120 L{500 - r} 120 A{r} {r} 0 0 1 {500} {120 + r} L500 360" fill="none" stroke="{CUIVRE}" stroke-width="16" stroke-linecap="round"/>'
    b += C(500 - r, 120 + r, 6, m) + f'<circle cx="{500 - r}" cy="{120 + r}" r="{r}" fill="none" stroke="{m}" stroke-width="2" stroke-dasharray="8 8"/>'
    b += T(500 - r - 30, 120 + r + 10, "rayon de pliage", t["ink"], 24, "end")
    b += T(700, 400, "PLIAGE D’UNE BARRE", m, 22)
    return b


def s_about(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(60, 180, 880, 150, m, 4) + support(820, 330, m)
    b += L(80, 300, 920, 300, CUIVRE, 11)
    if ok:
        b += P([(900, 300), (900, 210)], CUIVRE, 11)
        b += T(760, 170, "retour d’about", SIGNAL, 26, font="Sora", weight=600)
    b += L(80, 206, 700, 206, CUIVRE, 9)
    x = 100
    while x <= 920:
        b += L(x, 192, x, 318, ink, 4)
        x += 46
    b += T(500, 420, "EXTRÉMITÉ DE POUTRE SUR APPUI", m, 22)
    return b


def s_cale_dalle(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(100, 200, 800, 150, m, 4)
    y = 280 if ok else 344
    for x in range(130, 880, 56):
        b += L(x, y, x + 36, y, CUIVRE, 10)
    if ok:
        for x in (220, 420, 620, 820):
            b += P([(x - 18, 348), (x, 286), (x + 18, 348)], ink, 5)
        b += T(500, 420, "cales sous les aciers", SIGNAL, 26, font="Sora", weight=600)
    else:
        b += T(500, 420, "aciers posés sur le coffrage", t["ink"], 24)
    b += L(100, 350, 900, 350, m, 6)
    b += T(80, 280, "DALLE", m, 22, "end")
    return b


def s_nappe_semelle(t, ok):
    m, ink = t["muted"], t["ink"]
    b = R(180, 240, 640, 130, m, 4) + R(440, 100, 120, 140, m, 4) + T(500, 180, "POT.", m, 20)
    b += hatch(120, 370, 760, 50, m)
    if ok:
        b += L(210, 340, 790, 340, CUIVRE, 12)
        for x in range(240, 790, 60):
            b += P([(x, 340), (x, 300)], CUIVRE, 8)
        b += T(500, 450, "nappe en partie basse, barres relevées", SIGNAL, 26, font="Sora", weight=600)
    else:
        b += L(210, 268, 790, 268, CUIVRE, 12)
        b += T(500, 450, "nappe trop haute", t["ink"], 24)
    return b


SCENARIOS = {
    "poteau_cadres": dict(draw=s_poteau_cadres, zone=(520, 225, 135, 205), lab=(215, 230, "même espacement partout"), why=None),
    "poteau_enrobage": dict(draw=s_poteau_enrobage, zone=(530, 90, 180, 60), lab=(500, 430, "les barres touchent le coffrage"), why=None),
    "poteau_recouv": dict(draw=s_poteau_recouv, zone=(520, 355, 150, 70), lab=(520, 470, "recouvrement en pied de poteau"), why=None),
    "noeud": dict(draw=s_noeud, zone=(520, 225, 110, 95), lab=(250, 300, "aucun cadre dans le nœud"), why=None),
    "tremie": dict(draw=s_tremie, zone=(520, 220, 150, 110), lab=(520, 420, "trémie sans renfort"), why=None),
    "linteau": dict(draw=s_linteau, zone=(712, 195, 70, 70), lab=(760, 120, "appui trop court"), why=None),
    "voile": dict(draw=s_voile, zone=(500, 320, 330, 50), lab=(500, 440, ""), why=None),
    "longrine": dict(draw=s_longrine, zone=(500, 235, 120, 80), lab=(500, 130, "acier interrompu sur l’appui"), why=None),
    "radier": dict(draw=s_radier, zone=(500, 274, 350, 36), lab=(500, 70, "la nappe principale est en bas"), why=None),
    "souten": dict(draw=s_souten, zone=(368, 240, 46, 180), lab=(700, 90, "acier du mauvais côté"), why=None),
    "poteau_court": dict(draw=s_poteau_court, zone=(520, 130, 160, 115), lab=(520, 442, "cadres non resserrés sur la partie libre"), why=None),
    "reprise": dict(draw=s_reprise, zone=(500, 230, 320, 36), lab=(500, 140, "rien pour accrocher le béton suivant"), why=None),
    "epingles": dict(draw=s_epingles, zone=(500, 328, 140, 46), lab=(500, 440, ""), why=None),
    "treillis": dict(draw=s_treillis, zone=(510, 232, 90, 100), lab=(510, 60, "recouvrement trop court"), why=None),
    "porte_faux": dict(draw=s_porte_faux, zone=(450, 226, 130, 40), lab=(450, 100, "chapeaux trop courts"), why=None),
    "sens_dalle": dict(draw=s_sens_dalle, zone=(500, 210, 360, 150), lab=(500, 440, "grosses barres dans le mauvais sens"), why=None),
    "pliage": dict(draw=s_pliage, zone=(492, 150, 90, 90), lab=(700, 150, "angle trop vif"), why=None),
    "about": dict(draw=s_about, zone=(898, 290, 60, 50), lab=(700, 390, "la barre s’arrête net sur l’appui"), why=None),
    "cale_dalle": dict(draw=s_cale_dalle, zone=(500, 344, 380, 34), lab=(500, 420, ""), why=None),
    "nappe_semelle": dict(draw=s_nappe_semelle, zone=(500, 268, 320, 36), lab=(500, 450, ""), why=None),
    "barres_haut": dict(draw=s_barres_haut, zone=(500, 238, 470, 40), lab=(500, 330, "l'acier principal doit être en bas"), why=w_moment_pos),
    "console": dict(draw=s_console, zone=(530, 176, 400, 40), lab=(530, 108, "presque rien en haut"), why=w_console),
    "enrobage": dict(draw=s_enrobage, zone=(500, 380, 150, 50), lab=(500, 60, ""), why=None),
    "crochets": dict(draw=s_crochets, zone=(420, 90, 90, 80), lab=(260, 90, "cadre ouvert"), why=None),
    "recouvrement": dict(draw=s_recouvrement, zone=(500, 211, 110, 50), lab=(500, 120, "chevauchement trop court"), why=None),
    "attentes": dict(draw=s_attentes, zone=(500, 200, 140, 40), lab=(500, 120, "rien ne dépasse"), why=None),
    "semelle": dict(draw=lambda t, ok: s_semelle(t, ok), zone=(500, 280, 360, 36), lab=(500, 400, "nappe en haut"), why=w_semelle),
    "dalle": dict(draw=s_dalle, zone=(500, 210, 380, 190), lab=(500, 30, ""), why=None),
    "serrees": dict(draw=s_serrees, zone=(500, 346, 180, 44), lab=(500, 60, ""), why=None),
    "chapeaux": dict(draw=s_chapeaux, zone=(500, 150, 190, 36), lab=(500, 90, "rien au-dessus de l'appui"), why=w_moment_continu),
    "escalier": dict(draw=s_escalier, zone=(500, 170, 90, 60), lab=(640, 280, "angle rentrant"), why=None),
    "ancrage": dict(draw=s_ancrage, zone=(150, 236, 110, 50), lab=(300, 320, "barre non ancrée"), why=None),
    "semelle_sol": dict(draw=lambda t, ok: s_semelle(t, ok, sol=True), zone=(500, 364, 380, 34), lab=(500, 20, ""), why=None),
}


def scenario_svg(t, key, mode, w=900):
    """mode : erreur, reponse, correct, pourquoi."""
    sc = SCENARIOS[key]
    if mode == "pourquoi":
        return f'<svg width="{w}" viewBox="0 0 1000 450">{sc["why"](t)}</svg>'
    body = sc["draw"](t, mode == "correct")
    cx, cy, rx, ry = sc["zone"]
    if mode == "reponse":
        body += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{ALERTE}" stroke-width="7" stroke-dasharray="18 10"/>'
        lx, ly, s = sc["lab"]
        if s:
            body += T(lx, ly, s, ALERTE, 30, font="Sora", weight=600)
    elif mode == "correct":
        body += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{SIGNAL}" opacity=".14"/>'
    return f'<svg width="{w}" viewBox="0 0 1000 450">{body}</svg>'
