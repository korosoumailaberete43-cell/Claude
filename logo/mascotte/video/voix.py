"""Voix off de Tonton Ferraille, générée hors ligne (Piper « fr_FR-tom-medium » via sherpa-onnx).

python3 voix.py                      → voix.wav + voix.json de la présentation
python3 voix.py episodes/<nom>       → idem pour un épisode, à partir de episodes/<nom>/texte.json
  texte.json : {"segments": [["id", "texte"], ...], "pauses": {"id": secondes après}, "fin": secondes}
Si un fichier « voix_remy.mp3 » est fourni plus tard, il suffira de refaire le calage.
"""
import json
import pathlib
import re
import sys
import wave

import numpy as np
import sherpa_onnx

HERE = pathlib.Path(__file__).resolve().parent
MODEL = HERE.parent / "voix" / "vits-piper-fr_FR-tom-medium"
FPS = 30
DEBUT = 1.2          # silence avant la première phrase (entrée de Tonton)
PAUSE = 0.38         # respiration entre deux phrases
VITESSE = 0.94       # ≈ débit −6 %

SEGMENTS = [
    ("accroche", "Eh ! Toi là… oui, toi, l'ingénieur !"),
    ("intro", "Moi, c'est Tonton Ferraille. Trente ans de chantier… et aujourd'hui, je vais te parler de CivRebar."),
    ("probleme", "Sur un plan de ferraillage, chaque barre, chaque cadre, chaque cote… on les dessine à la main. Trait par trait. Poutre après poutre."),
    ("erreurs", "Résultat ? Des heures perdues… et des erreurs qui finissent sur le chantier."),
    ("solution", "Alors voilà la solution : CivRebar AI. Un outil de ferraillage, directement dans AutoCAD."),
    ("demo", "Tu donnes la section, la portée, les armatures… et lui, il dessine les barres, les cadres, les cotes et les repères."),
    ("route", "On commence par la poutre. Ensuite viendront les poteaux, les dalles, les semelles… et les escaliers."),
    ("signal", "Et puis, il y a Signal, mon petit assistant : l'intelligence artificielle."),
    ("promesse", "À terme, elle vérifiera tes plans et calculera les quantités… mais attention : c'est toujours l'ingénieur qui décide, et qui signe le plan !"),
    ("citation", "Rien n'y est décoratif… tout y est calculé."),
    ("logo", "CivRebar AI. L'intelligence de l'armature. Bientôt dans AutoCAD."),
    ("fin", "Abonne-toi… et on se retrouve sur le chantier !"),
]
# Aide à la prononciation (le texte affiché à l'écran garde l'orthographe normale)
PRONONCE = [("CivRebar AI", "Civ Rébar A. I."), ("CivRebar", "Civ Rébar"), ("AutoCAD", "Auto Cade")]


def main():
    global SEGMENTS
    dest, pauses, fin = HERE, {}, 3.2
    if len(sys.argv) > 1:
        dest = (HERE / sys.argv[1]).resolve()
        cfg_ep = json.loads((dest / "texte.json").read_text())
        SEGMENTS = [tuple(x) for x in cfg_ep["segments"]]
        pauses, fin = cfg_ep.get("pauses", {}), cfg_ep.get("fin", 3.2)
    cfg = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=str(MODEL / "fr_FR-tom-medium.onnx"), tokens=str(MODEL / "tokens.txt"),
                                                   data_dir=str(MODEL / "espeak-ng-data")), num_threads=4))
    tts = sherpa_onnx.OfflineTts(cfg)
    sr = None
    parts, segs, t = [], [], DEBUT
    for key, txt in SEGMENTS:
        say = txt
        for a, b in PRONONCE:
            say = say.replace(a, b)
        a = tts.generate(say, sid=0, speed=VITESSE)
        sr = a.sample_rate
        x = np.clip(np.asarray(a.samples, dtype=np.float32), -1, 1)
        # rogne les silences de bord pour un calage serré
        env = np.abs(x) > 0.01
        i0 = max(0, int(np.argmax(env)) - int(0.02 * sr))
        i1 = min(len(x), len(x) - int(np.argmax(env[::-1])) + int(0.06 * sr))
        x = x[i0:i1]
        dur = len(x) / sr
        # mots : répartis au prorata des lettres, les « … » comptent comme une petite pause
        mots = re.findall(r"\S+", txt)
        poids = [len(re.sub(r"[^\wÀ-ÿ']", "", m)) + (6 if "…" in m else 0) + 1 for m in mots]
        tot, acc, words = sum(poids), 0, []
        for m, p in zip(mots, poids):
            words.append({"w": m, "t": round(t + dur * acc / tot, 3)})
            acc += p
        segs.append({"id": key, "text": txt, "t0": round(t, 3), "t1": round(t + dur, 3), "words": words})
        parts.append(x)
        t += dur + pauses.get(key, PAUSE)
    total = t + fin     # fin : logo et appel à l'action
    audio = np.zeros(int(total * sr), dtype=np.float32)
    for s, x in zip(segs, parts):
        i = int(s["t0"] * sr)
        audio[i:i + len(x)] += x
    audio *= 0.95 / (np.max(np.abs(audio)) + 1e-9)
    with wave.open(str(dest / "voix.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((audio * 32767).astype("<i2").tobytes())
    # enveloppe (ouverture de bouche) : RMS par image, lissée
    hop = sr // FPS
    rms = np.array([np.sqrt(np.mean(audio[k * hop:(k + 1) * hop] ** 2)) for k in range(int(total * FPS))])
    rms = rms / (np.percentile(rms[rms > 0.01], 95) + 1e-9)
    rms = np.convolve(np.clip(rms, 0, 1.2), np.ones(2) / 2, mode="same")
    (dest / "voix.json").write_text(json.dumps({"dur": round(total, 2), "fps": FPS, "segments": segs,
                                                "mouth": [round(float(v), 3) for v in rms]}, ensure_ascii=False))
    print(f"voix : {total:.1f} s, {len(segs)} phrases")


if __name__ == "__main__":
    main()
