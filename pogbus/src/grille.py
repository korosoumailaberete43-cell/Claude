"""Géométrie des symboles POGBUS, construite sur une grille modulaire.

Toutes les cotes sont exprimées en modules (u). Le symbole vit dans une boîte
de 12 x 12 modules ; u = 10 unités SVG, soit une boîte de 120 x 120.
"""

U = 10.0           # 1 module = 10 unités SVG
BOITE = 12         # le symbole tient dans 12 x 12 modules


def m(*v):
    """Convertit des modules en unités SVG."""
    return tuple(x * U for x in v) if len(v) > 1 else v[0] * U


def poly(pts, **kw):
    d = " ".join(f"{x * U:.3f},{y * U:.3f}" for x, y in pts)
    attrs = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<polygon points="{d}"{attrs}/>'


def rect(x, y, w, h, r=0, **kw):
    attrs = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in kw.items())
    rr = f' rx="{r * U:.3f}"' if r else ""
    return f'<rect x="{x * U:.3f}" y="{y * U:.3f}" width="{w * U:.3f}" height="{h * U:.3f}"{rr}{attrs}/>'


def svg(inner, w=BOITE, h=BOITE, fond=None):
    f = f'<rect width="{w * U}" height="{h * U}" fill="{fond}"/>' if fond else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w * U:.0f} {h * U:.0f}" '
            f'width="{w * U:.0f}" height="{h * U:.0f}">{f}{inner}</svg>')
