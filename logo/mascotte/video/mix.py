"""Bande-son de la présentation : musique + bruitages (motion/sound.py) + voix, avec ducking.
python3 mix.py cues.json → presentation_audio.wav"""
import json
import pathlib
import subprocess
import sys
import wave

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SOUND = HERE.parents[1] / "motion" / "sound.py"
V = json.loads((HERE / "voix.json").read_text())
seg = {s["id"]: s for s in V["segments"]}
DUR = V["dur"]
MAP = {"error": "glitch", "stamp": "impact", "click": "tick"}
cues = []
riser = None
for c in json.loads(pathlib.Path(sys.argv[1]).read_text()):
    if c["type"] == "riser":
        riser = c["t"]
        continue
    cues.append({"t": c["t"], "type": MAP.get(c["type"], c["type"]), "g": c.get("g", 1)})

# grille 120 bpm : une mesure = 2 s, boucle Dm – Bb – F – C
boom = seg["solution"]["t0"] + 1.6
for c in cues:
    if c["type"] == "boom":
        boom = c["t"]
prog_ = ["Dm", "Bb", "F", "C"]
chords, t, i = [], 1.2, 0
fin = seg["fin"]["t1"] + 0.2
while t < fin:
    chords.append([prog_[i % 4], t, min(t + 2, fin)])
    t += 2; i += 1
intro = [1.2, seg["probleme"]["t0"]]
groove = [boom, seg["citation"]["t0"]]
outro = [seg["logo"]["t0"], fin]
music = {
    "chords": chords,
    "bass": [intro, groove, outro],
    "arp": [groove, [seg["logo"]["t1"], fin]],
    "hat": [[*intro, .35], [*groove, .4], [*outro, .35]],
    "kick": [[boom, seg["citation"]["t0"], .5], [seg["logo"]["t0"], fin, .45]],
    "clap": [[seg["demo"]["t0"], seg["citation"]["t0"], .3]],
    "drone": [seg["probleme"]["t0"], boom],
    "pedal": [seg["erreurs"]["t0"], boom],
    "riser": [riser or boom - 1.6, boom],
    "final": fin,
}
# pendant le problème, pas d'accords (tension seule)
music["chords"] = [c for c in chords if not (seg["probleme"]["t0"] - .1 < c[1] < boom - .1)]
tmp = HERE / "_cues_son.json"
tmp.write_text(json.dumps({"dur": DUR, "cues": cues, "music": music}))
subprocess.run([sys.executable, str(SOUND), str(tmp), str(HERE / "_musique.wav")], check=True)
tmp.unlink()


def lire(p):
    with wave.open(str(p)) as w:
        sr, ch = w.getframerate(), w.getnchannels()
        x = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(np.float32) / 32767
    return sr, x.reshape(-1, ch).T


sr, mus = lire(HERE / "_musique.wav")
vsr, voix = lire(HERE / "voix.wav")
# rééchantillonne la voix à 48 kHz (interpolation linéaire suffit pour la parole)
n = int(voix.shape[1] * sr / vsr)
voix = np.interp(np.arange(n) * vsr / sr, np.arange(voix.shape[1]), voix[0])
# petite chaleur : léger passe-haut + compression douce
voix = voix - np.convolve(voix, np.ones(400) / 400, mode="same")
voix = np.tanh(voix * 1.8) / np.tanh(1.8)
L = max(n, mus.shape[1])
out = np.zeros((2, L))
out[:, :mus.shape[1]] += mus * 0.55
# ducking : enveloppe de la voix lissée (attaque rapide, relâche lente)
env = np.abs(voix)
k = int(0.25 * sr)
env = np.convolve(env, np.ones(k) / k, mode="same")
env = np.clip(env / (np.percentile(env[env > 1e-3], 90) + 1e-9), 0, 1)
duck = np.ones(L)
duck[:n] = 1 - 0.55 * env
out *= duck
out[:, :n] += voix * 0.95
out /= np.max(np.abs(out)) + 1e-9
out *= 10 ** (-1 / 20)
with wave.open(str(HERE / "presentation_audio.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((out.T * 32767).astype("<i2").tobytes())
(HERE / "_musique.wav").unlink()
print("mix ok", L / sr)
