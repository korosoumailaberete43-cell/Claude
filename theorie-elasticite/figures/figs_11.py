import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrow
import numpy as np, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#000000"
def arrow(ax, x, y, dx, dy, hw=0.10, hl=0.16, lw=1.1):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=BK, linewidth=lw))

fig, ax = plt.subplots(figsize=(4.4, 5.0))
kx, ky = 0.46, 0.34
def P(X, Y, Z): return (X + kx * Z, Y + ky * Z)
def face(pts, fc="none", lw=1.3):
    ax.add_patch(Polygon([P(*p) for p in pts], closed=True, facecolor=fc,
                         edgecolor=BK, linewidth=lw))
# sol (dalle rigide)
face([(-1.5, 0, -1.3), (3.3, 0, -1.3), (3.3, 0, 2.6), (-1.5, 0, 2.6)], fc="#d6d6d6")
face([(-1.5, 0, -1.3), (3.3, 0, -1.3), (3.3, -0.30, -1.3), (-1.5, -0.30, -1.3)], fc="#c2c2c2")
# bloc
W, H, T = 1.5, 3.4, 1.2
face([(0, 0, 0), (W, 0, 0), (W, H, 0), (0, H, 0)], fc="#fdfdfd")      # avant
face([(0, H, 0), (W, H, 0), (W, H, T), (0, H, T)], fc="#efefef")      # dessus
face([(W, 0, 0), (W, 0, T), (W, H, T), (W, H, 0)], fc="#cfcfcf")      # droite
# pression p
for (X, Z) in [(0.2, 0.15), (0.55, 0.15), (0.95, 0.15), (1.35, 0.15),
               (0.05, 0.6), (0.05, 1.0)]:
    xa, ya = P(X, H + 0.95, Z); xb, yb = P(X, H + 0.06, Z)
    arrow(ax, xa, ya, 0.0, -(ya - yb))
xp, yp = P(W / 2, H + 1.15, 0.6)
ax.text(xp, yp + 0.08, r"$p$", color=BK, fontsize=14, ha="center", style="italic")
# repère
oxp, oyp = P(-1.05, 0.55, 0.7)
arrow(ax, oxp, oyp, 0.0, 0.72, hw=0.08, hl=0.13); ax.text(oxp + 0.08, oyp + 0.80, "z", color=BK, fontsize=11, style="italic")
arrow(ax, oxp, oyp, 0.72, 0.0, hw=0.08, hl=0.13); ax.text(oxp + 0.82, oyp - 0.04, "y", color=BK, fontsize=11, style="italic")
arrow(ax, oxp, oyp, -kx * 1.3, -ky * 1.3, hw=0.08, hl=0.13); ax.text(oxp - 0.86, oyp - 0.58, "x", color=BK, fontsize=11, style="italic")
ax.set_xlim(-2.4, 4.8); ax.set_ylim(-1.4, 6.3)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p78-bloc3d.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
print("figure p78 écrite")
