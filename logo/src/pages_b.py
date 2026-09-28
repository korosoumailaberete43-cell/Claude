"""Pages 5 à 12 : logo, protection, couleurs, typo, déclinaisons, interdits, applications, trajectoire."""
from brand import *
from lockup import logo_horizontal, logo_vertical, symbol, symbol_small, _inner_mark
from shell import page_shell
from pages_a import sized

WHITE = "#FFFFFF"


# ------------------------------------------------------------ 5. Le logo
def p05():
    h, *_ = logo_horizontal()
    v, *_ = logo_vertical()
    inner = f"""
<div class="kicker">04 — Le logo</div>
<h1 style="margin-top:10px">Trois formes, une seule signature.</h1>
<div class="grid">
  <div class="c main"><div class="lab">A · Version horizontale — principale</div>{sized(h, w=560)}
    <p>À utiliser par défaut : en-têtes, site, écran de démarrage du plugin, présentations.</p></div>
  <div class="c"><div class="lab">B · Version verticale</div>{sized(v, h=220)}
    <p>Formats carrés ou étroits : couverture, affiche, réseaux sociaux.</p></div>
  <div class="c"><div class="lab">C · Symbole seul</div>{sized(symbol(), w=170)}
    <p>Icône du plugin, favicon, avatar, tampon sur les plans.</p></div>
</div>"""
    css = f"""
.grid{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:250px 290px;gap:18px;margin-top:26px}}
.c{{background:#fff;border-radius:6px;padding:22px 26px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;position:relative}}
.c.main{{grid-column:1 / 3;flex-direction:column}}
.lab{{align-self:flex-start;font:500 10px Mono;letter-spacing:2px;text-transform:uppercase;color:#7b8591}}
.c p{{font-size:12px;text-align:center;margin:0}}
"""
    return page_shell(inner, 5, "Le logo", "light", css)


# ------------------------------------------------------------ 6. Protection & tailles minimales
def p06():
    h, W, H = logo_horizontal()
    # zone de protection = 1 hauteur de fût… ici 2x (x = 20 u) autour du logo
    pad = 40
    zone = f"""<svg viewBox="{-pad} {-pad} {W + 2 * pad} {H + 2 * pad}" width="590">
<rect x="{-pad}" y="{-pad}" width="{W + 2 * pad}" height="{H + 2 * pad}" fill="none" stroke="#E0249A" stroke-width="2" stroke-dasharray="8 6"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#E0249A" stroke-width="1" opacity=".5"/>
<g>{h[h.index('>') + 1:h.rindex('</svg>')]}</g>
{''.join(f'<rect x="{x}" y="{y}" width="40" height="40" fill="#E0249A" opacity=".18"/><text x="{x + 20}" y="{y + 25}" font-family="Mono" font-size="15" text-anchor="middle" fill="#E0249A">2x</text>' for x, y in [(-pad, -pad), (W, -pad), (-pad, H), (W, H)])}
</svg>"""
    sizes = ""
    for px in (48, 32, 24, 16):
        s = symbol() if px > 32 else symbol_small()
        sizes += f'<div class="sz">{sized(s, w=px)}<span>{px} px</span></div>'
    compare = "".join(f'<div class="sz">{sized(fn(), w=16)}<span>{lab}</span></div>'
                      for fn, lab in ((symbol, "standard"), (symbol_small, "optimisée")))
    inner = f"""
<div class="kicker">05 — Protection et tailles minimales</div>
<h1 style="margin-top:10px">Laisser respirer l'armature.</h1>
<div class="wrap">
  <div class="z">{zone}
    <p>Autour du logo, une marge vide égale à <b>2x</b> (deux diamètres de barre) doit toujours être respectée. Aucun texte, trait ni bord de page ne doit y entrer.</p>
    <div class="symz"><svg viewBox="-35 -30 320 320" width="150"><rect x="-35" y="-30" width="320" height="320" fill="none" stroke="#E0249A" stroke-width="3" stroke-dasharray="10 8"/>
      <rect x="5" y="10" width="240" height="240" fill="none" stroke="#E0249A" stroke-width="1.5" opacity=".5"/>{symbol()[symbol().index('>') + 1:symbol().rindex('</svg>')]}</svg>
      <p><b>Symbole seul :</b> marge minimale de <b>2x</b> également, mesurée depuis le carré de construction de 12x. Sur une icône d'application, le symbole occupe 70 % du carré.</p></div></div>
  <div class="side">
    <h3>Tailles minimales</h3>
    <div class="row">
      <div class="minlogo">{sized(h, w=150)}<span>Horizontal : 35 mm · 150 px</span></div>
    </div>
    <div class="sizes">{sizes}</div>
    <div class="small">
      <div class="big">{sized(symbol_small(), w=92)}</div>
      <div><h3>Version petites tailles</h3>
        <p>À 32 px et moins (icônes du ruban AutoCAD, favicons), on utilise un dessin optimisé : trait épaissi à 1,4x, panse refermée sur le fût, nœud Signal agrandi au cœur de la boucle.</p>
        <div class="cmp">{compare}</div></div>
    </div>
  </div>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:660px 1fr;gap:36px;margin-top:30px}}
.z{{background:#fff;border-radius:6px;padding:34px 30px 24px;text-align:center}}
.symz{{display:flex;gap:26px;align-items:center;margin-top:26px;padding-top:24px;border-top:1px solid #eee9e1}} .symz p{{margin:0!important}}
.z p{{font-size:12.5px;margin:22px 0 0;text-align:left}}
.side h3{{margin-bottom:14px}}
.minlogo{{background:#fff;border-radius:6px;padding:18px;display:flex;flex-direction:column;gap:10px}}
.minlogo span,.sz span{{font:400 10px Mono;color:#6b7684}}
.sizes{{display:flex;gap:18px;align-items:flex-end;background:#fff;border-radius:6px;padding:18px;margin:14px 0}}
.sz{{display:flex;flex-direction:column;align-items:center;gap:8px}}
.side p{{font-size:12.5px}}
.small{{display:flex;gap:18px;background:#fff;border-radius:6px;padding:18px}}
.small .big{{flex:none;background:{CHAUX};border-radius:6px;padding:10px}}
.small h3{{margin-bottom:6px}} .small p{{font-size:11.5px;line-height:1.5}}
.cmp{{display:flex;gap:22px;margin-top:10px}}
"""
    return page_shell(inner, 6, "Protection", "light", css)


# ------------------------------------------------------------ 7. Couleurs
COLORS = [
    ("Nuit d'acier", NUIT, "11 · 22 · 36", "95 · 75 · 45 · 65", "Fond principal, textes, logotype.", 55),
    ("Cuivre de forge", CUIVRE, "200 · 119 · 63", "15 · 60 · 85 · 5", "Couleur signature : l'armature, les accents.", 12),
    ("Signal IA", SIGNAL, "53 · 208 · 222", "65 · 0 · 15 · 0", "Réservé à l'IA : le nœud, les états actifs.", 3),
    ("Acier trempé", ACIER, "28 · 43 · 61", "88 · 70 · 45 · 45", "Surfaces sombres, cartes, interface.", 5),
    ("Béton coulé", BETON, "185 · 190 · 196", "28 · 18 · 15 · 0", "Traits techniques, textes secondaires.", 5),
    ("Blanc chaux", CHAUX, "243 · 240 · 234", "3 · 4 · 7 · 0", "Fond clair, respiration, papier.", 20),
]


def p07():
    cards = ""
    for name, hx, rgb, cmyk, use, _ in COLORS:
        dark = hx in (NUIT, ACIER, CUIVRE)
        fg = CHAUX if dark else NUIT
        cards += f"""<div class="sw" style="background:{hx};color:{fg}">
  <div class="nm">{name}</div>
  <div class="codes"><div><span>HEX</span>{hx.upper()}</div><div><span>RVB</span>{rgb}</div><div><span>CMJN</span>{cmyk}</div></div>
  <div class="use">{use}</div></div>"""
    bar = "".join(f'<div style="flex:{pct};background:{hx}" title="{name}"></div>' for name, hx, *_, pct in COLORS)
    acc = ""
    for name, hx, ok in [("Cuivre de forge", CUIVRE, False), ("Cuivre texte", CUIVRE_TEXTE, True),
                         ("Signal IA", SIGNAL, False), ("Signal texte", SIGNAL_TEXTE, True)]:
        r = contrast(hx, CHAUX)
        rs = f"{r:.1f}".replace(".", ",")
        verdict = "texte courant ✓" if r >= 4.5 else "titres et graphisme seulement"
        acc += (f'<div class="ac{" ok" if ok else ""}"><i style="background:{hx}"></i>'
                f'<div><b style="color:{hx}">{name}</b><span>{hx.upper()} · {rs}:1 · {verdict}</span></div></div>')
    inner = f"""
<div class="kicker">06 — Couleurs</div>
<h1 style="margin-top:10px">Le béton, le cuivre, le signal.</h1>
<div class="grid">{cards}</div>
<div class="prop"><div class="lab">Proportions dans une composition type</div><div class="bar">{bar}</div>
<div class="legend">{"".join(f'<span><i style="background:{hx}"></i>{name.split()[0] if name != "Signal IA" else "Signal"} {pct} %{" max" if hx == SIGNAL else ""}</span>' for name, hx, *_, pct in COLORS)}</div></div>
<div class="acc"><div class="lab">Couleurs de texte sur fond clair — contraste vérifié (norme WCAG AA ≥ 4,5:1)</div>
<div class="accrow">{acc}</div></div>
<p class="note">Valeurs CMJN indicatives : à valider sur épreuve avec l'imprimeur. Sur fond clair, tout texte de moins de 24 px utilise la version « texte ».</p>"""
    css = f"""
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:24px}}
.sw{{height:148px;border-radius:6px;padding:18px 20px;display:flex;flex-direction:column;justify-content:space-between}}
.sw[style*="{CHAUX}"]{{border:1px solid #ddd8ce}}
.nm{{font:600 17px Sora}}
.codes{{font:400 10.5px/1.7 Mono}} .codes span{{display:inline-block;width:44px;opacity:.6}}
.use{{font-size:11.5px;opacity:.85}}
.prop{{margin-top:22px}} .lab{{font:500 10px Mono;letter-spacing:2px;text-transform:uppercase;color:#7b8591;margin-bottom:8px}}
.bar{{display:flex;height:22px;border-radius:4px;overflow:hidden;border:1px solid #ddd8ce}}
.legend{{display:flex;gap:26px;font:400 10px Mono;color:#6b7684;margin-top:8px}} .legend i{{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:6px;border:1px solid #ccc;vertical-align:-1px}}
.note{{font-size:11px;margin-top:10px;color:#5b6572}}
.acc{{margin-top:18px}}
.accrow{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}
.ac{{display:flex;gap:10px;align-items:center;background:#fff;border-radius:6px;padding:10px 12px;border:1px solid transparent}}
.ac.ok{{border-color:#ddd8ce}}
.ac i{{flex:none;width:26px;height:26px;border-radius:4px}}
.ac b{{display:block;font:600 13px Sora}} .ac span{{font:400 9.5px Mono;color:#5b6572}}
"""
    return page_shell(inner, 7, "Couleurs", "light", css)


# ------------------------------------------------------------ 8. Typographie
def p08():
    inner = f"""
<div class="kicker">07 — Typographie</div>
<h1 style="margin-top:10px">Une voix d'ingénieur, précise et lisible.</h1>
<div class="grid">
  <div class="f big"><div class="lab">Titres · Logotype</div><div class="spec" style="font:600 70px/1 Sora;letter-spacing:-2px">Sora</div>
    <div class="alpha" style="font:600 20px Sora">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div>
    <p>Géométrique et technique. Le logotype est en Sora SemiBold, capitales espacées à +160.</p>
    <div class="w"><span style="font-weight:300">Light 300</span><span style="font-weight:400">Regular 400</span><span style="font-weight:600">SemiBold 600</span><span style="font-weight:700">Bold 700</span></div></div>
  <div class="f"><div class="lab">Texte courant</div><div class="spec" style="font:500 42px/1 Manrope">Manrope</div>
    <p style="font-size:13px;color:{NUIT}">La poutre P1 reçoit 3 HA16 filants en partie inférieure et des cadres HA8 espacés de 15 cm.</p>
    <p>Rapports, notices, site et interface.</p></div>
  <div class="f"><div class="lab">Données · Code · Cotes</div><div class="spec" style="font:500 36px/1 Mono">JetBrains Mono</div>
    <pre>(defun c:CR-POUTRE ()
  (setq b 25 h 50 ; cm
        barres "3HA16"))</pre>
    <p>Cotes, nomenclatures, code AutoLISP.</p></div>
  <div class="f ser"><div class="lab">Citations · Touche éditoriale</div><div class="sr"><div class="spec serif" style="font-size:46px;line-height:1">Instrument Serif</div>
    <p class="serif" style="font-size:26px;color:{CUIVRE};line-height:1.25">« L'intelligence de l'armature. »</p></div>
    <p>À utiliser avec parcimonie, en italique, pour les citations et les accroches.</p></div>
</div>
<p class="note">Toutes ces polices sont libres (licence SIL Open Font) et gratuites, y compris pour un usage commercial.</p>"""
    css = f"""
.grid{{display:grid;grid-template-columns:1.25fr 1fr 1fr;grid-template-rows:auto auto;gap:14px;margin-top:22px}}
.f{{background:#fff;border-radius:6px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}}
.f.big{{grid-row:1 / 3}} .f.ser{{grid-column:2 / 4}} .sr{{display:flex;align-items:baseline;gap:30px}}
.w{{display:flex;flex-direction:column;gap:6px;font:24px Sora;color:{NUIT};margin-top:auto;padding-top:14px;border-top:1px solid #eee9e1}}
.lab{{font:500 10px Mono;letter-spacing:2px;text-transform:uppercase;color:{CUIVRE_TEXTE}}}
.alpha{{line-height:1.5;color:{NUIT};letter-spacing:.5px;margin-top:8px}}
.f p{{font-size:12px;margin:0}}
pre{{font:400 11px/1.5 Mono;background:{NUIT};color:{CHAUX};padding:10px 12px;border-radius:4px}}
.note{{font-size:11px;margin-top:12px;color:#6b7684}}
"""
    return page_shell(inner, 8, "Typographie", "light", css)


# ------------------------------------------------------------ 9. Déclinaisons
def p09():
    variants = [
        ("Couleur · fond clair", CHAUX, dict()),
        ("Couleur · fond Nuit", NUIT, dict(bar=CHAUX, text=CHAUX)),
        ("Blanc et Nuit · fond Cuivre", CUIVRE, dict(bar=WHITE, text=WHITE, accent=NUIT, noeud=WHITE)),
        ("Blanc · fond Acier", ACIER, dict(bar=WHITE, text=WHITE, accent=CUIVRE)),
        ("Monochrome noir", WHITE, dict(bar="#000", text="#000", accent="#000", noeud="#000")),
        ("Monochrome blanc", "#000000", dict(bar=WHITE, text=WHITE, accent=WHITE, noeud=WHITE)),
    ]
    cells = ""
    for lab, bg, kw in variants:
        h, *_ = logo_horizontal(**kw)
        fg = NUIT if bg in (CHAUX, WHITE) else "#c9d0d8"
        cells += f'<div class="v" style="background:{bg}"><span style="color:{fg}">{lab}</span>{sized(h, w=270)}</div>'
    icons = ""
    for bg, kw in [(NUIT, dict(bar=CHAUX)), (CUIVRE, dict(bar=WHITE, accent=NUIT, noeud=WHITE)), (CHAUX, {}), (ACIER, dict(bar=WHITE))]:
        icons += f'<div class="ic">{sized(symbol(bg=bg, rx=52, **kw), w=78)}</div>'
    inner = f"""
<div class="kicker">08 — Déclinaisons</div>
<h1 style="margin-top:10px">Lisible sur tous les supports.</h1>
<div class="grid">{cells}</div>
<div class="icons"><div class="lab">Icônes d'application et de plugin</div>{icons}</div>"""
    css = f"""
.grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:22px}}
.v{{height:150px;border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;position:relative}}
.v[style*="{CHAUX}"],.v[style*="#FFFFFF"]{{border:1px solid #ddd8ce}}
.v span{{position:absolute;top:10px;left:14px;font:500 9px Mono;letter-spacing:1.8px;text-transform:uppercase}}
.icons{{display:flex;align-items:center;gap:18px;margin-top:18px;background:#fff;border-radius:6px;padding:14px 22px}}
.icons .lab{{font:500 10px Mono;letter-spacing:2px;text-transform:uppercase;color:#7b8591;margin-right:auto}}
.ic svg{{display:block;filter:drop-shadow(0 4px 8px rgba(11,22,36,.18))}}
"""
    return page_shell(inner, 9, "Déclinaisons", "light", css)


# ------------------------------------------------------------ 10. Interdits
def p10():
    h, *_ = logo_horizontal()
    inner_h = h[h.index(">") + 1:h.rindex("</svg>")]
    vb = h[h.index('viewBox="') + 9:h.index('"', h.index('viewBox="') + 9)]
    def box(content, lab):
        return f'<div class="x"><div class="art">{content}</div><div class="cap"><b>✕</b> {lab}</div></div>'
    donts = [
        (f'<svg viewBox="{vb}" width="300" height="80" preserveAspectRatio="none">{inner_h}</svg>', "Ne pas déformer ni étirer"),
        (f'<svg viewBox="{vb}" width="280">{inner_h.replace(NUIT, "#2E7D32").replace(CUIVRE, "#FBC02D")}</svg>', "Ne pas changer les couleurs"),
        (f'<svg viewBox="{vb}" width="280" style="transform:rotate(-12deg)">{inner_h}</svg>', "Ne pas incliner"),
        (f'<div style="background:{CUIVRE};padding:14px 18px"><svg viewBox="{vb}" width="244">{inner_h}</svg></div>', "Pas de logo couleur sur fond cuivre"),
        (f'<svg viewBox="{vb}" width="280" style="filter:drop-shadow(6px 6px 3px rgba(0,0,0,.55))">{inner_h}</svg>', "Pas d'ombre ni d'effet"),
        (f'<div style="display:flex;align-items:center;gap:10px">{sized(symbol(), w=48)}<span style="font:italic 700 28px Georgia;color:{NUIT}">CivRebar AI</span></div>', "Ne pas recomposer le texte"),
    ]
    cells = "".join(box(c, l) for c, l in donts)
    inner = f"""
<div class="kicker">09 — Usages interdits</div>
<h1 style="margin-top:10px">Une armature ne se déforme pas.</h1>
<div class="grid">{cells}</div>
<p class="note">Toujours utiliser les fichiers fournis dans le pack, sans les redessiner. En cas de doute : fond Chaux ou Nuit, logo horizontal couleur.</p>"""
    css = f"""
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:24px}}
.x{{background:#fff;border-radius:6px;overflow:hidden}}
.art{{height:150px;display:flex;align-items:center;justify-content:center;opacity:.9}}
.cap{{padding:10px 14px;font-size:12px;border-top:1px solid #eee;color:#3a4553}}
.cap b{{color:#D0342C;margin-right:6px}}
.note{{font-size:12px;margin-top:18px}}
"""
    return page_shell(inner, 10, "Interdits", "light", css)


# ------------------------------------------------------------ 11. Applications
def beam_drawing():
    """Petit dessin de ferraillage de poutre (élévation + coupe), style plan."""
    st = "".join(f'<line x1="{x}" y1="44" x2="{x}" y2="96" />' for x in list(range(40, 120, 9)) + list(range(128, 262, 16)) + list(range(270, 350, 9)))
    return f"""<svg viewBox="0 0 420 150" width="100%">
<rect x="30" y="36" width="330" height="68" fill="none" stroke="{BETON}" stroke-width="1.2"/>
<g stroke="{CUIVRE}" stroke-width="1.1">{st}</g>
<g stroke="{SIGNAL}" stroke-width="2"><line x1="34" y1="46" x2="356" y2="46"/><line x1="34" y1="94" x2="356" y2="94"/></g>
<g fill="none" stroke="{BETON}" stroke-width=".7"><line x1="30" y1="120" x2="360" y2="120"/><line x1="30" y1="115" x2="30" y2="125"/><line x1="360" y1="115" x2="360" y2="125"/></g>
<text x="195" y="134" fill="{BETON}" font-family="Mono" font-size="8" text-anchor="middle">L = 5,00 m</text>
<text x="195" y="28" fill="{CHAUX}" font-family="Mono" font-size="8" text-anchor="middle">POUTRE P1 — 25 × 50 — 3 HA16 + 2 HA12 — Cadres HA8</text>
<rect x="378" y="36" width="30" height="68" fill="none" stroke="{BETON}" stroke-width="1.2"/>
<rect x="382" y="40" width="22" height="60" rx="3" fill="none" stroke="{CUIVRE}" stroke-width="1.1"/>
<g fill="{SIGNAL}"><circle cx="386" cy="95" r="2.4"/><circle cx="393" cy="95" r="2.4"/><circle cx="400" cy="95" r="2.4"/><circle cx="386" cy="45" r="2"/><circle cx="400" cy="45" r="2"/></g>
</svg>"""


def p11():
    h_light, *_ = logo_horizontal(bar=CHAUX, text=CHAUX)
    h_dark, *_ = logo_horizontal()
    tools = ["Poutre", "Poteau", "Dalle", "Semelle", "Escalier", "Nomenclature"]
    glyph = {
        "Poutre": '<rect x="2" y="8" width="18" height="6"/>',
        "Poteau": '<rect x="8" y="2" width="6" height="18"/>',
        "Dalle": '<rect x="2" y="9" width="18" height="3"/><path d="M5 10.5h12"/>',
        "Semelle": '<path d="M9 2v10M13 2v10M3 12h16v6H3z"/>',
        "Escalier": '<path d="M3 19h4v-4h4v-4h4v-4h4"/>',
        "Nomenclature": '<path d="M4 5h14M4 9h14M4 13h14M4 17h9"/>',
    }
    ribbon = "".join(f'<div class="tb"><svg class="ti" viewBox="0 0 22 22" width="22" height="22" fill="none" stroke="{CUIVRE if i == 0 else BETON}" stroke-width="1.5">{glyph[t]}</svg>{t}</div>' for i, t in enumerate(tools))
    nom = [("1", "HA16", "3", "5,34 m", "25,3 kg"), ("2", "HA12", "2", "5,22 m", "9,3 kg"), ("3", "HA8", "31", "1,42 m", "17,4 kg")]
    nomen = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in nom)
    inner = f"""
<div class="kicker">10 — Applications</div>
<h1 style="margin-top:10px">Du plan de ferraillage à la carte de visite.</h1>
<div class="grid">
  <div class="app">
    <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="tt">AutoCAD — Plan_Ferraillage_R+2.dwg</span></div>
    <div class="ribbon"><div class="tab">CivRebar AI</div>{ribbon}</div>
    <div class="canvas">{beam_drawing()}
      <table class="nom"><tr><th>REP.</th><th>Ø</th><th>NB</th><th>LONG.</th><th>POIDS</th></tr>{nomen}<tr class="tot"><td colspan="4">TOTAL POUTRE P1</td><td>52,0 kg</td></tr></table>
      <div class="panel">{sized(symbol(bar=CHAUX), w=22)}<div><b>Assistant CivRebar</b><br>Espacement des cadres conforme. 3 HA16 filants proposés.</div></div>
    </div>
  </div>
  <div class="col">
    <div class="card front">{sized(h_light, w=220)}</div>
    <div class="card back"><div class="nm">Prénom Nom</div><div class="rl">Ingénieur génie civil · Fondateur</div>
      <div class="ct">contact@civrebar.ai<br>+225 00 00 00 00 00</div>{sized(symbol(), w=46)}</div>
    <div class="cart">
      <div class="c1">{sized(h_dark, w=150)}</div>
      <div class="c2"><span>PROJET</span>Immeuble R+2<br><span>PLANCHE</span>FER-04 · Poutres</div>
      <div class="c3"><span>ÉCHELLE</span>1/50<br><span>INDICE</span>A</div>
    </div>
    <div class="lab">Carte de visite · Cartouche de plan</div>
  </div>
</div>"""
    css = f"""
.grid{{display:grid;grid-template-columns:600px 1fr;gap:22px;margin-top:22px}}
.app{{background:{NUIT};border-radius:8px;overflow:hidden;height:560px;box-shadow:0 10px 30px rgba(11,22,36,.25)}}
.bar{{height:28px;background:#060d16;display:flex;align-items:center;gap:6px;padding:0 12px}}
.dot{{width:9px;height:9px;border-radius:50%;background:#2a394b}}
.tt{{font:400 10px Mono;color:#6f7c8b;margin-left:10px}}
.ribbon{{display:flex;align-items:stretch;background:{ACIER};border-bottom:2px solid {CUIVRE}}}
.tab{{background:{CUIVRE};color:{NUIT};font:600 11px Sora;padding:0 14px;display:flex;align-items:center}}
.tb{{font:500 10px Manrope;color:#c9d0d8;padding:8px 10px;display:flex;flex-direction:column;align-items:center;gap:4px;border-right:1px solid #24364b;min-width:66px}}
.nom{{border-collapse:collapse;font:400 9.5px Mono;color:#c9d0d8;margin-top:10px;width:300px}} .nom th{{text-align:left;color:{CUIVRE};font-weight:500;padding:4px 6px;border-bottom:1px solid #2c4057}} .nom td{{padding:4px 6px;border-bottom:1px solid #1c2b3d}} .nom .tot td{{color:{SIGNAL}}}
.canvas{{position:relative;padding:22px 22px;height:470px;background:radial-gradient(#15253a 1px,transparent 1px) 0 0/16px 16px}}
.panel{{position:absolute;right:18px;bottom:18px;width:250px;background:{ACIER};border:1px solid #2c4057;border-left:3px solid {SIGNAL};border-radius:6px;padding:12px;display:flex;gap:10px;font:400 11px/1.45 Manrope;color:#c9d0d8}}
.panel b{{color:{CHAUX};font-weight:700}}
.col{{display:flex;flex-direction:column;gap:14px}}
.card{{height:150px;border-radius:6px;box-shadow:0 8px 22px rgba(11,22,36,.18)}}
.front{{background:{NUIT};display:flex;align-items:center;justify-content:center}}
.back{{background:#fff;padding:18px 20px;position:relative}}
.back svg{{position:absolute;right:18px;bottom:18px}}
.nm{{font:600 16px Sora}} .rl{{font-size:11px;color:{CUIVRE_TEXTE};margin-top:2px}}
.ct{{font:400 10.5px/1.6 Mono;color:#3a4553;margin-top:26px}}
.cart{{display:grid;grid-template-columns:1.3fr 1fr .6fr;border:1.5px solid {NUIT};background:#fff;height:92px}}
.cart>div{{padding:10px;border-right:1px solid {NUIT};font:500 10px/1.5 Manrope;color:{NUIT}}}
.cart>div:last-child{{border:0}}
.cart span{{display:block;font:400 7.5px Mono;letter-spacing:1.2px;color:#7b8591}}
.c1{{display:flex;align-items:center;justify-content:center}}
.lab{{font:500 10px Mono;letter-spacing:2px;text-transform:uppercase;color:#7b8591}}
"""
    return page_shell(inner, 11, "Applications", "light", css)


# ------------------------------------------------------------ 12. La trajectoire
def p12():
    steps = [
        ("01", "AutoLISP", "Un script par élément. Premier objectif : la poutre, des paramètres au dessin coté et repéré."),
        ("02", "Boîte à outils", "Tous les scripts réunis sous un seul menu CivRebar AI : poutre, poteau, dalle, semelle, escalier."),
        ("03", "Plugin AutoCAD", "Une vraie extension, avec son onglet dans le ruban, une interface soignée et plus de fonctions."),
        ("04", "Intelligence", "Nomenclatures, quantitatifs, vérifications, échanges avec Robot Structural Analysis, assistant IA."),
    ]
    xs = [8, 263, 518, 773]
    line = f'<line x1="0" y1="60" x2="1000" y2="60" stroke="{CUIVRE}" stroke-width="6"/>'
    nodes = "".join(f'<circle cx="{x}" cy="60" r="{14 if i == 3 else 10}" fill="{SIGNAL if i == 3 else CHAUX}" stroke="{NUIT}" stroke-width="4"/>' for i, x in enumerate(xs))
    stirrups = "".join(f'<line x1="{x}" y1="44" x2="{x}" y2="76" stroke="#2a3b50" stroke-width="3"/>' for x in range(14, 1000, 32))
    cols = "".join(f'<div class="st"><div class="n">{n}</div><h2>{t}</h2><p>{d}</p></div>' for n, t, d in steps)
    inner = f"""
<div class="kicker">13 — La trajectoire</div>
<h1 style="margin-top:10px;color:{CHAUX}">On construit CivRebar comme on ferraille :<br><span style="color:{CUIVRE_CLAIR}">barre après barre.</span></h1>
<svg class="road" viewBox="0 0 1000 120" width="995">{stirrups}{line}{nodes}<text x="0" y="24" font-family="Mono" font-size="11" fill="{SIGNAL}" letter-spacing="2">NOUS SOMMES ICI</text></svg>
<div class="steps">{cols}</div>
<div class="end">{sized(logo_horizontal(bar=CHAUX, text=CHAUX)[0], w=260)}<span class="serif">L'intelligence de l'armature.</span></div>"""
    css = f"""
.road{{margin-top:40px}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:6px}}
.st .n{{font:500 12px Mono;color:{CUIVRE}}}
.st h2{{color:{CHAUX};margin:6px 0 8px;font-size:22px}}
.st p{{font-size:12.5px}}
.end{{position:absolute;left:64px;right:64px;bottom:70px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid #1f2f42;padding-top:24px}}
.end .serif{{font-size:26px;color:{CUIVRE_CLAIR}}}
"""
    return page_shell(inner, 14, "Trajectoire", "dark", css)


# ------------------------------------------------------------ images embarquées
import base64 as _b64
import io as _io
import pathlib as _pl

_ROOT = _pl.Path(__file__).resolve().parent.parent


def img_uri(path, max_w):
    """Image redimensionnée (~300 DPI à sa taille d'affichage) et encodée en JPEG base64."""
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = _io.BytesIO()
    im.save(buf, "JPEG", quality=86)
    return "data:image/jpeg;base64," + _b64.b64encode(buf.getvalue()).decode()


# ------------------------------------------------------------ 12. Supports numériques
def p_supports():
    d = _ROOT / "CivRebar_AI_Pack_Logo" / "05_Supports_numeriques"
    def im(name, w):
        f = d / f"{name}.png"
        return f'<img src="{img_uri(f, w)}">' if f.exists() else '<div class="miss">à générer</div>'
    inner = f"""
<div class="kicker">11 — Supports numériques</div>
<h1 style="margin-top:10px">Prêts à publier, dès aujourd'hui.</h1>
<div class="g">
  <figure class="li">{im("Banniere_LinkedIn_1584x396", 1400)}<figcaption>Bannière LinkedIn · 1584 × 396</figcaption></figure>
  <div class="row">
    <figure>{im("Photo_de_profil_1080x1080", 500)}<figcaption>Photo de profil · 1080²</figcaption></figure>
    <figure>{im("Post_annonce_1080x1350", 500)}<figcaption>Post annonce</figcaption></figure>
    <figure>{im("Ecran_demarrage_plugin_1280x720", 900)}<figcaption>Écran de démarrage du plugin · 1280 × 720</figcaption></figure>
    <figure>{im("Post_citation_1080x1080", 500)}<figcaption>Post citation · 1080²</figcaption></figure>
  </div>
</div>"""
    css = f"""
.g{{margin-top:22px}}
figure{{margin:0}} figure img{{display:block;border-radius:6px;box-shadow:0 6px 18px rgba(11,22,36,.18)}}
.li img{{width:100%}}
figcaption{{font:400 9.5px Mono;letter-spacing:1px;color:#5b6572;margin-top:6px;text-transform:uppercase}}
.row{{display:flex;justify-content:space-between;margin-top:16px}}
.row img{{height:208px;width:auto}}
.miss{{height:120px;border:1px dashed #b9bec4;border-radius:6px;display:flex;align-items:center;justify-content:center;font:400 11px Mono;color:#5b6572}}
"""
    return page_shell(inner, 12, "Supports", "light", css)


# ------------------------------------------------------------ 13. Mises en situation (grille bento)
BENTO = [
    ("01", "Casque de chantier", "a"),
    ("02", "Poste de travail AutoCAD", "b"),
    ("03", "Plaque en cuivre", "c"),
    ("04", "Étiquette de fagot", "d"),
    ("05", "Cartes de visite", "e"),
    ("06", "Polo brodé", "f"),
]


def p_bento():
    d = _ROOT / "mockups" / "images"
    cells = ""
    for n, title, area in BENTO:
        found = next(iter(sorted(d.glob(f"{n}*.*"))), None) if d.exists() else None
        if found:
            content = f'<img src="{img_uri(found, 1300)}">'
        else:
            content = (f'<div class="ph">{sized(symbol(bar="#23364d", accent="#23364d", noeud="#23364d"), w=70)}'
                       f'<span>Image {n} à venir</span></div>')
        cells += f'<div class="t {area}">{content}<div class="cap"><b>{n}</b>{title}</div></div>'
    inner = f"""
<div class="kicker">12 — Mises en situation</div>
<h1 style="margin-top:10px;color:{CHAUX}">La marque, sur le terrain.</h1>
<div class="bento">{cells}</div>"""
    css = f"""
.bento{{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,172px);gap:10px;margin-top:22px;
  grid-template-areas:'a a b b' 'a a c d' 'e f f d'}}
.a{{grid-area:a}} .b{{grid-area:b}} .c{{grid-area:c}} .d{{grid-area:d}} .e{{grid-area:e}} .f{{grid-area:f}}
.t{{position:relative;border-radius:8px;overflow:hidden;background:{ACIER}}}
.t img{{width:100%;height:100%;object-fit:cover;display:block}}
.ph{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;
  font:400 10px Mono;letter-spacing:2px;text-transform:uppercase;color:#56677b;
  background:repeating-linear-gradient(90deg,transparent 0 23px,#15253a 23px 24px)}}
.cap{{position:absolute;left:10px;bottom:10px;background:rgba(11,22,36,.82);color:{CHAUX};font:500 10px Manrope;
  padding:5px 9px;border-radius:4px;display:flex;gap:7px}}
.cap b{{font:500 10px Mono;color:{CUIVRE_CLAIR}}}
"""
    return page_shell(inner, 13, "Mises en situation", "dark", css)


PAGES = [p05, p06, p07, p08, p09, p10, p11, p_supports, p_bento, p12]
