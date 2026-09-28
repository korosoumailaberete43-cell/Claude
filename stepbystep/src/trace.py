"""Vectorisation fidèle des pictogrammes du logo original (potrace, courbes de Bézier).
Chaque zone est agrandie ×4 et lissée avant le tracé pour gommer la compression JPEG."""
import numpy as np
import cv2
import potrace
from PIL import Image

SRC = "source/logo_original.jpg"
_img = None


def _load():
    global _img
    if _img is None:
        _img = np.array(Image.open(SRC).convert("RGB")).astype(np.float32)
    return _img


def mask(region, fn, up=4, blur=1.2):
    """region=(x0,y0,x1,y1) ; fn(r,g,b)->bool. Renvoie le masque agrandi et lissé."""
    x0, y0, x1, y1 = region
    im = _load()[y0:y1, x0:x1]
    big = cv2.resize(im, ((x1 - x0) * up, (y1 - y0) * up), interpolation=cv2.INTER_CUBIC)
    big = cv2.GaussianBlur(big, (0, 0), blur * up / 2)
    r, g, b = big[..., 0], big[..., 1], big[..., 2]
    return fn(r, g, b)


def trace(region, fn, up=4, blur=1.2, turdsize=40, alphamax=1.0, opttolerance=0.2):
    """Renvoie un attribut d (path SVG, règle evenodd) en coordonnées de l'image originale."""
    x0, y0, _, _ = region
    m = mask(region, fn, up, blur)
    bm = potrace.Bitmap(~m)
    plist = bm.trace(turdsize=turdsize, alphamax=alphamax, opticurve=True, opttolerance=opttolerance)
    s = 1 / up

    def P(p):
        return f"{x0 + p.x * s:.2f} {y0 + p.y * s:.2f}"
    parts = []
    for curve in plist:
        parts.append(f"M{P(curve.start_point)}")
        for seg in curve.segments:
            if seg.is_corner:
                parts.append(f"L{P(seg.c)}L{P(seg.end_point)}")
            else:
                parts.append(f"C{P(seg.c1)} {P(seg.c2)} {P(seg.end_point)}")
        parts.append("Z")
    return "".join(parts)


WHITE = lambda r, g, b: (r > 150) & (g > 150) & (b > 150)
