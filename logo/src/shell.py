"""Gabarit commun des pages du dossier (A4 paysage, 1123 × 794 px)."""
from brand import NUIT, ACIER, CUIVRE, CUIVRE_CLAIR, CUIVRE_TEXTE, SIGNAL, BETON, CHAUX, BLANC, font_css

_FONTS = font_css()

BASE_CSS = f"""
{_FONTS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1123px;height:794px}}
body{{font-family:Manrope;color:{NUIT};-webkit-font-smoothing:antialiased}}
.page{{width:1123px;height:794px;position:relative;overflow:hidden;padding:54px 64px}}
.light{{background:{CHAUX}}} .dark{{background:{NUIT};color:{CHAUX}}}
.folio{{position:absolute;left:64px;right:64px;bottom:30px;display:flex;justify-content:space-between;
  font:400 9.5px Mono;letter-spacing:2.2px;text-transform:uppercase;color:#6b7480}}
.dark .folio{{color:#7c8896}}
.light .kicker,.light .num{{color:{CUIVRE_TEXTE}!important}}
.kicker{{font:500 11px Mono;letter-spacing:3px;text-transform:uppercase;color:{CUIVRE}}}
h1{{font:600 40px/1.08 Sora;letter-spacing:-1px}}
h2{{font:600 26px/1.15 Sora;letter-spacing:-.5px}}
h3{{font:600 15px/1.3 Sora;letter-spacing:-.1px}}
p{{font-size:13.5px;line-height:1.62;color:#3a4553}}
.dark p{{color:#aeb7c2}}
.serif{{font-family:InstrumentSerif;font-style:italic;font-weight:400}}
.mono{{font-family:Mono}}
.rule{{width:44px;height:3px;background:{CUIVRE};margin:18px 0}}
.num{{font:500 11px Mono;color:{CUIVRE};letter-spacing:1px}}
"""


def page_shell(inner, n, title, theme="light", extra_css=""):
    folio = (f'<div class="folio"><span>CivRebar AI — Manuel d\'identité</span>'
             f'<span>{title}</span><span>{n:02d}</span></div>') if n else ""
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head>
<body><div class="page {theme}">{inner}{folio}</div></body></html>"""
