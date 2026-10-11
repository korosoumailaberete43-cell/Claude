"""Quatre pistes d'emblème POGBUS : les initiales P et G, cachées dans un signe.

Même langage que le mot validé : tout angle droit ou coupé à 45°, graisse 2.05
pour une capitale de 12 modules (soit 17,1 %), coupe 13,3 % de la capitale.
"""
import alphabet as A
from alphabet import oct_rect, creux, d, DROITE, TOUS, BAS
from grille import U

OR, NOIR, BLANC = "#BE8A22", "#111111", "#FFFFFF"
RATIO_S, RATIO_C = 2.05 / 12, 1.60 / 12


def _panse(x0, x1, y0, y1, s, c, coins=DROITE):
    """Panse pleine à coupes 45° avec son contrepoinçon décalé parallèle."""
    ci = creux(c, s)
    return d(oct_rect(x0, y0, x1, y1, c, coins)) + d(oct_rect(x0 + s, y0 + s, x1 - s, y1 - s, ci, coins))


# ------------------------------------------------------------------ piste 1
def ligature_verticale(cap=19.0, c_haut=OR, c_bas=NOIR):
    """« Le Totem » : P sur G, fût commun. Vertical = l'ascension."""
    s, c = cap * RATIO_S, cap * RATIO_C
    larg = cap * 0.58
    h_p = cap * 0.40          # panse du P
    y_g = cap * 0.56          # haut de la panse du G
    g = [f'<path d="{d([(0, 0), (s, 0), (s, cap), (0, cap)])}" fill="{c_bas}"/>']
    g.append(f'<path d="{_panse(0, larg, 0, h_p, s, c)}" fill="{c_haut}" fill-rule="evenodd"/>')
    # panse basse en G : ouverture à droite + barre
    y_bar = (y_g + cap) / 2 - s * 0.55
    ouv = d([(larg - s, y_g + c), (larg, y_g + c), (larg, y_bar), (larg - s, y_bar)])
    g.append(f'<path d="{_panse(0, larg, y_g, cap, s, c)}{ouv}" fill="{c_bas}" fill-rule="evenodd"/>')
    g.append(f'<path d="{d([(larg / 2, y_bar), (larg, y_bar), (larg, y_bar + s), (larg / 2, y_bar + s)])}" fill="{c_bas}"/>')
    return "".join(g), larg, cap


# ------------------------------------------------------------------ piste 2
def ligature_horizontale(cap=14.0, c_p=OR, c_g=NOIR, jeu=0.55):
    """« Le Lien » : P et G imbriqués, séparés par un jeu de découpe."""
    s, c = cap * RATIO_S, cap * RATIO_C
    w_p, w_g = cap * 0.74, cap * 0.80
    dx = w_p - s * 1.6                       # recouvrement
    # G d'abord (dessous), évidé là où le P le croise
    ci = creux(c, s)
    y_bar = cap / 2 - s * 0.55
    ouv = d([(w_g - s, c), (w_g, c), (w_g, y_bar), (w_g - s, y_bar)])
    gg = (d(oct_rect(0, 0, w_g, cap, c, TOUS)) + d(oct_rect(s, s, w_g - s, cap - s, ci, TOUS)) + ouv)
    barre = d([(w_g / 2, y_bar), (w_g, y_bar), (w_g, y_bar + s), (w_g / 2, y_bar + s)])
    # masque : le P plus son jeu, soustrait du G
    masque = _panse(-jeu, w_p + jeu, -jeu, cap * 0.58 + jeu, s + 2 * jeu, c + jeu)
    g = [f'<g transform="translate({dx * U:.3f} 0)">'
         f'<mask id="mg"><rect x="-20" y="-20" width="{(w_g + 40) * U}" height="{(cap + 40) * U}" fill="white"/>'
         f'<path d="{masque}" fill="black" fill-rule="evenodd" transform="translate({-dx * U:.3f} 0)"/></mask>'
         f'<g mask="url(#mg)"><path d="{gg}" fill="{c_g}" fill-rule="evenodd"/>'
         f'<path d="{barre}" fill="{c_g}"/></g></g>']
    g.append(f'<path d="{d([(0, 0), (s, 0), (s, cap), (0, cap)])}" fill="{c_p}"/>')
    g.append(f'<path d="{_panse(0, w_p, 0, cap * 0.58, s, c)}" fill="{c_p}" fill-rule="evenodd"/>')
    return "".join(g), dx + w_g, cap


# ------------------------------------------------------------------ piste 3
def marches(cap=11.0, monte=4.4, c_p=OR, c_g=NOIR):
    """« L'Ascension » : le G au départ, le P une marche plus haut. Sortir du lot."""
    s, c = cap * RATIO_S, cap * RATIO_C
    ci = creux(c, s)
    w_g, w_p = cap * 0.80, cap * 0.74
    y_bar = cap / 2 - s * 0.55
    ouv = d([(w_g - s, c), (w_g, c), (w_g, y_bar), (w_g - s, y_bar)])
    gg = d(oct_rect(0, 0, w_g, cap, c, TOUS)) + d(oct_rect(s, s, w_g - s, cap - s, ci, TOUS)) + ouv
    barre = d([(w_g / 2, y_bar), (w_g, y_bar), (w_g, y_bar + s), (w_g / 2, y_bar + s)])
    g = [f'<g transform="translate(0 {monte * U:.3f})">'
         f'<path d="{gg}" fill="{c_g}" fill-rule="evenodd"/><path d="{barre}" fill="{c_g}"/></g>']
    dx = w_g + cap * 0.16
    g.append(f'<g transform="translate({dx * U:.3f} 0)">'
             f'<path d="{d([(0, 0), (s, 0), (s, cap), (0, cap)])}" fill="{c_p}"/>'
             f'<path d="{_panse(0, w_p, 0, cap * 0.58, s, c)}" fill="{c_p}" fill-rule="evenodd"/></g>')
    return "".join(g), dx + w_p, cap + monte


# ------------------------------------------------------------------ piste 4
def anneau_brise(cote=17.0, c_anneau=NOIR, c_p=OR):
    """« La Brèche » : le P perce l'anneau par le haut. Sortir du lot, littéralement."""
    s, c = cote * RATIO_S * 1.15, cote * RATIO_C
    ci = creux(c, s)
    cap_p = cote * 0.72
    sp, cp_ = cap_p * RATIO_S, cap_p * RATIO_C
    w_p = cap_p * 0.74
    x_p = (cote - w_p) / 2 - sp * 0.2
    y_p = -cote * 0.17
    # brèche : la fente par où passe le fût du P
    fente = d([(x_p - 0.55, -2), (x_p + sp + 0.55, -2), (x_p + sp + 0.55, s + 1.2), (x_p - 0.55, s + 1.2)])
    y_bar = cote / 2 - s * 0.5
    ouv = d([(cote - s, c), (cote, c), (cote, y_bar), (cote - s, y_bar)])
    anneau = (d(oct_rect(0, 0, cote, cote, c, TOUS)) + d(oct_rect(s, s, cote - s, cote - s, ci, TOUS))
              + fente + ouv)
    barre = d([(cote * 0.55, y_bar), (cote, y_bar), (cote, y_bar + s), (cote * 0.55, y_bar + s)])
    g = [f'<path d="{anneau}" fill="{c_anneau}" fill-rule="evenodd"/>',
         f'<path d="{barre}" fill="{c_anneau}"/>',
         f'<g transform="translate({x_p * U:.3f} {y_p * U:.3f})">'
         f'<path d="{d([(0, 0), (sp, 0), (sp, cap_p), (0, cap_p)])}" fill="{c_p}"/>'
         f'<path d="{_panse(0, w_p, 0, cap_p * 0.58, sp, cp_)}" fill="{c_p}" fill-rule="evenodd"/></g>']
    return "".join(g), cote, cote - y_p


PISTES = {"1 — Le Totem (P sur G, fut commun)": ligature_verticale,
          "2 — Le Lien (P et G imbriques)": ligature_horizontale,
          "3 — L'Ascension (le P une marche plus haut)": marches,
          "4 — La Breche (le P perce l'anneau)": anneau_brise}
