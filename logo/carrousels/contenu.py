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
]


# ---------------------------------------------------------------- jours 15 à 43 (13/10 → 10/11)
def _post(pid, titre, objectif, theme, kicker, slides, court, legende):
    return {"id": pid, "titre": titre, "objectif": objectif, "theme": theme, "kicker": kicker,
            "slides": slides + [dict(CTA)], "court": court, "legende": legende}


POSTS += [
    _post("J15_anatomie_poutre", "L'anatomie d'une poutre", "Pédagogie", "nuit", "Comprendre",
          [{"t": "cover", "title": "Tout ce qu'il y a / dans une **poutre**.", "sub": "Cinq familles d'armatures, et le rôle de chacune."},
           {"t": "text", "num": "01", "icon": "barres", "title": "Les barres / **inférieures**.", "body": "Elles reprennent la traction en partie basse, là où la poutre fléchit. Ce sont les plus grosses."},
           {"t": "text", "num": "02", "title": "Les **chapeaux**.", "body": "En partie haute, au-dessus des appuis : là, c'est le dessus de la poutre qui est tendu."},
           {"t": "text", "num": "03", "icon": "cadres", "title": "Les **cadres**.", "body": "Ils reprennent l'effort tranchant et tiennent les barres en place. Resserrés près des appuis."},
           {"t": "text", "num": "04", "title": "Les **épingles**.", "body": "Elles tiennent les barres qui ne sont pas dans les angles du cadre."},
           {"t": "text", "num": "05", "title": "Les **ancrages**.", "body": "Aux extrémités, la barre doit être retenue : retour, crochet, ou longueur suffisante."},
           {"t": "beam", "title": "Toutes ensemble.", "body": "Chaque famille a sa raison d'être. Enlève-en une, et la poutre change de comportement."}],
          "Les 5 familles d'armatures d'une poutre 🔩 Tu les connais toutes ? 👉",
          """L'anatomie d'une poutre en béton armé 🔩\n\n1️⃣ Les barres inférieures : la traction en partie basse.\n2️⃣ Les chapeaux : la traction en partie haute, sur appuis.\n3️⃣ Les cadres : l'effort tranchant, resserrés aux appuis.\n4️⃣ Les épingles : elles tiennent les barres intermédiaires.\n5️⃣ Les ancrages : pour que les barres ne glissent pas.\n\n💬 Laquelle est la plus souvent oubliée sur les plans ?"""),

    _post("J16_lire_un_plan", "Comment lire un plan de ferraillage", "Pédagogie", "chaux", "Méthode",
          [{"t": "cover", "title": "Lire un plan / de **ferraillage**.", "sub": "Dans quel ordre regarder, pour ne rien rater."},
           {"t": "steps", "title": "L'ordre de lecture", "steps": [["1. Le cartouche", "Projet, niveau, indice. Tu travailles sur la bonne version ?"],
                                                                   ["2. La vue en élévation", "La portée, les appuis, les dimensions."],
                                                                   ["3. Les coupes", "La section, les barres, les cadres, l'enrobage."],
                                                                   ["4. La nomenclature", "Les repères, les diamètres, les longueurs, les quantités."]]},
           {"t": "text", "title": "Le piège / de l'**indice**.", "body": "Un plan « indice B » et un plan « indice C » se ressemblent. Les aciers, eux, peuvent avoir changé."},
           {"t": "text", "title": "Le repère / fait le **lien**.", "body": "Un numéro de repère relie le trait du plan, la ligne de la nomenclature, et la barre façonnée en atelier."},
           {"t": "quote", "quote": "Un plan se lit deux fois : / une fois pour comprendre, / une fois pour vérifier."}],
          "Dans quel ordre lire un plan de ferraillage ? La méthode en 4 étapes 👉",
          """Comment lire un plan de ferraillage, dans le bon ordre 📐\n\n1️⃣ Le cartouche : projet, niveau, et surtout l'indice.\n2️⃣ L'élévation : portée, appuis, dimensions.\n3️⃣ Les coupes : section, barres, cadres, enrobage.\n4️⃣ La nomenclature : repères, diamètres, longueurs.\n\n⚠️ Le piège classique : travailler sur un indice périmé.\n\n💬 Et toi, tu commences par quoi ?"""),

    _post("J17_acier_beton", "Pourquoi l'acier et le béton vont ensemble", "Pédagogie", "nuit", "Les bases",
          [{"t": "cover", "title": "Pourquoi **l'acier** / et le **béton** ?", "sub": "Deux matériaux que rien ne rapprochait."},
           {"t": "compare", "title": "Chacun sa faiblesse", "a_label": "Le béton", "a": "Excellent en compression. Mais il casse net dès qu'on le tire.",
            "b_label": "L'acier", "b": "Excellent en traction. Mais seul, il flambe et il rouille."},
           {"t": "text", "title": "Ensemble, / ils se **complètent**.", "body": "Le béton prend la compression, l'acier prend la traction. Le béton protège l'acier de la rouille et du feu."},
           {"t": "text", "title": "Et ils se **dilatent** / pareil.", "body": "C'est la coïncidence qui rend tout possible : chauffés, les deux matériaux s'allongent presque de la même façon. Ils ne se décollent pas."},
           {"t": "big", "big": "100 %", "body": "de l'effort passe par **l'adhérence**. / C'est pour ça que les barres ont des nervures."}],
          "Pourquoi l'acier et le béton forment le meilleur duo du BTP 🔩 Glisse 👉",
          """Pourquoi l'acier et le béton vont si bien ensemble 🤝\n\n🧱 Le béton : très fort en compression, nul en traction.\n🔩 L'acier : très fort en traction, mais il flambe et il rouille.\n\nEnsemble, chacun couvre la faiblesse de l'autre. Et surtout : ils se dilatent presque pareil, donc ils ne se décollent pas.\n\nTout repose sur l'adhérence : c'est pour ça que les barres ont des nervures.\n\n💬 Tu l'expliquerais comment, toi ?"""),

    _post("J18_vocabulaire2", "Le ferraillage en 6 symboles", "Pédagogie", "chaux", "Vocabulaire",
          [{"t": "cover", "title": "Six **symboles** / qu'on lit tous les jours.", "sub": "Tu les décodes tous sans réfléchir ?"},
           {"t": "fields", "ph": "LES SYMBOLES DU PLAN", "title": "Le décodeur", "fields": [("Ø", "diamètre d'une barre"), ("HA", "barre à haute adhérence"),
                                                                                             ("e", "espacement entre cadres"), ("ls", "longueur de recouvrement"),
                                                                                             ("lb", "longueur d'ancrage"), ("c", "enrobage")]},
           {"t": "text", "title": "« 3 HA20 », / ça se lit **comment** ?", "body": "Trois barres à haute adhérence, de 20 millimètres de diamètre."},
           {"t": "text", "title": "« HA8 e = 15 », / ça veut dire ?", "body": "Des cadres en HA8, espacés de 15 centimètres les uns des autres."},
           {"t": "quote", "quote": "Le plan parle une langue. / Encore faut-il l'avoir apprise."}],
          "6 symboles du ferraillage, décodés 🔩 Tu les connais tous ? 👉",
          """Le décodeur du plan de ferraillage 📐\n\nØ : le diamètre d'une barre\nHA : barre à haute adhérence\ne : espacement entre cadres\nls : longueur de recouvrement\nlb : longueur d'ancrage\nc : enrobage\n\n« 3 HA20 » → 3 barres à haute adhérence de 20 mm.\n« HA8 e = 15 » → cadres HA8 tous les 15 cm.\n\n💬 Lequel t'a posé problème au début ?"""),

    _post("J19_anatomie_poteau", "L'anatomie d'un poteau", "Pédagogie", "nuit", "Comprendre",
          [{"t": "cover", "title": "Ce qu'il y a / dans un **poteau**.", "sub": "Il ne fléchit presque pas. Mais il doit quand même être armé."},
           {"t": "text", "num": "01", "title": "Les barres / **verticales**.", "body": "Elles aident le béton à reprendre la compression, et empêchent le poteau de se déformer latéralement."},
           {"t": "text", "num": "02", "title": "Les **cadres**.", "body": "Ils confinent le béton et empêchent les barres verticales de flamber vers l'extérieur."},
           {"t": "text", "num": "03", "title": "Les zones / **critiques**.", "body": "En tête et en pied, les efforts se concentrent. Les cadres y sont nettement plus serrés."},
           {"t": "text", "num": "04", "title": "Les **recouvrements**.", "body": "Les barres se reprennent d'un niveau à l'autre. Jamais dans une zone critique."},
           {"t": "quote", "quote": "Un poteau se ruine rarement / par ses barres. / Presque toujours par ses cadres."}],
          "Ce qu'il y a vraiment dans un poteau 🔩 Et pourquoi les cadres comptent autant 👉",
          """L'anatomie d'un poteau en béton armé 🏗️\n\n1️⃣ Les barres verticales : la compression.\n2️⃣ Les cadres : ils confinent le béton et empêchent le flambement.\n3️⃣ Les zones critiques (tête et pied) : cadres resserrés.\n4️⃣ Les recouvrements : jamais dans une zone critique.\n\nUn poteau se ruine rarement par ses barres. Presque toujours par ses cadres.\n\n💬 Tu resserres sur quelle hauteur, toi ?"""),

    _post("J20_anatomie_dalle", "L'anatomie d'une dalle", "Pédagogie", "chaux", "Comprendre",
          [{"t": "cover", "title": "Ce qu'il y a / dans une **dalle**.", "sub": "Le plus grand élément du bâtiment, et le plus discret."},
           {"t": "text", "num": "01", "title": "Le sens de **portée**.", "body": "Tout commence là. Sur deux appuis, la dalle porte dans le sens de la petite portée."},
           {"t": "text", "num": "02", "title": "La nappe **inférieure**.", "body": "En travée, c'est le dessous qui est tendu. Les aciers principaux y vont."},
           {"t": "text", "num": "03", "title": "Les **chapeaux**.", "body": "Sur les appuis et en porte-à-faux, c'est le dessus qui est tendu."},
           {"t": "text", "num": "04", "title": "Les **cales**.", "body": "Sans elles, les aciers se retrouvent au fond du coffrage. Et la dalle perd sa hauteur utile."},
           {"t": "big", "big": "e", "body": "Une dalle, c'est surtout une **épaisseur** / bien respectée."}],
          "Une dalle, ça se ferraille dans quel sens ? 👉",
          """L'anatomie d'une dalle 🧱\n\n1️⃣ Le sens de portée : tout commence là.\n2️⃣ La nappe inférieure : le dessous est tendu en travée.\n3️⃣ Les chapeaux : le dessus est tendu sur appuis et en porte-à-faux.\n4️⃣ Les cales : sans elles, pas d'enrobage et pas de hauteur utile.\n\n💬 Combien de cales au m² sur tes chantiers ?"""),

    _post("J21_anatomie_semelle", "L'anatomie d'une semelle", "Pédagogie", "nuit", "Comprendre",
          [{"t": "cover", "title": "Ce qu'il y a / dans une **semelle**.", "sub": "Elle travaille à l'envers de tout le reste."},
           {"t": "text", "title": "Le sol pousse / **vers le haut**.", "body": "La charge descend par le poteau, le sol réagit par en dessous. La semelle fléchit comme un plateau porté en son centre."},
           {"t": "text", "title": "Donc la nappe / va **en bas**.", "body": "C'est la face inférieure qui est tendue. Les aciers principaux y sont, avec juste l'enrobage nécessaire."},
           {"t": "text", "title": "Les barres sont / **relevées** en bout.", "body": "Un retour vertical en extrémité assure l'ancrage, là où la barre est encore tendue."},
           {"t": "text", "title": "Le béton de / **propreté**.", "body": "Une fine couche coulée avant : elle isole l'acier de la terre et permet de garantir l'enrobage."},
           {"t": "quote", "quote": "Une fondation ratée / ne se répare pas. / Elle se démolit."}],
          "Une semelle travaille à l'envers d'une poutre. Tu sais pourquoi ? 👉",
          """L'anatomie d'une semelle isolée 🪨\n\n⬆️ Le sol pousse vers le haut : la face inférieure est tendue.\n⬇️ Donc la nappe principale va en partie basse.\n↪️ Les barres sont relevées en bout pour être ancrées.\n🧱 Et sous le tout : un béton de propreté.\n\nUne fondation ratée ne se répare pas. Elle se démolit.\n\n💬 Tu coules toujours un béton de propreté ?"""),

    _post("J22_enrobage", "L'enrobage, expliqué en 6 images", "Pédagogie", "chaux", "Le guide",
          [{"t": "cover", "title": "**L'enrobage** : / le centimètre / qui change tout.", "sub": "Invisible après le coulage. Décisif pendant 50 ans."},
           {"t": "text", "title": "C'est quoi ?", "body": "La distance entre la surface du béton et l'armature la plus proche. Mesurée depuis l'extérieur du cadre."},
           {"t": "text", "num": "01", "title": "Il protège de / la **rouille**.", "body": "Le béton est basique : il passive l'acier. Sans épaisseur suffisante, l'air et l'eau atteignent la barre."},
           {"t": "text", "num": "02", "title": "Il protège du / **feu**.", "body": "En cas d'incendie, c'est lui qui retarde l'échauffement de l'acier."},
           {"t": "text", "num": "03", "title": "Il assure / **l'adhérence**.", "body": "Il faut du béton tout autour de la barre pour que l'effort passe."},
           {"t": "text", "title": "Combien ?", "body": "Ça dépend de l'exposition : à l'abri, en extérieur, en bord de mer… La valeur se lit dans la norme et se fixe au projet."}],
          "L'enrobage : le centimètre invisible qui décide de la durée de vie 👉",
          """L'enrobage, expliqué simplement 📏\n\nC'est la distance entre la surface du béton et l'armature la plus proche.\n\n1️⃣ Il protège de la rouille (le béton passive l'acier).\n2️⃣ Il protège du feu.\n3️⃣ Il assure l'adhérence.\n\nCombien ? Ça dépend de l'exposition : à l'abri, dehors, bord de mer… La valeur se fixe au projet selon la norme.\n\n💬 Quelle valeur tu utilises le plus souvent ?"""),

    _post("J23_ancrage_recouvrement", "Ancrage et recouvrement", "Pédagogie", "nuit", "Le guide",
          [{"t": "cover", "title": "**Ancrage** et / **recouvrement** : / quelle différence ?", "sub": "Deux longueurs qu'on confond souvent."},
           {"t": "compare", "title": "Deux problèmes différents", "a_label": "Ancrage", "a": "Une barre tendue arrive au bout. Il faut qu'elle tienne dans le béton sans glisser.",
            "b_label": "Recouvrement", "b": "Deux barres se relaient. L'effort passe de l'une à l'autre, à travers le béton."},
           {"t": "text", "title": "Dans les deux cas : / de **l'adhérence**.", "body": "Rien n'est soudé, rien n'est vissé. C'est le frottement entre l'acier nervuré et le béton qui travaille."},
           {"t": "text", "title": "Donc la longueur / **dépend** de tout.", "body": "Du diamètre, de la nuance de l'acier, de la qualité du béton, de la position de la barre, et de l'enrobage."},
           {"t": "text", "title": "Les **crochets** / raccourcissent.", "body": "Un retour en bout de barre permet de réduire la longueur droite nécessaire."},
           {"t": "quote", "quote": "Une barre mal ancrée / n'est pas une barre faible. / C'est une barre absente."}],
          "Ancrage ou recouvrement ? La différence en 1 minute 👉",
          """Ancrage et recouvrement : deux choses différentes 🔩\n\n⚓ L'ancrage : une barre tendue arrive en bout, il faut qu'elle ne glisse pas.\n🔗 Le recouvrement : deux barres se relaient, l'effort passe de l'une à l'autre.\n\nDans les deux cas, tout repose sur l'adhérence. La longueur dépend du diamètre, de la nuance, du béton, de la position et de l'enrobage.\n\nUne barre mal ancrée, ce n'est pas une barre faible : c'est une barre absente.\n\n💬 Tu les retiens comment, ces longueurs ?"""),

    _post("J24_crochets_pliages", "Crochets et pliages", "Pédagogie", "chaux", "Le guide",
          [{"t": "cover", "title": "**Crochets** / et **pliages**.", "sub": "Le détail qui se voit à l'atelier, et qui compte sur le chantier."},
           {"t": "text", "title": "Pourquoi un / crochet à **135°** ?", "body": "Replié vers le cœur du béton, il empêche le cadre de s'ouvrir sous l'effort. Un retour à 90° peut se déplier."},
           {"t": "text", "title": "Le **rayon** / de pliage.", "body": "Plier trop serré fissure le béton à l'intérieur de l'angle et fragilise l'acier. Chaque diamètre a son rayon minimal."},
           {"t": "text", "title": "On ne **redresse** / pas une barre.", "body": "Une barre déjà pliée puis redressée a perdu une partie de ses qualités. Sur chantier, c'est un réflexe à perdre."},
           {"t": "text", "title": "Et on ne **chauffe** / pas non plus.", "body": "Chauffer un acier à haute adhérence modifie ses propriétés. Le pliage se fait à froid, en atelier."},
           {"t": "quote", "quote": "Un cadre ouvert, / c'est un cadre absent."}],
          "Pourquoi les crochets sont à 135° et pas à 90° ? 👉",
          """Crochets et pliages : les règles de l'atelier 🔧\n\n↩️ Le crochet à 135° replie l'extrémité vers le cœur du béton : le cadre ne peut plus s'ouvrir.\n⭕ Le rayon de pliage : plier trop serré fissure le béton et fragilise l'acier.\n🚫 On ne redresse pas une barre déjà pliée.\n🔥 On ne chauffe pas : le pliage se fait à froid.\n\n💬 Tu as déjà vu des cadres ouverts sur un chantier ?"""),

    _post("J25_effort_tranchant", "L'effort tranchant, sans formule", "Pédagogie", "nuit", "Comprendre",
          [{"t": "cover", "title": "**L'effort tranchant**, / expliqué sans / une seule formule.", "sub": "Pourquoi on resserre les cadres près des appuis."},
           {"t": "text", "title": "Imagine un jeu / de **cartes**.", "body": "Pose un paquet de cartes à plat entre deux appuis et appuie au milieu. Les cartes glissent les unes sur les autres."},
           {"t": "text", "title": "Dans une poutre, / c'est **pareil**.", "body": "Les tranches de béton tendent à glisser les unes par rapport aux autres. Ce glissement, c'est l'effort tranchant."},
           {"t": "text", "title": "Il est maximal / **aux appuis**.", "body": "Et presque nul au milieu de la travée. C'est l'inverse du moment de flexion."},
           {"t": "text", "title": "D'où les **cadres**.", "body": "Ils cousent les tranches entre elles. Plus l'effort est fort, plus il faut de coutures : donc des cadres resserrés."},
           {"t": "beam", "title": "Serré aux appuis, / espacé au **milieu**.", "spacing": "e variable", "body": "Un espacement constant sur toute la poutre, c'est le signe d'un plan non calculé."}],
          "L'effort tranchant expliqué avec un jeu de cartes 🃏 Glisse 👉",
          """L'effort tranchant, sans formule 🃏\n\nPose un paquet de cartes entre deux appuis et appuie au milieu : les cartes glissent les unes sur les autres.\n\nDans une poutre, c'est pareil : les tranches de béton tendent à glisser. Ce glissement, c'est l'effort tranchant.\n\n📍 Il est maximal aux appuis, presque nul au milieu.\n🔩 Les cadres cousent les tranches entre elles : on les resserre là où ça glisse le plus.\n\n💬 On te l'avait expliqué comment, à toi ?"""),

    _post("J26_4_etapes", "Les 4 étapes d'un plan de ferraillage", "Méthode", "chaux", "Méthode",
          [{"t": "cover", "title": "Un plan de ferraillage, / en **4 étapes**.", "sub": "De la note de calcul à la feuille qui part au chantier."},
           {"t": "steps", "title": "La chaîne complète", "steps": [["1. Dimensionner", "La section, les sollicitations, les sections d'acier nécessaires."],
                                                                   ["2. Choisir les barres", "Diamètres, nombre, répartition. Ce qui rentre dans la section."],
                                                                   ["3. Dessiner", "Élévation, coupes, cotes, repères. La partie la plus longue."],
                                                                   ["4. Nomenclature", "Longueurs, façonnages, quantités, poids."]]},
           {"t": "big", "big": "3 et 4", "body": "sont **répétitives** et **mécaniques**. / C'est exactement là que CivRebar AI intervient."},
           {"t": "text", "title": "L'étape 1 et 2 / restent à **toi**.", "body": "Le dimensionnement et le choix des armatures relèvent de l'ingénieur. L'outil ne décide pas à ta place."},
           {"t": "quote", "quote": "Automatiser le dessin, / pas le jugement."}],
          "Les 4 étapes d'un plan de ferraillage — et les 2 qu'on peut automatiser 👉",
          """Un plan de ferraillage, en 4 étapes 📐\n\n1️⃣ Dimensionner : sections, sollicitations, aciers nécessaires.\n2️⃣ Choisir les barres : diamètres, nombre, répartition.\n3️⃣ Dessiner : élévation, coupes, cotes, repères.\n4️⃣ Nomenclature : longueurs, façonnages, quantités.\n\nLes étapes 3 et 4 sont répétitives et mécaniques. C'est là que CivRebar AI intervient.\n\nLes étapes 1 et 2 restent à l'ingénieur. Automatiser le dessin, pas le jugement.\n\n💬 Laquelle te prend le plus de temps ?"""),

    _post("J27_nomenclature", "La nomenclature, à quoi ça sert", "Pédagogie", "nuit", "Comprendre",
          [{"t": "cover", "title": "La **nomenclature** : / le tableau que / personne ne regarde.", "sub": "Et pourtant, c'est lui qui part à l'atelier."},
           {"t": "fields", "ph": "NOMENCLATURE · POUTRE P4", "title": "À quoi ça ressemble", "fields": [("Repère 1", "3 HA20 — L = 5,60 m"), ("Repère 2", "2 HA14 — L = 5,60 m"),
                                                                                                        ("Repère 3", "28 HA8 — cadres"), ("Repère 4", "6 HA10 — épingles")]},
           {"t": "text", "title": "Le **repère** / fait le lien.", "body": "Un numéro unique relie le trait sur le plan, la ligne du tableau, et la barre façonnée en atelier."},
           {"t": "text", "title": "Elle sert à / **commander**.", "body": "Les longueurs et les poids servent au métré, à la commande d'acier, et à la facturation."},
           {"t": "text", "title": "Elle se **recalcule** / à chaque modif.", "body": "Une section qui change, et toutes les longueurs bougent. C'est la partie la plus pénible à tenir à jour à la main."},
           {"t": "big", "big": "0", "body": "erreur de recopie : / c'est ce qu'on vise avec une nomenclature **générée**."}],
          "La nomenclature : le tableau que personne ne regarde, et qui part à l'atelier 👉",
          """La nomenclature d'armatures, à quoi ça sert ? 📋\n\n🔗 Le repère fait le lien entre le plan, le tableau et la barre façonnée.\n📦 Les longueurs et les poids servent au métré et à la commande.\n🔄 Elle se recalcule à chaque modification de section.\n\nC'est la partie la plus pénible à tenir à jour à la main… et celle où les erreurs de recopie coûtent le plus cher.\n\n💬 Tu la fais comment, ta nomenclature ?"""),

    _post("J28_checklist2", "7 points à vérifier avant de rendre", "Pratique", "chaux", "Checklist",
          [{"t": "cover", "title": "**7 points** / avant de rendre / ton plan.", "sub": "Enregistre-le. Tu le reliras."},
           {"t": "text", "num": "01", "title": "Le bon **indice**.", "body": "Tu travailles bien sur la dernière version du coffrage ?"},
           {"t": "text", "num": "02", "title": "Le sens de **portée**.", "body": "Les aciers principaux vont-ils bien dans le sens où ça porte ?"},
           {"t": "text", "num": "03", "title": "Les **chapeaux**.", "body": "Sur chaque appui intermédiaire et chaque porte-à-faux."},
           {"t": "text", "num": "04", "title": "Les **espacements**.", "body": "Resserrés aux appuis ? Et un maximum respecté partout ?"},
           {"t": "text", "num": "05", "title": "Les **ancrages**.", "body": "Chaque barre tendue se termine-t-elle quelque part de solide ?"},
           {"t": "text", "num": "06", "title": "**L'encombrement**.", "body": "Les barres rentrent-elles vraiment dans la section, avec l'enrobage et les cadres ?"},
           {"t": "text", "num": "07", "title": "La **nomenclature**.", "body": "Repères uniques, longueurs cohérentes, total qui tombe juste."}],
          "7 points à vérifier avant de rendre un plan de ferraillage ✅ Enregistre 📌",
          """7 points à vérifier avant de rendre ton plan ✅\n\n1️⃣ Le bon indice de coffrage\n2️⃣ Le sens de portée\n3️⃣ Les chapeaux sur appuis et porte-à-faux\n4️⃣ Les espacements (resserrés aux appuis)\n5️⃣ Les ancrages en bout de barre\n6️⃣ L'encombrement réel dans la section\n7️⃣ La nomenclature : repères uniques, total juste\n\n📌 Enregistre ce carrousel pour ton prochain plan.\n\n💬 Il t'en manque un ? Ajoute-le en commentaire."""),

    _post("J29_cout_du_temps", "Ce que coûte vraiment le dessin", "Problème", "nuit", "Le constat",
          [{"t": "cover", "title": "Combien de temps / tu passes à **dessiner** ?", "sub": "Faisons le calcul ensemble."},
           {"t": "big", "big": "80 %", "body": "du temps d'un plan de ferraillage, / c'est du **dessin**. Pas du calcul."},
           {"t": "text", "title": "Une poutre : / **30 à 60 minutes**.", "body": "Élévation, coupes, cadres, cotes, repères, nomenclature. Sans compter les reprises."},
           {"t": "text", "title": "Un niveau courant : / **20 à 40 poutres**.", "body": "Fais la multiplication. Puis ajoute les poteaux, les dalles et les semelles."},
           {"t": "text", "title": "Et à chaque / **modification**…", "body": "Une section qui change, une portée revue, et il faut reprendre le dessin et la nomenclature."},
           {"t": "quote", "quote": "Le temps passé à dessiner / n'est pas du temps / passé à concevoir."}],
          "80 % du temps d'un plan de ferraillage, c'est du dessin. Pas du calcul 😮‍💨👉",
          """Ce que coûte vraiment le dessin de ferraillage ⏳\n\n📊 80 % du temps d'un plan, c'est du dessin. Pas du calcul.\n⏱️ Une poutre : 30 à 60 minutes.\n🏢 Un niveau courant : 20 à 40 poutres. Puis les poteaux, les dalles, les semelles.\n🔄 Et à chaque modification, on reprend tout.\n\nLe temps passé à dessiner n'est pas du temps passé à concevoir.\n\n💬 Combien de temps pour une poutre, chez toi ?"""),

    _post("J30_v1", "Ce que fait la première version", "Produit", "chaux", "Le produit",
          [{"t": "cover", "title": "Ce que fait / la **première version**.", "sub": "Sans promesse en l'air. Voilà l'état réel."},
           {"t": "fields", "title": "Tu renseignes", "fields": [("Section", "30 × 60 cm"), ("Portée", "5,40 m"), ("Armatures", "3 HA20 / 2 HA14"), ("Cadres", "HA8")], "button": "Dessiner"},
           {"t": "text", "title": "Il dessine / **l'élévation**.", "body": "Barres filantes, chapeaux, cadres répartis, dans le bon sens et à la bonne échelle."},
           {"t": "text", "title": "Il dessine / les **coupes**.", "body": "Section, position des barres, cadres, enrobage respecté."},
           {"t": "text", "title": "Il pose / **cotes et repères**.", "body": "Cotation complète et repères numérotés, prêts pour la nomenclature."},
           {"t": "big", "big": "La poutre", "body": "D'abord. Le reste suit : **poteaux**, dalles, semelles, escaliers."}],
          "Ce que fait réellement la v1 de CivRebar AI 🔩 Sans promesse en l'air 👉",
          """Ce que fait la première version de CivRebar AI 🔩\n\n📝 Tu renseignes : section, portée, armatures, cadres.\n📐 Il dessine l'élévation : barres, chapeaux, cadres répartis.\n✂️ Il dessine les coupes : section, barres, enrobage.\n🏷️ Il pose les cotes et les repères.\n\nOn commence par la poutre. Les poteaux, dalles, semelles et escaliers suivront.\n\n💬 Par quel élément tu voudrais qu'on continue ?"""),

    _post("J31_ce_qu_il_ne_fera_pas", "Ce qu'il ne fera jamais", "Confiance", "nuit", "Notre limite",
          [{"t": "cover", "title": "Ce que CivRebar AI / ne fera **jamais**.", "sub": "Une promesse tient aussi à ce qu'elle refuse."},
           {"t": "text", "num": "01", "title": "Il ne **signera** / pas ton plan.", "body": "La signature engage une responsabilité. Elle est, et restera, celle de l'ingénieur."},
           {"t": "text", "num": "02", "title": "Il ne **décidera** / pas à ta place.", "body": "Le choix des sections et des armatures relève de ton jugement et de la note de calcul."},
           {"t": "text", "num": "03", "title": "Il ne **remplacera** / pas la norme.", "body": "Les valeurs se calculent selon le règlement applicable et les choix du projet."},
           {"t": "text", "num": "04", "title": "Il ne **masquera** / pas ses limites.", "body": "Ce qu'il ne sait pas faire, il te le dira. C'est la condition pour qu'on puisse lui faire confiance."},
           {"t": "quote", "quote": "L'outil dessine. / L'ingénieur décide, / et signe le plan."}],
          "Ce que CivRebar AI ne fera jamais. Et pourquoi c'est une bonne nouvelle 👉",
          """Ce que CivRebar AI ne fera jamais 🚫\n\n1️⃣ Signer ton plan : la responsabilité reste celle de l'ingénieur.\n2️⃣ Décider à ta place : les sections et armatures relèvent de ton jugement.\n3️⃣ Remplacer la norme : les valeurs se calculent selon le règlement applicable.\n4️⃣ Masquer ses limites : ce qu'il ne sait pas faire, il le dira.\n\nL'outil dessine. L'ingénieur décide, et signe.\n\n💬 Qu'est-ce qui te ferait confiance dans un outil comme ça ?"""),

    _post("J32_autolisp", "AutoLISP, c'est quoi ?", "Technique", "chaux", "Sous le capot",
          [{"t": "cover", "title": "**AutoLISP** : / le langage caché / d'AutoCAD.", "sub": "C'est avec lui que tout a commencé."},
           {"t": "text", "title": "Un langage **dans** / le logiciel.", "body": "AutoCAD sait exécuter des programmes écrits en AutoLISP. Pas besoin d'installer autre chose."},
           {"t": "text", "title": "Il dessine / comme **toi**.", "body": "Il place des lignes, des cercles, des cotes et des textes : exactement les mêmes entités que celles que tu crées à la main."},
           {"t": "text", "title": "Donc le résultat / est **modifiable**.", "body": "Rien n'est figé, rien n'est une image. Tu peux reprendre chaque trait après coup."},
           {"t": "text", "title": "Et c'est / **gratuit**.", "body": "Pas de licence supplémentaire, pas d'abonnement en plus : le langage est inclus dans AutoCAD."},
           {"t": "big", "big": "→ Plugin", "body": "L'AutoLISP est l'étape 1. / Le **plugin** viendra ensuite, puis l'IA."}],
          "AutoLISP : le langage caché d'AutoCAD, et le point de départ de CivRebar 👉",
          """AutoLISP, c'est quoi ? 💻\n\n🔧 Un langage de programmation intégré à AutoCAD.\n✏️ Il crée les mêmes entités que toi : lignes, cercles, cotes, textes.\n🔄 Donc tout reste modifiable à la main après coup.\n💰 Et il est inclus : pas de licence en plus.\n\nC'est l'étape 1 de CivRebar AI. Le plugin viendra ensuite, puis l'intelligence.\n\n💬 Tu as déjà écrit un petit LISP pour gagner du temps ?"""),

    _post("J33_pourquoi_autocad", "Pourquoi AutoCAD et pas autre chose", "Produit", "nuit", "Notre choix",
          [{"t": "cover", "title": "Pourquoi **AutoCAD** ?", "sub": "On aurait pu faire un logiciel à part. On a choisi l'inverse."},
           {"t": "text", "num": "01", "title": "Parce que tu / l'as **déjà**.", "body": "Rien à installer de lourd, rien à réapprendre. L'outil vient à toi, pas l'inverse."},
           {"t": "text", "num": "02", "title": "Parce que le plan / reste **modifiable**.", "body": "Le dessin produit est un dessin AutoCAD normal. Tu peux tout reprendre."},
           {"t": "text", "num": "03", "title": "Parce que c'est / le **standard**.", "body": "Le fichier part au bureau de contrôle, à l'entreprise, à l'atelier. Tout le monde sait l'ouvrir."},
           {"t": "text", "num": "04", "title": "Parce qu'on reste / dans ton **flux**.", "body": "Pas d'export, pas d'import, pas de conversion. Tu ne quittes pas ton dessin."},
           {"t": "quote", "quote": "Le meilleur outil, / c'est celui qu'on n'a pas / besoin d'adopter."}],
          "Pourquoi CivRebar vit dans AutoCAD, et pas ailleurs 👉",
          """Pourquoi AutoCAD, et pas un logiciel à part ? 🤔\n\n1️⃣ Parce que tu l'as déjà : rien à réapprendre.\n2️⃣ Parce que le plan produit reste modifiable.\n3️⃣ Parce que c'est le standard : tout le monde sait l'ouvrir.\n4️⃣ Parce que tu ne quittes pas ton flux de travail.\n\nLe meilleur outil, c'est celui qu'on n'a pas besoin d'adopter.\n\n💬 Tu travailles sur quoi, toi ?"""),

    _post("J34_avant_apres", "Avant / après", "Produit", "chaux", "La différence",
          [{"t": "cover", "title": "La même poutre. / Deux **méthodes**.", "sub": "Ce qui change, concrètement."},
           {"t": "compare", "title": "Le même résultat, pas le même chemin", "a_label": "À la main", "a": "30 à 60 minutes. Élévation, coupes, cadres un par un, cotes, repères, nomenclature.",
            "b_label": "Avec CivRebar", "b": "Tu renseignes la section, la portée et les armatures. Le reste se dessine."},
           {"t": "text", "title": "Ce qui **ne change pas**.", "body": "Le résultat : un dessin AutoCAD normal, modifiable, coté, aux mêmes conventions que les tiens."},
           {"t": "text", "title": "Ce qui **change**.", "body": "Le temps. Et le nombre de reprises après une modification de section."},
           {"t": "big", "big": "×", "body": "Le gain n'est pas sur **une** poutre. / Il est sur les **quarante** suivantes."}],
          "La même poutre, deux méthodes. Ce qui change vraiment 👉",
          """Avant / après : la même poutre, deux méthodes 📐\n\n✍️ À la main : 30 à 60 minutes. Élévation, coupes, cadres un par un, cotes, repères, nomenclature.\n⚡ Avec CivRebar : tu renseignes la section, la portée et les armatures. Le reste se dessine.\n\nCe qui ne change pas : le résultat reste un dessin AutoCAD normal et modifiable.\nCe qui change : le temps, et les reprises après modification.\n\nLe gain n'est pas sur une poutre. Il est sur les quarante suivantes.\n\n💬 Combien de poutres sur ton dernier projet ?"""),

    _post("J35_faq", "Vos questions, nos réponses", "Confiance", "nuit", "FAQ",
          [{"t": "cover", "title": "Vos **questions**, / nos réponses.", "sub": "Les cinq qui reviennent le plus souvent."},
           {"t": "compare", "title": "« C'est quelle norme ? »", "a_label": "La question", "a": "Sur quel règlement se base l'outil ?",
            "b_label": "La réponse", "b": "Les valeurs restent paramétrables : c'est le projet qui fixe le règlement applicable, pas l'outil."},
           {"t": "compare", "title": "« Ça coûte combien ? »", "a_label": "La question", "a": "Quel sera le prix ?",
            "b_label": "La réponse", "b": "Le modèle n'est pas encore arrêté. Les premiers testeurs seront prévenus en premier."},
           {"t": "compare", "title": "« C'est pour quand ? »", "a_label": "La question", "a": "Quand est-ce que je peux l'utiliser ?",
            "b_label": "La réponse", "b": "La poutre d'abord. On avance par élément, et on montre chaque étape ici."},
           {"t": "compare", "title": "« Et si je modifie après ? »", "a_label": "La question", "a": "Le dessin est-il figé ?",
            "b_label": "La réponse", "b": "Non. C'est un dessin AutoCAD normal : chaque trait reste modifiable."}],
          "Vos 4 questions les plus fréquentes sur CivRebar AI, et nos réponses 👉",
          """Vos questions, nos réponses 💬\n\n❓ « C'est quelle norme ? » → Les valeurs restent paramétrables : c'est le projet qui fixe le règlement.\n❓ « Ça coûte combien ? » → Le modèle n'est pas encore arrêté. Les testeurs seront prévenus en premier.\n❓ « C'est pour quand ? » → La poutre d'abord. On avance par élément, et on montre tout ici.\n❓ « Et si je modifie après ? » → C'est un dessin AutoCAD normal, entièrement modifiable.\n\n💬 Ta question n'y est pas ? Pose-la."""),

    _post("J36_poteau_court", "Le poteau court, ce piège discret", "Pédagogie", "chaux", "Comprendre",
          [{"t": "cover", "title": "Le **poteau court** : / le piège qu'on / dessine sans le voir.", "sub": "Une allège, et tout change."},
           {"t": "text", "title": "Un poteau normal / **fléchit**.", "body": "Sur toute sa hauteur. Les efforts se répartissent, les cadres habituels suffisent."},
           {"t": "text", "title": "Bride-le, et il / devient **raide**.", "body": "Une allège maçonnée collée au poteau l'empêche de bouger sur une partie de sa hauteur."},
           {"t": "text", "title": "Alors tout se / concentre sur / la partie **libre**.", "body": "Même déplacement, mais sur une hauteur bien plus courte : l'effort tranchant devient très élevé."},
           {"t": "text", "title": "Deux **solutions**.", "body": "Soit on resserre fortement les cadres sur la partie libre. Soit on désolidarise l'allège du poteau par un joint."},
           {"t": "quote", "quote": "Ce n'est pas le poteau / qui a changé. / C'est ce qu'on a mis autour."}],
          "Le poteau court : une allège, et le poteau devient dangereux 👉",
          """Le poteau court, ce piège discret 🏗️\n\n🔵 Un poteau normal fléchit sur toute sa hauteur.\n🧱 Bride-le avec une allège maçonnée : il ne peut plus bouger que sur une courte hauteur.\n⚡ Résultat : l'effort tranchant y devient très élevé. C'est une cause classique de rupture.\n\nDeux solutions : resserrer fortement les cadres sur la partie libre, ou désolidariser l'allège par un joint.\n\n💬 Tu en as déjà repéré sur un chantier ?"""),

    _post("J37_tremies", "Trémies et réservations", "Pédagogie", "nuit", "Le guide",
          [{"t": "cover", "title": "**Trémies** et / réservations.", "sub": "Un trou dans une dalle, ça ne s'improvise pas."},
           {"t": "text", "title": "Une trémie / **coupe** des barres.", "body": "Et une barre coupée ne porte plus rien. Il faut remplacer ce qu'on a enlevé."},
           {"t": "text", "title": "Des barres de / **chevêtre**.", "body": "Sur les quatre côtés de l'ouverture : elles reprennent ce que les barres coupées transportaient."},
           {"t": "text", "title": "Des barres en / **diagonale**.", "body": "Aux angles. C'est de là que partent les fissures, parce que l'effort y change brutalement de direction."},
           {"t": "text", "title": "Et pour les / **petites** trémies ?", "body": "En dessous d'une certaine taille, on peut souvent écarter les barres sans les couper. Au-delà, il faut un renfort."},
           {"t": "quote", "quote": "Une réservation oubliée / se perce après coup. / Et là, c'est pire."}],
          "Comment ferrailler autour d'une trémie dans une dalle 👉",
          """Trémies et réservations : les règles 🕳️\n\n✂️ Une trémie coupe des barres. Une barre coupée ne porte plus rien.\n🔲 Des barres de chevêtre sur les quatre côtés remplacent ce qui a été enlevé.\n↗️ Des barres en diagonale aux angles : c'est là que partent les fissures.\n📏 Pour les petites trémies, on peut souvent écarter les barres sans les couper.\n\nUne réservation oubliée se perce après coup. Et là, c'est pire.\n\n💬 Tu les anticipes comment, les réservations ?"""),

    _post("J38_du_plan_au_chantier", "Du plan au chantier : qui lit quoi", "Métier", "chaux", "Le circuit",
          [{"t": "cover", "title": "Ton plan part. / Qui va le **lire** ?", "sub": "Quatre métiers, quatre lectures différentes."},
           {"t": "steps", "title": "Le parcours d'un plan", "steps": [["Le bureau de contrôle", "Il vérifie les hypothèses, les sections, la conformité."],
                                                                      ["Le métreur", "Il lit la nomenclature : longueurs, poids, quantités à commander."],
                                                                      ["L'atelier de façonnage", "Il lit les repères et les schémas de pliage. Il ne voit pas la poutre."],
                                                                      ["Le ferrailleur", "Il lit l'élévation et les coupes, sur le chantier, parfois sous la pluie."]]},
           {"t": "text", "title": "Un plan clair / n'est pas un **luxe**.", "body": "Chacun de ces métiers lit vite, dans de mauvaises conditions. Ce qui est ambigu sera interprété."},
           {"t": "text", "title": "Le **repère** / est la clé.", "body": "C'est le seul lien entre ces quatre lectures. S'il est faux ou dupliqué, toute la chaîne se casse."},
           {"t": "quote", "quote": "Tu ne dessines pas pour toi. / Tu dessines pour celui / qui posera la barre."}],
          "Ton plan part. Qui va vraiment le lire ? 4 métiers, 4 lectures 👉",
          """Du plan au chantier : qui lit quoi ? 🔄\n\n🔍 Le bureau de contrôle : hypothèses, sections, conformité.\n📊 Le métreur : la nomenclature, les quantités à commander.\n🔧 L'atelier : les repères et les schémas de pliage. Il ne voit jamais la poutre.\n👷 Le ferrailleur : l'élévation et les coupes, sur le chantier.\n\nLe repère est le seul lien entre ces quatre lectures.\n\nTu ne dessines pas pour toi. Tu dessines pour celui qui posera la barre.\n\n💬 Tu as déjà eu un retour de chantier sur un plan ambigu ?"""),

    _post("J39_symbole", "Les quatre parties de notre symbole", "Marque", "nuit", "La marque",
          [{"t": "cover", "title": "Notre **symbole**, / pièce par pièce.", "sub": "Quatre éléments, quatre idées."},
           {"t": "symbol", "focus": "fut", "num": "01", "title": "Le **fût**.", "body": "La barre droite, verticale. C'est l'acier brut, avant toute transformation."},
           {"t": "symbol", "focus": "panse", "num": "02", "title": "La **panse**.", "body": "La courbe du R. C'est le pliage : le moment où la barre devient une armature."},
           {"t": "symbol", "focus": "crochet", "num": "03", "title": "Le **crochet**.", "body": "Le retour en bas. C'est l'ancrage : ce qui fait que la barre tient dans le béton."},
           {"t": "symbol", "focus": "noeud", "num": "04", "title": "Le **nœud**.", "body": "Le point cyan. C'est l'intelligence : le calcul qui décide de tout le reste."},
           {"t": "symbol", "focus": "tout", "title": "Un **R** façonné.", "body": "R comme Rebar. Et comme Rigueur."}],
          "Notre logo n'est pas un R. C'est une barre d'acier façonnée 🔩 Glisse 👉",
          """Les quatre parties de notre symbole 🔩\n\n1️⃣ Le fût : la barre droite, l'acier brut.\n2️⃣ La panse : la courbe, le pliage qui fait l'armature.\n3️⃣ Le crochet : le retour, l'ancrage dans le béton.\n4️⃣ Le nœud cyan : l'intelligence, le calcul.\n\nUn R façonné. R comme Rebar. Et comme Rigueur.\n\n💬 Tu l'avais vu, le parcours de la barre ?"""),

    _post("J40_quiz2", "Quiz : le sens de portée", "Interaction", "chaux", "Quiz",
          [{"t": "cover", "title": "**Quiz** : / dans quel sens / porte cette dalle ?", "sub": "Une dalle rectangulaire sur deux appuis. Réponds avant de glisser."},
           {"t": "text", "title": "L'énoncé", "body": "Une dalle de 3,00 m sur 6,00 m, appuyée uniquement sur ses deux grands côtés. Dans quel sens vont les aciers principaux ?"},
           {"t": "big", "big": "?", "body": "Dans le sens des **3 m** / ou dans le sens des **6 m** ?"},
           {"t": "text", "title": "La réponse", "body": "Dans le sens des 3,00 m. C'est la distance entre les deux appuis : c'est elle que la dalle doit franchir."},
           {"t": "text", "title": "Pourquoi / on se **trompe**.", "body": "On a tendance à suivre la plus grande dimension du rectangle. Mais ce qui compte, c'est la distance d'appui à appui."},
           {"t": "quote", "quote": "Une dalle porte / dans le sens où elle / n'a rien en dessous."}],
          "QUIZ 🧠 Dalle de 3 × 6 m sur deux appuis : les aciers vont dans quel sens ? 👉",
          """QUIZ : le sens de portée 🧠\n\nUne dalle de 3,00 m × 6,00 m, appuyée uniquement sur ses deux grands côtés.\n\nLes aciers principaux vont dans quel sens ?\n\n👉 Réponse : dans le sens des 3,00 m, la distance entre les deux appuis.\n\nL'erreur classique : suivre la plus grande dimension du rectangle au lieu de la distance d'appui à appui.\n\n💬 Tu avais bon ?"""),

    _post("J41_erreurs_couteuses", "Les 5 erreurs les plus coûteuses", "Pédagogie", "nuit", "Le classement",
          [{"t": "cover", "title": "Les **5 erreurs** / les plus coûteuses.", "sub": "Classées par ce qu'elles coûtent à réparer."},
           {"t": "text", "num": "01", "title": "L'acier du / **mauvais côté**.", "body": "Console, soutènement, radier : si l'acier est côté comprimé, l'élément est à refaire. Pas à réparer."},
           {"t": "text", "num": "02", "title": "**L'enrobage** / insuffisant.", "body": "Ça ne se voit qu'après des années. Puis le béton éclate, et c'est tout un ouvrage à reprendre."},
           {"t": "text", "num": "03", "title": "Les **chapeaux** / oubliés.", "body": "Sur un appui ou un porte-à-faux : fissuration immédiate, parfois rupture."},
           {"t": "text", "num": "04", "title": "Les cadres / **mal répartis**.", "body": "Une rupture par effort tranchant est brutale et sans signe avant-coureur."},
           {"t": "text", "num": "05", "title": "Les **ancrages** / absents.", "body": "La barre glisse, la fissure s'ouvre à l'about. Difficile et coûteux à réparer."},
           {"t": "quote", "quote": "Une erreur de plan coûte des heures. / Une erreur de chantier / coûte un ouvrage."}],
          "Les 5 erreurs de ferraillage les plus coûteuses, classées 👉",
          """Les 5 erreurs les plus coûteuses ⚠️\n\n1️⃣ L'acier du mauvais côté (console, soutènement, radier) : à refaire, pas à réparer.\n2️⃣ L'enrobage insuffisant : ça se voit après des années, et le béton éclate.\n3️⃣ Les chapeaux oubliés : fissuration immédiate, parfois rupture.\n4️⃣ Les cadres mal répartis : rupture brutale, sans signe avant-coureur.\n5️⃣ Les ancrages absents : la barre glisse, la fissure s'ouvre.\n\nUne erreur de plan coûte des heures. Une erreur de chantier coûte un ouvrage.\n\n💬 Laquelle tu as déjà rencontrée ?"""),

    _post("J42_bilan", "Un mois de publications", "Communauté", "chaux", "Le bilan",
          [{"t": "cover", "title": "Un **mois** / ensemble.", "sub": "Ce qu'on a partagé, et ce qui arrive."},
           {"t": "steps", "title": "Ce qu'on a couvert", "steps": [["Les bases", "Acier et béton, vocabulaire, lecture de plan."],
                                                                   ["L'anatomie", "Poutre, poteau, dalle, semelle : ce qu'il y a dedans."],
                                                                   ["Les règles", "Enrobage, ancrage, recouvrement, crochets, pliages."],
                                                                   ["Les pièges", "Un défi « Trouve l'erreur » chaque soir."]]},
           {"t": "text", "title": "Et le **projet** / a avancé.", "body": "La poutre fonctionne. Tonton Ferraille est né. Et on a commencé à montrer le dessin automatique en action."},
           {"t": "text", "title": "Ce qui arrive / **ensuite**.", "body": "Les poteaux, les dalles, les semelles. Puis le passage de l'AutoLISP au plugin."},
           {"t": "big", "big": "Merci", "body": "Pour chaque commentaire, chaque partage, / et chaque **erreur trouvée**."}],
          "Un mois de publications : le bilan, et la suite 🔩👉",
          """Un mois ensemble 🙏\n\n📚 Les bases : acier et béton, vocabulaire, lecture de plan.\n🔩 L'anatomie : poutre, poteau, dalle, semelle.\n📏 Les règles : enrobage, ancrage, recouvrement, crochets.\n🔍 Les pièges : un défi « Trouve l'erreur » chaque soir.\n\nEt le projet a avancé : la poutre fonctionne, Tonton Ferraille est né.\n\nEnsuite : les poteaux, les dalles, les semelles. Puis le plugin.\n\n💬 Quel sujet tu veux qu'on traite le mois prochain ?"""),

    _post("J43_testeurs", "Rejoins les premiers testeurs", "Conversion", "nuit", "L'invitation",
          [{"t": "cover", "title": "On cherche / les **premiers** / testeurs.", "sub": "Pas des spectateurs. Des gens qui dessinent vraiment."},
           {"t": "text", "title": "Pourquoi **toi** ?", "body": "Un outil de ferraillage ne se valide pas en laboratoire. Il se valide sur des plans réels, avec de vraies contraintes."},
           {"t": "text", "title": "Ce qu'on te / **demandera**.", "body": "Tester sur une poutre de ton choix, et nous dire ce qui ne va pas. Franchement."},
           {"t": "text", "title": "Ce que tu / y **gagnes**.", "body": "L'accès avant tout le monde, et une vraie influence sur ce que devient l'outil."},
           {"t": "text", "title": "Comment / **participer** ?", "body": "Écris-nous « TESTEUR » en message privé, ou en commentaire. On revient vers toi."},
           {"t": "big", "big": "TESTEUR", "body": "Un mot. En message ou en commentaire. / Et on **t'écrit**."}],
          "On cherche les premiers testeurs de CivRebar AI. Écris « TESTEUR » 📩👉",
          """On cherche les premiers testeurs 🔩\n\nPas des spectateurs : des gens qui dessinent vraiment du ferraillage.\n\n🎯 Ce qu'on te demandera : tester sur une poutre de ton choix, et nous dire franchement ce qui ne va pas.\n🎁 Ce que tu y gagnes : l'accès avant tout le monde, et une vraie influence sur l'outil.\n\n📩 Écris « TESTEUR » en message privé ou en commentaire. On revient vers toi.\n\n💬 Tu dessines quoi en ce moment ?"""),
]
