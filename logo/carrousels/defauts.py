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


SCENARIOS = {
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
