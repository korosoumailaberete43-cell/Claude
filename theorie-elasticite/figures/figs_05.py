import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow, Polygon, FancyBboxPatch
import numpy as np, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
INK = "#1a3a8f"

def arrow(ax, x, y, dx, dy, hw=0.085, hl=0.14, lw=1.3):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=INK, linewidth=lw))

def dbl(ax, x1, y1, x2, y2, label, off=(0, 0), fs=13):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label, color=INK,
            fontsize=fs, ha="center", va="center", style="italic")

def circled(ax, x, y, n, fs=12):
    ax.text(x, y, n, color=INK, fontsize=fs, ha="center", va="center",
            bbox=dict(boxstyle="circle,pad=0.30", fc="white", ec=INK, lw=1.2))

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches="tight",
                facecolor="white"); plt.close(fig)

# ------------------------------------------------- p.28 : encadré « NB »
fig, ax = plt.subplots(figsize=(6.4, 3.4))
def box(x, y, w, h, txt, fs=12, round_=False):
    style = "round,pad=0.12" if round_ else "square,pad=0.10"
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style,
                                fc="white", ec=INK, lw=1.5))
    ax.text(x + w / 2, y + h / 2, txt, color=INK, fontsize=fs,
            ha="center", va="center")

ax.text(5.0, 5.35, "NB :", color=INK, fontsize=13, ha="center", va="center",
        bbox=dict(boxstyle="circle,pad=0.45", fc="white", ec=INK, lw=1.4))
box(1.05, 3.75, 2.5, 0.75, r"Si $\varepsilon_{33}=0$")
box(6.45, 3.75, 2.5, 0.75, r"Si $\sigma_{33}=0$")
box(0.15, 1.55, 4.3, 0.85, "état plan de déformation", round_=True)
box(6.30, 1.40, 2.8, 1.10, "état plan\nde contrainte", round_=True)
ax.annotate("", xy=(2.75, 4.60), xytext=(4.45, 5.20),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
ax.annotate("", xy=(7.25, 4.60), xytext=(5.55, 5.20),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
ax.annotate("", xy=(2.30, 2.50), xytext=(2.30, 3.70),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
ax.annotate("", xy=(7.70, 2.60), xytext=(7.70, 3.70),
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
ax.set_xlim(-0.2, 9.4); ax.set_ylim(1.1, 6.1)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p28-nb.png")

# ------------------------------------------- p.28 : compression d'un bloc
fig, ax = plt.subplots(figsize=(5.8, 3.6))
W, H = 4.2, 1.85
ax.add_patch(Rectangle((0, 0), W, H, fill=False, hatch="///",
                       edgecolor=INK, linewidth=1.8))
ax.add_patch(Rectangle((-0.30, -0.34), W + 0.60, 0.30, fill=False,
                       edgecolor=INK, linewidth=1.5))      # sol
for x in np.linspace(0.18, W - 0.18, 8):
    arrow(ax, x, H + 0.85, 0.0, -0.78)
ax.text(W / 2 + 0.40, H + 1.02, r"$\vec{f}$", color=INK, fontsize=15)
circled(ax, W + 0.55, H + 0.72, "1")
dbl(ax, W + 0.55, 0, W + 0.55, H, "h", off=(0.26, 0.26))
circled(ax, W + 0.81, H / 2 - 0.34, "3")
dbl(ax, 0, -0.72, W, -0.72, "l", off=(0, -0.05))
circled(ax, W / 2 + 0.62, -0.72, "2")
ox, oy = -1.55, 0.18
arrow(ax, ox, oy, 0.0, 0.80); ax.text(ox + 0.10, oy + 0.92, "y", color=INK, fontsize=13, style="italic")
arrow(ax, ox, oy, 0.80, 0.0); ax.text(ox + 0.90, oy - 0.06, "x", color=INK, fontsize=13, style="italic")
circled(ax, -0.40, 1.25, "4")
ax.set_xlim(-2.1, 5.9); ax.set_ylim(-1.3, 3.3)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p28-bloc.png")

# ------------------------------------------- p.29 : état déformé du bloc
fig, ax = plt.subplots(figsize=(5.8, 3.6))
W, H = 3.6, 2.0
Wd, Hd = 4.1, 1.45
ax.add_patch(Rectangle((0, 0), W, H, fill=False, edgecolor=INK, linewidth=1.2))
ax.add_patch(Rectangle((-(Wd - W) / 2, 0), Wd, Hd, fill=False,
                       edgecolor=INK, linewidth=1.9))
ax.add_patch(Rectangle((-(Wd - W) / 2 - 0.12, -0.30), Wd + 0.24, 0.26,
                       fill=False, edgecolor=INK, linewidth=1.4))   # sol
for x in np.linspace(0.05, W - 0.05, 10):
    arrow(ax, x, H + 0.90, 0.0, -0.80)
ax.text(W + 0.14, H + 0.92, r"$\vec{f}$", color=INK, fontsize=15)
dbl(ax, W + 0.75, 0, W + 0.75, H, "h", off=(0.26, 0))
dbl(ax, -(Wd - W) / 2 - 0.55, 0, -(Wd - W) / 2 - 0.55, Hd, r"$h_1$", off=(-0.34, 0))
dbl(ax, 0, -0.72, W, -0.72, "l", off=(0, 0.24))
dbl(ax, -(Wd - W) / 2, -1.12, W + (Wd - W) / 2, -1.12, r"$l_1$", off=(0, 0.26))
ax.set_xlim(-1.7, 5.3); ax.set_ylim(-1.7, 3.4)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p29-deforme.png")

# ------------------------------------------------- p.30 : mur 3D
fig, ax = plt.subplots(figsize=(6.4, 4.6))
kx, ky = 0.46, 0.34                      # projection oblique sur z
def P(X, Y, Z): return (X + kx * Z, Y + ky * Z)
def face(pts, lw=1.6):
    ax.add_patch(Polygon([P(*p) for p in pts], closed=True, fill=False,
                         edgecolor=INK, linewidth=lw))

T = 1.10                                  # épaisseur (z)
# sol
face([(-0.9, 0, -0.9), (6.9, 0, -0.9), (6.9, 0, 2.3), (-0.9, 0, 2.3)], lw=1.4)
# mur central
face([(0.7, 0, 0), (5.3, 0, 0), (5.3, 1.8, 0), (0.7, 1.8, 0)])          # avant
face([(0.7, 1.8, 0), (5.3, 1.8, 0), (5.3, 1.8, T), (0.7, 1.8, T)])      # dessus
face([(5.3, 0, 0), (5.3, 0, T), (5.3, 1.8, T), (5.3, 1.8, 0)])          # droite
# panneaux de blocage (gauche / droite)
for X0 in (0.10, 5.30):
    face([(X0, 0, -0.5), (X0, 0, 1.9), (X0, 2.7, 1.9), (X0, 2.7, -0.5)], lw=1.4)
    face([(X0, 0, -0.5), (X0 + 0.30, 0, -0.5), (X0 + 0.30, 2.7, -0.5), (X0, 2.7, -0.5)], lw=1.4)
# charge f
for X in np.linspace(0.95, 5.05, 10):
    xa, ya = P(X, 2.72, T / 2)
    xb, yb = P(X, 1.82, T / 2)
    arrow(ax, xa, ya, 0.0, -(ya - yb), hw=0.09, hl=0.15)
x0, y0 = P(3.0, 2.78, T / 2); ax.plot(*zip(P(0.95, 2.72, T/2), P(5.05, 2.72, T/2)), color=INK, lw=1.4)
ax.text(x0 + 0.18, y0 + 0.30, r"$\vec{f}$", color=INK, fontsize=15)
# repère
oxp, oyp = P(2.55, 0.05, 1.25)
arrow(ax, oxp, oyp, 0.0, 1.00); ax.text(oxp + 0.10, oyp + 1.10, "y", color=INK, fontsize=13, style="italic")
arrow(ax, oxp, oyp, 1.00, 0.0); ax.text(oxp + 1.10, oyp - 0.06, "x", color=INK, fontsize=13, style="italic")
arrow(ax, oxp, oyp, -kx * 1.5, -ky * 1.5); ax.text(oxp - 0.95, oyp - 0.60, "z", color=INK, fontsize=13, style="italic")
# annotation
ax.text(3.0, -1.95, "Système de blocage\ndu déplacement suivant l'axe x",
        color=INK, fontsize=11.5, ha="center", va="top")
for Xt in (0.25, 5.45):
    xa, ya = P(Xt, 0.05, -0.5)
    ax.annotate("", xy=(xa, ya), xytext=(3.0, -1.80),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
ax.set_xlim(-1.6, 8.4); ax.set_ylim(-3.6, 4.6)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p30-mur.png")
print("figures p28 (x2), p29, p30 écrites")
