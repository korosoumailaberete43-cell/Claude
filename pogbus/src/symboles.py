"""Trois pistes de symbole pour POGBUS GROUP, construites sur la grille de 12 x 12 modules."""
from grille import poly, rect, svg, U

OR = "#D4A02C"
NOIR = "#0A0A0A"


# ---------------------------------------------------------------- piste A
def piste_a(c=NOIR, accent=None):
    """« Le Pilier et la Pointe » : fût en 5 segments + panse en pointe de flèche."""
    a = accent or c
    g = []
    # fût : 5 segments (les 5 activites) separes par des interstices
    h, n, jeu = 12.0, 5, 0.26
    seg = (h - (n - 1) * jeu) / n
    for i in range(n):
        y = i * (seg + jeu)
        g.append(rect(1.0, y, 2.0, seg, fill=c))
    # panse : triangle creux pointant vers le haut-droite
    ext = [(3.0, 0.0), (10.6, 3.4), (3.0, 6.8)]
    inn = [(3.0, 2.0), (6.3, 3.4), (3.0, 4.8)]
    d = ("M" + "L".join(f"{x * U:.2f} {y * U:.2f}" for x, y in ext) + "Z"
         "M" + "L".join(f"{x * U:.2f} {y * U:.2f}" for x, y in inn) + "Z")
    g.append(f'<path d="{d}" fill="{a}" fill-rule="evenodd"/>')
    return "".join(g)


# ---------------------------------------------------------------- piste B
def piste_b(c=NOIR, accent=None):
    """« L'Escalier » : un P plein dont le contrepoinçon est un escalier qui monte."""
    a = accent or c
    g = [rect(1.0, 0.0, 2.0, 12.0, fill=c)]           # fût
    # panse pleine : rectangle a angle sup-droit coupe en biais
    ext = [(3.0, 0.0), (9.4, 0.0), (11.0, 1.6), (11.0, 5.2), (9.4, 6.8), (3.0, 6.8)]
    # contrepoinçon : escalier a 3 marches qui monte vers la droite
    inn = [(5.0, 2.0), (6.4, 2.0), (6.4, 3.3), (7.8, 3.3), (7.8, 4.8), (5.0, 4.8)]
    pts = lambda p: "M" + "L".join(f"{x * U:.2f} {y * U:.2f}" for x, y in p) + "Z"
    g.append(f'<path d="{pts(ext)}{pts(inn)}" fill="{a}" fill-rule="evenodd"/>')
    return "".join(g)


# ---------------------------------------------------------------- piste C
def piste_c(c=NOIR, accent=None):
    """« Le Sceau » : losange a bordure de triangles bogolan, P en reserve."""
    a = accent or c
    g = [poly([(6, 0), (12, 6), (6, 12), (0, 6)], fill=c)]
    # triangles bogolan sur les quatre bords
    for i in range(4):
        rot = f'rotate({i * 90} {6 * U} {6 * U})'
        tr = []
        for k in range(3):
            x0 = 2.2 + k * 1.3
            tr.append(poly([(x0, 3.8 - 0.0), (x0 + 0.95, 3.8), (x0 + 0.47, 2.95)], fill=a))
        g.append(f'<g transform="{rot}">{"".join(tr)}</g>')
    # P en reserve au centre
    g.append(rect(4.4, 4.2, 0.95, 4.4, fill="#FFFFFF"))
    g.append(poly([(5.35, 4.2), (7.9, 4.2), (7.9, 6.6), (5.35, 6.6)], fill="#FFFFFF"))
    g.append(poly([(6.3, 4.95), (7.15, 4.95), (7.15, 5.85), (6.3, 5.85)], fill=c))
    return "".join(g)


PISTES = {"A": piste_a, "B": piste_b, "C": piste_c}
