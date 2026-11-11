// usage : node rendu_png.js "in.html|out.png|w|h" ...  (capture à l'échelle 1:1)
// S'arrête à la première erreur avec un code de sortie 1.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const travaux = process.argv.slice(2);
  if (travaux.length === 0) throw new Error('usage : node rendu_png.js "in.html|out.png|w|h" …');
  const b = await chromium.launch();
  try {
    for (const job of travaux) {
      const [inp, out, w, h] = job.split('|');
      if (!inp || !out || !(+w > 0) || !(+h > 0)) throw new Error(`travail mal formé : ${job}`);
      const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
      try {
        await p.goto('file://' + path.resolve(inp));
        await p.evaluate(() => document.fonts.ready);
        await p.screenshot({ path: out });
      } finally {
        await p.close();
      }
    }
  } finally {
    await b.close();
  }
})().catch((e) => {
  console.error('rendu_png : ' + e.message.split('\n')[0]);
  process.exit(1);
});
