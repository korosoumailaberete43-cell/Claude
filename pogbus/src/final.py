"""POGBUS GROUP — logo définitif.

Système : une seule règle de forme (tout angle droit ou coupé à 45°), une seule
construction de lettre. Le symbole n'est pas un signe ajouté à côté du mot :
c'est le P du mot, isolé. Même grille, même graisse, même coupe.

Grille : hauteur de capitale H = 12 modules, graisse de fût s = 2.05,
coupe à 45° c = 1.60 sur les contours extérieurs.
"""
import pathlib
from grille import U
from alphabet import LETTRES, CRENAGE, mot, H

OR = "#BE8A22"      # or POGBUS — 3.1:1 sur blanc, 6.5:1 sur noir
NOIR = "#111111"
BLANC = "#FFFFFF"

S_MOT, C_MOT, APPRO = 2.05, 1.60, 1.45
CAP_BASE, ECART_BASE = 3.2, 1.9


def _lettre(ch, x, couleur, accent=None):
    chemins, w = LETTRES[ch](S_MOT, C_MOT)
    out = []
    for i, (dd, regle) in enumerate(chemins):
        c = accent if (accent and ch == "P") else couleur
        out.append(f'<path d="{dd}" fill="{c}" fill-rule="{regle}" '
                   f'transform="translate({x * U:.3f} 0)"/>')
    return "".join(out), w


def symbole(couleur=OR):
    """Le P seul — identique au P du mot."""
    g, w = _lettre("P", 0, couleur)
    return g, w, H


def logo(couleur=NOIR, accent=OR, baseline=True):
    """Logo complet. Renvoie (fragment SVG, largeur, hauteur) en modules."""
    parts, x = [], 0.0
    for i, ch in enumerate("POGBUS"):
        g, w = _lettre(ch, x, couleur, accent)
        parts.append(g)
        if i < 5:
            x += w + APPRO + CRENAGE.get((ch, "POGBUS"[i + 1]), 0.0)
        else:
            x += w
    larg, haut = x, H
    if baseline:
        kb = CAP_BASE / H
        _, w0 = mot("GROUP", s=2.6, c=1.0, appro=0.0)
        ap = ((larg / kb) - w0) / 4
        gb, _ = mot("GROUP", s=2.6, c=1.0, appro=ap, couleur=couleur)
        y = H + ECART_BASE
        parts.append(f'<g transform="translate(0 {y * U:.3f}) scale({kb:.5f})">{gb}</g>')
        haut = y + CAP_BASE
    return "".join(parts), larg, haut


def fichier(inner, larg, haut, fond=None, titre="POGBUS GROUP"):
    w, h = larg * U, haut * U
    f = f'<rect width="{w:.2f}" height="{h:.2f}" fill="{fond}"/>' if fond else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
            f'width="{w:.2f}" height="{h:.2f}" role="img" aria-label="{titre}">'
            f'<title>{titre}</title>{f}{inner}</svg>')


VERSIONS = {
    "logo_couleur":        lambda: logo(NOIR, OR),
    "logo_blanc_sur_fonce": lambda: logo(BLANC, OR),
    "logo_noir":           lambda: logo(NOIR, NOIR),
    "logo_blanc":          lambda: logo(BLANC, BLANC),
    "symbole_or":          lambda: symbole(OR),
    "symbole_noir":        lambda: symbole(NOIR),
    "symbole_blanc":       lambda: symbole(BLANC),
}




def tuile(fond=NOIR, lettre=OR, cote=16.0, coupe=3.4, cap=8.6):
    """Avatar : carré à coins coupés à 45°, P centré. Même langage de forme."""
    from alphabet import oct_rect, d, TOUS
    g = f'<path d="{d(oct_rect(0, 0, cote, cote, coupe, TOUS))}" fill="{fond}"/>'
    gp, w = _lettre("P", 0, lettre)
    k = cap / H
    x = (cote - w * k) / 2
    y = (cote - cap) / 2
    g += f'<g transform="translate({x * U:.3f} {y * U:.3f}) scale({k:.5f})">{gp}</g>'
    return g, cote, cote


VERSIONS["symbole_tuile_or_sur_noir"] = lambda: tuile(NOIR, OR)
VERSIONS["symbole_tuile_noir_sur_or"] = lambda: tuile(OR, NOIR)

if __name__ == "__main__":
    dossier = pathlib.Path("../livraison"); dossier.mkdir(parents=True, exist_ok=True)
    for nom, fab in VERSIONS.items():
        g, lg, ht = fab()
        (dossier / f"pogbus_{nom}.svg").write_text(fichier(g, lg, ht))
        print(f"{nom:24s} {lg * U:7.1f} x {ht * U:6.1f}")
