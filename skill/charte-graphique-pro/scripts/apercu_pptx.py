"""Aperçu d'un .pptx simple (textes, formes, images recadrées, fonds) rendu en PNG via HTML + Chromium.
Sert quand LibreOffice est absent ou incomplet (fréquent en environnement cloud).

    python3 apercu_pptx.py deck.pptx dossier_sortie/

Les polices sont celles installées sur le système : convertir d'abord les .woff2 de la marque
en .ttf dans ~/.fonts (voir references/pieges.md), sinon Chromium les remplace.
Gérés : couleurs RVB et couleurs de thème, polices/tailles héritées (repli : sans-serif, 18 pt),
ancrage et alignement, images recadrées (srcRect), fonds unis et images.
Limites, signalées sur stderr : groupes, tableaux et graphiques ne sont pas rendus ; une zone
de texte n'a qu'un style (celui de son premier run).
Aperçu fidèle pour les mises en page simples ; ce n'est pas le rendu exact de PowerPoint.
Dépendances : pip install python-pptx ; node + playwright ; rendu_png.js à côté de ce script."""
import base64
import os
import pathlib
import subprocess
import sys

from lxml import etree
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.util import Emu

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PX = 96  # px par pouce
TAILLE_PAR_DEFAUT = 18  # pt, valeur PowerPoint quand rien n'est précisé
# clrMap standard : tx1/bg1/tx2/bg2 désignent dk1/lt1/dk2/lt2 dans le thème
ALIAS = {"tx1": "dk1", "bg1": "lt1", "tx2": "dk2", "bg2": "lt2"}
ALIGN = {1: "left", 2: "center", 3: "right", 4: "justify"}
ANCRAGE = {"t": "flex-start", "ctr": "center", "b": "flex-end"}


def avertir(msg):
    print(f"attention : {msg}", file=sys.stderr)


def px(v):
    return Emu(v or 0).inches * PX


def couleur(c, theme):
    """Élément de couleur DrawingML (srgbClr, sysClr, schemeClr) → '#RRGGBB' ou None."""
    if c is None:
        return None
    tag = etree.QName(c).localname
    if tag == "srgbClr":
        return "#" + c.get("val")
    if tag == "sysClr":
        return "#" + c.get("lastClr", "000000")
    if tag == "schemeClr":
        return theme.get(ALIAS.get(c.get("val"), c.get("val")))
    return None


def remplissage(parent, theme):
    """Couleur du premier a:solidFill directement contenu dans parent (spPr, ln, rPr…)."""
    sf = parent.find(f"{A}solidFill") if parent is not None else None
    return couleur(sf[0], theme) if sf is not None and len(sf) else None


def charger_theme(prs):
    """Couleurs du thème du premier masque : {'dk1': '#…', 'accent1': '#…', …}."""
    try:
        part = prs.slide_masters[0].part.part_related_by(RT.THEME)
    except KeyError:
        return {}
    scheme = etree.fromstring(part.blob).find(f".//{A}clrScheme")
    if scheme is None:
        return {}
    return {etree.QName(el).localname: couleur(el[0], {}) for el in scheme if len(el)}


def image_html(sh, box, w, h):
    """Image, recadrée comme dans PowerPoint (srcRect en millièmes de pour cent)."""
    src = sh._element.find(f".//{A}srcRect")
    marges = {"l": 0.0, "t": 0.0, "r": 0.0, "b": 0.0}
    if src is not None:
        marges = {k: int(src.get(k, 0)) / 100000 for k in marges}
    l, t, r, b = marges["l"], marges["t"], marges["r"], marges["b"]
    # taille de l'image complète telle qu'elle s'afficherait avant recadrage
    fw, fh = w / max(1 - l - r, 0.01), h / max(1 - t - b, 0.01)
    data = base64.b64encode(sh.image.blob).decode()
    return (f'<div style="{box}overflow:hidden">'
            f'<img style="position:absolute;left:{-l * fw:.2f}px;top:{-t * fh:.2f}px;'
            f'width:{fw:.2f}px;height:{fh:.2f}px" src="data:{sh.image.content_type};base64,{data}"></div>')


def slide_html(prs, slide, numero, theme):
    W, H = px(prs.slide_width), px(prs.slide_height)
    bg = ""
    fond = slide._element.find(f".//{P}bg")
    if fond is not None:
        blip = fond.find(f".//{A}blip")
        if blip is not None:
            part = slide.part.related_part(blip.get(f"{R}embed"))
            data = base64.b64encode(part.blob).decode()
            bg = f"background:url(data:{part.content_type};base64,{data}) 0 0/100% 100%;"
        else:
            sf = fond.find(f".//{A}solidFill")  # p:bg > p:bgPr > a:solidFill
            couleur_fond = couleur(sf[0], theme) if sf is not None and len(sf) else None
            if couleur_fond:
                bg = f"background:{couleur_fond};"
    out = []
    for sh in slide.shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            avertir(f"diapo {numero} : groupe ignoré, son contenu n'est pas rendu")
            continue
        if getattr(sh, "has_table", False) or getattr(sh, "has_chart", False):
            avertir(f"diapo {numero} : tableau ou graphique non rendu")
            continue
        x, y, w, h = px(sh.left), px(sh.top), px(sh.width), px(sh.height)
        box = f"position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;"
        if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
            out.append(image_html(sh, box, w, h))
            continue
        sp = sh._element
        spPr = sp.find(f"{P}spPr")
        prst = sp.find(f".//{A}prstGeom")
        geom = prst.get("prst") if prst is not None else "rect"
        fill = remplissage(spPr, theme)
        ln = spPr.find(f"{A}ln") if spPr is not None else None
        line = remplissage(ln, theme) if ln is not None else None
        lw = int(ln.get("w", 12700)) / 12700 * 96 / 72 if ln is not None else 0
        if geom == "line":
            out.append(f'<div style="position:absolute;left:{x}px;top:{y - lw / 2}px;width:{w}px;'
                       f'height:{lw}px;background:{line or "#000000"}"></div>')
        elif not sh.has_text_frame or not sh.text_frame.text.strip() or fill:
            rad = "50%" if geom == "ellipse" else ("8px" if geom == "roundRect" else "0")
            b = f"border:{lw}px solid {line};" if line else ""
            out.append(f'<div style="{box}background:{fill or "transparent"};border-radius:{rad};{b}box-sizing:border-box"></div>')
        if sh.has_text_frame and sh.text_frame.text.strip():
            tf = sh.text_frame
            run = next((r for p in tf.paragraphs for r in p.runs), None)
            if run is None:  # zone réduite à un champ (numéro de page…) : rien de mesurable
                continue
            f = run.font
            rpr = run._r.find(f"{A}rPr")
            col = remplissage(rpr, theme) or "#000000"
            spc = int(rpr.get("spc", 0)) / 100 if rpr is not None else 0
            al = tf.paragraphs[0].alignment
            align = ALIGN.get(int(al) if al else 1, "left")
            bodypr = tf._txBody.find(f"{A}bodyPr")
            anchor = bodypr.get("anchor", "t") if bodypr is not None else "t"
            jc = ANCRAGE.get(anchor, "flex-start")  # « just » et « dist » : repli en haut
            m = [px(v) for v in (tf.margin_top, tf.margin_right, tf.margin_bottom, tf.margin_left)]
            txt = tf.text.replace("&", "&amp;").replace("<", "&lt;").replace("\n", "<br>").replace("\x0b", "<br>")
            famille = f.name.strip() if f.name and f.name.strip() else "sans-serif"
            taille = f.size.pt if f.size is not None else TAILLE_PAR_DEFAUT
            out.append(
                f'<div style="{box}display:flex;flex-direction:column;justify-content:{jc};padding:{m[0]}px {m[1]}px {m[2]}px {m[3]}px;'
                f'box-sizing:border-box">'
                f'<div style="font-family:\'{famille}\';font-size:{taille * 96 / 72}px;line-height:1.2;'
                f'font-weight:{700 if f.bold else 400};font-style:{"italic" if f.italic else "normal"};color:{col};'
                f'letter-spacing:{spc * 96 / 72}px;text-align:{align}">{txt}</div></div>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0}}'
            f'body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;{bg}}}</style></head><body>{"".join(out)}</body></html>')


def main(pptx_path, out_dir):
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    prs = Presentation(pptx_path)
    theme = charger_theme(prs)
    W, H = round(px(prs.slide_width)), round(px(prs.slide_height))
    jobs = []
    for i, s in enumerate(prs.slides, 1):
        f = out / f"slide-{i:02d}.html"
        f.write_text(slide_html(prs, s, i, theme), encoding="utf-8")
        jobs.append(f"{f}|{out / f'slide-{i:02d}.png'}|{W}|{H}")
    env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"], text=True).strip())
    subprocess.run(["node", str(pathlib.Path(__file__).parent / "rendu_png.js"), *jobs], check=True, env=env)
    print("ok", len(jobs))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage : python3 apercu_pptx.py deck.pptx dossier_sortie/")
    main(*sys.argv[1:3])
