// « Tonton Ferraille présente CivRebar AI » — motion design vertical 1080x1920, calé sur voix.json.
// Couches : fond → graphismes arrière → Tonton (3D) → graphismes avant et sous-titres.
import * as THREE from 'three';
import { createStudio } from '../studio.js';
import { POSES, EXPR } from '../poses.js';

const W = 1080, H = 1920, FPS = 30;
const V = await (await fetch('voix.json')).json();
const DUR = V.dur;
const S = Object.fromEntries(V.segments.map(s => [s.id, s]));
const COL = { nuit: '#0B1624', acier: '#1C2B3D', cuivre: '#C8773F', cuivreC: '#E3A56C', signal: '#35D0DE', beton: '#B9BEC4', chaux: '#F3F0EA', rouge: '#D64545' };

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
const wt = (seg, w) => { const s = S[seg]; const x = s.words.find(o => o.w.toLowerCase().includes(w.toLowerCase())); return x ? x.t : s.t0; };
const end = seg => S[seg].t1;
const beg = seg => S[seg].t0;

// ------------------------------------------------------------ 3D
const st = createStudio(W, H);
const { renderer, scene, camera, tonton } = st;
const P = tonton.parts;
const out = document.getElementById('c');
const ctx = out.getContext('2d');

// Chorégraphie : [instant, pose, expression]
const KEYS = [
  [0, 'idle', 'happy'],
  [beg('accroche') - 0.1, 'point', 'surprised'],
  [wt('accroche', 'oui') - 0.1, 'point', 'happy'],
  [beg('intro'), 'explain', 'proud'],
  [wt('intro', 'aujourd'), 'idle', 'happy'],
  [beg('probleme'), 'think', 'think'],
  [wt('probleme', 'Trait'), 'explain', 'serious'],
  [beg('erreurs'), 'angry', 'angry'],
  [beg('solution'), 'idle', 'surprised'],
  [wt('solution', 'CivRebar') - 0.2, 'cheer', 'happy'],
  [wt('solution', 'outil'), 'explain', 'proud'],
  [beg('demo'), 'pointUp', 'happy'],
  [wt('demo', 'lui'), 'pointUp', 'proud'],
  [beg('route'), 'count', 'happy'],
  [beg('signal'), 'lookSignal', 'surprised'],
  [wt('signal', 'assistant'), 'lookSignal', 'happy'],
  [beg('promesse'), 'explain', 'serious'],
  [wt('promesse', 'attention'), 'finger', 'serious'],
  [beg('citation'), 'cross', 'proud'],
  [beg('logo'), 'salute', 'proud'],
  [beg('fin'), 'wave', 'happy'],
];
const PKEYS = ['rX', 'rZ', 'rElbow', 'lX', 'lZ', 'lElbow', 'headNod', 'headTurn', 'headTilt', 'bow', 'lean', 'turn'];
const XKEYS = ['brow', 'browAngle', 'lid', 'lookX', 'lookY', 'open'];
function blendKeys(t) {
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

function updateTonton(t) {
  const { pose, ex, name } = blendKeys(t);
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
  sg.visible = t > beg('intro');
  const orb = prog(t, beg('signal'), end('signal') + 0.4);
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

// Caméra : cadrage plan moyen, Tonton en bas de l'écran, légers mouvements
const CAMS = [
  [0, { az: 0, dist: 6.4, ty: 2.3, tx: 0 }],
  [beg('accroche'), { az: 0.05, dist: 5.6, ty: 2.35, tx: 0 }],
  [beg('intro'), { az: -0.18, dist: 6.2, ty: 2.3, tx: 0 }],
  [beg('probleme'), { az: 0.22, dist: 6.4, ty: 2.25, tx: 0 }],
  [beg('erreurs'), { az: 0.0, dist: 5.4, ty: 2.35, tx: 0 }],
  [beg('solution'), { az: -0.12, dist: 6.6, ty: 2.25, tx: 0 }],
  [beg('demo'), { az: 0.2, dist: 6.6, ty: 2.25, tx: 0 }],
  [beg('route'), { az: -0.2, dist: 6.2, ty: 2.3, tx: 0 }],
  [beg('signal'), { az: 0.3, dist: 5.8, ty: 2.35, tx: 0 }],
  [beg('promesse'), { az: -0.1, dist: 6.2, ty: 2.3, tx: 0 }],
  [beg('citation'), { az: 0.0, dist: 5.2, ty: 2.4, tx: 0 }],
  [beg('logo'), { az: 0.15, dist: 6.6, ty: 2.25, tx: 0 }],
  [beg('fin'), { az: 0, dist: 6.2, ty: 2.3, tx: 0 }],
];
function updateCamera(t) {
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

function scenes(t, front) {
  // --- accroche
  if (!front) {
    const a = win(t, beg('accroche') - 0.1, beg('intro') + 0.05, 0.1, 0.3);
    slam(t, beg('accroche'), 'EH ! TOI LÀ !', W / 2, 420, font(700, 118), COL.chaux, { alpha: a, stroke: 0 });
    slam(t, wt('accroche', 'oui'), 'OUI, TOI, L’INGÉNIEUR !', W / 2, 540, font(600, 54), COL.cuivreC, { alpha: a });
  }
  // --- intro : carte de nom
  if (!front) {
    const a = win(t, beg('intro') + 0.1, beg('probleme'), 0.3, 0.3);
    if (a > 0) {
      const k = eoX(prog(t, beg('intro') + 0.1, beg('intro') + 0.6));
      const x = lerp(-700, 90, k);
      ctx.save(); ctx.globalAlpha = a;
      roundRect(x, 300, 900, 200, 26, COL.cuivre);
      txt('TONTON FERRAILLE', x + 40, 395, font(700, 70), COL.nuit, { align: 'left', track: 2 });
      txt('Chef de chantier · 30 ans d’expérience', x + 42, 455, font(600, 36, 'Manrope'), COL.nuit, { align: 'left' });
      ctx.restore();
      const kl = prog(t, wt('intro', 'CivRebar') - 0.1, wt('intro', 'CivRebar') + 0.3);
      if (kl > 0) { drawSymbol(W / 2, 640, 0.42 * eoB(kl), a); }
    }
  }
  // --- problème : plan dessiné à la main + horloge
  if (!front) {
    const t0 = beg('probleme'), t1 = beg('erreurs') + 0.3;
    const a = panelBox(t, t0, end('erreurs') + 0.15);
    if (a > 0) {
      txt('À LA MAIN…', 140, 310, font(500, 30, 'Mono'), COL.signal, { align: 'left', track: 6, alpha: a });
      const kk = clamp((t - t0 - 0.4) / (end('probleme') - t0 - 0.2)) * 0.8;
      beam(t, 150, 380, W - 300, 150, kk, a, true);
      // étiquettes « barre / cadre / cote »
      [['barre', COL.cuivreC, 230], ['cadre', COL.chaux, 540], ['cote', COL.signal, 850]].forEach(([w, c, x]) => {
        const k = prog(t, wt('probleme', w), wt('probleme', w) + 0.25);
        if (k > 0) { ctx.save(); ctx.globalAlpha = a; ctx.translate(x, 600); ctx.scale(eoB(k), eoB(k)); roundRect(-95, -34, 190, 56, 28, rgba(c, .16), c, 2); txt(w.toUpperCase(), 0, 6, font(600, 30), c); ctx.restore(); }
      });
      // horloge
      const hc = 880, vc = 300, r = 34, ang = (t - t0) * 2.6;
      ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = COL.chaux; ctx.lineWidth = 4; ctx.beginPath(); ctx.arc(hc, vc, r, 0, 7); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(hc, vc); ctx.lineTo(hc + Math.sin(ang) * r * 0.8, vc - Math.cos(ang) * r * 0.8); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(hc, vc); ctx.lineTo(hc + Math.sin(ang / 12) * r * 0.5, vc - Math.cos(ang / 12) * r * 0.5); ctx.stroke(); ctx.restore();
      // erreurs : compteur d'heures + croix rouges
      const ke = prog(t, beg('erreurs'), beg('erreurs') + 0.3);
      if (ke > 0) {
        ctx.save(); ctx.globalAlpha = a * 0.94 * ke; ctx.fillStyle = COL.nuit; ctx.fillRect(84, 234, W - 168, 432); ctx.restore();
        const h = Math.floor(lerp(1, 6, eo3(prog(t, beg('erreurs'), wt('erreurs', 'perdues') + 0.2))));
        slam(t, beg('erreurs'), `+ ${h} HEURES`, W / 2, 400, font(700, 104), COL.chaux, { alpha: a });
        [[380, 510], [540, 510], [700, 510]].forEach(([x, y], i) => {
          const k = prog(t, wt('erreurs', 'erreurs') + i * 0.18, wt('erreurs', 'erreurs') + i * 0.18 + 0.2);
          if (k > 0) { ctx.save(); ctx.globalAlpha = a; ctx.translate(x, y); ctx.scale(eoB(k) * 0.75, eoB(k) * 0.75); ctx.strokeStyle = COL.rouge; ctx.lineWidth = 16; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(-34, -34); ctx.lineTo(34, 34); ctx.moveTo(34, -34); ctx.lineTo(-34, 34); ctx.stroke(); ctx.restore(); }
        });
        slam(t, wt('erreurs', 'erreurs'), 'ERREURS SUR LE CHANTIER', W / 2, 625, font(700, 44), COL.rouge, { alpha: a });
      }
    }
  }
  // --- solution : logo
  if (!front) {
    const t0 = wt('solution', 'CivRebar') - 0.15;
    const a = win(t, t0, beg('demo') + 0.1, 0.2, 0.35);
    if (a > 0) {
      const k = eoB(prog(t, t0, t0 + 0.6));
      ctx.save(); ctx.globalAlpha = a;
      // rayons
      ctx.translate(W / 2, 340); ctx.rotate(t * 0.25);
      for (let i = 0; i < 16; i++) { ctx.rotate(Math.PI / 8); ctx.fillStyle = rgba(COL.cuivre, 0.06); ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(-40, -700); ctx.lineTo(40, -700); ctx.fill(); }
      ctx.restore();
      glow(W / 2, 340, 380, COL.signal, 0.25 * a);
      ctx.save(); ctx.translate(W / 2, 340); ctx.scale(k, k); ctx.translate(-W / 2, -340); lockup(W / 2, 340, 1, a); ctx.restore();
      const kb = prog(t, wt('solution', 'AutoCAD') - 0.2, wt('solution', 'AutoCAD') + 0.1);
      if (kb > 0) { ctx.save(); ctx.globalAlpha = a * kb; roundRect(W / 2 - 330, 555, 660, 64, 32, COL.signal); txt('DIRECTEMENT DANS AUTOCAD', W / 2, 598, font(700, 30), COL.nuit, { track: 2 }); ctx.restore(); }
    }
  }
  // --- démo : fiche + poutre automatique
  if (!front) {
    const t0 = beg('demo'), t1 = end('demo') + 0.25;
    const a = panelBox(t, t0, t1);
    if (a > 0) {
      const fields = [['Section', '30 × 60 cm', 'section'], ['Portée', '5,40 m', 'portée'], ['Armatures', '3 HA20 / 2 HA14', 'armatures']];
      const draw0 = wt('demo', 'lui');
      const kf = 1 - prog(t, draw0 - 0.1, draw0 + 0.2);
      fields.forEach(([l, v, w], i) => {
        const tt = wt('demo', w), n = Math.floor(clamp((t - tt) / 0.5) * v.length);
        const y = 330 + i * 92;
        ctx.save(); ctx.globalAlpha = a * kf;
        txt(l, 140, y + 12, font(500, 34, 'Mono'), COL.beton, { align: 'left' });
        roundRect(440, y - 32, 500, 64, 12, null, 'rgba(185,190,196,.35)', 2);
        txt(v.slice(0, n), 466, y + 12, font(500, 36, 'Mono'), COL.chaux, { align: 'left' });
        ctx.restore();
      });
      if (t > draw0) {
        beam(t, 150, 330, W - 300, 170, clamp((t - draw0) / 1.4), a);
        const labs = [['barres', 'BARRES', COL.cuivreC, 200], ['cadres', 'CADRES', COL.chaux, 420], ['cotes', 'COTES', COL.signal, 640], ['repères', 'REPÈRES', COL.chaux, 860]];
        labs.forEach(([w, s, c, x]) => {
          const k = prog(t, wt('demo', w), wt('demo', w) + 0.25);
          if (k > 0) { ctx.save(); ctx.globalAlpha = a; ctx.translate(x, 590); ctx.scale(eoB(k), eoB(k)); txt('✓ ' + s, 0, 0, font(700, 34), c); ctx.restore(); }
        });
      }
      txt('CIVREBAR AI · POUTRE', 140, 262, font(500, 24, 'Mono'), COL.signal, { align: 'left', track: 4, alpha: a });
    }
  }
  // --- feuille de route
  if (!front) {
    const t0 = beg('route'), t1 = end('route') + 0.3;
    const a = win(t, t0, t1, 0.3, 0.3);
    if (a > 0) {
      const items = [['poutre', 'POUTRE', true], ['poteaux', 'POTEAUX'], ['dalles', 'DALLES'], ['semelles', 'SEMELLES'], ['escaliers', 'ESCALIERS']];
      const x0 = 150, x1 = W - 150, y = 470;
      ctx.save(); ctx.globalAlpha = a;
      ctx.strokeStyle = rgba(COL.beton, .25); ctx.lineWidth = 10; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
      const reach = clamp((t - wt('route', 'poutre')) / (wt('route', 'escaliers') - wt('route', 'poutre')));
      ctx.strokeStyle = COL.cuivre; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x0 + (x1 - x0) * eio(reach), y); ctx.stroke();
      ctx.restore();
      items.forEach(([w, s, first], i) => {
        const x = x0 + (x1 - x0) * i / 4, tk = wt('route', w), k = prog(t, tk, tk + 0.3);
        ctx.save(); ctx.globalAlpha = a;
        ctx.fillStyle = k > 0 ? (first ? COL.cuivre : COL.chaux) : COL.acier; ctx.strokeStyle = rgba(COL.beton, .5); ctx.lineWidth = 3;
        ctx.beginPath(); ctx.arc(x, y, 22 + 10 * decay(t, tk, 6), 0, 7); ctx.fill(); if (k <= 0) ctx.stroke();
        if (k > 0) {
          ctx.translate(x, i % 2 ? 560 : 400); ctx.scale(eoB(k), eoB(k));
          txt(s, 0, 0, font(700, i === 0 ? 40 : 34), first ? COL.cuivreC : COL.chaux);
          if (first) txt('EN COURS', 0, 40, font(500, 22, 'Mono'), COL.signal, { track: 4 });
        }
        ctx.restore();
      });
      txt('LA FEUILLE DE ROUTE', W / 2, 300, font(500, 30, 'Mono'), COL.signal, { track: 6, alpha: a });
    }
  }
  // --- Signal (avant-plan : étiquette)
  if (front) {
    const a = win(t, wt('signal', 'Signal'), end('signal') + 0.2, 0.3, 0.3);
    if (a > 0) {
      slam(t, wt('signal', 'Signal'), 'SIGNAL', W / 2, 380, font(700, 110), COL.signal, { alpha: a, track: 8 });
      slam(t, wt('signal', 'intelligence') - 0.1, 'L’IA QUI T’ASSISTE', W / 2, 470, font(600, 46), COL.chaux, { alpha: a });
    }
  }
  // --- promesse : l'IA vérifie / l'ingénieur signe + tampon
  if (!front) {
    const t0 = beg('promesse'), t1 = end('promesse') + 0.3;
    const a = panelBox(t, t0, t1);
    if (a > 0) {
      txt('À TERME, L’IA…', 140, 320, font(500, 28, 'Mono'), COL.signal, { align: 'left', track: 5, alpha: a });
      [['vérifiera', '✓ vérifie les plans', 400], ['quantités', '✓ calcule les quantités', 470]].forEach(([w, s, y]) => {
        const k = prog(t, wt('promesse', w), wt('promesse', w) + 0.3);
        if (k > 0) txt(s, 140 + (1 - eoX(k)) * 40, y, font(600, 44), COL.chaux, { align: 'left', alpha: a * k });
      });
      const kd = prog(t, wt('promesse', 'ingénieur') - 0.1, wt('promesse', 'ingénieur') + 0.3);
      if (kd > 0) txt('L’INGÉNIEUR DÉCIDE.', 140, 575, font(700, 50), COL.cuivreC, { align: 'left', alpha: a * kd });
      const ts = wt('promesse', 'signe');
      const ks = prog(t, ts, ts + 0.22);
      if (ks > 0) {
        ctx.save(); ctx.globalAlpha = a; ctx.translate(850, 555); ctx.rotate(-0.18); ctx.scale(lerp(2, 0.72, eoX(ks)), lerp(2, 0.72, eoX(ks)));
        roundRect(-150, -58, 300, 116, 16, null, COL.rouge, 8);
        txt('SIGNÉ', 0, 22, font(700, 64), COL.rouge, { track: 6 });
        ctx.restore();
      }
    }
  }
  // --- citation (avant-plan, sur voile sombre)
  if (front) {
    const a = win(t, beg('citation') - 0.1, beg('logo'), 0.3, 0.3);
    if (a > 0) {
      ctx.save(); ctx.globalAlpha = a * 0.55; ctx.fillStyle = '#050b14'; ctx.fillRect(0, 0, W, H); ctx.restore();
      const k1 = prog(t, beg('citation'), beg('citation') + 0.5), k2 = prog(t, wt('citation', 'tout'), wt('citation', 'tout') + 0.5);
      txt('« Rien n’y est', W / 2, 400, font('italic 400', 96, 'Serif'), COL.chaux, { alpha: a * k1 });
      txt('décoratif…', W / 2, 500, font('italic 400', 96, 'Serif'), COL.chaux, { alpha: a * k1 });
      txt('tout y est calculé. »', W / 2, 620, font('italic 400', 96, 'Serif'), COL.cuivreC, { alpha: a * k2 });
    }
  }
  // --- logo final + appel à l'action
  if (!front) {
    const t0 = beg('logo') - 0.1;
    const a = win(t, t0, DUR + 1, 0.3, 0.3);
    if (a > 0) {
      const k = eoB(prog(t, t0, t0 + 0.6));
      glow(W / 2, 340, 420, COL.signal, 0.18 * a);
      ctx.save(); ctx.translate(W / 2, 330); ctx.scale(k * 0.95, k * 0.95); ctx.translate(-W / 2, -330); lockup(W / 2, 330, 1, a); ctx.restore();
      const kt = prog(t, wt('logo', 'intelligence') - 0.1, wt('logo', 'intelligence') + 0.4);
      txt('L’intelligence de l’armature.', W / 2, 565, font('italic 400', 54, 'Serif'), COL.beton, { alpha: a * kt });
      const kb = prog(t, wt('logo', 'Bientôt'), wt('logo', 'Bientôt') + 0.3);
      if (kb > 0) { ctx.save(); ctx.globalAlpha = a * kb; roundRect(W / 2 - 270, 600, 540, 62, 31, null, COL.cuivre, 3); txt('BIENTÔT DANS AUTOCAD', W / 2, 642, font(700, 30), COL.cuivreC, { track: 3 }); ctx.restore(); }
    }
  }
  if (front) {
    const tb = wt('fin', 'Abonne');
    const k = prog(t, tb, tb + 0.35);
    if (k > 0) {
      const press = decay(t, tb + 0.9, 7);
      ctx.save(); ctx.translate(W / 2, 1420); ctx.scale(eoB(k) * (1 - press * 0.08), eoB(k) * (1 - press * 0.08));
      roundRect(-250, -60, 500, 120, 60, t > tb + 0.9 ? COL.acier : COL.cuivre);
      txt(t > tb + 0.9 ? '✓ ABONNÉ' : '+ ABONNE-TOI', 0, 16, font(700, 46), t > tb + 0.9 ? COL.chaux : COL.nuit, { track: 1 });
      ctx.restore();
      if (t > tb + 0.5 && t < tb + 1.4) { // main-curseur qui tape
        const kk = eio(prog(t, tb + 0.5, tb + 0.9));
        const x = lerp(W / 2 + 320, W / 2 + 120, kk), y = lerp(1560, 1450, kk);
        ctx.save(); ctx.fillStyle = COL.chaux; ctx.strokeStyle = COL.nuit; ctx.lineWidth = 4;
        ctx.beginPath(); ctx.arc(x, y, 26 - press * 6, 0, 7); ctx.fill(); ctx.stroke(); ctx.restore();
      }
    }
  }
}

// ------------------------------------------------------------ sous-titres (mot à mot)
function captions(t) {
  const seg = V.segments.find(s => t >= s.t0 - 0.05 && t <= s.t1 + 0.25);
  if (!seg || seg.id === 'citation') return;
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

// ------------------------------------------------------------ rendu d'une image
function renderFrame(t) {
  updateTonton(t); updateCamera(t);
  renderer.render(scene, camera);
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1; ctx.filter = 'none';
  background(t);
  scenes(t, false);
  ctx.drawImage(renderer.domElement, 0, 0);
  scenes(t, true);
  captions(t);
  // flashs sur les temps forts
  const fl = Math.max(0.7 * decay(t, wt('solution', 'CivRebar') - 0.15, 6), 0.5 * decay(t, 0.15, 8), 0.4 * decay(t, beg('logo') - 0.1, 7));
  if (fl > 0.01) { ctx.fillStyle = `rgba(243,240,234,${fl})`; ctx.fillRect(0, 0, W, H); }
  const v = ctx.createRadialGradient(W / 2, H / 2, H * 0.35, W / 2, H / 2, H * 0.75);
  v.addColorStop(0, 'rgba(0,0,0,0)'); v.addColorStop(1, 'rgba(0,0,0,.45)');
  ctx.fillStyle = v; ctx.fillRect(0, 0, W, H);
  const fade = Math.max(1 - prog(t, 0, 0.25), prog(t, DUR - 0.8, DUR));
  if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
}

// Repères sonores pour le mixage
const CUES = [
  { t: 0.15, type: 'pop' }, { t: beg('accroche'), type: 'slam' }, { t: wt('accroche', 'oui'), type: 'pop' },
  { t: beg('intro'), type: 'whoosh' }, { t: wt('intro', 'CivRebar'), type: 'pop' },
  { t: beg('probleme'), type: 'whoosh' }, { t: wt('probleme', 'barre'), type: 'pop' }, { t: wt('probleme', 'cadre'), type: 'pop' }, { t: wt('probleme', 'cote'), type: 'pop' },
  { t: beg('erreurs'), type: 'slam' }, { t: wt('erreurs', 'erreurs'), type: 'error' }, { t: wt('erreurs', 'erreurs') + 0.18, type: 'error' }, { t: wt('erreurs', 'erreurs') + 0.36, type: 'error' },
  { t: wt('solution', 'CivRebar') - 0.8, type: 'riser' }, { t: wt('solution', 'CivRebar') - 0.15, type: 'boom' }, { t: wt('solution', 'AutoCAD') - 0.2, type: 'pop' },
  { t: beg('demo'), type: 'whoosh' }, { t: wt('demo', 'lui'), type: 'draw' },
  ...['barres', 'cadres', 'cotes', 'repères'].map(w => ({ t: wt('demo', w), type: 'tick' })),
  { t: beg('route'), type: 'whoosh' }, ...['poutre', 'poteaux', 'dalles', 'semelles', 'escaliers'].map(w => ({ t: wt('route', w), type: 'blip' })),
  { t: wt('signal', 'Signal'), type: 'shine' }, { t: wt('signal', 'intelligence'), type: 'chime' },
  { t: beg('promesse'), type: 'whoosh' }, { t: wt('promesse', 'vérifiera'), type: 'tick' }, { t: wt('promesse', 'quantités'), type: 'tick' }, { t: wt('promesse', 'signe'), type: 'stamp' },
  { t: beg('citation') - 0.1, type: 'swell' }, { t: beg('logo') - 0.1, type: 'boom' }, { t: wt('logo', 'Bientôt'), type: 'pop' },
  { t: wt('fin', 'Abonne'), type: 'pop' }, { t: wt('fin', 'Abonne') + 0.9, type: 'click' },
];

window.DUR = DUR; window.FPS = FPS; window.CUES = CUES;
window.renderFrame = t => { renderFrame(t); return out.toDataURL('image/jpeg', 0.92); };
await document.fonts.ready;
renderFrame(0);
window.ready = true;
