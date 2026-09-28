"""Habillage sonore original (synthèse pure, aucun échantillon externe : zéro souci de droits).
Intro : logo sonore calé image par image sur l'animation. Outro : musique douce et positive
(Ré majeur, 96 BPM) + bruitages (confettis, pops, clic, cloche, transitions).
usage : python3 audio.py intro_generique|intro_titre_exemple|outro sortie.wav"""
import sys
import wave
import numpy as np

SR = 48000
rs = np.random.default_rng(3)


def N(sec):
    return int(round(sec * SR))


def hz(note):                       # 'D4', 'F#5'…
    names = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    n, o = note[:-1], int(note[-1])
    return 440 * 2 ** ((names[n] + 12 * (o + 1) - 69) / 12)


class Track:
    def __init__(self, dur):
        self.L = np.zeros(N(dur) + SR * 4)
        self.R = np.zeros_like(self.L)
        self.dur = dur

    def add(self, t, sig, gain=1.0, pan=0.0):
        """pan : -1 gauche … +1 droite (loi à puissance constante)."""
        if sig.ndim == 2:
            l, r = sig
        else:
            l = r = sig
        a = (pan + 1) * np.pi / 4
        i = N(t)
        if i < 0:
            l, r, i = l[-i:], r[-i:], 0
        n = min(len(l), len(self.L) - i)
        self.L[i:i + n] += l[:n] * gain * np.cos(a) * 1.414
        self.R[i:i + n] += r[:n] * gain * np.sin(a) * 1.414


# ------------------------------------------------------------------------------------ outils DSP
def tvec(sec):
    return np.arange(N(sec)) / SR


def adsr(n, a=.005, d=.1, s=.6, r=.3, hold=None):
    a, d, r = N(a), N(d), N(r)
    hold = n - a - d - r if hold is None else N(hold)
    hold = max(0, hold)
    e = np.concatenate([np.linspace(0, 1, a, endpoint=False), np.linspace(1, s, d, endpoint=False),
                        np.full(hold, s), np.linspace(s, 0, r)])
    return np.pad(e, (0, max(0, n - len(e))))[:n]


def fft_filter(x, lo=None, hi=None, tilt=0.0):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.ones_like(f)
    if hi:
        g *= 1 / np.sqrt(1 + (f / hi) ** 4)
    if lo:
        g *= 1 / np.sqrt(1 + (lo / np.maximum(f, 1)) ** 4)
    if tilt:
        g *= (np.maximum(f, 20) / 1000) ** tilt
    return np.fft.irfft(X * g, len(x))


def sweep_filter(x, f0, f1, q=2.0, blocks=64):
    """Passe-bande glissant (par blocs recouvrants) : pour les whoosh."""
    n = len(x)
    out = np.zeros(n)
    hop = n // blocks
    win = np.hanning(hop * 2)
    for b in range(blocks + 1):
        s = max(0, b * hop - hop // 2)
        seg = x[s:s + hop * 2]
        if len(seg) < 16:
            continue
        fc = f0 * (f1 / f0) ** (b / blocks)
        seg = fft_filter(seg, lo=fc / q, hi=fc * q)
        out[s:s + len(seg)] += seg * win[:len(seg)]
    return out


def norm(x, peak=1.0):
    m = np.max(np.abs(x)) or 1
    return x / m * peak


def reverb(L, R, secs=2.2, wet=.22, damp=4500):
    n = N(secs)
    t = np.arange(n) / SR
    outs = []
    for ch, x in enumerate((L, R)):
        ir = rs.standard_normal(n) * np.exp(-t * 6.9 / secs)
        ir = fft_filter(ir, lo=180, hi=damp)
        ir[:N(.012)] = 0
        ir /= np.sqrt(np.sum(ir ** 2))
        m = len(x) + n
        size = 1 << (m - 1).bit_length()
        y = np.fft.irfft(np.fft.rfft(x, size) * np.fft.rfft(ir, size), size)[:len(x)]
        outs.append(x + wet * y)
    return outs


# ------------------------------------------------------------------------------------ instruments
def marimba(f, dur=1.2, bright=1.0):
    t = tvec(dur)
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t * 3.2)
         + .35 * bright * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 14)
         + .10 * bright * np.sin(2 * np.pi * f * 9.9 * t) * np.exp(-t * 30))
    x *= np.minimum(1, t / .0015)
    return x


def pluck(f, dur=1.4, bright=.5):
    """Karplus-Strong (corde pincée), vectorisé par périodes."""
    p = int(SR / f)
    n = N(dur)
    buf = rs.uniform(-1, 1, p)
    buf = fft_filter(np.tile(buf, 4), hi=2000 + 6000 * bright)[:p]
    out = np.zeros(n)
    out[:p] = buf
    decay = .996
    for i in range(p, n, p):
        prev = out[i - p:i]
        nxt = .5 * (prev + np.roll(prev, 1)) * decay
        out[i:i + p] = nxt[:min(p, n - i)]
    return out * np.exp(-tvec(dur) * .8)


def bell(f, dur=2.5):
    t = tvec(dur)
    parts = [(1, 1, 1.4), (2.0, .45, 2.2), (2.76, .35, 3.2), (5.4, .18, 5.5), (8.93, .08, 8)]
    x = sum(a * np.sin(2 * np.pi * f * r * t + r) * np.exp(-t * d) for r, a, d in parts)
    return x * np.minimum(1, t / .002)


def pad(freqs, dur, attack=.8, release=1.2, bright=.5, voices=3):
    t = tvec(dur)
    x = np.zeros_like(t)
    for f in freqs:
        for v in range(voices):
            det = f * (1 + (v - (voices - 1) / 2) * .0035)
            vib = 1 + .002 * np.sin(2 * np.pi * (4.3 + v * .7) * t + v)
            ph = 2 * np.pi * np.cumsum(det * vib) / SR + rs.uniform(0, 6)
            for k in range(1, 9):              # dent de scie douce (harmoniques filtrées)
                x += np.sin(k * ph) / k * np.exp(-k * (1.2 - bright))
    env = adsr(len(t), a=attack, d=.3, s=.85, r=release)
    return x * env / (len(freqs) * voices)


def sub_boom(dur=1.4, f0=110, f1=38):
    t = tvec(dur)
    f = f1 + (f0 - f1) * np.exp(-t * 9)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.2)
    click = fft_filter(rs.standard_normal(len(t)), hi=2500) * np.exp(-t * 60) * .4
    return x + click


def kick(dur=.45):
    t = tvec(dur)
    f = 45 + 110 * np.exp(-t * 28)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) + fft_filter(rs.standard_normal(len(t)), hi=4000) * np.exp(-t * 200) * .25


def snap(dur=.35):
    t = tvec(dur)
    x = fft_filter(rs.standard_normal(len(t)), lo=900, hi=6500) * np.exp(-t * 22)
    return x + .4 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30)


def shaker(dur=.09):
    t = tvec(dur)
    return fft_filter(rs.standard_normal(len(t)), lo=6000, hi=14000) * np.sin(np.pi * np.minimum(1, t / dur)) ** 2


def whoosh(dur=.9, f0=300, f1=3500, peak=.6):
    t = tvec(dur)
    x = sweep_filter(rs.standard_normal(len(t)), f0, f1, q=1.8)
    env = np.where(t < dur * peak, (t / (dur * peak)) ** 2, np.exp(-(t - dur * peak) * 9))
    return norm(x * env)


def stereo_whoosh(dur=.9, f0=300, f1=3500, peak=.6, pan_from=.8, pan_to=-.8):
    x = whoosh(dur, f0, f1, peak)
    p = np.linspace(pan_from, pan_to, len(x))
    a = (p + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)]) * 1.414


def pop(f=700, dur=.18):
    t = tvec(dur)
    ff = f * (1 + 1.2 * np.exp(-t * 40))
    return np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t * 26)


def tick(dur=.03):
    t = tvec(dur)
    return fft_filter(rs.standard_normal(len(t)), lo=2500, hi=9000) * np.exp(-t * 300)


def sparkle(dur, density=18, lo='D6', seed=1):
    r = np.random.default_rng(seed)
    out = np.zeros((2, N(dur) + SR))
    scale = [hz(n) for n in ('D6', 'E6', 'F#6', 'A6', 'B6', 'D7', 'E7', 'F#7')]
    for _ in range(int(density * dur)):
        t0 = r.uniform(0, dur)
        f = scale[r.integers(len(scale))]
        s = bell(f, .6) * .25
        pan = r.uniform(-.8, .8)
        a = (pan + 1) * np.pi / 4
        i = N(t0)
        out[0, i:i + len(s)] += s * np.cos(a)
        out[1, i:i + len(s)] += s * np.sin(a)
    return out


# ------------------------------------------------------------------------------------ INTRO
def intro(titre=False):
    dur = 7.6 if titre else 6.2
    wipe = dur - 1.05
    tr = Track(dur)
    # nappe grave et montée (0 → 1 s)
    tr.add(0.0, fft_filter(pad([hz('D2'), hz('A2')], 3.2, attack=1.2, release=1.5, bright=.2), hi=500), .55)
    tr.add(0.0, stereo_whoosh(1.2, 120, 2200, .85, -.6, .6), .16)
    # le fil doré se trace
    tr.add(0.28, stereo_whoosh(.95, 900, 6000, .5, -.7, .7), .10)
    tr.add(0.28, sparkle(.9, 14, seed=4), .35)
    # 5 marches : notes montantes (Ré majeur pentatonique)
    for k, n in enumerate(['D4', 'F#4', 'A4', 'B4', 'D5']):
        t0 = 0.90 + k * 0.16 + .03
        tr.add(t0, marimba(hz(n), 1.3), .42, pan=-.35 + k * .17)
        tr.add(t0, marimba(hz(n) * 2, .8, .5), .10, pan=-.35 + k * .17)
        tr.add(t0, sub_boom(.35, 90, 50), .10)
    # la coche : « ding » de validation
    tr.add(2.30, bell(hz('D6'), 2.6), .34, pan=.25)
    tr.add(2.32, bell(hz('A6'), 2.0), .16, pan=.35)
    tr.add(2.30, sparkle(.5, 30, seed=7), .3)
    # chute de la toque puis impact + accord plein
    tr.add(2.46, stereo_whoosh(.55, 2500, 400, .9, -.5, -.2), .14)
    tr.add(2.98, sub_boom(1.8, 120, 36), .85)
    tr.add(2.98, snap(.5), .12)
    chord = [hz(n) for n in ('D3', 'A3', 'C#4', 'E4', 'F#4', 'A4')]
    tr.add(2.98, pad(chord, dur - 2.98 + .4, attack=.05, release=1.1, bright=.6), .9)
    for k, n in enumerate(['D5', 'F#5', 'A5', 'C#6', 'E6']):
        tr.add(3.00 + k * .07, pluck(hz(n), 2.2, .6), .22, pan=-.5 + k * .25)
    # le nom s'écrit : poussière scintillante ; le reflet balaie le logo
    tr.add(3.12, sparkle(1.0, 16, seed=11), .22)
    tr.add(4.10, stereo_whoosh(1.0, 2000, 9000, .55, -.6, .6), .07)
    if titre:
        tr.add(4.02, stereo_whoosh(.9, 300, 2600, .55, -.3, .7), .16)
        for k, n in enumerate(['A5', 'D6']):
            tr.add(4.62 + k * .14, marimba(hz(n), 1.0), .16, pan=-.4)
    # transition escalier : 5 passages rapides
    tr.add(wipe - .05, stereo_whoosh(.8, 250, 4200, .55, .9, -.9), .5)
    for k in range(5):
        tr.add(wipe + .05 + k * .03, tick(), .10, pan=.6 - k * .3)
    tr.add(wipe + .38, sub_boom(.9, 70, 32), .35)
    return tr, dur


# ------------------------------------------------------------------------------------ OUTRO
def outro():
    dur = 20.0
    tr = Track(dur)
    bpm = 96
    beat = 60 / bpm
    bar = 4 * beat                     # 2,5 s
    prog = [('D', ['D3', 'A3', 'D4', 'F#4', 'A4']), ('A', ['C#3', 'A3', 'C#4', 'E4', 'A4']),
            ('Bm', ['B2', 'F#3', 'B3', 'D4', 'F#4']), ('G', ['G2', 'D3', 'B3', 'D4', 'F#4']),
            ('D', ['D3', 'A3', 'D4', 'F#4', 'A4']), ('A', ['E3', 'A3', 'C#4', 'E4', 'A4']),
            ('G', ['G2', 'D3', 'B3', 'D4', 'G4']), ('D', ['D3', 'A3', 'D4', 'E4', 'F#4', 'A4'])]
    roots = ['D2', 'A1', 'B1', 'G1', 'D2', 'A1', 'G1', 'D2']
    arp = [0, 2, 3, 4, 3, 2, 4, 3]                 # motif d'arpège (croches)
    for b, (_, notes) in enumerate(prog):
        t0 = b * bar
        last = b == len(prog) - 1
        L = bar + (2.5 if last else .9)
        tr.add(t0, pad([hz(n) for n in notes[1:]], L, attack=.35 if b else .05, release=1.4 if last else .9, bright=.45), .55)
        # arpège pincé
        for k in range(8 if not last else 3):
            f = hz(notes[arp[k] % len(notes)]) * 2
            vel = .20 if k % 2 == 0 else .13
            tr.add(t0 + k * beat / 2, pluck(f, 1.2, .55), vel, pan=(-.4 if k % 2 else .4))
        # basse
        if b >= 1:
            for k in (0, 2):
                tr.add(t0 + k * beat, fft_filter(pad([hz(roots[b])], beat * 1.8, attack=.01, release=.3, bright=.3, voices=1), hi=300), .55)
        # batterie (à partir de la scène B, coupée à la fin)
        if 1 <= b <= 6:
            for k in range(4):
                tt = t0 + k * beat
                if tt < 3.3:
                    continue
                if k in (0, 2):
                    tr.add(tt, kick(), .38)
                else:
                    tr.add(tt, snap(), .16, pan=.1)
                for h in range(4):
                    tr.add(tt + h * beat / 4, shaker(), .05 + (.03 if h == 2 else 0), pan=.35)
    tr.add(len(prog) * bar - bar, bell(hz('D6'), 3.5), .12, pan=.3)

    # --- bruitages
    tr.add(0.05, stereo_whoosh(.7, 600, 5000, .5, -.6, .6), .08)
    for k, n in enumerate(['D4', 'F#4', 'A4', 'B4', 'D5']):
        tr.add(.14 + k * .1, marimba(hz(n), 1.0), .26, pan=-.4 + k * .2)
    tr.add(.86, bell(hz('D6'), 2.4), .32, pan=-.2)
    tr.add(.88, bell(hz('A6'), 1.8), .14, pan=-.1)
    tr.add(.90, sparkle(1.8, 26, seed=21), .26)
    conf = fft_filter(rs.standard_normal(N(2.2)), lo=3000, hi=12000) * np.exp(-tvec(2.2) * 1.4) * (rs.random(N(2.2)) > .985)
    tr.add(.9, fft_filter(conf, hi=9000), .5)
    for w in (2.90, 8.20):
        tr.add(w - .05, stereo_whoosh(.8, 250, 4200, .55, .9, -.9), .38)
        tr.add(w + .38, sub_boom(.8, 70, 32), .22)
    for i in range(3):                              # apparition des cartes
        tr.add(3.325 + .45 + i * .42, pop(520 + i * 120), .32, pan=-.6 + i * .6)
        tr.add(3.325 + .45 + i * .42, marimba(hz(['A4', 'D5', 'F#5'][i]), .9), .16, pan=-.6 + i * .6)
    tr.add(6.62, tick(.02), .5, pan=.5)             # clic de souris
    tr.add(6.62, pop(1400, .06), .3, pan=.5)
    tr.add(6.67, bell(hz('A5'), 1.6), .2, pan=.5)   # la cloche sonne
    tr.add(6.67, bell(hz('D6'), 1.8), .14, pan=.55)
    tr.add(6.70, pop(900), .22, pan=.5)             # badge vert
    for i in range(5):                              # écran de fin : éléments qui se posent
        tr.add(8.675 + .2 + i * .16, pop(650 + i * 60, .12), .12, pan=-.5 + i * .25)
    return tr, dur


def master(tr, dur, fade_in=0.0, fade_out=.6):
    L, R = reverb(tr.L, tr.R)
    n = N(dur)
    L, R = L[:n], R[:n]
    env = np.ones(n)
    if fade_out:
        m = N(fade_out)
        env[-m:] *= np.linspace(1, 0, m) ** 1.5
    L *= env; R *= env
    # compression douce + limiteur
    x = np.stack([L, R])
    x = np.tanh(x / np.max(np.abs(x)) * 1.6) / np.tanh(1.6)
    x = x * (10 ** (-1 / 20))                    # crête à -1 dBFS
    return x


def write(path, x):
    y = (np.clip(x, -1, 1).T * 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(y.tobytes())


if __name__ == '__main__':
    nom, out = sys.argv[1], sys.argv[2]
    if nom.startswith('intro'):
        tr, dur = intro(titre='titre' in nom)
        x = master(tr, dur, fade_out=.25)
    else:
        tr, dur = outro()
        x = master(tr, dur, fade_out=1.4)
    write(out, x)
    print(out, f'{dur:.1f} s')
