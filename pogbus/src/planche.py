"""Planche de contact : chaque piste sur fond blanc et sur fond noir, en 3 tailles."""
import sys, pathlib
import cairosvg
from grille import U
import symboles as S

OR, NOIR, BLANC = S.OR, S.NOIR, "#FFFFFF"
B = 12 * U   # cote de la boite symbole


def bloc(fn, fond, corps, accent, x, y, taille, legende=None):
    k = taille / B
    g = f'<g transform="translate({x} {y}) scale({k:.4f})">{fn(corps, accent)}</g>'
    if legende:
        g += (f'<text x="{x}" y="{y + taille + 26}" font-family="DejaVu Sans" font-size="15" '
              f'fill="{"#FFFFFF" if fond == NOIR else "#111111"}">{legende}</text>')
    return g


def planche(sortie="../out/pistes.png"):
    L, lig = 1500, 430
    parts = []
    for i, (nom, fn) in enumerate(S.PISTES.items()):
        y0 = i * lig
        # moitie gauche : fond blanc / moitie droite : fond noir
        parts.append(f'<rect x="0" y="{y0}" width="{L/2}" height="{lig}" fill="{BLANC}"/>')
        parts.append(f'<rect x="{L/2}" y="{y0}" width="{L/2}" height="{lig}" fill="{NOIR}"/>')
        parts.append(f'<text x="30" y="{y0 + 40}" font-family="DejaVu Sans" font-size="22" '
                     f'font-weight="bold" fill="#111">PISTE {nom}</text>')
        for j, t in enumerate((220, 110, 48)):
            xs = [40, 320, 480][j]
            parts.append(bloc(fn, BLANC, NOIR, OR, xs, y0 + 80, t, f"{t}px"))
            parts.append(bloc(fn, NOIR, BLANC, OR, L/2 + xs, y0 + 80, t, f"{t}px"))
        # version tout noir / tout blanc (monochrome)
        parts.append(bloc(fn, BLANC, NOIR, NOIR, 620, y0 + 80, 150, "mono noir"))
        parts.append(bloc(fn, NOIR, BLANC, BLANC, L/2 + 620, y0 + 80, 150, "mono blanc"))
        # version or pleine
        parts.append(bloc(fn, BLANC, OR, OR, 820, y0 + 80, 150, "or plein"))
        parts.append(bloc(fn, NOIR, OR, OR, L/2 + 620 + 200, y0 + 80, 150, "or plein"))
    h = lig * len(S.PISTES)
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {h}" width="{L}" height="{h}">'
         + "".join(parts) + "</svg>")
    p = pathlib.Path(sortie); p.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=s.encode(), write_to=str(p), output_width=L * 2)
    print("écrit", p, p.stat().st_size // 1024, "Ko")


if __name__ == "__main__":
    planche(*sys.argv[1:])
