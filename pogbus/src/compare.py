"""Planche de comparaison : variantes de la lettre, fond blanc / fond noir, 3 tailles."""
import pathlib, cairosvg
from grille import U
from lettre import lettre_p

OR, NOIR, BLANC = "#D4A02C", "#0A0A0A", "#FFFFFF"
B = 12 * U


def planche(variantes, sortie, colonne=520, lig=360):
    L = colonne * 2
    parts, h = [], lig * len(variantes)
    for i, (titre, kw) in enumerate(variantes):
        y0 = i * lig
        parts.append(f'<rect x="0" y="{y0}" width="{colonne}" height="{lig}" fill="{BLANC}"/>')
        parts.append(f'<rect x="{colonne}" y="{y0}" width="{colonne}" height="{lig}" fill="{NOIR}"/>')
        parts.append(f'<text x="24" y="{y0+34}" font-family="DejaVu Sans" font-size="20" '
                     f'font-weight="bold" fill="#111">{titre}</text>')
        for fond, dx, corps in ((BLANC, 0, NOIR), (NOIR, colonne, BLANC)):
            x = dx + 30
            for t in (190, 92, 44):
                k = t / B
                a = dict(kw)
                a.setdefault("couleur", corps)
                if a.get("c_fut") == "corps": a["c_fut"] = corps
                if a.get("c_panse") == "corps": a["c_panse"] = corps
                parts.append(f'<g transform="translate({x} {y0+70}) scale({k:.4f})">{lettre_p(**a)}</g>')
                x += t * (10.2/12) + 60
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {h}" width="{L}" height="{h}">'
         + "".join(parts) + "</svg>")
    p = pathlib.Path(sortie); p.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=s.encode(), write_to=str(p), output_width=L * 2)
    print("écrit", p)


if __name__ == "__main__":
    planche([
        ("1  contrepoincon plein, coupes 45 deg",      dict(contre="plein", c_fut="corps", c_panse=OR)),
        ("2  contrepoincon fleche (ambition)",          dict(contre="fleche", c_fut="corps", c_panse=OR)),
        ("3  contrepoincon escalier (transmission)",    dict(contre="escalier", c_fut="corps", c_panse=OR)),
        ("4  fut detache : le jeu = la transmission",   dict(contre="plein", jeu=0.55, c_fut="corps", c_panse=OR)),
        ("5  monochrome, coupes accentuees",            dict(contre="plein", coupe=2.6)),
    ], "../out/variantes.png")
