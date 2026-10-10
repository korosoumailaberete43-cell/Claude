import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import numpy as np, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#000000"
def arrow(ax, x, y, dx, dy, hw=0.11, hl=0.17, lw=1.1):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=BK, linewidth=lw))
def dbl(ax, x1, y1, x2, y2, label, off=(0, 0), fs=12):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=BK, lw=1.1))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label, color=BK,
            fontsize=fs, ha="center", va="center", style="italic")
def save(fig, n):
    fig.savefig(os.path.join(OUT, n), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# --------------------------------------------- Figure 4 : plaque (page 71)
fig, ax = plt.subplots(figsize=(7.0, 4.4))
W, H = 6.2, 3.1
ax.add_patch(Rectangle((0, 0), W, H, facecolor="#b8b8b8", edgecolor=BK, linewidth=1.3))
for x in np.linspace(0.18, W - 0.18, 16):
    arrow(ax, x, H, 0.0, 0.85); arrow(ax, x, 0, 0.0, -0.85)
ax.text(W / 2, H + 1.08, r"$\sigma_2$", color=BK, fontsize=13, ha="center")
ax.text(W / 2, -1.42, r"$\sigma_2$", color=BK, fontsize=13, ha="center")
for y in np.linspace(0.18, H - 0.18, 9):
    arrow(ax, 0, y, -0.85, 0.0); arrow(ax, W, y, 0.85, 0.0)
ax.text(-1.45, H / 2, r"$\sigma_1$", color=BK, fontsize=13, va="center", ha="center")
ax.text(W + 1.45, H / 2, r"$\sigma_1$", color=BK, fontsize=13, va="center", ha="center")
ax.text(2.85, H - 0.38, "1", color=BK, fontsize=11, ha="center")
ax.text(0.33, H / 2 - 0.10, "2", color=BK, fontsize=11, ha="center")
ax.text(2.85, 0.33, "3", color=BK, fontsize=11, ha="center")
ax.text(W - 0.60, H / 2 - 0.10, "4", color=BK, fontsize=11, ha="center")
dbl(ax, 1.55, 0.78, 1.55, H - 0.10, "h", off=(-0.24, 0))
dbl(ax, 0.55, 0.78, W - 0.25, 0.78, r"$\ell$", off=(0, 0.24))
ox, oy = 3.05, H / 2 - 0.42
arrow(ax, ox, oy, 0.0, 0.62, hw=0.08, hl=0.12); ax.text(ox - 0.14, oy + 0.52, "y", color=BK, fontsize=11, style="italic")
arrow(ax, ox, oy, 0.72, 0.0, hw=0.08, hl=0.12); ax.text(ox + 0.86, oy - 0.03, "x", color=BK, fontsize=11, style="italic")
ax.set_xlim(-2.1, 8.3); ax.set_ylim(-1.9, 4.5)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p71-figure4.png")

# --------------------------------------------- Figure 1 : plaque cisaillée (page 72)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
W, H = 5.2, 2.2
ax.add_patch(Rectangle((0, 0), W, H, facecolor="#ededed", edgecolor=BK, linewidth=2.2))
for x in np.linspace(0.15, W - 1.05, 5):
    arrow(ax, x, H + 0.50, 0.90, 0.0, hw=0.17, hl=0.26, lw=2.6)
for x in np.linspace(1.05, W - 0.15, 5):
    arrow(ax, x, -0.50, -0.90, 0.0, hw=0.17, hl=0.26, lw=2.6)
ax.text(W / 2, H + 0.78, r"$\sigma_{yx}$", color=BK, fontsize=14, ha="center", weight="bold")
ax.text(W / 2, -1.12, r"$\sigma_{yx}$", color=BK, fontsize=14, ha="center", weight="bold")
ox, oy = -0.95, 0.70
arrow(ax, ox, oy, 0.0, 0.62, hw=0.09, hl=0.14); ax.text(ox + 0.10, oy + 0.70, "y", color=BK, fontsize=13, style="italic")
ax.plot([ox, ox], [oy - 0.40, oy], color=BK, lw=1.2)
arrow(ax, ox, oy - 0.40, 0.62, 0.0, hw=0.09, hl=0.14); ax.text(ox + 0.30, oy - 0.26, "x", color=BK, fontsize=13, style="italic")
ax.set_xlim(-1.9, 6.0); ax.set_ylim(-1.6, 3.3)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p72-figure1.png")
print("figures p71, p72 écrites")
