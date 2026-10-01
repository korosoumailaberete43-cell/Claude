# Prompts à copier dans Claude Code

Ouvrez Claude Code **dans le dossier `ECHO_U_KABALA_N3`**. Il lit automatiquement `CLAUDE.md` (les règles).
Envoyez les prompts **un par un**, dans l'ordre. Ne passez au suivant qu'après avoir validé le résultat.

---

## Prompt 1 : audit de la collecte
```
Lis CLAUDE.md, puis tout le dossier : la charte dans 01_REFERENCES, les anciens numéros, et chaque fiche.md
avec ses photos. Fais l'étape 1 (audit de la collecte) et écris 20_PRODUCTION/01_audit.md.
Pour chaque rubrique, dis : ce qui est complet, ce qui manque (liste précise de questions à me poser),
les photos manquantes, floues ou mal nommées, et les incohérences. Termine par la liste des questions,
numérotées, à laquelle je pourrai répondre directement. Ne commence pas la maquette.
```
➡️ Complétez les fiches (ou répondez aux questions dans le chat), puis demandez : `Relis les fiches et mets à jour l'audit.`

## Prompt 2 : chemin de fer (plan page par page)
```
Fais l'étape 2 : propose le chemin de fer du bulletin dans 20_PRODUCTION/02_chemin_de_fer.md.
Un tableau page par page : n° de page, rubrique, titre, contenu résumé, photos utilisées (noms de fichiers),
type de gabarit (couverture, ouverture de partie, page texte + 1 photo, page 2 photos, pleine photo, galerie…).
Vise 16 à 24 pages en nombre pair. Explique en 3 lignes tes choix. Attends ma validation.
```

## Prompt 3 : direction artistique (choix du design)
```
Fais l'étape 3 : crée 3 pistes de design différentes, toutes conformes à la charte JCI, mais nouvelles par
rapport aux anciens numéros. Pour chaque piste, rends la couverture et une page intérieure avec de vraies photos
du dossier, en PNG dans 20_PRODUCTION/03_pistes/. Donne à chaque piste un nom et une phrase d'explication.
Montre-moi les images. Attends mon choix.
```
➡️ Répondez par exemple : `Je prends la piste B, mais avec la couverture plus bleue et des photos plus grandes.`

## Prompt 4 : rédaction des textes
```
Fais l'étape 4 : rédige tous les textes du bulletin dans 20_PRODUCTION/04_textes.md, rubrique par rubrique,
dans l'ordre du chemin de fer validé. N'utilise que les informations des fiches ; ce qui manque reste en
[À COMPLÉTER : …]. Respecte la longueur que chaque page peut contenir. Attends ma relecture.
```

## Prompt 5 : mise en page complète
```
Fais l'étape 5 : monte le bulletin complet dans la piste validée, avec les textes validés et les photos,
puis génère 20_PRODUCTION/Echo_U_Kabala_N3_brouillon.pdf et un PNG par page. Regarde toi-même chaque page
et corrige les défauts avant de me montrer le résultat. Donne-moi la liste des pages avec un commentaire court.
```
➡️ Donnez vos retours page par page : `Page 5 : photo trop petite. Page 9 : changer le titre en « … ».`

## Prompt 6 : contrôle qualité
```
Fais l'étape 6 : passe la checklist de CLAUDE.md sur le brouillon, écris 20_PRODUCTION/06_controle.md,
corrige tout ce qui ne passe pas, régénère le PDF et dis-moi ce que tu as corrigé.
```

## Prompt 7 : livraison
```
Fais l'étape 7 : produis la version finale (impression), la version WhatsApp de moins de 15 Mo et les PNG
des pages dans 20_PRODUCTION/. Donne-moi la taille de chaque fichier.
```

---

## Prompts utiles à tout moment
- `Montre-moi la page 7 en image.`
- `Remplace la photo de la page 4 par 2026-08-10_safe-plus_03.jpg.`
- `J'ai ajouté une activité dans 08_DEVELOPPEMENT_INDIVIDUEL : mets à jour textes et maquette.`
- `Pour le n°4, garde le même design : copie ce dossier, vide les fiches et les photos, et prépare la suite.`
