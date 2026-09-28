// Rendu image par image du teaser.
//   node render.js stills out/ 3.9 8.8 ...     → captures PNG aux instants donnés
//   node render.js frames out/frames [workers] → toutes les images (JPEG) + out/cues.json
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function openPage(browser) {
  const p = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(__dirname, 'teaser.html'));
  await p.evaluate(() => window.ready);
  return p;
}

(async () => {
  const [mode, outDir, ...rest] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ args: ['--disable-gpu-vsync'] });
  if (mode === 'stills') {
    const p = await openPage(browser);
    for (const s of rest) {
      await p.evaluate(t => window.renderFrame(t), +s);
      await p.locator('canvas').screenshot({ path: path.join(outDir, `still_${String(s).padStart(5, '0')}.png`) });
    }
  } else {
    const workers = +(rest[0] || 4);
    const probe = await openPage(browser);
    const info = await probe.evaluate(() => ({ cues: window.CUES, dur: window.DUR, fps: window.FPS }));
    fs.writeFileSync(path.join(path.dirname(outDir), 'cues.json'), JSON.stringify(info, null, 1));
    await probe.close();
    const n = Math.round(info.dur * info.fps);
    let done = 0;
    await Promise.all([...Array(workers).keys()].map(async w => {
      const p = await openPage(browser);
      for (let i = w; i < n; i += workers) {
        const url = await p.evaluate(t => { window.renderFrame(t); return document.getElementById('c').toDataURL('image/jpeg', .95); }, i / info.fps);
        fs.writeFileSync(path.join(outDir, `f${String(i).padStart(5, '0')}.jpg`), Buffer.from(url.split(',')[1], 'base64'));
        if (++done % 150 === 0) console.log(`${done}/${n}`);
      }
    }));
  }
  await browser.close();
})();
