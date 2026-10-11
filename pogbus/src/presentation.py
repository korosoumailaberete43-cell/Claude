"""Planche de présentation POGBUS GROUP — fond blanc et fond noir, format 4:5 (WhatsApp / réseaux)."""
import pathlib, cairosvg
from grille import U
from final import logo, symbole, tuile, OR, NOIR, BLANC

L, Ht = 1600, 2000
MI = Ht / 2


def placer(g, lg, ht, cx, cy, largeur):
    k = largeur / (lg * U)
    x, y = cx - largeur / 2, cy - (ht * U * k) / 2
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({k:.5f})">{g}</g>'


def planche():
    p = [f'<rect width="{L}" height="{MI}" fill="{BLANC}"/>',
         f'<rect y="{MI}" width="{L}" height="{MI}" fill="{NOIR}"/>']
    for haut, corps, fond_txt in ((0, NOIR, "#8A8A8A"), (MI, BLANC, "#8A8A8A")):
        g, lg, ht = logo(corps, OR)
        p.append(placer(g, lg, ht, L / 2, haut + MI * 0.40, 1120))
        sy, lgs, hts = symbole(OR if corps == BLANC else NOIR)
        p.append(placer(sy, lgs, hts, L / 2, haut + MI * 0.70, 92))
        p.append(f'<text x="{L/2}" y="{haut + MI * 0.845:.0f}" text-anchor="middle" '
                 f'font-family="DejaVu Sans" font-size="21" letter-spacing="5" '
                 f'fill="{fond_txt}">{"FOND CLAIR" if corps == NOIR else "FOND SOMBRE"}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {Ht}">' + "".join(p) + "</svg>"


if __name__ == "__main__":
    d = pathlib.Path("../livraison"); d.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=planche().encode(), write_to=str(d / "POGBUS_presentation.png"),
                     output_width=L)
    # PNG transparents, prêts à l'emploi
    for nom, fab, larg in (("logo_couleur", lambda: logo(NOIR, OR), 3000),
                           ("logo_blanc_sur_fonce", lambda: logo(BLANC, OR), 3000),
                           ("logo_noir", lambda: logo(NOIR, NOIR), 3000),
                           ("symbole_or", lambda: symbole(OR), 1200),
                           ("symbole_noir", lambda: symbole(NOIR), 1200),
                           ("symbole_blanc", lambda: symbole(BLANC), 1200),
                           ("tuile_or_sur_noir", lambda: tuile(NOIR, OR), 1200)):
        g, lg, ht = fab()
        from final import fichier
        cairosvg.svg2png(bytestring=fichier(g, lg, ht).encode(),
                         write_to=str(d / f"pogbus_{nom}.png"), output_width=larg)
    print("\n".join(f"{f.name:34s} {f.stat().st_size//1024:4d} Ko" for f in sorted(d.iterdir())))
