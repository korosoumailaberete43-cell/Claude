// CivRebar AI — « POV » : format natif TikTok, légendes en autocollants, humour de bureau d'études.
// 1080x1920, 32 s. Nuit blanche à ferrailler à la main → une seule commande → appel à l'action.
const DUR = 32;
const CX = W / 2;

const T = {
  phases: [0.3, 3.5, 5.3, 7.1], freeze: 9.0, etsi: 9.1, cmd: 10.2, rewind: [10.3, 11.8],
  panel: 12.0, fields: [12.2, 12.45, 12.7, 12.95], click: 13.4, draw: 13.6, grid: 14.8, done: 17.4, lit: 18.3,
  logo: 19.8, clang: 21.2, letters: 21.6, rule: 22.1, ai: 22.4, tagline: 23.0, cmdTxt: 23.8, cmdSlam: 24.3,
  cta: 25.8, abo: 27.0, share: 28.4, fade: 31.2,
};
const chords = [];
for (let a = 12.0, i = 0; a < T.logo - .01; a += 2, i++) chords.push([['Dm', 'Bb', 'F', 'C'][i % 4], a, Math.min(a + 2, T.logo)]);
const MUSIC = {
  drone: [0, T.freeze], suspense: [[0, T.freeze]],
  chords, bass: [[T.click, T.logo]], arp: [[T.grid, T.logo]],
  kick: [[T.click, T.logo, .4], [T.cmdTxt, 31.0, .35]], hat: [[T.click, T.logo, .12], [T.cmdTxt, 31.0, .12]], clap: [[T.grid, T.logo, .3]],
  final: T.logo,
};

// ------------------------------------------------------------ dessin « à la main »
// Poutre décomposée en segments, comme on la tracerait trait par trait.
const BX0 = 150, BX1 = 930, BY0 = 820, BY1 = 1010;
const SEGS = [
  [[BX0, BY0], [BX1, BY0], 'b'], [[BX1, BY0], [BX1, BY1], 'b'], [[BX1, BY1], [BX0, BY1], 'b'], [[BX0, BY1], [BX0, BY0], 'b'],
  [[BX0 + 24, BY0 + 22], [BX1 - 24, BY0 + 22], 'c'], [[BX0 + 24, BY1 - 22], [BX1 - 24, BY1 - 22], 'c'],
];
for (let x = BX0 + 50; x < BX1 - 30; x += 52) SEGS.push([[x, BY0 + 12], [x, BY1 - 12], 's']);
const SEG_DT = .26;
const phaseOf = t => { let p = -1; T.phases.forEach((a, i) => { if (t >= a) p = i; }); return p; };
function manualProgress(t) {
  // nombre de segments tracés dans la phase courante (repart de zéro à chaque nouvelle poutre)
  const p = phaseOf(t);
  if (p < 0 || t >= T.freeze + 1.3) return { p, n: 0, k: 0 };
  let n = (Math.min(t, T.freeze) - T.phases[p]) / SEG_DT + (p === 0 ? 0 : 3);
  if (t > T.rewind[0]) n *= 1 - eio3(prog(t, T.rewind[0], T.rewind[1]));
  return { p, n: Math.min(n, SEGS.length), k: n % 1 };
}
T.phases.forEach((a, p) => {
  for (let i = p === 0 ? 0 : 3; ; i++) {
    const tc = a + (i - (p === 0 ? 0 : 3) + 1) * SEG_DT;
    if (tc >= (T.phases[p + 1] || T.freeze) || i >= SEGS.length) break;
    cue(tc, 'key', 1);
  }
  if (p > 0) cue(a, 'whoosh', .5);
});
const CLOCKS = ['23:47', '01:15', '02:38', '04:06'];

// ------------------------------------------------------------ repères sonores
[.3, 1.0, 2.1, 3.5, 5.3, 7.1].forEach(t0 => cue(t0, 'pop', .8));
cue(T.freeze, 'scratch', 1.2); cue(T.etsi, 'pop', 1);
cue(T.cmd, 'pop', 1); cue(T.rewind[1] - .65, 'suck', 1);
cue(T.panel, 'whoosh', .5);
T.fields.forEach(f => { for (let i = 0; i < 6; i++) cue(f + i * .035, 'key', .6); });
cue(T.click, 'blip', 1); cue(T.click + .05, 'slam', .6); shakeAt(T.click, 6);
cue(T.draw, 'draw', .6);
for (let i = 0; i < 16; i++) cue(T.draw + .4 + i * .03, 'tick', .3);
for (let i = 0; i < 12; i++) cue(T.grid + i * .2, 'pop', .6);
cue(T.done, 'chime', .6); cue(T.done, 'pop', 1); cue(T.lit, 'pop', 1);
cue(T.logo - .6, 'suck', .8); cue(T.logo, 'boom', 1.4); shakeAt(T.logo, 20);
cue(T.logo + .05, 'draw', .9);
cue(T.clang, 'clang', 1.1); shakeAt(T.clang, 8);
for (let i = 0; i < 8; i++) cue(T.letters + i * .06, 'tick', .5);
cue(T.rule, 'tick', .8); cue(T.ai, 'glitch', .7); cue(T.ai, 'slam', .6);
cue(T.tagline, 'chime', .7);
cue(T.cmdSlam, 'slam', 1); shakeAt(T.cmdSlam, 10);
cue(T.cta, 'whoosh', .6); cue(T.cta + .1, 'blip', .8);
cue(T.abo, 'pop', 1); cue(T.share, 'pop', 1);

// ------------------------------------------------------------ autocollants (légendes TikTok)
function sticker(t, lines, y, t0, o = {}) {
  const k = prog(t, t0, t0 + .28);
  const out = o.out != null ? prog(t, o.out, o.out + .2) : 0;
  if (k <= 0 || out >= 1) return;
  const size = o.size || 50, lh = size * 1.42;
  const f = F('700 # Manrope', size, 0);
  const sc = eoBack(k) * (1 - out * .3);
  ctx.save();
  ctx.globalAlpha = 1 - out;
  ctx.translate(CX, y); ctx.rotate((o.rot || 0) * Math.PI / 180); ctx.scale(sc, sc);
  setFont(f); ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  lines.forEach((s, i) => {
    const w = ctx.measureText(s).width, yy = (i - (lines.length - 1) / 2) * lh;
    ctx.fillStyle = o.bg || COL.chaux;
    ctx.beginPath(); ctx.roundRect(-w / 2 - 26, yy - lh / 2 + 3, w + 52, lh - 6, 14); ctx.fill();
    ctx.fillStyle = o.fg || COL.nuit; ctx.fillText(s, 0, yy + 2);
  });
  ctx.restore();
}

// ------------------------------------------------------------ écran de dessin
function chrome(t, a) {
  const p = phaseOf(t);
  ctx.save(); ctx.globalAlpha = a;
  // bandeau d'outils
  ctx.fillStyle = COL.acier; ctx.fillRect(0, 250, W, 84);
  setFont(F('400 # Mono', 20, 1)); ctx.textAlign = 'left'; ctx.fillStyle = COL.beton;
  ctx.fillText('Accueil   Insérer   Annoter   Vue', 40, 300);
  // horloge
  let clock = CLOCKS[Math.max(0, p)];
  if (t >= T.rewind[0]) {
    const k = eio3(prog(t, T.rewind[0], T.rewind[1]));
    const m0 = 4 * 60 + 6 + 24 * 60, m1 = 23 * 60 + 47, m = Math.round(lerp(m0, m1, k)) % (24 * 60);
    clock = String(Math.floor(m / 60)).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0');
  }
  const late = t < T.rewind[0] && p >= 1;
  setFont(F('500 # Mono', 30, 1)); ctx.textAlign = 'right';
  ctx.fillStyle = late ? (Math.floor(t * 3) % 2 ? COL.cuivreC : COL.chaux) : COL.chaux;
  ctx.fillText(clock, W - 40, 304);
  // compteur de poutres
  let n = t < T.freeze ? Math.max(1, p + (p >= 2 ? 0 : 1)) : 1;
  if (p === 3 && t < T.freeze) n = 3;
  if (t >= T.grid) n = Math.min(12, 1 + Math.floor((t - T.grid) / .2));
  const ok = n === 12;
  const chip = `POUTRE ${String(n).padStart(2, '0')}/12`;
  setFont(F('500 # Mono', 22, 3)); ctx.textAlign = 'left';
  const cw = ctx.measureText(chip).width;
  ctx.fillStyle = ok ? rgba(COL.signal, .2) : rgba(COL.cuivre, .18);
  ctx.beginPath(); ctx.roundRect(40, 360, cw + (ok ? 70 : 36), 48, 10); ctx.fill();
  ctx.fillStyle = ok ? COL.signal : COL.cuivreC; ctx.fillText(chip, 58, 392);
  if (ok) { ctx.strokeStyle = COL.signal; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(58 + cw + 12, 383); ctx.lineTo(58 + cw + 22, 393); ctx.lineTo(58 + cw + 40, 372); ctx.stroke(); }
  // ligne de commande
  ctx.fillStyle = rgba(COL.acier, .95); ctx.fillRect(0, 1400, W, 70);
  setFont(F('400 # Mono', 22, 0)); ctx.fillStyle = COL.beton;
  const cmd = t < T.freeze ? 'Commande : LIGNE   Spécifiez le point suivant :' : t < T.click ? 'Commande :' : 'Ferraillage dessiné.';
  ctx.fillText(cmd, 40, 1444);
  if (Math.floor(t * 3) % 2 === 0) { const w = ctx.measureText(cmd).width; ctx.fillStyle = COL.signal; ctx.fillRect(48 + w, 1425, 12, 24); }
  ctx.restore();
}
function dotGrid(a) {
  ctx.save(); ctx.fillStyle = rgba(COL.beton, .13 * a);
  for (let x = 30; x < W; x += 40) for (let y = 440; y < 1390; y += 40) ctx.fillRect(x, y, 2, 2);
  ctx.restore();
}
function segStyle(kind) {
  if (kind === 'c') { ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 5; }
  else if (kind === 's') { ctx.strokeStyle = rgba(COL.chaux, .85); ctx.lineWidth = 2.5; }
  else { ctx.strokeStyle = rgba(COL.beton, .8); ctx.lineWidth = 2; }
}
function manual(t, a) {
  const { n } = manualProgress(t);
  let cur = null;
  ctx.save(); ctx.globalAlpha = a; ctx.lineCap = 'round';
  for (let i = 0; i < Math.ceil(n); i++) {
    const [p0, p1, kind] = SEGS[i], u = Math.min(1, n - i);
    segStyle(kind);
    // le curseur rejoint le point de départ puis tire le trait
    const uu = clamp((u - .45) / .55);
    const pe = [lerp(p0[0], p1[0], uu), lerp(p0[1], p1[1], uu)];
    if (uu > 0) { ctx.beginPath(); ctx.moveTo(p0[0], p0[1]); ctx.lineTo(pe[0], pe[1]); ctx.stroke(); }
    if (i === Math.ceil(n) - 1) {
      const prev = i > 0 ? SEGS[i - 1][1] : [CX, 1200];
      cur = u < .45 ? [lerp(prev[0], p0[0], eio3(u / .45)), lerp(prev[1], p0[1], eio3(u / .45))] : pe;
    }
  }
  ctx.restore();
  return cur;
}
function crosshair(x, y, a) {
  ctx.save(); ctx.globalAlpha = a * .9; ctx.strokeStyle = COL.chaux; ctx.lineWidth = 1.2;
  ctx.beginPath(); ctx.moveTo(x - 90, y); ctx.lineTo(x + 90, y); ctx.moveTo(x, y - 90); ctx.lineTo(x, y + 90); ctx.stroke();
  ctx.strokeRect(x - 9, y - 9, 18, 18);
  ctx.restore();
}
// Poutre complète (dessin instantané), dans une boîte quelconque
function beam(t, t0, x0, y0, w, h, dur, a) {
  const k = prog(t, t0, t0 + dur);
  if (k <= 0) return;
  ctx.save(); ctx.globalAlpha = a;
  ctx.strokeStyle = rgba(COL.beton, .8); ctx.lineWidth = 2;
  ctx.setLineDash([2 * (w + h) * eo3(clamp(k * 2)), 9999]); ctx.strokeRect(x0, y0, w, h); ctx.setLineDash([]);
  const kb = eo3(clamp(k * 2 - .3));
  ctx.strokeStyle = COL.cuivre; ctx.lineWidth = Math.max(2, h * .035);
  [y0 + h * .12, y0 + h * .88].forEach(y => { ctx.beginPath(); ctx.moveTo(x0 + w * .03, y); ctx.lineTo(x0 + w * (.03 + .94 * kb), y); ctx.stroke(); });
  const ks = clamp(k * 1.6 - .6);
  ctx.strokeStyle = rgba(COL.chaux, .85); ctx.lineWidth = Math.max(1, h * .014);
  const ns = 15;
  for (let i = 0; i < Math.floor(ns * ks); i++) {
    const x = x0 + w * (.065 + .87 * i / (ns - 1));
    ctx.beginPath(); ctx.moveTo(x, y0 + h * .06); ctx.lineTo(x, y0 + h * .94); ctx.stroke();
  }
  ctx.restore();
  if (k < 1) glow(x0 + w * (.03 + .94 * kb), y0 + h * .5, h, COL.signal, .5);
}
function panel(t, a) {
  const k = win(t, T.panel, T.draw + .2, .3, .3);
  if (k <= 0) return;
  const y0 = 470;
  ctx.save(); ctx.globalAlpha = a * k;
  ctx.translate(CX, y0 + 230); ctx.scale(lerp(.9, 1, eoBack(prog(t, T.panel, T.panel + .3))), lerp(.9, 1, eoBack(prog(t, T.panel, T.panel + .3)))); ctx.translate(-CX, -(y0 + 230));
  ctx.fillStyle = rgba(COL.acier, .96); ctx.strokeStyle = rgba(COL.beton, .3); ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.roundRect(110, y0, 860, 460, 18); ctx.fill(); ctx.stroke();
  setFont(F('500 # Mono', 20, 4)); ctx.textAlign = 'left'; ctx.fillStyle = COL.beton;
  ctx.fillText('CIVREBAR AI  ·  POUTRE', 150, y0 + 50);
  [['Section', '30 × 60 cm'], ['Portée', '5,40 m'], ['Armatures', '3 HA20 / 2 HA14'], ['Cadres', 'HA8 — e = 15 cm']].forEach(([l, v], i) => {
    const y = y0 + 120 + i * 72, n = Math.floor(clamp((t - T.fields[i]) / .2) * v.length);
    setFont(F('400 # Mono', 24, 1)); ctx.fillStyle = COL.beton; ctx.fillText(l, 150, y);
    ctx.strokeStyle = rgba(COL.beton, .25); ctx.strokeRect(400, y - 34, 530, 50);
    setFont(F('500 # Mono', 26, 1)); ctx.fillStyle = COL.chaux; ctx.fillText(v.slice(0, n), 420, y);
  });
  const on = t >= T.click, press = decay(t, T.click, 8);
  ctx.fillStyle = on ? COL.cuivre : rgba(COL.cuivre, .25); ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.roundRect(620 + press * 4, y0 + 385 + press * 3, 310 - press * 8, 54 - press * 6, 10); ctx.fill(); ctx.stroke();
  setFont(F('500 # Mono', 22, 6)); ctx.textAlign = 'center'; ctx.fillStyle = on ? COL.nuit : COL.cuivreC;
  ctx.fillText('DESSINER', 775, y0 + 420);
  ctx.restore();
}
function sceneScreen(t) {
  if (t >= T.logo + .1) return;
  const out = prog(t, T.logo - .5, T.logo);
  const a = 1 - out;
  const z = 1 - .15 * eio3(out);
  const freeze = t >= T.freeze && t < T.panel;
  ctx.save();
  ctx.translate(CX, 960); ctx.scale(z, z); ctx.translate(-CX, -960);
  // fatigue : léger flottement de l'image pendant la nuit blanche
  if (t < T.freeze) ctx.translate(Math.sin(t * 1.3) * 3 * prog(t, 3, 9), Math.cos(t * .9) * 3 * prog(t, 3, 9));
  dotGrid(a);
  const cur = manual(t, a);
  if (cur && t < T.freeze) crosshair(cur[0], cur[1], a);
  panel(t, a);
  // dessin en une commande, puis les 12 poutres
  if (t >= T.draw) {
    const ka = 1 - prog(t, T.grid - .3, T.grid);
    beam(t, T.draw, BX0, BY0, BX1 - BX0, BY1 - BY0, .9, a * ka);
    for (let i = 0; i < 12; i++) {
      const c = i % 2, r = Math.floor(i / 2);
      beam(t, T.grid + i * .2, 90 + c * 470, 470 + r * 150, 430, 96, .35, a);
    }
  }
  chrome(t, a);
  ctx.restore();
  if (freeze) {
    ctx.save(); ctx.globalAlpha = .55 * (1 - prog(t, T.panel - .3, T.panel)); ctx.fillStyle = '#000'; ctx.fillRect(0, 0, W, H); ctx.restore();
  }
  // légendes
  const o1 = T.phases[1] - .2;
  sticker(t, ['POV :'], 520, .3, { size: 64, out: o1, rot: -3 });
  sticker(t, ['il est 23 h 47'], 620, 1.0, { out: o1 });
  sticker(t, ['et il te reste 12 poutres', 'à ferrailler pour demain.'], 1180, 2.1, { out: o1 });
  sticker(t, ['Cadre par cadre…'], 560, T.phases[1], { out: T.phases[2] - .15, rot: 2 });
  sticker(t, ['Cote par cote…'], 560, T.phases[2], { out: T.phases[3] - .15, rot: -2 });
  sticker(t, ['Café n° 4…'], 560, T.phases[3], { out: T.freeze - .1, rot: 3, bg: COL.cuivre, fg: COL.nuit });
  sticker(t, ['Et si…'], 860, T.etsi, { size: 96, out: T.panel - .3 });
  sticker(t, ['…une seule commande', 'suffisait ?'], 1040, T.cmd, { size: 60, out: T.panel - .3, bg: COL.signal });
  sticker(t, ['12 poutres. Barres, cadres,', 'cotes et repères.'], 1180, T.done, { size: 44, out: T.logo - .5 });
  sticker(t, ['Et toi… au lit.'], 1320, T.lit, { size: 56, out: T.logo - .5, bg: COL.cuivre, rot: -2 });
}
// ------------------------------------------------------------ logo & appel à l'action
function sceneBrand(t) {
  if (t < T.logo - .7) return;
  const up = eio3(prog(t, T.cta - .3, T.cta + .5));
  const cx = CX, cy = lerp(780, 470, up), S = lerp(1.5, .95, up);
  const TR0 = { ox: CX - 125 * 2.6, oy: 800 - 135 * 2.6, s: 2.6 };
  const k = eio3(prog(t, T.clang + .1, T.letters + .2));
  const TL = symInLockupV(cx, cy, S);
  const tr = t < T.cta - .3 ? { ox: lerp(TR0.ox, TL.ox, k), oy: lerp(TR0.oy, TL.oy, k), s: lerp(TR0.s, TL.s, k) } : TL;
  const [nx, ny] = symPt(tr, NODE.x, NODE.y);
  if (t < T.logo) {
    const q = ei3(prog(t, T.logo - .6, T.logo));
    glow(nx, ny, 30 + q * 150, COL.signal, q * .9);
    return;
  }
  const breathe = .5 + .5 * Math.sin((t - T.logo) * 2.6);
  glow(CX, cy, 800, COL.acier, .55);
  glow(nx, ny, 110 + 260 * decay(t, T.logo, 1.6) + 25 * breathe, COL.signal, .3 + .6 * decay(t, T.logo, 1.2));
  ring(t, T.logo, nx, ny, 1600, 1.3, COL.signal, 10);
  ring(t, T.logo + .12, nx, ny, 1000, 1.5, COL.cuivre, 4);
  sparks(t, T.logo, 140, nx, ny, 21, [COL.signal, COL.chaux, COL.cuivreC]);
  flare(nx, ny, decay(t, T.logo, 2.2), 1800);
  const pb = eio3(prog(t, T.logo + .1, T.logo + 1.1));
  const pr = eoX(prog(t, T.clang - .3, T.clang));
  drawSymbol(tr, { bar: pb, rel: pr, node: eoBack(prog(t, T.logo, T.logo + .35)), nodeGlow: 18 + 20 * breathe, glowBar: 4, glowRel: 20 * decay(t, T.clang, 1.2) + 3 });
  sparks(t, T.clang, 60, ...symPt(tr, 210, 220), 77, [COL.cuivreC, COL.cuivre, COL.chaux], .8);
  const letters = VG.map((_, i) => prog(t, T.letters + i * .06, T.letters + i * .06 + .5));
  const aiG = t >= T.ai && t < T.ai + .4 ? 1 - prog(t, T.ai, T.ai + .4) : 0;
  drawWordmarkV(t, cx, cy, S, { letters, rule: prog(t, T.rule, T.rule + .35), ai: t >= T.ai ? 1 : 0, aiGlitch: aiG });
  const a1 = 1 - prog(t, T.cta - .4, T.cta - .1);
  reveal(t, 'L’intelligence de l’armature.', CX, 1150, F('italic 400 # Serif', 58, .5), { t0: T.tagline, st: .03, dur: .6, mode: 'blur', color: COL.beton, alpha: a1 });
  reveal(t, 'Le ferraillage,', CX, 1280, F('600 # Sora', 66, -1), { t0: T.cmdTxt, st: .03, dur: .4, mode: 'rise', color: COL.chaux, alpha: a1 });
  slam(t, 'en une commande.', CX, 1380, F('700 # Sora', 84, -2), T.cmdSlam, COL.cuivre, 'center', a1);
  // appel à l'action
  reveal(t, 'Bientôt dans AutoCAD.', CX, 820, F('700 # Sora', 76, -2), { t0: T.cta, st: .025, dur: .4, mode: 'rise', color: COL.chaux });
  sticker(t, ['Abonne-toi pour ne pas', 'rater la sortie'], 1010, T.abo, { size: 48, bg: COL.signal, rot: -2 });
  sticker(t, ['Partage à un collègue qui', 'ferraille encore à la main'], 1250, T.share, { size: 48, bg: COL.cuivre, rot: 2 });
}

// ------------------------------------------------------------ rendu
function renderFrame(t) {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over'; ctx.filter = 'none';
  ctx.fillStyle = COL.nuit; ctx.fillRect(0, 0, W, H);
  const [sx, sy] = shake(t);
  ctx.save(); ctx.translate(sx, sy);
  if (t >= T.logo - .7) grid(.3 * prog(t, T.logo, T.logo + .8));
  sceneScreen(t); sceneBrand(t);
  ctx.restore();
  const fl = Math.max(.85 * decay(t, T.logo, 5), .4 * decay(t, T.freeze, 10), .3 * decay(t, T.click, 10));
  if (fl > .01) { ctx.fillStyle = `rgba(243,240,234,${fl})`; ctx.fillRect(0, 0, W, H); }
  vignette(.6);
  ctx.save();
  ctx.globalAlpha = .055; ctx.globalCompositeOperation = 'overlay';
  const gi = Math.floor(t * FPS);
  ctx.fillStyle = ctx.createPattern(GRAIN[gi % GRAIN.length], 'repeat');
  ctx.translate(-rnd(gi) * 256, -rnd(gi + 1) * 256);
  ctx.fillRect(0, 0, W + 256, H + 256);
  ctx.restore();
  const fade = Math.max(1 - prog(t, 0, .3), prog(t, T.fade, DUR - .2));
  if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
}

window.T = T;
window.MUSIC = MUSIC;
boot(renderFrame, DUR);
