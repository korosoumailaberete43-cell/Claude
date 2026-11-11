"""Rapport de contraste WCAG 2.1 entre couleurs.

    python3 contraste.py "#C8773F" "#F3F0EA"          → 3,0:1  titres et graphisme seulement
    python3 contraste.py --palette "#0B1624,#C8773F,#35D0DE" --fonds "#FFFFFF,#F3F0EA"

Seuils : 4,5:1 pour le texte courant (AA), 3:1 pour les grands titres (≥ 24 px) et les
éléments graphiques. Une couleur de marque vive échoue souvent sur fond clair : créer alors
une variante « texte » plus foncée (même teinte) et la réserver aux petits textes.
Sur fond sombre, la variante est au contraire éclaircie.
"""
import sys

SEUIL_TEXTE = 4.5
USAGE = ('usage : contraste.py "#RRGGBB" "#RRGGBB"\n'
         '        contraste.py --palette "#c1,#c2,…" [--fonds "#f1,#f2"]')


def rgb(h):
    """'#C8773F' ou 'C8F' → [200, 119, 63]. Lève une erreur claire si la forme est fausse."""
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6 or any(c not in "0123456789abcdefABCDEF" for c in h):
        raise ValueError(f"couleur invalide : {h!r} (attendu #RRGGBB)")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def luminance(h):
    c = [v / 255 for v in rgb(h)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contraste(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    # comparer le ratio exact : arrondi avant seuil, 4,46 deviendrait « 4,5 ✓ » à tort
    if r >= SEUIL_TEXTE:
        return "texte courant ✓"
    if r >= 3:
        return "titres et graphisme seulement"
    return "à éviter pour du texte"


def fonce_jusqua(hexa, fond, cible=SEUIL_TEXTE):
    """Variante « texte » : même teinte, assombrie sur fond clair, éclaircie sur fond sombre,
    jusqu'à atteindre le contraste cible. Renvoie None si aucune variante n'y arrive."""
    cible_rgb = (0, 0, 0) if luminance(fond) > 0.18 else (255, 255, 255)
    base = rgb(hexa)
    for pas in range(101):
        t = pas / 100
        c = [round(v + (w - v) * t) for v, w in zip(base, cible_rgb)]
        hx = "#%02X%02X%02X" % tuple(c)
        if contraste(hx, fond) >= cible:
            return hx
    return None


def ratio_fr(r):
    return f"{r:.1f}".replace(".", ",") + ":1"


def main(args):
    if args and args[0] == "--palette":
        if len(args) < 2:
            print(USAGE, file=sys.stderr)
            return 2
        pal = args[1].split(",")
        fonds = args[args.index("--fonds") + 1].split(",") if "--fonds" in args else ["#FFFFFF"]
        for f in fonds:
            print(f"Sur {f} :")
            for c in pal:
                r = contraste(c, f)
                extra = ""
                if r < SEUIL_TEXTE:
                    variante = fonce_jusqua(c, f)
                    extra = (f"   → variante texte proposée : {variante}" if variante
                             else "   → aucune variante n'atteint 4,5:1 sur ce fond")
                print(f"  {c}  {ratio_fr(r)}  {verdict(r)}{extra}")
        return 0
    if len(args) != 2:
        print(USAGE, file=sys.stderr)
        return 2
    r = contraste(args[0], args[1])
    print(f"{ratio_fr(r)}  {verdict(r)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
