import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow, Polygon
import numpy as np, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#000000"
def arrow(ax, x, y, dx, dy, hw=0.09, hl=0.15, lw=1.1):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=BK, linewidth=lw))
def dbl(ax, x1, y1, x2, y2, label, off=(0, 0), fs=13):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=BK, lw=1.2))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label, color=BK,
            fontsize=fs, ha="center", va="center", style="italic")
def save(fig, n):
    fig.savefig(os.path.join(OUT, n), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# -------------------------------------- Figure 2 : mur (sujet, page 61)
fig, ax = plt.subplots(figsize=(7.0, 3.8))
kx, ky = 0.40, 0.30
def P(X, Y, Z): return (X + kx * Z, Y + ky * Z)
def face(pts, lw=1.2, fc="none"):
    ax.add_patch(Polygon([P(*p) for p in pts], closed=True, facecolor=fc,
                         edgecolor=BK, linewidth=lw))
T, L, H = 1.30, 8.0, 2.10
face([(0, 0, 0), (L, 0, 0), (L, H, 0), (0, H, 0)], fc="#f0f0f0")       # avant
face([(0, H, 0), (L, H, 0), (L, H, T), (0, H, T)], fc="#fafafa")       # dessus
face([(L, 0, 0), (L, 0, T), (L, H, T), (L, H, 0)], fc="#bfbfbf")       # droite
for X0 in (-0.42, L + 0.12):                                           # panneaux
    face([(X0, -0.30, -0.55), (X0, -0.30, T + 0.95), (X0, H + 1.15, T + 0.95),
          (X0, H + 1.15, -0.55)], fc="#fcfcfc")
    face([(X0, -0.30, -0.55), (X0 + 0.22, -0.30, -0.55),
          (X0 + 0.22, H + 1.15, -0.55), (X0, H + 1.15, -0.55)], fc="#f2f2f2")
for X in np.linspace(0.15, L - 0.15, 15):                              # charge f
    xa, ya = P(X, H + 1.55, T / 2); xb, yb = P(X, H + 0.04, T / 2)
    arrow(ax, xa, ya, 0.0, -(ya - yb))
xf, yf = P(L / 2, H + 1.72, T / 2)
ax.text(xf, yf + 0.10, r"$\vec{f}$", color=BK, fontsize=15, ha="center")
oxp, oyp = P(L / 2 - 0.9, 0.35, T / 2)                                 # repère
arrow(ax, oxp, oyp, 0.0, 0.95); ax.text(oxp + 0.10, oyp + 1.02, "y", color=BK, fontsize=12, style="italic")
arrow(ax, oxp, oyp, 1.70, 0.0); ax.text(oxp + 1.80, oyp - 0.05, "x", color=BK, fontsize=12, style="italic")
arrow(ax, oxp, oyp, -kx * 1.6, -ky * 1.6); ax.text(oxp - 0.95, oyp - 0.60, "z", color=BK, fontsize=12, style="italic")
ax.text(L / 2 - 1.1, -1.95, "Système de blocage du déplacement suivant l'axe x",
        color=BK, fontsize=10, ha="center", style="italic")
for Xt in (-0.35, L + 0.22):
    xa, ya = P(Xt, -0.25, -0.55)
    ax.annotate("", xy=(xa, ya), xytext=(L / 2 - 1.1, -1.80),
                arrowprops=dict(arrowstyle="->", color=BK, lw=0.8, ls=(0, (2, 2))))
ax.set_xlim(-1.8, 10.6); ax.set_ylim(-2.8, 5.3)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p61-figure2.png")

# -------------------------------------- Figure 3 : bloc (sujet, page 63)
fig, ax = plt.subplots(figsize=(6.4, 3.4))
W, H = 5.4, 2.2
ax.add_patch(Rectangle((0, 0), W, H, fill=False, hatch="////",
                       edgecolor=BK, linewidth=1.3))
ax.add_patch(Rectangle((-0.70, -0.26), W + 1.40, 0.24, facecolor=BK, edgecolor=BK))
for x in np.linspace(0.08, W - 0.08, 14):
    arrow(ax, x, H + 0.80, 0.0, -0.74)
ax.text(W / 2, H + 1.00, r"$\vec{f}$", color=BK, fontsize=15, ha="center")
dbl(ax, W + 0.55, 0, W + 0.55, H, "h", off=(-0.26, 0))
dbl(ax, 0, -0.85, W, -0.85, r"$\ell$", off=(0, 0.26))
ox, oy = -1.45, 0.55
arrow(ax, ox, oy, 0.0, 0.62); ax.text(ox + 0.10, oy + 0.70, "y", color=BK, fontsize=12, style="italic")
arrow(ax, ox + 0.30, oy - 0.30, 0.60, 0.0); ax.plot([ox, ox + 0.30], [oy, oy - 0.30], color=BK, lw=0)
ax.plot([ox, ox], [oy - 0.30, oy], color=BK, lw=1.1); ax.plot([ox, ox + 0.30], [oy - 0.30, oy - 0.30], color=BK, lw=1.1)
ax.text(ox + 0.98, oy - 0.33, "x", color=BK, fontsize=12, style="italic")
ax.set_xlim(-2.1, 6.6); ax.set_ylim(-1.4, 3.7)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p63-figure3.png")
print("figures p61, p63 écrites")
