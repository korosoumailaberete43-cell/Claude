// usage: node render.js in.html out(.png|.pdf) [widthPx heightPx]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, w = '1123', h = '794'] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  if (out.endsWith('.pdf')) await p.pdf({ path: out, width: '297mm', height: '210mm', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  else await p.screenshot({ path: out });
  await b.close();
})();
