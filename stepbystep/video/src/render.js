// Rendu image par image d'une page animée (window.renderAt(t)) en vidéo, avec flou de mouvement.
// usage : node render.js page.html sortie.mp4 [fps=30] [sous-images=4] [processus=4] [--stills t1,t2,...]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const FF = process.env.FFMPEG;

const [inp, out, fpsA, subA, wA, ...rest] = process.argv.slice(2);
const fps = +(fpsA || 30), sub = +(subA || 4), workers = +(wA || 4), SHUTTER = .5;

async function openPage(b) {
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  return p;
}

async function stills(ts) {
  const b = await chromium.launch();
  const p = await openPage(b);
  for (const t of ts) {
    await p.evaluate(t => window.renderAt(t), t);
    await p.screenshot({ path: `${out}_${t.toFixed(2)}.png` });
  }
  await b.close();
}

async function segment(b, k0, k1, file) {
  const p = await openPage(b);
  const ff = spawn(FF, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps * sub), '-i', '-',
    '-vf', `tmix=frames=${sub},select='eq(mod(n\\,${sub})\\,${sub - 1})',setpts=N/(${fps}*TB)`,
    '-r', String(fps), '-c:v', 'libx264rgb', '-preset', 'ultrafast', '-crf', '0', file], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let k = k0; k < k1; k++) {
    for (let j = 0; j < sub; j++) {
      const t = Math.max(0, (k + ((j + .5) / sub - .5) * SHUTTER) / fps);
      await p.evaluate(t => window.renderAt(t), t);
      const buf = await p.screenshot({ type: 'png' });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await p.close();
}

(async () => {
  if (rest[0] === '--stills') return stills(rest[1].split(',').map(Number));
  const b = await chromium.launch();
  const probe = await openPage(b);
  const dur = await probe.evaluate(() => window.DUREE);
  await probe.close();
  const N = Math.round(dur * fps), per = Math.ceil(N / workers), segs = [];
  const t0 = Date.now();
  await Promise.all([...Array(workers).keys()].map(i => {
    const f = `${out}.part${i}.mkv`; segs.push(f);
    return segment(b, i * per, Math.min(N, (i + 1) * per), f);
  }));
  await b.close();
  fs.writeFileSync(out + '.txt', segs.map(s => `file '${path.resolve(s)}'`).join('\n'));
  console.log(`${N} images en ${((Date.now() - t0) / 1000).toFixed(0)} s`);
})();
