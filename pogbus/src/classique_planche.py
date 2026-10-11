"""Proposition 3 — la structure du logo d'origine, redessinée."""
import pathlib, cairosvg
import classique as K
from grille import U

OR, NOIR, BLANC = K.OR, K.NOIR, K.BLANC
D = pathlib.Path("../livraison_03_bonnet")


def planche():
    L, Ht = 1600, 2000
    MI = Ht / 2
    p = [f'<rect width="{L}" height="{MI}" fill="{BLANC}"/>',
         f'<rect y="{MI}" width="{L}" height="{MI}" fill="{NOIR}"/>']
    for haut, corps in ((0, NOIR), (MI, BLANC)):
        g, w, h = K.logo("bonnet", c_lettre=corps, c_accent=OR)
        largeur = 1200
        k = largeur / (w * U)
        x, y = (L - largeur) / 2, haut + (MI - h * U * k) / 2 - 30
        p.append(f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.5f})">{g}</g>')
        p.append(f'<text x="{L/2}" y="{haut + MI*0.895:.0f}" text-anchor="middle" '
                 f'font-family="DejaVu Sans" font-size="21" letter-spacing="5" fill="#8A8A8A">'
                 f'{"FOND CLAIR" if corps == NOIR else "FOND SOMBRE"}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {Ht}">' + "".join(p) + "</svg>", L


def fichiers():
    D.mkdir(parents=True, exist_ok=True)
    s, L = planche()
    cairosvg.svg2png(bytestring=s.encode(), write_to=str(D / "POGBUS_presentation.png"), output_width=L)
    for nom, corps, accent in (("couleur", NOIR, OR), ("blanc_sur_fonce", BLANC, OR),
                               ("noir", NOIR, NOIR), ("blanc", BLANC, BLANC)):
        g, w, h = K.logo("bonnet", c_lettre=corps, c_accent=accent)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w*U:.2f} {h*U:.2f}" '
               f'width="{w*U:.2f}" height="{h*U:.2f}"><title>POGBUS GROUP</title>{g}</svg>')
        (D / f"pogbus_logo_{nom}.svg").write_text(svg)
        if nom != "blanc":
            cairosvg.svg2png(bytestring=svg.encode(), write_to=str(D / f"pogbus_logo_{nom}.png"),
                             output_width=3000)
    return sorted(f.name for f in D.iterdir())


if __name__ == "__main__":
    print("\n".join(fichiers()))
