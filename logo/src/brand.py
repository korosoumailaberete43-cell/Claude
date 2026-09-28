"""CivRebar AI — constantes de marque, symbole et gabarit de page."""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"

# ---------------------------------------------------------------- Palette
NUIT = "#0B1624"      # Nuit d'acier — fond principal, texte
ACIER = "#1C2B3D"     # Acier trempé — surfaces sombres secondaires
CUIVRE = "#C8773F"    # Cuivre de forge — couleur signature (l'armature)
CUIVRE_CLAIR = "#E3A56C"
SIGNAL = "#35D0DE"    # Signal IA — l'intelligence, à doser
BETON = "#B9BEC4"     # Béton coulé — neutres, traits techniques
CHAUX = "#F3F0EA"     # Blanc chaux — fond clair
BLANC = "#FFFFFF"

# ---------------------------------------------------------------- Symbole
# Couleurs de texte accessibles sur fond clair (contraste ≥ 4,5:1, WCAG AA)
CUIVRE_TEXTE = "#9A5526"
SIGNAL_TEXTE = "#0B7480"

def contrast(a, b):
    """Rapport de contraste WCAG 2.1 entre deux couleurs hex."""
    def lum(h):
        c = [int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


# Grille : module x = diamètre de la barre = 20 unités. Carré de construction 12x × 12x.
X = 20


def mark_small(bar=NUIT, relevee=CUIVRE, noeud=SIGNAL, bg=None, size=None, cls="", rx=48):
    """Version « petites tailles » (≤ 32 px) : trait épaissi à 1,4x, le crochet se referme
    sur le fût, le nœud Signal grossit (Ø 1,3x) et se place au cœur de la panse."""
    w = f' width="{size}" height="{size}"' if size else ""
    back = f'<rect x="5" y="10" width="240" height="240" rx="{rx}" fill="{bg}"/>' if bg else ""
    return f"""<svg class="{cls}" viewBox="5 10 240 240"{w} xmlns="http://www.w3.org/2000/svg">{back}
<g fill="none" stroke-width="28" stroke-linecap="butt" stroke-linejoin="round">
  <path d="M120 160 L180 220 H214" stroke="{relevee}"/>
  <path d="M50 234 V90 A50 50 0 0 1 100 40 H120 A60 60 0 0 1 120 160 H50" stroke="{bar}"/>
</g>
<circle cx="112" cy="100" r="13" fill="{noeud}"/>
</svg>"""


def mark(bar=NUIT, relevee=CUIVRE, noeud=SIGNAL, bg=None, size=None, cls=""):
    """Le « R façonné » : une barre longitudinale + étrier façonné (fût et panse),
    une barre relevée à 45° (jambe), le nœud Signal tenu dans le crochet (l'IA)."""
    w = f' width="{size}" height="{size}"' if size else ""
    back = f'<rect x="5" y="10" width="240" height="240" rx="48" fill="{bg}"/>' if bg else ""
    return f"""<svg class="{cls}" viewBox="5 10 240 240"{w} xmlns="http://www.w3.org/2000/svg">{back}
<g fill="none" stroke-width="20" stroke-linecap="butt" stroke-linejoin="round">
  <path d="M120 160 L180 220 H210" stroke="{relevee}"/>
  <path d="M50 230 V90 A50 50 0 0 1 100 40 H120 A60 60 0 0 1 120 160 H100 A20 20 0 0 1 85.86 125.86 L105.86 105.86" stroke="{bar}"/>
</g>
<circle cx="100" cy="140" r="7" fill="{noeud}"/>
</svg>"""


def font_css():
    specs = [
        ("Sora", "sora-latin-300-normal.woff2", 300, "normal"),
        ("Sora", "sora-latin-400-normal.woff2", 400, "normal"),
        ("Sora", "sora-latin-600-normal.woff2", 600, "normal"),
        ("Sora", "sora-latin-700-normal.woff2", 700, "normal"),
        ("Manrope", "manrope-latin-400-normal.woff2", 400, "normal"),
        ("Manrope", "manrope-latin-500-normal.woff2", 500, "normal"),
        ("Manrope", "manrope-latin-700-normal.woff2", 700, "normal"),
        ("InstrumentSerif", "instrument-serif-latin-400-normal.woff2", 400, "normal"),
        ("InstrumentSerif", "instrument-serif-latin-400-italic.woff2", 400, "italic"),
        ("Mono", "jetbrains-mono-latin-400-normal.woff2", 400, "normal"),
        ("Mono", "jetbrains-mono-latin-500-normal.woff2", 500, "normal"),
    ]
    out = []
    for fam, f, wt, st in specs:
        b = base64.b64encode((FONTS / f).read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b}) format('woff2');"
                   f"font-weight:{wt};font-style:{st}}}")
    return "\n".join(out)
