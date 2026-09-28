// CivRebar AI — socle commun des teasers (outils, textes, effets, symbole).
// Chaque composition charge ce fichier puis définit DUR, T, ses scènes et renderFrame(t).
const cv = document.getElementById('c');
const ctx = cv.getContext('2d');
const W = cv.width, H = cv.height, FPS = 30;
const COL = {
  nuit: '#0B1624', acier: '#1C2B3D', cuivre: '#C8773F', cuivreC: '#E3A56C',
  signal: '#35D0DE', beton: '#B9BEC4', chaux: '#F3F0EA',
};

// ------------------------------------------------------------ outils
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const prog = (t, a, b) => clamp((t - a) / (b - a));
const lerp = (a, b, k) => a + (b - a) * k;
const eo3 = k => 1 - Math.pow(1 - k, 3);
const ei3 = k => k * k * k;
const eio3 = k => (k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2);
const eoX = k => (k >= 1 ? 1 : 1 - Math.pow(2, -10 * k));
const eoBack = k => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(k - 1, 3) + c1 * Math.pow(k - 1, 2); };
const rnd = n => { const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
const win = (t, a, b, fi = .4, fo = .4) => Math.min(prog(t, a, a + fi), 1 - prog(t, b - fo, b));
const decay = (t, t0, rate) => (t < t0 ? 0 : Math.exp(-(t - t0) * rate));
const rgba = (hex, a) => {
  const n = parseInt(hex.slice(1), 16);
  return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`;
};

// ------------------------------------------------------------ repères
const CUES = [];
const cue = (t, type, g = 1) => CUES.push({ t: +t.toFixed(3), type, g });
const SHAKES = [];
const shakeAt = (t, a) => SHAKES.push([t, a]);

// Plages de tremblement croissant (tension avant un noir)
const TENSION = [];

// ------------------------------------------------------------ géométrie du logo
// Symbole (unités du SVG d'origine)
const SYM_BAR = 'M50 230 V90 A50 50 0 0 1 100 40 H120 A60 60 0 0 1 120 160 H100 A20 20 0 0 1 85.86 125.86 L105.86 105.86';
const SYM_REL = 'M120 160 L180 220 H210';
const NODE = { x: 100, y: 140, r: 7 };
const P_BAR = new Path2D(SYM_BAR), P_REL = new Path2D(SYM_REL);
const svgNS = 'http://www.w3.org/2000/svg';
const measure = d => { const p = document.createElementNS(svgNS, 'path'); p.setAttribute('d', d); const s = document.createElementNS(svgNS, 'svg'); s.appendChild(p); document.body.appendChild(s); return p; };
const EL_BAR = measure(SYM_BAR), EL_REL = measure(SYM_REL);
const LEN_BAR = EL_BAR.getTotalLength(), LEN_REL = EL_REL.getTotalLength();
// ------------------------------------------------------------ textes
const F = (font, size, track = 0) => ({ font: font.replace('#', size + 'px'), size, track });
function setFont(f) { ctx.font = f.font; ctx.letterSpacing = (f.track || 0) + 'px'; }
function layout(str, f) {
  setFont(f);
  const xs = [];
  for (let i = 0; i < str.length; i++) xs.push(ctx.measureText(str.slice(0, i)).width);
  return { xs, total: ctx.measureText(str).width - (f.track || 0) };
}
// Apparition lettre à lettre : 'rise' (sortie d'un masque) ou 'blur' (mise au point)
function reveal(t, str, x, y, f, o) {
  const L = layout(str, f);
  const x0 = o.align === 'left' ? x : x - L.total / 2;
  const alpha = o.alpha == null ? 1 : o.alpha;
  if (alpha <= 0) return;
  for (let i = 0; i < str.length; i++) {
    const ch = str[i];
    if (ch === ' ') continue;
    const k = clamp((t - o.t0 - i * o.st) / o.dur);
    if (k <= 0) continue;
    ctx.save();
    setFont(f); ctx.letterSpacing = '0px';
    ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = typeof o.color === 'function' ? o.color(i, k) : o.color;
    if (o.mode === 'rise') {
      const e = eoX(k);
      ctx.globalAlpha = alpha * clamp(k * 4);
      ctx.beginPath(); ctx.rect(x0 - 60, y - f.size * 1.05, L.total + 120, f.size * 1.36); ctx.clip();
      ctx.fillText(ch, x0 + L.xs[i], y + (1 - e) * f.size * 1.15);
    } else {
      const e = eo3(k);
      ctx.globalAlpha = alpha * e;
      if (k < 1) ctx.filter = `blur(${((1 - e) * 16).toFixed(2)}px)`;
      ctx.fillText(ch, x0 + L.xs[i] + (1 - e) * 36, y);
    }
    ctx.restore();
  }
}
// Mot « claqué » : grossissement → taille réelle
function slam(t, str, x, y, f, t0, color, align = 'center', alpha = 1) {
  const k = prog(t, t0, t0 + .32);
  if (k <= 0 || alpha <= 0) return;
  const e = eoX(k);
  ctx.save();
  setFont(f); ctx.textAlign = align; ctx.textBaseline = 'alphabetic';
  ctx.translate(x, y - f.size * .35); ctx.scale(lerp(2.1, 1, e), lerp(2.1, 1, e)); ctx.translate(0, f.size * .35);
  ctx.globalAlpha = alpha * clamp(k * 3);
  if (k < 1) ctx.filter = `blur(${((1 - e) * 10).toFixed(2)}px)`;
  ctx.fillStyle = color; ctx.fillText(str, 0, 0);
  ctx.restore();
}
// Texte glitché : décalage RVB + tranches déplacées
function glitchText(t, str, x, y, f, color, g, seed = 1, alpha = 1) {
  ctx.save();
  setFont(f); ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
  ctx.globalAlpha = alpha;
  const fr = Math.floor(t * FPS) + seed * 97;
  if (g > .01) {
    const d = 6 + g * 26 * rnd(fr);
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = alpha * .75;
    ctx.fillStyle = COL.signal; ctx.fillText(str, x - d, y);
    ctx.fillStyle = '#d0343a'; ctx.fillText(str, x + d, y + (rnd(fr + 3) - .5) * 6);
    ctx.globalCompositeOperation = 'source-over';
    ctx.globalAlpha = alpha;
  }
  ctx.fillStyle = color; ctx.fillText(str, x, y);
  if (g > .01) {
    const n = 3 + Math.floor(g * 7);
    const L = layout(str, f).total;
    for (let s = 0; s < n; s++) {
      const by = y - f.size * .95 + rnd(fr * 13 + s) * f.size * 1.2;
      const bh = 3 + rnd(fr * 7 + s) * f.size * .22;
      const xo = (rnd(fr * 5 + s * 3) - .5) * g * 160;
      ctx.save();
      ctx.beginPath(); ctx.rect(x - L / 2 - 200, by, L + 400, bh); ctx.clip();
      ctx.fillStyle = COL.nuit; ctx.fillRect(x - L / 2 - 200, by, L + 400, bh);
      ctx.fillStyle = rnd(fr + s) > .7 ? COL.chaux : color;
      ctx.fillText(str, x + xo, y);
      ctx.restore();
    }
  }
  ctx.restore();
}

// ------------------------------------------------------------ fond, grain, caméra
const GRAIN = [];
for (let k = 0; k < 6; k++) {
  const c = document.createElement('canvas'); c.width = c.height = 256;
  const g = c.getContext('2d'), im = g.createImageData(256, 256);
  for (let i = 0; i < im.data.length; i += 4) { const v = rnd(i * .37 + k * 1000) * 255; im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255; }
  g.putImageData(im, 0, 0); GRAIN.push(c);
}
function grid(alpha, zoom = 1) {
  if (alpha <= 0) return;
  ctx.save();
  ctx.translate(W / 2, H / 2); ctx.scale(zoom, zoom); ctx.translate(-W / 2, -H / 2);
  for (let x = -600; x <= W + 600; x += 48) {
    const major = ((x + 600) / 48) % 5 === 0;
    ctx.strokeStyle = rgba(major ? '#3a5570' : '#243a52', alpha * (major ? .55 : .35));
    ctx.lineWidth = major ? 1.2 : 1;
    ctx.beginPath(); ctx.moveTo(x + .5, -600); ctx.lineTo(x + .5, H + 600); ctx.stroke();
  }
  for (let y = -600; y <= H + 600; y += 48) {
    const major = ((y + 600) / 48) % 5 === 0;
    ctx.strokeStyle = rgba(major ? '#3a5570' : '#243a52', alpha * (major ? .55 : .35));
    ctx.lineWidth = major ? 1.2 : 1;
    ctx.beginPath(); ctx.moveTo(-600, y + .5); ctx.lineTo(W + 600, y + .5); ctx.stroke();
  }
  ctx.restore();
}
function vignette(a = .6) {
  const g = ctx.createRadialGradient(W / 2, H / 2, H * .5, W / 2, H / 2, H * 1.15);
  g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, `rgba(0,0,0,${a})`);
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
}
function glow(x, y, r, color, a) {
  if (a <= 0) return;
  const g = ctx.createRadialGradient(x, y, 0, x, y, r);
  g.addColorStop(0, rgba(color, a)); g.addColorStop(.35, rgba(color, a * .35)); g.addColorStop(1, rgba(color, 0));
  ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.fillStyle = g;
  ctx.fillRect(x - r, y - r, 2 * r, 2 * r); ctx.restore();
}
function shake(t) {
  let x = 0, y = 0;
  for (const [t0, a] of SHAKES) {
    if (t < t0) continue;
    const d = Math.exp(-(t - t0) * 7) * a, f = Math.floor(t * FPS);
    x += (rnd(f * 3 + t0) - .5) * 2 * d; y += (rnd(f * 7 + t0 * 3) - .5) * 2 * d;
  }
  // Tension croissante avant un noir
  const f = Math.floor(t * FPS);
  for (const [a, b] of TENSION) {
    const ten = prog(t, a, b) * (t < b ? 1 : 0) * 7;
    x += (rnd(f * 11) - .5) * 2 * ten; y += (rnd(f * 13) - .5) * 2 * ten;
  }
  return [x, y];
}

// ------------------------------------------------------------ symbole & logo
// Symbole dessiné dans le repère écran : écran = (ox, oy) + p * s
function drawSymbol(tr, o) {
  ctx.save();
  ctx.translate(tr.ox, tr.oy); ctx.scale(tr.s, tr.s);
  ctx.lineCap = 'butt'; ctx.lineJoin = 'round'; ctx.lineWidth = 20;
  ctx.globalAlpha = o.alpha == null ? 1 : o.alpha;
  if (o.bar > 0) {
    ctx.strokeStyle = COL.chaux;
    if (o.bar < 1) ctx.setLineDash([LEN_BAR * o.bar, LEN_BAR + 10]);
    if (o.glowBar) { ctx.shadowColor = rgba(COL.chaux, .6); ctx.shadowBlur = o.glowBar * tr.s; }
    ctx.stroke(P_BAR); ctx.setLineDash([]); ctx.shadowBlur = 0;
  }
  if (o.rel > 0) {
    ctx.strokeStyle = COL.cuivre;
    if (o.rel < 1) ctx.setLineDash([LEN_REL * o.rel, LEN_REL + 10]);
    if (o.glowRel) { ctx.shadowColor = rgba(COL.cuivre, .9); ctx.shadowBlur = o.glowRel * tr.s; }
    ctx.stroke(P_REL); ctx.setLineDash([]); ctx.shadowBlur = 0;
  }
  if (o.node > 0) {
    ctx.fillStyle = COL.signal;
    ctx.shadowColor = COL.signal; ctx.shadowBlur = (o.nodeGlow || 0) * tr.s;
    ctx.beginPath(); ctx.arc(NODE.x, NODE.y, NODE.r * o.node, 0, Math.PI * 2); ctx.fill();
  }
  ctx.restore();
}
const symPt = (tr, x, y) => [tr.ox + x * tr.s, tr.oy + y * tr.s];

// ------------------------------------------------------------ effets
function drawPolyPartial(pts, L, p) {
  let rem = L * p;
  ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]);
  let last = pts[0];
  for (let k = 1; k < pts.length && rem > 0; k++) {
    const [x0, y0] = pts[k - 1], [x1, y1] = pts[k];
    const d = Math.hypot(x1 - x0, y1 - y0), u = Math.min(1, rem / d);
    last = [x0 + (x1 - x0) * u, y0 + (y1 - y0) * u];
    ctx.lineTo(last[0], last[1]); rem -= d;
  }
  ctx.stroke();
  return last;
}
// Étincelles
function sparks(t, t0, n, x, y, seed, colors, spd = 1) {
  const dt = t - t0;
  if (dt <= 0 || dt > 2.2) return;
  ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.lineCap = 'round';
  for (let i = 0; i < n; i++) {
    const life = .5 + rnd(seed + i * 3) * 1.3;
    if (dt > life) continue;
    const a = rnd(seed + i) * Math.PI * 2, v = (250 + rnd(seed + i * 7) * 1300) * spd;
    const drag = 2.2, g = 520;
    const f = (1 - Math.exp(-drag * dt)) / drag;
    const px = x + Math.cos(a) * v * f, py = y + Math.sin(a) * v * f + .5 * g * dt * dt;
    const vx = Math.cos(a) * v * Math.exp(-drag * dt), vy = Math.sin(a) * v * Math.exp(-drag * dt) + g * dt;
    const al = 1 - dt / life;
    ctx.strokeStyle = rgba(colors[i % colors.length], al);
    ctx.lineWidth = 1.5 + rnd(seed + i * 11) * 2.5;
    ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(px - vx * .03, py - vy * .03); ctx.stroke();
  }
  ctx.restore();
}
function ring(t, t0, x, y, maxR, dur, color, w) {
  const k = prog(t, t0, t0 + dur);
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.globalCompositeOperation = 'lighter';
  ctx.strokeStyle = rgba(color, (1 - k) * .9); ctx.lineWidth = w * (1 - k) + 1;
  ctx.beginPath(); ctx.arc(x, y, maxR * eo3(k), 0, Math.PI * 2); ctx.stroke();
  ctx.restore();
}
function flare(x, y, a, len = 1500, color = COL.signal) {
  if (a <= 0) return;
  ctx.save(); ctx.globalCompositeOperation = 'lighter';
  const g = ctx.createLinearGradient(x - len / 2, 0, x + len / 2, 0);
  g.addColorStop(0, rgba(color, 0)); g.addColorStop(.5, rgba(color, a)); g.addColorStop(1, rgba(color, 0));
  ctx.fillStyle = g;
  ctx.filter = 'blur(3px)';
  ctx.fillRect(x - len / 2, y - 3, len, 6);
  ctx.globalAlpha = .5; ctx.fillRect(x - len / 4, y - 1, len / 2, 2);
  ctx.restore();
}

function drawPolyPartialPoint(pts, L, p) {
  let rem = L * p;
  for (let k = 1; k < pts.length; k++) {
    const [x0, y0] = pts[k - 1], [x1, y1] = pts[k];
    const d = Math.hypot(x1 - x0, y1 - y0);
    if (rem <= d) return [x0 + (x1 - x0) * rem / d, y0 + (y1 - y0) * rem / d];
    rem -= d;
  }
  return pts[pts.length - 1];
}

// ------------------------------------------------------------ démarrage
function boot(renderFrame, dur) {
  window.CUES = CUES; window.DUR = dur; window.FPS = FPS;
  window.renderFrame = renderFrame;
  window.ready = (async () => {
    const specs = ['300 20px Sora', '600 20px Sora', '700 20px Sora', '500 20px Manrope', 'italic 400 20px Serif', '400 20px Mono', '500 20px Mono'];
    await Promise.all(specs.map(s => document.fonts.load(s, 'AÔé…·²×Ø■')));
    await document.fonts.ready;
    renderFrame(0);
    return true;
  })();
  // Aperçu interactif dans un navigateur (espace = pause)
  if (!/headless/i.test(navigator.userAgent)) {
    let t0 = performance.now(), paused = false, tp = 0;
    addEventListener('keydown', e => { if (e.code === 'Space') { paused = !paused; if (!paused) t0 = performance.now() - tp * 1000; } });
    const loop = () => { if (!paused) { tp = ((performance.now() - t0) / 1000) % dur; renderFrame(tp); } requestAnimationFrame(loop); };
    window.ready.then(() => requestAnimationFrame(loop));
  }
}
