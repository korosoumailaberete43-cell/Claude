import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
os.makedirs(OUT, exist_ok=True)
INK = "#1a3a8f"   # encre bleue du cahier

def arrow(ax, x, y, dx, dy, **kw):
    kw.setdefault("head_width", 0.09)
    kw.setdefault("head_length", 0.14)
    kw.setdefault("length_includes_head", True)
    kw.setdefault("color", INK)
    kw.setdefault("linewidth", 1.4)
    ax.add_patch(FancyArrow(x, y, dx, dy, **kw))

def dblarrow(ax, x1, y1, x2, y2, label, offset=(0, 0), fs=13):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
    ax.text((x1 + x2) / 2 + offset[0], (y1 + y2) / 2 + offset[1], label,
            color=INK, fontsize=fs, ha="center", va="center", style="italic")

# ---------------------------------------------------------------- figure p.1
fig, ax = plt.subplots(figsize=(5.6, 3.5))
L, H = 4.0, 2.0

# plaque hachurée
ax.add_patch(Rectangle((0, 0), L, H, fill=False, hatch="///",
                       edgecolor=INK, linewidth=1.8))
# bande verticale (bord gauche) et bande horizontale (bord bas) du croquis
ax.add_patch(Rectangle((0, 0), 0.30, H, fill=False, edgecolor=INK, linewidth=1.4))
ax.add_patch(Rectangle((0, 0), L, 0.30, fill=False, edgecolor=INK, linewidth=1.4))

# cotes h et l
dblarrow(ax, -0.45, 0, -0.45, H, "h", offset=(-0.22, 0))
dblarrow(ax, 0, -0.55, L, -0.55, "l", offset=(0, -0.26))

# repère x, y
arrow(ax, -1.25, -0.95, 0.0, 0.85)          # y
arrow(ax, -1.25, -0.95, 0.85, 0.0)          # x
ax.text(-1.40, 0.00, "y", color=INK, fontsize=13, style="italic", ha="center")
ax.text(-0.33, -1.15, "x", color=INK, fontsize=13, style="italic", ha="center")

# contraintes
arrow(ax, 1.15, H + 0.08, 0.0, 0.52)        # sigma_yy
ax.text(1.32, H + 0.68, r"$\sigma_{yy}$", color=INK, fontsize=13, va="center")

arrow(ax, 2.70, H + 0.52, 0.72, 0.0)        # sigma_yx
ax.text(3.55, H + 0.52, r"$\sigma_{yx}$", color=INK, fontsize=13, va="center")

arrow(ax, L + 0.12, 0.95, 0.0, 0.52)        # sigma_xy
ax.text(L + 0.28, 1.56, r"$\sigma_{xy}$", color=INK, fontsize=13, va="center")

arrow(ax, L + 0.05, 0.72, 0.62, 0.0)        # sigma_xx
ax.text(L + 0.72, 0.72, r"$\sigma_{xx}$", color=INK, fontsize=13, va="center")

ax.set_xlim(-1.9, 6.0)
ax.set_ylim(-1.5, 3.3)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p01-plaque.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
plt.close(fig)
print("fig-p01-plaque.png écrit")
