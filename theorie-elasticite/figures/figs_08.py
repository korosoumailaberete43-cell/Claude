import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import numpy as np, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#000000"
def arrow(ax, x, y, dx, dy, hw=0.10, hl=0.16, lw=1.3):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=BK, linewidth=lw))

fig, ax = plt.subplots(figsize=(5.8, 4.4))
W, H = 3.4, 3.4
ax.add_patch(Rectangle((0, 0), W, H, fill=False, hatch="////",
                       edgecolor=BK, linewidth=2.2))
ax.add_patch(Rectangle((-0.45, -0.30), W + 0.90, 0.26,
                       facecolor=BK, edgecolor=BK))        # sol rigide
for x in np.linspace(0.12, W - 0.12, 8):
    arrow(ax, x, H + 1.05, 0.0, -0.95)
ax.text(W / 2 - 0.15, H + 1.30, r"$\sigma yy\ =\ f$", color=BK, fontsize=15, ha="center")
ax.text(W + 0.18, H + 0.22, r"$f$", color=BK, fontsize=15)
ax.text(-0.10, H - 0.35, r"$\sigma xx =\ 0$", color=BK, fontsize=15, ha="right")
ax.text(-0.08, H / 2 + 0.25, r"$\sigma xy{=}0$", color=BK, fontsize=14, ha="right")
ax.text(W + 0.12, H / 2 + 0.25, r"$\sigma xy = 0$", color=BK, fontsize=15, ha="left")
ax.text(W / 2 - 0.30, -0.85, r"$u_y{=}\ 0$", color=BK, fontsize=15, ha="center")
ox, oy = -0.95, 0.55
arrow(ax, ox, oy, 0.0, 0.70); ax.text(ox - 0.06, oy + 0.84, "y", color=BK, fontsize=16, style="italic", ha="center")
arrow(ax, ox, oy, 0.70, 0.0); ax.text(ox + 0.84, oy - 0.04, "x", color=BK, fontsize=16, style="italic")
ax.set_xlim(-2.5, 5.1); ax.set_ylim(-1.3, 5.2)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p58-bloc-cl.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
print("figure p58 écrite")
