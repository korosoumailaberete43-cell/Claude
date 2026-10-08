// usage: node render_png.js "in.html|out.png|w|h" ...  (capture à l'échelle 1:1)
// Réessaie une capture qui échoue : sous charge, Chromium rend parfois la main trop tôt.
const { chromium } = require('playwright');
const path = require('path');

const pause = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  let b = await chromium.launch();
  for (const job of process.argv.slice(2)) {
    const [inp, out, w, h] = job.split('|');
    for (let essai = 1; ; essai++) {
      try {
        const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
        await p.goto('file://' + path.resolve(inp));
        await p.evaluate(() => document.fonts.ready);
        await p.screenshot({ path: out });
        await p.close();
        break;
      } catch (e) {
        if (essai >= 3) throw e;
        console.error(`reprise ${essai}/2 : ${path.basename(out)} (${e.message.split('\n')[0]})`);
        await pause(2000 * essai);
        try { await b.close(); } catch { /* navigateur déjà perdu */ }
        b = await chromium.launch();
      }
    }
  }
  await b.close();
})();
