"""CivRebar AI — générateur de carrousels quotidiens (affiches à faire glisser).

    python3 carrousels.py            → toutes les publications de contenu.py
    python3 carrousels.py J03 J07    → seulement celles-ci

Pour chaque publication, dans out/<Jxx_nom>/ :
    4x5/01.png …   1080 x 1350 : Instagram, Facebook, LinkedIn
    9x16/01.png …  1080 x 1920 : TikTok (mode photo), Statuts WhatsApp, stories
    LinkedIn.pdf   le carrousel en document (format recommandé sur LinkedIn)
    legendes.txt   les textes à coller sous la publication, par réseau
    apercu.jpg     planche de contrôle
Et out/PLANNING.md : le calendrier de publication.
"""
import html
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "src"))
from brand import NUIT, ACIER, CUIVRE, CUIVRE_CLAIR, SIGNAL, BETON, CHAUX, CUIVRE_TEXTE, SIGNAL_TEXTE, font_css  # noqa: E402
from contenu import POSTS, HASHTAGS  # noqa: E402

PACK = HERE.parent / "CivRebar_AI_Pack_Logo"
OUT = HERE / "out"
FONTS = font_css()
W = 1080
FORMATS = {"4x5": 1350, "9x16": 1920}

THEMES = {
    "nuit": dict(bg=NUIT, ink=CHAUX, muted="#aeb7c2", cu=CUIVRE, cu_s=CUIVRE_CLAIR, si=SIGNAL, line="#1d2e42", card=ACIER, stir="#2a3b50"),
    "chaux": dict(bg=CHAUX, ink=NUIT, muted="#56606d", cu=CUIVRE, cu_s=CUIVRE_TEXTE, si=SIGNAL_TEXTE, line="#e2ddd3", card="#E9E4DA", stir="#d6d0c4"),
}


# ------------------------------------------------------------ logo et symbole (fichiers officiels du pack)
def _svg(path, w, recolor=None):
    s = (PACK / path).read_text()
    for a, b in (recolor or {}).items():
        s = s.replace(a, b)
    return s.replace("<svg ", f'<svg width="{w}" ', 1)


def logo_vertical(theme, w):
    # sur fond Nuit : barre et nom en Blanc chaux, comme la version horizontale « pour fond sombre »
    rec = {'"#0B1624"': f'"{CHAUX}"'} if theme == "nuit" else None
    return _svg("01_Logo_principal_avec_nom/CivRebar_AI_logo_vertical_couleur.svg", w, rec)


def logo_horizontal(theme, w):
    f = "couleur_pour_fond_sombre" if theme == "nuit" else "couleur"
    return _svg(f"01_Logo_principal_avec_nom/CivRebar_AI_logo_horizontal_{f}.svg", w)


# Le « R façonné » décomposé en ses cinq pièces (voir la charte, page du symbole)
SYM_PARTS = {
    "fut": '<path d="M50 230 V90"/>',
    "panse": '<path d="M50 90 A50 50 0 0 1 100 40 H120 A60 60 0 0 1 120 160 H100"/>',
    "crochet": '<path d="M100 160 A20 20 0 0 1 85.86 125.86 L105.86 105.86"/>',
    "relevee": '<path d="M120 160 L180 220 H210"/>',
}


def symbol_focus(t, focus, w):
    """Symbole avec une pièce en couleur et le reste estompé."""
    dim = t["line"] if t["bg"] == NUIT else "#d9d3c8"
    col = {"fut": t["ink"], "panse": t["ink"], "crochet": t["ink"], "relevee": CUIVRE}
    g = ""
    for k, p in SYM_PARTS.items():
        on = focus in (k, "tout")
        g += p.replace("<path ", f'<path stroke="{col[k] if on else dim}" ')
    node_on = focus in ("noeud", "tout")
    halo = f'<circle cx="100" cy="140" r="26" fill="{SIGNAL}" opacity=".18"/>' if focus == "noeud" else ""
    return (f'<svg width="{w}" viewBox="20 20 210 230"><g fill="none" stroke-width="20" stroke-linejoin="round">{g}</g>'
            f'{halo}<circle cx="100" cy="140" r="{9 if focus == "noeud" else 7}" fill="{SIGNAL if node_on else dim}"/></svg>')


# ------------------------------------------------------------ illustrations techniques
def beam_svg(t, w, labels=True, spacing="e = 15 cm", length="L = 5,40 m"):
    st = "".join(f'<line x1="{x}" y1="44" x2="{x}" y2="156" stroke="{t["ink"]}" stroke-width="3" opacity=".85"/>'
                 for x in range(64, 940, 24))
    lab = ""
    if labels:
        lab = (f'<line x1="40" y1="232" x2="960" y2="232" stroke="{t["muted"]}" stroke-width="2"/>'
               f'<path d="M34 240 L46 224 M954 240 L966 224 M40 214 V250 M960 214 V250" stroke="{t["muted"]}" stroke-width="2"/>'
               f'<rect x="400" y="214" width="200" height="36" fill="{t["bg"]}"/>'
               f'<text x="500" y="241" text-anchor="middle" font-family="Mono" font-size="28" fill="{t["ink"]}">{length}</text>'
               f'<text x="40" y="18" font-family="Mono" font-size="24" fill="{t["cu_s"]}">2 HA14</text>'
               f'<text x="90" y="200" font-family="Mono" font-size="24" fill="{t["cu_s"]}">3 HA20</text>'
               f'<text x="500" y="18" text-anchor="middle" font-family="Mono" font-size="24" fill="{t["ink"]}">Cadres HA8 — {spacing}</text>')
    return f"""<svg width="{w}" viewBox="0 -10 1000 270">
<rect x="20" y="30" width="960" height="140" fill="none" stroke="{t["muted"]}" stroke-width="3"/>
<rect x="20" y="170" width="50" height="40" fill="none" stroke="{t["muted"]}" stroke-width="3"/>
<rect x="930" y="170" width="50" height="40" fill="none" stroke="{t["muted"]}" stroke-width="3"/>
{st}
<path d="M40 90 V52 H960 V90" fill="none" stroke="{CUIVRE}" stroke-width="9" stroke-linejoin="round"/>
<path d="M40 110 V148 H960 V110" fill="none" stroke="{CUIVRE}" stroke-width="9" stroke-linejoin="round"/>
{lab}</svg>"""


def icon(kind, t, w=260):
    """Petits pictogrammes : barres, cadres, cotes, repères."""
    ink, m = t["ink"], t["muted"]
    body = {
        "barres": f'<path d="M20 70 V40 H180 V70" stroke="{CUIVRE}" stroke-width="12" fill="none" stroke-linejoin="round"/>'
                  f'<path d="M20 130 V160 H180 V130" stroke="{CUIVRE}" stroke-width="12" fill="none" stroke-linejoin="round"/>',
        "cadres": f'<rect x="50" y="30" width="100" height="140" rx="6" stroke="{ink}" stroke-width="10" fill="none"/>'
                  f'<path d="M58 44 L92 78" stroke="{ink}" stroke-width="10"/><circle cx="68" cy="46" r="8" fill="{CUIVRE}"/>'
                  f'<circle cx="132" cy="46" r="8" fill="{CUIVRE}"/><circle cx="68" cy="154" r="8" fill="{CUIVRE}"/><circle cx="132" cy="154" r="8" fill="{CUIVRE}"/>',
        "cotes": f'<line x1="20" y1="100" x2="180" y2="100" stroke="{ink}" stroke-width="5"/>'
                 f'<path d="M12 112 L28 88 M172 112 L188 88 M20 70 V130 M180 70 V130" stroke="{ink}" stroke-width="5"/>'
                 f'<text x="100" y="80" text-anchor="middle" font-family="Mono" font-size="26" fill="{t["si"]}">5,40</text>',
        "reperes": f'<line x1="40" y1="150" x2="180" y2="150" stroke="{CUIVRE}" stroke-width="10"/>'
                   f'<line x1="90" y1="150" x2="120" y2="80" stroke="{m}" stroke-width="4"/>'
                   f'<circle cx="130" cy="58" r="34" fill="none" stroke="{ink}" stroke-width="5"/>'
                   f'<text x="130" y="70" text-anchor="middle" font-family="Sora" font-weight="600" font-size="34" fill="{ink}">3</text>',
    }[kind]
    return f'<svg width="{w}" viewBox="0 0 200 200">{body}</svg>'


def rebar_band(t, i, n, h):
    """Barre cuivre continue d'une affiche à l'autre : elle invite à glisser et relie tout le carrousel."""
    y = 40
    phase = (i * W) % 48
    stirrups = "".join(f'<line x1="{x}" y1="{y - 22}" x2="{x}" y2="{y + 22}" stroke="{t["stir"]}" stroke-width="3"/>'
                       for x in range(24 - phase, W, 48))
    x0 = 90 if i == 0 else 0
    x1 = W - 90 if i == n - 1 else W
    hook0 = f'<path d="M{x0} {y} V{y - 34}" stroke="{CUIVRE}" stroke-width="10"/>' if i == 0 else ""
    hook1 = f'<path d="M{x1} {y} V{y - 34}" stroke="{CUIVRE}" stroke-width="10"/>' if i == n - 1 else ""
    return (f'<svg class="band" width="{W}" height="80">{stirrups}'
            f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{CUIVRE}" stroke-width="10"/>{hook0}{hook1}</svg>')


# ------------------------------------------------------------ modèles d'affiches
def esc(s):
    """Texte sûr, avec **gras cuivre** et retours à la ligne « / »."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<em class="hl">\1</em>', s)
    s = re.sub(r" ([?!:;»])", "\u00a0\\1", s).replace("« ", "«\u00a0")  # espaces insécables à la française
    return s.replace(" / ", "<br>")


def slide_html(post, s, i, n, fmt):
    t = THEMES[s.get("theme", post["theme"])]
    H = FORMATS[fmt]
    kind = s["t"]
    tall = fmt == "9x16"
    kick = esc(s.get("kicker", post["kicker"]))
    if kind == "cover":
        main = f"""<div class="ghost">{symbol_focus(t, "tout", 900)}</div>
<div class="kick">{kick}</div>
<h1 class="cover">{esc(s["title"])}</h1>
{f'<p class="lead">{esc(s["sub"])}</p>' if s.get("sub") else ""}
<div class="swipe">Glisse <span>→</span></div>"""
    elif kind == "text":
        num = f'<div class="num">{esc(s["num"])}</div>' if s.get("num") else ""
        ill = s.get("icon")
        main = f"""{num}{f'<div class="ill">{icon(ill, t)}</div>' if ill else ""}
<h2>{esc(s["title"])}</h2>{f'<p class="body">{esc(s["body"])}</p>' if s.get("body") else ""}"""
    elif kind == "big":
        size = "" if len(s["big"]) <= 4 else ' style="font-size:140px;letter-spacing:-4px"'
        main = f"""<div class="huge"{size}>{esc(s["big"])}</div>{f'<p class="body center">{esc(s["body"])}</p>' if s.get("body") else ""}"""
    elif kind == "quote":
        main = f"""<div class="qmark">«</div><blockquote>{esc(s["quote"])}</blockquote>
{f'<div class="by">{esc(s["by"])}</div>' if s.get("by") else ""}"""
    elif kind == "compare":
        main = f"""<h2 class="small">{esc(s.get("title", ""))}</h2>
<div class="cmp bad"><div class="tag">{esc(s.get("a_label", "Mythe"))}</div><p>{esc(s["a"])}</p></div>
<div class="cmp good"><div class="tag">{esc(s.get("b_label", "Réalité"))}</div><p>{esc(s["b"])}</p></div>"""
    elif kind == "fields":
        rows = "".join(f'<div class="row"><span>{esc(k)}</span><b>{esc(v)}</b></div>' for k, v in s["fields"])
        main = f"""{f'<div class="num">{esc(s["num"])}</div>' if s.get("num") else ""}<h2>{esc(s["title"])}</h2>
<div class="panel"><div class="ph">CIVREBAR AI · POUTRE</div>{rows}{f'<div class="btn">{esc(s["button"])}</div>' if s.get("button") else ""}</div>
{f'<p class="body">{esc(s["body"])}</p>' if s.get("body") else ""}"""
    elif kind == "beam":
        main = f"""{f'<div class="num">{esc(s["num"])}</div>' if s.get("num") else ""}<h2>{esc(s["title"])}</h2>
<div class="ill wide">{beam_svg(t, 900, s.get("labels", True), s.get("spacing", "e = 15 cm"))}</div>
{f'<p class="body">{esc(s["body"])}</p>' if s.get("body") else ""}"""
    elif kind == "symbol":
        main = f"""<div class="ill sym">{symbol_focus(t, s["focus"], 330 if not tall else 400)}</div>
{f'<div class="num">{esc(s["num"])}</div>' if s.get("num") else ""}<h2>{esc(s["title"])}</h2><p class="body">{esc(s["body"])}</p>"""
    elif kind == "steps":
        items = "".join(f'<div class="step{" on" if j == len(s["steps"]) - 1 else ""}"><i></i><div><b>{esc(a)}</b><p>{esc(b)}</p></div></div>'
                        for j, (a, b) in enumerate(s["steps"]))
        main = f"""<h2 class="small">{esc(s["title"])}</h2><div class="steps">{items}</div>"""
    elif kind == "cta":
        acts = "".join(f"<span>{esc(a)}</span>" for a in s.get("actions", ["Abonne-toi", "Partage", "Enregistre"]))
        main = f"""<div class="logo">{logo_vertical(s.get("theme", post["theme"]), 360)}</div>
<h2 class="center">{esc(s["title"])}</h2>{f'<p class="body center">{esc(s["body"])}</p>' if s.get("body") else ""}
<div class="acts">{acts}</div>"""
    else:
        raise ValueError(kind)

    small_logo = "" if kind in ("cta",) else f'<div class="mini">{logo_horizontal(s.get("theme", post["theme"]), 230)}</div>'
    counter = f'<div class="count">{i + 1:02d} / {n:02d}</div>'
    arrow = "" if i == n - 1 or kind == "cover" else '<div class="next">→</div>'
    pad_top, pad_bot, pad_r = (250, 470, 150) if tall else (90, 190, 90)
    band_bottom = 380 if tall else 70
    css = f"""{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;background:{t["bg"]};color:{t["ink"]};font-family:Manrope;position:relative}}
.grid{{position:absolute;inset:0;background-image:linear-gradient({t["line"]} 1.5px,transparent 1.5px),linear-gradient(90deg,{t["line"]} 1.5px,transparent 1.5px);background-size:54px 54px;opacity:.55}}
.frame{{position:absolute;left:90px;right:{pad_r}px;top:{pad_top}px;bottom:{pad_bot}px;display:flex;flex-direction:column;justify-content:center}}
.top{{position:absolute;left:90px;right:{pad_r}px;top:{pad_top - 40 if not tall else pad_top - 90}px;display:flex;justify-content:space-between;align-items:center}}
.mini svg{{display:block}}
.count{{font:500 22px Mono;letter-spacing:.2em;color:{t["muted"]}}}
.band{{position:absolute;left:0;bottom:{band_bottom}px}}
.next{{position:absolute;right:{pad_r - 10}px;bottom:{band_bottom + 70}px;font:600 64px Sora;color:{t["cu"]}}}
.kick{{font:500 24px Mono;letter-spacing:.22em;text-transform:uppercase;color:{t["si"]};margin-bottom:34px}}
h1.cover{{font:600 {104 if tall else 96}px/1.04 Sora;letter-spacing:-3px}}
h2{{font:600 {76 if tall else 70}px/1.1 Sora;letter-spacing:-2px;margin-bottom:30px}}
h2.small{{font-size:{58 if tall else 54}px;margin-bottom:40px}}
.hl{{font-style:normal;color:{t["cu"]}}}
.lead{{font:500 40px/1.45 Manrope;color:{t["muted"]};margin-top:36px;max-width:820px}}
.body{{font:500 {40 if tall else 38}px/1.5 Manrope;color:{t["muted"]};max-width:860px}}
.body .hl{{color:{t["cu_s"]}}}
.center{{text-align:center;margin-left:auto;margin-right:auto}}
.num{{font:700 150px/1 Sora;color:{t["cu"]};margin-bottom:24px;letter-spacing:-4px}}
.huge{{font:700 {230 if tall else 210}px/1 Sora;color:{t["cu"]};text-align:center;letter-spacing:-8px;margin-bottom:40px}}
.ill{{margin-bottom:40px}}
.ill.wide svg{{max-width:100%}}
.ill.sym{{align-self:center}}
.qmark{{font:400 220px/0.6 InstrumentSerif;color:{t["cu"]};height:140px}}
blockquote{{font:italic 400 {84 if tall else 78}px/1.18 InstrumentSerif}}
.by{{font:500 24px Mono;letter-spacing:.2em;text-transform:uppercase;color:{t["muted"]};margin-top:40px}}
.swipe{{margin-top:60px;align-self:flex-start;font:600 34px Sora;color:{NUIT};background:{CUIVRE};padding:18px 34px;border-radius:60px}}
.swipe span{{margin-left:10px}}
.ghost{{position:absolute;right:-300px;top:{-60 if not tall else 120}px;opacity:{.07 if t["bg"] == NUIT else .05}}}
.cmp{{border-radius:22px;padding:34px 40px;margin-bottom:26px}}
.cmp .tag{{font:500 22px Mono;letter-spacing:.22em;text-transform:uppercase;margin-bottom:14px}}
.cmp p{{font:600 {44 if tall else 42}px/1.3 Sora;letter-spacing:-1px}}
.cmp.bad{{border:3px dashed {t["muted"]};opacity:.75}}
.cmp.bad p{{text-decoration:line-through;text-decoration-thickness:4px;text-decoration-color:{t["cu"]}}}
.cmp.bad .tag{{color:{t["muted"]}}}
.cmp.good{{background:{t["card"]};border-left:12px solid {t["cu"]}}}
.cmp.good .tag{{color:{t["si"]}}}
.panel{{background:{ACIER};border-radius:22px;padding:30px 36px;margin:10px 0 36px;color:{CHAUX}}}
.panel .ph{{font:500 20px Mono;letter-spacing:.2em;color:{BETON};margin-bottom:16px}}
.panel .row{{display:flex;justify-content:space-between;font:400 30px Mono;padding:16px 0;border-bottom:1.5px solid #2a3b50}}
.panel .row span{{color:{BETON}}}
.panel .btn{{margin-top:24px;margin-left:auto;width:max-content;background:{CUIVRE};color:{NUIT};font:500 26px Mono;letter-spacing:.2em;padding:16px 34px;border-radius:12px}}
.steps{{position:relative;padding-left:70px}}
.steps:before{{content:"";position:absolute;left:18px;top:20px;bottom:20px;width:8px;background:{CUIVRE}}}
.step{{position:relative;margin-bottom:{40 if tall else 30}px}}
.step i{{position:absolute;left:-66px;top:8px;width:36px;height:36px;border-radius:50%;background:{t["ink"]};border:6px solid {t["bg"]}}}
.step.on i{{background:{SIGNAL};box-shadow:0 0 0 10px rgba(53,208,222,.2)}}
.step b{{font:600 {40 if tall else 38}px Sora;display:block}}
.step p{{font:500 {30 if tall else 29}px/1.4 Manrope;color:{t["muted"]};margin-top:6px}}
.logo{{align-self:center;margin-bottom:50px}}
.acts{{display:flex;gap:18px;justify-content:center;margin-top:44px;flex-wrap:wrap}}
.acts span{{font:500 24px Mono;letter-spacing:.14em;text-transform:uppercase;border:2.5px solid {t["cu"]};color:{t["cu_s"]};padding:14px 24px;border-radius:40px}}
"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="grid"></div>
<div class="top">{small_logo if kind != "cover" else logo_horizontal(s.get("theme", post["theme"]), 260)}{counter}</div>
<div class="frame">{main}</div>
{rebar_band(t, i, n, H)}{arrow}
</body></html>"""


# ------------------------------------------------------------ légendes
def captions(post):
    tags = " ".join(post.get("hashtags", []) + HASHTAGS)
    c = post["legende"].strip()
    court = post["court"].strip()
    return f"""=== TIKTOK (mode photo) ===
{court}

{tags}

=== FACEBOOK / INSTAGRAM ===
{c}

{tags}

=== LINKEDIN (joindre LinkedIn.pdf comme document) ===
{c}

{" ".join((post.get("hashtags", []) + HASHTAGS)[:5])}
"""


# ------------------------------------------------------------ production
def build(posts):
    OUT.mkdir(exist_ok=True)
    tmp = OUT / "_html"
    tmp.mkdir(exist_ok=True)
    jobs = []
    for p in posts:
        d = OUT / p["id"]
        n = len(p["slides"])
        for fmt, H in FORMATS.items():
            (d / fmt).mkdir(parents=True, exist_ok=True)
            for i, s in enumerate(p["slides"]):
                f = tmp / f'{p["id"]}_{fmt}_{i + 1:02d}.html'
                f.write_text(slide_html(p, s, i, n, fmt))
                jobs.append(f"{f}|{d / fmt / f'{i + 1:02d}.png'}|{W}|{H}")
        (d / "legendes.txt").write_text(captions(p))
    env = {**os.environ, "NODE_PATH": subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()}
    for k in range(0, len(jobs), 40):
        subprocess.run(["node", str(HERE.parent / "src" / "render_png.js"), *jobs[k:k + 40]], check=True, env=env)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()
    from PIL import Image
    for p in posts:
        d = OUT / p["id"]
        imgs = [Image.open(d / "4x5" / f"{i + 1:02d}.png").convert("RGB") for i in range(len(p["slides"]))]
        imgs[0].save(d / "LinkedIn.pdf", save_all=True, append_images=imgs[1:], resolution=150)
        th = [im.resize((270, 338)) for im in imgs]
        sheet = Image.new("RGB", (270 * len(th) + 10 * (len(th) - 1), 338), "#000")
        for i, im in enumerate(th):
            sheet.paste(im, (i * 280, 0))
        sheet.save(d / "apercu.jpg", quality=85)
    plan = ["# Planning de publication — carrousels CivRebar AI", "",
            "Une publication par jour. Publier le même carrousel sur tous les réseaux le même jour.", "",
            "| Jour | Publication | Affiches | Objectif |", "|---|---|---|---|"]
    for p in POSTS:
        plan.append(f'| {p["id"][:3]} | {p["titre"]} | {len(p["slides"])} | {p["objectif"]} |')
    plan += ["", "Formats : `4x5/` pour Instagram, Facebook et LinkedIn ; `9x16/` pour TikTok (mode photo) et les Statuts WhatsApp ;",
             "`LinkedIn.pdf` à publier comme « document » sur LinkedIn. Textes prêts à coller dans `legendes.txt`."]
    (OUT / "PLANNING.md").write_text("\n".join(plan) + "\n")


if __name__ == "__main__":
    ids = sys.argv[1:]
    build([p for p in POSTS if not ids or p["id"][:3] in ids])
