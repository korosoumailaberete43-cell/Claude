import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow, Circle, Polygon
import numpy as np, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
INK = "#1a3a8f"

def arrow(ax, x, y, dx, dy, hw=0.08, hl=0.13, lw=1.3):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=INK, linewidth=lw))

def dblarrow(ax, x1, y1, x2, y2, label, off=(0, 0), fs=13):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label,
            color=INK, fontsize=fs, ha="center", va="center", style="italic")

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)

# --------------------------------------- p.14 : colonne sous compression
fig, ax = plt.subplots(figsize=(5.4, 4.2))
W, H = 1.65, 2.60
dx, dy = 0.58, 0.45

front = [(0, 0), (W, 0), (W, H), (0, H)]
top   = [(0, H), (W, H), (W + dx, H + dy), (dx, H + dy)]
right = [(W, 0), (W + dx, dy), (W + dx, H + dy), (W, H)]
for poly in (front, top, right):
    ax.add_patch(Polygon(poly, closed=True, fill=False,
                         edgecolor=INK, linewidth=1.7))

# charge répartie P
ax.plot([0.08, 0.08 + dx * 0.95 + W * 0.92], [H + 0.80, H + 0.80 + dy * 0.95],
        color=INK, lw=1.5)
for k in np.linspace(0.10, 0.92, 5):
    xa = 0.08 + k * (W + dx) * 0.95
    ya = H + 0.80 + k * dy * 0.95
    ytop = H + (dy if xa > W else dy * (xa / max(dx, 1e-9)) if xa < dx else dy)
    ytop = min(H + dy, ytop)
    arrow(ax, xa, ya, 0.0, -(ya - ytop - 0.03))
ax.text(W / 2 + 0.08, H + 1.08, r"$\vec{P}$", color=INK, fontsize=15, ha="center")

# cotes
dblarrow(ax, -0.34, 0, -0.34, H, "h", off=(-0.22, 0))
dblarrow(ax, 0, -0.38, W, -0.38, "a", off=(0, -0.24))
dblarrow(ax, W + 0.10, -0.12, W + dx + 0.10, dy - 0.12, "b", off=(0.26, -0.10))

# repère z, y, x
ox, oy = -2.25, 1.05
arrow(ax, ox, oy, 0.0, 0.78); ax.text(ox - 0.06, oy + 0.92, "z", color=INK, fontsize=13, style="italic")
arrow(ax, ox, oy, 0.85, 0.0); ax.text(ox + 0.96, oy - 0.04, "y", color=INK, fontsize=13, style="italic")
arrow(ax, ox, oy, -0.52, -0.62); ax.text(ox - 0.68, oy - 0.92, "x", color=INK, fontsize=13, style="italic")

ax.set_xlim(-3.3, 3.3); ax.set_ylim(-1.0, 4.3)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p14-colonne.png")

# --------------------------------------- p.17 : cercles de Mohr
fig, ax = plt.subplots(figsize=(5.8, 4.0))
s1, s2, s3 = -0.44, -0.12, 0.04
for a, b in [(s1, s3), (s1, s2), (s2, s3)]:
    ax.add_patch(Circle(((a + b) / 2, 0), abs(b - a) / 2, fill=False,
                        edgecolor=INK, linewidth=1.5))
arrow(ax, -0.62, 0, 0.92, 0, hw=0.022, hl=0.035)
ax.text(0.325, -0.045, r"$\sigma$", color=INK, fontsize=15)
arrow(ax, 0, -0.30, 0.0, 0.40, hw=0.022, hl=0.035)
ax.text(0.018, 0.345, r"$\tau$", color=INK, fontsize=15)
for val, name, dxt in [(s1, r"$\sigma_1$", 0.012), (s2, r"$\sigma_2$", 0.012),
                       (s3, r"$\sigma_3$", 0.012)]:
    ax.plot([val], [0], "o", color=INK, markersize=4)
    ax.text(val + dxt, -0.068, name, color=INK, fontsize=13)
ax.set_xlim(-0.68, 0.40); ax.set_ylim(-0.36, 0.44)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p17-mohr.png")

# --------------------------------------- p.18 : plaque exercice 8
fig, ax = plt.subplots(figsize=(6.0, 4.0))
W, H = 4.2, 2.1
ax.add_patch(Rectangle((0, 0), W, H, fill=False, edgecolor=INK, linewidth=1.7))

for x in np.linspace(0, W, 7):                       # sigma_2 (haut / bas)
    arrow(ax, x, H, 0.0, 0.80)
    arrow(ax, x, 0, 0.0, -0.80)
ax.text(W / 2, H + 1.05, r"$\sigma_2$", color=INK, fontsize=14, ha="center")
ax.text(W / 2, -1.28, r"$\sigma_2$", color=INK, fontsize=14, ha="center")

for y in np.linspace(0, H, 4):                       # sigma_1 (gauche / droite)
    arrow(ax, 0, y, -0.95, 0.0)
    arrow(ax, W, y, 0.95, 0.0)
ax.text(-1.95, H / 2, r"$\sigma_1$", color=INK, fontsize=14, va="center")
ax.text(W + 1.15, H / 2, r"$\sigma_1$", color=INK, fontsize=14, va="center")

# numéros des faces
ax.text(1.75, H - 0.30, "1", color=INK, fontsize=13, ha="center")
ax.text(0.34, H / 2 - 0.46, "2", color=INK, fontsize=13, ha="center")
ax.text(2.05, 0.22, "3", color=INK, fontsize=13, ha="center")
ax.text(W - 0.28, H / 2 - 0.05, "4", color=INK, fontsize=13, ha="center")

# cotes h et l + repère intérieur
dblarrow(ax, 0.90, 0.22, 0.90, H - 0.22, "h", off=(-0.20, 0), fs=12)
ax.text(1.26, H / 2 - 0.42, "l", color=INK, fontsize=13, style="italic")
ox, oy = 2.30, H / 2 - 0.30
arrow(ax, ox, oy, 0.0, 0.62); ax.text(ox + 0.10, oy + 0.72, "y", color=INK, fontsize=12, style="italic")
arrow(ax, ox, oy, 0.80, 0.0); ax.text(ox + 0.90, oy - 0.02, "x", color=INK, fontsize=12, style="italic")

ax.set_xlim(-2.6, 6.4); ax.set_ylim(-1.7, 2.9)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p18-plaque.png")
print("figures p14, p17, p18 écrites")
