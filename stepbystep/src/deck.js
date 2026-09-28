// Modèle PowerPoint « support de cours » Step by Step Academy — node deck.js <sortie.pptx>
const pptxgen = require("pptxgenjs");
const path = require("path");

const A = (f) => path.join(__dirname, "..", "out", "office_assets", f);
const C = { noir: "111111", or: "F5C518", orTexte: "8A6A00", ivoire: "FAF7F0", sable: "EFE8D8", blanc: "FFFFFF",
  gris: "5E5A52", grisClair: "C9C2B4", vert: "5DB12E", vertTexte: "437F21", graphite: "2A2A2A" };
const TITRE = "Quicksand", TEXTE = "Nunito", ACC = "Comfortaa";
const H_R = 1800 / 540, P_R = 1200 / 1323;
const LARG = [296, 385, 491, 620, 767];

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Step by Step Academy — Support de cours";
pres.company = "Step by Step Academy";

const T = (s, text, o) => s.addText(text, Object.assign({ margin: 0, isTextBox: true, valign: "top" }, o));
function kicker(s, text, dark, x = 0.8, y = 0.6) {
  T(s, text.toUpperCase(), { x, y, w: 9, h: 0.3, fontFace: ACC, bold: true, fontSize: 11, charSpacing: 3, color: dark ? C.or : C.orTexte });
}
function marches(s, x, y, w, h, gap, col) {       // motif des 5 marches, aligné à droite
  LARG.forEach((v, i) => {
    const ww = w * v / 767;
    s.addShape(pres.shapes.RECTANGLE, { x: x + w - ww, y: y + i * (h + gap), w: ww, h, fill: { color: col }, line: { color: col, width: 0 } });
  });
}
function pied(s, n, dark) {
  const col = dark ? "9C958A" : C.gris;
  s.addImage({ path: A(dark ? "logo_horizontal_sombre.png" : "logo_horizontal_clair.png"), x: 0.8, y: 6.85, w: 1.5, h: 1.5 / H_R });
  T(s, "Module · Titre du module", { x: 4.5, y: 6.93, w: 4.3, h: 0.3, align: "center", fontFace: ACC, bold: true, fontSize: 9, charSpacing: 2, color: col });
  T(s, String(n).padStart(2, "0"), { x: 11.53, y: 6.93, w: 1, h: 0.3, align: "right", fontFace: ACC, bold: true, fontSize: 10, color: col });
}
function titre(s, text, dark, y = 0.95, size = 32, h = 0.9) {
  T(s, text, { x: 0.8, y, w: 11.7, h, fontFace: TITRE, bold: true, fontSize: size, color: dark ? C.ivoire : C.noir });
}

// 1. Couverture du module
{
  const s = pres.addSlide();
  s.background = { path: A("bg_couverture.png") };
  s.addImage({ path: A("logo_horizontal_sombre.png"), x: 0.8, y: 0.6, w: 3.4, h: 3.4 / H_R });
  kicker(s, "Formation AutoCAD · Niveau 1 · Découvrir", true, 0.8, 2.25);
  T(s, "Dessiner son premier plan", { x: 0.8, y: 2.65, w: 11, h: 1.0, fontFace: TITRE, bold: true, fontSize: 44, color: C.ivoire });
  T(s, "Module 01 · Interface, lignes et calques", { x: 0.8, y: 3.6, w: 10, h: 0.5, fontFace: TEXTE, fontSize: 20, color: C.grisClair });
  T(s, "Formateur : Prénom Nom  ·  Date", { x: 7.3, y: 6.8, w: 5.2, h: 0.35, align: "right", fontFace: TEXTE, fontSize: 12, color: "9C958A" });
  s.addNotes("Modifier le logiciel, le niveau, le titre et le nom du formateur. Le fond est une image : ne pas l'étirer.");
}

// 2. Objectifs de la séance
{
  const s = pres.addSlide();
  s.background = { color: C.ivoire };
  kicker(s, "Objectifs", false);
  titre(s, "À la fin de cette séance, vous saurez :", false);
  ["Vous repérer dans l'interface d'AutoCAD", "Tracer des lignes, cercles et rectangles précis", "Organiser votre dessin avec des calques"].forEach((t, i) => {
    const y = 2.3 + i * 1.3;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.8, y, w: 7.4, h: 1.05, rectRadius: 0.1, fill: { color: C.blanc }, line: { color: C.sable, width: 0.75 } });
    s.addShape(pres.shapes.OVAL, { x: 1.05, y: y + 0.24, w: 0.58, h: 0.58, fill: { color: C.or }, line: { color: C.or } });
    T(s, String(i + 1), { x: 1.05, y: y + 0.24, w: 0.58, h: 0.58, align: "center", valign: "middle", fontFace: ACC, bold: true, fontSize: 16, color: C.noir });
    T(s, t, { x: 1.9, y: y + 0.28, w: 6.1, h: 0.5, fontFace: TITRE, bold: true, fontSize: 19, color: C.noir });
  });
  marches(s, 9.0, 2.3, 3.5, 0.52, 0.17, C.or);
  T(s, "Durée : 2 h\nPrérequis : aucun", { x: 9.0, y: 5.8, w: 3.5, h: 0.8, align: "right", fontFace: TEXTE, fontSize: 14, color: C.gris });
  pied(s, 2, false);
}

// 3. Plan du module (les marches)
{
  const s = pres.addSlide();
  s.background = { color: C.ivoire };
  kicker(s, "Plan du module", false);
  titre(s, "Cinq étapes, une à la fois.", false);
  const etapes = ["L'interface", "Les outils de dessin", "La précision", "Les calques", "Exercice final"];
  etapes.forEach((t, i) => {
    const h = 0.6 + i * 0.42, x = 0.8 + i * 2.38, y = 6.2 - h;
    const done = i < 1, now = i === 1;
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 2.28, h, fill: { color: done ? C.or : now ? C.noir : C.sable }, line: { width: 0, color: C.sable } });
    T(s, `${i + 1}`, { x: x + 0.2, y: y + 0.12, w: 1, h: 0.4, fontFace: ACC, bold: true, fontSize: 14, color: now ? C.or : C.noir });
    T(s, t, { x, y: y - 0.55, w: 2.28, h: 0.45, fontFace: TITRE, bold: true, fontSize: 16, color: C.noir });
  });
  T(s, "Étape en cours en noir, étapes validées en or.", { x: 0.8, y: 1.85, w: 8, h: 0.4, fontFace: TEXTE, fontSize: 14, color: C.gris });
  pied(s, 3, false);
}

// 4. Intercalaire de partie
{
  const s = pres.addSlide();
  s.background = { path: A("bg_section.png") };
  T(s, "02", { x: 0.8, y: 1.3, w: 4, h: 2.15, fontFace: TITRE, bold: true, fontSize: 120, color: C.or });
  T(s, "Les outils de dessin", { x: 0.8, y: 3.45, w: 11, h: 0.9, fontFace: TITRE, bold: true, fontSize: 44, color: C.ivoire });
  T(s, "Ligne, cercle, rectangle, polyligne : les gestes de base.", { x: 0.8, y: 4.35, w: 9, h: 0.5, fontFace: TEXTE, fontSize: 18, color: C.grisClair });
  pied(s, 4, true);
}

// 5. Contenu + capture d'écran
{
  const s = pres.addSlide();
  s.background = { color: C.ivoire };
  kicker(s, "02 — Les outils de dessin", false);
  titre(s, "Tracer une ligne précise", false);
  const pas = [["Taper L puis Entrée", "La commande LIGNE démarre."], ["Cliquer le point de départ", "Ou saisir des coordonnées : 0,0."],
               ["Saisir la longueur", "Exemple : @500<0 pour 500 mm à l'horizontale."], ["Valider avec Entrée", "La ligne est tracée."]];
  pas.forEach(([t, d], i) => {
    const y = 2.1 + i * 1.1;
    T(s, String(i + 1).padStart(2, "0"), { x: 0.8, y, w: 0.7, h: 0.4, fontFace: ACC, bold: true, fontSize: 14, color: C.orTexte });
    T(s, t, { x: 1.5, y: y - 0.03, w: 4.7, h: 0.4, fontFace: TITRE, bold: true, fontSize: 17, color: C.noir });
    T(s, d, { x: 1.5, y: y + 0.4, w: 4.7, h: 0.5, fontFace: TEXTE, fontSize: 13, color: C.gris });
  });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.6, y: 1.95, w: 5.93, h: 4.5, rectRadius: 0.08, fill: { color: C.noir }, line: { color: C.noir } });
  T(s, "Capture d'écran ici\n(clic droit › Modifier l'image)", { x: 6.6, y: 1.95, w: 5.93, h: 4.5, align: "center", valign: "middle", fontFace: TEXTE, fontSize: 13, color: "8C857A" });
  pied(s, 5, false);
}

// 6. Exercice pratique
{
  const s = pres.addSlide();
  s.background = { color: C.ivoire };
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.8, y: 0.7, w: 11.73, h: 5.8, rectRadius: 0.12, fill: { color: C.noir }, line: { color: C.noir } });
  T(s, "À VOUS DE JOUER", { x: 1.3, y: 1.1, w: 6, h: 0.35, fontFace: ACC, bold: true, fontSize: 12, charSpacing: 3, color: C.or });
  T(s, "Exercice 1 · Le plan d'une pièce", { x: 1.3, y: 1.55, w: 10, h: 0.7, fontFace: TITRE, bold: true, fontSize: 32, color: C.ivoire });
  T(s, [
    { text: "Dessinez une pièce de 4,00 × 3,50 m.", options: { bullet: { code: "25A0" }, breakLine: true } },
    { text: "Ajoutez une porte de 0,90 m et une fenêtre de 1,20 m.", options: { bullet: { code: "25A0" }, breakLine: true } },
    { text: "Placez murs, porte et fenêtre sur trois calques différents.", options: { bullet: { code: "25A0" } } },
  ], { x: 1.3, y: 2.55, w: 7, h: 2.2, fontFace: TEXTE, fontSize: 18, color: C.ivoire, paraSpaceAfter: 10 });
  T(s, "20 min", { x: 9.3, y: 2.5, w: 2.8, h: 1.0, align: "right", fontFace: TITRE, bold: true, fontSize: 54, color: C.or });
  T(s, "Validez chaque étape avec le formateur avant de passer à la suivante.", { x: 1.3, y: 5.5, w: 10, h: 0.5, fontFace: TEXTE, italic: true, fontSize: 14, color: C.grisClair });
  pied(s, 6, false);
}

// 7. À retenir
{
  const s = pres.addSlide();
  s.background = { color: C.ivoire };
  kicker(s, "À retenir", false);
  titre(s, "Trois réflexes pour un dessin propre", false);
  [["Toujours saisir les cotes", "Ne jamais dessiner « à l'œil » : la précision se tape au clavier."],
   ["Un calque par famille", "Murs, portes, cotations : chacun son calque, chacun sa couleur."],
   ["Enregistrer souvent", "Ctrl + S toutes les 10 minutes, et une copie en fin de séance."]].forEach(([t, d], i) => {
    const x = 0.8 + i * 4.0;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.2, w: 3.73, h: 3.6, rectRadius: 0.1, fill: { color: C.blanc }, line: { color: C.sable, width: 0.75 } });
    s.addShape(pres.shapes.OVAL, { x: x + 0.35, y: 2.55, w: 0.62, h: 0.62, fill: { color: "EEF6E8" }, line: { color: C.vert, width: 2 } });
    T(s, "✓", { x: x + 0.35, y: 2.55, w: 0.62, h: 0.62, align: "center", valign: "middle", fontFace: TEXTE, bold: true, fontSize: 18, color: C.vertTexte });
    T(s, t, { x: x + 0.35, y: 3.45, w: 3.1, h: 0.8, fontFace: TITRE, bold: true, fontSize: 19, color: C.noir });
    T(s, d, { x: x + 0.35, y: 4.3, w: 3.05, h: 1.3, fontFace: TEXTE, fontSize: 14, color: C.gris });
  });
  pied(s, 7, false);
}

// 8. Fin / contact
{
  const s = pres.addSlide();
  s.background = { path: A("bg_couverture.png") };
  s.addImage({ path: A("logo_principal_sombre.png"), x: 9.0, y: 0.9, w: 3.2, h: 3.2 / P_R });
  T(s, "Étape validée !", { x: 0.8, y: 1.3, w: 7.5, h: 1.0, fontFace: TITRE, bold: true, fontSize: 48, color: C.ivoire });
  T(s, "Prochaine marche : Module 02 · La cotation", { x: 0.8, y: 2.35, w: 7.5, h: 0.5, fontFace: TEXTE, fontSize: 20, color: C.or });
  T(s, "step.by.step.academy4@gmail.com\n+223 89 48 33 27 · WhatsApp", { x: 0.8, y: 3.3, w: 7, h: 0.9, fontFace: TEXTE, bold: true, fontSize: 16, color: C.ivoire });
}

pres.writeFile({ fileName: process.argv[2] || "StepByStep_Modele_support_de_cours.pptx" }).then((f) => console.log("ok", f));
