"""Fusionne le manuel et produit le pack de fichiers logo CivRebar AI."""
import io
import pathlib
import re
import shutil

import cairosvg
from PIL import Image
from pypdf import PdfWriter

from brand import NUIT, ACIER, CUIVRE, SIGNAL, CHAUX, BETON
from lockup import logo_horizontal, logo_vertical, symbol

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "out" / "pages"
PACK = ROOT / "CivRebar_AI_Pack_Logo"
W = "#FFFFFF"

COULEUR = dict()
NOIR = dict(bar="#000000", text="#000000", accent="#000000", noeud="#000000")
BLANC = dict(bar=W, text=W, accent=W, noeud=W)


def sym(bg=None, bar=NUIT, accent=CUIVRE, noeud=SIGNAL, text=None, rx=48):
    return symbol(bar=bar, accent=accent, noeud=noeud, bg=bg, rx=rx)


def with_bg(svg, bg):
    """Ajoute un fond plein (pour JPEG ou versions sur fond couleur)."""
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    x, y, w, h = m.groups()
    i = svg.index(">") + 1
    return svg[:i] + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' + svg[i:]


def pad(svg, p):
    """Élargit le viewBox d'une marge p (zone de protection dans les fichiers à fond)."""
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    x, y, w, h = map(float, m.groups())
    return svg.replace(m.group(0), f'viewBox="{x - p} {y - p} {w + 2 * p} {h + 2 * p}"', 1)


def export(svg, folder, name, jpeg_bg, png_w=3000, margin=40):
    """margin : zone de protection transparente (2x = 40 u) incluse dans le fichier."""
    folder.mkdir(parents=True, exist_ok=True)
    if margin:
        svg = pad(svg, margin)
    base = folder / name
    b = svg.encode()
    (base.with_suffix(".svg")).write_bytes(b)
    cairosvg.svg2pdf(bytestring=b, write_to=str(base.with_suffix(".pdf")))
    cairosvg.svg2eps(bytestring=b, write_to=str(base.with_suffix(".eps")))
    png = cairosvg.svg2png(bytestring=b, output_width=png_w)
    base.with_suffix(".png").write_bytes(png)
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    bg = Image.new("RGBA", im.size, jpeg_bg)
    bg.alpha_composite(im)
    bg.convert("RGB").save(base.with_suffix(".jpg"), quality=90, dpi=(300, 300))


def main():
    # ---- manuel fusionné
    docs = PACK / "04_Documents"
    if PACK.exists():
        shutil.rmtree(PACK)
    docs.mkdir(parents=True)
    wr = PdfWriter()
    for f in sorted(PAGES.glob("page_*.pdf")):
        wr.append(str(f))
    wr.add_metadata({"/Title": "CivRebar AI — Manuel d'identité de marque", "/Author": "CivRebar AI"})
    manual = docs / "CivRebar_AI_Charte_graphique.pdf"
    with open(manual, "wb") as fh:
        wr.write(fh)

    # ---- 01 logo avec nom
    d1 = PACK / "01_Logo_principal_avec_nom"
    for label, kw, jbg in [("couleur", COULEUR, W), ("noir", NOIR, W), ("blanc", BLANC, NUIT)]:
        h, *_ = logo_horizontal(**kw)
        v, *_ = logo_vertical(**kw)
        export(h, d1, f"CivRebar_AI_logo_horizontal_{label}", jbg)
        export(v, d1, f"CivRebar_AI_logo_vertical_{label}", jbg, png_w=2000)
    h, *_ = logo_horizontal(bar=CHAUX, text=CHAUX)
    export(h, d1, "CivRebar_AI_logo_horizontal_couleur_pour_fond_sombre", NUIT)

    # ---- 02 symbole seul
    d2 = PACK / "02_Symbole_seul"
    export(sym(), d2, "CivRebar_AI_symbole_couleur", W, 2000)
    export(sym(**NOIR), d2, "CivRebar_AI_symbole_noir", W, 2000)
    export(sym(**BLANC), d2, "CivRebar_AI_symbole_blanc", NUIT, 2000)
    export(sym(bar=CHAUX), d2, "CivRebar_AI_symbole_couleur_pour_fond_sombre", NUIT, 2000)
    icon = sym(bg=NUIT, bar=CHAUX, rx=52)
    export(icon, d2, "CivRebar_AI_icone_application", NUIT, 1024, margin=0)
    fav = d2 / "favicons"
    fav.mkdir()
    for s in (16, 32, 48, 64, 180, 192, 512):
        cairosvg.svg2png(bytestring=icon.encode(), output_width=s, write_to=str(fav / f"favicon_{s}.png"))
    ims = [Image.open(fav / f"favicon_{s}.png") for s in (16, 32, 48)]
    ims[0].save(fav / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=ims[1:])

    # ---- 03 versions sur fond couleur (fond intégré, marge de protection 2x = 40 u)
    d3 = PACK / "03_Versions_sur_fond_couleur"
    fonds = [
        ("fond_nuit", NUIT, dict(bar=CHAUX, text=CHAUX)),
        ("fond_acier", ACIER, dict(bar=W, text=W)),
        ("fond_cuivre", CUIVRE, dict(bar=W, text=W, accent=NUIT, noeud=W)),
        ("fond_chaux", CHAUX, dict()),
    ]
    for name, bg, kw in fonds:
        h, *_ = logo_horizontal(**kw)
        export(with_bg(pad(h, 80), bg), d3, f"CivRebar_AI_logo_{name}", bg, margin=0)
        s = sym(bar=kw.get("bar", NUIT), accent=kw.get("accent", CUIVRE), noeud=kw.get("noeud", SIGNAL))
        export(with_bg(pad(s, 40), bg), d3, f"CivRebar_AI_symbole_{name}", bg, 2000, margin=0)

    shutil.copy(ROOT / "LISEZ-MOI.txt", PACK / "LISEZ-MOI.txt")
    print("ok", manual)


if __name__ == "__main__":
    main()
