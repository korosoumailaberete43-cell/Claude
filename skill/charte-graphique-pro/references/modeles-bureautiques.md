# Supports numériques et modèles bureautiques

Livrer la marque « prête à l'emploi » : l'utilisateur doit pouvoir publier et présenter le
jour même. Ces livrables ont été demandés et validés sur CivRebar AI.

## Supports numériques (PNG aux dimensions exactes, rendus en HTML + Chromium)

| Fichier | Dimensions | Composition |
|---|---|---|
| Photo de profil | 1080 × 1080 | symbole seul, centré, sur fond sombre + trame |
| Bannière LinkedIn | 1584 × 396 | logo + signature décalés à droite (la photo de profil masque le bas-gauche), symbole en filigrane |
| Couverture Facebook | 1640 × 624 | logo + signature, zone sûre centrale |
| Post annonce | 1080 × 1350 | sur-titre mono, titre fort, 2 lignes d'explication, logo en bas |
| Post citation | 1080 × 1080 | citation en serif italique, logo en bas |
| Écran de démarrage (logiciel/plugin) | 1280 × 720 | logo, signature, barre de chargement en couleur d'accent, version |

Script type : un dictionnaire `nom → (largeur, hauteur, fonction_html)`, rendu en lot avec
`scripts/rendu_png.js` (viewport à la taille exacte, `deviceScaleFactor: 1`).
Les montrer ensuite dans la charte (page « Supports numériques ») en insérant les PNG réels.

## Modèle PowerPoint (pptxgenjs)

8 diapositives remplies avec le vrai contenu du projet (pas de lorem) : couverture, sommaire
en cartes, intercalaire de section (grand numéro), texte + zone image, chiffres clés,
feuille de route avec le motif de la marque, citation, fin/contact. Notes de présentateur pour
ce qui est à remplacer. Fonds et logos en PNG générés depuis les SVG de la marque.

- Utiliser les polices de la marque et **prévenir** qu'il faut les installer
  (Google Fonts, gratuites) : sans elles PowerPoint substitue et la mise en page bouge.
- Valider avec `validate.py` de la compétence pptx.
- Si LibreOffice est indisponible ou incomplet (erreur « source file could not be loaded »,
  même sur un .txt), vérifier avec `scripts/verifier_pptx.py` (débordements mesurés avec les
  vraies polices) et `scripts/apercu_pptx.py` (aperçu PNG). Dire à l'utilisateur que l'aperçu
  n'est pas le rendu PowerPoint exact.

## Modèles Word (docx-js)

- **Papier à en-tête** : logo dans l'en-tête sur un filet fin, pied de page en mono avec les
  coordonnées, exemple de lettre complet. Lieu : « Ville, le … » (ne pas deviner la ville).
- **Modèle métier** (ici une note de calcul) : page de garde (logo, sur-titre, titre, tableau
  d'identification : projet, élément, référence, indice, date, rédigé/vérifié par), puis titres
  Heading 1/2 stylés aux couleurs, tableaux d'exemple à en-tête sombre, puces en couleur d'accent.
  Page de garde sans en-tête (`titlePage: true`), numéros de page ensuite.
- Sans LibreOffice complet, on ne peut pas voir le rendu : vérifier structure et contenu
  (python-docx, validate.py) et **le dire clairement** à l'utilisateur.

## Coordonnées fictives

Tous les modèles contiennent « Prénom Nom », un e-mail et un téléphone d'exemple.
Les signaler en fin de livraison et proposer de les remplacer.
