"""Le logo POGBUS GROUP : symbole + mot, en plusieurs assemblages."""
import math
from grille import U
from alphabet import mot, H, oct_rect, creux, d, DROITE

OR = "#D4A02C"
NOIR = "#0A0A0A"
BLANC = "#FFFFFF"


def symbole(fut=2.6, panse_h=7.2, panse_l=10.4, coupe=3.0, c_fut=NOIR, c_panse=OR):
    """Le P-emblème : fût pleine hauteur, panse à coupes 45°, contrepoinçon décalé parallèle."""
    ci = creux(coupe, fut)
    g = f'<path d="{d([(0, 0), (fut, 0), (fut, H), (0, H)])}" fill="{c_fut}"/>'
    ext = oct_rect(fut, 0, panse_l, panse_h, coupe, DROITE)
    inn = oct_rect(fut, fut, panse_l - fut, panse_h - fut, ci, DROITE)
    g += f'<path d="{d(ext)}{d(inn)}" fill="{c_panse}" fill-rule="evenodd"/>'
    return g, panse_l


def bloc_horizontal(c_mot=NOIR, c_fut=NOIR, c_panse=OR, coupe_mot=1.8, s_mot=2.05,
                    cap=7.6, ecart=2.8, baseline="GROUP", c_base=None):
    """Symbole à gauche, POGBUS à droite, GROUP en dessous. Unités : modules du symbole."""
    sym, sym_l = symbole(c_fut=c_fut, c_panse=c_panse)
    k = cap / H                                    # échelle du mot
    gmot, w_mot = mot("POGBUS", s=s_mot, c=coupe_mot, appro=1.45, couleur=c_mot)
    w_mot_r = w_mot * k
    x_mot = sym_l + ecart
    y_mot = 0.0                                    # haut du mot aligné sur le haut du symbole

    parts = [f'<g>{sym}</g>',
             f'<g transform="translate({x_mot * U:.3f} {y_mot * U:.3f}) scale({k:.5f})">{gmot}</g>']

    # ligne de base : GROUP, interlettré, calé sur la largeur du mot
    if baseline:
        cap_b = 2.05
        kb = cap_b / H
        # approche calculée pour que GROUP occupe exactement la largeur de POGBUS
        _, w0 = mot(baseline, s=2.6, c=1.2, appro=0.0)
        n = len(baseline) - 1
        appro_b = ((w_mot_r / kb) - w0) / n
        gbase, _ = mot(baseline, s=2.6, c=1.2, appro=appro_b, couleur=c_base or c_mot)
        y_b = cap + 1.75
        parts.append(f'<g transform="translate({x_mot * U:.3f} {y_b * U:.3f}) scale({kb:.5f})">{gbase}</g>')
        bas = y_b + cap_b
    else:
        bas = cap

    larg = x_mot + w_mot_r
    haut = max(H, bas)
    return "".join(parts), larg, haut


def svg_bloc(inner, larg, haut, marge=1.6, fond=None):
    w, h = (larg + 2 * marge) * U, (haut + 2 * marge) * U
    f = f'<rect width="{w:.2f}" height="{h:.2f}" fill="{fond}"/>' if fond else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}">'
            f'{f}<g transform="translate({marge * U:.2f} {marge * U:.2f})">{inner}</g></svg>')


def mot_bicolore(texte="POGBUS", s=2.05, c=1.6, appro=1.45,
                 c_corps=NOIR, c_fut=None, c_panse=OR):
    """Le mot, dont la première lettre (P) est bicolore : fût corps + panse accent.

    C'est l'emblème rejoué à l'échelle du mot — pas un second P ajouté à côté.
    """
    from alphabet import LETTRES, CRENAGE
    parts, x = [], 0.0
    for i, ch in enumerate(texte):
        chemins, w = LETTRES[ch](s, c)
        if i == 0:
            fut, panse = chemins[0], chemins[1]
            parts.append(f'<path d="{fut[0]}" fill="{c_fut or c_corps}" fill-rule="{fut[1]}" '
                         f'transform="translate({x * U:.3f} 0)"/>')
            parts.append(f'<path d="{panse[0]}" fill="{c_panse}" fill-rule="{panse[1]}" '
                         f'transform="translate({x * U:.3f} 0)"/>')
        else:
            for dd, regle in chemins:
                parts.append(f'<path d="{dd}" fill="{c_corps}" fill-rule="{regle}" '
                             f'transform="translate({x * U:.3f} 0)"/>')
        x += w + (appro + CRENAGE.get((ch, texte[i + 1]), 0.0) if i < len(texte) - 1 else 0)
    return "".join(parts), x


def bloc_integre(c_corps=NOIR, c_panse=OR, coupe_mot=1.6, s_mot=2.05,
                 baseline="GROUP", ecart_base=1.6, cap_base=2.05):
    """POGBUS avec le P bicolore, GROUP interlettré dessous, calé sur la largeur."""
    gmot, w = mot_bicolore(s=s_mot, c=coupe_mot, c_corps=c_corps, c_panse=c_panse)
    parts = [gmot]
    haut = H
    if baseline:
        kb = cap_base / H
        _, w0 = mot(baseline, s=2.6, c=1.0, appro=0.0)
        appro_b = ((w / kb) - w0) / (len(baseline) - 1)
        gb, _ = mot(baseline, s=2.6, c=1.0, appro=appro_b, couleur=c_corps)
        y_b = H + ecart_base
        parts.append(f'<g transform="translate(0 {y_b * U:.3f}) scale({kb:.5f})">{gb}</g>')
        haut = y_b + cap_base
    return "".join(parts), w, haut
