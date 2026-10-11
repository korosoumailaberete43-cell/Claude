"""Le P de POGBUS : une lettre géométrique paramétrique, construite sur 12 x 12 modules.

Langage de forme : tout angle est soit droit, soit coupé à 45°. La coupe à 45° est
le triangle du bogolan — c'est le motif du bonnet et le fil conducteur de la marque.
"""
from grille import U

def _d(pts, close=True):
    return "M" + "L".join(f"{x * U:.3f} {y * U:.3f}" for x, y in pts) + ("Z" if close else "")


def cadre(x0, y0, x1, y1, coupe_hd=0, coupe_bd=0, coupe_hg=0, coupe_bg=0):
    """Rectangle dont chaque coin peut être coupé à 45° (valeur = longueur de la coupe, en modules)."""
    p = []
    p.append((x0 + coupe_hg, y0))
    p.append((x1 - coupe_hd, y0))
    if coupe_hd: p.append((x1, y0 + coupe_hd))
    p.append((x1, y1 - coupe_bd))
    if coupe_bd: p.append((x1 - coupe_bd, y1))
    p.append((x0 + coupe_bg, y1))
    if coupe_bg: p.append((x0, y1 - coupe_bg))
    p.append((x0, y0 + coupe_hg))
    if coupe_hg: pass
    return p


# ------------------------------------------------------------------ contrepoinçons
def contre_plein(x0, y0, x1, y1, c):
    return cadre(x0, y0, x1, y1, coupe_hd=c, coupe_bd=c)


def contre_fleche(x0, y0, x1, y1, c):
    """Le vide intérieur dessine une flèche qui monte vers la droite."""
    return [(x0, y1), (x0, y1 - 1.25), (x1 - 1.6, y0 + 1.25), (x1 - 1.6, y0 + 2.5),
            (x1, y0 + 0.4), (x1 - 2.1, y0), (x1 - 2.35, y0 + 1.2),
            (x0 + 0.0, y1 - 2.6)]


def contre_escalier(x0, y0, x1, y1, c, n=3):
    """Le vide intérieur dessine un escalier qui monte vers la droite."""
    pas_x = (x1 - x0) / n
    pas_y = (y1 - y0) / n
    p = [(x0, y1)]
    for k in range(n):
        p.append((x0 + k * pas_x, y1 - k * pas_y))
        p.append((x0 + (k + 1) * pas_x, y1 - k * pas_y))
    p.append((x1, y0))
    p.append((x1, y1))
    return p


CONTRES = {"plein": contre_plein, "fleche": contre_fleche, "escalier": contre_escalier}


def lettre_p(contre="plein", fut=2.6, panse_h=7.2, panse_l=10.2, coupe=1.9,
             jeu=0.0, c_fut=None, c_panse=None, couleur="#0A0A0A"):
    """Renvoie le fragment SVG du P.

    jeu : écart entre le fût et la panse (0 = lettre d'un seul tenant).
    """
    cf = c_fut or couleur
    cp = c_panse or couleur
    g = []
    g.append(f'<path d="{_d(cadre(0, 0, fut, 12))}" fill="{cf}"/>')
    x0 = fut + jeu
    ext = cadre(x0, 0, panse_l, panse_h, coupe_hd=coupe, coupe_bd=coupe)
    ci, cx0, cy0 = coupe - 0.9, x0, fut * 0.78
    inn = CONTRES[contre](cx0, cy0, panse_l - fut, panse_h - fut * 0.78, max(ci, 0.6))
    g.append(f'<path d="{_d(ext)}{_d(inn)}" fill="{cp}" fill-rule="evenodd"/>')
    return "".join(g)
