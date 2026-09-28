# Exemple complet : CivRebar AI

Code réel ayant produit l'identité CivRebar AI (logiciel de ferraillage pour AutoCAD) :
logo « R façonné », charte de 14 pages, pack de 7 dossiers, modèles PowerPoint et Word.
Validé par l'utilisateur. À **adapter**, pas à copier : la palette, le symbole et tous les
textes sont propres à ce projet.

| Fichier | Rôle |
|---|---|
| `brand.py` | palette, couleurs texte, contraste, symbole SVG (normal et petites tailles), @font-face |
| `lockup.py` | logotypes horizontal/vertical avec texte converti en tracés |
| `shell.py` | gabarit de page A4 paysage (folio, sur-titre, styles) |
| `pages_a.py`, `pages_b.py` | les 14 pages de la charte (dont `p_bento` et `p_supports`) |
| `build.py` | rend les pages en PDF + aperçus PNG (vérification) |
| `supports.py` | visuels réseaux sociaux et écran de démarrage |
| `pptx_assets.py`, `deck.js` | fonds/logos PNG puis modèle PowerPoint (pptxgenjs) |
| `word.js` | papier à en-tête et note de calcul (docx-js) |
| `export.py` | pack 01 → 07 et fusion de la charte |
| `check_pptx.py`, `preview_pptx.py` | versions d'origine de `scripts/verifier_pptx.py` et `scripts/apercu_pptx.py` |
| `make_all.sh` | enchaîne tout |

Arborescence attendue : `src/` (ces fichiers), `fonts/` (woff2 copiés depuis @fontsource),
`mockups/images/0N_*.jpg`, `out/`, `LISEZ-MOI.txt`.
