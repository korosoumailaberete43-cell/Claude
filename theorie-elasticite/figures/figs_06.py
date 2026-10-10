import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrow
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
INK = "#1a3a8f"
def arrow(ax, x, y, dx, dy, hw=0.09, hl=0.15, lw=1.3):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=INK, linewidth=lw))

fig, ax = plt.subplots(figsize=(5.8, 3.8))
s3, s2, s1 = -2.0, 0.4, 2.0          # sigma_III, sigma_II, sigma_I
for a, b in [(s3, s1), (s3, s2), (s2, s1)]:
    ax.add_patch(Circle(((a + b) / 2, 0), abs(b - a) / 2, fill=False,
                        edgecolor=INK, linewidth=1.5))
arrow(ax, -2.75, 0, 5.70, 0)
ax.text(2.85, -0.26, r"$\sigma$", color=INK, fontsize=15)
arrow(ax, 0, -1.55, 0.0, 2.65)
ax.text(0.14, 1.00, r"$\tau$", color=INK, fontsize=15)
for v, n in [(s3, r"$\sigma_{III}$"), (s2, r"$\sigma_{II}$"), (s1, r"$\sigma_{I}$")]:
    ax.plot([v], [0], "o", color=INK, markersize=4)
    ax.text(v, 0.16, n, color=INK, fontsize=12.5, ha="center")
ax.set_xlim(-3.0, 3.3); ax.set_ylim(-1.7, 1.6)
ax.set_aspect("equal"); ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p39-mohr.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
print("figure p39 écrite")
