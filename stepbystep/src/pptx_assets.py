"""Fonds et logos PNG pour les modèles PowerPoint et Word."""
import cairosvg
from brand import *
from pages_a import marches_motif

OUT = ROOT / "out" / "office_assets"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 2667, 1500


def png(svg, name, w=None):
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / name), output_width=w)


def fond(bg, motif=None):
    m = ""
    if motif:
        x, y, w, h, gap, col = motif
        m = f'<g transform="translate({x} {y})">{marches_motif(0, 0, w, h, gap, col)}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="{bg}"/>{m}</svg>'


png(fond(NOIR, (0, 830, 1200, 96, 32, OR)), "bg_couverture.png")
png(fond(NOIR, (1767, 760, 900, 80, 26, "#2E2B24")), "bg_section.png")
png(fond(IVOIRE), "bg_contenu.png")
png(principal("sombre"), "logo_principal_sombre.png", 1200)
png(principal("clair"), "logo_principal_clair.png", 1200)
png(horizontal("sombre"), "logo_horizontal_sombre.png", 1800)
png(horizontal("clair"), "logo_horizontal_clair.png", 1800)
png(compact("clair"), "marches.png", 800)
print("ok")

# panneau gauche de l'attestation (A4 paysage : 250 × 595 pt), rendu ×4
from pages_a import marches_motif as _mm
lg = principal("clair")
x, y, w, h = VB_PRINCIPAL
panel = (f'<svg xmlns="http://www.w3.org/2000/svg" width="250" height="595" viewBox="0 0 250 595">'
         f'<rect width="250" height="595" fill="#FFFFFF"/>'
         f'<svg x="40" y="44" width="170" height="{170 * h / w:.1f}" viewBox="{x} {y} {w} {h}">{inner(lg)}</svg>'
         f'<g transform="translate(0 405)">{_mm(0, 0, 250, 22, 8)}</g></svg>')
png(panel, "attestation_panneau.png", 1000)
