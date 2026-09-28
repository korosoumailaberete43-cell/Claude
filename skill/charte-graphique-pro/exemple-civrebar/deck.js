// Modèle PowerPoint CivRebar AI — node deck.js <sortie.pptx>
const pptxgen = require("pptxgenjs");
const path = require("path");

const A = (f) => path.join(__dirname, "..", "out", "pptx_assets", f);
const C = { nuit: "0B1624", acier: "1C2B3D", cuivre: "C8773F", cuivreClair: "E3A56C", cuivreTexte: "9A5526",
  signal: "35D0DE", beton: "B9BEC4", chaux: "F3F0EA", blanc: "FFFFFF", gris: "5B6572", grisClair: "AEB7C2" };
const TITRE = "Sora", TEXTE = "Manrope", SERIF = "Instrument Serif", MONO = "JetBrains Mono";
const LOGO_R = 1600 / 302; // largeur / hauteur des PNG du logo horizontal

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13,333 × 7,5 in
pres.title = "CivRebar AI — Présentation";
pres.company = "CivRebar AI";

// ---------- éléments communs
function kicker(s, text, dark, x = 0.8, y = 0.6) {
  s.addText(text.toUpperCase(), { x, y, w: 8, h: 0.3, margin: 0, isTextBox: true,
    fontFace: MONO, fontSize: 11, charSpacing: 3, color: dark ? C.cuivre : C.cuivreTexte });
}
function folio(s, n, dark) {
  const col = dark ? "7C8896" : C.gris;
  s.addText("CIVREBAR AI", { x: 0.8, y: 6.95, w: 3, h: 0.25, margin: 0, isTextBox: true, fontFace: MONO, fontSize: 9, charSpacing: 2, color: col });
  s.addText(String(n).padStart(2, "0"), { x: 11.53, y: 6.95, w: 1, h: 0.25, margin: 0, isTextBox: true, align: "right", fontFace: MONO, fontSize: 9, color: col });
}
function title(s, text, dark, y = 0.95, h = 1.0, size = 34) {
  s.addText(text, { x: 0.8, y, w: 11.7, h, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: size,
    color: dark ? C.chaux : C.nuit, valign: "top" });
}

// ---------- 1. Couverture
{
  const s = pres.addSlide();
  s.background = { path: A("bg_cover.png") };
  kicker(s, "Présentation du projet · 2026", true);
  s.addImage({ path: A("logo_dark.png"), x: 0.8, y: 2.35, w: 6.2, h: 6.2 / LOGO_R });
  s.addText("Le ferraillage assisté pour AutoCAD", { x: 0.8, y: 3.75, w: 8, h: 0.6, margin: 0, isTextBox: true,
    fontFace: TITRE, fontSize: 26, color: C.chaux });
  s.addText("L'intelligence de l'armature.", { x: 0.8, y: 4.35, w: 8, h: 0.6, margin: 0, isTextBox: true,
    fontFace: SERIF, italic: true, fontSize: 26, color: C.cuivreClair });
  s.addText("Prénom Nom · Fondateur", { x: 0.8, y: 6.3, w: 6, h: 0.3, margin: 0, isTextBox: true, fontFace: TEXTE, fontSize: 12, color: C.grisClair });
  s.addNotes("Remplacer « Prénom Nom » par le nom du présentateur. Le fond et le logo sont des images : ne pas les étirer.");
}

// ---------- 2. Sommaire
{
  const s = pres.addSlide();
  s.background = { color: C.chaux };
  kicker(s, "Sommaire", false);
  title(s, "Ce que nous allons voir", false);
  const items = [["01", "Le constat", "Le ferraillage, une tâche longue et répétitive"],
                 ["02", "La solution", "Des outils AutoLISP, puis un vrai plugin"],
                 ["03", "La feuille de route", "Quatre étapes, barre après barre"],
                 ["04", "L'ambition", "Une IA qui assiste l'ingénieur"]];
  items.forEach(([n, t, d], i) => {
    const x = 0.8 + i * 3.0, y = 2.9;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 2.8, h: 3.1, rectRadius: 0.08, fill: { color: C.blanc }, line: { color: "E3DED4", width: 0.75 } });
    s.addText(n, { x: x + 0.3, y: y + 0.3, w: 2.2, h: 0.9, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 44, color: C.cuivre });
    s.addText(t, { x: x + 0.3, y: y + 1.5, w: 2.2, h: 0.5, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 16, color: C.nuit });
    s.addText(d, { x: x + 0.3, y: y + 2.05, w: 2.2, h: 1.0, margin: 0, isTextBox: true, fontFace: TEXTE, fontSize: 13, color: C.gris, valign: "top" });
  });
  folio(s, 2, false);
}

// ---------- 3. Intercalaire
{
  const s = pres.addSlide();
  s.background = { path: A("bg_section.png") };
  s.addText("01", { x: 0.8, y: 1.3, w: 4, h: 2.1, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 120, color: C.cuivre });
  s.addText("Le constat", { x: 0.8, y: 3.5, w: 10, h: 1.0, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 48, color: C.chaux });
  s.addText("Pourquoi le ferraillage mérite de meilleurs outils.", { x: 0.8, y: 4.5, w: 10, h: 0.5, margin: 0, isTextBox: true,
    fontFace: SERIF, italic: true, fontSize: 24, color: C.cuivreClair });
  folio(s, 3, true);
}

// ---------- 4. Texte + visuel
{
  const s = pres.addSlide();
  s.background = { color: C.blanc };
  kicker(s, "01 — Le constat", false);
  title(s, "Dessiner une armature prend\ndes heures. Elle ne pardonne rien.", false, 0.95, 1.4, 30);
  const pts = [
    ["Une tâche répétitive", "Chaque poutre, poteau ou semelle se redessine barre par barre, cadre par cadre."],
    ["Un risque d'erreur réel", "Un espacement mal reporté ou une cote oubliée se paie sur le chantier."],
    ["Des outils peu adaptés", "AutoCAD dessine tout, mais ne connaît rien au béton armé."],
  ];
  pts.forEach(([t, d], i) => {
    const y = 2.75 + i * 1.25;
    s.addText(t, { x: 0.8, y, w: 5.6, h: 0.4, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 17, color: C.nuit });
    s.addText(d, { x: 0.8, y: y + 0.42, w: 5.6, h: 0.7, margin: 0, isTextBox: true, fontFace: TEXTE, fontSize: 14, color: C.gris, valign: "top" });
  });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.1, y: 2.6, w: 5.43, h: 3.95, rectRadius: 0.08, fill: { color: C.nuit }, line: { color: C.nuit } });
  s.addText("Remplacer par une image\n(clic droit › Modifier l'image)", { x: 7.1, y: 2.6, w: 5.43, h: 3.95, isTextBox: true, align: "center", valign: "middle",
    fontFace: MONO, fontSize: 11, color: "56677B" });
  folio(s, 4, false);
}

// ---------- 5. Chiffres clés
{
  const s = pres.addSlide();
  s.background = { color: C.chaux };
  kicker(s, "02 — La solution", false);
  title(s, "Une commande, un dessin complet.", false);
  const stats = [["1", "commande pour dessiner le ferraillage d'une poutre"], ["5", "éléments visés : poutre, poteau, dalle, semelle, escalier"], ["0", "barre redessinée à la main"]];
  stats.forEach(([n, d], i) => {
    const x = 0.8 + i * 4.0;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.5, w: 3.73, h: 3.6, rectRadius: 0.08, fill: { color: C.nuit }, line: { color: C.nuit } });
    s.addText(n, { x: x + 0.4, y: 2.8, w: 3, h: 1.6, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 96, color: C.cuivreClair });
    s.addText(d, { x: x + 0.4, y: 4.5, w: 2.95, h: 1.2, margin: 0, isTextBox: true, fontFace: TEXTE, fontSize: 15, color: C.chaux, valign: "top" });
  });
  s.addNotes("Chiffres illustratifs, à adapter à l'avancement réel du projet.");
  folio(s, 5, false);
}

// ---------- 6. Feuille de route (motif barre + nœuds)
{
  const s = pres.addSlide();
  s.background = { color: C.blanc };
  kicker(s, "03 — La feuille de route", false);
  title(s, "Barre après barre.", false);
  s.addShape(pres.shapes.LINE, { x: 0.8, y: 3.35, w: 11.73, h: 0, line: { color: C.cuivre, width: 5 } });
  const steps = [["01", "AutoLISP", "Un script par élément. Premier objectif : la poutre."],
                 ["02", "Boîte à outils", "Tous les scripts sous un seul menu CivRebar AI."],
                 ["03", "Plugin AutoCAD", "Un onglet dans le ruban, une interface soignée."],
                 ["04", "Intelligence", "Quantitatifs, vérifications, lien avec Robot, assistant IA."]];
  steps.forEach(([n, t, d], i) => {
    const x = 0.8 + i * 3.0, last = i === 3;
    const r = last ? 0.2 : 0.14;
    s.addShape(pres.shapes.OVAL, { x: x + 0.05, y: 3.35 - r, w: 2 * r, h: 2 * r, fill: { color: last ? C.signal : C.nuit }, line: { color: C.blanc, width: 2 } });
    s.addText(n, { x, y: 3.95, w: 2.7, h: 0.35, margin: 0, isTextBox: true, fontFace: MONO, fontSize: 12, color: C.cuivreTexte });
    s.addText(t, { x, y: 4.35, w: 2.7, h: 0.55, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 22, color: C.nuit });
    s.addText(d, { x, y: 5.0, w: 2.6, h: 1.3, margin: 0, isTextBox: true, fontFace: TEXTE, fontSize: 14, color: C.gris, valign: "top" });
  });
  s.addText("NOUS SOMMES ICI", { x: 0.8, y: 2.75, w: 3, h: 0.3, margin: 0, isTextBox: true, fontFace: MONO, fontSize: 10, charSpacing: 2, color: SIGNAL_TXT() });
  folio(s, 6, false);
}
function SIGNAL_TXT() { return "0B7480"; }

// ---------- 7. Citation
{
  const s = pres.addSlide();
  s.background = { path: A("bg_quote.png") };
  kicker(s, "04 — L'ambition", true);
  s.addText("« Une intelligence qui assiste,\nsans jamais remplacer,\ncelui qui signe le plan. »", { x: 0.8, y: 1.7, w: 9.5, h: 3.2, margin: 0, isTextBox: true,
    fontFace: SERIF, italic: true, fontSize: 44, color: C.chaux, valign: "top" });
  s.addText("La promesse CivRebar AI", { x: 0.8, y: 5.2, w: 6, h: 0.4, margin: 0, isTextBox: true, fontFace: MONO, fontSize: 12, charSpacing: 2, color: C.cuivre });
  folio(s, 7, true);
}

// ---------- 8. Fin
{
  const s = pres.addSlide();
  s.background = { path: A("bg_section.png") };
  s.addImage({ path: A("logo_dark.png"), x: 0.8, y: 2.3, w: 6.2, h: 6.2 / LOGO_R });
  s.addText("Merci.", { x: 0.8, y: 3.7, w: 8, h: 0.9, margin: 0, isTextBox: true, fontFace: TITRE, bold: true, fontSize: 40, color: C.chaux });
  s.addText("contact@civrebar.ai  ·  +225 00 00 00 00 00", { x: 0.8, y: 4.6, w: 8, h: 0.4, margin: 0, isTextBox: true, fontFace: MONO, fontSize: 13, color: C.grisClair });
  s.addNotes("Remplacer l'adresse e-mail et le numéro par les vraies coordonnées.");
}

pres.writeFile({ fileName: process.argv[2] || "CivRebar_AI_Modele_presentation.pptx" }).then((f) => console.log("ok", f));
