// usage : node rendu_png.js "in.html|out.png|w|h" ...  (capture à l'échelle 1:1)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const job of process.argv.slice(2)) {
    const [inp, out, w, h] = job.split('|');
    const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.resolve(inp));
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: out });
    await p.close();
  }
  await b.close();
})();
