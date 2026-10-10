import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import numpy as np, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#000000"
fig, ax = plt.subplots(figsize=(3.8, 3.6))
W, H, t = 2.8, 2.9, 0.34
ax.add_patch(Rectangle((0, 0), W, H, facecolor="white", hatch="xxxx",
                       edgecolor=BK, linewidth=1.0))
for (x, y, w, h) in [(-t, -t, t, H + t), (W, -t, t, H + t), (-t, -t, W + 2 * t, t)]:
    ax.add_patch(Rectangle((x, y), w, h, facecolor=BK, edgecolor=BK))
for x in np.linspace(0.18, W - 0.18, 7):
    ax.add_patch(FancyArrow(x, H + 0.78, 0.0, -0.70, head_width=0.13,
                            head_length=0.18, length_includes_head=True,
                            color=BK, linewidth=2.0))
ax.text(W / 2, H + 0.92, r"$p$", color=BK, fontsize=14, ha="center", style="italic")
ax.set_xlim(-0.8, 3.6); ax.set_ylim(-0.8, 4.3)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p83-mohrcoulomb.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
print("figure p83 écrite")
