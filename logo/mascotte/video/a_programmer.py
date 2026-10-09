"""Liste les vidéos fabriquées qui ne sont pas encore programmées sur Metricool.

python3 video/a_programmer.py          → ce qu'il reste à programmer (date, URL, texte)
python3 video/a_programmer.py h10_declic h11_zoom   → marque ces épisodes comme programmés
"""
import json
import pathlib
import subprocess
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[2]
SUIVI = ICI / "episodes" / "programmees.json"


def main():
    fait = json.loads(SUIVI.read_text())
    if len(sys.argv) > 1:                       # marquer comme programmés
        fait = sorted(set(fait) | set(sys.argv[1:]))
        SUIVI.write_text(json.dumps(fait, ensure_ascii=False) + "\n")
        print(f"{len(fait)}/33 programmées")
        return
    prog = json.loads((ICI / "episodes" / "programme.json").read_text())
    sha = subprocess.run(["git", "-C", str(RACINE), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    base = f"https://raw.githubusercontent.com/korosoumailaberete43-cell/Claude/{sha}/logo/mascotte/out"
    prets = {f.name[len("Tonton_"):-4] for f in (ICI.parent / "out").glob("Tonton_h*.mp4")}
    reste = [p for p in prog["posts"] if p["ep"] in prets and p["ep"] not in fait]
    print(f"# {len(fait)}/33 programmées · {len(prets)} fabriquées · {len(reste)} à programmer")
    for p in sorted(reste, key=lambda x: x["jour"]):
        print(f'### {p["jour"]}T14:00:00+00:00 | {p["ep"]} | {p["titre"]}')
        print(f'{base}/Tonton_{p["ep"]}.mp4')
        print(json.dumps(p["texte"] + "\n\n" + prog["hashtags"], ensure_ascii=False))
    manque = [p["ep"] for p in prog["posts"] if p["ep"] not in prets]
    if manque:
        print(f'# encore à fabriquer : {" ".join(manque)}')


if __name__ == "__main__":
    main()
