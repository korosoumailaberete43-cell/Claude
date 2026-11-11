// usage : node rendu_pdf.js a.html b.html …  → a.pdf, b.pdf à côté (A4 paysage, fonds imprimés)
// S'arrête à la première erreur (fichier absent, page cassée) avec un code de sortie 1.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const fichiers = process.argv.slice(2);
  if (fichiers.length === 0) throw new Error('usage : node rendu_pdf.js page.html …');
  const b = await chromium.launch();
  try {
    const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
    for (const f of fichiers) {
      if (!/\.html?$/i.test(f)) throw new Error(`pas un fichier HTML : ${f}`);
      const sortie = f.replace(/\.html?$/i, '.pdf');
      await p.goto('file://' + path.resolve(f));
      await p.evaluate(() => document.fonts.ready);
      await p.pdf({ path: sortie, width: '297mm', height: '210mm', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
      console.log(sortie);
    }
  } finally {
    await b.close();
  }
})().catch((e) => {
  console.error('rendu_pdf : ' + e.message.split('\n')[0]);
  process.exit(1);
});
