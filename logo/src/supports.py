"""Supports numériques : réseaux sociaux et écran de démarrage du plugin (PNG).
python3 supports.py  →  CivRebar_AI_Pack_Logo/05_Supports_numeriques/"""
import os
import pathlib
import subprocess

from brand import NUIT, ACIER, CUIVRE, CUIVRE_CLAIR, SIGNAL, BETON, CHAUX, font_css
from lockup import logo_horizontal, logo_vertical, symbol
from pages_a import sized

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "CivRebar_AI_Pack_Logo" / "05_Supports_numeriques"
TMP = ROOT / "out" / "supports"
FONTS = font_css()


def trame(w, h, step=48, color=ACIER, bars=True, y0=None):
    """Filigrane d'étriers verticaux + deux barres filantes, comme sur la couverture."""
    ls = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(step // 2, w, step))
    y0 = y0 or int(h * 0.78)
    b = (f'<line x1="0" y1="{y0}" x2="{w}" y2="{y0}" stroke="{color}" stroke-width="{max(6, h // 90)}"/>'
         f'<line x1="0" y1="{y0 + h // 22}" x2="{w}" y2="{y0 + h // 22}" stroke="{color}" stroke-width="{max(6, h // 90)}"/>') if bars else ""
    return f'<svg class="trame" width="{w}" height="{h}"><g stroke="{color}" stroke-width="1.2" opacity=".7">{ls}</g>{b}</svg>'


def doc(w, h, body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w}px;height:{h}px;overflow:hidden;background:{NUIT};color:{CHAUX};font-family:Manrope;position:relative}}
.trame{{position:absolute;inset:0}}
.serif{{font-family:InstrumentSerif;font-style:italic}}
.mono{{font-family:Mono;letter-spacing:.2em;text-transform:uppercase}}
{css}</style></head><body>{body}</body></html>"""


def logo_dark(w):
    return sized(logo_horizontal(bar=CHAUX, text=CHAUX)[0], w=w)


def ghost(w):
    return sized(symbol(bar="#13233A", accent="#162840", noeud="#162840"), w=w)


SUPPORTS = {
    # nom : (largeur, hauteur, html)
    "Photo_de_profil_1080x1080": (1080, 1080, lambda: doc(1080, 1080, f"""
{trame(1080, 1080, 60, bars=False)}
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{sized(symbol(bar=CHAUX), w=560)}</div>""")),

    "Banniere_LinkedIn_1584x396": (1584, 396, lambda: doc(1584, 396, f"""
{trame(1584, 396, 44, y0=330)}
<div style="position:absolute;right:-40px;top:-60px">{ghost(520)}</div>
<div style="position:absolute;left:460px;top:120px">{logo_dark(520)}</div>
<div class="serif" style="position:absolute;left:462px;top:232px;font-size:40px;color:{CUIVRE_CLAIR}">L'intelligence de l'armature.</div>""")),

    "Couverture_Facebook_1640x624": (1640, 624, lambda: doc(1640, 624, f"""
{trame(1640, 624, 48, y0=520)}
<div style="position:absolute;right:-30px;top:-40px">{ghost(700)}</div>
<div style="position:absolute;left:120px;top:210px">{logo_dark(640)}</div>
<div class="serif" style="position:absolute;left:124px;top:350px;font-size:48px;color:{CUIVRE_CLAIR}">L'intelligence de l'armature.</div>""")),

    "Post_annonce_1080x1350": (1080, 1350, lambda: doc(1080, 1350, f"""
{trame(1080, 1350, 54, y0=1130)}
<div style="position:absolute;right:-200px;top:-140px;opacity:.8">{ghost(640)}</div>
<div class="mono" style="position:absolute;left:90px;top:96px;font-size:22px;color:{CUIVRE}">Bientôt · Étape 01</div>
<div style="position:absolute;left:90px;top:420px;font:600 92px/1.02 Sora;letter-spacing:-3px">Le ferraillage<br>d'une poutre,<br><span style="color:{CUIVRE_CLAIR}">en une commande.</span></div>
<div style="position:absolute;left:92px;top:820px;font:400 30px/1.5 Manrope;color:#aeb7c2;width:780px">Vous saisissez la section, la portée et les armatures. CivRebar AI dessine barres, cadres, cotes et repères dans AutoCAD.</div>
<div style="position:absolute;left:90px;bottom:96px">{logo_dark(460)}</div>""")),

    "Post_citation_1080x1080": (1080, 1080, lambda: doc(1080, 1080, f"""
{trame(1080, 1080, 54, y0=880)}
<div class="mono" style="position:absolute;left:92px;top:96px;font-size:22px;color:{CUIVRE}">Manifeste</div>
<div class="serif" style="position:absolute;left:90px;top:300px;width:900px;font-size:104px;line-height:1.05">« Ce qui tient un ouvrage <span style="color:{CUIVRE_CLAIR}">ne se voit pas.</span> »</div>
<div style="position:absolute;left:90px;bottom:90px">{logo_dark(420)}</div>""")),

    "Ecran_demarrage_plugin_1280x720": (1280, 720, lambda: doc(1280, 720, f"""
{trame(1280, 720, 40, y0=600)}
<div style="position:absolute;right:-60px;top:-30px">{ghost(560)}</div>
<div style="position:absolute;left:96px;top:240px">{logo_dark(560)}</div>
<div class="serif" style="position:absolute;left:98px;top:360px;font-size:36px;color:{CUIVRE_CLAIR}">L'intelligence de l'armature.</div>
<div style="position:absolute;left:98px;top:470px;width:360px;height:3px;background:{ACIER}"><div style="width:62%;height:100%;background:{SIGNAL}"></div></div>
<div class="mono" style="position:absolute;left:98px;top:490px;font-size:13px;color:#7c8896">Chargement des outils de ferraillage…</div>
<div class="mono" style="position:absolute;left:98px;bottom:40px;font-size:12px;color:#5f6b79">Version 0.1 · Pour AutoCAD</div>""")),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    jobs = []
    for name, (w, h, fn) in SUPPORTS.items():
        f = TMP / f"{name}.html"
        f.write_text(fn(), encoding="utf-8")
        jobs.append(f"{f}|{OUT / (name + '.png')}|{w}|{h}")
    env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"], text=True).strip())
    subprocess.run(["node", str(pathlib.Path(__file__).parent / "render_png.js"), *jobs], check=True, env=env)
    print("ok", len(jobs))


if __name__ == "__main__":
    main()
