import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow, Polygon, Arc
import numpy as np, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
BK = "#000000"
def arrow(ax, x, y, dx, dy, hw=0.11, hl=0.17, lw=1.3, c=BK):
    ax.add_patch(FancyArrow(x, y, dx, dy, head_width=hw, head_length=hl,
                            length_includes_head=True, color=c, linewidth=lw))
def dbl(ax, x1, y1, x2, y2, label, off=(0, 0), fs=12):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color=BK, lw=1.1))
    ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], label, color=BK,
            fontsize=fs, ha="center", va="center", style="italic")
def circled(ax, x, y, n, fs=11):
    ax.text(x, y, n, color=BK, fontsize=fs, ha="center", va="center",
            bbox=dict(boxstyle="circle,pad=0.26", fc="white", ec=BK, lw=1.0))
def save(fig, n):
    fig.savefig(os.path.join(OUT, n), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ---------------------------------------- Fig. 5.a : colonne (page 87)
fig, ax = plt.subplots(figsize=(4.6, 4.0))
kx, ky = 0.44, 0.33
def P(X, Y, Z): return (X + kx * Z, Y + ky * Z)
def face(pts, fc="none", lw=1.3):
    ax.add_patch(Polygon([P(*p) for p in pts], closed=True, facecolor=fc,
                         edgecolor=BK, linewidth=lw))
W, H, T = 3.6, 1.5, 1.25
# support rigide en L (sombre)
face([(-0.95, -0.55, -0.6), (-0.42, -0.55, -0.6), (-0.42, H + 1.5, -0.6), (-0.95, H + 1.5, -0.6)], fc="#3a3a3a")
face([(-0.95, -0.55, -0.6), (W + 0.6, -0.55, -0.6), (W + 0.6, -0.05, -0.6), (-0.95, -0.05, -0.6)], fc="#3a3a3a")
face([(-0.95, -0.55, -0.6), (-0.95, -0.55, T + 1.1), (-0.95, H + 1.5, T + 1.1), (-0.95, H + 1.5, -0.6)], fc="#555555")
# colonne
face([(0, 0, 0), (W, 0, 0), (W, H, 0), (0, H, 0)], fc="#ffffff")
face([(0, H, 0), (W, H, 0), (W, H, T), (0, H, T)], fc="#f0f0f0")
face([(W, 0, 0), (W, 0, T), (W, H, T), (W, H, 0)], fc="#dcdcdc")
for Y in np.linspace(0.12, H - 0.12, 5):                    # effort P
    xa, ya = P(W + 1.00, Y, T / 2); xb, yb = P(W + 0.04, Y, T / 2)
    arrow(ax, xa, ya, -(xa - xb), -(ya - yb), hw=0.10, hl=0.16)
xp, yp = P(W + 1.15, H + 0.30, T / 2)
ax.text(xp, yp, r"$\vec{P}$", color=BK, fontsize=14, ha="center")
dbl(ax, *P(0, H + 0.55, T / 2), *P(W, H + 0.55, T / 2), "h", off=(0, 0.24))
oxp, oyp = P(0.35, H + 1.35, T / 2)
arrow(ax, oxp, oyp, -0.70, 0.0, hw=0.08, hl=0.13); ax.text(oxp - 0.88, oyp - 0.04, "x", color=BK, fontsize=11, style="italic")
arrow(ax, oxp, oyp, 0.0, -0.62, hw=0.08, hl=0.13); ax.text(oxp - 0.04, oyp - 0.84, "y", color=BK, fontsize=11, style="italic")
arrow(ax, oxp, oyp, kx * 1.4, ky * 1.4, hw=0.08, hl=0.13); ax.text(oxp + 0.78, oyp + 0.56, "z", color=BK, fontsize=11, style="italic")
circled(ax, *P(W / 2, -0.95, T / 2), "a")
ax.set_xlim(-2.0, 6.6); ax.set_ylim(-1.8, 4.3)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p87-figure5a.png")

# ---------------------------------------- Fig. 5.b : plaque (page 87)
fig, ax = plt.subplots(figsize=(5.6, 3.8))
W, H, t = 4.3, 2.2, 0.34
ax.add_patch(Rectangle((-t, -t), t, H + t, facecolor="#2b2b2b", edgecolor=BK))   # appui gauche
ax.add_patch(Rectangle((-t, -t), W + t, t, facecolor="#2b2b2b", edgecolor=BK))   # appui bas
ax.add_patch(Rectangle((0, 0), W, H, fill=False, hatch="///", edgecolor=BK, linewidth=1.4))
arrow(ax, 1.15, H + 0.08, 0.0, 0.62)
ax.text(1.32, H + 0.80, r"$\sigma_{yy}$", color=BK, fontsize=13)
arrow(ax, 2.75, H + 0.58, 0.78, 0.0)
ax.text(3.70, H + 0.58, r"$\sigma_{yx}$", color=BK, fontsize=13, va="center")
arrow(ax, W + 0.10, 1.05, 0.0, 0.58)
ax.text(W + 0.26, 1.72, r"$\sigma_{xy}$", color=BK, fontsize=13)
arrow(ax, W + 0.05, 0.75, 0.68, 0.0)
ax.text(W + 0.80, 0.75, r"$\sigma_{xx}$", color=BK, fontsize=13, va="center")
dbl(ax, -0.95, 0, -0.95, H, "h", off=(-0.24, 0))
dbl(ax, 0, -1.00, W, -1.00, r"$\ell$", off=(0, -0.26))
ox, oy = -2.05, 0.60
arrow(ax, ox, oy, 0.0, 0.62, hw=0.08, hl=0.13); ax.text(ox + 0.10, oy + 0.70, "y", color=BK, fontsize=12, style="italic")
arrow(ax, ox, oy, 0.62, 0.0, hw=0.08, hl=0.13); ax.text(ox + 0.72, oy - 0.04, "x", color=BK, fontsize=12, style="italic")
circled(ax, W / 2, -1.62, "b")
ax.set_xlim(-2.7, 6.4); ax.set_ylim(-2.1, 3.6)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p87-figure5b.png")

# ---------------------------------------- Fig. 2.a (page 88)
fig, ax = plt.subplots(figsize=(5.2, 3.2))
W, H = 3.8, 2.3
ax.add_patch(Rectangle((0, 0), W, H, fill=False, edgecolor=BK, linewidth=1.5))
dbl(ax, 0, H + 0.45, W, H + 0.45, r"$\ell_0$", off=(0, 0.26))
dbl(ax, W + 0.45, 0, W + 0.45, H, r"$h_0$", off=(0.30, 0))
arrow(ax, -0.25, H / 2, -0.85, 0.0, hw=0.18, hl=0.26, lw=2.6)
ax.text(-1.25, H / 2 + 0.26, r"$\varepsilon_{xx}$", color=BK, fontsize=13, ha="center")
arrow(ax, W + 0.25, H / 2, 0.85, 0.0, hw=0.18, hl=0.26, lw=2.6)
ax.text(W + 1.25, H / 2 + 0.26, r"$\varepsilon_{xx}$", color=BK, fontsize=13, ha="center")
ox, oy = W / 2 - 0.35, H / 2
ax.plot([ox - 0.40, ox + 0.10], [oy, oy], color=BK, lw=0.9, ls=(0, (3, 3)))
ax.plot([ox, ox], [oy - 0.35, oy + 0.10], color=BK, lw=0.9, ls=(0, (3, 3)))
arrow(ax, ox, oy, 0.0, 0.60, hw=0.08, hl=0.12); ax.text(ox + 0.10, oy + 0.66, "y", color=BK, fontsize=11, style="italic")
arrow(ax, ox, oy, 0.60, 0.0, hw=0.08, hl=0.12); ax.text(ox + 0.42, oy + 0.12, "x", color=BK, fontsize=11, style="italic")
circled(ax, 0.22, -0.42, "a")
ax.set_xlim(-2.1, 6.2); ax.set_ylim(-0.9, 3.4)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p88-figure2a.png")

# ---------------------------------------- Fig. 2.b (page 89)
fig, ax = plt.subplots(figsize=(5.4, 3.4))
W, H = 3.4, 2.1
ax.add_patch(Rectangle((0, 0), W, H, fill=False, edgecolor=BK, linewidth=1.5))
arrow(ax, 0.75, H + 0.12, 0.0, 0.72, hw=0.13, hl=0.20, lw=1.6)
ax.text(0.52, H + 0.98, "60 kPa", color=BK, fontsize=12, ha="right")
arrow(ax, 1.75, H + 0.72, 0.85, 0.0, hw=0.13, hl=0.20, lw=1.6)
ax.text(2.18, H + 0.95, "25 kPa", color=BK, fontsize=12, ha="center")
arrow(ax, W + 0.14, H - 0.75, 0.0, 0.72, hw=0.13, hl=0.20, lw=1.6)
ax.text(W + 0.34, H + 0.12, "25 kPa", color=BK, fontsize=12, ha="left")
arrow(ax, W + 0.05, H / 2 - 0.25, 0.80, 0.0, hw=0.13, hl=0.20, lw=1.6)
ax.text(W + 0.95, H / 2 - 0.25, "45 kPa", color=BK, fontsize=12, ha="left", va="center")
ox, oy = W / 2 - 0.30, H / 2 - 0.05
ax.plot([ox - 0.42, ox + 0.12], [oy, oy], color=BK, lw=0.9)
ax.plot([ox, ox], [oy - 0.38, oy + 0.12], color=BK, lw=0.9)
arrow(ax, ox, oy, 0.0, 0.58, hw=0.08, hl=0.12); ax.text(ox + 0.10, oy + 0.62, "z", color=BK, fontsize=11, style="italic")
arrow(ax, ox, oy, 0.62, 0.0, hw=0.08, hl=0.12); ax.text(ox + 0.40, oy + 0.14, "x", color=BK, fontsize=11, style="italic")
circled(ax, -0.30, 0.18, "b")
ax.set_xlim(-0.9, 6.2); ax.set_ylim(-0.6, 3.9)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p89-figure2b.png")

# ---------------------------------------- logo KGB (page 91)
fig, ax = plt.subplots(figsize=(4.0, 4.6))
ax.add_patch(Arc((0, 0), 6.4, 6.4, theta1=-250, theta2=55, lw=9, color=BK))
ax.add_patch(Arc((0, 0), 6.4, 6.4, theta1=125, theta2=180, lw=9, color=BK))
# écusson
sh = [(-0.95, 1.30), (0.95, 1.30), (0.95, 2.40), (0.0, 2.72), (-0.95, 2.40)]
ax.add_patch(Polygon(sh, closed=True, facecolor=BK, edgecolor=BK))
ax.plot([-0.62, 0.0, 0.62], [2.22, 2.40, 2.22], color="white", lw=2.2)
ax.text(0, 1.78, "KGB", color="white", fontsize=15, weight="bold",
        ha="center", va="center", family="DejaVu Sans")
ax.text(0, -0.55, "KGB", color=BK, fontsize=66, weight="bold",
        ha="center", va="center", family="DejaVu Sans")
ax.set_xlim(-4.0, 4.0); ax.set_ylim(-4.2, 3.4)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-p91-kgb.png")
print("figures p87 (x2), p88, p89, p91 écrites")
