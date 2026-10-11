"""Génère tous les fichiers POGBUS : mot horizontal (validé), emblème PG, verrouillage vertical."""
import pathlib, cairosvg
import monogramme as M
import final as F
from grille import U

OR, NOIR, BLANC = F.OR, F.NOIR, F.BLANC
D = pathlib.Path("../livraison")

CAP_EMBLEME, RECOUVRE, JEU = 16.0, 0.30, 0.52
# En monochrome, la couleur ne sépare plus les deux lettres : le P se lit « F ».
# On réduit alors le recouvrement pour que chaque lettre reste entière.
RECOUVRE_MONO, JEU_MONO = 0.08, 0.80
HAUT_EMBLEME, ECART = 26.0, 5.4        # dans le verrouillage vertical, en modules du mot


def embleme(c_p=OR, c_g=NOIR):
    mono = (c_p == c_g)
    return M.monogramme(CAP_EMBLEME, CAP_EMBLEME,
                        recouvre=RECOUVRE_MONO if mono else RECOUVRE,
                        jeu=JEU_MONO if mono else JEU, c_p=c_p, c_g=c_g)


def tuile(c_fond=NOIR, c_p=OR, c_g=BLANC):
    mono = (c_p == c_g)
    return M.ecusson(cap=13.0, c_fond=c_fond, c_p=c_p, c_g=c_g,
                     recouvre=RECOUVRE_MONO if mono else RECOUVRE,
                     jeu=JEU_MONO if mono else JEU)


def vertical(corps=NOIR, accent=OR, c_g=None):
    gm, wm, hm = embleme(accent, c_g if c_g is not None else corps)
    gw, ww, hw = F.logo(corps, accent)
    k = HAUT_EMBLEME / hm
    dx = (ww - wm * k) / 2
    g = (f'<g transform="translate({dx*U:.3f} 0) scale({k:.5f})">{gm}</g>'
         f'<g transform="translate(0 {(HAUT_EMBLEME + ECART)*U:.3f})">{gw}</g>')
    return g, ww, HAUT_EMBLEME + ECART + hw


VERSIONS = {
    # le mot seul — validé, inchangé
    "logo_couleur":             lambda: F.logo(NOIR, OR),
    "logo_blanc_sur_fonce":     lambda: F.logo(BLANC, OR),
    "logo_noir":                lambda: F.logo(NOIR, NOIR),
    "logo_blanc":               lambda: F.logo(BLANC, BLANC),
    # verrouillage vertical : emblème + mot
    "vertical_couleur":         lambda: vertical(NOIR, OR),
    "vertical_blanc_sur_fonce": lambda: vertical(BLANC, OR),
    "vertical_noir":            lambda: vertical(NOIR, NOIR),
    "vertical_blanc":           lambda: vertical(BLANC, BLANC),
    # emblème seul
    "embleme_PG_couleur":       lambda: embleme(OR, NOIR),
    "embleme_PG_sur_fonce":     lambda: embleme(OR, BLANC),
    "embleme_PG_noir":          lambda: embleme(NOIR, NOIR),
    "embleme_PG_blanc":         lambda: embleme(BLANC, BLANC),
    # avatar
    "embleme_tuile_sur_noir":   lambda: tuile(NOIR, OR, BLANC),
    "embleme_tuile_sur_or":     lambda: tuile(OR, NOIR, NOIR),
    # le P seul (favicon, marque de page)
    "symbole_P_or":             lambda: F.symbole(OR),
    "symbole_P_noir":           lambda: F.symbole(NOIR),
    "symbole_P_blanc":          lambda: F.symbole(BLANC),
}

PNG = {"logo_couleur": 3000, "logo_blanc_sur_fonce": 3000, "logo_noir": 3000,
       "vertical_couleur": 2400, "vertical_blanc_sur_fonce": 2400, "vertical_noir": 2400,
       "embleme_PG_couleur": 1600, "embleme_PG_sur_fonce": 1600, "embleme_PG_noir": 1600,
       "embleme_tuile_sur_noir": 1200, "symbole_P_or": 1200, "symbole_P_noir": 1200}


def planche():
    """Planche de présentation : le verrouillage vertical, fond clair et fond sombre."""
    L, Ht = 1600, 2000
    MI = Ht / 2
    p = [f'<rect width="{L}" height="{MI}" fill="{BLANC}"/>',
         f'<rect y="{MI}" width="{L}" height="{MI}" fill="{NOIR}"/>']
    for haut, corps in ((0, NOIR), (MI, BLANC)):
        g, w, h = vertical(corps, OR)
        largeur = 820
        k = largeur / (w * U)
        x, y = (L - largeur) / 2, haut + (MI - h * U * k) / 2 - 40
        p.append(f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.5f})">{g}</g>')
        p.append(f'<text x="{L/2}" y="{haut + MI * 0.925:.0f}" text-anchor="middle" '
                 f'font-family="DejaVu Sans" font-size="21" letter-spacing="5" fill="#8A8A8A">'
                 f'{"FOND CLAIR" if corps == NOIR else "FOND SOMBRE"}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {Ht}">' + "".join(p) + "</svg>"


if __name__ == "__main__":
    D.mkdir(parents=True, exist_ok=True)
    for nom, fab in VERSIONS.items():
        g, w, h = fab()
        svg = F.fichier(g, w, h)
        (D / f"pogbus_{nom}.svg").write_text(svg)
        if nom in PNG:
            cairosvg.svg2png(bytestring=svg.encode(), write_to=str(D / f"pogbus_{nom}.png"),
                             output_width=PNG[nom])
        print(f"  {nom:28s} {w*U:7.1f} x {h*U:6.1f}")
    cairosvg.svg2png(bytestring=planche().encode(),
                     write_to=str(D / "POGBUS_presentation_vertical.png"), output_width=1600)
    print("\nplanche verticale écrite")
