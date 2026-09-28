"""Pack Step by Step Academy : logos (SVG/PDF/EPS/PNG/JPEG), favicons, charte fusionnée, modèles."""
import os
import pathlib
import shutil
import subprocess

import cairosvg
from pypdf import PdfWriter

from brand import *
from exporter_logo import exporter, elargir, favicons
from pages_b import attestation_html, ATT_CSS

PACK = ROOT / "pack"
M = 67  # zone de protection : une marche


def fond(svg, couleur, marge):
    """Version avec fond plein intégré et marge de protection."""
    import re
    svg = elargir(svg, marge)
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    x, y, w, h = m.groups()
    i = svg.index(">") + 1
    return svg[:i] + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{couleur}"/>' + svg[i:]


def main():
    for sub in ("01_Logo_principal", "02_Symbole_et_icone", "03_Versions_sur_fond", "04_Documents"):
        if (PACK / sub).exists():
            shutil.rmtree(PACK / sub)
    jpeg_bg = {"clair": BLANC, "sombre": NOIR, "noir": BLANC, "blanc": NOIR}

    d1 = PACK / "01_Logo_principal"
    for th in THEMES:
        exporter(principal(th), d1, f"StepByStep_logo_principal_{th}", jpeg_bg[th], 1800, M)
        exporter(horizontal(th), d1, f"StepByStep_logo_horizontal_{th}", jpeg_bg[th], 2400, M)
        if th in ("clair", "sombre"):
            exporter(principal(th, detail=False), d1, f"StepByStep_logo_principal_sans_tildes_ni_livre_{th}", jpeg_bg[th], 1800, M)

    d2 = PACK / "02_Symbole_et_icone"
    for th in THEMES:
        exporter(symbole(th), d2, f"StepByStep_symbole_{th}", jpeg_bg[th], 2000, M)
    icone = compact("clair", bg=NOIR, rx=150)
    exporter(icone, d2, "StepByStep_icone_application", NOIR, 1024, 0)
    exporter(compact("clair"), d2, "StepByStep_marches_seules_clair", BLANC, 1024, M)
    favicons(icone, icone, d2 / "favicons")

    d3 = PACK / "03_Versions_sur_fond"
    for nom, bg, th in [("ivoire", IVOIRE, "clair"), ("blanc", BLANC, "clair"), ("noir", NOIR, "sombre"),
                        ("graphite", GRAPHITE, "sombre"), ("or", OR, "noir")]:
        exporter(fond(principal(th), bg, 2 * M), d3, f"StepByStep_logo_sur_fond_{nom}", bg, 1800, 0)
        exporter(fond(horizontal(th), bg, M), d3, f"StepByStep_horizontal_sur_fond_{nom}", bg, 2400, 0)

    d4 = PACK / "04_Documents"
    d4.mkdir(parents=True)
    wr = PdfWriter()
    for f in sorted((ROOT / "out" / "pages").glob("page_*.pdf")):
        wr.append(str(f))
    wr.add_metadata({"/Title": "Step by Step Academy — Charte graphique", "/Author": "Step by Step Academy"})
    with open(d4 / "StepByStep_Academy_Charte_graphique.pdf", "wb") as fh:
        wr.write(fh)
    shutil.copy(ROOT / "mockups" / "PROMPTS_ChatGPT.md", d4 / "StepByStep_Prompts_mises_en_situation.md")
    # exemple d'attestation en image (sert au prompt 04)
    html = ROOT / "out" / "attestation_exemple.html"
    html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{font_css()}*{{margin:0;padding:0;box-sizing:border-box}}'
                    f'body{{width:842px;height:595px;font-family:Nunito}}{ATT_CSS}</style></head><body>{attestation_html()}</body></html>', encoding="utf-8")
    env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"], text=True).strip())
    subprocess.run(["node", str(pathlib.Path(__file__).parent / "render_png.js"),
                    f"{html}|{d4 / 'Exemple_attestation.png'}|842|595"], check=True, env=env)

    d6 = PACK / "06_Modeles_bureautiques"
    if (ROOT / "out" / "office").exists():
        d6.mkdir(exist_ok=True)
        for f in (ROOT / "out" / "office").glob("*.*x"):
            shutil.copy(f, d6 / f.name)

    d7 = PACK / "07_Mises_en_situation"
    imgs = sorted((ROOT / "mockups" / "images").glob("0*_*.jpg")) if (ROOT / "mockups" / "images").exists() else []
    if imgs:
        shutil.rmtree(d7, ignore_errors=True)
        d7.mkdir()
        for f in imgs:
            shutil.copy(f, d7 / f"StepByStep_{f.name}")
    shutil.copy(ROOT / "LISEZ-MOI.txt", PACK / "LISEZ-MOI.txt")
    print("ok")


if __name__ == "__main__":
    main()
