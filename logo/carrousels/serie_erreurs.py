"""Série « Trouve l'erreur » : un défi chaque soir à 20 h, 14 numéros.

Même structure pour chaque numéro : accroche, plan fautif, indice, réponse entourée,
pourquoi, bon plan, lien avec CivRebar AI, appel à l'action. Les dessins sont dans defauts.py
(le n° 1 utilise le modèle « plan » de carrousels.py). Les règles sont énoncées comme des
principes : les valeurs réelles se calculent selon la norme et le projet.
"""


def trouve_erreur(n, key, sujet, indice, rep, rep_body, pq_title, pq_body, ok, ok_body, accroche, diagramme=False, plan=False):
    typ = "plan" if plan else "scn"

    def dessin(mode, tag, title, body):
        d = {"t": typ, "mode": mode, "tag": tag, "title": title, "body": body}
        if not plan:
            d["key"] = key
        return d

    if plan and diagramme:
        pourquoi = dessin("tranchant", "Pourquoi ?", pq_title, pq_body)
    elif diagramme:
        pourquoi = dessin("pourquoi", "Pourquoi ?", pq_title, pq_body)
    else:
        pourquoi = {"t": "text", "title": pq_title, "body": pq_body}
    return {
        "id": f"TE{n:02d}_{key}", "titre": f"Trouve l'erreur n° {n}", "objectif": "Défi du soir",
        "theme": "nuit" if n % 2 else "chaux", "kicker": f"Trouve l'erreur · n° {n}", "hashtags": ["#TrouveLErreur"],
        "slides": [
            {"t": "cover", "title": "Trouve **l'erreur** / sur ce plan.", "sub": f"{sujet} Un seul détail cloche. Réponds en commentaire avant de glisser."},
            dessin("erreur", "Le plan", "Tu as trouvé ?", "Écris ta réponse en commentaire, puis glisse."),
            {"t": "text", "title": "Un indice ?", "body": indice},
            dessin("reponse", "Réponse", rep, rep_body),
            pourquoi,
            dessin("correct", "Le bon plan", ok, ok_body),
            {"t": "text", "title": "Ce genre de détail, / CivRebar AI t'aidera / à le **repérer**.",
             "body": "Les vérifications font partie de notre feuille de route. Un nouveau défi chaque soir à 20 h."},
            {"t": "cta", "title": "Tu avais **trouvé** ?", "body": "Dis-le en commentaire, et abonne-toi pour le défi de demain.",
             "actions": ["Commente", "Partage", "Abonne-toi"]},
        ],
        "court": f"🔍 TROUVE L'ERREUR n° {n} : {accroche} Réponds en commentaire AVANT de glisser 👀",
        "legende": f"""🔍 TROUVE L'ERREUR — n° {n}

{sujet} Un seul détail cloche.

💬 Écris ta réponse en commentaire AVANT de regarder la solution 👀

Un nouveau défi chaque soir à 20 h. Abonne-toi pour ne pas le rater 🔩""",
    }


ERREURS = [
    trouve_erreur(1, "cadres", "Poutre sur deux appuis, charge répartie.",
                  "Demande-toi où l'**effort tranchant** est le plus fort sur cette poutre.",
                  "Les cadres sont serrés / au **mauvais endroit**.", "Espacés de 25 cm près des appuis, serrés à 10 cm au milieu : c'est l'inverse qu'il faut.",
                  "L'effort tranchant", "Sur une poutre sur deux appuis, il est **maximal aux appuis** et presque nul au milieu. Or ce sont les cadres qui le reprennent.",
                  "Serrés aux **appuis**, / plus espacés au milieu.", "Exemple de principe : les espacements réels se calculent selon les charges et la norme.",
                  "un seul détail cloche sur ce plan de poutre.", diagramme=True, plan=True),
    trouve_erreur(2, "barres_haut", "Poutre sur deux appuis, charge répartie.",
                  "Sur cette poutre, quelle face est **tendue** : le haut ou le bas ?",
                  "Les grosses barres / sont **en haut**.", "Les 3 HA20 sont en haut, les 2 HA14 en bas : c'est l'inverse qu'il faut.",
                  "Le moment fléchissant", "Sur deux appuis, la poutre fléchit vers le bas : c'est la **fibre inférieure** qui est tendue. Le béton ne résiste pas à la traction, l'acier si.",
                  "L'acier principal / **en bas**.", "Les barres les plus fortes là où le béton est tendu.",
                  "une poutre, deux appuis, un détail qui cloche.", diagramme=True),
    trouve_erreur(3, "console", "Console (balcon) encastrée dans un mur.",
                  "Une console plie vers le bas… quelle face **s'allonge** ?",
                  "L'acier principal / est **en bas**.", "Sur une console, c'est l'une des erreurs les plus dangereuses : le balcon peut s'effondrer.",
                  "La console travaille / à l'envers", "Encastrée dans le mur, elle est tendue **en haut**. L'acier principal doit y être, bien ancré dans le mur.",
                  "Acier principal **en haut**, / ancré dans le mur.", "Les barres du dessous servent surtout au montage.",
                  "ce balcon cache une erreur dangereuse.", diagramme=True),
    trouve_erreur(4, "enrobage", "Coupe d'une poutre, juste avant le bétonnage.",
                  "Regarde la distance entre l'acier et la **surface** du béton.",
                  "Les barres touchent / le **coffrage**.", "Enrobage nul : l'acier sera à nu dès le décoffrage.",
                  "Pourquoi c'est grave", "Sans béton autour, l'acier rouille, gonfle et fait éclater le béton. En cas d'incendie, il chauffe trop vite. L'enrobage minimal dépend de l'exposition : voir la norme.",
                  "Un **enrobage** / tout autour.", "Des cales entre l'acier et le coffrage garantissent l'enrobage prévu au plan.",
                  "une coupe de poutre, un détail invisible après coulage."),
    trouve_erreur(5, "crochets", "Coupe d'une poutre : un cadre et ses barres.",
                  "Regarde bien le **coin en haut à gauche** du cadre.",
                  "Le cadre / est **ouvert**.", "Ses extrémités s'arrêtent sans crochet : il peut s'ouvrir sous l'effort.",
                  "Un cadre doit rester fermé", "Les crochets à **135°** replient les extrémités vers le cœur du béton : le cadre reste fermé et tient les barres, même en cas de séisme.",
                  "Fermé par des / crochets à **135°**.", "Le détail que seuls les gens du métier remarquent.",
                  "regarde bien ce cadre."),
    trouve_erreur(6, "recouvrement", "Deux barres HA16 raboutées dans une poutre.",
                  "Pour que l'effort passe d'une barre à l'autre, il faut de la **longueur**.",
                  "Le recouvrement / est **trop court**.", "10 cm de chevauchement : la barre peut glisser, l'effort ne passe pas.",
                  "Comment l'effort passe", "Par adhérence au béton, sur toute la longueur de chevauchement. On compte en général **40 à 50 fois le diamètre**, selon le béton, l'acier et la norme.",
                  "Un recouvrement / d'environ **50 Ø**.", "Pour un HA16 : de l'ordre de 65 à 80 cm.",
                  "deux barres, un raccord qui ne tiendra pas."),
    trouve_erreur(7, "attentes", "Un poteau qui doit continuer à l'étage au-dessus.",
                  "Comment le poteau de l'étage supérieur va-t-il se **raccorder** ?",
                  "Il n'y a pas / d'**attentes**.", "Les barres s'arrêtent au niveau du plancher : le poteau du dessus ne sera pas relié.",
                  "À quoi servent les attentes", "Ce sont les barres qui dépassent, en attente du niveau suivant. Elles assurent la **continuité** : sans elles, le poteau supérieur est simplement posé.",
                  "Des attentes sur une / longueur de **recouvrement**.", "Elles se chevauchent avec les barres du poteau supérieur.",
                  "ce poteau va poser problème à l'étage."),
    trouve_erreur(8, "semelle", "Semelle isolée sous un poteau.",
                  "Le sol pousse sous la semelle : quelle face est **tendue** ?",
                  "La nappe / est **en haut**.", "Placée en partie haute, elle ne sert presque à rien.",
                  "La semelle fléchit", "Le poteau appuie au centre, le sol repousse partout : la semelle se cintre et son **bas est tendu**.",
                  "La nappe **en bas**, / sur cales.", "Avec l'enrobage prévu, sur un béton de propreté.",
                  "une fondation, une nappe mal placée.", diagramme=True),
    trouve_erreur(9, "dalle", "Dalle portant entre deux murs, vue de dessus.",
                  "Les grosses barres doivent suivre le chemin des charges vers les **appuis**.",
                  "Les barres principales / sont dans le **mauvais sens**.", "Elles sont parallèles aux murs : elles ne portent rien jusqu'aux appuis.",
                  "Le sens de la portée", "Une dalle qui porte entre deux murs fléchit dans le sens de la portée. Les barres principales vont **d'un mur à l'autre** ; les barres de répartition sont perpendiculaires.",
                  "Principales / **d'un mur à l'autre**.", "Les barres fines, perpendiculaires, répartissent les charges.",
                  "cette dalle est armée… dans le bon sens ?"),
    trouve_erreur(10, "serrees", "Coupe d'une poutre fortement armée.",
                  "Imagine le béton et ses graviers qui doivent **couler** entre ces barres.",
                  "Les barres sont / **trop serrées**.", "Six HA25 collées : le béton ne passe pas, il restera des vides.",
                  "Laisser passer le béton", "Entre deux barres, il faut au moins **le diamètre de la barre**, et assez d'espace pour le plus gros granulat. Sinon : nids de cailloux et acier mal enrobé.",
                  "**Deux lits**, / bien espacés.", "Même section d'acier, mais le béton peut enrober chaque barre.",
                  "beaucoup d'acier… trop serré ?"),
    trouve_erreur(11, "chapeaux", "Poutre continue sur trois appuis.",
                  "Au-dessus de l'appui du milieu, la poutre se plie dans l'**autre sens**.",
                  "Il manque / les **chapeaux**.", "Au-dessus de l'appui intermédiaire, il n'y a qu'une fine barre de montage.",
                  "Le moment sur appui", "Sur une poutre continue, le moment devient **négatif** sur l'appui intermédiaire : c'est le haut qui est tendu, il faut de l'acier en haut.",
                  "Des **chapeaux** / sur l'appui.", "Des barres supérieures prolongées de part et d'autre de l'appui.",
                  "trois appuis, un oubli classique.", diagramme=True),
    trouve_erreur(12, "escalier", "Paillasse et palier d'un escalier, en coupe.",
                  "Regarde la barre du dessous au **changement de pente**.",
                  "La barre suit / l'**angle rentrant**.", "Tendue, elle va vouloir se redresser et faire sauter le béton sous l'angle.",
                  "L'effet « poussée au vide »", "Une barre tendue qui suit un angle rentrant pousse vers l'extérieur et fait éclater l'enrobage. Il faut **croiser** les barres et ancrer chacune au-delà de l'angle.",
                  "Des barres **croisées** / et ancrées.", "Chaque barre continue droit et s'ancre dans l'autre partie.",
                  "un escalier, un angle piège."),
    trouve_erreur(13, "ancrage", "Extrémité d'une poutre sur son appui de rive.",
                  "Regarde où s'**arrête** la barre du dessous.",
                  "La barre n'est / pas **ancrée**.", "Elle s'arrête au nu de l'appui : elle ne peut pas transmettre son effort.",
                  "Ancrer, c'est accrocher", "Une barre tendue doit se prolonger dans l'appui sur sa **longueur d'ancrage**, droite ou avec crochet, pour que l'effort passe au béton.",
                  "Prolongée dans l'appui, / avec **crochet**.", "La longueur d'ancrage se calcule selon le diamètre et le béton.",
                  "la fin de cette poutre ne tiendra pas."),
    trouve_erreur(14, "semelle_sol", "Semelle isolée, nappe en place avant le coulage.",
                  "Qu'y a-t-il entre l'acier et la **terre** ?",
                  "La nappe est posée / **à même le sol**.", "Pas de béton de propreté, pas de cales : l'acier touche la terre.",
                  "Protéger l'acier", "Au contact de la terre humide, l'acier rouille. On coule d'abord un **béton de propreté**, puis on pose la nappe sur des cales pour garantir l'enrobage.",
                  "Béton de propreté / + **cales**.", "L'enrobage est assuré sur toute la surface.",
                  "une erreur qu'on voit sur beaucoup de chantiers."),
]
