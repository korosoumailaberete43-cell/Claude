// Rendu image par image de la présentation (workers Playwright en parallèle).
//   node video/render.js frames/ [workers] [t1,t2,...]   (liste de temps = captures de test)
const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.woff2': 'font/woff2', '.png': 'image/png', '.json': 'application/json' };

(async () => {
  const [outDir, nw = '4', only] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const server = http.createServer((req, res) => {
    const f = path.join(ROOT, decodeURIComponent(req.url.split('?')[0]));
    if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  }).listen(0);
  const url = `http://localhost:${server.address().port}/mascotte/video/presentation.html`;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const open = async () => {
    const p = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
    p.on('pageerror', e => console.log('pageerror:', e.message));
    p.on('console', m => { if (m.type() === 'error') console.log('console:', m.text()); });
    await p.goto(url);
    await p.waitForFunction(() => window.ready === true, null, { timeout: 180000 });
    return p;
  };
  const first = await open();
  const { DUR, FPS, CUES } = await first.evaluate(() => ({ DUR: window.DUR, FPS: window.FPS, CUES: window.CUES }));
  fs.writeFileSync(path.join(outDir, 'cues.json'), JSON.stringify(CUES));
  let jobs;
  if (only) jobs = only.split(',').map(s => ({ t: +s, name: `t${(+s).toFixed(1).padStart(5, '0')}.jpg` }));
  else jobs = Array.from({ length: Math.round(DUR * FPS) }, (_, i) => ({ t: i / FPS, name: `f${String(i).padStart(5, '0')}.jpg` }))
    .filter(j => !fs.existsSync(path.join(outDir, j.name)));
  const pages = [first];
  for (let i = 1; i < Math.min(+nw, jobs.length); i++) pages.push(await open());
  let k = 0, done = 0; const t0 = Date.now();
  await Promise.all(pages.map(async p => {
    while (k < jobs.length) {
      const j = jobs[k++];
      const d = await p.evaluate(t => window.renderFrame(t), j.t);
      fs.writeFileSync(path.join(outDir, j.name), Buffer.from(d.split(',')[1], 'base64'));
      if (++done % 60 === 0) console.log(`${done}/${jobs.length}  ${((Date.now() - t0) / done).toFixed(0)} ms/img`);
    }
  }));
  await browser.close(); server.close();
  console.log('fini', done);
})();
