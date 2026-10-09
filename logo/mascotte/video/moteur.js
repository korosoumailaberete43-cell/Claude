// Moteur des vidéos de Tonton Ferraille (format vertical 1080x1920).
// Chaque épisode fournit : KEYS (poses calées sur la voix), CAMS (caméra), scenes(t, front), CUES (sons), flashes.
// Couches : fond → graphismes arrière → Tonton (3D) → graphismes avant → sous-titres.
import { createStudio } from '../studio.js';
import { POSES, EXPR } from '../poses.js';

export const W = 1080, H = 1920, FPS = 30;
export const COL = { nuit: '#0B1624', acier: '#1C2B3D', cuivre: '#C8773F', cuivreC: '#E3A56C', signal: '#35D0DE', beton: '#B9BEC4', chaux: '#F3F0EA', rouge: '#D64545', vert: '#4CC38A' };
let V, S, ctx, out, st, camera, renderer, scene, tonton, P, DUR;

// ------------------------------------------------------------ outils
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const prog = (t, a, b) => clamp((t - a) / (b - a));
const lerp = (a, b, k) => a + (b - a) * k;
const eo3 = k => 1 - Math.pow(1 - k, 3);
const eio = k => (k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2);
const eoX = k => (k >= 1 ? 1 : 1 - Math.pow(2, -10 * k));
const eoB = k => { const c1 = 1.9, c3 = c1 + 1; return 1 + c3 * Math.pow(k - 1, 3) + c1 * Math.pow(k - 1, 2); };
const rnd = n => { const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
const decay = (t, t0, r) => (t < t0 ? 0 : Math.exp(-(t - t0) * r));
const win = (t, a, b, fi = .3, fo = .3) => Math.min(prog(t, a, a + fi), 1 - prog(t, b - fo, b));
const rgba = (hex, a) => { const n = parseInt(hex.slice(1), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; };
// instant où un mot du segment est prononcé
export const wt = (seg, w) => { const s = S[seg]; const x = s.words.find(o => o.w.toLowerCase().includes(w.toLowerCase())); return x ? x.t : s.t0; };
export const end = seg => S[seg].t1;
export const beg = seg => S[seg].t0;


export { clamp, prog, lerp, eo3, eio, eoX, eoB, rnd, decay, win, rgba };

const PKEYS = ['rX', 'rZ', 'rElbow', 'lX', 'lZ', 'lElbow', 'headNod', 'headTurn', 'headTilt', 'bow', 'lean', 'turn'];
const XKEYS = ['brow', 'browAngle', 'lid', 'lookX', 'lookY', 'open'];
function blendKeys(t, KEYS) {
  let i = 0; while (i < KEYS.length - 1 && KEYS[i + 1][0] <= t) i++;
  const [t0, p0, e0] = KEYS[i], prev = KEYS[Math.max(0, i - 1)];
  const k = eio(prog(t, t0, t0 + 0.35));
  const pa = { ...POSES.idle, ...POSES[prev[1]] }, pb = { ...POSES.idle, ...POSES[p0] };
  const pose = {}; for (const key of PKEYS) pose[key] = lerp(pa[key] || 0, pb[key] || 0, i === 0 ? 1 : k);
  const ea = EXPR[prev[2]], eb = EXPR[e0];
  const ex = {}; for (const key of XKEYS) ex[key] = lerp(ea[key] || 0, eb[key] || 0, i === 0 ? 1 : k);
  ex.mouth = (k > 0.5 ? eb : ea).mouth;
  return { pose, ex, name: p0 };
}
const mouthAt = t => { const f = Math.floor(t * FPS); return V.mouth[f] || 0; };

function updateTonton(t, E) {
  const { pose, ex, name } = blendKeys(t, E.KEYS);
  const talk = clamp(mouthAt(t) * 1.1);
  const speaking = V.segments.some(s => t >= s.t0 && t <= s.t1);
  // vie : respiration, hochements en parlant, clignements
  pose.headNod += speaking ? Math.sin(t * 7.3) * 0.035 * talk : Math.sin(t * 1.3) * 0.015;
  pose.headTurn += Math.sin(t * 0.9) * 0.05;
  if (name === 'wave') pose.rZ += Math.sin(t * 9) * 0.28;
  if (name === 'count') { pose.rElbow += Math.sin(t * 4) * 0.2; }
  if (name === 'explain') pose.rX += Math.sin(t * 3.1) * 0.12 * (speaking ? 1 : 0.3);
  pose.bounce = Math.abs(Math.sin(t * 2.2)) * 0.012;
  // entrée : Tonton surgit du sol avec un rebond
  const pop = eoB(prog(t, 0.15, 0.75));
  tonton.root.scale.setScalar(Math.max(0.001, pop));
  tonton.setPose(pose);
  const blink = (t % 3.4) < 0.11 ? 1 : 0;
  tonton.setExpression({ ...ex, mouth: speaking && talk > 0.12 ? ex.mouth : ex.mouth, talk: speaking ? talk : 0, lid: Math.max(ex.lid || 0, blink) });
  P.torso.scale.set(1, 1 + Math.sin(t * 2.1) * 0.008, 1);
  // Signal : flotte près de l'épaule ; entre en scène pendant « signal »
  const sg = P.signal;
  sg.visible = E.signalVisible ? E.signalVisible(t) : true;
  const orb = E.orbit ? prog(t, E.orbit[0], E.orbit[1]) : 0;
  if (orb > 0 && orb < 1) {
    const a = orb * Math.PI * 3.2 + 0.5;
    const r = lerp(1.1, 0.95, orb);
    sg.position.set(Math.cos(a) * r, 2.35 + Math.sin(orb * Math.PI) * 0.35, Math.sin(a) * r + 0.3);
    sg.scale.setScalar(1 + Math.sin(orb * Math.PI) * 0.9);
  } else {
    sg.position.set(0.95 + Math.sin(t * 1.4) * 0.05, 2.45 + Math.sin(t * 2) * 0.07, 0.4);
    sg.scale.setScalar(1);
  }
}

function updateCamera(t, CAMS) {
  let i = 0; while (i < CAMS.length - 1 && CAMS[i + 1][0] <= t) i++;
  const a = CAMS[Math.max(0, i - 1)][1], b = CAMS[i][1];
  const k = i === 0 ? 1 : eio(prog(t, CAMS[i][0], CAMS[i][0] + 0.9));
  const c = {}; for (const key in b) c[key] = lerp(a[key], b[key], k);
  const az = c.az + Math.sin(t * 0.35) * 0.04, el = 0.07;
  camera.fov = 30; camera.aspect = W / H; camera.updateProjectionMatrix();
  camera.position.set(c.tx + Math.sin(az) * Math.cos(el) * c.dist, c.ty + Math.sin(el) * c.dist, Math.cos(az) * Math.cos(el) * c.dist);
  camera.lookAt(c.tx, c.ty, 0);
}

// ------------------------------------------------------------ 2D : textes
function font(w, size, fam = 'Sora') { return `${w} ${size}px ${fam}`; }
function txt(s, x, y, f, color, { align = 'center', track = 0, alpha = 1, stroke = 0, strokeColor = COL.nuit } = {}) {
  if (alpha <= 0) return;
  ctx.save(); ctx.globalAlpha *= alpha; ctx.font = f; ctx.letterSpacing = track + 'px'; ctx.textAlign = align; ctx.textBaseline = 'alphabetic';
  if (stroke) { ctx.lineJoin = 'round'; ctx.lineWidth = stroke; ctx.strokeStyle = strokeColor; ctx.strokeText(s, x, y); }
  ctx.fillStyle = color; ctx.fillText(s, x, y); ctx.restore();
}
function slam(t, t0, s, x, y, f, color, opts = {}) {
  const k = prog(t, t0, t0 + 0.3);
  if (k <= 0) return;
  const e = eoX(k), sc = lerp(1.8, 1, e);
  ctx.save(); ctx.translate(x, y); ctx.scale(sc, sc); ctx.rotate(opts.rot || 0);
  txt(s, 0, 0, f, color, { ...opts, alpha: (opts.alpha == null ? 1 : opts.alpha) * clamp(k * 3) });
  ctx.restore();
}
function roundRect(x, y, w, h, r, fill, stroke, lw = 2) {
  ctx.beginPath(); ctx.roundRect(x, y, w, h, r);
  if (fill) { ctx.fillStyle = fill; ctx.fill(); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; ctx.stroke(); }
}
function glow(x, y, r, c, a) {
  if (a <= 0) return;
  const g = ctx.createRadialGradient(x, y, 0, x, y, r);
  g.addColorStop(0, rgba(c, a)); g.addColorStop(1, rgba(c, 0));
  ctx.fillStyle = g; ctx.fillRect(x - r, y - r, 2 * r, 2 * r);
}
// Logo « R façonné » officiel
function drawSymbol(x, y, s, a = 1, bar = COL.chaux) {
  ctx.save(); ctx.globalAlpha = a; ctx.translate(x, y); ctx.scale(s, s); ctx.translate(-125, -135);
  ctx.lineWidth = 20; ctx.lineJoin = 'round';
  ctx.strokeStyle = COL.cuivre; ctx.stroke(new Path2D('M120 160 L180 220 H210'));
  ctx.strokeStyle = bar; ctx.stroke(new Path2D('M50 230 V90 A50 50 0 0 1 100 40 H120 A60 60 0 0 1 120 160 H100 A20 20 0 0 1 85.86 125.86 L105.86 105.86'));
  ctx.fillStyle = COL.signal; ctx.beginPath(); ctx.arc(100, 140, 7, 0, 7); ctx.fill();
  ctx.restore();
}
function lockup(x, y, s, a = 1) {
  drawSymbol(x, y - 120 * s, 0.85 * s, a);
  txt('CIVREBAR', x + 8 * s, y + 70 * s, font(600, 86 * s), COL.chaux, { track: 14 * s, alpha: a });
  ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = COL.cuivre; ctx.fillRect(x - 55 * s, y + 98 * s, 110 * s, 4 * s); ctx.restore();
  txt('A I', x + 4 * s, y + 160 * s, font(300, 52 * s), COL.cuivre, { track: 10 * s, alpha: a });
}

// ------------------------------------------------------------ fond
function background(t) {
  const g = ctx.createLinearGradient(0, 0, 0, H);
  g.addColorStop(0, '#0d1b2c'); g.addColorStop(1, '#070f1a');
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  ctx.save(); ctx.strokeStyle = 'rgba(58,85,112,.22)'; ctx.lineWidth = 1;
  const off = (t * 12) % 60;
  for (let x = -60 + off; x < W; x += 60) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
  for (let y = -60 + off; y < H; y += 60) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
  ctx.restore();
  glow(W / 2, 1180, 760, COL.acier, 0.9);
  // poussière de chantier qui flotte
  for (let i = 0; i < 40; i++) {
    const x = (rnd(i) * W + t * (8 + rnd(i + 3) * 18)) % W, y = (rnd(i + 9) * H - t * (6 + rnd(i + 5) * 12) + H) % H;
    ctx.fillStyle = rgba(COL.beton, 0.08 + rnd(i + 2) * 0.12); ctx.beginPath(); ctx.arc(x, y, 1.5 + rnd(i + 1) * 2.5, 0, 7); ctx.fill();
  }
}

// ------------------------------------------------------------ scènes (graphismes du haut, zone y ≈ 200 → 700)
function panelBox(t, t0, t1, y = 230, h = 440) {
  const a = win(t, t0, t1, 0.35, 0.3);
  if (a <= 0) return 0;
  const k = eoB(prog(t, t0, t0 + 0.45));
  ctx.save(); ctx.globalAlpha = a;
  ctx.translate(W / 2, y + h / 2); ctx.scale(lerp(0.85, 1, k), lerp(0.85, 1, k)); ctx.translate(-W / 2, -(y + h / 2));
  roundRect(80, y, W - 160, h, 30, 'rgba(20,34,52,.92)', 'rgba(185,190,196,.22)', 2);
  ctx.restore();
  return a;
}
function beam(t, x0, y0, w, h, prog1, a, manual = false) {
  if (a <= 0 || prog1 <= 0) return;
  ctx.save(); ctx.globalAlpha = a;
  const k = prog1;
  ctx.strokeStyle = rgba(COL.beton, .85); ctx.lineWidth = 3;
  ctx.setLineDash([2 * (w + h) * clamp(k * 2.2), 9999]); ctx.strokeRect(x0, y0, w, h); ctx.setLineDash([]);
  const kb = clamp(k * 2 - 0.35);
  ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 8; ctx.lineCap = 'round';
  [y0 + h * 0.16, y0 + h * 0.84].forEach(y => { ctx.beginPath(); ctx.moveTo(x0 + 18, y); ctx.lineTo(x0 + 18 + (w - 36) * kb, y); ctx.stroke(); });
  const ns = 22, ks = clamp(k * 1.6 - 0.6);
  ctx.strokeStyle = rgba(COL.chaux, .9); ctx.lineWidth = 3;
  for (let i = 0; i < Math.floor(ns * ks); i++) {
    const x = x0 + 34 + (w - 68) * i / (ns - 1);
    ctx.beginPath(); ctx.moveTo(x, y0 + 8); ctx.lineTo(x, y0 + h - 8); ctx.stroke();
  }
  if (manual && k < 1) { // crayon qui trace
    const px = x0 + 18 + (w - 36) * kb, py = y0 + h * 0.84;
    ctx.fillStyle = COL.cuivreC; ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(px + 18, py - 40); ctx.lineTo(px + 34, py - 32); ctx.closePath(); ctx.fill();
  }
  ctx.restore();
}

export { font, txt, slam, roundRect, glow, drawSymbol, lockup, background, panelBox, beam };
export const g = () => ctx;

// ------------------------------------------------------------ sous-titres (mot à mot)
function captions(t, E) {
  const seg = V.segments.find(s => t >= s.t0 - 0.05 && t <= s.t1 + 0.25);
  if (!seg || (E.noCaptions || []).includes(seg.id)) return;
  // groupes de mots : coupure à la ponctuation ou tous les 3 mots
  const groups = []; let g = [];
  seg.words.forEach((w, i) => { g.push(w); if (/[.,!?:…]$/.test(w.w) || g.length === 3 || i === seg.words.length - 1) { groups.push(g); g = []; } });
  let cur = groups[0];
  for (const gr of groups) if (t >= gr[0].t - 0.05) cur = gr;
  const t0 = cur[0].t;
  const k = eoB(prog(t, t0 - 0.05, t0 + 0.18));
  ctx.save(); ctx.translate(W / 2, 1610);
  ctx.font = font(800, 70); ctx.letterSpacing = '0px';
  const words = cur.map(w => w.w.toUpperCase());
  const widths = words.map(w => ctx.measureText(w + ' ').width);
  const fit = Math.min(1, 960 / widths.reduce((a, b) => a + b, 0));
  ctx.scale(lerp(0.85, 1, k) * fit, lerp(0.85, 1, k) * fit);
  let x = -widths.reduce((a, b) => a + b, 0) / 2;
  words.forEach((w, i) => {
    const active = t >= cur[i].t - 0.03;
    ctx.textAlign = 'left'; ctx.lineJoin = 'round'; ctx.lineWidth = 16; ctx.strokeStyle = COL.nuit;
    ctx.strokeText(w, x, 0);
    ctx.fillStyle = active && (i === cur.length - 1 || t < cur[i + 1].t) ? COL.cuivreC : (active ? COL.chaux : 'rgba(243,240,234,.55)');
    ctx.fillText(w, x, 0);
    x += widths[i];
  });
  ctx.restore();
}


// Lance un épisode : charge la voix, prépare la 3D, expose renderFrame au moteur de rendu.
export async function lancer(voixUrl, build) {
  V = await (await fetch(voixUrl)).json();
  DUR = V.dur;
  S = Object.fromEntries(V.segments.map(s => [s.id, s]));
  const par = new URLSearchParams(location.search);
  const q = +(par.get('q') || 0.68);                   // échelle de rendu 3D (0.68 : net à l'écran, bien plus rapide)
  const ombres = +(par.get('ombres') || 1024);         // finesse des ombres
  st = createStudio(Math.round(W * q), Math.round(H * q), { ombres });
  ({ renderer, scene, camera, tonton } = st);
  P = tonton.parts;
  out = document.getElementById('c');
  ctx = out.getContext('2d');
  const E = build({ DUR, S, V });
  function frame(t) {
    updateTonton(t, E); updateCamera(t, E.CAMS);
    renderer.render(scene, camera);
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1; ctx.filter = 'none';
    background(t);
    E.scenes(t, false);
    ctx.drawImage(renderer.domElement, 0, 0, W, H);
    E.scenes(t, true);
    captions(t, E);
    const fl = Math.max(0.5 * decay(t, 0.15, 8), ...(E.flashes || []).map(([t0, a]) => a * decay(t, t0, 6.5)));
    if (fl > 0.01) { ctx.fillStyle = `rgba(243,240,234,${fl})`; ctx.fillRect(0, 0, W, H); }
    const v = ctx.createRadialGradient(W / 2, H / 2, H * 0.35, W / 2, H / 2, H * 0.75);
    v.addColorStop(0, 'rgba(0,0,0,0)'); v.addColorStop(1, 'rgba(0,0,0,.45)');
    ctx.fillStyle = v; ctx.fillRect(0, 0, W, H);
    const fade = Math.max(1 - prog(t, 0, 0.25), prog(t, DUR - 0.8, DUR));
    if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
  }
  window.DUR = DUR; window.FPS = FPS; window.CUES = E.CUES;
  window.renderFrame = t => { frame(t); return out.toDataURL('image/jpeg', 0.92); };
  await document.fonts.ready;
  frame(0);
  window.ready = true;
}
