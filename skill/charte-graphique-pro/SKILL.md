---
name: "charte-graphique-pro"
description: "Créer un logo haut de gamme avec son histoire, une charte graphique complète (PDF paysage de 14 pages : manifeste, symbole décodé, construction cotée, couleurs avec contrastes vérifiés, typographie, déclinaisons, applications, grille bento de mises en situation), et le pack livrable (logos SVG/PDF/EPS/PNG/JPEG, favicons, supports réseaux sociaux, modèles PowerPoint et Word, prompts pour images photoréalistes). À utiliser dès qu'on parle de logo, identité visuelle, charte graphique, manuel de marque, branding, kit de marque, pack logo, concours de logo ou présentation à un jury — même si l'utilisateur dit seulement « fais-moi un logo pour mon projet »."
---

# Charte graphique et identité de marque, niveau agence

## Quand l'utiliser

Pour tout logo, identité visuelle, charte ou pack de marque à livrer à un client, un jury
ou pour un projet personnel ambitieux. Le niveau attendu est celui d'une agence : un concept
avec une histoire, une charte qui la raconte, et des fichiers prêts à l'emploi.

## Principe technique

Tout est fabriqué en code, donc modifiable et vectoriel :

```
brand.py (palette, symbole SVG, polices)  →  pages HTML  →  Chromium/Playwright  →  PDF par page  →  fusion pypdf
                                          →  logos SVG (texte en tracés)  →  cairosvg  →  SVG/PDF/EPS/PNG/JPEG
                                          →  supports PNG, PowerPoint (pptxgenjs), Word (docx-js)
```

Un exemple complet et fonctionnel (projet CivRebar AI) est dans `exemple-civrebar/` :
`make_all.sh` régénère toute l'identité d'une commande. S'en inspirer plutôt que de repartir
de zéro ; l'adapter (palette, symbole, textes), pas le copier tel quel.

## Déroulé

### 1. Comprendre le projet (avant tout dessin)

Nom exact, activité en 2-3 phrases, public, valeurs, cadre (concours ? cahier des charges ?
date ?), couleurs aimées ou interdites, idées de symbole, livrables attendus. Si l'utilisateur
décrit le projet sans tout préciser, choisir soi-même et le dire.

### 2. Trouver le concept et son histoire

Lire `references/concept-et-histoire.md`. En bref : partir d'un **geste ou objet du métier**
que les initiés reconnaissent, construire le symbole avec les règles de ce métier, loger
l'innovation dans **un seul** accent, puis décoder chaque élément (nom métier + sens de marque).
Écrire un manifeste et une signature d'une ligne.

Pour un projet ambitieux, présenter **un concept abouti** plutôt que trois pistes rapides :
des pistes plates et vite faites ont été refusées en bloc (« c'est un projet de grande
envergure, je veux quelque chose de très sophistiqué, qui a une histoire »).

### 3. Dessiner et verrouiller le logo

- Symbole en SVG sur une grille : module `x` = épaisseur du trait ; toutes les cotes en `x`.
  Itérer en rendant symbole grand, sur fond sombre, et à 64/32/16 px ; regarder chaque rendu.
- Logotype : essayer 2-3 compositions et garder la plus institutionnelle ; convertir le texte
  en tracés avec `scripts/texte_en_traces.py` (le logo ne dépend plus des polices).
- Version horizontale (principale), verticale, symbole seul.
- **Version « petites tailles »** pour ≤ 32 px (trait épaissi, détails fusionnés, accent
  agrandi) : elle sert aux favicons et aux icônes d'interface.
- Couleurs : 1 dominante sombre, 1 signature, 1 accent rare, 2-3 neutres. Passer la palette
  dans `scripts/contraste.py` ; créer des variantes « texte » pour toute couleur < 4,5:1 sur
  fond clair et les utiliser pour les petits textes (sur-titres, légendes, liens).

### 4. Écrire la charte

Suivre `references/structure-charte.md` (14 pages dans un ordre éprouvé). Gabarit commun en
Python : constantes de couleur, `@font-face` en base64 (PDF autonome), CSS de base,
`page_shell(inner, n, titre, theme)`. Format **A4 paysage 297 × 210 mm**. Une fonction par
page, 2-3 pages par fichier. Rendu : `node scripts/rendu_pdf.js page_*.html`.

**Règle non négociable : après chaque modification, rendre la page en PNG et la regarder.**
Les pages ont une hauteur fixe ; ce qui dépasse est rogné sans erreur ni avertissement.

```python
import pymupdf
d = pymupdf.open('out/page_05.pdf')
d[0].get_pixmap(matrix=pymupdf.Matrix(1.6, 1.6)).save('out/page_05.png')
```

### 5. Proposer la grille bento de mises en situation

Sans attendre qu'on la demande : lire `references/mises-en-situation.md`. Livrer 6 prompts
prêts à coller (ChatGPT ou autre), avec le fichier logo à joindre et le format de chaque image ;
prévoir la page bento avec des cases « à venir » ; à réception, identifier les images,
vérifier la fidélité du logo image par image, recadrer avec `object-position`, intégrer.

### 6. Produire les supports et modèles

Lire `references/modeles-bureautiques.md` : photo de profil, bannières, posts, écran de
démarrage ; modèle PowerPoint rempli avec le vrai contenu ; papier à en-tête et modèle de
document métier en Word. Les montrer dans la charte (page « Supports numériques »).

### 7. Assembler le pack

```
01_Logo_principal_avec_nom/     horizontal + vertical : couleur, noir, blanc, couleur pour fond sombre
02_Symbole_seul/                couleur, noir, blanc, petites tailles, icône d'application, favicons/
03_Versions_sur_fond_couleur/   logo et symbole sur chaque couleur de la palette (fond intégré)
04_Documents/                   charte PDF, prompts des mises en situation
05_Supports_numeriques/         réseaux sociaux, écran de démarrage
06_Modeles_bureautiques/        .pptx, .docx
07_Mises_en_situation/          photos générées
LISEZ-MOI.txt                   contenu, HEX/RVB/CMJN, couleurs texte, polices + lien de téléchargement, règles
```

Chaque logo en **SVG + PDF + EPS + PNG + JPEG** avec `scripts/exporter_logo.py` (marge de
protection incluse ; JPEG des versions blanches sur fond sombre de la palette ; EPS via
cairosvg, BoundingBox vérifiée). Favicons : fonction `favicons()` du même script.

Zipper le pack et viser **moins de 10 Mo** (limite courante des pièces jointes) : images à
~300 DPI de leur taille d'affichage, JPEG qualité 86-88, rien d'inutilisé.

Écrire un script unique qui régénère tout (voir `exemple-civrebar/make_all.sh`) : chaque
retouche de l'utilisateur se refait alors en une commande.

### 8. Livrer

Envoyer la charte PDF et le zip. Dans le message : le concept en 5 lignes, le contenu du
pack, et **ce qui n'a pas pu être vérifié** (ex. rendu Word sans LibreOffice, EPS non ouverts
dans Illustrator, CMJN à valider par l'imprimeur, coordonnées fictives à remplacer, polices à
installer). Proposer ensuite des améliorations concrètes, classées par priorité.

## Pièges connus

Voir `references/pieges.md` (polices bloquées, nom de famille CSS réservé, outils absents,
LibreOffice incomplet, favicons flous, contraste, apostrophes dans les f-strings…).
Les plus coûteux :

| Symptôme | Solution |
|---|---|
| Contenu rogné en bas de page | regarder chaque page en PNG |
| Page blanche | `grid-template-areas` entre apostrophes dans un attribut `style` |
| Serif remplacée par une police générique | ne jamais nommer une famille `Serif` ou `Monospace` |
| Polices Google bloquées (403) | `npm i @fontsource/<police>` |
| EPS tronqué / outils absents | `cairosvg.svg2eps` |
| Pas de rendu Office possible | `scripts/verifier_pptx.py`, `scripts/apercu_pptx.py`, et le dire |

## Vérification finale

- [ ] Le concept a une histoire ; chaque élément du symbole est décodé
- [ ] Chaque page du PDF a été regardée en image, rien de rogné, pas de page à moitié vide
- [ ] Contrastes mesurés ; variantes « texte » définies et appliquées aux petits textes
- [ ] Version petites tailles testée à 16 et 32 px ; favicons générés depuis elle
- [ ] Logo avec **et** sans le nom ; couleur, noir, blanc, blanc sur chaque fond
- [ ] SVG, PDF, EPS, PNG **et JPEG** pour chaque version ; texte du logo en tracés
- [ ] Prompts de mises en situation livrés ; grille bento prête (cases « à venir » ou images)
- [ ] Fidélité du logo contrôlée sur chaque image générée
- [ ] Supports numériques aux dimensions exactes ; modèles PowerPoint/Word
- [ ] LISEZ-MOI : HEX/RVB/CMJN, couleurs texte, polices et où les télécharger
- [ ] Zip < 10 Mo ; script de régénération fourni
- [ ] Ce qui n'a pas été vérifié est dit clairement à l'utilisateur
