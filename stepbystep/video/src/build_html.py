"""Construit les pages HTML animées (intro / outro) à partir du logo vectoriel d'origine.
Chaque page expose window.renderAt(t) : l'image est une fonction pure du temps, ce qui permet
un rendu image par image exact (et le flou de mouvement par sous-échantillonnage)."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "src"))

import logo as L          # noqa: E402
import brand as B         # noqa: E402

OUT = HERE.parent / "build"


def logo_data():
    """Pièces du logo (repère 1280 de l'original), séparées pour être animées une à une."""
    p = L.parts(texte=B.BLANC, or_=B.OR, vert=B.VERT)
    letters = re.findall(r'<path [^>]*/>', p["texte"])
    assert len(letters) == 17, len(letters)
    extras = re.findall(r'<path [^>]*/>', p["extras"])
    return {
        "toque": p["toque"],
        "letters": letters,          # Step(4) · Step(4) · By(2) · ACADEMY(7)
        "tildes": extras[:2],
        "livre": extras[2:],
        "marches": L.MARCHES,
        "marcheDroite": L.MARCHE_DROITE,
        "marcheH": L.MARCHE_H,
        "horizontal": B.horizontal("sombre"),
    }


def page(scene_js, config):
    lib = (HERE / "lib.js").read_text()
    scene = (HERE / scene_js).read_text()
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{B.font_css()}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1920px;height:1080px;overflow:hidden;background:{B.NOIR}}}
#root{{position:absolute;inset:0;overflow:hidden;background:{B.NOIR};font-family:Nunito;color:{B.IVOIRE}}}
svg{{position:absolute;left:0;top:0;overflow:visible}}
.abs{{position:absolute}}
.mask{{overflow:hidden;display:block}}
.mask>span{{display:inline-block;will-change:transform}}
</style></head><body><div id="root"></div>
<script>
const LOGO = {json.dumps(logo_data())};
const CFG = {json.dumps(config, ensure_ascii=False)};
const C = {json.dumps(dict(noir=B.NOIR, or_=B.OR, ivoire=B.IVOIRE, vert=B.VERT, sable=B.SABLE, graphite=B.GRAPHITE))};
{lib}
{scene}
</script></body></html>"""


VARIANTES = {
    "intro_generique": ("intro.js", dict(mode="generique", duree=6.2)),
    "intro_titre_exemple": ("intro.js", dict(
        mode="titre", duree=7.6,
        kicker="Cours en ligne · Niveau 1",
        titre=["AutoCAD", "pour débutants"],
        lecon="Leçon 03 · Les calques")),
    "outro": ("outro.js", dict(duree=20.0, chaine="Step by Step Academy",
                               tel="+223 89 48 33 27")),
}


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    extra = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    noms = [sys.argv[1]] if len(sys.argv) > 1 and sys.argv[1] in VARIANTES else list(VARIANTES)
    for nom in noms:
        js, cfg = VARIANTES[nom]
        cfg = {**cfg, **extra}
        (OUT / f"{nom}.html").write_text(page(js, cfg))
        print(OUT / f"{nom}.html", cfg["duree"])
