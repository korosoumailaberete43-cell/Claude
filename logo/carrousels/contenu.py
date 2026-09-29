"""Contenu des carrousels CivRebar AI : une publication par jour, 14 jours.

Chaque publication : une suite d'affiches (slides) + les légendes à coller.
Types d'affiches : cover, text, big, quote, compare, fields, beam, symbol, steps, cta.
Mise en forme : « **mot** » s'affiche en cuivre ; « / » force un retour à la ligne.

Tout ce qui est dit du produit reprend la charte (trajectoire, promesse, symbole) :
premier objectif la poutre, puis poteaux, dalles, semelles, escaliers, puis plugin, puis IA.
"""

HASHTAGS = ["#GénieCivil", "#BétonArmé", "#Ferraillage", "#AutoCAD", "#BTP", "#CivRebarAI"]

CTA = {"t": "cta", "title": "Bientôt dans **AutoCAD**.", "body": "Abonne-toi pour suivre la sortie."}

POSTS = [
    # ------------------------------------------------------------------ J01
    {
        "id": "J01_teaser", "titre": "Quelque chose se prépare", "objectif": "Créer le mystère", "theme": "nuit",
        "kicker": "Projet confidentiel",
        "slides": [
            {"t": "cover", "title": "Un nouvel outil arrive / pour le **génie civil**.", "sub": "Glisse pour découvrir ce qui se prépare."},
            {"t": "text", "title": "Chaque ouvrage / cache une **ossature**.", "body": "Sous le béton, il y a l'armature. Une fois le coulage fait, plus personne ne la voit. Pourtant, c'est elle qui porte tout."},
            {"t": "text", "title": "Des milliers de barres. / Choisies. Pliées. **Placées.**", "body": "Et chacune a d'abord été dessinée, trait par trait, sur un plan."},
            {"t": "quote", "quote": "Rien n'y est décoratif. / Tout y est calculé."},
            {"t": "big", "big": "?", "body": "Et si l'armature devenait **intelligente** ?"},
            dict(CTA, title="**CivRebar AI** arrive.", body="Abonne-toi : on te montre tout, étape par étape."),
        ],
        "court": "Quelque chose se prépare pour le génie civil… 🔩 Glisse jusqu'au bout 👉",
        "legende": """Quelque chose se prépare pour les ingénieurs, techniciens et dessinateurs en génie civil. 🔩

Sous le béton, il y a l'armature. Des milliers de barres, choisies, pliées, placées… et chacune a d'abord été dessinée sur un plan.

Et si l'armature devenait intelligente ?

👉 Glisse jusqu'à la dernière image, et abonne-toi pour suivre la suite : chaque jour, on lève un peu plus le voile.""",
    },
    # ------------------------------------------------------------------ J02
    {
        "id": "J02_probleme", "titre": "Pourquoi le ferraillage prend autant de temps", "objectif": "Poser le problème", "theme": "chaux",
        "kicker": "Le constat",
        "slides": [
            {"t": "cover", "title": "Pourquoi ferrailler / prend-il autant / de **temps** ?", "sub": "4 raisons que tout dessinateur connaît."},
            {"t": "text", "num": "01", "title": "Tout se dessine / **à la main**.", "body": "Chaque barre, chaque cadre, chaque cote est tracé trait par trait."},
            {"t": "text", "num": "02", "title": "Tout se **répète**.", "body": "Une poutre, puis la suivante, puis la suivante… avec presque les mêmes gestes."},
            {"t": "text", "num": "03", "title": "Tout se **vérifie**.", "body": "Enrobages, espacements, ancrages, repères : une erreur sur le plan se paie sur le chantier."},
            {"t": "text", "num": "04", "title": "Tout **change**.", "body": "Une section modifiée, une portée revue ? Il faut reprendre le dessin."},
            {"t": "big", "big": "Des heures", "body": "de dessin, de vérification et de reprises. / Et si une seule commande suffisait ?"},
            dict(CTA, title="On y travaille.", body="Abonne-toi pour découvrir **CivRebar AI**."),
        ],
        "court": "4 raisons pour lesquelles le ferraillage prend autant de temps. Tu te reconnais ? 😮‍💨👉",
        "legende": """Pourquoi le ferraillage prend-il autant de temps ? ⏳

1️⃣ Tout se dessine à la main, trait par trait.
2️⃣ Tout se répète, d'une poutre à l'autre.
3️⃣ Tout se vérifie : enrobages, espacements, ancrages, repères.
4️⃣ Tout change : une section modifiée, et il faut reprendre le dessin.

C'est exactement ce problème que CivRebar AI veut résoudre.

💬 Laquelle de ces 4 étapes te prend le plus de temps ? Dis-le en commentaire.""",
    },
    # ------------------------------------------------------------------ J03
    {
        "id": "J03_cest_quoi", "titre": "CivRebar AI, c'est quoi ?", "objectif": "Présenter la solution", "theme": "nuit",
        "kicker": "La solution",
        "slides": [
            {"t": "cover", "title": "**CivRebar AI**, / c'est quoi / exactement ?", "sub": "Tout comprendre en quelques images."},
            {"t": "text", "num": "01", "title": "Un outil de / ferraillage pour / **AutoCAD**.", "body": "Pas un logiciel de plus à apprendre : il travaille dans AutoCAD, là où tu dessines déjà."},
            {"t": "text", "num": "02", "title": "Tu donnes les / paramètres, il / **dessine**.", "body": "Section, portée, armatures : CivRebar AI trace les barres, les cadres, les cotes et les repères."},
            {"t": "text", "num": "03", "title": "Élément par / **élément**.", "body": "Premier objectif : la poutre. Puis les poteaux, les dalles, les semelles et les escaliers."},
            {"t": "text", "num": "04", "title": "Puis une / **intelligence**.", "body": "À terme : nomenclatures, quantitatifs, vérifications et un assistant IA."},
            {"t": "quote", "quote": "Une intelligence qui assiste, / sans jamais remplacer / celui qui signe le plan.", "by": "La promesse CivRebar AI"},
            CTA,
        ],
        "court": "CivRebar AI expliqué en 5 images 👉 Le ferraillage assisté, directement dans AutoCAD.",
        "legende": """CivRebar AI, c'est quoi exactement ? 🔩

✅ Un outil de ferraillage conçu pour AutoCAD.
✅ Tu donnes la section, la portée et les armatures : il dessine les barres, les cadres, les cotes et les repères.
✅ Élément par élément : la poutre d'abord, puis les poteaux, les dalles, les semelles et les escaliers.
✅ À terme, une intelligence qui vérifie et quantifie.

Et une promesse : une IA qui assiste, sans jamais remplacer celui qui signe le plan.

👉 Abonne-toi pour suivre la sortie.""",
    },
    # ------------------------------------------------------------------ J04
    {
        "id": "J04_comment", "titre": "Comment ça marche, en 3 étapes", "objectif": "Montrer la simplicité", "theme": "chaux",
        "kicker": "Mode d'emploi",
        "slides": [
            {"t": "cover", "title": "Le ferraillage / d'une poutre, / en **une commande**.", "sub": "Voici comment, en 3 étapes."},
            {"t": "fields", "num": "01", "title": "Tu **saisis**.", "fields": [("Section", "30 × 60 cm"), ("Portée", "5,40 m"), ("Armatures", "3 HA20 / 2 HA14"), ("Cadres", "HA8 e = 15")]},
            {"t": "fields", "num": "02", "title": "Tu **lances**.", "fields": [("Section", "30 × 60 cm"), ("Portée", "5,40 m")], "button": "DESSINER", "body": "Un clic. C'est tout."},
            {"t": "beam", "num": "03", "title": "Il **dessine**.", "body": "Barres, cadres, cotes et repères, directement dans ton plan."},
            {"t": "text", "title": "Et tu gardes / **la main**.", "body": "Tu vérifies, tu ajustes, tu signes. L'outil t'assiste ; la décision reste la tienne."},
            CTA,
        ],
        "court": "Le ferraillage d'une poutre en une commande : 1. tu saisis 2. tu lances 3. il dessine 👉",
        "legende": """Le ferraillage d'une poutre, en une seule commande. Voici comment ça marchera 👇

1️⃣ Tu saisis : la section, la portée, les armatures, les cadres.
2️⃣ Tu lances la commande.
3️⃣ CivRebar AI dessine les barres, les cadres, les cotes et les repères, directement dans AutoCAD.

Et toi, tu gardes la main : tu vérifies, tu ajustes, tu signes.

💬 Combien de temps te prend le ferraillage d'une poutre aujourd'hui ? Dis-le en commentaire.""",
    },
    # ------------------------------------------------------------------ J05
    {
        "id": "J05_quiz", "titre": "Quiz : combien de cadres ?", "objectif": "Faire réagir (commentaires)", "theme": "nuit",
        "kicker": "Quiz d'ingénieur",
        "slides": [
            {"t": "cover", "title": "Combien de **cadres** / dans cette poutre ?", "sub": "Réponds en commentaire avant de regarder la solution."},
            {"t": "beam", "title": "Les données", "labels": True, "body": "Poutre de **5,40 m**, cadres régulièrement espacés de **15 cm**, un cadre à chaque extrémité."},
            {"t": "text", "title": "Un indice ?", "body": "Nombre de cadres = / longueur ÷ espacement **+ 1**"},
            {"t": "big", "big": "37", "body": "5,40 ÷ 0,15 = 36 intervalles, / donc **37 cadres**."},
            {"t": "text", "title": "Et ce n'est / qu'**une poutre**.", "body": "Imagine un bâtiment entier. C'est exactement ce que CivRebar AI veut dessiner pour toi."},
            dict(CTA, title="Tu avais trouvé ?", body="Dis-le en commentaire, et abonne-toi pour le prochain quiz.", actions=["Commente", "Partage", "Abonne-toi"]),
        ],
        "court": "Quiz 🧠 Combien de cadres dans une poutre de 5,40 m espacés de 15 cm ? Réponds AVANT de glisser 👀",
        "legende": """🧠 QUIZ D'INGÉNIEUR

Poutre de 5,40 m. Cadres régulièrement espacés de 15 cm, un cadre à chaque extrémité.
Combien de cadres faut-il ?

💬 Réponds en commentaire AVANT de regarder la solution (dernières images) 👀

Et ce n'est qu'une poutre… Imagine un bâtiment entier. C'est ce que CivRebar AI veut dessiner pour toi.""",
    },
    # ------------------------------------------------------------------ J06
    {
        "id": "J06_ce_quil_dessine", "titre": "Ce que CivRebar AI dessine", "objectif": "Détailler la fonction", "theme": "chaux",
        "kicker": "Ce qu'il dessine",
        "slides": [
            {"t": "cover", "title": "**4 choses** que / CivRebar AI dessine / pour toi.", "sub": "À partir de quelques paramètres."},
            {"t": "text", "icon": "barres", "title": "Les **barres**.", "body": "Les armatures longitudinales, supérieures et inférieures, avec leurs ancrages."},
            {"t": "text", "icon": "cadres", "title": "Les **cadres**.", "body": "Répartis sur toute la longueur, selon l'espacement choisi."},
            {"t": "text", "icon": "cotes", "title": "Les **cotes**.", "body": "Longueurs et espacements, lisibles sur le plan."},
            {"t": "text", "icon": "reperes", "title": "Les **repères**.", "body": "Chaque barre identifiée, pour s'y retrouver du bureau jusqu'au chantier."},
            CTA,
        ],
        "court": "Barres, cadres, cotes, repères : CivRebar AI les dessine pour toi 🔩👉",
        "legende": """4 choses que CivRebar AI dessinera pour toi, à partir de quelques paramètres 👇

🔸 Les barres longitudinales, avec leurs ancrages
🔸 Les cadres, répartis selon l'espacement choisi
🔸 Les cotes, lisibles sur le plan
🔸 Les repères, pour s'y retrouver jusqu'au chantier

Le tout directement dans AutoCAD.

👉 Abonne-toi pour la suite.""",
    },
    # ------------------------------------------------------------------ J07
    {
        "id": "J07_logo", "titre": "Pourquoi notre logo est un R façonné", "objectif": "Raconter la marque", "theme": "nuit",
        "kicker": "L'histoire du symbole",
        "slides": [
            {"t": "cover", "title": "Notre logo cache / un **plan de / ferraillage**.", "sub": "Tu l'avais remarqué ?"},
            {"t": "symbol", "focus": "fut", "num": "01", "title": "La barre / **longitudinale**", "body": "Le fût du R. La colonne vertébrale de l'ouvrage : l'ingénieur, sa méthode, sa responsabilité."},
            {"t": "symbol", "focus": "panse", "num": "02", "title": "L'étrier / **façonné**", "body": "La panse du R. Il ceinture et confine : les règles de l'art qui encadrent chaque décision."},
            {"t": "symbol", "focus": "crochet", "num": "03", "title": "Le crochet / **à 135°**", "body": "L'ancrage des étriers. Un détail que seuls les gens du métier remarquent."},
            {"t": "symbol", "focus": "relevee", "num": "04", "title": "La barre / **relevée**", "body": "En cuivre. Elle reprend l'effort tranchant, et part vers l'avant : le projet qui avance."},
            {"t": "symbol", "focus": "noeud", "num": "05", "title": "Le nœud / **Signal**", "body": "L'IA, au cœur de l'armature, tenue et guidée par l'ingénierie. Jamais à sa place."},
            dict(CTA, title="L'intelligence / de l'**armature**.", body="Abonne-toi pour suivre l'aventure."),
        ],
        "court": "Notre logo cache un plan de ferraillage. Tu l'avais vu ? 👀👉",
        "legende": """Notre logo n'est pas qu'un « R ». C'est un détail de ferraillage 🔩

1️⃣ La barre longitudinale : l'ingénieur, sa méthode, sa responsabilité.
2️⃣ L'étrier façonné : les règles de l'art qui encadrent chaque décision.
3️⃣ Le crochet à 135° : l'ancrage des étriers, un clin d'œil aux gens du métier.
4️⃣ La barre relevée, en cuivre : l'effort tranchant, et le projet qui avance.
5️⃣ Le nœud Signal : l'IA, tenue et guidée par l'ingénierie. Jamais à sa place.

💬 Tu avais repéré le crochet à 135° ?""",
    },
    # ------------------------------------------------------------------ J08
    {
        "id": "J08_mythes", "titre": "L'IA va-t-elle remplacer l'ingénieur ?", "objectif": "Rassurer, prendre position", "theme": "chaux",
        "kicker": "Mythe ou réalité",
        "slides": [
            {"t": "cover", "title": "L'IA va-t-elle / **remplacer** / l'ingénieur ?", "sub": "3 idées reçues, et notre réponse."},
            {"t": "compare", "title": "Idée reçue n° 1", "a": "L'IA décide à ta place.", "b": "L'IA propose. / L'ingénieur décide et signe."},
            {"t": "compare", "title": "Idée reçue n° 2", "a": "Plus besoin de connaître les règles.", "b": "Il faut les maîtriser pour vérifier ce que l'outil propose."},
            {"t": "compare", "title": "Idée reçue n° 3", "a": "C'est une boîte noire.", "b": "Le résultat est un dessin AutoCAD : tu le vois, tu le contrôles."},
            {"t": "quote", "quote": "L'IA sert l'ingénieur, / jamais l'inverse.", "by": "Une valeur CivRebar AI"},
            CTA,
        ],
        "court": "L'IA va-t-elle remplacer l'ingénieur ? Notre réponse en 3 idées reçues 👉",
        "legende": """L'IA va-t-elle remplacer l'ingénieur ? 🤖👷🏾‍♂️

Notre réponse est claire : non.

❌ « L'IA décide à ta place » → L'IA propose, l'ingénieur décide et signe.
❌ « Plus besoin de connaître les règles » → Il faut les maîtriser pour vérifier.
❌ « C'est une boîte noire » → Le résultat est un dessin AutoCAD : tu le vois, tu le contrôles.

Chez CivRebar AI, l'IA sert l'ingénieur, jamais l'inverse.

💬 Et toi, l'IA dans le génie civil : opportunité ou menace ?""",
    },
    # ------------------------------------------------------------------ J09
    {
        "id": "J09_pour_qui", "titre": "Pour qui ?", "objectif": "Cibler, faire identifier", "theme": "nuit",
        "kicker": "Pour qui ?",
        "slides": [
            {"t": "cover", "title": "Tu te reconnais / dans l'un de ces / **profils** ?", "sub": "CivRebar AI est pensé pour toi."},
            {"t": "text", "num": "01", "title": "Ingénieur / **structure**", "body": "Tu calcules, tu dimensionnes, tu signes. Tu veux des plans fidèles à tes notes de calcul."},
            {"t": "text", "num": "02", "title": "Dessinateur / **projeteur**", "body": "Tu traces le ferraillage au quotidien. Tu veux passer moins de temps sur les gestes répétitifs."},
            {"t": "text", "num": "03", "title": "Bureau / **d'études**", "body": "Tu enchaînes les projets. Tu veux des plans homogènes, quel que soit celui qui dessine."},
            {"t": "text", "num": "04", "title": "Étudiant en / **génie civil**", "body": "Tu apprends le béton armé. Tu veux voir concrètement comment un ferraillage se construit."},
            dict(CTA, title="Identifie un **collègue**", body="qui devrait voir ça.", actions=["Identifie", "Partage", "Abonne-toi"]),
        ],
        "court": "Ingénieur, dessinateur, bureau d'études ou étudiant ? CivRebar AI est pensé pour toi 👉 Identifie un collègue !",
        "legende": """CivRebar AI, c'est pour qui ? 👇

👷🏾‍♂️ Ingénieurs structure : des plans fidèles à vos notes de calcul.
✏️ Dessinateurs et projeteurs : moins de gestes répétitifs.
🏢 Bureaux d'études : des plans homogènes, quel que soit celui qui dessine.
🎓 Étudiants en génie civil : comprendre concrètement le ferraillage.

💬 Identifie en commentaire un collègue qui devrait voir ça !""",
    },
    # ------------------------------------------------------------------ J10
    {
        "id": "J10_checklist", "titre": "5 points à vérifier sur un plan de ferraillage", "objectif": "Apporter de la valeur (enregistrements)", "theme": "chaux",
        "kicker": "Checklist",
        "slides": [
            {"t": "cover", "title": "**5 points** à vérifier / sur un plan de / ferraillage.", "sub": "Enregistre ce post pour ton prochain plan."},
            {"t": "text", "num": "01", "title": "L'**enrobage**", "body": "L'épaisseur de béton entre l'acier et la surface. Elle protège les armatures de la corrosion et du feu."},
            {"t": "text", "num": "02", "title": "Les **espacements**", "body": "Entre les barres et entre les cadres : assez larges pour bien couler le béton, assez serrés pour reprendre les efforts."},
            {"t": "text", "num": "03", "title": "Ancrages et / **recouvrements**", "body": "Des longueurs suffisantes pour que l'effort passe du béton à la barre, et d'une barre à l'autre."},
            {"t": "text", "num": "04", "title": "Les **diamètres**", "body": "Chaque barre repérée avec son diamètre et sa nuance : HA8, HA12, HA16…"},
            {"t": "text", "num": "05", "title": "Cotes et **repères**", "body": "Un plan clair, c'est moins d'erreurs de façonnage et de pose sur le chantier."},
            dict(CTA, title="**Enregistre** ce post", body="et partage-le à ton équipe.", actions=["Enregistre", "Partage", "Abonne-toi"]),
        ],
        "court": "5 points à vérifier sur un plan de ferraillage ✅ Enregistre-le pour ton prochain plan 📌",
        "legende": """✅ 5 points à vérifier sur un plan de ferraillage :

1️⃣ L'enrobage : il protège les armatures de la corrosion et du feu.
2️⃣ Les espacements : assez larges pour couler, assez serrés pour reprendre les efforts.
3️⃣ Les ancrages et recouvrements : pour que l'effort passe d'une barre à l'autre.
4️⃣ Les diamètres : chaque barre repérée (HA8, HA12, HA16…).
5️⃣ Les cotes et repères : un plan clair, c'est moins d'erreurs sur le chantier.

📌 Enregistre ce post pour ton prochain plan, et partage-le à ton équipe.""",
    },
    # ------------------------------------------------------------------ J11
    {
        "id": "J11_feuille_de_route", "titre": "Notre feuille de route", "objectif": "Montrer la vision", "theme": "nuit",
        "kicker": "Feuille de route",
        "slides": [
            {"t": "cover", "title": "On construit / CivRebar comme / on **ferraille**.", "sub": "Barre après barre. Voici les étapes."},
            {"t": "text", "num": "01", "title": "**AutoLISP**", "body": "Un script par élément. Premier objectif : la poutre, des paramètres au dessin coté et repéré."},
            {"t": "text", "num": "02", "title": "Boîte à **outils**", "body": "Tous les scripts sous un seul menu : poutre, poteau, dalle, semelle, escalier."},
            {"t": "text", "num": "03", "title": "Plugin / **AutoCAD**", "body": "Une vraie extension, avec son onglet dans le ruban et une interface soignée."},
            {"t": "text", "num": "04", "title": "**Intelligence**", "body": "Nomenclatures, quantitatifs, vérifications, échanges avec les logiciels de calcul, assistant IA."},
            {"t": "steps", "title": "Nous sommes ici :", "steps": [("Intelligence", "La destination."), ("Plugin AutoCAD", "L'extension complète."), ("Boîte à outils", "Tous les éléments."), ("AutoLISP · Poutre", "Le premier pas. On y est.")]},
            dict(CTA, title="Suis chaque **étape**", body="avec nous.", actions=["Abonne-toi", "Active les notifs"]),
        ],
        "court": "La feuille de route de CivRebar AI : de l'AutoLISP à l'intelligence artificielle 🔩👉",
        "legende": """On construit CivRebar AI comme on ferraille : barre après barre. 🔩

01 · AutoLISP : un script par élément, en commençant par la poutre.
02 · Boîte à outils : poutre, poteau, dalle, semelle, escalier sous un seul menu.
03 · Plugin AutoCAD : une vraie extension, avec son onglet dans le ruban.
04 · Intelligence : nomenclatures, quantitatifs, vérifications, assistant IA.

📍 Nous sommes à l'étape 01.

👉 Abonne-toi et active les notifications pour suivre chaque étape.""",
    },
    # ------------------------------------------------------------------ J12
    {
        "id": "J12_vocabulaire", "titre": "Le ferraillage en 6 mots", "objectif": "Éduquer, élargir l'audience", "theme": "chaux",
        "kicker": "Vocabulaire",
        "slides": [
            {"t": "cover", "title": "Le ferraillage / en **6 mots**.", "sub": "Que tu sois étudiant ou pro, révise les bases."},
            {"t": "text", "icon": "barres", "title": "Barre / **longitudinale**", "body": "Parallèle à l'axe de l'élément, elle reprend les efforts de traction dus à la flexion."},
            {"t": "text", "icon": "cadres", "title": "Cadre / (ou **étrier**)", "body": "Il entoure les barres, reprend l'effort tranchant et les maintient en place."},
            {"t": "text", "num": "03", "title": "**Enrobage**", "body": "L'épaisseur de béton entre la surface et l'armature la plus proche."},
            {"t": "text", "num": "04", "title": "**Ancrage**", "body": "La longueur nécessaire pour qu'une barre transmette son effort au béton."},
            {"t": "text", "num": "05", "title": "**Recouvrement**", "body": "La zone où deux barres se chevauchent pour assurer la continuité."},
            {"t": "text", "num": "06", "title": "Crochet / **à 135°**", "body": "L'extrémité recourbée des cadres, qui assure leur ancrage dans le béton."},
            dict(CTA, title="Lequel tu **confonds** ?", body="Dis-le en commentaire.", actions=["Commente", "Enregistre", "Abonne-toi"]),
        ],
        "court": "Le ferraillage en 6 mots 🔩 Étudiant ou pro, tu les connais tous ? 👉",
        "legende": """Le ferraillage en 6 mots 🔩

🔸 Barre longitudinale : reprend les efforts de traction dus à la flexion.
🔸 Cadre (étrier) : reprend l'effort tranchant et maintient les barres.
🔸 Enrobage : l'épaisseur de béton qui protège l'armature.
🔸 Ancrage : la longueur pour que la barre transmette son effort au béton.
🔸 Recouvrement : la zone où deux barres se chevauchent.
🔸 Crochet à 135° : l'ancrage des cadres.

📌 Enregistre pour réviser, et 💬 dis-nous quel mot manque à la liste !""",
    },
    # ------------------------------------------------------------------ J13
    {
        "id": "J13_valeurs", "titre": "Nos 3 valeurs", "objectif": "Créer la confiance", "theme": "nuit",
        "kicker": "Nos valeurs",
        "slides": [
            {"t": "cover", "title": "**3 valeurs** / qui guident / CivRebar AI.", "sub": "Ce qui ne changera jamais."},
            {"t": "text", "num": "01", "title": "**Rigueur**", "body": "Chaque trait respecte les règles de l'art. Rien n'est décoratif, tout est calculé."},
            {"t": "text", "num": "02", "title": "**Progression**", "body": "On construit par étapes, sur du solide. D'abord la poutre, puis le reste."},
            {"t": "text", "num": "03", "title": "**Assistance**", "body": "L'IA sert l'ingénieur, jamais l'inverse. C'est lui qui signe le plan."},
            {"t": "quote", "quote": "Ce qui tient un ouvrage / ne se voit pas.", "by": "CivRebar AI"},
            CTA,
        ],
        "court": "Rigueur. Progression. Assistance. Les 3 valeurs de CivRebar AI 🔩",
        "legende": """3 valeurs qui guident CivRebar AI 🔩

01 · Rigueur : chaque trait respecte les règles de l'art.
02 · Progression : on construit par étapes, sur du solide.
03 · Assistance : l'IA sert l'ingénieur, jamais l'inverse.

Ce qui tient un ouvrage ne se voit pas. Mais c'est lui qui porte tout.

👉 Abonne-toi pour suivre la suite.""",
    },
    # ------------------------------------------------------------------ J14
    {
        "id": "J14_rejoindre", "titre": "Sois parmi les premiers", "objectif": "Convertir (abonnés, contacts)", "theme": "chaux",
        "kicker": "Rejoins-nous",
        "slides": [
            {"t": "cover", "title": "Tu veux découvrir / CivRebar AI / **parmi les premiers** ?", "sub": "4 gestes, 10 secondes."},
            {"t": "text", "num": "01", "title": "**Abonne-toi** / à la page.", "body": "C'est ici que tout sera annoncé en premier."},
            {"t": "text", "num": "02", "title": "Active les / **notifications**.", "body": "Pour ne rien rater de la sortie."},
            {"t": "text", "num": "03", "title": "Écris-nous / « **MOI** ».", "body": "En message privé : on te préviendra personnellement."},
            {"t": "text", "num": "04", "title": "**Partage** à un / collègue.", "body": "Celui qui ferraille encore tout à la main te remerciera."},
            dict(CTA, title="À très **bientôt**.", body="L'intelligence de l'armature arrive dans AutoCAD.", actions=["Abonne-toi", "Écris « MOI »", "Partage"]),
        ],
        "court": "Tu veux découvrir CivRebar AI parmi les premiers ? Écris-nous « MOI » en message 📩",
        "legende": """Tu veux découvrir CivRebar AI parmi les premiers ? 🚀

1️⃣ Abonne-toi à la page
2️⃣ Active les notifications
3️⃣ Écris-nous « MOI » en message privé
4️⃣ Partage à un collègue qui ferraille encore tout à la main

L'intelligence de l'armature arrive bientôt dans AutoCAD. 🔩""",
    },
    # ------------------------------------------------------------------ J15 (série « Trouve l'erreur », n° 1)
    {
        "id": "J15_trouve_erreur_01", "titre": "Trouve l'erreur n° 1 : les cadres", "objectif": "Faire commenter, montrer l'expertise", "theme": "nuit",
        "kicker": "Trouve l'erreur · n° 1",
        "slides": [
            {"t": "cover", "title": "Trouve **l'erreur** / sur ce plan.", "sub": "Poutre sur deux appuis, charge répartie. Un seul détail cloche. Réponds en commentaire avant de glisser."},
            {"t": "plan", "mode": "erreur", "tag": "Poutre P1 — 30 × 60", "title": "Le plan", "body": "Regarde bien les cadres. Tu as trouvé ? Écris ta réponse en commentaire."},
            {"t": "text", "title": "Un indice ?", "body": "Demande-toi où l'**effort tranchant** est le plus fort sur cette poutre."},
            {"t": "plan", "mode": "reponse", "tag": "Réponse", "title": "Les cadres sont serrés / au **mauvais endroit**.", "body": "Espacés de 25 cm près des appuis, serrés à 10 cm au milieu : c'est l'inverse qu'il faut."},
            {"t": "plan", "mode": "tranchant", "tag": "Pourquoi ?", "title": "L'effort tranchant", "body": "Sur une poutre sur deux appuis, il est **maximal aux appuis** et presque nul au milieu. Or ce sont les cadres qui le reprennent."},
            {"t": "plan", "mode": "correct", "tag": "Le bon plan", "title": "Serrés aux **appuis**, / plus espacés au milieu.", "body": "Exemple de principe : les espacements réels se calculent selon les charges et la norme."},
            {"t": "text", "title": "Ce genre de détail, / CivRebar AI t'aidera / à le **repérer**.", "body": "Les vérifications font partie de notre feuille de route. Un nouveau « Trouve l'erreur » chaque semaine."},
            dict(CTA, title="Tu avais **trouvé** ?", body="Dis-le en commentaire, et abonne-toi pour le prochain défi.", actions=["Commente", "Partage", "Abonne-toi"]),
        ],
        "court": "🔍 TROUVE L'ERREUR n° 1 : un seul détail cloche sur ce plan de poutre. Réponds en commentaire AVANT de glisser 👀",
        "legende": """🔍 TROUVE L'ERREUR — n° 1

Poutre sur deux appuis, charge répartie. Un seul détail cloche sur ce plan.

💬 Écris ta réponse en commentaire AVANT de regarder la solution (images 4 à 6) 👀

Indice : où l'effort tranchant est-il le plus fort ?

Un nouveau « Trouve l'erreur » chaque semaine. Abonne-toi pour ne pas le rater 🔩""",
    },
]
