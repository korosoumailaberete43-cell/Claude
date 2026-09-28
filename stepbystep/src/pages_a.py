"""Pages 1 à 5 : couverture, manifeste, histoire du logo, remasterisation, construction."""
import base64
from brand import *
from shell import page_shell, marches_mini
import logo as L

MAGENTA = "#D6247F"
EMAIL, TEL, PAYS = "step.by.step.academy4@gmail.com", "+223 89 48 33 27", "Mali"
LARGEURS = [296, 385, 491, 620, 767]


def marches_motif(x, y, w_max, h, gap, color=OR, align="right"):
    """Motif des 5 marches (proportions exactes du logo) en SVG, aligné à droite comme dans le logo."""
    out = ""
    for i, wv in enumerate(LARGEURS):
        w = w_max * wv / 767
        xx = x + (w_max - w if align == "right" else 0)
        out += f'<rect x="{xx:.1f}" y="{y + i * (h + gap):.1f}" width="{w:.1f}" height="{h}" fill="{color}"/>'
    return out


def img64(path, mime="image/jpeg"):
    return f"data:{mime};base64,{base64.b64encode(open(path, 'rb').read()).decode()}"


# ------------------------------------------------------------ 1. Couverture (claire)
def p01():
    motif = marches_motif(0, 0, 520, 38, 14)
    inner = f"""
<div class="k kicker">Charte graphique · Édition 2.0 · 2026</div>
<div class="t"><h1>La progression,<br><span class="or2">étape par étape.</span></h1>
<p class="sub">Manuel d'identité visuelle de Step by Step Academy — formations aux logiciels d'ingénierie,
à l'intelligence artificielle et soutien scolaire, en ligne, en présentiel et à domicile.</p></div>
<svg class="motif" viewBox="0 0 520 246" width="520">{motif}</svg>
<div class="lg">{sized(principal('clair'), w=330)}</div>
<div class="bas">{EMAIL} · {TEL} · {PAYS}</div>"""
    css = f"""
.k{{position:absolute;left:72px;top:64px}}
.t{{position:absolute;left:72px;top:150px;width:520px}}
.t h1{{font-size:52px;line-height:1.02;letter-spacing:-1.6px}}
.or2{{color:{NOIR};background:linear-gradient(transparent 58%,{OR} 58%,{OR} 86%,transparent 86%)}}
.sub{{margin-top:22px;font-size:15px;color:{GRIS};width:440px}}
.motif{{position:absolute;left:0;bottom:92px}}
.lg{{position:absolute;right:86px;top:112px;background:{BLANC};border-radius:18px;padding:34px 40px;box-shadow:0 20px 50px rgba(17,17,17,.08)}}
.bas{{position:absolute;right:72px;bottom:56px;font:700 10px Comfortaa;letter-spacing:1.6px;color:{GRIS}}}
"""
    return page_shell(inner, 0, "", "light", css)


# ------------------------------------------------------------ 2. Manifeste
def p02():
    inner = f"""
<div class="kicker">01 — Manifeste</div>
<div class="wrap">
  <div class="left">
    <h1 class="big">Chaque réussite commence par une <span class="or">première marche.</span></h1>
    <svg viewBox="0 0 300 150" width="300" style="margin-top:34px">{marches_motif(0, 0, 300, 22, 8)}</svg>
  </div>
  <div class="right">
    <p class="lead">Personne n'arrive au sommet d'un bond. On y arrive marche après marche, avec quelqu'un qui montre le chemin.</p>
    <p>C'est la conviction de Step by Step Academy. Qu'il s'agisse de dessiner un premier plan sur AutoCAD, de modéliser un bâtiment sur Revit ou ArchiCAD, de traiter un relevé sur Global Mapper, de maîtriser un logiciel minier ou hydraulique, de découvrir l'intelligence artificielle, ou de rattraper un retard à l'école : chaque apprenant part d'où il est.</p>
    <p>Notre rôle est de découper l'effort en étapes franchissables, de valider chacune avant de passer à la suivante, et de rester présents jusqu'à la dernière, en ligne, en salle ou à domicile.</p>
    <div class="vals">
      <div><b>01</b><h3>Méthode</h3><p>Des étapes claires, un objectif à chaque séance.</p></div>
      <div><b>02</b><h3>Accompagnement</h3><p>Un formateur qui suit chaque apprenant.</p></div>
      <div><b>03</b><h3>Réussite</h3><p>Chaque étape validée se voit et se célèbre.</p></div>
    </div>
  </div>
</div>
<div class="offre"><span class="lab">Ce que nous enseignons</span>
  <div class="chips"><i>Logiciels d'ingénierie</i><i>Géomatique &amp; mines</i><i>Hydraulique</i><i>Intelligence artificielle</i><i>Soutien scolaire</i></div>
  <div class="fmt"><span>En ligne</span><span>Présentiel</span><span>À domicile</span></div></div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:380px 1fr;gap:60px;margin-top:40px}}
.big{{font-size:46px;line-height:1.05;letter-spacing:-1.4px}}
.lead{{font:600 19px/1.5 Quicksand;color:{NOIR};margin-bottom:14px}}
.right p{{margin-bottom:11px}}
.vals{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:22px;padding-top:20px;border-top:1px solid #E4DCCB}}
.offre{{position:absolute;left:64px;right:64px;bottom:76px;display:flex;flex-wrap:wrap;align-items:center;gap:10px 18px;padding-top:16px;border-top:1px solid #E4DCCB}} .offre>.lab{{width:100%}}
.chips{{display:flex;gap:6px;flex:1}} .chips i{{white-space:nowrap;font:600 12px Quicksand;font-style:normal;background:{BLANC};border-radius:20px;padding:7px 13px}}
.fmt{{display:flex;gap:6px}} .fmt span{{white-space:nowrap;font:700 10px Comfortaa;letter-spacing:1px;background:{NOIR};color:{OR};border-radius:20px;padding:7px 11px}}
.vals b{{font:700 11px Comfortaa;color:{OR_TEXTE}}} .vals h3{{margin:6px 0 4px}} .vals p{{font-size:12.5px;line-height:1.5;margin:0}}
"""
    return page_shell(inner, 2, "Manifeste", "light", css)


# ------------------------------------------------------------ 3. L'histoire du logo (sombre)
def p03():
    lg = inner(principal("sombre"))
    pins = [(1, 250, 215, 60, 150), (2, 700, 192, 700, 110), (3, 300, 722, 60, 722),
            (4, 889, 240, 889, 110), (5, 612, 1105, 460, 1105), (6, 188, 850, 60, 860)]
    marks = ""
    for n, x, y, lx, ly in pins:
        marks += (f'<line x1="{x}" y1="{y}" x2="{lx}" y2="{ly}" stroke="#8C857A" stroke-width="2" stroke-dasharray="6 6"/>'
                  f'<circle cx="{lx}" cy="{ly}" r="22" fill="{OR}"/>'
                  f'<text x="{lx}" y="{ly + 8}" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="22" fill="{NOIR}">{n}</text>')
    items = [
        ("La toque", "L'objectif : une compétence reconnue, un diplôme, une attestation. Elle est posée au départ du fil, comme une promesse."),
        ("Le fil doré", "L'accompagnement. Il relie l'objectif à chaque marche et descend jusqu'au sol : le formateur vient chercher l'apprenant là où il se trouve."),
        ("Les cinq marches", "Cinq niveaux de progression. Chacune est environ 27 % plus large que celle du dessus : les bases sont larges, puis l'effort se concentre."),
        ("La coche", "L'étape validée. Rien ne se franchit sans être acquis : exercices, évaluations, attestation."),
        ("Le livre", "Le savoir, point d'appui de tout le reste, à l'école comme dans les métiers de l'ingénierie."),
        ("Le nom", "« Step By Step » : la méthode dit tout. « By », plus discret, fait le lien entre deux étapes."),
    ]
    lst = "".join(f'<div class="it"><span class="pin">{i + 1}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(items))
    inner_ = f"""
<div class="kicker">02 — L'histoire du logo</div>
<h1 style="margin-top:10px;color:{IVOIRE}">Un logo qui raconte une méthode.</h1>
<div class="wrap"><svg class="sym" viewBox="20 60 1080 1110">{lg}{marks}</svg><div class="list">{lst}</div></div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:430px 1fr;gap:36px;margin-top:22px;align-items:center}}
.sym{{width:430px;height:442px}}
.it{{display:flex;gap:14px;padding:8px 0;border-bottom:1px solid #2E2B26}} .it:last-child{{border:0}}
.pin{{flex:none;width:22px;height:22px;border-radius:50%;background:{OR};color:{NOIR};font:700 11px/22px Comfortaa;text-align:center}}
.it h3{{color:{IVOIRE};margin-bottom:2px}} .it p{{font-size:12.3px;line-height:1.48}}
"""
    return page_shell(inner_, 3, "Histoire du logo", "dark", css)


# ------------------------------------------------------------ 4. La remasterisation
def p04():
    orig = img64(str(ROOT / "source" / "logo_original.jpg"))
    rows = [("Fichier", "Image JPEG 1280 px, fond noir incrusté", "Vectoriel (SVG, PDF, EPS), fond transparent"),
            ("Marches", "Texture de papier doré", "Aplat d'or net #F5C518"),
            ("Toque", "Bords flous", "Redessinée en géométrie nette"),
            ("Coche", "Icône 3D d'une autre banque d'images", "Redessinée à plat, même vert"),
            ("Livre", "Emoji", "Pictogramme dessiné"),
            ("Textes", "Police non documentée", "Quicksand SemiBold + Comfortaa identifiées, lettres recalées une à une"),
            ("Fonds", "Noir uniquement", "Clair, sombre, monochromes noir et blanc")]
    tbl = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    inner_ = f"""
<div class="kicker">03 — Remasterisation</div>
<h1 style="margin-top:10px">Le même logo. Enfin propre.</h1>
<div class="wrap">
  <div>
    <div class="ba">
      <figure><img src="{orig}"><figcaption>Avant · image d'origine</figcaption></figure>
      <figure><div class="blk">{sized(principal('sombre'), h=270)}</div><figcaption>Après · vectoriel, fond transparent</figcaption></figure>
    </div>
    <p class="note"><b>93 %</b> de recouvrement pixel à pixel avec l'original : composition, proportions, positions et textes sont inchangés.
    Seule l'exécution a été reprise. L'ancien fichier JPEG ne doit plus être utilisé.</p>
  </div>
  <table><tr><th></th><th>Avant</th><th>Après</th></tr>{tbl}</table>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:600px 1fr;gap:30px;margin-top:26px}}
.ba{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
figure img,.blk{{width:293px;height:293px;border-radius:10px;display:block}}
.blk{{background:#000;display:flex;align-items:center;justify-content:center}}
figcaption{{font:700 9.5px Comfortaa;letter-spacing:1.6px;text-transform:uppercase;color:{GRIS};margin-top:8px}}
table{{border-collapse:collapse;width:100%;font-size:12px}}
th{{text-align:left;font:700 9.5px Comfortaa;letter-spacing:1.6px;text-transform:uppercase;color:{GRIS};padding:0 8px 8px}}
td{{padding:7px 8px;border-top:1px solid #E4DCCB;vertical-align:top}} td:first-child{{font-weight:700;width:70px}}
td:nth-child(2){{color:#8C857A}} td:nth-child(3){{color:{NOIR}}}
.note{{font-size:12.5px;margin-top:18px}}
"""
    return page_shell(inner_, 4, "Remasterisation", "light", css)


# ------------------------------------------------------------ 5. Construction cotée
def p05():
    M = MAGENTA
    x0 = 150
    grid = "".join(f'<line x1="{x}" y1="300" x2="{x}" y2="780" stroke="#E4DCCB" stroke-width="1"/>' for x in range(150, 1100, 67))
    bars = marches_motif(0, 0, 1, 1, 0)  # non utilisé, gardé pour lisibilité
    rects = ""
    for i, ((x, y), w) in enumerate(zip(L.MARCHES, LARGEURS)):
        rects += f'<rect x="{x}" y="{y}" width="{w}" height="67" fill="{OR}"/>'
    def pill(x, y, t):
        w = 16 + 12.5 * len(t)
        return (f'<rect x="{x - w / 2}" y="{y - 15}" width="{w}" height="30" rx="15" fill="{M}"/>'
                f'<text x="{x}" y="{y + 7}" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="19" fill="#fff">{t}</text>')
    cotes = ""
    for (x, y), w, t in zip(L.MARCHES, LARGEURS, ["4,4 m", "5,7 m", "7,3 m", "9,3 m", "11,4 m"]):
        cotes += f'<line x1="{x}" y1="{y + 33}" x2="{x - 36}" y2="{y + 33}" stroke="{M}" stroke-width="2"/>' + pill(x - 90, y + 33, t)
    ratios = ""
    for i, r in enumerate(["×1,30", "×1,27", "×1,26", "×1,24"]):
        y = L.MARCHES[i][1] + 67 + 11
        ratios += pill(1130, y, r)
    extra = (
             f'<circle cx="889.5" cy="277.5" r="45" fill="none" stroke="{VERT}" stroke-width="9.5"/>'
             f'<circle cx="889.5" cy="277.5" r="55" fill="none" stroke="{M}" stroke-width="1.5" stroke-dasharray="6 5"/>' + pill(760, 278, "Ø 1,5 m")
             + f'<path d="M1010 192.5 A70 70 0 0 1 1080 262.5" fill="none" stroke="{OR}" stroke-width="13"/>'
             f'<path d="M503 192.5 H1010" stroke="{OR}" stroke-width="13"/><path d="M1080 262 V420" stroke="{OR}" stroke-width="13"/>'
             + pill(1150, 215, "R ≈ 1 m"))
    rows = [("Module m", "hauteur d'une marche"), ("Épaisseur d'une marche", "1 m"), ("Espace entre marches", "≈ 1/3 m"),
            ("Largeurs", "4,4 · 5,7 · 7,3 · 9,3 · 11,4 m"), ("Progression", "≈ ×1,27 d'une marche à l'autre"),
            ("Alignement", "bord droit commun"), ("Fil doré", "épaisseur 0,2 m · rayon ≈ 1 m"), ("Coche", "Ø 1,5 m, centrée sur la marche haute")]
    tbl = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    inner_ = f"""
<div class="kicker">04 — Construction</div>
<h1 style="margin-top:10px;font-size:34px">Une progression mesurée,<br>pas un escalier au hasard.</h1>
<div class="wrap">
  <div><p>Mesuré sur l'original, l'escalier suit une <b>progression géométrique</b> : chaque marche est environ 27 % plus large
  que celle du dessus. Toutes les cotes s'expriment en <b>m</b>, la hauteur d'une marche.</p><table>{tbl}</table></div>
  <svg class="plan" viewBox="105 170 1145 620"><rect x="105" y="170" width="1145" height="620" fill="#fff"/>{grid}{rects}{extra}{cotes}{ratios}</svg>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:300px 1fr;gap:34px;margin-top:22px}}
.plan{{width:680px;height:368px;border-radius:10px;margin-top:6px}}
table{{margin-top:14px;border-collapse:collapse;width:100%;font-size:12px}}
td{{padding:6px 0;border-bottom:1px solid #E4DCCB}} td:first-child{{color:{GRIS}}} td:last-child{{text-align:right;font-weight:700}}
"""
    return page_shell(inner_, 5, "Construction", "light", css)


PAGES = [p01, p02, p03, p04, p05]
