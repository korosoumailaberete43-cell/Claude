"""POGBUS GROUP — la structure du logo d'origine : le mot, l'arc doré, et un O travaillé.

Le O remplace le portrait. Il ne montre pas l'homme, il le signifie.
"""
import math
import alphabet as A
from alphabet import LETTRES, CRENAGE, oct_rect, creux, d, TOUS, H, mot
from grille import U

OR, NOIR, BLANC = "#BE8A22", "#111111", "#FFFFFF"
S, C = 2.05, 1.60


# ------------------------------------------------------------------ l'arc
def croissant(cx, cy, R, a1, a2, ep, n=90):
    """Croissant doré : épais au départ, effilé en pointe à l'arrivée."""
    ext, inn = [], []
    for i in range(n + 1):
        t = i / n
        a = math.radians(a1 + (a2 - a1) * t)
        e = ep * (1 - t) ** 1.45
        ext.append((cx + math.cos(a) * R, cy + math.sin(a) * R))
        inn.append((cx + math.cos(a) * (R - e), cy + math.sin(a) * (R - e)))
    return d(ext + inn[::-1])


# ------------------------------------------------------------------ les O
def _anneau_o(w, cap, s, c, decale=0.0):
    ci = creux(c, s)
    return (d(oct_rect(-decale, -decale, w + decale, cap + decale, c, TOUS))
            + d(oct_rect(s - decale, s - decale, w - s + decale, cap - s + decale, ci, TOUS)))


def o_bonnet(w=10.2, cap=12.6, s=2.15, c=1.75, c_lettre=NOIR, c_accent=OR,
             ampleur=0.95, incl=-7.0, dome_or=False, n_tri=5, decal_x=0.75):
    """Le O est la tête, réduite à un anneau. Le bonnet la coiffe et déborde du mot.

    Transposition du logo d'origine : même silhouette, aucun visage.
    La calotte a un pan coupé à 45° de chaque côté, comme toutes les lettres.
    """
    g = [f'<path d="{_anneau_o(w, cap, s, c)}" fill="{c_lettre}" fill-rule="evenodd"/>']
    cx = w / 2 + decal_x
    lb = w * 1.30 * ampleur                  # largeur du bandeau
    hd = cap * 0.56 * ampleur                # hauteur de la calotte
    y_b0, y_b1 = -0.1, 1.75                  # le bandeau mord sur le haut du O
    ep = (y_b1 - y_b0)
    # calotte : montants verticaux courts, épaules coupées à 45°, sommet plat
    lt = lb * 0.46                           # largeur du sommet
    ep_mur = hd * 0.22                       # hauteur du montant avant la coupe
    calotte = [(cx - lb / 2 + 0.3, y_b0),
               (cx - lb / 2 + 0.3, y_b0 - ep_mur),
               (cx - lt / 2, y_b0 - hd),
               (cx + lt / 2, y_b0 - hd),
               (cx + lb / 2 - 0.3, y_b0 - ep_mur),
               (cx + lb / 2 - 0.3, y_b0)]
    bandeau = oct_rect(cx - lb / 2, y_b0, cx + lb / 2, y_b1, ep * 0.40, TOUS)
    c_dome = c_accent if dome_or else c_lettre
    c_tri = c_lettre if dome_or else c_accent
    tri = []
    etendue = lb * 0.56                      # les triangles restent dans la calotte
    pas = etendue / max(n_tri - 1, 1)
    bt = min(lb * 0.105, pas * 0.44)
    for k in range(n_tri):
        tx = cx + (k - (n_tri - 1) / 2) * pas
        tri.append(d([(tx - bt, y_b0 - hd * 0.16), (tx + bt, y_b0 - hd * 0.16),
                      (tx, y_b0 - hd * 0.72)]))
    g.append(f'<g transform="rotate({incl} {cx*U:.2f} {y_b0*U:.2f})">'
             f'<path d="{d(calotte)}" fill="{c_dome}"/>'
             f'<path d="{"".join(tri)}" fill="{c_tri}"/>'
             f'<path d="{d(bandeau)}" fill="{c_accent if not dome_or else c_lettre}"/></g>')
    return "".join(g), w, cap


def o_frise(w=10.0, cap=12.6, s=2.3, c=1.75, c_lettre=NOIR, c_accent=OR):
    """Le O ceint d'une frise bogolan : le motif du bonnet, sans le bonnet."""
    ci = creux(c, s)
    g = [f'<path d="{_anneau_o(w, cap, s, c)}" fill="{c_lettre}" fill-rule="evenodd"/>']
    v = oct_rect(s * 0.42, s * 0.42, w - s * 0.42, cap - s * 0.42, c, TOUS)
    out = []
    for i in range(len(v)):
        ax, ay = v[i]
        bx, by = v[(i + 1) % len(v)]
        lx, ly = bx - ax, by - ay
        lg = math.hypot(lx, ly)
        ux, uy = lx / lg, ly / lg
        nx, ny = uy, -ux
        if (ax + nx - w / 2) ** 2 + (ay + ny - cap / 2) ** 2 > (ax - w / 2) ** 2 + (ay - cap / 2) ** 2:
            nx, ny = -nx, -ny
        for k in range(2):
            t = (k + 0.5) * lg / 2
            mx, my = ax + ux * t, ay + uy * t
            tt = s * 0.46
            out.append(d([(mx - ux * tt, my - uy * tt), (mx + ux * tt, my + uy * tt),
                          (mx + nx * tt * 1.25, my + ny * tt * 1.25)]))
    g.append(f'<path d="{"".join(out)}" fill="{c_accent}"/>')
    return "".join(g), w, cap


def o_etoile(w=10.2, cap=12.8, s=2.1, c=1.75, c_lettre=NOIR, c_accent=OR):
    """Le O garde une étoile à huit branches : le repère, la direction."""
    g = [f'<path d="{_anneau_o(w, cap, s, c)}" fill="{c_lettre}" fill-rule="evenodd"/>']
    cx, cy, R = w / 2, cap / 2, min(w, cap) / 2 - s - 0.30
    br = []
    for i in range(8):
        a = math.radians(i * 45)
        ca, sa = math.cos(a), math.sin(a)
        px, py = -sa, ca
        pointe = R if i % 2 == 0 else R * 0.62
        demi = R * 0.21
        br.append(d([(cx + ca * pointe, cy + sa * pointe),
                     (cx + px * demi, cy + py * demi), (cx - px * demi, cy - py * demi)]))
    g.append(f'<path d="{"".join(br)}" fill="{c_accent}"/>')
    return "".join(g), w, cap


def o_cinq(w=10.2, cap=12.8, s=2.4, c=1.75, c_lettre=NOIR, c_accent=OR):
    """Le O fendu en cinq segments : les cinq métiers, un seul anneau."""
    g = []
    anneau = _anneau_o(w, cap, s, c)
    cx, cy = w / 2, cap / 2
    coupes = []
    for i in range(5):
        a = math.radians(-90 + i * 72 + 36)
        ca, sa = math.cos(a), math.sin(a)
        px, py = -sa, ca
        e = 0.34
        r0, r1 = min(w, cap) / 2 - s - 0.2, min(w, cap) / 2 + 0.6
        coupes.append(d([(cx + ca * r0 + px * e, cy + sa * r0 + py * e),
                         (cx + ca * r1 + px * e, cy + sa * r1 + py * e),
                         (cx + ca * r1 - px * e, cy + sa * r1 - py * e),
                         (cx + ca * r0 - px * e, cy + sa * r0 - py * e)]))
    g.append(f'<path d="{anneau}{"".join(coupes)}" fill="{c_lettre}" fill-rule="evenodd"/>')
    return "".join(g), w, cap


O_VARIANTES = {"bonnet": o_bonnet, "frise": o_frise, "etoile": o_etoile, "cinq": o_cinq}


# ------------------------------------------------------------------ la traînée dorée
def trainee(x0, x1, x_apex, y_apex, y_depart, ep, n=120):
    """Comète dorée : épaisse au départ, effilée en pointe. Trajectoire parabolique."""
    a = (y_depart - y_apex) / (x0 - x_apex) ** 2
    haut, bas = [], []
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = a * (x - x_apex) ** 2 + y_apex
        e = ep * (1 - t) ** 1.30
        haut.append((x, y))
        bas.append((x, y + e))
    return d(haut + bas[::-1])


# ------------------------------------------------------------------ l'assemblage
def logo(variante="bonnet", c_lettre=NOIR, c_accent=OR, baseline=True,
         arc=True, cap_base=3.4, appro_base=7.0, ecart_base=2.0):
    """POGBUS avec un O travaillé, GROUP dessous, et la traînée dorée au-dessus."""
    parts, x = [], 0.0
    bas_mot = H
    for i, ch in enumerate("POGBUS"):
        if ch == "O":
            g, w, cap = O_VARIANTES[variante](c_lettre=c_lettre, c_accent=c_accent)
            dy = (H - cap) / 2
            parts.append(f'<g transform="translate({x*U:.3f} {dy*U:.3f})">{g}</g>')
            bas_mot = max(bas_mot, dy + cap)
        else:
            chem, w = LETTRES[ch](S, C)
            for dd, r in chem:
                parts.append(f'<path d="{dd}" fill="{c_lettre}" fill-rule="{r}" '
                             f'transform="translate({x*U:.3f} 0)"/>')
        if i < 5:
            x += w + 1.45 + CRENAGE.get((ch, "POGBUS"[i + 1]), 0.0)
        else:
            x += w
    larg = x
    haut_bas = bas_mot
    if baseline:
        kb = cap_base / H
        gb, wb = mot("GROUP", s=1.85, c=1.60, appro=appro_base, couleur=c_lettre)
        dx = (larg - wb * kb) / 2
        y = bas_mot + ecart_base
        parts.append(f'<g transform="translate({dx*U:.3f} {y*U:.3f}) scale({kb:.5f})">{gb}</g>')
        haut_bas = y + cap_base
    haut_sommet = 0.0
    if arc:
        # la traînée jaillit de derrière le bonnet, comme dans le logo d'origine
        a = trainee(x0=10.5, x1=larg + 2.5, x_apex=larg * 0.80, y_apex=-9.6,
                    y_depart=-4.4, ep=2.5)
        parts.insert(0, f'<path d="{a}" fill="{c_accent}"/>')
        haut_sommet = -9.6 - 0.3
    g = "".join(parts)
    if haut_sommet < 0:
        g = f'<g transform="translate(0 {-haut_sommet*U:.3f})">{g}</g>'
    return g, larg, haut_bas - haut_sommet
