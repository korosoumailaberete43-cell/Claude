"""Le P de POGBUS : panse à coupes 45°, contrepoinçon = vrai décalage parallèle de la panse.

La forme intérieure est la forme extérieure, décalée vers l'intérieur d'une épaisseur de fût.
C'est la définition géométrique de la transmission : ce qui est dedans a la forme de ce qui l'engendre.
"""
import math
from grille import U

R2 = math.sqrt(2)


def _d(pts):
    return "M" + "L".join(f"{x * U:.4f} {y * U:.4f}" for x, y in pts) + "Z"


def panse(x0, x1, y0, y1, c):
    """Rectangle à coupes 45° sur les deux coins de droite. c = longueur de coupe."""
    demi = (y1 - y0) / 2
    c = min(c, demi)
    return [(x0, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1 - c), (x1 - c, y1), (x0, y1)]


def lettre(fut=2.6, h=12.0, panse_h=7.2, panse_l=10.4, coupe=2.52,
           c_fut="#0A0A0A", c_panse="#D4A02C", jeu=0.0):
    x0 = fut + jeu
    ext = panse(0.0, panse_l, 0.0, panse_h, coupe)
    # contrepoinçon : décalage parallèle de « fut » vers l'intérieur
    ci = max(coupe - fut * (2 - R2), 0.0)
    inn = panse(x0, panse_l - fut, fut, panse_h - fut, ci)
    g = f'<path d="{_d([(0,0),(fut,0),(fut,h),(0,h)])}" fill="{c_fut}"/>'
    g += f'<path d="{_d(ext)}{_d(inn)}" fill="{c_panse}" fill-rule="evenodd"/>'
    return g, ci


if __name__ == "__main__":
    import pathlib, cairosvg
    OR, NOIR, BLANC = "#D4A02C", "#0A0A0A", "#FFFFFF"
    essais = [("coupe 1.8", 1.8), ("coupe 2.2", 2.2), ("coupe 2.52 (pointe interieure)", 2.52),
              ("coupe 3.0", 3.0), ("coupe 3.6 (pointe exterieure)", 3.6)]
    col, lig = 560, 300
    parts, h = [], lig * len(essais)
    for i, (t, c) in enumerate(essais):
        y0 = i * lig
        parts.append(f'<rect x="0" y="{y0}" width="{col}" height="{lig}" fill="{BLANC}"/>')
        parts.append(f'<rect x="{col}" y="{y0}" width="{col}" height="{lig}" fill="{NOIR}"/>')
        g, ci = lettre(coupe=c)
        parts.append(f'<text x="22" y="{y0+30}" font-family="DejaVu Sans" font-size="18" '
                     f'font-weight="bold" fill="#111">{t} — contre {ci:.2f}</text>')
        for fond, dx, corps in ((BLANC, 0, NOIR), (NOIR, col, BLANC)):
            x = dx + 26
            for taille in (170, 80, 40):
                k = taille / (12 * U)
                gg, _ = lettre(coupe=c, c_fut=corps, c_panse=OR)
                parts.append(f'<g transform="translate({x} {y0+60}) scale({k:.4f})">{gg}</g>')
                x += taille * 0.95 + 46
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {col*2} {h}" '
         f'width="{col*2}" height="{h}">' + "".join(parts) + "</svg>")
    p = pathlib.Path("../out/coupes.png"); p.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=s.encode(), write_to=str(p), output_width=col * 4)
    print("écrit", p)
