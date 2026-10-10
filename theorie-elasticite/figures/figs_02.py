import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow, Circle
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
INK = "#1a3a8f"

def arrow(ax, x, y, dx, dy, hw=0.09, hl=0.14, lw=1.4):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=INK, linewidth=lw))

def dblarrow(ax, x1, y1, x2, y2, label, off=(0, 0), fs=13):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label,
            color=INK, fontsize=fs, ha="center", va="center", style="italic")

# ------------------------------------------- p.9 : essai de compression
fig, ax = plt.subplots(figsize=(5.4, 4.0))
W, H = 3.0, 2.0          # éprouvette
t = 0.42                 # épaisseur des parois rigides

# éprouvette (matériau pointillé)
ax.add_patch(Rectangle((0, 0), W, H, facecolor="white", hatch="....",
                       edgecolor=INK, linewidth=1.3))
# enceinte rigide : 4 parois hachurées
walls = [(-t, -t, t, H + 2 * t),        # paroi gauche
         (W, -t, t, H + 2 * t),         # paroi droite
         (0, H, W, t),                  # plateau supérieur
         (0, -t, W, t)]                 # plateau inférieur
for (x, y, w, h) in walls:
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white", hatch="\\\\\\",
                           edgecolor=INK, linewidth=1.6))

# effort F
arrow(ax, W / 2, H + t + 0.78, 0.0, -0.58, hw=0.13, hl=0.18, lw=1.8)
ax.text(W / 2 + 0.20, H + t + 0.50, r"$\vec{F}$", color=INK, fontsize=15)

# repère
arrow(ax, -1.75, 0.55, 0.0, 0.70)
arrow(ax, -1.75, 0.55, 0.70, 0.0)
ax.text(-1.90, 1.22, "y", color=INK, fontsize=13, style="italic")
ax.text(-0.93, 0.40, "x", color=INK, fontsize=13, style="italic")

# cotes h et b
dblarrow(ax, -0.72, 0, -0.72, H, "h", off=(-0.24, 0))
dblarrow(ax, 0, -t - 0.42, W, -t - 0.42, "b", off=(0, -0.26))
arrow(ax, W + t / 2, -t - 0.18, 0.0, -0.42)     # petite flèche bas-droite

ax.set_xlim(-2.3, 4.1)
ax.set_ylim(-1.6, 3.5)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p09-compression.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
plt.close(fig)

# ------------------------------------------- p.12 : cercles de Mohr
fig, ax = plt.subplots(figsize=(5.8, 4.0))
s1, s2, s3 = -0.47, -2.47, -0.97     # sigma_1, sigma_2, sigma_3

for a, b in [(s2, s1), (s2, s3), (s3, s1)]:
    ax.add_patch(Circle(((a + b) / 2, 0), abs(b - a) / 2, fill=False,
                        edgecolor=INK, linewidth=1.5))

# axe sigma
arrow(ax, -3.15, 0, 4.45, 0, hw=0.10, hl=0.16)
ax.text(1.42, -0.22, r"$\sigma$", color=INK, fontsize=15)
# axe tau, tracé en sigma_1 comme sur le croquis
arrow(ax, s1, -0.15, 0.0, 1.70, hw=0.10, hl=0.16)
ax.text(s1 + 0.14, 1.62, r"$\tau$", color=INK, fontsize=15)

for val, name in [(s2, r"$\sigma_2$"), (s3, r"$\sigma_3$"), (s1, r"$\sigma_1$")]:
    ax.plot([val], [0], "o", color=INK, markersize=4)
    ax.text(val + 0.06, -0.30, name, color=INK, fontsize=13)
ax.plot([0.95], [0], "o", color=INK, markersize=3)

ax.set_xlim(-3.4, 1.9)
ax.set_ylim(-1.45, 1.95)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig(os.path.join(OUT, "fig-p12-mohr.png"), dpi=200,
            bbox_inches="tight", facecolor="white")
plt.close(fig)
print("figures p9 et p12 écrites")
