"""Verrouillage vertical : l'emblème PG au-dessus, POGBUS GROUP en dessous."""
import importlib
import monogramme as M; importlib.reload(M)
import final as F; importlib.reload(F)
from grille import U

OR, NOIR, BLANC = F.OR, F.NOIR, F.BLANC


def lockup(corps=NOIR, accent=OR, hauteur_embleme=26.0, ecart=5.4, **kw):
    """L'emblème est centré sur la largeur du mot. Hauteurs en modules du mot."""
    gm, wm, hm = M.monogramme(c_p=accent, c_g=corps, **kw)
    gw, ww, hw = F.logo(corps, accent)
    k = hauteur_embleme / hm
    wm_r = wm * k
    dx = (ww - wm_r) / 2
    g = (f'<g transform="translate({dx*U:.3f} 0) scale({k:.5f})">{gm}</g>'
         f'<g transform="translate(0 {(hauteur_embleme + ecart)*U:.3f})">{gw}</g>')
    return g, ww, hauteur_embleme + ecart + hw
