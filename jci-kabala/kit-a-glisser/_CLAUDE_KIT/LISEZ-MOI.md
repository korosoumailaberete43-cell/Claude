# Démarrer Claude Code sur votre ordinateur

## Une seule fois : installer Claude Code
- Le plus simple : l'application **Claude pour ordinateur** (claude.ai/download), onglet **Code**.
- Ou dans un terminal : voir https://code.claude.com/docs (commande d'installation officielle), puis `claude` pour se connecter.

## Préparer le dossier
1. Téléchargez le dossier Drive « Echo de U Kabala N°3 » sur votre ordinateur (clic droit > Télécharger,
   puis décompressez), ou utilisez Google Drive pour ordinateur.
2. Décompressez ce kit et copiez **`CLAUDE.md`**, **`_CLAUDE_KIT`** et le dossier caché **`.claude`** à la **racine** de ce dossier,
   à côté de « Activité statutaires », « Croissance & Motivation », etc. Ne renommez pas `CLAUDE.md`.
   `.claude` commence par un point : il est masqué par défaut. Windows : Explorateur > Affichage > « Éléments masqués ».
   Mac : dans le Finder, touches Cmd + Maj + point.
3. Évitez de lancer Claude Code directement dans le dossier synchronisé Google Drive : travaillez sur une copie locale.

## Lancer la session
- **Application :** onglet Code > choisir le dossier « Echo de U Kabala N°3 » > nouvelle session.
- **Terminal :** `cd` vers le dossier, puis tapez `claude`.
Collez ensuite le **Prompt 1** de `_CLAUDE_KIT/PROMPTS.md`. Répondez aux questions, dites « questions terminées »,
puis passez aux prompts suivants dans l'ordre.

## Si la session s'arrête en cours de route
Ouvrez une nouvelle session dans le même dossier et écrivez :
`Lis CLAUDE.md et 20_PRODUCTION/, dis-moi où nous en sommes et reprends à l'étape suivante.`
Tout le travail est enregistré dans `20_PRODUCTION/`, rien n'est perdu.

## Choisir le modèle pour économiser
Le modèle de la conversation se change avec la commande **`/model`** (ou le sélecteur de modèle dans l'application).
- **Étapes 0, 1, 4, 6, 7** (inventaire, questions, textes, contrôle, livraison) : **Sonnet** suffit.
- **Étapes 2, 3, 5** (plan, design, mise en page) : **Opus**, pour la qualité du design.
Quel que soit votre choix, Claude confie automatiquement le tri des photos et la vérification des pages à des
assistants Sonnet (dossier `.claude/agents`).
