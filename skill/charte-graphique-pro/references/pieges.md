# Pièges techniques rencontrés (et solutions)

| Symptôme | Cause | Solution |
|---|---|---|
| Contenu manquant en bas de page | hauteur fixe + `overflow:hidden` | prévisualiser chaque page en PNG |
| Page entièrement blanche | `grid-template-areas` avec guillemets doubles dans `style="…"` | apostrophes : `'a a b' 'c c b'` |
| La serif ne s'affiche pas (police générique à la place) | famille nommée `Serif` (ou `Monospace`…) : mot-clé CSS générique | noms uniques : `InstrumentSerif`, `Mono` |
| Google Fonts / GitHub renvoient 403 | réseau filtré | `npm i @fontsource/<police>` puis copier `files/*-latin-<graisse>-normal.woff2` |
| `.woff2` inutilisable par Office ou LibreOffice | format web | fontTools : `t=TTFont(f); t.flavor=None; t.save('x.ttf')` puis `fc-cache -f` |
| Famille installée avec un nom inattendu (« Manrope ExtraLight ») | fichiers fontsource issus d'une police variable | contrôler `fc-list`; l'aperçu peut basculer sur une police de repli |
| `rsvg-convert` / `pdftops` / `gs` absents | environnement minimal | `pip install cairosvg` : `svg2pdf`, `svg2eps` (BoundingBox correcte), `svg2png` |
| EPS tronqué à l'ouverture | `rsvg-convert -f eps` | `cairosvg.svg2eps`, ou `rsvg-convert -f pdf` puis `pdftops -eps` |
| `import fitz` échoue | PyMuPDF non installé | `pip install pymupdf` (`import pymupdf`) |
| LibreOffice : « source file could not be loaded » même sur un .txt | modules Writer/Impress absents | `scripts/verifier_pptx.py` + `scripts/apercu_pptx.py` ; dire que Word n'a pas été vu |
| favicon.ico flou | Pillow a mis à l'échelle depuis l'image 16 px | base = image 48 px, `append_images=[16, 32]` |
| Symbole illisible à 16 px (détails qui disparaissent) | même dessin à toutes les tailles | version « petites tailles » : trait ×1,4, détails fusionnés, accent agrandi |
| Petits textes d'accent peu lisibles sur fond clair | couleur vive < 4,5:1 | `scripts/contraste.py` ; variante « texte » plus foncée |
| `SyntaxError` dans un f-string contenant « l'armature » | apostrophe dans un f-string à apostrophes | `&#8217;` ou chaîne entre guillemets doubles |
| Logo texte différent selon la machine | texte SVG dépendant des polices installées | `scripts/texte_en_traces.py` : texte converti en tracés |
| Pack trop lourd | images embarquées à 4× | ~300 DPI de la taille affichée, JPEG 86-88 |
| Suppression refusée (`rm -f $DOSSIER/*`) | garde-fou contre une variable vide | `rm -f "${DOSSIER:?}"/*` ou chemin littéral |
| L'outil Bash ne répond plus (« no safety verdict ») | incident passager côté serveur | continuer avec Write/Edit/Read, relancer plus tard ; ne pas insister en boucle |
