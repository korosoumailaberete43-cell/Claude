"""Logotypes CivRebar AI en SVG 100 % vectoriel (texte converti en tracés)."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

from brand import FONTS, NUIT, CUIVRE, SIGNAL, CHAUX, mark

_fonts = {}


def _font(weight):
    if weight not in _fonts:
        _fonts[weight] = TTFont(FONTS / f"sora-latin-{weight}-normal.woff2")
    return _fonts[weight]


def text_path(text, weight, size, tracking=0.0):
    """Renvoie (d, largeur) : le texte en un seul tracé, ligne de base à y=0.
    tracking en fraction de la taille (0.18 = 180/1000 em)."""
    f = _font(weight)
    upm = f["head"].unitsPerEm
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    s = size / upm
    x = 0.0
    parts = []
    for i, ch in enumerate(text):
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(pen)
        d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({x:.2f} 0) scale({s:.5f} {-s:.5f})" d="{d}"/>')
        x += hmtx[g][0] * s
        if i < len(text) - 1:
            x += tracking * size
    return "".join(parts), x


def cap_height(weight, size):
    f = _font(weight)
    gs = f.getGlyphSet()
    bp = BoundsPen(gs)
    gs[f.getBestCmap()[ord("H")]].draw(bp)
    return bp.bounds[3] * size / f["head"].unitsPerEm


def _inner_mark(bar, relevee, noeud):
    """Contenu du symbole sans la balise <svg>, dans son repère 5 10 240 240."""
    s = mark(bar, relevee, noeud)
    return s[s.index(">") + 1: s.rindex("</svg>")]


def logo_horizontal(bar=NUIT, text=NUIT, accent=CUIVRE, noeud=SIGNAL, bg=None):
    """Symbole + CIVREBAR | AI. Hauteur du symbole = 240 u."""
    size = 118
    ch = cap_height(600, size)
    d1, w1 = text_path("CIVREBAR", 600, size, 0.16)
    d2, w2 = text_path("AI", 300, size, 0.12)
    gap_mark = 44        # espace symbole → texte
    gap_bar = 38         # espace texte → filet → AI
    tx = 240 + gap_mark
    base = 130 + ch / 2  # texte centré optiquement sur le symbole
    bar_x = tx + w1 + gap_bar
    ai_x = bar_x + 3 + gap_bar
    W = ai_x + w2 + 6
    back = f'<rect width="{W:.0f}" height="240" fill="{bg}"/>' if bg else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 240">{back}
<g transform="translate(-5 -10)">{_inner_mark(bar, accent, noeud)}</g>
<g fill="{text}" transform="translate({tx:.2f} {base:.2f})">{d1}</g>
<rect x="{bar_x:.2f}" y="{base - ch - 6:.2f}" width="3" height="{ch + 12:.2f}" fill="{accent}"/>
<g fill="{accent}" transform="translate({ai_x:.2f} {base:.2f})">{d2}</g>
</svg>""", W, 240


def logo_vertical(bar=NUIT, text=NUIT, accent=CUIVRE, noeud=SIGNAL, bg=None):
    """Symbole centré au-dessus de CIVREBAR, puis AI sous un filet."""
    size = 70
    ch = cap_height(600, size)
    d1, w1 = text_path("CIVREBAR", 600, size, 0.16)
    d2, w2 = text_path("AI", 300, 44, 0.3)
    ch2 = cap_height(300, 44)
    W = max(w1, 180) + 40
    mx = (W - 180) / 2
    y1 = 180 + 56 + ch
    y_rule = y1 + 34
    y2 = y_rule + 30 + ch2
    H = y2 + 20
    back = f'<rect width="{W:.0f}" height="{H:.0f}" fill="{bg}"/>' if bg else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}">{back}
<g transform="translate({mx:.2f} 0) scale(0.75) translate(-5 -10)">{_inner_mark(bar, accent, noeud)}</g>
<g fill="{text}" transform="translate({(W - w1) / 2:.2f} {y1:.2f})">{d1}</g>
<rect x="{W / 2 - 40:.2f}" y="{y_rule:.2f}" width="80" height="3" fill="{accent}"/>
<g fill="{accent}" transform="translate({(W - w2) / 2:.2f} {y2:.2f})">{d2}</g>
</svg>""", W, H


def symbol(bar=NUIT, accent=CUIVRE, noeud=SIGNAL, bg=None, rx=48):
    back = f'<rect x="5" y="10" width="240" height="240" rx="{rx}" fill="{bg}"/>' if bg else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="5 10 240 240">{back}{_inner_mark(bar, accent, noeud)}</svg>"""


if __name__ == "__main__":
    import pathlib
    out = pathlib.Path(__file__).resolve().parent.parent / "out"
    h, *_ = logo_horizontal()
    v, *_ = logo_vertical()
    hd, *_ = logo_horizontal(bar=CHAUX, text=CHAUX)
    html = f"""<html><body style="margin:0;background:#ddd">
<div style="background:{CHAUX};padding:40px">{h.replace('<svg ', '<svg width="900" ')}</div>
<div style="background:{NUIT};padding:40px">{hd.replace('<svg ', '<svg width="900" ')}</div>
<div style="background:{CHAUX};padding:40px">{v.replace('<svg ', '<svg width="560" ')}</div></body></html>"""
    (out / "lockup_test.html").write_text(html)
