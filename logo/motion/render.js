// Rendu image par image d'un teaser.
//   node render.js <page.html> stills <dossier> 3.9 8.8 ...  → captures PNG aux instants donnés
//   node render.js <page.html> frames <dossier> [workers]    → toutes les images (JPEG)
//     + <page>.cues.json à côté de la page (repères sonores et plan musical pour sound.py)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function openPage(browser, page) {
  const size = await (async () => {
    const html = fs.readFileSync(page, 'utf8');
    const m = html.match(/<canvas[^>]*width="(\d+)"[^>]*height="(\d+)"/);
    return { width: +m[1], height: +m[2] };
  })();
  const p = await browser.newPage({ viewport: size, deviceScaleFactor: 1 });
  await p.goto('file://' + page);
  await p.evaluate(() => window.ready);
  return p;
}

(async () => {
  const [pageArg, mode, outDir, ...rest] = process.argv.slice(2);
  const page = path.resolve(__dirname, pageArg);
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  if (mode === 'stills') {
    const p = await openPage(browser, page);
    for (const s of rest) {
      await p.evaluate(t => window.renderFrame(t), +s);
      await p.locator('canvas').screenshot({ path: path.join(outDir, `still_${String(s).padStart(5, '0')}.png`) });
    }
  } else {
    const workers = +(rest[0] || 4);
    const probe = await openPage(browser, page);
    const info = await probe.evaluate(() => ({ cues: window.CUES, music: window.MUSIC, dur: window.DUR, fps: window.FPS }));
    fs.writeFileSync(page.replace(/\.html$/, '.cues.json'), JSON.stringify(info, null, 1));
    await probe.close();
    const n = Math.round(info.dur * info.fps);
    let done = 0;
    await Promise.all([...Array(workers).keys()].map(async w => {
      const p = await openPage(browser, page);
      for (let i = w; i < n; i += workers) {
        const url = await p.evaluate(t => { window.renderFrame(t); return document.getElementById('c').toDataURL('image/jpeg', .95); }, i / info.fps);
        fs.writeFileSync(path.join(outDir, `f${String(i).padStart(5, '0')}.jpg`), Buffer.from(url.split(',')[1], 'base64'));
        if (++done % 300 === 0) console.log(`${done}/${n}`);
      }
    }));
  }
  await browser.close();
})();
