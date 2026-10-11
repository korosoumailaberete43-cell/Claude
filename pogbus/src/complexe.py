"""Quatre pistes d'emblème riche pour POGBUS GROUP.

RÈGLE : toute la géométrie est exprimée en MODULES. La fonction d() convertit
en unités SVG. Seuls les attributs bruts (line, rect, translate) multiplient par U.
La complexité y est toujours réglée — symétrie, grille, répétition.
"""
import math
import alphabet as A
from alphabet import oct_rect, d, TOUS
import monogramme as M
from grille import U

OR, NOIR, BLANC = "#BE8A22", "#111111", "#FFFFFF"
CUT = 1 / (2 + math.sqrt(2))      # coupe d'un octogone régulier
_id = [0]


def octogone(cx, cy, r):
    return oct_rect(cx - r, cy - r, cx + r, cy + r, 2 * r * CUT, TOUS)


def anneau(cx, cy, r, ep, couleur):
    return (f'<path d="{d(octogone(cx, cy, r))}{d(octogone(cx, cy, r - ep))}" '
            f'fill="{couleur}" fill-rule="evenodd"/>')


def frise(cx, cy, r, n_par_cote, taille, couleur, decale=0.0):
    """Triangles bogolan le long des huit côtés d'un octogone, pointe vers l'intérieur."""
    v = octogone(cx, cy, r)
    out = []
    for i in range(len(v)):
        ax, ay = v[i]
        bx, by = v[(i + 1) % len(v)]
        lx, ly = bx - ax, by - ay
        lg = math.hypot(lx, ly)
        ux, uy = lx / lg, ly / lg
        nx, ny = uy, -ux                       # normale vers le centre
        if (ax + ux * lg / 2 + nx - cx) ** 2 + (ay + uy * lg / 2 + ny - cy) ** 2 > \
           (ax + ux * lg / 2 - cx) ** 2 + (ay + uy * lg / 2 - cy) ** 2:
            nx, ny = -nx, -ny
        pas = lg / n_par_cote
        for k in range(n_par_cote):
            t = (k + 0.5) * pas
            mx, my = ax + ux * t + nx * decale, ay + uy * t + ny * decale
            out.append(d([(mx - ux * taille / 2, my - uy * taille / 2),
                          (mx + ux * taille / 2, my + uy * taille / 2),
                          (mx + nx * taille * 0.80, my + ny * taille * 0.80)]))
    return f'<path d="{"".join(out)}" fill="{couleur}"/>'


def mono(cx, cy, largeur, c_p, c_g, **kw):
    """Monogramme PG centré sur (cx, cy), de « largeur » modules."""
    g, w, h = M.monogramme(16, 16, c_p=c_p, c_g=c_g, **kw)
    k = largeur / w
    return (f'<g transform="translate({(cx - largeur/2)*U:.3f} {(cy - h*k/2)*U:.3f}) '
            f'scale({k:.5f})">{g}</g>')


# ------------------------------------------------------------------ piste 1
def sceau(c_fond=NOIR, c_trait=OR, c_p=OR, c_g=BLANC, cote=44.0):
    """« Le Sceau » : médaillon octogonal, double filet, frise bogolan, monogramme."""
    c = r = cote / 2
    g = [f'<path d="{d(octogone(c, c, r))}" fill="{c_fond}"/>',
         anneau(c, c, r * 0.985, r * 0.035, c_trait),
         frise(c, c, r * 0.90, 3, r * 0.135, c_trait, decale=r * 0.02),
         anneau(c, c, r * 0.665, r * 0.030, c_trait),
         mono(c, c, r * 1.00, c_p, c_g)]
    return "".join(g), cote, cote


# ------------------------------------------------------------------ piste 2
def rosace(c_fond=NOIR, c_rayon=OR, c_p=OR, c_g=BLANC, cote=44.0):
    """« La Rosace » : étoile à seize branches, monogramme au cœur."""
    c = r = cote / 2
    g = [f'<path d="{d(octogone(c, c, r))}" fill="{c_fond}"/>']
    longues, courtes = [], []
    for i in range(8):
        for a_deg, pointe, demi, cible in ((i * 45, r * 0.93, r * 0.072, longues),
                                           (i * 45 + 22.5, r * 0.80, r * 0.052, courtes)):
            a = math.radians(a_deg)
            ca, sa = math.cos(a), math.sin(a)
            px, py = -sa, ca
            base = r * 0.60
            cible.append(d([(c + ca * pointe, c + sa * pointe),
                            (c + ca * base + px * demi, c + sa * base + py * demi),
                            (c + ca * base - px * demi, c + sa * base - py * demi)]))
    g.append(f'<path d="{"".join(longues)}{"".join(courtes)}" fill="{c_rayon}"/>')
    g.append(anneau(c, c, r * 0.575, r * 0.030, c_rayon))
    g.append(mono(c, c, r * 0.80, c_p, c_g))
    return "".join(g), cote, cote


# ------------------------------------------------------------------ piste 3
def ecu(c_fond=NOIR, c_chef=OR, c_p=OR, c_g=BLANC, larg=38.0, haut=44.0):
    """« L'Écu » : blason à coins coupés, chef bogolan, monogramme en cœur."""
    W, H, c = larg, haut, larg * 0.16
    corps = [(c, 0), (W - c, 0), (W, c), (W, H * 0.60), (W / 2, H), (0, H * 0.60), (0, c)]
    hc = H * 0.225
    chef = [(c, 0), (W - c, 0), (W, c), (W, hc), (0, hc), (0, c)]
    n = 7
    t = W / n
    tri = [d([(i * t, hc), ((i + 1) * t, hc), (i * t + t / 2, hc + t * 0.58)]) for i in range(n)]
    g = [f'<path d="{d(corps)}" fill="{c_fond}"/>',
         f'<path d="{d(chef)}" fill="{c_chef}"/>',
         f'<path d="{"".join(tri)}" fill="{c_chef}"/>',
         mono(W / 2, H * 0.585, W * 0.60, c_p, c_g)]
    return "".join(g), larg, haut


# ------------------------------------------------------------------ piste 4
def colonne(c_fond=NOIR, c_trait=OR, c_p=OR, c_g=BLANC, larg=34.0, haut=46.0):
    """« La Colonne » : socle à degrés, fût, monogramme au sommet. Bâtir et monter."""
    W, H = larg, haut
    g = [f'<path d="{d(octogone(W / 2, H * 0.345, W * 0.455))}" fill="{c_fond}"/>',
         anneau(W / 2, H * 0.345, W * 0.445, W * 0.030, c_trait),
         mono(W / 2, H * 0.345, W * 0.56, c_p, c_g)]
    # socle : trois degrés qui s'élargissent vers le bas
    y = H * 0.775
    for i, (lf, ep) in enumerate(((0.44, 0.052), (0.62, 0.052), (0.86, 0.062))):
        g.append(f'<path d="{d(oct_rect(W/2 - W*lf/2, y, W/2 + W*lf/2, y + H*ep, H*ep*0.62, A.DROITE))}" '
                 f'fill="{c_trait if i == 2 else c_fond}"/>')
        y += H * ep + H * 0.022
    return "".join(g), larg, haut


PISTES = {
    "1 — LE SCEAU  (medaillon, frise bogolan)": sceau,
    "2 — LA ROSACE  (etoile a seize branches)": rosace,
    "3 — L'ECU  (blason, chef bogolan)": ecu,
    "4 — LA COLONNE  (socle a degres)": colonne,
}


def frise_alternee(cx, cy, r_ext, r_int, n_par_cote, couleur):
    """Bande de triangles alternés pointe-dedans / pointe-dehors : le vrai rythme du bogolan."""
    ve, vi = octogone(cx, cy, r_ext), octogone(cx, cy, r_int)
    out = []
    for i in range(len(ve)):
        ae, be = ve[i], ve[(i + 1) % len(ve)]
        ai, bi = vi[i], vi[(i + 1) % len(vi)]
        for k in range(n_par_cote):
            t0, t1 = k / n_par_cote, (k + 1) / n_par_cote
            tm = (t0 + t1) / 2
            pe = lambda t: (ae[0] + (be[0] - ae[0]) * t, ae[1] + (be[1] - ae[1]) * t)
            pi = lambda t: (ai[0] + (bi[0] - ai[0]) * t, ai[1] + (bi[1] - ai[1]) * t)
            if k % 2 == 0:
                out.append(d([pe(t0), pe(t1), pi(tm)]))      # pointe vers le centre
            else:
                out.append(d([pi(t0), pi(t1), pe(tm)]))      # pointe vers l'extérieur
    return f'<path d="{"".join(out)}" fill="{couleur}"/>'


def sceau2(c_fond=NOIR, c_trait=OR, c_p=OR, c_g=BLANC, cote=44.0,
           frise_type="alternee", n=3, petite_taille=False):
    """« Le Sceau », version travaillée. petite_taille retire la frise."""
    c = r = cote / 2
    g = [f'<path d="{d(octogone(c, c, r))}" fill="{c_fond}"/>']
    if petite_taille:
        g.append(anneau(c, c, r * 0.97, r * 0.075, c_trait))
        g.append(mono(c, c, r * 1.10, c_p, c_g))
        return "".join(g), cote, cote
    g.append(anneau(c, c, r * 0.985, r * 0.032, c_trait))
    if frise_type == "alternee":
        g.append(frise_alternee(c, c, r * 0.935, r * 0.775, n, c_trait))
    elif frise_type == "simple":
        g.append(frise(c, c, r * 0.90, n, r * 0.135, c_trait, decale=r * 0.02))
    else:
        g.append(frise(c, c, r * 0.90, n + 1, r * 0.105, c_trait, decale=r * 0.03))
    g.append(anneau(c, c, r * 0.735, r * 0.030, c_trait))
    g.append(mono(c, c, r * 1.02, c_p, c_g))
    return "".join(g), cote, cote


def ecu2(c_fond=NOIR, c_chef=OR, c_p=OR, c_g=BLANC, larg=36.0, haut=46.0):
    """« L'Écu », version travaillée : chef plus mince, frise rentrée, pointe allongée."""
    W, H, c = larg, haut, larg * 0.185
    corps = [(c, 0), (W - c, 0), (W, c), (W, H * 0.55), (W / 2, H), (0, H * 0.55), (0, c)]
    hc = H * 0.175
    chef = [(c, 0), (W - c, 0), (W, c), (W, hc), (0, hc), (0, c)]
    n = 9
    t = W / n
    tri = [d([(i * t, hc), ((i + 1) * t, hc), (i * t + t / 2, hc + t * 0.72)]) for i in range(n)]
    filet = d(oct_rect(0, hc + t * 0.85, W, hc + t * 0.85 + H * 0.013, 0, A.AUCUN))
    g = [f'<path d="{d(corps)}" fill="{c_fond}"/>',
         f'<path d="{d(chef)}" fill="{c_chef}"/>',
         f'<path d="{"".join(tri)}" fill="{c_chef}"/>',
         f'<path d="{filet}" fill="{c_chef}"/>',
         mono(W / 2, H * 0.615, W * 0.60, c_p, c_g)]
    return "".join(g), larg, haut


def texte_circulaire(cx, cy, rayon, texte, cap, couleur, angle_centre=0.0, appro=0.9):
    """Texte disposé en arc, lettres suspendues depuis le rayon donné.

    angle_centre en degrés, 0 = sommet du sceau. Les lettres pendent vers le centre.
    """
    from alphabet import LETTRES, H as HC
    k = cap / HC
    larg = []
    for ch in texte:
        _, w = LETTRES[ch](2.05, 1.60)
        larg.append(w * k)
    arc = sum(larg) + appro * k * (len(texte) - 1)
    span = math.degrees(arc / rayon)
    a = angle_centre - span / 2
    out = []
    for ch, w in zip(texte, larg):
        da = math.degrees(w / rayon)
        chem, _ = LETTRES[ch](2.05, 1.60)
        corps = "".join(f'<path d="{dd}" fill="{couleur}" fill-rule="{r}"/>' for dd, r in chem)
        out.append(f'<g transform="translate({cx*U:.3f} {cy*U:.3f}) rotate({a + da/2:.4f}) '
                   f'translate(0 {-rayon*U:.3f}) translate({-w*U/2:.3f} 0) scale({k:.5f})">{corps}</g>')
        a += da + math.degrees(appro * k / rayon)
    return "".join(out)


def sceau_devise(c_fond=NOIR, c_trait=OR, c_p=OR, c_g=BLANC, cote=50.0,
                 devise="L'AUDACIEUX", petite_taille=False):
    """« Le Sceau à devise » : médaillon, nom de guerre en arc, frise en pied."""
    c = r = cote / 2
    g = [f'<path d="{d(octogone(c, c, r))}" fill="{c_fond}"/>']
    if petite_taille:
        g.append(anneau(c, c, r * 0.97, r * 0.070, c_trait))
        g.append(mono(c, c, r * 1.08, c_p, c_g))
        return "".join(g), cote, cote
    g.append(anneau(c, c, r * 0.985, r * 0.028, c_trait))
    g.append(anneau(c, c, r * 0.660, r * 0.026, c_trait))
    # devise en arc, suspendue depuis le filet extérieur
    g.append(texte_circulaire(c, c, r * 0.945, devise, r * 0.190, c_trait, angle_centre=0))
    # frise en pied, entre les deux filets
    v_ext, v_int = octogone(c, c, r * 0.930), octogone(c, c, r * 0.775)
    out = []
    for i in (3, 4, 5):                    # les trois côtés du bas : la frise reste symétrique
        ae, be, ai, bi = v_ext[i], v_ext[(i + 1) % 8], v_int[i], v_int[(i + 1) % 8]
        for kk in range(5):
            t0, t1, tm = kk / 5, (kk + 1) / 5, (kk + 0.5) / 5
            pe = lambda t: (ae[0] + (be[0] - ae[0]) * t, ae[1] + (be[1] - ae[1]) * t)
            pi = lambda t: (ai[0] + (bi[0] - ai[0]) * t, ai[1] + (bi[1] - ai[1]) * t)
            out.append(d([pe(t0), pe(t1), pi(tm)]) if kk % 2 == 0 else d([pi(t0), pi(t1), pe(tm)]))
    g.append(f'<path d="{"".join(out)}" fill="{c_trait}"/>')
    # losanges de séparation à gauche et à droite
    for a_deg in (90, 270):
        a = math.radians(a_deg - 90)
        px, py = c + math.cos(a) * r * 0.815, c + math.sin(a) * r * 0.815
        t = r * 0.055
        g.append(f'<path d="{d([(px, py - t), (px + t, py), (px, py + t), (px - t, py)])}" fill="{c_trait}"/>')
    g.append(mono(c, c, r * 0.90, c_p, c_g))
    return "".join(g), cote, cote
