"""Alphabet POGBUS : lettres géométriques dont tout angle est droit ou coupé à 45°.

La coupe à 45° est le triangle du bogolan. Une seule règle de forme gouverne
le symbole et le mot : c'est elle qui fait tenir l'identité ensemble.

Repère : hauteur de capitale H = 12 modules, graisse de fût s, coupe c.
"""
import math
from grille import U

R2 = math.sqrt(2)
H = 12.0

# coins : h-g, h-d, b-d, b-g
TOUS = (1, 1, 1, 1)
DROITE = (0, 1, 1, 0)
BAS = (0, 0, 1, 1)
HAUT = (1, 1, 0, 0)
AUCUN = (0, 0, 0, 0)


def oct_rect(x0, y0, x1, y1, c, coins=TOUS):
    """Rectangle à coins coupés à 45°. coins = (hg, hd, bd, bg)."""
    hg, hd, bd, bg = (c if k else 0 for k in coins)
    w, h = x1 - x0, y1 - y0
    hg, hd, bd, bg = (min(v, w / 2, h / 2) for v in (hg, hd, bd, bg))
    p = [(x0 + hg, y0), (x1 - hd, y0)]
    if hd: p.append((x1, y0 + hd))
    p.append((x1, y1 - bd))
    if bd: p.append((x1 - bd, y1))
    p.append((x0 + bg, y1))
    if bg: p.append((x0, y1 - bg))
    if hg: p.append((x0, y0 + hg))
    return p


def creux(c, s):
    """Longueur de coupe du contour intérieur pour une graisse s (vrai décalage parallèle)."""
    return max(c - s * (2 - R2), 0.0)


def d(pts):
    return "M" + "L".join(f"{x * U:.4f} {y * U:.4f}" for x, y in pts) + "Z"


# --------------------------------------------------------------------- lettres
# Chaque fonction renvoie (liste de chemins, chasse) — chasse = largeur d'avance.

def _anneau(x0, y0, x1, y1, s, c, coins=TOUS):
    ci = creux(c, s)
    return d(oct_rect(x0, y0, x1, y1, c, coins)) + d(oct_rect(x0 + s, y0 + s, x1 - s, y1 - s, ci, coins))


def L_O(s, c, w=9.4):
    return [(_anneau(0, 0, w, H, s, c), "evenodd")], w




def L_P(s, c, w=8.9, bh=7.0):
    ci = creux(c, s)
    fut = d([(0, 0), (s, 0), (s, H), (0, H)])
    panse = d(oct_rect(0, 0, w, bh, c, DROITE)) + d(oct_rect(s, s, w - s, bh - s, ci, DROITE))
    return [(fut, "nonzero"), (panse, "evenodd")], w


def L_R(s, c, w=9.1, bh=6.8):
    ci = creux(c, s)
    fut = d([(0, 0), (s, 0), (s, H), (0, H)])
    panse = d(oct_rect(0, 0, w - 0.5, bh, c, DROITE)) + d(oct_rect(s, s, w - 0.5 - s, bh - s, ci, DROITE))
    jambe = d([(s, bh - s), (s + s * 1.05, bh - s), (w, H), (w - s * 1.05, H)])
    return [(fut, "nonzero"), (panse, "evenodd"), (jambe, "nonzero")], w


def L_B(s, c, w=9.0):
    ci, taille = creux(c, s), H / 2 + s * 0.25
    fut = d([(0, 0), (s, 0), (s, H), (0, H)])
    haut = d(oct_rect(0, 0, w - 0.7, taille, c, DROITE)) + d(oct_rect(s, s, w - 0.7 - s, taille - s, ci, DROITE))
    bas = d(oct_rect(0, taille - s, w, H, c, DROITE)) + d(oct_rect(s, taille, w - s, H - s, ci, DROITE))
    return [(fut, "nonzero"), (haut, "evenodd"), (bas, "evenodd")], w





def L_G(s, c, w=9.6):
    """G : anneau octogonal, ouverture 45° à droite au-dessus de la barre."""
    ci = creux(c, s)
    y_bar = H / 2 - s * 0.55
    # l'ouverture commence franchement sous la coupe, sinon la terminaison fait une languette
    y_haut = H * 0.30
    anneau = (d(oct_rect(0, 0, w, H, c, TOUS))
              + d(oct_rect(s, s, w - s, H - s, ci, TOUS))
              + d([(w - s, y_haut), (w, y_haut), (w, y_bar), (w - s, y_bar)]))
    barre = d([(w / 2 - 0.35, y_bar), (w, y_bar), (w, y_bar + s), (w / 2 - 0.35, y_bar + s)])
    return [(anneau, "evenodd"), (barre, "nonzero")], w


def L_U(s, c, w=9.2):
    """U : contour intérieur arrêté exactement sur le bord supérieur (sinon il déborde)."""
    ci = creux(c, s)
    ext = oct_rect(0, 0, w, H, c, BAS)
    inn = oct_rect(s, 0, w - s, H - s, ci, BAS)
    return [(d(ext) + d(inn), "evenodd")], w


def L_S(s, c, w=8.9):
    """S : polygone unique, terminaisons coupées à 45°. Pas de contour intérieur."""
    t = s * 0.75
    mid, dm = H / 2, s / 2
    p = [(t, 0), (w - t, 0), (w, t), (w, s), (s, s), (s, mid - dm),
         (w - c, mid - dm), (w, mid - dm + c), (w, H - t), (w - t, H),
         (t, H), (0, H - t), (0, H - s), (w - s, H - s), (w - s, mid + dm),
         (0, mid + dm), (0, t)]
    return [(d(p), "nonzero")], w


LETTRES = {"O": L_O, "G": L_G, "P": L_P, "R": L_R, "B": L_B, "U": L_U, "S": L_S}


CRENAGE = {("P", "O"): -0.75, ("P", "G"): -0.75, ("P", "U"): -0.55,
           ("B", "U"): -0.20, ("U", "S"): -0.25, ("G", "B"): -0.15,
           ("R", "O"): -0.30, ("O", "U"): -0.20}


def mot(texte, s=2.15, c=2.45, appro=1.5, couleur="#0A0A0A", echelle=1.0):
    """Compose un mot. Renvoie (fragment SVG, largeur totale en modules)."""
    x, parts = 0.0, []
    for i, ch in enumerate(texte):
        chemins, w = LETTRES[ch](s, c)
        for dd, regle in chemins:
            parts.append(f'<path d="{dd}" fill="{couleur}" fill-rule="{regle}" '
                         f'transform="translate({x * U:.3f} 0)"/>')
        if i < len(texte) - 1:
            x += w + appro + CRENAGE.get((ch, texte[i + 1]), 0.0)
        else:
            x += w
    g = "".join(parts)
    if echelle != 1.0:
        g = f'<g transform="scale({echelle})">{g}</g>'
    return g, x


if __name__ == "__main__":
    import pathlib, cairosvg
    OR, NOIR, BLANC = "#D4A02C", "#0A0A0A", "#FFFFFF"
    g, w = mot("POGBUS", couleur=NOIR)
    marge = 1.5
    vb_w, vb_h = (w + 2 * marge) * U, (H + 2 * marge) * U
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.0f} {vb_h:.0f}">'
         f'<rect width="{vb_w:.0f}" height="{vb_h:.0f}" fill="{BLANC}"/>'
         f'<g transform="translate({marge * U} {marge * U})">{g}</g></svg>')
    p = pathlib.Path("../out/mot.png"); p.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=s.encode(), write_to=str(p), output_width=1800)
    print("écrit", p, f"largeur {w:.2f} modules")
