# Prompts à copier dans Claude Code

Ouvrez Claude Code **dans votre dossier « Echo de U Kabala N°3 »** (celui où vous avez placé `CLAUDE.md` et `_CLAUDE_KIT`).
Il lit automatiquement `CLAUDE.md` (les règles).
Envoyez les prompts **un par un**, dans l'ordre. Ne passez au suivant qu'après avoir validé le résultat.

---

## Prompt 1 : inventaire et questions (le plus important)
```
Lis CLAUDE.md puis tout le dossier, y compris _CLAUDE_KIT. Fais l'étape 0 (inventaire) : rattache chaque document
et chaque photo à une rubrique du bulletin, regarde les photos, et montre-moi le résultat.
Puis enchaîne sur l'étape 1 : pose-moi les questions de complément, rubrique par rubrique, 5 à 8 questions à la
fois, en commençant par l'Activité statutaire. Note mes réponses au fur et à mesure dans 20_PRODUCTION/01_reponses.md.
Ne commence ni le design ni la mise en page tant que je n'ai pas dit « questions terminées ».
```
➡️ Répondez aux questions comme dans une conversation. Vous pouvez aussi ajouter des fichiers dans vos dossiers puis
écrire : `J'ai ajouté des photos dans tel dossier, regarde-les.`


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
rapport aux anciens numéros, en t'inspirant des magazines institutionnels modernes. Pour chaque piste, rends la couverture et une page intérieure avec de vraies photos
du dossier, en PNG dans 20_PRODUCTION/03_pistes/. Donne à chaque piste un nom et une phrase d'explication.
Montre-moi les images. Attends mon choix.
```
➡️ Répondez par exemple : `Je prends la piste B, mais avec la couverture plus bleue et des photos plus grandes.`

## Prompt 4 : rédaction des textes
```
Fais l'étape 4 : rédige tous les textes du bulletin dans 20_PRODUCTION/04_textes.md, rubrique par rubrique,
dans l'ordre du chemin de fer validé. N'utilise que les informations des sources (réponses, documents, notes) ; ce qui manque reste en
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
- `Pour le n°4, garde le même design et prépare un nouveau dossier.`
