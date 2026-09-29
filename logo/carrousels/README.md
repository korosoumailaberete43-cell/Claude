# Carrousels quotidiens CivRebar AI

Des affiches à faire glisser, une publication par jour, aux formats de chaque réseau.

## Ce qu'il y a dans `out/`

| Fichier | Pour |
|---|---|
| `Jxx_…/4x5/01.png …` (1080 × 1350) | Instagram, Facebook, LinkedIn (images) |
| `Jxx_…/9x16/01.png …` (1080 × 1920) | TikTok en mode photo, Statuts WhatsApp, stories |
| `Jxx_…/LinkedIn.pdf` | LinkedIn : publier comme « document », le format carrousel qui y marche le mieux |
| `Jxx_…/legendes.txt` | Textes prêts à coller : TikTok, Facebook/Instagram, LinkedIn |
| `PLANNING.md` | L'ordre de publication et l'objectif de chaque jour |

Sur TikTok, les affiches 9x16 laissent volontairement de la marge en haut et en bas :
les boutons et la légende de l'application s'y superposent sans rien cacher.

## Ajouter ou modifier une publication

Tout le texte est dans `contenu.py`. Pour un nouveau jour, copier un bloc, changer `id`
(`J15_…`), puis les affiches. Types d'affiches disponibles :

- `cover` : l'accroche (titre + sous-titre + bouton « Glisse »)
- `text` : un point numéroté (`num`), avec pictogramme possible (`icon` : barres, cadres, cotes, reperes)
- `big` : un chiffre ou un mot géant
- `quote` : une citation
- `compare` : mythe barré / réalité
- `fields` : la fiche de saisie du plugin ; `beam` : le dessin de poutre ; `symbol` : une pièce du logo
- `steps` : une frise ; `cta` : le logo et l'appel à l'action

Dans les textes, `**mot**` s'affiche en cuivre et ` / ` force un retour à la ligne.

## Produire les images

```sh
python3 carrousels.py          # toutes les publications
python3 carrousels.py J15      # seulement celle-ci
```

Prérequis : python3 + Pillow, node + playwright (le même outillage que `logo/src`).
