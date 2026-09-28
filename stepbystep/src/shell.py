"""Gabarit commun des pages (A4 paysage, 1123 × 794 px)."""
from brand import NOIR, OR, IVOIRE, SABLE, GRAPHITE, OR_TEXTE, GRIS, BLANC, font_css

_FONTS = font_css()

BASE_CSS = f"""
{_FONTS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1123px;height:794px}}
body{{font-family:Nunito;color:{NOIR};-webkit-font-smoothing:antialiased}}
.page{{width:1123px;height:794px;position:relative;overflow:hidden;padding:54px 64px}}
.light{{background:{IVOIRE}}} .dark{{background:{NOIR};color:{IVOIRE}}}
.folio{{position:absolute;left:64px;right:64px;bottom:28px;display:flex;justify-content:space-between;align-items:center;
  font:700 9px Comfortaa;letter-spacing:2.4px;text-transform:uppercase;color:{GRIS}}}
.dark .folio{{color:#9C958A}}
.folio .m{{display:inline-flex;flex-direction:column;gap:1.5px;align-items:flex-end;vertical-align:middle}} .folio .m i{{display:block;height:2.5px}}
.kicker{{font:700 11px Comfortaa;letter-spacing:3px;text-transform:uppercase;color:{OR_TEXTE}}}
.dark .kicker{{color:{OR}}}
h1{{font:600 40px/1.08 Quicksand;letter-spacing:-.8px}}
h2{{font:600 25px/1.15 Quicksand;letter-spacing:-.3px}}
h3{{font:700 15px/1.3 Quicksand}}
p{{font-size:13.5px;line-height:1.62;color:#3B3832}}
.dark p{{color:#C9C2B4}}
.lab{{font:700 9.5px Comfortaa;letter-spacing:2px;text-transform:uppercase;color:{GRIS}}}
.card{{background:{BLANC};border-radius:10px}}
.or{{color:{OR_TEXTE}}} .dark .or{{color:{OR}}}
"""


def marches_mini(w=46, color=OR):
    """Petit motif des 5 marches (largeurs du logo : ×1,27 d'une marche à l'autre)."""
    ws = [296, 385, 491, 620, 767]
    return "".join(f'<i style="width:{w * x / 767:.1f}px;background:{color}"></i>' for x in ws)


def page_shell(inner, n, title, theme="light", extra_css=""):
    folio = (f'<div class="folio"><span>Step by Step Academy — Charte graphique</span>'
             f'<span>{title}</span><span style="display:flex;align-items:center;gap:10px"><span class="m">{marches_mini(34)}</span><b>{n:02d}</b></span></div>') if n else ""
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head>
<body><div class="page {theme}">{inner}{folio}</div></body></html>"""
