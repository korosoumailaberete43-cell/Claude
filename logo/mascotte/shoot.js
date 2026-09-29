// Capture une page de la mascotte (modules ES → servis par un petit serveur local).
//   node shoot.js fiche.html out/fiche.png 1920 1350  (ou .pdf → document imprimable)
const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.woff2': 'font/woff2', '.png': 'image/png', '.json': 'application/json' };

(async () => {
  const [page, out, w, h] = process.argv.slice(2);
  const server = http.createServer((req, res) => {
    const f = path.join(ROOT, decodeURIComponent(req.url.split('?')[0]));
    if (!f.startsWith(ROOT) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  }).listen(0);
  const port = server.address().port;
  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: +w, height: +h } });
  p.on('console', m => { if (m.type() === 'error') console.log('console:', m.text()); });
  p.on('pageerror', e => console.log('pageerror:', e.message));
  await p.goto(`http://localhost:${port}/mascotte/${page}`);
  await p.waitForFunction(() => window.ready === true, null, { timeout: 180000 });
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  if (out.endsWith('.pdf')) await p.pdf({ path: out, width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true }); else await p.screenshot({ path: out, fullPage: true });
  await browser.close(); server.close();
})();
