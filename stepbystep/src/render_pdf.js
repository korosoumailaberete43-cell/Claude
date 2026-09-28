// usage: node render_pdf.js a.html b.html ...  -> a.pdf, b.pdf à côté
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + path.resolve(f));
    await p.evaluate(() => document.fonts.ready);
    await p.pdf({ path: f.replace(/\.html$/, '.pdf'), width: '297mm', height: '210mm', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  }
  await b.close();
})();
