import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#1a1a1a"

def arrow(ax, x, y, dx, dy, hw=0.13, hl=0.20, lw=2.0, c=BK):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=c, linewidth=lw))

def dbl(ax, x1, y1, x2, y2, label, off=(0, 0), fs=13):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="|-|,widthA=0.4,widthB=0.4",
                                color=BK, lw=1.4))
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=BK, lw=1.4))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label, color=BK,
            fontsize=fs, ha="center", va="center", style="italic")

# ---- Figure 6 du sujet : essai de compression en enceinte indéformable
fig, ax = plt.subplots(figsize=(4.6, 5.2))
W, H = 3.0, 3.6
t = 0.42
# matériau (moucheté)
ax.add_patch(Rectangle((0, 0), W, H, facecolor="#d9d9d9", hatch="....",
                       edgecolor=BK, linewidth=1.0))
# parois latérales et fond (noirs, indéformables)
for (x, y, w, h) in [(-t, -t, t, H + t), (W, -t, t, H + t), (-t, -t, W + 2 * t, t)]:
    ax.add_patch(Rectangle((x, y), w, h, facecolor=BK, edgecolor=BK))
# piston supérieur
ax.add_patch(Rectangle((0, H + 0.12), W, 0.34, facecolor="#4d4d4d", edgecolor=BK))
# effort F
arrow(ax, W / 2, H + 1.45, 0.0, -0.80)
ax.text(W / 2 + 0.22, H + 1.42, r"$\vec{F}$", color=BK, fontsize=15)
# cotes
dbl(ax, -0.95, 0, -0.95, H, "h", off=(-0.26, 0))
dbl(ax, 0, -1.05, W, -1.05, "b", off=(0, 0.26))
# repère
ox, oy = -1.95, -0.55
arrow(ax, ox, oy, 0.0, 0.62, hw=0.10, hl=0.15, lw=1.4)
ax.text(ox + 0.12, oy + 0.72, "y", color=BK, fontsize=12, style="italic")
arrow(ax, ox, oy - 0.55, 0.62, 0.0, hw=0.10, hl=0.15, lw=1.4)
ax.plot([ox, ox], [oy - 0.55, oy], color=BK, lw=1.4)
ax.text(ox + 0.10, oy - 0.92, "x", color=BK, fontsize=12, style="italic")

ax.set_xlim(-2.6, 4.0); ax.set_ylim(-1.7, 5.6)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p53-figure6.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
print("Figure 6 écrite")
