"""Supports numériques Step by Step Academy (PNG aux dimensions exactes)."""
import os
import pathlib
import subprocess

from brand import *
from pages_a import marches_motif, EMAIL, TEL, PAYS
from pages_b import picto, POLES, niveau

OUT = ROOT / "pack" / "05_Supports_numeriques"
TMP = ROOT / "out" / "supports"
FONTS = font_css()


def doc(w, h, body, bg=IVOIRE, fg=NOIR, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w}px;height:{h}px;overflow:hidden;background:{bg};color:{fg};font-family:Nunito;position:relative}}
.k{{font:700 22px Comfortaa;letter-spacing:6px;text-transform:uppercase;color:{OR_TEXTE if bg != NOIR else OR}}}
.q{{font-family:Quicksand;font-weight:600}}
.chip{{display:inline-block;font:700 22px Comfortaa;letter-spacing:2px;background:{NOIR};color:{OR};border-radius:40px;padding:14px 26px;margin-right:12px}}
.dk .chip{{background:{OR};color:{NOIR}}}
{css}</style></head><body>{body}</body></html>"""


def motif(w, h_bar, gap, color=OR):
    return f'<svg width="{w}" height="{5 * h_bar + 4 * gap}">{marches_motif(0, 0, w, h_bar, gap, color)}</svg>'


def contact(size=26, col=NOIR):
    return f'<div style="font:700 {size}px Nunito;color:{col}">{TEL} · {EMAIL}</div>'


SUPPORTS = {
    "Photo_de_profil_1080x1080": (1080, 1080, lambda: doc(1080, 1080, f"""
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{sized(symbole('sombre'), w=820)}</div>""", NOIR, IVOIRE)),

    "Banniere_Facebook_1640x624": (1640, 624, lambda: doc(1640, 624, f"""
<div style="position:absolute;left:0;bottom:60px">{motif(520, 52, 16)}</div>
<div style="position:absolute;left:600px;top:110px">{sized(horizontal('clair'), w=760)}</div>
<div class="q" style="position:absolute;left:606px;top:360px;font-size:44px">La progression, <span style="background:linear-gradient(transparent 60%,{OR} 60%,{OR} 90%,transparent 90%)">étape par étape.</span></div>
<div style="position:absolute;left:606px;top:450px;font:600 24px Nunito;color:{GRIS}">Logiciels d'ingénierie · Mines · Hydraulique · IA · Soutien scolaire</div>
<div style="position:absolute;left:606px;top:500px">{contact(24)}</div>""")),

    "Banniere_LinkedIn_1584x396": (1584, 396, lambda: doc(1584, 396, f"""
<div style="position:absolute;right:0;bottom:0">{motif(380, 36, 11)}</div>
<div style="position:absolute;left:470px;top:70px">{sized(horizontal('clair'), w=560)}</div>
<div class="q" style="position:absolute;left:476px;top:268px;font-size:34px">La progression, étape par étape.</div>""")),

    "Post_formation_1080x1350": (1080, 1350, lambda: doc(1080, 1350, f"""
<div style="position:absolute;left:80px;top:80px">{sized(horizontal('sombre'), w=430)}</div>
<div class="k" style="position:absolute;left:80px;top:330px">Nouvelle session · Inscriptions ouvertes</div>
<div class="q" style="position:absolute;left:76px;top:390px;font-size:112px;line-height:1;color:{IVOIRE}">AutoCAD</div>
<div class="q" style="position:absolute;left:80px;top:510px;font-size:48px;color:{OR}">du niveau 1 au niveau 3</div>
<div style="position:absolute;left:80px;top:610px">{niveau(3, 300, inactif="#3A3833", k=3.2)}</div>
<div style="position:absolute;left:80px;top:760px;width:880px;font:600 30px/1.5 Nunito;color:#D9D2C4">Dessin 2D, calques, cotation, mise en page et impression : un plan complet, étape par étape, avec un formateur à vos côtés.</div>
<div style="position:absolute;left:80px;top:990px" class="dk"><span class="chip">En ligne</span><span class="chip">Présentiel</span><span class="chip">À domicile</span></div>
<div style="position:absolute;left:80px;bottom:90px;font:800 34px Nunito;color:{OR}">Inscription WhatsApp : {TEL}</div>
<div style="position:absolute;right:0;top:60px;opacity:.14">{motif(300, 28, 10)}</div>""", NOIR, IVOIRE)),

    "Statut_WhatsApp_1080x1920": (1080, 1920, lambda: doc(1080, 1920, f"""
<div style="position:absolute;left:0;right:0;top:160px;display:flex;justify-content:center">{sized(principal('clair'), w=520)}</div>
<div class="q" style="position:absolute;left:90px;right:90px;top:840px;text-align:center;font-size:64px;line-height:1.1">Apprenez étape par étape.</div>
<div style="position:absolute;left:90px;right:90px;top:990px;display:flex;flex-direction:column;gap:18px">
{''.join(f'<div style="display:flex;align-items:center;gap:26px;background:{BLANC};border-radius:22px;padding:16px 28px"><div style="background:{SABLE};border-radius:18px;padding:10px">{picto(k, s=60)}</div><div style="font:700 34px Quicksand">{t}</div></div>' for k, t, _ in POLES)}
</div>
<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font:800 40px Nunito">WhatsApp {TEL}</div>""")),

    "Miniature_cours_1280x720": (1280, 720, lambda: doc(1280, 720, f"""
<div class="k" style="position:absolute;left:70px;top:70px;font-size:20px">Cours en ligne · Niveau 1</div>
<div class="q" style="position:absolute;left:66px;top:130px;font-size:92px;line-height:.98;color:{IVOIRE}">AutoCAD<br>pour<br>débutants</div>
<div style="position:absolute;left:70px;bottom:70px;font:700 30px Nunito;color:#D9D2C4">Leçon 03 · Les calques</div>
<div style="position:absolute;right:60px;top:120px">{sized(symbole('sombre'), w=470)}</div>
<div style="position:absolute;right:60px;bottom:50px">{niveau(1, 200, inactif="#3A3833", k=2.4)}</div>""", NOIR, IVOIRE)),

    "Post_reussite_1080x1080": (1080, 1080, lambda: doc(1080, 1080, f"""
<svg style="position:absolute;left:80px;top:90px" width="170" height="170" viewBox="0 0 60 60"><circle cx="30" cy="30" r="26" fill="none" stroke="{VERT}" stroke-width="4"/><path d="M18 31 L27 40 L43 21" fill="none" stroke="{VERT}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="k" style="position:absolute;left:80px;top:320px">Étape validée</div>
<div class="q" style="position:absolute;left:76px;top:380px;font-size:88px;line-height:1.02">Félicitations,<br>Aminata !</div>
<div style="position:absolute;left:80px;top:600px;font:600 34px/1.45 Nunito;color:{GRIS};width:860px">Niveau 3 validé en Revit. Prochaine marche : la modélisation BIM avancée.</div>
<div style="position:absolute;left:80px;bottom:90px">{sized(horizontal('clair'), w=420)}</div>
<div style="position:absolute;right:0;bottom:80px">{motif(330, 34, 11)}</div>""")),
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
