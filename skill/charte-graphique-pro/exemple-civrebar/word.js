// Modèles Word CivRebar AI : papier à en-tête + note de calcul. node word.js <dossier_sortie>
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Header, Footer, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, ShadingType, PageBreak, HeadingLevel, PageNumber,
  TabStopType, VerticalAlign, LevelFormat,
} = require("docx");

const OUT = process.argv[2] || ".";
const A = (f) => fs.readFileSync(path.join(__dirname, "..", "out", "pptx_assets", f));
const C = { nuit: "0B1624", cuivre: "C8773F", cuivreTexte: "9A5526", gris: "5B6572", filet: "D9D4CA", chaux: "F3F0EA", signalTexte: "0B7480" };
const TITRE = "Sora", TEXTE = "Manrope", MONO = "JetBrains Mono";
const LOGO_R = 1600 / 302;
const CONTENT_W = 9638; // A4 (11906) − marges 1134 × 2

const styles = {
  default: { document: { run: { font: TEXTE, size: 21, color: C.nuit }, paragraph: { spacing: { after: 120, line: 300 } } } },
  paragraphStyles: [
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: TITRE, size: 32, bold: true, color: C.nuit }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0 } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: TITRE, size: 24, bold: true, color: C.cuivreTexte }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
  ],
};
const numbering = { config: [{ reference: "puces", levels: [{ level: 0, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT,
  style: { paragraph: { indent: { left: 360, hanging: 240 } }, run: { color: C.cuivre } } }] }] };

const page = { size: { width: 11906, height: 16838 }, margin: { top: 1700, bottom: 1300, left: 1134, right: 1134, header: 600, footer: 500 } };

function logo(w_cm) {
  const w = w_cm / 2.54 * 96;
  return new ImageRun({ type: "png", data: A("logo_light.png"), transformation: { width: Math.round(w), height: Math.round(w / LOGO_R) },
    altText: { title: "Logo CivRebar AI", description: "Logo CivRebar AI", name: "logo" } });
}
function header() {
  return new Header({ children: [new Paragraph({ children: [logo(5.2)], spacing: { after: 0 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.filet, space: 10 } } })] });
}
function footer(withPage) {
  const kids = [new TextRun({ text: "CivRebar AI  ·  contact@civrebar.ai  ·  +225 00 00 00 00 00", font: MONO, size: 14, color: C.gris })];
  if (withPage) kids.push(new TextRun({ children: ["\t", PageNumber.CURRENT], font: MONO, size: 14, color: C.gris }));
  return new Footer({ children: [new Paragraph({ children: kids, tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
    border: { top: { style: BorderStyle.SINGLE, size: 4, color: C.filet, space: 8 } } })] });
}
const P = (text, o = {}) => new Paragraph({ ...o, children: [new TextRun({ text, ...(o.run || {}) })] });
const kicker = (text) => P(text.toUpperCase(), { run: { font: MONO, size: 16, color: C.cuivreTexte, characterSpacing: 40 }, spacing: { after: 80 } });

// ------------------------------------------------------------ 1. Papier à en-tête
const lettre = new Document({
  creator: "CivRebar AI", title: "CivRebar AI — Papier à en-tête", styles, numbering,
  sections: [{ properties: { page }, headers: { default: header() }, footers: { default: footer(false) }, children: [
    P("Ville, le 28 septembre 2026", { alignment: AlignmentType.RIGHT, spacing: { after: 480 } }),
    P("Nom du destinataire", { run: { bold: true }, spacing: { after: 0 } }),
    P("Fonction · Organisation", { spacing: { after: 0 } }),
    P("Adresse", { spacing: { after: 480 } }),
    new Paragraph({ spacing: { after: 360 }, children: [
      new TextRun({ text: "Objet : ", bold: true, font: TITRE }), new TextRun({ text: "présentation du projet CivRebar AI", font: TITRE })] }),
    P("Madame, Monsieur,"),
    P("Nous avons le plaisir de vous présenter CivRebar AI, un outil de ferraillage assisté pour AutoCAD. À partir des paramètres d'un élément de structure, il dessine automatiquement les armatures, les cadres, les cotations et le repérage."),
    P("Le projet avance par étapes : des scripts AutoLISP, puis une boîte à outils, puis un plugin AutoCAD, et à terme une intelligence qui assiste l'ingénieur dans ses vérifications et ses quantitatifs."),
    P("Nous restons à votre disposition pour vous en faire la démonstration.", { spacing: { after: 240 } }),
    P("Veuillez agréer, Madame, Monsieur, l'expression de nos salutations distinguées.", { spacing: { after: 720 } }),
    P("Prénom Nom", { run: { bold: true, font: TITRE }, spacing: { after: 0 } }),
    P("Fondateur, CivRebar AI", { run: { color: C.cuivreTexte } }),
  ] }],
});

// ------------------------------------------------------------ 2. Note de calcul
function cell(text, w, o = {}) {
  return new TableCell({ width: { size: w, type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
    margins: { top: 90, bottom: 90, left: 140, right: 140 },
    shading: o.fill ? { type: ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
    borders: { top: { style: BorderStyle.SINGLE, size: 4, color: C.filet }, bottom: { style: BorderStyle.SINGLE, size: 4, color: C.filet },
               left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } },
    children: [new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text, font: o.mono ? MONO : TEXTE, size: o.size || 19,
      bold: !!o.bold, color: o.color || C.nuit })] })] });
}
function table(rows, widths, head) {
  return new Table({ width: { size: widths.reduce((a, b) => a + b), type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ tableHeader: head && i === 0, children: r.map((t, j) =>
      cell(t, widths[j], head && i === 0 ? { bold: true, fill: C.nuit, color: "FFFFFF", size: 17 } : (j === 0 && !head ? { color: C.gris } : { mono: head && j > 0 }))) })) });
}

const garde = [
  new Paragraph({ children: [logo(7)], spacing: { after: 1800 } }),
  kicker("Note de calcul · Béton armé"),
  P("Ferraillage de la poutre P1", { run: { font: TITRE, size: 56, bold: true }, spacing: { after: 120 } }),
  P("Immeuble R+2 — Plancher haut du rez-de-chaussée", { run: { size: 26, color: C.gris }, spacing: { after: 1200 } }),
  table([
    ["Projet", "Immeuble R+2"], ["Élément", "Poutre P1 — 25 × 50 cm — L = 5,00 m"], ["Référence", "NC-FER-004"],
    ["Indice", "A — première diffusion"], ["Date", "28 septembre 2026"], ["Rédigé par", "Prénom Nom"], ["Vérifié par", "Prénom Nom"],
  ], [2600, CONTENT_W - 2600], false),
  new Paragraph({ children: [new PageBreak()] }),
];
const corps = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("1. Hypothèses")] }),
  new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("1.1 Matériaux")] }),
  table([["Matériau", "Désignation", "Valeur"], ["Béton", "C25/30", "fck = 25 MPa"], ["Acier", "HA B500B", "fyk = 500 MPa"],
         ["Enrobage", "Classe XC1", "c = 3 cm"]], [3000, 3319, 3319], true),
  new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("1.2 Charges")] }),
  new Paragraph({ numbering: { reference: "puces", level: 0 }, children: [new TextRun("Charges permanentes G : à compléter.")] }),
  new Paragraph({ numbering: { reference: "puces", level: 0 }, children: [new TextRun("Charges d'exploitation Q : à compléter.")] }),
  new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("2. Ferraillage retenu")] }),
  table([["Rep.", "Ø", "Nombre", "Longueur", "Poids"], ["1", "HA16", "3", "5,34 m", "25,3 kg"], ["2", "HA12", "2", "5,22 m", "9,3 kg"],
         ["3", "HA8", "31", "1,42 m", "17,4 kg"]], [1400, 1800, 1800, 2319, 2319], true),
  P("Valeurs données à titre d'exemple : remplacer par les résultats du calcul.", { run: { size: 17, color: C.gris, italics: true }, spacing: { before: 120 } }),
];
const note = new Document({
  creator: "CivRebar AI", title: "CivRebar AI — Note de calcul", styles, numbering,
  sections: [
    { properties: { page, titlePage: true }, headers: { default: header(), first: new Header({ children: [new Paragraph("")] }) },
      footers: { default: footer(true), first: footer(false) }, children: [...garde, ...corps] },
  ],
});

Promise.all([
  Packer.toBuffer(lettre).then((b) => fs.writeFileSync(path.join(OUT, "CivRebar_AI_Papier_en-tete.docx"), b)),
  Packer.toBuffer(note).then((b) => fs.writeFileSync(path.join(OUT, "CivRebar_AI_Modele_note_de_calcul.docx"), b)),
]).then(() => console.log("ok"));
