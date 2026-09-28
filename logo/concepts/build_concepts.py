"""Planche des 3 pistes de logo CivRebar AI -> concepts.html"""
import base64, pathlib

HERE = pathlib.Path(__file__).parent
FONTS = HERE.parent / "fonts"

# Palette
BETON = "#1B2733"   # anthracite béton
ACIER = "#E8702A"   # orange acier / rouille HA
IA = "#1FB5C9"      # cyan IA
GRIS = "#8A96A3"
FOND = "#F4F2EE"


def ff(name, file, weight):
    b = base64.b64encode((FONTS / file).read_bytes()).decode()
    return f"@font-face{{font-family:'{name}';src:url(data:font/woff2;base64,{b}) format('woff2');font-weight:{weight}}}"


FONT_CSS = "".join([
    ff("SG", "space-grotesk-latin-500-normal.woff2", 500),
    ff("SG", "space-grotesk-latin-700-normal.woff2", 700),
    ff("IN", "inter-latin-400-normal.woff2", 400),
    ff("IN", "inter-latin-600-normal.woff2", 600),
])

# --- Piste A : la section de poutre (étrier + 4 barres, une barre "IA") ---
def symbol_a(c1=BETON, c2=ACIER, c3=IA):
    return f"""
<svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
  <rect x="52" y="24" width="136" height="192" rx="26" fill="none" stroke="{c1}" stroke-width="16"/>
  <path d="M83 26 L120 63 M53 56 L90 93" stroke="{c1}" stroke-width="13" stroke-linecap="round"/>
  <circle cx="77" cy="50" r="14" fill="{c2}"/>
  <circle cx="163" cy="50" r="14" fill="{c2}"/>
  <circle cx="77" cy="190" r="14" fill="{c2}"/>
  <circle cx="163" cy="190" r="14" fill="{c3}"/>
</svg>"""


# --- Piste B : monogramme "C" en étrier avec crochets à 135° + réticule AutoCAD ---
def symbol_b(c1=BETON, c2=ACIER, c3=IA):
    return f"""
<svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
  <path d="M176 64 L176 64 Q176 40 152 40 L76 40 Q40 40 40 76 L40 164 Q40 200 76 200 L152 200 Q176 200 176 176"
        fill="none" stroke="{c1}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M176 64 L150 90" stroke="{c1}" stroke-width="20" stroke-linecap="round"/>
  <path d="M176 176 L150 150" stroke="{c1}" stroke-width="20" stroke-linecap="round"/>
  <circle cx="84" cy="84" r="15" fill="{c2}"/>
  <circle cx="84" cy="156" r="15" fill="{c2}"/>
  <g stroke="{c3}" stroke-width="7" stroke-linecap="round">
    <path d="M168 120 L228 120"/><path d="M198 90 L198 150"/>
  </g>
  <rect x="188" y="110" width="20" height="20" fill="none" stroke="{c3}" stroke-width="5"/>
</svg>"""


# --- Piste C : poutre en élévation dont les étriers deviennent un réseau neuronal ---
def symbol_c(c1=BETON, c2=ACIER, c3=IA):
    xs = [44, 82, 120, 158, 196]
    stirrups = "".join(f'<path d="M{x} 70 L{x} 170" stroke="{c1}" stroke-width="12" stroke-linecap="round"/>' for x in xs)
    nodes = "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="{c2}"/>' for x in xs for y in (70, 170))
    net = f"""
  <path d="M82 70 L120 170 L158 70 L196 170" fill="none" stroke="{c3}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="120" cy="170" r="11" fill="{c3}"/><circle cx="158" cy="70" r="11" fill="{c3}"/>"""
    return f"""
<svg viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg">
  <path d="M28 70 L212 70 M28 170 L212 170" stroke="{c1}" stroke-width="16" stroke-linecap="round"/>
  {stirrups}{net}{nodes.replace(f'cx="120" cy="170" r="11" fill="{c2}"', 'r="0"').replace(f'cx="158" cy="70" r="11" fill="{c2}"', 'r="0"')}
</svg>"""


def wordmark(dark=False):
    civ = "#FFFFFF" if dark else BETON
    return (f'<div class="wm"><span style="color:{civ}">Civ</span><span style="color:{ACIER}">Rebar</span>'
            f'<span class="ai">AI</span></div>')


def card(letter, title, sym, pitch):
    return f"""
<section class="card">
  <div class="tag">Piste {letter}</div>
  <h2>{title}</h2>
  <div class="hero">
    <div class="sym">{sym()}</div>
    {wordmark()}
  </div>
  <div class="variants">
    <div class="v dark"><div class="s">{sym('#FFFFFF', ACIER, IA)}</div>{wordmark(True)}</div>
    <div class="v icon"><div class="s">{sym('#FFFFFF', '#FFFFFF', IA)}</div></div>
    <div class="v mono"><div class="s">{sym('#111', '#111', '#111')}</div></div>
  </div>
  <p>{pitch}</p>
</section>"""


html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
{FONT_CSS}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1680px;height:980px;background:{FOND};font-family:IN;color:{BETON};padding:56px 64px}}
header{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:36px}}
header h1{{font-family:SG;font-weight:700;font-size:44px;letter-spacing:-1px}}
header p{{font-size:17px;color:#5a6672;max-width:620px;text-align:right;line-height:1.45}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}}
.card{{background:#fff;border-radius:20px;padding:28px;box-shadow:0 1px 0 #e3dfd8}}
.tag{{font-family:SG;font-weight:700;color:{ACIER};text-transform:uppercase;letter-spacing:2px;font-size:14px}}
.card h2{{font-family:SG;font-weight:700;font-size:26px;margin:4px 0 18px}}
.hero{{height:330px;border:1px solid #eee9e1;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}}
.hero .sym svg{{width:190px;height:190px}}
.wm{{font-family:SG;font-weight:700;font-size:40px;letter-spacing:-1px;display:flex;align-items:center;gap:2px}}
.wm .ai{{font-size:18px;background:{IA};color:#fff;border-radius:6px;padding:3px 7px;margin-left:8px;letter-spacing:1px}}
.variants{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:12px;margin:14px 0 18px}}
.v{{height:120px;border-radius:12px;display:flex;align-items:center;justify-content:center;gap:8px}}
.v .s svg{{width:74px;height:74px}}
.v.dark{{background:{BETON}}} .v.dark .wm{{font-size:22px}} .v.dark .wm .ai{{font-size:11px;padding:2px 5px;margin-left:5px}}
.v.icon{{background:{ACIER}}} .v.mono{{background:#fff;border:1px solid #eee9e1}}
.card p{{font-size:15.5px;line-height:1.55;color:#3c4854}}
footer{{margin-top:30px;display:flex;gap:18px;align-items:center;font-size:15px;color:#5a6672}}
.sw{{display:flex;align-items:center;gap:8px}} .sw i{{width:26px;height:26px;border-radius:6px;display:inline-block}}
</style></head><body>
<header><h1>CivRebar AI — 3 pistes de logo</h1>
<p>Un logiciel de ferraillage pour AutoCAD, construit étape par étape : du premier AutoLISP poutre jusqu'au plugin assisté par l'IA.</p></header>
<div class="grid">
{card('A', 'La section armée', symbol_a, "La coupe d'une poutre : l'étrier et ses 4 barres filantes. Une des barres est en cyan : c'est l'IA, placée au cœur de la structure. Très lisible en petit (favicon, icône de menu AutoCAD).")}
{card('B', "Le C en étrier", symbol_b, "Le « C » de Civ dessiné comme un étrier, avec ses crochets à 135°. Le réticule cyan rappelle le curseur d'AutoCAD, là où l'outil dessine. C'est un vrai monogramme, idéal comme icône de plugin.")}
{card('C', 'La poutre neuronale', symbol_c, "Une poutre en élévation : les barres haute et basse et les étriers. Le tracé cyan en zigzag transforme les nœuds en réseau de neurones. Elle raconte toute la trajectoire, du ferraillage vers l'IA.")}
</div>
<footer><b style="color:{BETON}">Palette proposée</b>
<span class="sw"><i style="background:{BETON}"></i>Béton anthracite {BETON}</span>
<span class="sw"><i style="background:{ACIER}"></i>Acier HA {ACIER}</span>
<span class="sw"><i style="background:{IA}"></i>Cyan IA {IA}</span>
<span class="sw"><i style="background:{FOND};border:1px solid #ccc"></i>Blanc chaux {FOND}</span>
<span style="margin-left:auto">Typographie : Space Grotesk (logo) · Inter (textes)</span></footer>
</body></html>"""

(HERE / "concepts.html").write_text(html, encoding="utf-8")
print("ok")
