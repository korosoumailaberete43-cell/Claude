"""Step by Step Academy — palette, variantes du logo remasterisé, polices."""
import base64
import pathlib

import logo as L

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"

# ---------------------------------------------------------------- Palette
NOIR = "#111111"        # Noir fondateur
OR = "#F5C518"          # Or excellence (logo, grands aplats, accents)
IVOIRE = "#FAF7F0"      # Ivoire — fond principal de la charte et des documents
SABLE = "#EFE8D8"       # Sable — surfaces claires secondaires
GRAPHITE = "#2A2A2A"    # Graphite — surfaces sombres secondaires
VERT = "#5DB12E"        # Vert réussite — validation uniquement
BLANC = "#FFFFFF"
# couleurs de TEXTE sur fond clair (contraste ≥ 4,5:1)
OR_TEXTE = "#8A6A00"    # Or bronze
VERT_TEXTE = "#437F21"
GRIS = "#5E5A52"        # texte secondaire chaud

# ---------------------------------------------------------------- Variantes de couleur du logo
THEMES = {
    "clair":  dict(texte=NOIR, or_=OR, vert=VERT),          # sur ivoire / blanc — version principale
    "sombre": dict(texte=BLANC, or_=OR, vert=VERT),         # sur noir / graphite
    "noir":   dict(texte="#000000", or_="#000000", vert="#000000"),   # monochrome (tampon, fax, gravure)
    "blanc":  dict(texte=BLANC, or_=BLANC, vert=BLANC),     # monochrome inversé (sur photo, sur or)
}

VB_PRINCIPAL = (125, 73, 982, 1083)      # logo complet, marge incluse
VB_SYMBOLE = (125, 73, 982, 737)         # toque + fil + marches + coche, sans le nom
VB_COMPACT = (230, 78.5, 827, 827)       # marches + coche, carré (icône, favicon)


def _svg(vb, body, bg=None, rx=0):
    x, y, w, h = vb
    back = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}">{back}{body}</svg>'


def principal(theme="clair", bg=None, detail=True):
    p = L.parts(**THEMES[theme], detail=detail)
    return _svg(VB_PRINCIPAL, p["fil"] + p["marches"] + p["coche"] + p["toque"] + p["texte"] + p["extras"], bg)


def symbole(theme="clair", bg=None):
    p = L.parts(**THEMES[theme])
    return _svg(VB_SYMBOLE, p["fil"] + p["marches"] + p["coche"] + p["toque"], bg)


def compact(theme="clair", bg=None, rx=0):
    p = L.parts(**THEMES[theme])
    return _svg(VB_COMPACT, p["marches"] + p["coche"], bg, rx)


def horizontal(theme="clair", bg=None):
    """Déclinaison d'usage pour bandeaux et en-têtes : symbole à gauche, nom à droite.
    Aucun élément n'est redessiné, seuls les blocs sont réarrangés."""
    p = L.parts(**THEMES[theme], detail=False)
    sx, sy, sw, sh = VB_SYMBOLE
    tx0, ty0, tw, th = 178, 772, 916, 275          # bloc texte d'origine (Step By Step + ACADEMY)
    s = sh * 0.56 / th                             # le nom occupe 56 % de la hauteur du symbole
    gap = 70
    ox = sx + sw + gap - tx0 * s
    oy = sy + (sh - th * s) / 2 + 40 - ty0 * s     # centré optiquement sur les marches
    W = sw + gap + tw * s + 30
    body = (p["fil"] + p["marches"] + p["coche"] + p["toque"]
            + f'<g transform="translate({ox:.2f} {oy:.2f}) scale({s:.4f})">{p["texte"]}</g>')
    return _svg((sx, sy, W, sh), body, bg)


def sized(svg, w=None, h=None):
    attrs = (f'width="{w}" ' if w else "") + (f'height="{h}" ' if h else "")
    return svg.replace("<svg ", f"<svg {attrs}", 1)


def inner(svg):
    return svg[svg.index(">") + 1: svg.rindex("</svg>")]


# ---------------------------------------------------------------- Polices
FONT_SPECS = [
    ("Quicksand", "quicksand-latin-400-normal.woff2", 400, "normal"),
    ("Quicksand", "quicksand-latin-500-normal.woff2", 500, "normal"),
    ("Quicksand", "quicksand-latin-600-normal.woff2", 600, "normal"),
    ("Quicksand", "quicksand-latin-700-normal.woff2", 700, "normal"),
    ("Comfortaa", "comfortaa-latin-300-normal.woff2", 300, "normal"),
    ("Comfortaa", "comfortaa-latin-400-normal.woff2", 400, "normal"),
    ("Comfortaa", "comfortaa-latin-700-normal.woff2", 700, "normal"),
    ("Nunito", "nunito-latin-400-normal.woff2", 400, "normal"),
    ("Nunito", "nunito-latin-400-italic.woff2", 400, "italic"),
    ("Nunito", "nunito-latin-600-normal.woff2", 600, "normal"),
    ("Nunito", "nunito-latin-700-normal.woff2", 700, "normal"),
    ("Nunito", "nunito-latin-800-normal.woff2", 800, "normal"),
]


def font_css():
    out = []
    for fam, f, wt, st in FONT_SPECS:
        b = base64.b64encode((FONTS / f).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b}) format('woff2');"
                   f"font-weight:{wt};font-style:{st}}}")
    return "\n".join(out)


def contrast_ratio(a, b):
    """Contraste WCAG 2.1 entre deux couleurs hex."""
    def lum(h):
        c = [int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)
