// Modèles Word Step by Step Academy : papier à en-tête + attestation de réussite. node word.js <dossier>
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, TextRun, ImageRun, Header, Footer, AlignmentType, BorderStyle, TabStopType,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom, PageOrientation } = require("docx");

const OUT = process.argv[2] || ".";
const A = (f) => fs.readFileSync(path.join(__dirname, "..", "out", "office_assets", f));
const C = { noir: "111111", or: "F5C518", orTexte: "8A6A00", gris: "5E5A52", filet: "E4DCCB", vertTexte: "437F21" };
const TITRE = "Quicksand", TEXTE = "Nunito", ACC = "Comfortaa";
const H_R = 1800 / 540;
const CONTACT = "step.by.step.academy4@gmail.com  ·  +223 89 48 33 27  ·  Mali";

const styles = { default: { document: { run: { font: TEXTE, size: 21, color: C.noir }, paragraph: { spacing: { after: 120, line: 300 } } } } };
const P = (text, o = {}) => new Paragraph({ ...o, children: [new TextRun({ text, ...(o.run || {}) })] });
const logoH = (wcm) => { const w = wcm / 2.54 * 96; return new ImageRun({ type: "png", data: A("logo_horizontal_clair.png"),
  transformation: { width: Math.round(w), height: Math.round(w / H_R) }, altText: { title: "Logo", description: "Logo Step by Step Academy", name: "logo" } }); };

// ------------------------------------------------ papier à en-tête (A4 portrait)
const lettre = new Document({ creator: "Step by Step Academy", title: "Papier à en-tête", styles,
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1900, bottom: 1300, left: 1134, right: 1134, header: 600, footer: 500 } } },
    headers: { default: new Header({ children: [new Paragraph({ children: [logoH(5.5)], spacing: { after: 0 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: C.or, space: 10 } } })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: CONTACT, font: ACC, size: 14, color: C.gris })],
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: C.filet, space: 8 } } })] }) },
    children: [
      P("Ville, le 15 octobre 2026", { alignment: AlignmentType.RIGHT, spacing: { after: 480 } }),
      P("Nom du destinataire", { run: { bold: true }, spacing: { after: 0 } }),
      P("Adresse", { spacing: { after: 480 } }),
      new Paragraph({ spacing: { after: 360 }, children: [new TextRun({ text: "Objet : ", bold: true, font: TITRE }), new TextRun({ text: "inscription à la formation AutoCAD — niveau 1", font: TITRE })] }),
      P("Madame, Monsieur,"),
      P("Nous avons le plaisir de confirmer votre inscription à la formation AutoCAD — niveau 1 « Découvrir ». Les séances se dérouleront en présentiel et en ligne, selon le calendrier joint."),
      P("Comme pour toutes nos formations, vous progresserez étape par étape, avec un formateur à vos côtés, jusqu'à la validation de chaque compétence."),
      P("Nous restons à votre disposition pour toute question.", { spacing: { after: 240 } }),
      P("Veuillez agréer, Madame, Monsieur, l'expression de nos salutations distinguées.", { spacing: { after: 720 } }),
      P("Prénom Nom", { run: { bold: true, font: TITRE }, spacing: { after: 0 } }),
      P("Directeur, Step by Step Academy", { run: { color: C.orTexte } }),
    ] }] });

// ------------------------------------------------ attestation de réussite (A4 paysage)
const panneau = new ImageRun({ type: "png", data: A("attestation_panneau.png"),
  transformation: { width: Math.round(250 * 96 / 72), height: Math.round(595 * 96 / 72) },
  floating: { horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 0 },
              verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 0 }, behindDocument: true, allowOverlap: true },
  altText: { title: "Logo", description: "Bandeau Step by Step Academy", name: "panneau" } });
const att = new Document({ creator: "Step by Step Academy", title: "Attestation de réussite", styles,
  background: { color: "FAF7F0" },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
      margin: { top: 1100, bottom: 800, left: 6200, right: 1200 } } },
    children: [
      new Paragraph({ children: [panneau, new TextRun({ text: "ATTESTATION DE RÉUSSITE", font: ACC, bold: true, size: 22, color: C.orTexte, characterSpacing: 80 })], spacing: { after: 360 } }),
      P("Décernée à", { run: { color: C.gris, size: 24 }, spacing: { after: 60 } }),
      new Paragraph({ children: [new TextRun({ text: "Prénom Nom de l'apprenant", font: TITRE, bold: true, size: 72, highlight: "yellow" })],
        border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.or, space: 6 } }, spacing: { after: 300 } }),
      P("pour avoir validé la formation", { run: { color: C.gris, size: 24 }, spacing: { after: 60 } }),
      new Paragraph({ children: [new TextRun({ text: "AutoCAD — Dessin technique 2D", font: TITRE, bold: true, size: 40, highlight: "yellow" })], spacing: { after: 200 } }),
      new Paragraph({ children: [new TextRun({ text: "Niveau ", font: TEXTE, bold: true, size: 24, color: C.gris }), new TextRun({ text: "3", font: TEXTE, bold: true, size: 24, highlight: "yellow" }),
        new TextRun({ text: " sur 5  ·  Découvrir › Comprendre › ", font: TEXTE, bold: true, size: 24, color: C.gris }), new TextRun({ text: "Pratiquer", font: TEXTE, bold: true, size: 24, color: C.noir })], spacing: { after: 900 } }),
      new Paragraph({ tabStops: [{ type: TabStopType.LEFT, position: 3400 }],
        children: [new TextRun({ text: "DATE", font: ACC, bold: true, size: 16, color: C.gris }), new TextRun({ text: "\tLE FORMATEUR", font: ACC, bold: true, size: 16, color: C.gris })], spacing: { after: 60 } }),
      new Paragraph({ tabStops: [{ type: TabStopType.LEFT, position: 3400 }],
        children: [new TextRun({ text: "15 octobre 2026", font: TEXTE, bold: true, size: 24, highlight: "yellow" }), new TextRun({ text: "\tSignature", font: TEXTE, size: 24, color: C.gris })] }),
      P("Les champs surlignés sont à remplacer, puis retirer le surlignage (Accueil › Couleur de surlignage › Aucune couleur).",
        { run: { size: 14, color: C.gris, italics: true }, spacing: { before: 500 } }),
    ] }] });

Promise.all([
  Packer.toBuffer(lettre).then((b) => fs.writeFileSync(path.join(OUT, "StepByStep_Papier_en-tete.docx"), b)),
  Packer.toBuffer(att).then((b) => fs.writeFileSync(path.join(OUT, "StepByStep_Attestation_de_reussite.docx"), b)),
]).then(() => console.log("ok"));
