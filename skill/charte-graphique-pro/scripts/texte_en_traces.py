"""Convertit un texte en tracés SVG (le logo ne dépend plus d'aucune police installée).

Utilisation comme module :
    from texte_en_traces import texte_en_traces, hauteur_capitales
    d, largeur = texte_en_traces("polices/sora-latin-600-normal.woff2", "CIVREBAR", taille=118, interlettrage=0.16)
    svg = f'<g fill="#0B1624" transform="translate(284 172)">{d}</g>'   # ligne de base à y = 0

En ligne de commande (aperçu rapide) :
    python3 texte_en_traces.py police.woff2 "MON TEXTE" 100 0.12 > texte.svg

Accepte .ttf, .otf et .woff2 (pip install fonttools brotli).
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

_cache = {}


def _police(chemin):
    if chemin not in _cache:
        _cache[chemin] = TTFont(chemin)
    return _cache[chemin]


def texte_en_traces(police, texte, taille, interlettrage=0.0):
    """Renvoie (fragment SVG, largeur). interlettrage en fraction de la taille (0.16 = +160)."""
    f = _police(police)
    upm = f["head"].unitsPerEm
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    s = taille / upm
    x, parts = 0.0, []
    for i, ch in enumerate(texte):
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(pen)
        d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({x:.2f} 0) scale({s:.5f} {-s:.5f})" d="{d}"/>')
        x += hmtx[g][0] * s
        if i < len(texte) - 1:
            x += interlettrage * taille
    return "".join(parts), x


def hauteur_capitales(police, taille):
    """Hauteur du « H » : sert à centrer optiquement le texte sur le symbole."""
    f = _police(police)
    gs = f.getGlyphSet()
    bp = BoundsPen(gs)
    gs[f.getBestCmap()[ord("H")]].draw(bp)
    return bp.bounds[3] * taille / f["head"].unitsPerEm


if __name__ == "__main__":
    police, texte, taille = sys.argv[1], sys.argv[2], float(sys.argv[3])
    inter = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
    d, w = texte_en_traces(police, texte, taille, inter)
    h = hauteur_capitales(police, taille)
    print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-h - 10:.0f} {w:.0f} {h + 30:.0f}"><g>{d}</g></svg>')
