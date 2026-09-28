"""Images de fond et logos (PNG) pour le modèle PowerPoint."""
import pathlib
import cairosvg

from brand import NUIT, ACIER, CUIVRE, SIGNAL, CHAUX
from lockup import logo_horizontal, symbol

OUT = pathlib.Path(__file__).resolve().parent.parent / "out" / "pptx_assets"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 2667, 1500  # 13,333 × 7,5 in à 200 DPI


def inner(svg):
    return svg[svg.index(">") + 1: svg.rindex("</svg>")]


def trame(bars_y=None, ghost=None, step=80):
    lines = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(step // 2, W, step))
    bars = ""
    if bars_y:
        bars = "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{ACIER}" stroke-width="18"/>' for y in bars_y)
    g = ""
    if ghost:
        x, y, s = ghost
        g = (f'<g transform="translate({x} {y}) scale({s / 240}) translate(-5 -10)">'
             f'{inner(symbol(bar="#13233A", accent="#162840", noeud="#162840"))}</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="{NUIT}"/>'
            f'<g stroke="{ACIER}" stroke-width="2" opacity=".7">{lines}</g>{g}{bars}</svg>')


def png(svg, name, w=None):
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / name), output_width=w)


png(trame(bars_y=(1180, 1240), ghost=(1500, 60, 1250)), "bg_cover.png")
png(trame(bars_y=(1180, 1240)), "bg_section.png")
png(trame(ghost=(1700, 250, 1100)), "bg_quote.png")
png(logo_horizontal(bar=CHAUX, text=CHAUX)[0], "logo_dark.png", 1600)
png(logo_horizontal()[0], "logo_light.png", 1600)
png(symbol(), "symbole.png", 600)
png(symbol(bar=CHAUX), "symbole_dark.png", 600)
print("ok")
