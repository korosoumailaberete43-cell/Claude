"""Exporte un logo SVG en SVG + PDF + EPS + PNG + JPEG, sans rsvg-convert ni Ghostscript.

    python3 exporter_logo.py logo.svg dossier/ Nom_fichier --fond-jpeg "#FFFFFF" --png 3000 --marge 40

--marge  : zone de protection transparente ajoutée autour (unités du viewBox, 0 pour aucune)
--fond-jpeg : le JPEG n'a pas de transparence ; poser les versions blanches sur une couleur sombre

Le nom de fichier est pris tel quel : « Logo_v1.0 » donne Logo_v1.0.svg, Logo_v1.0.pdf…

Dépendances : pip install cairosvg pillow   (cairosvg utilise libcairo, présent sur la plupart des systèmes).
cairosvg.svg2eps écrit une BoundingBox correcte (contrairement à `rsvg-convert -f eps`).
"""
import argparse
import io
import pathlib
import re

import cairosvg
from PIL import Image

NOMBRE = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"


def elargir(svg, marge):
    """Ajoute `marge` de chaque côté du viewBox. Accepte virgules et espaces comme séparateurs."""
    m = re.search(rf'viewBox="\s*({NOMBRE})[\s,]+({NOMBRE})[\s,]+({NOMBRE})[\s,]+({NOMBRE})\s*"', svg)
    if not m:
        raise ValueError("SVG sans attribut viewBox : impossible d'ajouter la zone de protection")
    x, y, w, h = map(float, m.groups())
    nouveau = f'viewBox="{x - marge:g} {y - marge:g} {w + 2 * marge:g} {h + 2 * marge:g}"'
    return svg.replace(m.group(0), nouveau, 1)


def exporter(svg, dossier, nom, fond_jpeg="#FFFFFF", png=3000, marge=0):
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    if marge:
        svg = elargir(svg, marge)
    b = svg.encode()

    def fichier(ext):
        # pas de with_suffix() : il remplacerait « .0 » dans « Logo_v1.0 »
        return dossier / f"{nom}.{ext}"

    fichier("svg").write_bytes(b)
    cairosvg.svg2pdf(bytestring=b, write_to=str(fichier("pdf")))
    cairosvg.svg2eps(bytestring=b, write_to=str(fichier("eps")))
    data = cairosvg.svg2png(bytestring=b, output_width=png)
    fichier("png").write_bytes(data)
    im = Image.open(io.BytesIO(data)).convert("RGBA")
    fond = Image.new("RGBA", im.size, fond_jpeg)
    fond.alpha_composite(im)
    fond.convert("RGB").save(fichier("jpg"), quality=90, dpi=(300, 300))
    bbox = next((l for l in fichier("eps").read_text(errors="ignore").splitlines() if l.startswith("%%BoundingBox")), "?")
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
