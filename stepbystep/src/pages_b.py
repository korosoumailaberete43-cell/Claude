"""Pages 6 à 16 : versions, protection, couleurs, typo, fonds, interdits, univers, applications,
supports numériques, mises en situation, contact."""
import base64
import io
import pathlib

from brand import *
from brand import contrast_ratio
from shell import page_shell, marches_mini
from pages_a import marches_motif, EMAIL, TEL, PAYS, LARGEURS

MAGENTA = "#D6247F"


def img_uri(path, max_w):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=86)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


# ------------------------------------------------------------ pictogrammes des pôles (trait 2,2 px, 40 × 40)
def picto(nom, col=NOIR, acc=OR, s=40):
    d = {
        "ingenierie": f'<path d="M6 34 V14 L16 8 L26 14 V34 Z M11 34 V24 H21 V34" /><path d="M29 34 L29 12 L37 34 Z M31 29 H34" stroke="{acc}"/>',
        "geomatique": f'<path d="M3 34 L14 16 L20 24 L27 13 L37 34 Z"/><path d="M27 4 C31 4 33 7 33 9 C33 13 27 18 27 18 C27 18 21 13 21 9 C21 7 23 4 27 4 Z" stroke="{acc}"/><circle cx="27" cy="9" r="1.6" fill="{acc}" stroke="none"/>',
        "hydraulique": f'<path d="M20 5 C26 14 30 19 30 25 A10 10 0 0 1 10 25 C10 19 14 14 20 5 Z"/><path d="M4 36 C8 33 12 33 16 36 C20 39 24 39 28 36 C32 33 34 33 37 35" stroke="{acc}"/>',
        "ia": f'<rect x="10" y="10" width="20" height="20" rx="3"/><path d="M15 10 V5 M20 10 V5 M25 10 V5 M15 30 V35 M20 30 V35 M25 30 V35 M10 15 H5 M10 20 H5 M10 25 H5 M30 15 H35 M30 20 H35 M30 25 H35"/><path d="M15 23 L18 16 L21 23 M16 21 H20 M24.5 16 V23" stroke="{acc}"/>',
        "scolaire": f'<path d="M4 10 C10 8 15 9 20 12 C25 9 30 8 36 10 V32 C30 30 25 31 20 34 C15 31 10 30 4 32 Z M20 12 V34"/><path d="M27 4 L35 12 L25 22 L22 23 L23 20 Z" stroke="{acc}"/>',
    }[nom]
    return (f'<svg viewBox="0 0 40 40" width="{s}" height="{s}" fill="none" stroke="{col}" stroke-width="2.2" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')


POLES = [
    ("ingenierie", "Logiciels d'ingénierie", "AutoCAD · Revit · ArchiCAD — dessin, modélisation, BIM"),
    ("geomatique", "Géomatique & mines", "Global Mapper · logiciels miniers — cartes, relevés, gisements"),
    ("hydraulique", "Hydraulique", "Logiciels de calcul et de modélisation des réseaux et ouvrages"),
    ("ia", "Intelligence artificielle", "Comprendre et utiliser l'IA dans ses études et son métier"),
    ("scolaire", "Soutien scolaire", "Cours de soutien et cours personnalisés, jusqu'à domicile"),
]


def niveau(n, w=64, actif=OR, inactif="#E4DCCB", k=1.0):
    """Badge de niveau : les 5 marches, remplies jusqu'au niveau n (de la plus basse vers la plus haute)."""
    rows = ""
    for i, wv in enumerate(LARGEURS):         # i=0 : marche du haut
        rank = 5 - i                           # 5 = haut
        col = actif if rank <= n else inactif
        ww = w * wv / 767
        rows += f'<rect x="{w - ww:.1f}" y="{i * 5.4 * k:.1f}" width="{ww:.1f}" height="{3.8 * k:.1f}" fill="{col}"/>'
    return f'<svg viewBox="0 0 {w} {26 * k:.0f}" width="{w}" height="{26 * k:.0f}">{rows}</svg>'


# ------------------------------------------------------------ 6. Le logo et ses versions
def p06():
    inner_ = f"""
<div class="kicker">05 — Le logo et ses versions</div>
<h1 style="margin-top:10px">Une signature, quatre formats.</h1>
<div class="g">
  <div class="c a"><div class="lab">A · Logo principal</div><div class="v">{sized(principal('clair'), h=380)}</div><p>Version de référence : documents, affiches, attestations, site.</p></div>
  <div class="c b"><div class="lab">B · Déclinaison horizontale</div><div class="v">{sized(horizontal('clair'), w=440)}</div><p>Bandeaux, en-têtes, signatures d'e-mail : aucun élément redessiné, seuls les blocs sont réarrangés.</p></div>
  <div class="c c1"><div class="lab">C · Symbole</div><div class="v">{sized(symbole('clair'), w=170)}</div><p>Quand le nom est déjà écrit à côté.</p></div>
  <div class="c d"><div class="lab">D · Icône</div><div class="v">{sized(compact('clair', bg=NOIR, rx=150), w=110)}</div><p>Photo de profil, favicon, application.</p></div>
</div>"""
    css = f"""
.g{{display:grid;grid-template-columns:330px 1fr 1fr;grid-template-rows:268px 268px;gap:14px;margin-top:22px;grid-template-areas:'a b b' 'a c d'}}
.c{{background:{BLANC};border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;justify-content:space-between}}
.a{{grid-area:a}} .b{{grid-area:b}} .c1{{grid-area:c}} .d{{grid-area:d}}
.v{{display:flex;justify-content:center;align-items:center;flex:1}}
.c p{{font-size:11.5px;line-height:1.45;margin:0;text-align:center}}
"""
    return page_shell(inner_, 6, "Versions", "light", css)


# ------------------------------------------------------------ 7. Protection et tailles minimales
def p07():
    lg = inner(principal("clair"))
    x, y, w, h = VB_PRINCIPAL
    m = 67          # module : hauteur d'une marche
    zone = f"""<svg viewBox="{x - m} {y - m} {w + 2 * m} {h + 2 * m}" height="520">
<rect x="{x - m}" y="{y - m}" width="{w + 2 * m}" height="{h + 2 * m}" fill="#fff"/>
<rect x="{x - m}" y="{y - m}" width="{w + 2 * m}" height="{h + 2 * m}" fill="none" stroke="{MAGENTA}" stroke-width="4" stroke-dasharray="16 12"/>
<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{MAGENTA}" stroke-width="2" opacity=".45"/>
{lg}
<rect x="{x - m}" y="{y + h / 2 - m / 2}" width="{m}" height="{m}" fill="{MAGENTA}" opacity=".18"/>
<text x="{x - m / 2}" y="{y + h / 2 + 12}" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="34" fill="{MAGENTA}">m</text></svg>"""
    sizes = "".join(f'<div class="sz">{sized(compact("clair", bg=NOIR, rx=150), w=px)}<span>{px} px</span></div>' for px in (64, 32, 24, 16))
    inner_ = f"""
<div class="kicker">06 — Protection et tailles minimales</div>
<h1 style="margin-top:10px">Une marche d'espace, tout autour.</h1>
<div class="wrap">
  <div class="z">{zone}</div>
  <div class="side">
    <p>La zone de protection vaut <b>m</b>, la hauteur d'une marche du logo. Aucun texte, aucune image ni aucun bord de page n'y entre.</p>
    <table>
      <tr><td>Logo principal</td><td>25 mm · 120 px</td></tr>
      <tr><td>Déclinaison horizontale</td><td>40 mm · 200 px</td></tr>
      <tr><td>Symbole</td><td>15 mm · 72 px</td></tr>
      <tr><td>Icône</td><td>16 px</td></tr>
    </table>
    <div class="lab" style="margin:18px 0 10px">Icône aux petites tailles</div>
    <div class="sizes">{sizes}</div>
    <p style="font-size:12px;margin-top:10px">Sous 120 px de large, le nom devient illisible : utiliser le symbole ou l'icône.</p>
  </div>
</div>"""
    css = f"""
.wrap{{display:grid;grid-template-columns:auto 1fr;gap:40px;margin-top:24px;align-items:start}}
.z svg{{border-radius:10px;display:block}}
table{{border-collapse:collapse;width:100%;font-size:12.5px;margin-top:14px}}
td{{padding:7px 0;border-bottom:1px solid #E4DCCB}} td:last-child{{text-align:right;font-weight:700}}
.sizes{{display:flex;gap:18px;align-items:flex-end;background:{BLANC};border-radius:10px;padding:16px}}
.sz{{display:flex;flex-direction:column;align-items:center;gap:6px}} .sz span{{font:700 9px Comfortaa;color:{GRIS}}}
"""
    return page_shell(inner_, 7, "Protection", "light", css)


# ------------------------------------------------------------ 8. Couleurs
COLORS = [
    ("Noir fondateur", NOIR, "17 · 17 · 17", "0 · 0 · 0 · 93", "Textes, logo sur fond clair, pages fortes.", 30),
    ("Or excellence", OR, "245 · 197 · 24", "0 · 18 · 90 · 4", "Les marches, les accents, les grands aplats.", 15),
    ("Ivoire", IVOIRE, "250 · 247 · 240", "0 · 1 · 4 · 2", "Fond principal : documents, charte, supports.", 45),
    ("Vert réussite", VERT, "93 · 177 · 46", "47 · 0 · 74 · 31", "Uniquement pour valider : coche, badges, réussite.", 3),
    ("Sable", SABLE, "239 · 232 · 216", "0 · 3 · 10 · 6", "Surfaces claires secondaires, tableaux.", 5),
    ("Graphite", GRAPHITE, "42 · 42 · 42", "0 · 0 · 0 · 84", "Surfaces sombres secondaires.", 2),
]


def p08():
    cards = ""
    for name, hx, rgb, cmyk, use, _ in COLORS:
        dark = hx in (NOIR, GRAPHITE, VERT)
        fg = IVOIRE if dark else NOIR
        cards += f"""<div class="sw" style="background:{hx};color:{fg}">
  <div class="nm">{name}</div>
  <div class="codes"><div><span>HEX</span>{hx.upper()}</div><div><span>RVB</span>{rgb}</div><div><span>CMJN</span>{cmyk}</div></div>
  <div class="use">{use}</div></div>"""
    bar = "".join(f'<div style="flex:{c[5]};background:{c[1]}"></div>' for c in COLORS)
    legend = "".join(f'<span><i style="background:{hx}"></i>{name.split()[0]} {pct} %</span>' for name, hx, *_, pct in COLORS)
    acc = ""
    for name, hx in [("Or excellence", OR), ("Or bronze (texte)", OR_TEXTE), ("Vert réussite", VERT), ("Vert texte", VERT_TEXTE)]:
        r = contrast_ratio(hx, IVOIRE)
        rs = f"{r:.1f}".replace(".", ",")
        ok = r >= 4.5
        acc += (f'<div class="ac{" ok" if ok else ""}"><i style="background:{hx}"></i><div><b style="color:{hx if ok else NOIR}">{name}</b>'
                f'<span>{hx.upper()} · {rs}:1 sur ivoire · {"texte courant ✓" if ok else "grands aplats seulement"}</span></div></div>')
    inner_ = f"""
<div class="kicker">07 — Couleurs</div>
<h1 style="margin-top:10px">L'or pour briller, l'ivoire pour respirer.</h1>
<div class="grid">{cards}</div>
<div class="row2">
  <div><div class="lab">Proportions</div><div class="bar">{bar}</div><div class="legend">{legend}</div></div>
</div>
<div class="acc"><div class="lab">Texte sur fond clair — contraste vérifié (WCAG AA ≥ 4,5:1)</div><div class="accrow">{acc}</div></div>
<p class="note">L'or est magnifique en aplat, mais illisible en petit texte sur fond clair : pour les textes, utiliser l'Or bronze. Sur fond noir, l'or d'origine est parfait (11,6:1). CMJN indicatifs, à valider sur épreuve.</p>"""
    css = f"""
.grid{{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:22px}}
.sw{{height:232px;border-radius:10px;padding:14px;display:flex;flex-direction:column;justify-content:space-between}}
.sw[style*="{IVOIRE}"],.sw[style*="{SABLE}"]{{border:1px solid #E4DCCB}}
.nm{{font:700 15px/1.15 Quicksand}}
.codes{{font:600 9.5px/1.75 Nunito}} .codes span{{display:inline-block;width:34px;opacity:.6;font-weight:700}}
.use{{font-size:10.5px;line-height:1.35;opacity:.9}}
.row2{{margin-top:16px}} .bar{{display:flex;height:16px;border-radius:4px;overflow:hidden;border:1px solid #E4DCCB;margin-top:8px}}
.legend{{display:flex;gap:18px;font:600 10px Nunito;color:{GRIS};margin-top:6px}} .legend i{{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;border:1px solid #ccc;vertical-align:-1px}}
.acc{{margin-top:14px}} .accrow{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:8px}}
.ac{{display:flex;gap:10px;align-items:center;background:{BLANC};border-radius:8px;padding:9px 11px;border:1px solid transparent}}
.ac.ok{{border-color:#E4DCCB}} .ac i{{flex:none;width:24px;height:24px;border-radius:5px}}
.ac b{{display:block;font:700 12.5px Quicksand}} .ac span{{font:600 9.5px Nunito;color:{GRIS}}}
.note{{font-size:11.5px;margin-top:10px;color:{GRIS}}}
"""
    return page_shell(inner_, 8, "Couleurs", "light", css)


# ------------------------------------------------------------ 9. Typographie
def p09():
    inner_ = f"""
<div class="kicker">08 — Typographie</div>
<h1 style="margin-top:10px">Les polices du logo, enfin écrites noir sur blanc.</h1>
<div class="grid">
  <div class="f big"><div class="kicker">Titres — issue du logo</div><div class="spec" style="font:600 72px/1 Quicksand;letter-spacing:-2px">Quicksand</div>
    <div class="alpha" style="font:600 19px Quicksand">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div>
    <p>La police de « Step » dans le logo. Ronde, accessible, sérieuse sans être froide. Graisses 500 à 700 pour les titres.</p>
    <div class="w"><span style="font-weight:500">Medium 500</span><span style="font-weight:600">SemiBold 600</span><span style="font-weight:700">Bold 700</span></div></div>
  <div class="f"><div class="kicker">Accents — issue du logo</div><div class="spec" style="font:300 40px/1 Comfortaa">Comfortaa</div>
    <div style="font:700 11px Comfortaa;letter-spacing:3px">SUR-TITRES · ÉTIQUETTES · NIVEAUX</div>
    <p>La police de « ACADEMY ». Réservée aux sur-titres en capitales espacées et aux petites étiquettes. Jamais en texte long.</p></div>
  <div class="f"><div class="kicker">Texte courant</div><div class="spec" style="font:700 40px/1 Nunito">Nunito</div>
    <p style="font-size:13px;color:{NOIR}">Dans ce module, vous apprendrez à dessiner un plan de niveau complet sur AutoCAD, étape par étape.</p>
    <p>Arrondie comme les polices du logo, mais conçue pour la lecture : supports de cours, e-mails, site.</p></div>
  <div class="f wide"><div class="kicker">Hiérarchie type</div>
    <div class="h"><span style="font:600 26px Quicksand">Titre de module</span><span style="font:700 10px Comfortaa;letter-spacing:2.5px;color:{OR_TEXTE}">NIVEAU 2 · AUTOCAD</span><span style="font:400 13px Nunito">Texte courant en Nunito 11-13 pt, interligne 1,5.</span></div></div>
</div>
<p class="note">Trois polices gratuites (licence SIL Open Font), disponibles sur fonts.google.com. À installer avant d'utiliser les modèles PowerPoint et Word.</p>"""
    css = f"""
.grid{{display:grid;grid-template-columns:1.25fr 1fr 1fr;grid-template-rows:auto auto;gap:12px;margin-top:20px;grid-template-areas:'b f1 f2' 'b w w'}}
.f{{background:{BLANC};border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;gap:9px}}
.f.big{{grid-area:b}} .f.wide{{grid-area:w}}
.alpha{{line-height:1.5;color:{NOIR};margin-top:4px}}
.f p{{font-size:12px;margin:0}}
.w{{display:flex;flex-direction:column;gap:4px;font:22px Quicksand;margin-top:auto;padding-top:12px;border-top:1px solid #EFE8D8}}
.h{{display:flex;align-items:baseline;gap:22px;flex-wrap:wrap}}
.note{{font-size:11.5px;margin-top:12px;color:{GRIS}}}
"""
    return page_shell(inner_, 9, "Typographie", "light", css)


# ------------------------------------------------------------ 10. Fonds
def p10():
    variants = [("Ivoire · version principale", IVOIRE, "clair"), ("Blanc", BLANC, "clair"), ("Noir", NOIR, "sombre"),
                ("Graphite", GRAPHITE, "sombre"), ("Or · monochrome noir", OR, "noir"), ("Photo · monochrome blanc", "photo", "blanc")]
    cells = ""
    for lab, bg, th in variants:
        style = (f"background:linear-gradient(135deg,rgba(17,17,17,.55),rgba(17,17,17,.75)),repeating-linear-gradient(90deg,#6d6252 0 18px,#7b6f5c 18px 36px)"
                 if bg == "photo" else f"background:{bg}")
        fg = NOIR if bg in (IVOIRE, BLANC, OR) else IVOIRE
        cells += f'<div class="v" style="{style}"><span style="color:{fg}">{lab}</span>{sized(principal(th), h=196)}</div>'
    inner_ = f"""
<div class="kicker">09 — Déclinaisons sur fonds</div>
<h1 style="margin-top:10px">Du clair au sombre, sans jamais faiblir.</h1>
<div class="grid">{cells}</div>
<p class="note">Sur une photo, toujours poser un voile sombre (55 à 75 % de noir) avant le logo blanc. Sur l'or, uniquement le logo monochrome noir.</p>"""
    css = f"""
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}}
.v{{height:252px;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}}
.v[style*="{IVOIRE}"],.v[style*="#FFFFFF"]{{border:1px solid #E4DCCB}}
.v span{{position:absolute;top:10px;left:14px;font:700 9px Comfortaa;letter-spacing:1.8px;text-transform:uppercase}}
.v svg{{margin-top:14px}}
.note{{font-size:12px;margin-top:12px;color:{GRIS}}}
"""
    return page_shell(inner_, 10, "Fonds", "light", css)


# ------------------------------------------------------------ 11. Interdits
def p11():
    orig = img_uri(ROOT / "source" / "logo_original.jpg", 400)
    base = principal("clair")
    vb = " ".join(str(v) for v in VB_PRINCIPAL)
    body = inner(base)
    donts = [
        (f'<img src="{orig}" style="height:150px;border-radius:6px">', "Ne plus utiliser l'ancien fichier JPEG"),
        (f'<svg viewBox="{vb}" width="250" height="110" preserveAspectRatio="none">{body}</svg>', "Ne pas déformer"),
        (f'<svg viewBox="{vb}" height="150">{body.replace(OR, "#2F80ED")}</svg>', "Ne pas changer les couleurs"),
        (f'<div style="background:{OR};padding:12px;border-radius:6px">{sized(principal("clair"), h=126)}</div>', "Pas de logo couleur sur l'or"),
        (f'<div style="background:repeating-linear-gradient(45deg,#8a7d6a 0 10px,#b3a58f 10px 20px);padding:12px;border-radius:6px">{sized(principal("clair"), h=126)}</div>', "Pas de photo chargée sans voile"),
        (f'<div style="font:800 34px Georgia;font-style:italic;text-align:center;line-height:1.1">Step by Step<br><span style="font-size:22px">Academy</span></div>', "Ne pas réécrire le nom dans une autre police"),
    ]
    cells = "".join(f'<div class="x"><div class="art">{c}</div><div class="cap"><b>✕</b> {l}</div></div>' for c, l in donts)
    inner_ = f"""
<div class="kicker">10 — Usages interdits</div>
<h1 style="margin-top:10px">Six erreurs à ne plus jamais voir.</h1>
<div class="grid">{cells}</div>"""
    css = f"""
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}}
.x{{background:{BLANC};border-radius:10px;overflow:hidden}}
.art{{height:222px;display:flex;align-items:center;justify-content:center}}
.cap{{padding:10px 14px;font-size:12px;border-top:1px solid #EFE8D8}} .cap b{{color:#C62828;margin-right:6px}}
"""
    return page_shell(inner_, 11, "Interdits", "light", css)


# ------------------------------------------------------------ 12. Univers graphique : pôles, niveaux, motif
def p12():
    poles = "".join(f'<div class="pole"><div class="ic">{picto(k)}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in POLES)
    lv_names = ["Découvrir", "Comprendre", "Pratiquer", "Maîtriser", "Certifier"]
    niveaux = "".join(f'<div class="lv">{niveau(i + 1, 96, k=1.6)}<b>Niveau {i + 1}</b><span>{n}</span></div>' for i, n in enumerate(lv_names))
    fmts = "".join(f'<span class="tag">{t}</span>' for t in ("En ligne", "Présentiel", "À domicile"))
    parcours = ""
    for i, n in enumerate(lv_names):
        etat = "done" if i < 2 else ("now" if i == 2 else "todo")
        mark = "✓" if etat == "done" else str(i + 1)
        parcours += f'<div class="st {etat}" style="height:{26 + i * 9}px"><b>{mark}</b><span>{n}</span></div>'

    inner_ = f"""
<div class="kicker">11 — Univers graphique</div>
<h1 style="margin-top:10px">Cinq pôles, cinq niveaux, un seul escalier.</h1>
<div class="lab" style="margin-top:18px">Les pôles de formation · pictogrammes au trait, accent or</div>
<div class="poles">{poles}</div>
<div class="duo">
  <div class="card blk"><div class="lab">Les niveaux · le logo devient un indicateur de progression</div><div class="lvs">{niveaux}</div></div>
  <div class="card blk"><div class="lab">Formats</div><div class="tags">{fmts}</div>
    <div class="lab" style="margin-top:16px">Validation</div>
    <div class="tags"><span class="ok"><svg viewBox="0 0 20 20" width="14"><circle cx="10" cy="10" r="8" fill="none" stroke="{VERT}" stroke-width="2.4"/><path d="M6 10 L9 13 L14 7" fill="none" stroke="{VERT}" stroke-width="2.4" stroke-linecap="round"/></svg> Module validé</span></div></div>
</div>
<div class="card parc"><div class="lab">Composant « parcours » · supports de cours et pages web</div>
  <div class="steps">{parcours}</div></div>"""
    css = f"""
.poles{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:10px}}
.pole{{background:{BLANC};border-radius:10px;padding:18px 16px;min-height:190px}}
.ic{{width:52px;height:52px;border-radius:12px;background:{SABLE};display:flex;align-items:center;justify-content:center;margin-bottom:10px}}
.pole h3{{font-size:14px}} .pole p{{font-size:11px;line-height:1.45;margin-top:4px}}
.duo{{display:grid;grid-template-columns:1.8fr 1fr;gap:12px;margin-top:14px}}
.blk{{padding:18px 18px;min-height:170px}}
.lvs{{display:flex;gap:22px;margin-top:16px}} .lv{{display:flex;flex-direction:column;gap:5px}}
.lv b{{font:700 12.5px Quicksand}} .lv span{{font:600 11px Nunito;color:{GRIS}}}
.tags{{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}}
.parc{{margin-top:12px;padding:14px 18px}} .steps{{display:flex;align-items:flex-end;gap:6px;margin-top:10px}}
.st{{flex:1;border-radius:6px 6px 0 0;display:flex;align-items:flex-end;gap:8px;padding:0 10px 6px;font:700 11px Nunito}}
.st b{{font:700 11px Comfortaa}} .st.done{{background:{OR};color:{NOIR}}} .st.now{{background:{NOIR};color:{OR}}} .st.todo{{background:{SABLE};color:{GRIS}}}
.tag{{font:700 10px Comfortaa;letter-spacing:1px;background:{NOIR};color:{OR};border-radius:20px;padding:7px 12px}}
.ok{{display:inline-flex;gap:6px;align-items:center;font:700 11px Nunito;color:{VERT_TEXTE};background:#EEF6E8;border-radius:20px;padding:6px 12px}}
"""
    return page_shell(inner_, 12, "Univers graphique", "light", css)


# ------------------------------------------------------------ 13. Applications : attestation, carte, miniature de cours
def attestation_html(nom="Aminata Traoré", module="AutoCAD — Dessin technique 2D", niveau_n=3, date="15 octobre 2026", scale=1.0):
    return f"""<div class="att" style="transform:scale({scale});transform-origin:top left">
  <div class="att-l">{sized(principal('clair'), h=150)}<div class="att-m">{marches_motif_html()}</div></div>
  <div class="att-r">
    <div class="att-k">Attestation de réussite</div>
    <div class="att-t">Décernée à</div><div class="att-n">{nom}</div>
    <div class="att-t">pour avoir validé la formation</div><div class="att-mod">{module}</div>
    <div class="att-lv">{niveau(niveau_n, 90)}<span>Niveau {niveau_n} sur 5</span></div>
    <div class="att-f"><div><span>Date</span>{date}</div><div><span>Le formateur</span>Signature</div>
      <div class="seal"><svg viewBox="0 0 60 60" width="54"><circle cx="30" cy="30" r="26" fill="none" stroke="{VERT}" stroke-width="3.5"/><path d="M19 31 L27 39 L42 22" fill="none" stroke="{VERT}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
  </div></div>"""


def marches_motif_html():
    return "".join(f'<i style="width:{100 * w / 767:.0f}%"></i>' for w in LARGEURS)


ATT_CSS = f"""
.att{{width:842px;height:595px;background:{IVOIRE};display:grid;grid-template-columns:250px 1fr;position:relative;overflow:hidden}}
.att-l{{background:{BLANC};display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:40px 0 0}}
.att-m{{width:100%;display:flex;flex-direction:column;align-items:flex-end;gap:7px;padding-bottom:40px}} .att-m i{{display:block;height:20px;background:{OR}}}
.att-r{{padding:56px 60px 40px 56px;display:flex;flex-direction:column}}
.att-k{{font:700 12px Comfortaa;letter-spacing:4px;text-transform:uppercase;color:{OR_TEXTE}}}
.att-t{{font:400 14px Nunito;color:{GRIS};margin-top:22px}}
.att-n{{font:600 44px/1.1 Quicksand;color:{NOIR};margin-top:4px;border-bottom:2px solid {OR};padding-bottom:8px}}
.att-mod{{font:700 22px Quicksand;color:{NOIR};margin-top:4px}}
.att-lv{{display:flex;align-items:center;gap:12px;margin-top:18px;font:700 12px Nunito;color:{GRIS}}}
.att-f{{margin-top:auto;display:flex;gap:40px;align-items:flex-end;font:600 13px Nunito}} .att-f span{{display:block;font:700 9px Comfortaa;letter-spacing:1.5px;text-transform:uppercase;color:{GRIS};margin-bottom:4px}}
.att-f div:nth-child(2){{border-top:1px solid #CFC6B4;padding-top:6px;min-width:150px}} .seal{{margin-left:auto}}
"""


def p13():
    s = 0.62
    carte = f"""<div class="cv front">{sized(horizontal('sombre'), w=250)}</div>
<div class="cv back"><div><b>Prénom Nom</b><span>Formateur · Logiciels d'ingénierie</span></div>
<div class="ct">{EMAIL}<br>{TEL}<br>{PAYS}</div><div class="mk">{sized(compact('clair'), w=70)}</div></div>"""
    thumb = f"""<div class="yt"><div class="yt-l"><span class="yt-k">Cours en ligne · Niveau 1</span><div class="yt-t">AutoCAD<br>pour débutants</div>
<div class="yt-s">Leçon 03 · Les calques</div></div><div class="yt-r">{sized(symbole('sombre'), w=150)}</div>{niveau(1, 70)}</div>"""
    inner_ = f"""
<div class="kicker">12 — Applications</div>
<h1 style="margin-top:10px">Ce que l'apprenant garde en main.</h1>
<div class="wrap">
  <div><div class="attw">{attestation_html(scale=s)}</div><div class="lab" style="margin-top:10px">Attestation de réussite · A4 paysage · modèle Word fourni</div></div>
  <div class="col">{carte}<div class="lab">Carte de visite recto / verso</div>{thumb}<div class="lab">Miniature de cours en ligne · 1280 × 720</div></div>
</div>"""
    css = ATT_CSS + f"""
.wrap{{display:grid;grid-template-columns:530px 1fr;gap:24px;margin-top:20px}}
.attw{{width:{842 * s:.0f}px;height:{595 * s:.0f}px;box-shadow:0 12px 30px rgba(17,17,17,.12);border-radius:4px;overflow:hidden}}
.col{{display:flex;flex-direction:column;gap:8px}}
.cv{{height:92px;border-radius:8px;box-shadow:0 6px 16px rgba(17,17,17,.1)}}
.front{{background:{NOIR};display:flex;align-items:center;justify-content:center}}
.back{{background:{BLANC};display:grid;grid-template-columns:1fr auto;padding:12px 16px;position:relative}}
.back b{{font:700 14px Quicksand;display:block}} .back span{{font:600 10px Nunito;color:{OR_TEXTE}}}
.ct{{font:600 10px/1.5 Nunito;color:{GRIS};grid-column:1;align-self:end}} .mk{{grid-row:1/3;grid-column:2;align-self:center}}
.yt{{height:190px;border-radius:8px;background:{NOIR};position:relative;overflow:hidden;display:flex;margin-top:6px}}
.yt-l{{padding:18px 20px;flex:1;display:flex;flex-direction:column}}
.yt-k{{font:700 9px Comfortaa;letter-spacing:2px;text-transform:uppercase;color:{OR}}}
.yt-t{{font:700 30px/1.02 Quicksand;color:{IVOIRE};margin-top:10px}} .yt-s{{margin-top:auto;font:600 11px Nunito;color:#C9C2B4}}
.yt-r{{display:flex;align-items:center;padding-right:16px}} .yt>svg{{position:absolute;right:16px;bottom:14px}}
"""
    return page_shell(inner_, 13, "Applications", "light", css)


# ------------------------------------------------------------ 14. Supports numériques
def p14():
    d = ROOT / "pack" / "05_Supports_numeriques"
    def im(name, w):
        f = d / f"{name}.png"
        return f'<img src="{img_uri(f, w)}">' if f.exists() else '<div class="miss">à générer</div>'
    inner_ = f"""
<div class="kicker">13 — Supports numériques</div>
<h1 style="margin-top:10px">Prêts à publier, dès aujourd'hui.</h1>
<div class="r1">
  <figure>{im("Banniere_Facebook_1640x624", 1300)}<figcaption>Couverture Facebook · 1640 × 624</figcaption></figure>
  <figure>{im("Photo_de_profil_1080x1080", 500)}<figcaption>Photo de profil</figcaption></figure>
  <figure>{im("Statut_WhatsApp_1080x1920", 400)}<figcaption>Statut WhatsApp</figcaption></figure>
</div>
<div class="r2">
  <figure>{im("Post_formation_1080x1350", 500)}<figcaption>Annonce de formation</figcaption></figure>
  <figure>{im("Miniature_cours_1280x720", 900)}<figcaption>Miniature de cours · 1280 × 720</figcaption></figure>
  <figure>{im("Post_reussite_1080x1080", 500)}<figcaption>Félicitations</figcaption></figure>
  <figure>{im("Banniere_LinkedIn_1584x396", 900)}<figcaption>Bannière LinkedIn</figcaption></figure>
</div>"""
    css = f"""
figure{{margin:0}} figure img{{display:block;border-radius:6px;box-shadow:0 6px 18px rgba(17,17,17,.14)}}
figcaption{{font:700 8.5px Comfortaa;letter-spacing:1.2px;color:{GRIS};margin-top:6px;text-transform:uppercase}}
.r1,.r2{{display:flex;gap:14px;align-items:flex-start}} .r1{{margin-top:16px}} .r2{{margin-top:12px}}
.r1 img{{height:228px;width:auto}} .r2 img{{height:196px;width:auto}} .r2 figure:last-child img{{height:auto;width:230px;margin-top:0}}
.miss{{height:120px;border:1px dashed #B9B0A0;border-radius:6px;display:flex;align-items:center;justify-content:center;font:600 11px Nunito;color:{GRIS}}}
"""
    return page_shell(inner_, 14, "Supports", "light", css)


# ------------------------------------------------------------ 15. Mises en situation (bento)
BENTO = {
    "01": ("Salle de formation", "50% 50%"),
    "02": ("Cours en ligne", "50% 30%"),
    "03": ("Enseigne de façade", "50% 50%"),
    "04": ("Attestation remise", "50% 45%"),
    "05": ("Cours à domicile", "50% 50%"),
    "06": ("Polo du formateur", "50% 45%"),
}


def p15():
    d = ROOT / "mockups" / "images"
    img = {n: next(iter(sorted(d.glob(f"{n}_*.*"))), None) if d.exists() else None for n in BENTO}
    order = [("a", "01"), ("b", "02"), ("c", "03"), ("d", "04"), ("e", "05"), ("f", "06")]
    cells = ""
    for area, n in order:
        title, pos = BENTO[n]
        if img[n]:
            content = f'<img src="{img_uri(img[n], 1300)}" style="object-position:{pos}">'
        else:
            content = f'<div class="ph">{sized(compact("sombre"), w=80)}<span>Image {n} à venir</span></div>'
        cells += f'<div class="t {area}">{content}<div class="cap"><b>{n}</b>{title}</div></div>'
    inner_ = f"""
<div class="kicker">14 — Mises en situation</div>
<h1 style="margin-top:10px;color:{IVOIRE}">La marque, là où l'on apprend.</h1>
<div class="bento">{cells}</div>"""
    css = f"""
.bento{{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,172px);gap:10px;margin-top:22px;
  grid-template-areas:'a a b b' 'a a c d' 'e f f d'}}
.a{{grid-area:a}} .b{{grid-area:b}} .c{{grid-area:c}} .d{{grid-area:d}} .e{{grid-area:e}} .f{{grid-area:f}}
.t{{position:relative;border-radius:10px;overflow:hidden;background:{GRAPHITE}}}
.t img{{width:100%;height:100%;object-fit:cover;display:block}}
.ph{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;
  font:700 9.5px Comfortaa;letter-spacing:2px;text-transform:uppercase;color:#6d665c;opacity:.9}}
.ph svg{{opacity:.25}}
.cap{{position:absolute;left:10px;bottom:10px;background:rgba(17,17,17,.82);color:{IVOIRE};font:700 10px Nunito;padding:5px 9px;border-radius:5px;display:flex;gap:7px}}
.cap b{{font:700 10px Comfortaa;color:{OR}}}
"""
    return page_shell(inner_, 15, "Mises en situation", "dark", css)


# ------------------------------------------------------------ 16. Contact (fin)
def p16():
    inner_ = f"""
<svg class="mt" viewBox="0 0 560 280" width="560">{marches_motif(0, 0, 560, 44, 14)}</svg>
<div class="lg">{sized(principal('sombre'), h=330)}</div>
<div class="txt"><div class="kicker">La progression, étape par étape.</div>
<h1 style="color:{IVOIRE};margin-top:12px">Prêts pour la<br>première marche ?</h1>
<div class="ct"><div><span>E-mail</span>{EMAIL}</div><div><span>Téléphone · WhatsApp</span>{TEL}</div><div><span>Pays</span>{PAYS}</div></div></div>"""
    css = f"""
.mt{{position:absolute;left:0;bottom:70px;opacity:.95}}
.lg{{position:absolute;right:80px;top:70px}}
.txt{{position:absolute;left:72px;top:80px;width:520px}}
.txt h1{{font-size:46px;line-height:1.05}}
.ct{{margin-top:34px;display:flex;flex-direction:column;gap:14px;font:600 17px Nunito;color:{IVOIRE}}}
.ct span{{display:block;font:700 9px Comfortaa;letter-spacing:2px;text-transform:uppercase;color:{OR};margin-bottom:3px}}
"""
    return page_shell(inner_, 16, "Contact", "dark", css)


PAGES = [p06, p07, p08, p09, p10, p11, p12, p13, p14, p15, p16]
