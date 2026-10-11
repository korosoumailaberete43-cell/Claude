"""Proposition 2 — « LE SCEAU DE L'AUDACIEUX » : médaillon à devise au-dessus du mot."""
import complexe as C
import final as F
from grille import U

OR, NOIR, BLANC = F.OR, F.NOIR, F.BLANC
HAUT_SCEAU, ECART = 33.0, 4.6        # en modules du mot


def embleme(fond_sombre=False, petite=False):
    """fond_sombre : le médaillon s'évide, seuls les filets et la frise restent."""
    return C.sceau_devise(c_fond="none" if fond_sombre else NOIR, c_trait=OR,
                          c_p=OR, c_g=BLANC, petite_taille=petite)


def vertical(corps=NOIR, accent=OR, petite=False):
    ge, we, he = embleme(fond_sombre=(corps == BLANC), petite=petite)
    gw, ww, hw = F.logo(corps, accent)
    k = HAUT_SCEAU / he
    dx = (ww - we * k) / 2
    g = (f'<g transform="translate({dx*U:.3f} 0) scale({k:.5f})">{ge}</g>'
         f'<g transform="translate(0 {(HAUT_SCEAU + ECART)*U:.3f})">{gw}</g>')
    return g, ww, HAUT_SCEAU + ECART + hw


def planche(sortie="../out/sceau_planche.png"):
    import pathlib, cairosvg
    L, Ht = 1600, 2000
    MI = Ht / 2
    p = [f'<rect width="{L}" height="{MI}" fill="{BLANC}"/>',
         f'<rect y="{MI}" width="{L}" height="{MI}" fill="{NOIR}"/>']
    for haut, corps in ((0, NOIR), (MI, BLANC)):
        g, w, h = vertical(corps, OR)
        largeur = 760
        k = largeur / (w * U)
        x, y = (L - largeur) / 2, haut + (MI - h * U * k) / 2 - 40
        p.append(f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.5f})">{g}</g>')
        p.append(f'<text x="{L/2}" y="{haut + MI*0.93:.0f}" text-anchor="middle" '
                 f'font-family="DejaVu Sans" font-size="21" letter-spacing="5" fill="#8A8A8A">'
                 f'{"FOND CLAIR" if corps == NOIR else "FOND SOMBRE"}</text>')
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {Ht}">' + "".join(p) + "</svg>"
    pathlib.Path(sortie).parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=s.encode(), write_to=sortie, output_width=L)
    return sortie


if __name__ == "__main__":
    print("écrit", planche())
