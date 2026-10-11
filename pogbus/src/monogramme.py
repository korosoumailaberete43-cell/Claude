"""Le monogramme PG : les deux initiales imbriquées, séparées par un jeu de découpe.

Les lettres ne sont pas redessinées : ce sont exactement le P et le G de l'alphabet
validé, repris tels quels. Le P passe devant, le G est évidé là où le P le croise.
"""
import alphabet as A
from alphabet import LETTRES, H, oct_rect, creux, d, DROITE, TOUS
from grille import U

OR, NOIR, BLANC = "#BE8A22", "#111111", "#FFFFFF"
S, C = 2.05, 1.60
_n = 0


def _lettre(ch, couleur, tx=0.0, ty=0.0, k=1.0):
    chem, w = LETTRES[ch](S, C)
    corps = "".join(f'<path d="{dd}" fill="{couleur}" fill-rule="{r}"/>' for dd, r in chem)
    return f'<g transform="translate({tx*U:.3f} {ty*U:.3f}) scale({k:.5f})">{corps}</g>', w * k, H * k


def _silhouette_p(k, jeu):
    """Contour du P épaissi de « jeu » : sert de masque pour creuser le G."""
    s, c = S + 2 * jeu / k, C + jeu / k
    bh = 6.8
    ci = creux(c, s)
    return (d([(-jeu/k, -jeu/k), (s - jeu/k, -jeu/k), (s - jeu/k, H + jeu/k), (-jeu/k, H + jeu/k)])
            + d(oct_rect(-jeu/k, -jeu/k, 8.9 + jeu/k, bh + jeu/k, c, DROITE))
            + d(oct_rect(-jeu/k + s, -jeu/k + s, 8.9 + jeu/k - s, bh + jeu/k - s, ci, DROITE)))


def monogramme(cap_p=16.0, cap_g=16.0, recouvre=0.30, jeu=0.52,
               c_p=OR, c_g=NOIR, cale="bas"):
    """P et G imbriqués. recouvre = part de la largeur du G mangée par le P.

    cale : « bas » = même ligne de pied ; « haut » = même ligne de tête.
    """
    global _n; _n += 1
    kp, kg = cap_p / H, cap_g / H
    w_p, w_g = 8.9 * kp, 9.6 * kg
    dx = w_p - w_g * recouvre
    haut = max(cap_p, cap_g)
    if cale == "bas":           # même ligne de pied
        y_p, y_g = haut - cap_p, haut - cap_g
    elif cale == "haut":        # même ligne de tête
        y_p, y_g = 0.0, 0.0
    elif cale == "centre":      # G centré sur la hauteur du P
        y_p, y_g = 0.0, (cap_p - cap_g) / 2
    else:                       # « niche » : le G sous la panse du P
        y_p, y_g = 0.0, cap_p * (6.8 / H)
        haut = max(cap_p, y_g + cap_g)

    gp, _, _ = _lettre("P", c_p, 0, y_p, kp)
    gg, _, _ = _lettre("G", c_g, 0, 0, kg)
    mid = f"m{_n}"
    masque = (f'<mask id="{mid}">'
              f'<rect x="{-5*U}" y="{-5*U}" width="{(w_g+20)*U}" height="{(haut+20)*U}" fill="white"/>'
              f'<path d="{_silhouette_p(kp, jeu)}" fill="black" fill-rule="evenodd" '
              f'transform="translate({-dx*U:.3f} {y_p*U:.3f}) scale({kp:.5f})"/></mask>')
    g = (f'<g transform="translate({dx*U:.3f} {y_g*U:.3f})">{masque}'
         f'<g mask="url(#{mid})">{gg}</g></g>{gp}')
    return g, dx + w_g, haut


def ecusson(cap=13.0, marge=2.6, coupe=3.2, c_fond=NOIR, c_p=OR, c_g=BLANC, **kw):
    """Le monogramme posé dans un écusson octogonal."""
    g, w, h = monogramme(cap, cap, c_p=c_p, c_g=c_g, **kw)
    cote_x, cote_y = w + 2 * marge, h + 2 * marge
    fond = f'<path d="{d(oct_rect(0, 0, cote_x, cote_y, coupe, TOUS))}" fill="{c_fond}"/>'
    return fond + f'<g transform="translate({marge*U:.3f} {marge*U:.3f})">{g}</g>', cote_x, cote_y
