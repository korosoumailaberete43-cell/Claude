"""Pages 1 à 4 : couverture, manifeste, symbole décodé, construction cotée."""
from brand import *
from lockup import logo_horizontal, symbol, _inner_mark
from shell import page_shell

MAGENTA = "#E0249A"


def sized(svg, w=None, h=None):
    attrs = (f'width="{w}" ' if w else "") + (f'height="{h}" ' if h else "")
    return svg.replace("<svg ", f"<svg {attrs}", 1)


# ------------------------------------------------------------ 1. Couverture
def p01():
    h, *_ = logo_horizontal(bar=CHAUX, text=CHAUX)
    # grande trame de ferraillage en filigrane
    lines = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="794" />' for x in range(40, 1123, 56))
    inner = f"""
<svg class="trame" width="1123" height="794"><g stroke="{ACIER}" stroke-width="1">{lines}</g>
  <line x1="0" y1="610" x2="1123" y2="610" stroke="{ACIER}" stroke-width="10"/>
  <line x1="0" y1="640" x2="1123" y2="640" stroke="{ACIER}" stroke-width="10"/></svg>
<div class="ghost">{sized(symbol(bar="#13233A", accent="#162840", noeud="#162840"), w=620)}</div>
<div class="k kicker">Manuel d'identité de marque · Édition 1.0 · 2026</div>
<div class="lg">{sized(h, w=560)}</div>
<div class="tag serif">L'intelligence de l'armature.</div>
<div class="sub">Logiciel de ferraillage assisté pour AutoCAD — poutres, poteaux, dalles, semelles, escaliers.</div>
"""
    css = f"""
.trame{{position:absolute;inset:0;opacity:.55}}
.ghost{{position:absolute;right:-70px;top:40px;opacity:.9}}
.k{{position:absolute;left:72px;top:64px}}
.lg{{position:absolute;left:72px;top:300px}}
.tag{{position:absolute;left:74px;top:480px;font-size:40px;color:{CUIVRE_CLAIR}}}
.sub{{position:absolute;left:74px;bottom:62px;font:400 13px Manrope;color:#8d99a8;letter-spacing:.2px}}
"""
    return page_shell(inner, 0, "", "dark", css)


# ------------------------------------------------------------ 2. Manifeste
def p02():
    inner = f"""
<div class="kicker">01 — Le manifeste</div>
<div class="wrap">
  <div class="left">
    <h1 class="big">Ce qui tient<br>un ouvrage<br><span style="color:{CUIVRE}">ne se voit pas.</span></h1>
    <div class="rule"></div>
    <p class="serif quote">« Comme une armature, CivRebar se construit barre après barre. »</p>
  </div>
  <div class="right">
    <p class="lead">Sous le béton, il y a l'armature. Une fois le coulage fait, plus personne ne la voit. Pourtant, c'est elle qui porte tout : les charges, les efforts, le temps.</p>
    <p>Chaque barre y est choisie, pliée, placée et ligaturée avec méthode. Rien n'y est décoratif. Tout y est calculé. C'est cette rigueur silencieuse que CivRebar AI veut mettre entre les mains de l'ingénieur et du dessinateur.</p>
    <p>Le projet commence petit, et c'est voulu : un AutoLISP qui dessine le ferraillage d'une poutre à partir de ses paramètres. Puis les poteaux, les dalles, les semelles, les escaliers. Puis une boîte à outils. Puis un vrai plugin AutoCAD. Puis une intelligence qui vérifie, quantifie et dialogue avec les logiciels de calcul.</p>
    <p>Une intelligence qui <b>assiste</b>, sans jamais remplacer, celui qui signe le plan. C'est la promesse de la marque, et c'est exactement ce que raconte son symbole.</p>
    <div class="vals">
      <div><span class="num">01</span><h3>Rigueur</h3><p>Chaque trait respecte les règles de l'art.</p></div>
      <div><span class="num">02</span><h3>Progression</h3><p>On construit par étapes, sur du solide.</p></div>
      <div><span class="num">03</span><h3>Assistance</h3><p>L'IA sert l'ingénieur, jamais l'inverse.</p></div>
    </div>
  </div>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:400px 1fr;gap:56px;margin-top:34px}}
.big{{font-size:50px;line-height:1.02;letter-spacing:-1.6px}}
.quote{{font-size:23px;line-height:1.3;color:{NUIT}}}
.lead{{font:500 17px/1.55 Manrope;color:{NUIT};margin-bottom:14px}}
.right p{{margin-bottom:11px}}
.vals{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:22px;padding-top:20px;border-top:1px solid #d9d4ca}}
.vals h3{{margin:6px 0 4px}} .vals p{{font-size:12px;line-height:1.5;margin:0}}
"""
    return page_shell(inner, 2, "Manifeste", "light", css)


# ------------------------------------------------------------ 3. Le symbole décodé
def p03():
    m = _inner_mark(CHAUX, CUIVRE, SIGNAL)
    # pastilles numérotées + lignes de rappel (repère du symbole 5 10 240 240)
    callouts = [
        (1, 50, 190, -10, 190),
        (2, 175, 90, 260, 60),
        (3, 96, 116, 30, 60),
        (4, 160, 200, 260, 170),
        (5, 100, 140, 260, 125),
    ]
    marks = ""
    for n, x, y, lx, ly in callouts:
        marks += (f'<line x1="{x}" y1="{y}" x2="{lx}" y2="{ly}" stroke="{BETON}" stroke-width="0.8" stroke-dasharray="3 3"/>'
                  f'<circle cx="{lx}" cy="{ly}" r="9" fill="{CUIVRE}"/>'
                  f'<text x="{lx}" y="{ly + 3.6}" text-anchor="middle" font-family="Mono" font-size="10" fill="{NUIT}" font-weight="500">{n}</text>')
    items = [
        ("La barre longitudinale", "Le fût du R. La colonne vertébrale de l'ouvrage : l'ingénieur, sa méthode, sa responsabilité."),
        ("L'étrier façonné", "La panse du R. Il ceinture et confine : ce sont les règles de l'art et les normes qui encadrent chaque décision."),
        ("Le crochet à 135°", "L'ancrage réglementaire des étriers. Un détail que seuls les gens du métier remarquent : la marque parle leur langue."),
        ("La barre relevée à 45°", "La jambe du R, en cuivre. En béton armé, elle reprend l'effort tranchant. Ici, elle part vers l'avant : le projet qui avance étape par étape."),
        ("Le nœud Signal", "La barre tenue dans le crochet. L'IA est au cœur de l'armature, tenue et guidée par l'ingénierie. Jamais à sa place."),
    ]
    lst = "".join(f'<div class="it"><span class="pin">{i + 1}</span><div><h3>{t}</h3><p>{d}</p></div></div>'
                  for i, (t, d) in enumerate(items))
    inner = f"""
<div class="kicker">02 — L'histoire du symbole</div>
<h1 style="margin-top:10px;color:{CHAUX}">Un R façonné comme une vraie armature.</h1>
<div class="wrap">
  <svg class="sym" viewBox="-30 10 310 240">{m}{marks}</svg>
  <div class="list">{lst}</div>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:470px 1fr;gap:40px;margin-top:30px;align-items:center}}
.sym{{width:470px;height:364px}}
.it{{display:flex;gap:14px;padding:11px 0;border-bottom:1px solid #1f2f42}}
.it:last-child{{border:0}}
.pin{{flex:none;width:22px;height:22px;border-radius:50%;background:{CUIVRE};color:{NUIT};font:500 11px/22px Mono;text-align:center}}
.it h3{{color:{CHAUX};margin-bottom:3px}} .it p{{font-size:12.5px;line-height:1.5}}
"""
    return page_shell(inner, 3, "Le symbole", "dark", css)


# ------------------------------------------------------------ 4. Construction cotée
def p04():
    g = ""
    for v in range(-20, 271, 10):
        wgt = 0.6 if v % 20 == 0 else 0.3
        g += f'<line x1="{v}" y1="0" x2="{v}" y2="270" stroke="#d6d1c7" stroke-width="{wgt}"/>'
    for v in range(0, 271, 10):
        wgt = 0.6 if v % 20 == 0 else 0.3
        g += f'<line x1="-20" y1="{v}" x2="270" y2="{v}" stroke="#d6d1c7" stroke-width="{wgt}"/>'
    M = MAGENTA
    cons = f"""
<g fill="none" stroke="{M}" stroke-width="0.9" stroke-dasharray="4 3">
  <circle cx="100" cy="90" r="50"/><circle cx="120" cy="100" r="60"/><circle cx="100" cy="140" r="20"/>
  <line x1="50" y1="0" x2="50" y2="236"/><line x1="-20" y1="160" x2="262" y2="160"/>
  <line x1="-20" y1="230" x2="262" y2="230"/><line x1="-20" y1="40" x2="262" y2="40"/>
  <line x1="120" y1="160" x2="200" y2="240"/>
</g>
<g stroke="{M}" stroke-width="1.1">
  <path d="M96 90h8M100 86v8"/><path d="M116 100h8M120 96v8"/><path d="M96 140h8M100 136v8"/>
</g>
<path d="M150 160 A30 30 0 0 1 141.2 181.2" fill="none" stroke="{M}" stroke-width="1.1"/>
"""
    def pill(x, y, t):
        w = 6 + 4.3 * len(t)
        return (f'<rect x="{x - w / 2}" y="{y - 5.5}" width="{w}" height="11" rx="5.5" fill="{M}"/>'
                f'<text x="{x}" y="{y + 2.5}" text-anchor="middle" font-family="Mono" font-size="7" fill="#fff">{t}</text>')
    dims = f"""
<g stroke="{NUIT}" stroke-width="0.8">
  <line x1="40" y1="258" x2="210" y2="258"/><line x1="40" y1="253" x2="40" y2="263"/><line x1="210" y1="253" x2="210" y2="263"/><line x1="40" y1="241" x2="60" y2="241"/>
  <line x1="-8" y1="30" x2="-8" y2="230"/><line x1="-14" y1="30" x2="-2" y2="30"/><line x1="-14" y1="230" x2="-2" y2="230"/>
</g>
{pill(125, 258, "8,5x")}{pill(-8, 130, "10x")}
{pill(75, 64, "R 2,5x")}{pill(182, 100, "R 3x")}{pill(100, 172, "r 1x")}
{pill(163, 176, "45°")}{pill(128, 118, "135°")}{pill(76, 241, "Ø = x")}
"""
    rows = [("Module x", "Ø de la barre"), ("Hauteur totale", "10x"), ("Largeur totale", "8,5x"),
            ("Coude supérieur", "R 2,5x (à l'axe)"), ("Panse (étrier)", "R 3x (à l'axe)"), ("Crochet", "r 1x · retour 135°"),
            ("Barre relevée", "45° · palier 1,5x"), ("Nœud Signal", "Ø 0,7x, centré sur le crochet"),
            ("Jeu fût / crochet", "0,5x")]
    tbl = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    inner = f"""
<div class="kicker">03 — Construction</div>
<div class="wrap">
  <div>
    <h1 style="margin-top:10px;font-size:33px">Tracé sur une grille,<br>pas dessiné à l'œil.</h1>
    <div class="rule"></div>
    <p>Toutes les mesures sont exprimées en modules <b>x</b>, où x est le diamètre de la barre. Le symbole se reproduit ainsi à l'identique, de l'icône de 16 px à la bâche de chantier.</p>
    <table>{tbl}</table>
  </div>
  <svg class="plan" viewBox="-30 -5 300 275">
    <rect x="-30" y="-5" width="300" height="275" fill="#fff"/>{g}
    <g opacity=".9">{_inner_mark(NUIT, CUIVRE, SIGNAL)}</g>{cons}{dims}
  </svg>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:340px 1fr;gap:44px}}
.plan{{width:630px;height:578px;margin-top:-8px;border:1px solid #d9d4ca}}
table{{margin-top:16px;border-collapse:collapse;width:100%;font-size:12px}}
td{{padding:6px 0;border-bottom:1px solid #ddd8ce}} td:first-child{{color:#6b7684}}
td:last-child{{font-family:Mono;font-size:11px;text-align:right;color:{NUIT}}}
"""
    return page_shell(inner, 4, "Construction", "light", css)


PAGES = [p01, p02, p03, p04]
