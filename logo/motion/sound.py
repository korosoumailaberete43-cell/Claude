"""Bande-son des teasers CivRebar AI, entièrement synthétisée (numpy).
usage : python3 sound.py [cues.json] [out/teaser_audio.wav]
Les repères et le plan musical viennent du fichier exporté par render.js."""
import json
import pathlib
import sys
import wave

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SR = 48000
ARGS = sys.argv[1:] + [None, None]
info = json.loads(pathlib.Path(ARGS[0] or HERE / "cues.json").read_text())
DUR = info["dur"]
N = int(DUR * SR) + SR
rng = np.random.default_rng(7)

dry = np.zeros((2, N))
send = np.zeros((2, N))  # bus réverbération


def tt(d):
    return np.arange(int(d * SR)) / SR


def lowpass(x, fc):
    """Passe-bas à un pôle ; fc constante ou tableau (balayage)."""
    fc = np.broadcast_to(np.asarray(fc, float), x.shape)
    a = 1 - np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    s = 0.0
    for i in range(len(x)):
        s += a[i] * (x[i] - s)
        y[i] = s
    return y


def highpass(x, fc):
    return x - lowpass(x, fc)


def sine_sweep(f0, f1, d, curve="exp"):
    t = tt(d)
    f = f0 * (f1 / f0) ** (t / d) if curve == "exp" else f0 + (f1 - f0) * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def put(sig, t0, g=1.0, pan=0.0, wet=0.25):
    i = int(t0 * SR)
    if i < 0:
        sig, i = sig[-i:], 0
    n = min(len(sig), N - i)
    if n <= 0:
        return
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    for ch, k in ((0, l), (1, r)):
        dry[ch, i:i + n] += sig[:n] * g * k * 1.414
        send[ch, i:i + n] += sig[:n] * g * k * 1.414 * wet


def env_ad(d, a, dec):
    t = tt(d)
    return np.minimum(t / max(a, 1e-4), 1) * np.exp(-np.maximum(t - a, 0) / dec)


noise = lambda d: rng.standard_normal(int(d * SR))

# ---------------------------------------------------------------- instruments
def heart():
    d = .45
    s = sine_sweep(75, 38, d) * env_ad(d, .006, .11)
    return np.tanh(2.2 * s) * .9


def key():
    d = .03
    return (highpass(noise(d), 2500) * .5 + np.sin(2 * np.pi * 2300 * tt(d)) * .3) * env_ad(d, .001, .006)


def tick():
    d = .06
    t = tt(d)
    return (np.sin(2 * np.pi * 3100 * t) + .5 * np.sin(2 * np.pi * 5200 * t)) * env_ad(d, .001, .012) * .5


def blip():
    d = .14
    s = np.sign(sine_sweep(900, 1500, d)) * .25 + sine_sweep(900, 1500, d) * .5
    return lowpass(s, 5000) * env_ad(d, .002, .045)


def whoosh(d=1.3):
    n = noise(d)
    t = tt(d)
    fc = 300 + 5000 * np.sin(np.pi * t / d) ** 2
    s = lowpass(n, fc) - lowpass(n, fc * .25)
    return s * np.sin(np.pi * (t / d) ** .7) ** 2 * 1.3


def slam():
    d = .9
    sub = sine_sweep(160, 42, .35)
    sub = np.concatenate([sub, np.sin(2 * np.pi * 42 * tt(d - .35) + np.pi * 0)])[: int(d * SR)]
    s = sub * env_ad(d, .002, .22) * 1.1
    s += highpass(noise(d), 1200) * env_ad(d, .001, .035) * .6
    return np.tanh(1.8 * s)


def impact(d=2.6, big=1.0):
    sub = sine_sweep(120, 28, d) * env_ad(d, .003, .55 * big)
    body = lowpass(noise(d), 900) * env_ad(d, .002, .18 * big) * 1.2
    crack = highpass(noise(d), 2000) * env_ad(d, .001, .05) * .5
    return np.tanh(2.0 * (sub * 1.2 + body + crack))


def boom():
    d = 4.5
    s = impact(d, 1.9)
    t = tt(d)
    # queue métallique scintillante
    shimmer = sum(np.sin(2 * np.pi * f * t + i) for i, f in enumerate([1760, 2217, 2637, 3520])) * env_ad(d, .05, 1.2) * .05
    return s + shimmer


def clang():
    d = 3.0
    t = tt(d)
    parts = [(523, 1.4, 1), (1307, 1.0, .7), (2011, .7, .55), (2897, .5, .4), (3780, .35, .3), (5230, .2, .25)]
    s = sum(a * np.sin(2 * np.pi * f * t * (1 + .002 * np.sin(2 * np.pi * 5 * t))) * np.exp(-t / dec) for f, dec, a in parts)
    s = s / 3 * env_ad(d, .001, 3)
    s += highpass(noise(d), 3000) * env_ad(d, .001, .02) * .7
    sl = slam()
    s[: len(sl)] += sl * .6
    return s


def chime(f0=880):
    d = 3.5
    t = tt(d)
    s = sum(a * np.sin(2 * np.pi * f0 * m * t) * np.exp(-t / dec) for m, a, dec in [(1, 1, 1.6), (2.76, .45, .8), (5.4, .25, .4), (8.93, .12, .25)])
    return s * env_ad(d, .002, 4) * .5


def swell(d=1.4):
    t = tt(d)
    s = highpass(noise(d), 3500) * (t / d) ** 2.5
    return s * .9


def glitch(d=.28):
    out = np.zeros(int(d * SR))
    i = 0
    while i < len(out):
        L = int(rng.uniform(.008, .03) * SR)
        f = rng.choice([80, 160, 440, 880, 1760, 3520]) * rng.uniform(.9, 1.1)
        seg = np.sign(np.sin(2 * np.pi * f * np.arange(L) / SR))
        if rng.random() < .4:
            seg = np.round(rng.standard_normal(L) * 2) / 2
        out[i:i + L] = seg[: len(out) - i] * rng.uniform(.3, 1) * (rng.random() > .15)
        i += L
    return lowpass(out, 7000) * .45


def suck(d=.65):
    s = impact(1.6)[: int(d * SR)] + highpass(noise(d), 1500) * .6
    t = tt(d)
    return s[::-1] * (t / d) ** 2 * 1.2


def shine():
    d = 1.4
    t = tt(d)
    s = sine_sweep(1800, 5400, d) * .3 + sine_sweep(2700, 8100, d) * .15
    return s * np.sin(np.pi * t / d) ** 2 * .35


def draw_fx(d=1.6):
    t = tt(d)
    n = noise(d)
    s = (lowpass(n, 400 + 3000 * t / d) - lowpass(n, 200)) * .8 + sine_sweep(220, 660, d) * .15
    return s * np.sin(np.pi * t / d) * .8


def scratch():
    d = .7
    t = tt(d)
    f = 900 * (1 - t / d) ** 2 + 40
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * .6 + lowpass(noise(d), 1500) * .5
    return s * (1 - t / d)


def pop():
    d = .12
    return sine_sweep(300, 900, d) * env_ad(d, .002, .03)


INSTR = {
    "heart": (heart, 0, .12), "key": (key, None, .05), "tick": (tick, None, .15), "blip": (blip, None, .2),
    "whoosh": (whoosh, None, .3), "slam": (slam, 0, .25), "impact": (impact, 0, .5), "boom": (boom, 0, .55),
    "clang": (clang, .15, .5), "chime": (chime, 0, .6), "swell": (swell, 0, .4), "glitch": (glitch, None, .1),
    "suck": (suck, 0, .6), "shine": (shine, .1, .5), "draw": (draw_fx, 0, .3),
    "scratch": (scratch, 0, .2), "pop": (pop, None, .2),
}
GAIN = {"heart": .9, "key": .14, "tick": .22, "blip": .35, "whoosh": .45, "slam": .75, "impact": .8, "boom": .95,
        "clang": .55, "chime": .28, "swell": .3, "glitch": .35, "suck": .55, "shine": .35, "draw": .3, "scratch": .6, "pop": .4}

for c in info["cues"]:
    ty = c["type"]
    if ty in INSTR:
        fn, pan, wet = INSTR[ty]
        p = pan if pan is not None else rng.uniform(-.5, .5)
        put(fn(), c["t"], GAIN[ty] * c["g"], p, wet)

# ---------------------------------------------------------------- nappes & musique
def note(f, d, a=.8, r=1.2, bright=5.0, det=(-.12, 0, .12)):
    t = tt(d)
    s = np.zeros_like(t)
    for cents in det:
        ff = f * 2 ** (cents / 12)
        for h in range(1, 10):
            s += np.sin(2 * np.pi * ff * h * t + h * cents) / h * np.exp(-h / bright)
    e = np.minimum(t / a, 1) * np.minimum((d - t) / r, 1)
    return s * np.clip(e, 0, 1) / len(det)


def midi(m):
    return 440 * 2 ** ((m - 69) / 12)


M = info["music"]


def spans(key):
    """Plages [a, b] d'une clé du plan musical (une seule ou une liste ; absente → aucune)."""
    v = M.get(key) or []
    return [v] if v and not isinstance(v[0], list) else v


# Tension : bourdon grave qui monte, coupé net au noir
for a, b in spans("drone"):
    d = b - a
    t = tt(d)
    drone = (np.sin(2 * np.pi * 36.7 * t) * .6 + np.sin(2 * np.pi * 73.4 * t + .5) * .25 + lowpass(noise(d), 120) * 1.5)
    drone *= (.25 + .75 * (t / d) ** 1.5) * np.minimum(t / 2, 1) * np.minimum((d - t) / .01, 1)
    put(drone, a, .45, 0, .2)
# pédale aiguë inquiétante
for a, b in spans("pedal"):
    d = b - a
    put(note(midi(74), d, a=3, r=.01, bright=2) * (tt(d) / d) ** 1.2, a, .06, .3, .6)
# Montée
for a, b in spans("riser"):
    d = b - a
    t = tt(d)
    k = t / d
    rate = 3 + 22 * k ** 2
    trem = .6 + .4 * np.sin(2 * np.pi * np.cumsum(rate) / SR)
    riser = (sine_sweep(110, 1100, d) * .5 + sine_sweep(165, 1650, d) * .25 + highpass(noise(d), 800 + 6000 * k) * .6) * trem
    riser *= k ** 2.2 * np.minimum((d - t) / .01, 1)
    put(riser, a, .38, 0, .3)

# Après la révélation : accords en ré mineur
CH = {"Dm": [50, 57, 62, 65, 69], "Bb": [46, 53, 58, 62, 65], "F": [41, 53, 57, 60, 65], "C": [48, 55, 60, 64, 67]}
chords = M.get("chords", [])
first = chords[0][1] if chords else 0
for name, a, b in chords:
    for i, m in enumerate(CH[name]):
        put(note(midi(m), b - a + .6, a=1.2 if a > first + .5 else .3, r=.8), a, .09 if i else .12, (i - 2) * .25, .6)


def inside(x, spans):
    return any(a <= x < b for a, b, *_ in spans)


# basse pulsée (croches, 120 bpm) + arpège (doubles croches), sur les plages demandées
for name, a, b in chords:
    root = CH[name][0] - 12 if CH[name][0] > 45 else CH[name][0]
    tb = a
    while tb < b - .01:
        if inside(tb, M.get("bass", [])):
            dd = .45
            s = np.sin(2 * np.pi * midi(root) * tt(dd)) + .3 * np.sin(4 * np.pi * midi(root) * tt(dd))
            put(np.tanh(1.5 * s) * env_ad(dd, .005, .12), tb, .32, 0, .05)
        tb += .25
    tones = [m + 12 for m in CH[name][1:]]
    seq = tones + tones[::-1][1:-1]
    ta, j = a, 0
    while ta < b - .01:
        if inside(ta, M.get("arp", [])):
            dd = .3
            f = midi(seq[j % len(seq)])
            s = (np.sin(2 * np.pi * f * tt(dd)) + .35 * np.sin(4 * np.pi * f * tt(dd))) * env_ad(dd, .002, .07)
            put(s, ta, .1, .45 * np.sin(j), .5)
        ta += .125
        j += 1
# grosse caisse (noires)
for a, b, g in M.get("kick", []):
    tb = a
    while tb < b - .01:
        dd = .4
        kk = sine_sweep(140, 45, dd) * env_ad(dd, .002, .09)
        put(np.tanh(2 * kk), tb, g, 0, .05)
        tb += .5
# claquements (temps 2 et 4) et charleston (croches)
for a, b, g in M.get("clap", []):
    tb = a + .5
    while tb < b - .01:
        d = .25
        put(highpass(noise(d), 900) * env_ad(d, .002, .05) * .8, tb, g, .1, .35)
        tb += 1.0
for a, b, g in M.get("hat", []):
    tb = a + .25
    while tb < b - .01:
        d = .06
        put(highpass(noise(d), 6000) * env_ad(d, .001, .015), tb, g, -.2, .1)
        tb += .5
# Suspense : tic-tac + cœur + note tenue
for a, b in spans("suspense"):
    tb = a + .5
    while tb < b - .3:
        put(tick(), tb, .18, -.3 if int(tb * 2) % 2 else .3, .4)
        tb += .5
    d = b - a
    put(note(midi(38), d, a=1.5, r=.3, bright=1.5) * np.linspace(.4, 1, int(d * SR)), a, .22, 0, .4)
for h in M.get("suspenseHearts", []):
    put(heart(), h, .7, 0, .1)
    put(heart(), h + .24, .45, 0, .1)
# Accord final (ré mineur ouvert) → fin
if "final" in M:
    fin = M["final"]
    d = DUR - fin + .5
    for i, m in enumerate([38, 50, 57, 62, 65, 69, 74]):
        put(note(midi(m), d, a=.05 if i < 2 else .6, r=3.5, bright=6), fin, .1 if i else .18, (i - 3) * .2, .7)

# ---------------------------------------------------------------- réverbération, mixage
L = int(2.8 * SR)
tir = np.arange(L) / SR
wet = np.zeros_like(dry)
for ch in range(2):
    ir = rng.standard_normal(L) * np.exp(-tir / .55)
    ir = lowpass(ir, 6000)
    ir /= np.sqrt(np.sum(ir ** 2))
    nfft = 1 << int(np.ceil(np.log2(N + L)))
    wet[ch] = np.fft.irfft(np.fft.rfft(send[ch], nfft) * np.fft.rfft(ir, nfft), nfft)[:N]
mix = dry + wet * .9
mix = mix[:, : int(DUR * SR)]
# fondus d'entrée/sortie
n = mix.shape[1]
tm = np.arange(n) / SR
mix *= np.clip(tm / .05, 0, 1) * np.clip((DUR - tm) / 1.2, 0, 1)
# limiteur doux
mix /= np.max(np.abs(mix)) + 1e-9
mix = np.tanh(1.6 * mix) / np.tanh(1.6)
mix *= 10 ** (-1 / 20)
dest = pathlib.Path(ARGS[1] or HERE / "out" / "teaser_audio.wav")
dest.parent.mkdir(exist_ok=True)
pcm = (mix.T * 32767).astype("<i2")
with wave.open(str(dest), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("ok", n / SR, "s")
