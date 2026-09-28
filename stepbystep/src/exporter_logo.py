"""Exporte un logo SVG en SVG + PDF + EPS + PNG + JPEG, sans rsvg-convert ni Ghostscript.

    python3 exporter_logo.py logo.svg dossier/ Nom_fichier --fond-jpeg "#FFFFFF" --png 3000 --marge 40

--marge  : zone de protection transparente ajoutée autour (unités du viewBox, 0 pour aucune)
--fond-jpeg : le JPEG n'a pas de transparence ; poser les versions blanches sur une couleur sombre

Dépendances : pip install cairosvg pillow   (cairosvg utilise libcairo, présent sur la plupart des systèmes).
cairosvg.svg2eps écrit une BoundingBox correcte (contrairement à `rsvg-convert -f eps`).
"""
import argparse
import io
import pathlib
import re

import cairosvg
from PIL import Image


def elargir(svg, marge):
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    x, y, w, h = map(float, m.groups())
    return svg.replace(m.group(0), f'viewBox="{x - marge} {y - marge} {w + 2 * marge} {h + 2 * marge}"', 1)


def exporter(svg, dossier, nom, fond_jpeg="#FFFFFF", png=3000, marge=0):
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    if marge:
        svg = elargir(svg, marge)
    b = svg.encode()
    base = dossier / nom
    base.with_suffix(".svg").write_bytes(b)
    cairosvg.svg2pdf(bytestring=b, write_to=str(base.with_suffix(".pdf")))
    cairosvg.svg2eps(bytestring=b, write_to=str(base.with_suffix(".eps")))
    data = cairosvg.svg2png(bytestring=b, output_width=png)
    base.with_suffix(".png").write_bytes(data)
    im = Image.open(io.BytesIO(data)).convert("RGBA")
    fond = Image.new("RGBA", im.size, fond_jpeg)
    fond.alpha_composite(im)
    fond.convert("RGB").save(base.with_suffix(".jpg"), quality=90, dpi=(300, 300))
    bbox = next((l for l in base.with_suffix(".eps").read_text(errors="ignore").splitlines() if l.startswith("%%BoundingBox")), "?")
    return bbox


def favicons(svg_normal, svg_petit, dossier):
    """16 et 32 px depuis la version « petites tailles », le reste depuis la version normale."""
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    for s in (16, 32, 48, 64, 180, 192, 512):
        src = svg_petit if s <= 32 else svg_normal
        cairosvg.svg2png(bytestring=src.encode(), output_width=s, write_to=str(dossier / f"favicon_{s}.png"))
    ims = [Image.open(dossier / f"favicon_{s}.png") for s in (16, 32, 48)]
    # la plus grande image sert de base, les petites sont fournies telles quelles
    ims[2].save(dossier / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=ims[:2])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("dossier")
    ap.add_argument("nom")
    ap.add_argument("--fond-jpeg", default="#FFFFFF")
    ap.add_argument("--png", type=int, default=3000)
    ap.add_argument("--marge", type=float, default=0)
    a = ap.parse_args()
    print(exporter(pathlib.Path(a.svg).read_text(), a.dossier, a.nom, a.fond_jpeg, a.png, a.marge))
