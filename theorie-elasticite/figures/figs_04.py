import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import numpy as np, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
INK = "#1a3a8f"

def arrow(ax, x, y, dx, dy, hw=0.085, hl=0.14, lw=1.3):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=INK, linewidth=lw))

# ------------------------------- p.19 : état plan de contrainte (cisaillement)
fig, ax = plt.subplots(figsize=(5.6, 3.2))
W, H = 4.0, 1.5
ax.add_patch(Rectangle((0, 0), W, H, fill=False, hatch="///",
                       edgecolor=INK, linewidth=1.7))

for x in np.linspace(0.25, W - 1.05, 5):        # sigma_yx vers la droite (haut)
    arrow(ax, x, H + 0.42, 0.70, 0.0)
ax.text(W / 2, H + 0.78, r"$\sigma_{yx}$", color=INK, fontsize=14, ha="center")

for x in np.linspace(0.95, W - 0.35, 5):        # sigma_yx vers la gauche (bas)
    arrow(ax, x, -0.42, -0.70, 0.0)
ax.text(W / 2, -1.08, r"$\sigma_{yx}$", color=INK, fontsize=14, ha="center")

ox, oy = -1.45, 0.10
arrow(ax, ox, oy, 0.0, 0.85); ax.text(ox + 0.10, oy + 0.95, "y", color=INK, fontsize=13, style="italic")
arrow(ax, ox, oy, 0.85, 0.0); ax.text(ox + 0.95, oy - 0.04, "x", color=INK, fontsize=13, style="italic")

ax.set_xlim(-2.0, 4.6); ax.set_ylim(-1.5, 2.6)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p19-cisaillement.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
plt.close(fig)
print("figure p19 écrite")
