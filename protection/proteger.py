#!/usr/bin/env python3
"""Produit une version de test protegee d'un fichier AutoLISP :
- supprime tous les commentaires (historique, nom du projet, explications) ;
- renomme toutes les fonctions et variables globales internes CRP_... en noms
  sans signification (les commandes CRP / CRPT / CIVREBAR_... restent) ;
- compacte le code (plus d'indentation, plus de mise en page) ;
- ajoute une date d'expiration de la version de test.
Usage : python3 proteger.py source.lsp sortie.lsp [jours] [nb_essais]
  jours     : duree de validite apres le 1er lancement (defaut 3)
  nb_essais : nombre d'executions autorisees (defaut 2)
Au-dela de la duree OU du nombre d'essais, le fichier .lsp s'efface lui-meme.
"""
import re, sys, random, os

src, dst = sys.argv[1], sys.argv[2]
jours    = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0
essais   = int(sys.argv[4])   if len(sys.argv) > 4 else 2
basename = os.path.basename(dst)
text = open(src, encoding="utf-8").read().replace("\r\n", "\n")

# --- 1. Decoupage en jetons : chaine / commentaire / code -------------------
toks, i, n = [], 0, len(text)
while i < n:
    c = text[i]
    if c == '"':
        j = i + 1
        while text[j] != '"':
            j += 2 if text[j] == "\\" else 1
        toks.append(("str", text[i:j + 1])); i = j + 1
    elif text.startswith(";|", i):
        j = text.index("|;", i + 2); i = j + 2; toks.append(("ws", " "))
    elif c == ";":
        j = text.find("\n", i); i = n if j < 0 else j
    elif c.isspace():
        j = i
        while j < n and text[j].isspace(): j += 1
        toks.append(("ws", " ")); i = j
    else:
        j = i
        while j < n and not text[j].isspace() and text[j] not in '";': j += 1
        toks.append(("code", text[i:j])); i = j

# --- 2. Table de renommage (AutoLISP ne distingue pas les majuscules) ------
sym_re = re.compile(r"\*?CRP_[A-Za-z0-9_]+\*?", re.I)
names = set()
for k, v in toks:
    if k == "code":
        names.update(m.group(0).upper() for m in sym_re.finditer(v))
rnd = random.Random(20260928)
used, table = set(), {}
for nm in sorted(names):
    while True:
        new = "_" + "".join(rnd.choice("lI1") for _ in range(10))
        if new not in used: break
    used.add(new)
    table[nm] = ("*" + new + "*") if nm.startswith("*") else new

def ren(s):
    return sym_re.sub(lambda m: table.get(m.group(0).upper(), m.group(0)), s)

out = []
for k, v in toks:
    if k == "code":
        out.append(ren(v))
    elif k == "str":
        # appels de fonctions dans les chaines (action_tile "(CRP_...)")
        out.append(re.sub(r"(?<=\()\*?CRP_[A-Za-z0-9_]+\*?",
                          lambda m: table.get(m.group(0).upper(), m.group(0)), v))
    else:
        out.append(" ")

# --- 3. Compactage (hors chaines de caracteres) ----------------------------
def compacte(t):
    t = re.sub(r" +", " ", t)
    t = re.sub(r" ?\( ?", "(", t)
    return re.sub(r" \)", ")", t)
res, line = [], ""
for part in re.split(r'("(?:\\.|[^"\\])*")', "".join(out)):
    if part.startswith('"'):
        line += part
    else:
        for ch in compacte(part):
            line += ch
            if ch == ")" and len(line) > 200:
                res.append(line.strip()); line = ""
res.append(line.strip())
code = "\n".join(l for l in res if l)

# --- 4. Garde : duree de validite + nombre d'essais + auto-effacement ------
lanceur = table["CRP_LANCER"]
garde = (
 '(defun _lIlIlIlIlI ( / K now d0 n fp)'
 '(setq K "HKEY_CURRENT_USER\\\\Software\\\\CivRebarTest\\\\%%FN%%")'
 '(setq now (getvar "DATE"))'
 '(setq fp (findfile "%%BN%%"))'
 '(setq d0 (vl-registry-read K "d"))'
 '(if (null d0)(progn (vl-registry-write K "d" (rtos now 2 8))(setq d0 (rtos now 2 8))))'
 '(setq d0 (atof d0))'
 '(setq n (vl-registry-read K "n"))'
 '(setq n (if n (1+ (atoi n)) 1))'
 '(vl-registry-write K "n" (itoa n))'
 '(cond'
 '((> (- now d0) %%J%%.0)'
 '(alert "Version de test expiree (delai de %%J%% jours depasse).")'
 '(if fp (vl-file-delete fp)) nil)'
 '((> n %%E%%)'
 '(alert "Version de test : nombre d essais atteint.")'
 '(if fp (vl-file-delete fp)) nil)'
 '(T (if (>= n %%E%%) (if fp (vl-file-delete fp))) T)))'
).replace("%%FN%%", "".join(c for c in basename if c.isalnum()))\
 .replace("%%BN%%", basename)\
 .replace("%%J%%", ("%g" % jours))\
 .replace("%%E%%", str(essais))

code = garde + "\n" + code.replace("(defun %s(" % lanceur,
                                   "(defun %s_(" % lanceur, 1)
code += "\n(defun %s(m)(if (_lIlIlIlIlI)(%s_ m))(princ))" % (lanceur, lanceur)
code += "\n(princ)\n"

open(dst, "w", encoding="utf-8", newline="\r\n").write(code)
print("%d symboles renommes, %d essais, %g jours, %d -> %d caracteres"
      % (len(table), essais, jours, len(text), len(code)))
