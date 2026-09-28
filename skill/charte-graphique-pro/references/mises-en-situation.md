# Mises en situation photoréalistes et grille bento

La grille bento de photos « la marque sur le terrain » est ce qui fait passer une charte de
« propre » à « agence ». La proposer d'office, sans attendre qu'on la demande.

## 1. Choisir 6 scènes

Deux familles, à mélanger :
- **Objets du métier du client** (les plus forts) : casque de chantier, étiquette sur un fagot
  d'armatures, poste de travail avec le logiciel ouvert, plaque d'entreprise sur mur en béton.
- **Supports classiques** : cartes de visite posées sur un document métier, polo ou gilet brodé.

Donner à chaque scène un numéro (01-06) et un format adapté à sa case :

| Case | Format demandé | Remarque |
|---|---|---|
| a (grande, 2×2) | paysage 3:2 | la plus spectaculaire (ex. casque au coucher de soleil) |
| b (large, 2×1) | paysage 3:2 | sujet dans la **bande horizontale centrale** |
| c (1×1) | paysage 3:2 | |
| d (verticale, 1×2) | portrait 2:3 | |
| e (1×1) | carré 1:1 | |
| f (large, 2×1) | paysage 3:2 | sujet dans la bande centrale |

Disposition CSS : `grid-template-areas:'a a b b' 'a a c d' 'e f f d'`, 4 colonnes, 3 rangées
d'environ 172 px, écart 10 px, coins arrondis, `object-fit:cover`, et un **`object-position` par
image** pour garder le logo visible une fois recadré (ex. `50% 12%` pour un écran dont le logo
est en haut). Légende en pastille : numéro en mono + titre.

## 2. Écrire les prompts (pour ChatGPT ou tout générateur d'images)

L'environnement ne peut souvent pas télécharger d'images générées : passer par l'utilisateur.
Livrer un fichier `PROMPTS_ChatGPT.md` avec un mode d'emploi puis, pour chaque scène :
le **fichier logo à joindre** (couleur pour fond clair, blanc ou « couleur pour fond sombre »
pour fond sombre), le **format**, et un prompt qui dit toujours :

- « utilise EXACTEMENT le logo fourni, sans le modifier, le redessiner, ni changer ses
  couleurs ou ses proportions » ;
- le HEX du support (casque `#0B1624`, carte `#F3F0EA`…) ;
- cadrage, lumière, matière, style (« photographie de marque haut de gamme, sans texte ajouté,
  sans autre logo, sans filigrane ») ;
- où placer le sujet si l'image sera recadrée ;
- pour les personnes : de dos ou visage non visible (évite les soucis de droit à l'image).

Mode d'emploi à inclure : une nouvelle conversation par image ; joindre le logo avant de
coller le prompt ; phrase de relance si le logo est modifié :
« Le logo a été modifié. Refais l'image en reprenant le logo fourni à l'identique. »

## 3. Recevoir les images

- L'environnement cloud n'a **pas accès** au dossier Téléchargements de l'utilisateur. Lui
  proposer : les joindre dans la conversation (trombone), ou les déposer dans un dossier
  Google Drive si le connecteur est disponible.
- Les pièces jointes arrivent dans un dossier `images/` de la session (`1.jpg`, `2.webp`…),
  sans leur nom d'origine : identifier chaque image **visuellement** et la renommer
  `01_casque_chantier.jpg`, etc.
- Une image envoyée **pendant** que l'agent travaille peut s'afficher sans être enregistrée
  sur disque : vérifier le dossier ; si elle manque, demander de la renvoyer seule.
- Construire la page pour qu'elle marche avec les images présentes : cases « Image 0N à venir »
  (trame + symbole en filigrane), ou disposition de repli avec une case de marque
  (logo + signature) si la grande image manque.

## 4. Contrôler la fidélité du logo sur chaque image

Tableau à rendre à l'utilisateur, image par image (✅ / ⚠️). Défauts fréquents des
générateurs : couleur du symbole changée sur fond sombre (ex. R bleu-gris au lieu de blanc
cassé), nom omis, lettres inventées, proportions modifiées, point d'accent disparu. Pour chaque
⚠️, fournir un prompt de correction prêt à coller. Ne pas intégrer silencieusement une image
qui trahit le logo.

## 5. Intégration

Redimensionner à ~300 DPI de la taille affichée (≈ 1300 px de large pour la grande case),
JPEG qualité 86. Copier aussi les originaux dans le pack (`07_Mises_en_situation/`).
