"""Rapport de contraste WCAG 2.1 entre couleurs.

    python3 contraste.py "#C8773F" "#F3F0EA"          → 3,0:1  titres et graphisme seulement
    python3 contraste.py --palette "#0B1624,#C8773F,#35D0DE" --fonds "#FFFFFF,#F3F0EA"

Seuils : 4,5:1 pour le texte courant (AA), 3:1 pour les grands titres (≥ 24 px) et les
éléments graphiques. Une couleur de marque vive échoue souvent sur fond clair : créer alors
une variante « texte » plus foncée (même teinte) et la réserver aux petits textes.
"""
import sys


def luminance(h):
    c = [int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contraste(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    r = round(r, 1)
    if r >= 4.5:
        return "texte courant ✓"
    if r >= 3:
        return "titres et graphisme seulement"
    return "à éviter pour du texte"


def fonce_jusqua(hexa, fond, cible=4.5):
    """Assombrit une couleur (même teinte) jusqu'à atteindre le contraste cible sur le fond."""
    r, g, b = (int(hexa.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    k = 1.0
    while k > 0:
        c = "#%02X%02X%02X" % (round(r * k), round(g * k), round(b * k))
        if contraste(c, fond) >= cible:
            return c
        k -= 0.01
    return "#000000"


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--palette":
        pal = args[1].split(",")
        fonds = args[args.index("--fonds") + 1].split(",") if "--fonds" in args else ["#FFFFFF"]
        for f in fonds:
            print(f"Sur {f} :")
            for c in pal:
                r = contraste(c, f)
                extra = "" if r >= 4.5 else f"   → variante texte proposée : {fonce_jusqua(c, f)}"
                print(f"  {c}  {r:.1f}:1  {verdict(r)}{extra}".replace(".", ",", 1))
    else:
        r = contraste(args[0], args[1])
        print(f"{r:.1f}:1  {verdict(r)}".replace(".", ","))
