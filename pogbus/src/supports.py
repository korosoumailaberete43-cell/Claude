"""Deux planches à envoyer : le nuancier des versions, et le guide des supports."""
import pathlib, cairosvg
import final as F, livrer as L
from grille import U

OR, NOIR, BLANC = F.OR, F.NOIR, F.BLANC
GRIS, GRIS_T = "#F2F0EC", "#8A8A8A"
D = pathlib.Path("../livraison")


def poser(g, w, h, bx, by, bw, bh, part=0.78):
    """Centre un logo dans une boîte, à « part » de sa largeur ou de sa hauteur."""
    k = min(bw * part / (w * U), bh * part / (h * U))
    x = bx + (bw - w * U * k) / 2
    y = by + (bh - h * U * k) / 2
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({k:.5f})">{g}</g>'


def txt(s, x, y, taille=15, fill=GRIS_T, poids="normal", ancre="middle", esp=2.4):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{ancre}" font-family="DejaVu Sans" '
            f'font-size="{taille}" font-weight="{poids}" letter-spacing="{esp}" fill="{fill}">{s}</text>')


# ------------------------------------------------------------------ planche 1
def versions():
    L_, pad = 1600, 60
    titre_h, panneau_h, lig = 30, 210, 310
    lignes = [
        ("LOGO VERTICAL", lambda c: L.vertical(c, OR), lambda c: L.vertical(c, c)),
        ("LOGO HORIZONTAL", lambda c: F.logo(c, OR), lambda c: F.logo(c, c)),
        ("EMBLEME PG", lambda c: L.embleme(OR, c), lambda c: L.embleme(c, c)),
        ("LE P SEUL", lambda c: F.symbole(OR if c == BLANC else NOIR), lambda c: F.symbole(c)),
    ]
    h = 120 + lig * len(lignes) + 20
    p = [f'<rect width="{L_}" height="{h}" fill="{BLANC}"/>',
         txt("POGBUS GROUP", L_ / 2, 58, 27, NOIR, "bold", 7),
         txt("LES VERSIONS DU LOGO", L_ / 2, 88, 14, GRIS_T, "normal", 5)]
    col = (L_ - 2 * pad) / 3
    for i, (nom, couleur, mono) in enumerate(lignes):
        y0 = 120 + i * lig
        yp = y0 + titre_h
        p.append(txt(nom, pad, y0 + 16, 14, NOIR, "bold", ancre="start", esp=3.4))
        p.append(f'<rect x="{pad}" y="{y0+22}" width="{L_-2*pad}" height="1.5" fill="{OR}"/>')
        fonds = [(BLANC, '#E4E0D9'), (NOIR, None), (BLANC, '#E4E0D9')]
        for j, (f, trait) in enumerate(fonds):
            st = f' stroke="{trait}"' if trait else ""
            p.append(f'<rect x="{pad + j*col}" y="{yp}" width="{col}" height="{panneau_h}" fill="{f}"{st}/>')
        for j, fab in enumerate((lambda: couleur(NOIR), lambda: couleur(BLANC), lambda: mono(NOIR))):
            g, w, hh = fab()
            p.append(poser(g, w, hh, pad + j * col, yp, col, panneau_h, 0.70))
        for j, lab in enumerate(("couleur / fond clair", "couleur / fond sombre", "monochrome noir")):
            p.append(txt(lab, pad + col * (j + 0.5), yp + panneau_h + 26, 12, GRIS_T, "normal", 1.2))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L_} {h}">' + "".join(p) + "</svg>", L_


# ------------------------------------------------------------------ planche 2
def supports():
    L_, pad, cols = 1600, 50, 3
    cw = (L_ - 2 * pad) / cols
    ch = 430
    cases = [
        ("PHOTO DE PROFIL", "WhatsApp, Facebook, TikTok", "ecusson", "rond"),
        ("FAVICON / ICONE", "navigateur, application", "P", "carre_noir"),
        ("TAMPON ENCREUR", "encre unique, gravure", "embleme_mono", "rond_trait"),
        ("BANNIÈRE DE PAGE", "couverture de page", "horizontal_sombre", "banniere"),
        ("PUBLICATION CARRÉE", "Instagram, Facebook", "vertical_sombre", "carre"),
        ("STORY / REEL", "format vertical 9:16", "vertical_sombre", "story"),
        ("ENSEIGNE / FAÇADE", "panneau, vitrine, kakemono", "vertical_sombre", "enseigne"),
        ("CARTE DE VISITE", "recto, fond clair", "horizontal_clair", "carte"),
        ("EN-TÊTE DE DOCUMENT", "facture, devis, courrier", "horizontal_noir", "page"),
        ("VÊTEMENT BRODÉ", "polo, casquette, chasuble", "vertical_blanc", "textile"),
        ("COUVERTURE DE LIVRE", "édition, livret de formation", "embleme_sombre", "livre"),
        ("SIGNATURE E-MAIL", "petite taille, fond clair", "horizontal_clair", "mail"),
    ]

    def logo_de(cle):
        if cle == "ecusson":           return L.tuile(NOIR, OR, BLANC)
        if cle == "P":                 return F.symbole(OR)
        if cle == "embleme_mono":      return L.embleme(NOIR, NOIR)
        if cle == "embleme_sombre":    return L.embleme(OR, BLANC)
        if cle == "horizontal_sombre": return F.logo(BLANC, OR)
        if cle == "horizontal_clair":  return F.logo(NOIR, OR)
        if cle == "horizontal_noir":   return F.logo(NOIR, NOIR)
        if cle == "vertical_sombre":   return L.vertical(BLANC, OR)
        if cle == "vertical_blanc":    return L.vertical(BLANC, BLANC)
        return F.logo(NOIR, OR)

    NOMS = {"ecusson": "écusson PG sur noir", "P": "le P seul, or sur noir",
            "embleme_mono": "emblème PG, noir", "embleme_sombre": "emblème PG sur sombre",
            "horizontal_sombre": "horizontal, fond sombre",
            "horizontal_clair": "horizontal, couleur", "horizontal_noir": "horizontal, noir",
            "vertical_sombre": "vertical, fond sombre", "vertical_blanc": "vertical, blanc"}

    def forme(kind, x, y, w, h):
        """Le support lui-même : renvoie (fond svg, boîte utile)."""
        cx, cy = x + w / 2, y + h / 2
        if kind == "rond":
            r = min(w, h) * 0.37
            return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{NOIR}"/>',
                    (cx - r * .72, cy - r * .72, r * 1.44, r * 1.44))
        if kind == "carre_noir":
            s = min(w, h) * 0.42
            return (f'<rect x="{cx-s/2}" y="{cy-s/2}" width="{s}" height="{s}" rx="{s*0.22}" fill="{NOIR}"/>',
                    (cx - s / 2, cy - s / 2, s, s))
        if kind == "rond_trait":
            r = min(w, h) * 0.37
            return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{NOIR}" stroke-width="5"/>',
                    (cx - r * .66, cy - r * .66, r * 1.32, r * 1.32))
        if kind == "banniere":
            bw, bh = w * 0.90, h * 0.40
            return (f'<rect x="{cx-bw/2}" y="{cy-bh/2}" width="{bw}" height="{bh}" fill="{NOIR}"/>',
                    (cx - bw / 2, cy - bh / 2, bw, bh))
        if kind == "carre":
            s = min(w, h) * 0.76
            return (f'<rect x="{cx-s/2}" y="{cy-s/2}" width="{s}" height="{s}" fill="{NOIR}"/>',
                    (cx - s / 2, cy - s / 2, s, s))
        if kind == "story":
            bh2 = h * 0.84; bw2 = bh2 * 9 / 16
            return (f'<rect x="{cx-bw2/2}" y="{cy-bh2/2}" width="{bw2}" height="{bh2}" rx="10" fill="{NOIR}"/>',
                    (cx - bw2 / 2, cy - bh2 / 2, bw2, bh2))
        if kind == "enseigne":
            bw3, bh3 = w * 0.80, h * 0.62
            return (f'<rect x="{cx-bw3/2}" y="{cy-bh3/2}" width="{bw3}" height="{bh3}" fill="{NOIR}"/>'
                    f'<rect x="{cx-bw3/2}" y="{cy+bh3/2}" width="{bw3}" height="7" fill="#CFCAC2"/>',
                    (cx - bw3 / 2, cy - bh3 / 2, bw3, bh3))
        if kind == "carte":
            bw4 = w * 0.80; bh4 = bw4 * 55 / 85
            return (f'<rect x="{cx-bw4/2}" y="{cy-bh4/2}" width="{bw4}" height="{bh4}" rx="6" '
                    f'fill="{BLANC}" stroke="#D8D3CB" stroke-width="2"/>',
                    (cx - bw4 / 2, cy - bh4 / 2, bw4, bh4))
        if kind == "page":
            bh5 = h * 0.80; bw5 = bh5 * 0.707
            return (f'<rect x="{cx-bw5/2}" y="{cy-bh5/2}" width="{bw5}" height="{bh5}" '
                    f'fill="{BLANC}" stroke="#D8D3CB" stroke-width="2"/>'
                    + "".join(f'<rect x="{cx-bw5/2+18}" y="{cy-bh5/2+88+i*13}" '
                              f'width="{bw5-36-(26 if i==5 else 0)}" height="4" fill="#E6E2DA"/>' for i in range(6)),
                    (cx - bw5 / 2 + 16, cy - bh5 / 2 + 18, bw5 - 32, 58))
        if kind == "textile":
            s6 = min(w, h) * 0.62
            return (f'<rect x="{cx-s6/2}" y="{cy-s6/2}" width="{s6}" height="{s6}" rx="{s6*0.10}" fill="#232323"/>',
                    (cx - s6 * 0.34, cy - s6 * 0.30, s6 * 0.68, s6 * 0.60))
        if kind == "livre":
            bh7 = h * 0.78; bw7 = bh7 * 0.68
            return (f'<rect x="{cx-bw7/2}" y="{cy-bh7/2}" width="{bw7}" height="{bh7}" rx="3" fill="{NOIR}"/>'
                    f'<rect x="{cx-bw7/2}" y="{cy-bh7/2}" width="9" height="{bh7}" fill="#262626"/>',
                    (cx - bw7 / 2 + 14, cy - bh7 / 2 + 26, bw7 - 22, bh7 * 0.42))
        # mail
        bw8, bh8 = w * 0.84, h * 0.46
        return (f'<rect x="{cx-bw8/2}" y="{cy-bh8/2}" width="{bw8}" height="{bh8}" '
                f'fill="{BLANC}" stroke="#D8D3CB" stroke-width="2"/>'
                f'<rect x="{cx-bw8/2+16}" y="{cy-bh8/2+16}" width="{bw8*0.5}" height="4" fill="#E6E2DA"/>'
                f'<rect x="{cx-bw8/2+16}" y="{cy-bh8/2+28}" width="{bw8*0.34}" height="4" fill="#E6E2DA"/>',
                (cx - bw8 / 2 + 16, cy - bh8 / 2 + 46, bw8 * 0.52, bh8 * 0.40))

    rows = (len(cases) + cols - 1) // cols
    h = 130 + rows * ch
    p = [f'<rect width="{L_}" height="{h}" fill="{GRIS}"/>',
         txt("POGBUS GROUP", L_ / 2, 60, 27, NOIR, "bold", 7),
         txt("QUELLE VERSION SUR QUEL SUPPORT", L_ / 2, 90, 14, GRIS_T, "normal", 5)]
    for i, (nom, detail, cle, kind) in enumerate(cases):
        cx0 = pad + (i % cols) * cw
        cy0 = 130 + (i // cols) * ch
        p.append(f'<rect x="{cx0+6}" y="{cy0+6}" width="{cw-12}" height="{ch-26}" fill="{BLANC}" rx="4"/>')
        fond, (bx, by, bw, bh) = forme(kind, cx0 + 6, cy0 + 6, cw - 12, ch - 150)
        p.append(fond)
        g, w, hh = logo_de(cle)
        p.append(poser(g, w, hh, bx, by, bw, bh, 0.68 if cle == 'P' else 0.84))
        p.append(txt(nom, cx0 + cw / 2, cy0 + ch - 92, 14, NOIR, "bold", 1.9))
        p.append(txt(detail, cx0 + cw / 2, cy0 + ch - 70, 11.5, GRIS_T, "normal", 0.3))
        p.append(f'<rect x="{cx0+cw/2-26}" y="{cy0+ch-58}" width="52" height="2" fill="{OR}"/>')
        p.append(txt(NOMS.get(cle, cle), cx0 + cw / 2, cy0 + ch - 36, 12, OR, "bold", 0.3))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L_} {h}">' + "".join(p) + "</svg>", L_


if __name__ == "__main__":
    for nom, fab in (("POGBUS_versions", versions), ("POGBUS_supports", supports)):
        s, w = fab()
        cairosvg.svg2png(bytestring=s.encode(), write_to=str(D / f"{nom}.png"), output_width=w)
        print(nom, (D / f"{nom}.png").stat().st_size // 1024, "Ko")
