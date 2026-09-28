// CivRebar AI — teaser vertical pour TikTok / WhatsApp (1080x1920, 30 i/s, 81 s).
// Même langage que le teaser paysage, avec des scènes en plus : le temps perdu,
// la démonstration en une commande, la feuille de route et la promesse de la marque.
// Les textes utiles restent dans la zone sûre TikTok (y ≈ 250 → 1450, x ≈ 70 → 960).
const DUR = 81;
const CX = W / 2;

// Temps clés
const T = {
  beats: [0.9, 2.4, 3.9],
  colIn: 5.4, stirrups: 7.0, milliers: 8.6, slams: [10.3, 10.95, 11.6], cut1: 12.5,
  rien: 13.0, tout: 15.5, calcule: 16.25, warp: 17.2,
  hours: 19.0, count: [19.2, 23.8], hl: [19.6, 20.7, 21.8],
  s4: 24.5, etsi: 24.8, devenait: 26.0, intel: 27.7, black: 30.5, reveal: 31.7,
  clang: 33.65, lockup: 35.5, letters: 36.05, rule: 36.6, ai: 37.0, tagline: 38.0, up: 40.6,
  demo: 41.5, fields: [42.0, 42.8, 43.6, 44.4], click: 45.3, draw: 45.7, cap2: 47.6, cmd: [49.6, 50.3], demoOut: 52.6,
  road: 53.2, steps: 55.0, roadOut: 61.0,
  prom: 61.7, promOut: 66.0,
  qc: 66.6, arrive: 67.6, sub: 68.8, ticker: 69.8, out6: 71.4,
  cut2: 72.0, rdv: 72.2, bientot: 74.2, final: 76.4, fade: 79.6,
};
TENSION.push([29.3, 30.5]);
// Plan musical (lu par sound.py)
const MUSIC = {
  drone: [0, 30.5], pedal: [12.5, 30.5], riser: [22.0, 30.5],
  chords: [['Dm', 31.6, 35.6], ['Bb', 35.6, 39.6], ['F', 39.6, 43.6], ['C', 43.6, 47.6], ['Dm', 47.6, 51.6],
    ['Bb', 51.6, 55.6], ['F', 55.6, 59.6], ['C', 59.6, 63.6], ['Dm', 63.6, 67.6], ['Bb', 67.6, 72.0]],
  bass: [[35.6, 61.4], [67.6, 72.0]], arp: [[39.6, 61.0], [67.6, 72.0]],
  kick: [[43.6, 47.6, .28], [47.6, 61.0, .4], [67.6, 71.9, .45]],
  suspense: [72.0, 76.4], suspenseHearts: [72.8, 74.3, 75.8], final: 76.4,
};

// ------------------------------------------------------------ repères sonores
T.beats.forEach(b => { cue(b, 'heart', 1); cue(b + .24, 'heart', .6); });
const TYPE_LINES = [
  { s: '> PROJET CONFIDENTIEL', t0: .5, cps: 22 },
  { s: '> ANALYSE DU PLAN EN COURS', t0: 1.8, cps: 24 },
  { s: '> CHARGEMENT', t0: 3.2, cps: 24 },
];
TYPE_LINES.forEach(L => { for (let i = 0; i < L.s.length; i++) if (L.s[i] !== ' ') cue(L.t0 + i / L.cps, 'key', .5 + .3 * rnd(i + L.t0)); });
cue(5.0, 'whoosh', .9);
cue(T.colIn, 'draw', .6);
const STIR = [];
{ let y = 560; while (y <= 1400) { STIR.push(y); y += (y < 780 || y > 1180) ? 36 : 72; } }
STIR.forEach((y, i) => cue(T.stirrups + i * (1.5 / STIR.length), 'tick', .45));
cue(T.milliers, 'swell', .6);
T.slams.forEach((s, i) => { cue(s, 'slam', i === 2 ? 1.1 : .9); shakeAt(s, i === 2 ? 14 : 9); });
cue(T.cut1, 'impact', .8); shakeAt(T.cut1, 8);
cue(T.rien, 'chime', .5);
cue(T.calcule, 'slam', 1.1); shakeAt(T.calcule, 12);
cue(T.warp, 'whoosh', 1.2);
cue(T.hours, 'impact', .5);
// compteur d'heures : un tic à chaque heure écoulée (accélère)
const COUNT_MAX = 170000;
const countAt = t => COUNT_MAX * ei3(prog(t, T.count[0], T.count[1]));
for (let h = 1; h * 3600 < COUNT_MAX; h++) cue(T.count[0] + Math.cbrt(h * 3600 / COUNT_MAX) * (T.count[1] - T.count[0]), 'tick', .5);
T.hl.forEach(s => { cue(s, 'slam', .55); shakeAt(s, 5); });
cue(T.count[1], 'glitch', .6); cue(T.count[1], 'impact', .5); shakeAt(T.count[1], 8);
cue(T.s4 - .3, 'whoosh', .6);
cue(T.intel, 'glitch', 1.1); cue(T.intel, 'slam', .9); shakeAt(T.intel, 16);
const GL = [28.6, 29.4, 29.85, 30.1, 30.3];
GL.forEach((g, i) => cue(g, 'glitch', .5 + i * .12));
cue(T.reveal - .65, 'suck', 1.2);
cue(T.reveal, 'boom', 1.4); shakeAt(T.reveal, 26);
cue(T.reveal + .05, 'draw', 1);
cue(T.clang, 'clang', 1.2); shakeAt(T.clang, 10);
cue(T.lockup - .15, 'whoosh', .7);
for (let i = 0; i < 8; i++) cue(T.letters + i * .06, 'tick', .55);
cue(T.rule, 'tick', .8);
cue(T.ai, 'glitch', .8); cue(T.ai + .02, 'slam', .7); shakeAt(T.ai, 6);
cue(T.tagline, 'chime', .8);
cue(T.up - .1, 'whoosh', .6);
// démonstration
const FIELDS = [
  ['Section', '30 × 60 cm'], ['Portée', '5,40 m'], ['Armatures', '3 HA20 / 2 HA14'], ['Cadres', 'HA8 — e = 15 cm'],
];
FIELDS.forEach(([, v], j) => { for (let i = 0; i < v.length; i++) if (v[i] !== ' ') cue(T.fields[j] + .15 + i / 26, 'key', .6); });
cue(T.click, 'blip', 1); cue(T.click + .1, 'slam', .5);
cue(T.draw, 'draw', .8);
const BSTIR = [];
{ let x = 130; while (x <= 950) { BSTIR.push(x); x += (x < 330 || x > 750) ? 24 : 48; } }
BSTIR.forEach((x, i) => cue(T.draw + .6 + i * (.9 / BSTIR.length), 'tick', .3));
cue(T.cap2, 'chime', .4);
cue(T.cmd[1], 'slam', 1); shakeAt(T.cmd[1], 10);
cue(T.demoOut, 'whoosh', .6);
// feuille de route
cue(T.road, 'swell', .4);
cue(T.road + 1.2, 'slam', .8); shakeAt(T.road + 1.2, 7);
for (let i = 0; i < 5; i++) cue(T.steps + i * .9, 'blip', .7);
cue(T.steps + 4 * .9, 'chime', .5);
cue(T.roadOut, 'whoosh', .5);
cue(T.prom, 'chime', .55);
cue(T.promOut, 'whoosh', .5);
// annonce
cue(T.qc, 'swell', .5);
cue(T.arrive, 'boom', .9); shakeAt(T.arrive, 12);
cue(T.sub, 'chime', .45);
for (let i = 0; i < 5; i++) cue(T.ticker + i * .32, 'blip', .7);
cue(T.out6, 'whoosh', .6);
cue(T.cut2, 'impact', .9); shakeAt(T.cut2, 8);
cue(T.rdv + .9, 'shine', .8);
cue(T.bientot, 'glitch', .45); cue(T.bientot, 'blip', .7);
cue(T.final - .7, 'suck', .8);
cue(T.final, 'boom', 1.5); shakeAt(T.final, 18);
cue(T.final + .9, 'chime', .9);

// Tracés Signal (question)
const TRACES = [];
for (let i = 0; i < 44; i++) {
  const a = (i / 44) * Math.PI * 2 + rnd(i) * .3;
  let x = CX + Math.cos(a) * 300, y = 900 + Math.sin(a) * 430;
  x = Math.round(x / 48) * 48; y = Math.round(y / 48) * 48;
  const pts = [[x, y]];
  const steps = 7 + Math.floor(rnd(i + 50) * 10);
  for (let s = 0; s < steps; s++) {
    const horiz = rnd(i * 31 + s) > .55;
    const len = 48 * (1 + Math.floor(rnd(i * 17 + s) * 4));
    if (horiz) x += Math.sign(Math.cos(a) || 1) * len; else y += Math.sign(Math.sin(a) || 1) * len;
    pts.push([x, y]);
  }
  let L = 0; for (let k = 1; k < pts.length; k++) L += Math.hypot(pts[k][0] - pts[k - 1][0], pts[k][1] - pts[k - 1][1]);
  TRACES.push({ pts, L, delay: rnd(i + 7) * .9 });
}
const veil = (y, r, a) => {
  const g = ctx.createRadialGradient(CX, y, 0, CX, y, r);
  g.addColorStop(0, rgba(COL.nuit, a)); g.addColorStop(1, rgba(COL.nuit, 0));
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
};

// ------------------------------------------------------------ 1 : veille (0 → 5.4)
function scene1(t) {
  const cy = 760;
  const a = win(t, .3, 5.6, .5, .5);
  if (a <= 0) return;
  let pulse = 0;
  T.beats.forEach(b => { pulse += decay(t, b, 9) + .6 * decay(t, b + .24, 11); });
  T.beats.forEach(b => ring(t, b, CX, cy, 420, 1.4, COL.signal, 3));
  // le point s'étire en barre verticale : la première armature du poteau
  const st = eio3(prog(t, 5.0, 5.45));
  ctx.save(); ctx.globalAlpha = a;
  glow(CX, cy, 70 + pulse * 110, COL.signal, .35 + pulse * .4);
  ctx.fillStyle = COL.signal; ctx.shadowColor = COL.signal;
  if (st <= 0) {
    ctx.shadowBlur = 20 + pulse * 30;
    ctx.beginPath(); ctx.arc(CX, cy, 7 + pulse * 5, 0, Math.PI * 2); ctx.fill();
  } else {
    const half = st * H * .6;
    ctx.shadowBlur = 25;
    ctx.fillRect(CX - 1.5 - 3 * (1 - st), cy - half, 3 + 6 * (1 - st), half * 2);
  }
  ctx.restore();
  const al = 1 - prog(t, 4.8, 5.2);
  const f = F('300 # Sora', 64, 0);
  reveal(t, 'Chaque ouvrage', CX, 980, f, { t0: 2.7, st: .04, dur: .7, mode: 'blur', color: COL.chaux, alpha: al });
  reveal(t, 'cache une ossature.', CX, 1062, f, { t0: 3.2, st: .035, dur: .7, mode: 'blur', color: COL.chaux, alpha: al });
  const ta = 1 - prog(t, 4.9, 5.3);
  TYPE_LINES.forEach((L, j) => {
    const n = Math.floor(clamp((t - L.t0) * L.cps, 0, L.s.length));
    if (n <= 0) return;
    let s = L.s.slice(0, n);
    if (j === 2 && n === L.s.length) {
      const pct = Math.floor(100 * eio3(prog(t, 3.8, 4.7)));
      const bars = Math.floor(pct / 10);
      s += '  [' + '■'.repeat(bars) + '·'.repeat(10 - bars) + '] ' + String(pct).padStart(3, ' ') + '%';
    }
    ctx.save(); ctx.globalAlpha = ta * .85;
    setFont(F('400 # Mono', 22, 1)); ctx.textAlign = 'left';
    ctx.fillStyle = j === 0 ? COL.cuivreC : COL.beton;
    ctx.fillText(s, 90, 1290 + j * 40);
    const last = TYPE_LINES.reduce((m, q, idx) => (t >= q.t0 ? idx : m), 0);
    if (j === last && Math.floor(t * 3) % 2 === 0) { const w = ctx.measureText(s).width; ctx.fillStyle = COL.signal; ctx.fillRect(90 + w + 6, 1272 + j * 40, 12, 23); }
    ctx.restore();
  });
  ctx.save(); ctx.globalAlpha = ta * .5 * prog(t, .6, 1.2);
  setFont(F('400 # Mono', 16, 3)); ctx.fillStyle = COL.beton; ctx.textAlign = 'center';
  ctx.fillText('RÉF. 00-CR  ·  NE PAS DIFFUSER', CX, 330);
  ctx.restore();
}

// ------------------------------------------------------------ 2 : le poteau (5.4 → 12.5)
function scene2(t) {
  const a = win(t, T.colIn, T.cut1, .4, .25);
  if (a <= 0) return;
  const zoom = lerp(1, 1.08, eio3(prog(t, T.colIn, T.cut1)));
  const dim = lerp(1, .3, eo3(prog(t, T.slams[0] - .2, T.slams[0] + .3)));
  ctx.save();
  ctx.globalAlpha = a * dim;
  ctx.translate(CX, 980); ctx.scale(zoom, zoom); ctx.translate(-CX, -980 + 20 * prog(t, 5.4, 12.5));
  const X0 = 390, X1 = 690, Y0 = 520, Y1 = 1420;
  // béton : fût + semelle
  const pc = eo3(prog(t, 5.5, 6.6));
  ctx.strokeStyle = rgba(COL.beton, .75); ctx.lineWidth = 2;
  ctx.setLineDash([2 * (X1 - X0 + Y1 - Y0) * pc, 6000]);
  ctx.strokeRect(X0, Y0, X1 - X0, Y1 - Y0); ctx.setLineDash([]);
  const pp = eo3(prog(t, 6.0, 6.8));
  const sx0 = CX - 290 * pp, sx1 = CX + 290 * pp;
  if (pp > 0) {
    ctx.strokeRect(sx0, Y1, sx1 - sx0, 110);
    ctx.save(); ctx.beginPath(); ctx.rect(sx0, Y1, sx1 - sx0, 110); ctx.clip();
    ctx.strokeStyle = rgba(COL.beton, .3); ctx.lineWidth = 1;
    for (let k = -120; k < 700; k += 16) { ctx.beginPath(); ctx.moveTo(sx0 + k, Y1 + 120); ctx.lineTo(sx0 + k + 120, Y1); ctx.stroke(); }
    ctx.restore();
  }
  // barres longitudinales (cuivre), ancrées dans la semelle
  [{ x: 425, t0: 5.9, hook: -1 }, { x: 655, t0: 6.2, hook: 1 }].forEach(b => {
    const k = eo3(prog(t, b.t0, b.t0 + 1.1));
    if (k <= 0) return;
    const pts = [[b.x, 500], [b.x, 1490], [b.x + b.hook * 90, 1490]];
    ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 6; ctx.lineJoin = 'round';
    ctx.shadowColor = rgba(COL.cuivre, .6); ctx.shadowBlur = 12;
    const tip = drawPolyPartial(pts, 990 + 90, k);
    ctx.shadowBlur = 0;
    if (k < 1) glow(tip[0], tip[1], 40, COL.cuivreC, .9);
  });
  // cadres
  STIR.forEach((y, i) => {
    const t0 = T.stirrups + i * (1.5 / STIR.length);
    const k = eoX(prog(t, t0, t0 + .18));
    if (k <= 0) return;
    ctx.strokeStyle = rgba(COL.chaux, .85); ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(410, y); ctx.lineTo(410 + 260 * k, y); ctx.stroke();
    const fl = decay(t, t0, 12);
    if (fl > .02) glow(CX, y, 50, COL.signal, fl * .7);
  });
  // cotes & repères
  const ca = eo3(prog(t, 8.1, 8.8));
  if (ca > 0) {
    ctx.globalAlpha = a * dim * ca;
    setFont(F('500 # Mono', 20, 1)); ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 1.2;
    ctx.beginPath(); ctx.moveTo(800, Y0); ctx.lineTo(800, Y1); ctx.stroke();
    [Y0, Y1].forEach(y => { ctx.beginPath(); ctx.moveTo(793, y + 7); ctx.lineTo(807, y - 7); ctx.moveTo(785, y); ctx.lineTo(815, y); ctx.stroke(); });
    ctx.save(); ctx.translate(800, (Y0 + Y1) / 2); ctx.rotate(-Math.PI / 2);
    ctx.fillStyle = COL.nuit; ctx.fillRect(-80, -16, 160, 30);
    ctx.fillStyle = COL.chaux; ctx.textAlign = 'center'; ctx.fillText('H = 3,00 m', 0, 6);
    ctx.restore();
    ctx.textAlign = 'right';
    const lead = (x0, y0, x1, y1, s, c) => { ctx.strokeStyle = rgba(COL.beton, .7); ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.lineTo(x1 - 24, y1); ctx.stroke(); ctx.fillStyle = c; ctx.fillText(s, x1 - 32, y1 + 7); ctx.beginPath(); ctx.arc(x0, y0, 3.5, 0, 7); ctx.fill(); };
    lead(425, 700, 330, 650, '4 HA16', COL.cuivreC);
    lead(430, 1000, 330, 1060, 'Cadres HA8', COL.chaux);
    ctx.fillStyle = COL.beton; ctx.fillText('e = 15 cm', 298, 1097);
    setFont(F('500 # Mono', 18, 3)); ctx.fillStyle = COL.signal; ctx.textAlign = 'left';
    ctx.fillText('POTEAU P1 — 30 × 30', X0, Y0 - 34);
  }
  ctx.restore();
  reveal(t, 'Des milliers', CX, 300, F('600 # Sora', 84, -1), {
    t0: T.milliers, st: .03, dur: .55, mode: 'rise', color: COL.chaux, alpha: a * (1 - prog(t, 12.0, 12.4)),
  });
  reveal(t, 'de barres.', CX, 400, F('600 # Sora', 84, -1), {
    t0: T.milliers + .3, st: .03, dur: .55, mode: 'rise', color: COL.chaux, alpha: a * (1 - prog(t, 12.0, 12.4)),
  });
  ['Choisies.', 'Pliées.', 'Placées.'].forEach((w, i) => {
    slam(t, w, CX, 880 + i * 150, F('700 # Sora', 132, -2), T.slams[i], i === 2 ? COL.cuivre : COL.chaux, 'center', a * (1 - prog(t, 12.1, 12.45)));
  });
}

// ------------------------------------------------------------ 3 : le calcul (12.5 → 19)
const DATA = ['HA12', 'HA16', 'HA20', 'HA8 e=15', 'As = 4,52 cm²', 'c = 3 cm', 'L = 5,40 m', 'ELU', 'ELS', 'M = 124 kN·m', 'V = 86 kN', 'fc28 = 25 MPa', 'fe 500', '×24', 'ls = 50Ø', 'e = 20 cm', '30 × 60', 'Ø10', 'HA25', 'σ ≤ 0,6 fc28'];
function scene3(t) {
  const a = win(t, T.cut1, T.hours, .15, .35);
  if (a <= 0) return;
  const ph = (t - T.cut1) * .085 + .75 * Math.pow(Math.max(0, t - T.warp), 2);
  const fast = clamp((t - T.warp) * 1.2);
  for (let i = 0; i < 130; i++) {
    const ang = rnd(i * 1.7) * Math.PI * 2, z0 = rnd(i * 2.3 + 9);
    const d = (z0 + ph) % 1;
    const dist = 90 + Math.pow(d, 2.2) * 1250;
    const sc = .4 + d * d * 2.6;
    const px = dd => CX + Math.cos(ang) * dd * .72, py = dd => 960 + Math.sin(ang) * dd * 1.25;
    const al = a * clamp(d * 5) * (1 - clamp((d - .85) * 6)) * .55;
    if (al <= .01) continue;
    const col = i % 7 === 0 ? COL.cuivreC : i % 11 === 0 ? COL.signal : COL.beton;
    if (fast > 0) {
      const d2 = Math.max(0, d - .06 * fast), dist2 = 90 + Math.pow(d2, 2.2) * 1250;
      ctx.strokeStyle = rgba(col, al * fast); ctx.lineWidth = 1 + sc;
      ctx.beginPath(); ctx.moveTo(px(dist), py(dist)); ctx.lineTo(px(dist2), py(dist2)); ctx.stroke();
    }
    ctx.globalAlpha = al * (1 - fast * .6);
    setFont(F('500 # Mono', Math.round(17 * sc), 1)); ctx.textAlign = 'center'; ctx.fillStyle = col;
    ctx.fillText(DATA[i % DATA.length], px(dist), py(dist));
    ctx.globalAlpha = 1;
  }
  veil(960, 560, .92 * a);
  const fr = F('italic 400 # Serif', 136, 0), ra = a * (1 - prog(t, 15.0, 15.4));
  reveal(t, 'Rien n’y est', CX, 920, fr, { t0: T.rien, st: .04, dur: .8, mode: 'blur', color: COL.chaux, alpha: ra });
  reveal(t, 'décoratif.', CX, 1050, fr, { t0: T.rien + .45, st: .04, dur: .8, mode: 'blur', color: COL.chaux, alpha: ra });
  const out = prog(t, 17.9, 18.6), f = F('600 # Sora', 124, -2);
  ctx.save();
  ctx.translate(CX, 960); ctx.scale(1 + out * .6, 1 + out * .6); ctx.translate(-CX, -960);
  if (out > 0) ctx.filter = `blur(${(out * 18).toFixed(1)}px)`;
  reveal(t, 'Tout y est', CX, 930, f, { t0: T.tout, st: .035, dur: .5, mode: 'rise', color: COL.chaux, alpha: a * (1 - out) });
  slam(t, 'calculé.', CX, 1070, F('700 # Sora', 140, -3), T.calcule, COL.cuivre, 'center', a * (1 - out));
  ctx.restore();
}

// ------------------------------------------------------------ 3b : le temps (19 → 24.5)
function sceneHours(t) {
  const a = win(t, T.hours, T.s4, .25, .35);
  if (a <= 0) return;
  const s = Math.floor(countAt(t));
  const hh = String(Math.floor(s / 3600)).padStart(2, '0'), mm = String(Math.floor(s / 60) % 60).padStart(2, '0'), ss = String(s % 60).padStart(2, '0');
  const frozen = t >= T.count[1];
  const g = frozen ? 1 - prog(t, T.count[1], T.count[1] + .35) : 0;
  const hot = frozen ? (Math.floor(t * 8) % 2 ? COL.cuivre : COL.chaux) : COL.chaux;
  ctx.save(); ctx.globalAlpha = a;
  setFont(F('400 # Mono', 22, 6)); ctx.textAlign = 'center'; ctx.fillStyle = COL.beton;
  ctx.fillText('TEMPS PASSÉ SUR UN PLAN', CX, 620);
  ctx.restore();
  glow(CX, 740, 420, frozen ? COL.cuivre : COL.signal, .12 * a);
  glitchText(t, `${hh}:${mm}:${ss}`, CX, 790, F('500 # Mono', 150, 0), hot, g * 1.2, 5, a);
  // barre de progression sous le compteur
  ctx.save(); ctx.globalAlpha = a;
  ctx.fillStyle = rgba(COL.beton, .2); ctx.fillRect(160, 850, 760, 4);
  ctx.fillStyle = frozen ? COL.cuivre : COL.signal; ctx.fillRect(160, 850, 760 * (countAt(t) / COUNT_MAX), 4);
  ctx.restore();
  const lines = ['Des heures de dessin.', 'De vérification.', 'De reprises.'];
  lines.forEach((s2, i) => slam(t, s2, CX, 1040 + i * 110, F('600 # Sora', 72, -1), T.hl[i], i === 2 ? COL.cuivreC : COL.chaux, 'center', a));
}

// ------------------------------------------------------------ 4 : la question (24.5 → 30.5)
function scene4(t) {
  if (t < T.s4 || t >= T.black) return;
  const a = prog(t, T.s4, T.s4 + .3);
  if (t > T.intel) {
    ctx.save(); ctx.lineWidth = 2; ctx.lineCap = 'square';
    TRACES.forEach((tr, i) => {
      const k = eo3(prog(t, T.intel + tr.delay, T.intel + tr.delay + 1.3));
      if (k <= 0) return;
      ctx.strokeStyle = rgba(COL.signal, .45);
      ctx.shadowColor = COL.signal; ctx.shadowBlur = 8;
      const tip = drawPolyPartial(tr.pts, tr.L, k);
      ctx.shadowBlur = 0;
      ctx.fillStyle = COL.signal; ctx.beginPath(); ctx.arc(tip[0], tip[1], k < 1 ? 4 : 3, 0, 7); ctx.fill();
      const pk = ((t - T.intel) * .7 + tr.delay) % 1;
      if (k >= 1 && i % 3 === 0) { const q = drawPolyPartialPoint(tr.pts, tr.L, pk); glow(q[0], q[1], 26, COL.signal, .8); }
    });
    ctx.restore();
    veil(930, 620, .95);
  }
  const outQ = prog(t, T.intel - .35, T.intel - .05);
  const fq = F('300 # Sora', 104, -1);
  ctx.save();
  if (outQ > 0) ctx.filter = `blur(${(outQ * 14).toFixed(1)}px)`;
  reveal(t, 'Et si', CX, 800, fq, { t0: T.etsi, st: .05, dur: .6, mode: 'rise', color: COL.chaux, alpha: a * (1 - outQ) });
  reveal(t, 'l’armature', CX, 920, fq, { t0: T.etsi + .35, st: .04, dur: .6, mode: 'rise', color: COL.chaux, alpha: a * (1 - outQ) });
  reveal(t, 'devenait…', CX, 1040, fq, { t0: T.devenait, st: .05, dur: .6, mode: 'rise', color: COL.chaux, alpha: a * (1 - outQ) });
  ctx.restore();
  if (t >= T.intel) {
    let g = t < T.intel + .25 ? .9 * (1 - prog(t, T.intel, T.intel + .25)) : 0;
    GL.forEach(b => { if (t >= b && t < b + .1) g = Math.max(g, .45); });
    g = Math.max(g, Math.pow(prog(t, 29.8, 30.5), 2) * .9);
    const sc = 1 + .05 * eo3(prog(t, T.intel, T.black));
    glow(CX, 930, 620, COL.signal, .10 + .05 * Math.sin(t * 6));
    ctx.save(); ctx.translate(CX, 930); ctx.scale(sc, sc); ctx.translate(-CX, -930);
    const f = F('700 # Sora', 140, -4), al = clamp((t - T.intel) * 10);
    glitchText(t, 'intelligente\u202f?', CX, 980, f, COL.signal, g, 3, al);
    ctx.restore();
  }
}

// ------------------------------------------------------------ 5 : révélation du logo (30.5 → 41)
const LOCK = { cx: CX, cy: 860, S: 1.66 };
const TR_INTRO = { ox: CX - 125 * 2.8, oy: 900 - 135 * 2.8, s: 2.8 };
function lockState(t) {
  const up = eio3(prog(t, T.up, T.up + .9));
  return { cx: CX, cy: lerp(LOCK.cy, 360, up), S: lerp(LOCK.S, .6, up) };
}
function scene5(t) {
  if (t < T.black + .5 || t >= T.out6 + .6) return;
  if (t < T.reveal) {
    const k = prog(t, T.reveal - .65, T.reveal);
    const [nx, ny] = symPt(TR_INTRO, NODE.x, NODE.y);
    glow(nx, ny, 30 + ei3(k) * 160, COL.signal, ei3(k) * .9);
    ctx.save(); ctx.fillStyle = rgba(COL.signal, ei3(k));
    ctx.beginPath(); ctx.arc(nx, ny, 2 + ei3(k) * 12, 0, 7); ctx.fill(); ctx.restore();
    return;
  }
  const A = 1 - prog(t, T.out6, T.out6 + .5);
  const L = lockState(t);
  const k = eio3(prog(t, T.lockup, T.lockup + 1.0));
  const TL = symInLockupV(L.cx, L.cy, L.S);
  const tr = { ox: lerp(TR_INTRO.ox, TL.ox, k), oy: lerp(TR_INTRO.oy, TL.oy, k), s: lerp(TR_INTRO.s, TL.s, k) };
  const [nx, ny] = symPt(tr, NODE.x, NODE.y);
  glow(CX, L.cy, 800, COL.acier, .55 * A);
  const breathe = .5 + .5 * Math.sin((t - T.reveal) * 2.6);
  glow(nx, ny, 120 + 260 * decay(t, T.reveal, 1.6) + 30 * breathe, COL.signal, (.3 + .6 * decay(t, T.reveal, 1.2)) * A);
  ring(t, T.reveal, nx, ny, 1600, 1.3, COL.signal, 10);
  ring(t, T.reveal + .12, nx, ny, 1100, 1.5, COL.chaux, 4);
  ring(t, T.reveal + .3, nx, ny, 800, 1.4, COL.cuivre, 3);
  sparks(t, T.reveal, 140, nx, ny, 11, [COL.signal, COL.chaux, COL.cuivreC, COL.signal]);
  flare(nx, ny, decay(t, T.reveal, 2.2), 1800);
  const pb = eio3(prog(t, T.reveal + .1, T.reveal + 1.7));
  const pr = eoX(prog(t, T.clang - .35, T.clang));
  drawSymbol(tr, {
    alpha: A, bar: pb, rel: pr, node: eoBack(prog(t, T.reveal, T.reveal + .35)),
    nodeGlow: 18 + 20 * breathe, glowBar: 14 * decay(t, T.reveal + 1.7, 1.5) + 4, glowRel: 20 * decay(t, T.clang, 1.2) + 3,
  });
  if (pb > 0 && pb < 1) {
    const p = EL_BAR.getPointAtLength(LEN_BAR * pb), [px, py] = symPt(tr, p.x, p.y);
    glow(px, py, 90, COL.chaux, .9); glow(px, py, 30, '#ffffff', 1);
  }
  if (pr > 0 && pr < 1) {
    const p = EL_REL.getPointAtLength(LEN_REL * pr), [px, py] = symPt(tr, p.x, p.y);
    glow(px, py, 90, COL.cuivreC, 1);
  }
  const [ex, ey] = symPt(tr, 210, 220);
  sparks(t, T.clang, 70, ex, ey, 77, [COL.cuivreC, COL.cuivre, COL.chaux], .8);
  ring(t, T.clang, ex, ey, 260, .7, COL.cuivre, 5);
  const letters = VG.map((_, i) => prog(t, T.letters + i * .06, T.letters + i * .06 + .55));
  const aiG = t >= T.ai && t < T.ai + .45 ? 1 - prog(t, T.ai, T.ai + .45) : 0;
  drawWordmarkV(t, L.cx, L.cy, L.S, { alpha: A, letters, rule: prog(t, T.rule, T.rule + .35), ai: t >= T.ai ? 1 : 0, aiGlitch: aiG });
  reveal(t, 'L’intelligence de l’armature.', CX, 1300, F('italic 400 # Serif', 62, .5), {
    t0: T.tagline, st: .03, dur: .7, mode: 'blur', color: COL.beton, alpha: 1 - prog(t, T.up - .3, T.up + .1),
  });
}

// ------------------------------------------------------------ 6 : démonstration (41.5 → 53)
function field(t, label, value, y, t0, a) {
  const k = prog(t, t0, t0 + .3);
  if (k <= 0) return;
  ctx.save(); ctx.globalAlpha = a * k;
  setFont(F('400 # Mono', 26, 1)); ctx.textAlign = 'left';
  ctx.fillStyle = COL.beton; ctx.fillText(label, 150, y);
  ctx.strokeStyle = rgba(COL.beton, .25); ctx.lineWidth = 1.5; ctx.strokeRect(430, y - 38, 500, 56);
  const n = Math.floor(clamp((t - t0 - .15) * 26, 0, value.length));
  setFont(F('500 # Mono', 28, 1));
  ctx.fillStyle = COL.chaux; ctx.fillText(value.slice(0, n), 452, y);
  if (n < value.length && Math.floor(t * 4) % 2 === 0) { const w = ctx.measureText(value.slice(0, n)).width; ctx.fillStyle = COL.signal; ctx.fillRect(452 + w + 4, y - 24, 12, 30); }
  ctx.restore();
}
function drawBeam(t, t0, a) {
  // poutre dessinée « en une commande » : même dessin que plus haut, en accéléré
  const X0 = 90, X1 = 990, Y0 = 640, Y1 = 790;
  ctx.save(); ctx.globalAlpha = a;
  const pc = eo3(prog(t, t0, t0 + .5));
  ctx.strokeStyle = rgba(COL.beton, .75); ctx.lineWidth = 2;
  ctx.setLineDash([2 * (X1 - X0 + Y1 - Y0) * pc, 5000]); ctx.strokeRect(X0, Y0, X1 - X0, Y1 - Y0); ctx.setLineDash([]);
  const pp = eo3(prog(t, t0 + .2, t0 + .6));
  [[X0, X0 + 50], [X1 - 50, X1]].forEach(([a0, a1]) => {
    ctx.strokeRect(a0, Y1, a1 - a0, 90 * pp);
    ctx.save(); ctx.beginPath(); ctx.rect(a0, Y1, a1 - a0, 90 * pp); ctx.clip();
    ctx.strokeStyle = rgba(COL.beton, .3); ctx.lineWidth = 1;
    for (let k = -100; k < 100; k += 12) { ctx.beginPath(); ctx.moveTo(a0 + k, Y1 + 100); ctx.lineTo(a0 + k + 100, Y1); ctx.stroke(); }
    ctx.restore();
  });
  [{ y: 662, hook: 1, d: .1 }, { y: 768, hook: -1, d: .25 }].forEach(b => {
    const k = eo3(prog(t, t0 + b.d, t0 + b.d + .6));
    if (k <= 0) return;
    ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 5; ctx.lineJoin = 'round';
    ctx.shadowColor = rgba(COL.cuivre, .6); ctx.shadowBlur = 10;
    const tip = drawPolyPartial([[X0 + 26, b.y + b.hook * 40], [X0 + 26, b.y], [X1 - 26, b.y], [X1 - 26, b.y + b.hook * 40]], 80 + X1 - X0 - 52, k);
    ctx.shadowBlur = 0;
    if (k < 1) glow(tip[0], tip[1], 34, COL.cuivreC, .9);
  });
  BSTIR.forEach((x, i) => {
    const s0 = t0 + .6 + i * (.9 / BSTIR.length), k = eoX(prog(t, s0, s0 + .12));
    if (k <= 0) return;
    ctx.strokeStyle = rgba(COL.chaux, .85); ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(x, 652); ctx.lineTo(x, 652 + 126 * k); ctx.stroke();
    const fl = decay(t, s0, 12);
    if (fl > .02) glow(x, 715, 40, COL.signal, fl * .7);
  });
  const ca = eo3(prog(t, t0 + 1.4, t0 + 1.9));
  if (ca > 0) {
    ctx.globalAlpha = a * ca;
    setFont(F('500 # Mono', 20, 1)); ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 1.2;
    ctx.beginPath(); ctx.moveTo(X0 + 50, 930); ctx.lineTo(X1 - 50, 930); ctx.stroke();
    [X0 + 50, X1 - 50].forEach(x => { ctx.beginPath(); ctx.moveTo(x - 6, 936); ctx.lineTo(x + 6, 924); ctx.moveTo(x, 915); ctx.lineTo(x, 945); ctx.stroke(); });
    ctx.textAlign = 'center'; ctx.fillStyle = COL.nuit; ctx.fillRect(CX - 80, 916, 160, 28);
    ctx.fillStyle = COL.chaux; ctx.fillText('L = 5,40 m', CX, 937);
    ctx.textAlign = 'left';
    ctx.fillStyle = COL.cuivreC; ctx.fillText('2 HA14', 150, 620); ctx.fillText('3 HA20', 790, 830);
    ctx.fillStyle = COL.chaux; ctx.fillText('Cadres HA8 — e = 15 cm', 380, 620);
    setFont(F('500 # Mono', 18, 3)); ctx.fillStyle = COL.signal; ctx.fillText('POUTRE P1 — 30 × 60', X0, 580);
  }
  ctx.restore();
}
function sceneDemo(t) {
  const a = win(t, T.demo, T.demoOut + .4, .4, .4);
  if (a <= 0) return;
  // fiche de saisie
  const ca = win(t, T.demo, T.draw + .3, .4, .5);
  if (ca > 0) {
    const y0 = lerp(620, 560, eo3(prog(t, T.demo, T.demo + .6)));
    ctx.save(); ctx.globalAlpha = a * ca;
    ctx.fillStyle = rgba(COL.acier, .92); ctx.strokeStyle = rgba(COL.beton, .25); ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.roundRect(90, y0, 900, 520, 18); ctx.fill(); ctx.stroke();
    ctx.fillStyle = rgba(COL.nuit, .8); ctx.beginPath(); ctx.roundRect(90, y0, 900, 64, [18, 18, 0, 0]); ctx.fill();
    [COL.cuivre, COL.beton, COL.beton].forEach((c, i) => { ctx.fillStyle = rgba(c, .7); ctx.beginPath(); ctx.arc(126 + i * 26, y0 + 32, 7, 0, 7); ctx.fill(); });
    setFont(F('500 # Mono', 20, 4)); ctx.fillStyle = COL.beton; ctx.textAlign = 'left';
    ctx.fillText('CIVREBAR AI  ·  POUTRE P1', 214, y0 + 39);
    ctx.restore();
    FIELDS.forEach(([l, v], j) => field(t, l, v, y0 + 140 + j * 84, T.fields[j], a * ca));
    const bk = prog(t, T.click - .4, T.click - .1);
    if (bk > 0) {
      const press = decay(t, T.click, 8);
      ctx.save(); ctx.globalAlpha = a * ca * bk;
      ctx.fillStyle = t >= T.click ? COL.cuivre : rgba(COL.cuivre, .25);
      ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.roundRect(610 + press * 4, y0 + 440 + press * 3, 320 - press * 8, 60 - press * 6, 10); ctx.fill(); ctx.stroke();
      setFont(F('500 # Mono', 22, 6)); ctx.textAlign = 'center'; ctx.fillStyle = t >= T.click ? COL.nuit : COL.cuivreC;
      ctx.fillText('DESSINER', 770, y0 + 478);
      ctx.restore();
      if (t >= T.click) glow(770, y0 + 470, 220, COL.cuivre, .6 * press);
    }
  }
  const c1 = F('500 # Manrope', 42, 0);
  const a1 = a * (1 - prog(t, T.draw - .1, T.draw + .3));
  reveal(t, 'Vous saisissez la section,', CX, 1180, c1, { t0: T.fields[0], st: .015, dur: .6, mode: 'blur', color: COL.chaux, alpha: a1 });
  reveal(t, 'la portée et les armatures.', CX, 1240, c1, { t0: T.fields[0] + .4, st: .015, dur: .6, mode: 'blur', color: COL.chaux, alpha: a1 });
  // dessin
  if (t >= T.draw) {
    drawBeam(t, T.draw, a);
    reveal(t, 'CivRebar AI dessine barres,', CX, 1070, c1, { t0: T.cap2, st: .015, dur: .6, mode: 'blur', color: COL.chaux, alpha: a });
    reveal(t, 'cadres, cotes et repères.', CX, 1130, c1, { t0: T.cap2 + .4, st: .015, dur: .6, mode: 'blur', color: COL.chaux, alpha: a });
    reveal(t, 'Le ferraillage d’une poutre,', CX, 1290, F('600 # Sora', 60, -1), { t0: T.cmd[0], st: .025, dur: .5, mode: 'rise', color: COL.chaux, alpha: a });
    slam(t, 'en une commande.', CX, 1395, F('700 # Sora', 84, -2), T.cmd[1], COL.cuivre, 'center', a);
    glow(CX, 1370, 420, COL.cuivre, .25 * decay(t, T.cmd[1], 2) * a);
  }
}

// ------------------------------------------------------------ 7 : feuille de route (53 → 61.5)
const STEPS = ['Poutres', 'Poteaux · dalles · semelles · escaliers', 'Une boîte à outils', 'Un vrai plugin AutoCAD', 'Une IA qui vérifie et quantifie'];
function sceneRoad(t) {
  const a = win(t, T.road, T.roadOut + .5, .4, .5);
  if (a <= 0) return;
  const f = F('600 # Sora', 62, -1);
  reveal(t, 'On construit CivRebar', CX, 620, f, { t0: T.road, st: .025, dur: .5, mode: 'rise', color: COL.chaux, alpha: a });
  reveal(t, 'comme on ferraille :', CX, 700, f, { t0: T.road + .35, st: .025, dur: .5, mode: 'rise', color: COL.chaux, alpha: a });
  slam(t, 'barre après barre.', CX, 800, F('700 # Sora', 70, -1), T.road + 1.2, COL.cuivre, 'center', a);
  const x = 170, y0 = 930, dy = 110;
  // la barre qui relie les étapes
  const reach = clamp((t - T.steps) / .9, 0, STEPS.length - 1);
  ctx.save(); ctx.globalAlpha = a;
  ctx.strokeStyle = rgba(COL.beton, .2); ctx.lineWidth = 6;
  ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y0 + dy * (STEPS.length - 1)); ctx.stroke();
  if (t >= T.steps) {
    ctx.strokeStyle = COL.cuivre; ctx.shadowColor = rgba(COL.cuivre, .6); ctx.shadowBlur = 10;
    ctx.beginPath(); ctx.moveTo(x, y0); ctx.lineTo(x, y0 + dy * eio3(reach / (STEPS.length - 1)) * (STEPS.length - 1)); ctx.stroke();
    ctx.shadowBlur = 0;
  }
  ctx.restore();
  STEPS.forEach((s, i) => {
    const t0 = T.steps + i * .9, k = prog(t, t0, t0 + .35), y = y0 + i * dy;
    const last = i === STEPS.length - 1;
    ctx.save(); ctx.globalAlpha = a;
    ctx.fillStyle = k > 0 ? (last ? COL.signal : COL.cuivre) : COL.acier;
    ctx.strokeStyle = rgba(COL.beton, .4); ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(x, y, 13 + 6 * decay(t, t0, 6), 0, 7); ctx.fill(); if (k <= 0) ctx.stroke();
    ctx.restore();
    if (k > 0 && last) glow(x, y, 90, COL.signal, .6 + .2 * Math.sin(t * 4));
    if (k > 0) glow(x, y, 60, COL.cuivre, .5 * decay(t, t0, 4));
    ctx.save(); ctx.globalAlpha = a * k;
    setFont(F('500 # Mono', 22, 2)); ctx.textAlign = 'left'; ctx.fillStyle = last ? COL.signal : COL.cuivreC;
    ctx.fillText(String(i + 1).padStart(2, '0'), x + 44 - (1 - eo3(k)) * 20, y + 8);
    setFont(F('500 # Manrope', 36, 0)); ctx.fillStyle = last ? COL.signal : COL.chaux;
    ctx.fillText(s, x + 100 - (1 - eo3(k)) * 30, y + 12);
    ctx.restore();
  });
}

// ------------------------------------------------------------ 8 : la promesse (61.5 → 66.5)
function sceneProm(t) {
  const a = win(t, T.prom - .2, T.promOut + .5, .4, .5);
  if (a <= 0) return;
  const f = F('italic 400 # Serif', 84, 0);
  const L = [['Une intelligence', COL.chaux], ['qui assiste,', COL.chaux], ['sans jamais remplacer', COL.beton], ['celui qui signe le plan.', COL.cuivreC]];
  L.forEach(([s, c], i) => reveal(t, s, CX, 760 + i * 110, f, { t0: T.prom + i * .7, st: .03, dur: .8, mode: 'blur', color: c, alpha: a }));
  ctx.save(); ctx.globalAlpha = a * eo3(prog(t, T.prom + 3, T.prom + 3.6));
  ctx.fillStyle = COL.cuivre; ctx.fillRect(CX - 60, 1250, 120, 3);
  ctx.restore();
}

// ------------------------------------------------------------ 9 : l'annonce (66.5 → 72)
function sceneArrive(t) {
  const a = 1 - prog(t, T.out6, T.out6 + .5);
  if (t < T.qc || a <= 0) return;
  const f = F('600 # Sora', 112, -2);
  reveal(t, 'Quelque chose', CX, 780, f, { t0: T.qc, st: .03, dur: .55, mode: 'rise', color: COL.chaux, alpha: a });
  reveal(t, 'de grand', CX, 900, f, { t0: T.qc + .35, st: .03, dur: .55, mode: 'rise', color: COL.chaux, alpha: a });
  slam(t, 'arrive.', CX, 1050, F('700 # Sora', 150, -3), T.arrive, COL.cuivre, 'center', a);
  glow(CX, 1010, 460, COL.cuivre, .25 * decay(t, T.arrive, 2) * a);
  const fs = F('500 # Manrope', 40, .2);
  reveal(t, 'Le ferraillage assisté par IA,', CX, 1170, fs, { t0: T.sub, st: .015, dur: .6, mode: 'blur', color: COL.beton, alpha: a });
  reveal(t, 'directement dans AutoCAD.', CX, 1225, fs, { t0: T.sub + .3, st: .015, dur: .6, mode: 'blur', color: COL.beton, alpha: a });
  const rows = [['POUTRES', 'POTEAUX', 'DALLES'], ['SEMELLES', 'ESCALIERS']];
  const ft = F('500 # Mono', 26, 5), sep = '  ·  ';
  let n = 0;
  rows.forEach((row, r) => {
    setFont(ft);
    const tot = ctx.measureText(row.join(sep)).width;
    let x = CX - tot / 2;
    row.forEach((it, j) => {
      const t0 = T.ticker + n++ * .32, k = prog(t, t0, t0 + .25);
      setFont(ft);
      const w = ctx.measureText(it).width, y = 1330 + r * 56;
      if (k > 0) {
        const hot = decay(t, t0, 3);
        ctx.save(); ctx.globalAlpha = a * k;
        ctx.fillStyle = rgba(COL.signal, .14 * hot); ctx.fillRect(x - 10, y - 30, w + 12, 42);
        ctx.fillStyle = hot > .3 ? COL.signal : COL.beton; ctx.textAlign = 'left'; ctx.fillText(it, x, y);
        if (j < row.length - 1) { ctx.fillStyle = COL.cuivre; ctx.fillText(sep, x + w, y); }
        ctx.restore();
      }
      x += w + ctx.measureText(sep).width;
    });
  });
}

// ------------------------------------------------------------ 10 : rendez-vous (72 → 81)
function sceneRdv(t) {
  if (t < T.cut2) return;
  const out = prog(t, T.final - .7, T.final - .2);
  const f = F('600 # Sora', 116, -3);
  const lift = eio3(prog(t, T.bientot - .2, T.bientot + .4)) * 50;
  ctx.save();
  if (out > 0) ctx.filter = `blur(${(out * 20).toFixed(1)}px)`;
  reveal(t, 'Soyez', CX, 880 - lift, f, { t0: T.rdv, st: .03, dur: .6, mode: 'rise', color: COL.chaux, alpha: 1 - out });
  reveal(t, 'au rendez-vous.', CX, 1010 - lift, f, { t0: T.rdv + .25, st: .03, dur: .6, mode: 'rise', color: COL.chaux, alpha: 1 - out });
  ctx.restore();
  const sk = prog(t, T.rdv + .9, T.rdv + 1.9);
  if (sk > 0 && sk < 1 && out <= 0) {
    setFont(f);
    const w = ctx.measureText('au rendez-vous.').width, sx = CX - w / 2 - 200 + (w + 400) * eio3(sk);
    const g = ctx.createLinearGradient(sx - 140, 0, sx + 140, 0);
    g.addColorStop(0, 'rgba(255,255,255,0)'); g.addColorStop(.5, 'rgba(255,255,255,.95)'); g.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.save(); ctx.fillStyle = g; ctx.textAlign = 'center';
    ctx.fillText('Soyez', CX, 880 - lift); ctx.fillText('au rendez-vous.', CX, 1010 - lift);
    ctx.restore();
  }
  if (t >= T.bientot) {
    const fl = t < T.bientot + .5 ? (rnd(Math.floor(t * FPS)) > .45 ? 1 : .15) : 1;
    const bw = 110 * eo3(prog(t, T.bientot, T.bientot + .6));
    ctx.save(); ctx.globalAlpha = fl * (1 - out);
    if (out > 0) ctx.filter = `blur(${(out * 20).toFixed(1)}px)`;
    setFont(F('500 # Mono', 44, 26)); ctx.textAlign = 'center'; ctx.fillStyle = COL.cuivre;
    ctx.fillText('BIENTÔT', CX + 13, 1120);
    ctx.fillStyle = rgba(COL.cuivre, .6);
    ctx.fillRect(CX - 330, 1105, bw, 2); ctx.fillRect(CX + 330 - bw, 1105, bw, 2);
    ctx.restore();
  }
  if (t >= T.final - .05) {
    const k = eo3(prog(t, T.final, T.final + .9));
    const S = lerp(1.78, 1.6, k), cy = 800;
    const tr = symInLockupV(CX, cy, S);
    const [nx, ny] = symPt(tr, NODE.x, NODE.y);
    glow(CX, cy, 800, COL.acier, .6 * k);
    const breathe = .5 + .5 * Math.sin((t - T.final) * 2.6);
    glow(nx, ny, 110 + 300 * decay(t, T.final, 1.8) + 25 * breathe, COL.signal, .3 + .6 * decay(t, T.final, 1.3));
    ring(t, T.final, nx, ny, 1700, 1.4, COL.signal, 10);
    ring(t, T.final + .1, nx, ny, 1200, 1.6, COL.cuivre, 4);
    flare(nx, ny, decay(t, T.final, 2.2), 1900);
    sparks(t, T.final, 110, nx, ny, 311, [COL.signal, COL.chaux, COL.cuivreC]);
    ctx.save();
    if (k < 1) ctx.filter = `blur(${((1 - k) * 12).toFixed(1)}px)`;
    drawSymbol(tr, { alpha: k, bar: 1, rel: 1, node: 1, nodeGlow: 18 + 20 * breathe, glowBar: 4, glowRel: 3 });
    drawWordmarkV(t, CX, cy, S, { alpha: k, ...FULL });
    ctx.restore();
    reveal(t, 'L’intelligence de l’armature.', CX, 1220, F('italic 400 # Serif', 62, .5), {
      t0: T.final + .8, st: .03, dur: .7, mode: 'blur', color: COL.beton,
    });
    const ka = prog(t, T.final + 1.6, T.final + 2.3);
    ctx.save(); ctx.globalAlpha = ka * .9;
    setFont(F('500 # Mono', 24, 8)); ctx.textAlign = 'center'; ctx.fillStyle = COL.cuivreC;
    ctx.fillText('BIENTÔT DISPONIBLE', CX, 1340);
    ctx.fillStyle = COL.beton; ctx.fillText('PLUGIN AUTOCAD', CX, 1384);
    ctx.restore();
  }
}

// ------------------------------------------------------------ rendu
function letterbox(t) {
  let h;
  if (t < T.reveal) h = 150 + 50 * eio3(prog(t, 29.3, T.black));
  else h = 200 * (1 - eoX(prog(t, T.reveal, T.reveal + .7)));
  if (h <= 0) return;
  ctx.fillStyle = '#000';
  ctx.fillRect(0, 0, W, h); ctx.fillRect(0, H - h, W, h);
}
function renderFrame(t) {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over'; ctx.filter = 'none';
  ctx.fillStyle = COL.nuit; ctx.fillRect(0, 0, W, H);
  const [sx, sy] = shake(t);
  ctx.save();
  ctx.translate(sx, sy);
  const black = t >= T.black && t < T.reveal;
  if (!black) {
    let ga = 0;
    ga += .9 * win(t, T.colIn - .2, T.cut1, .6, .2);
    ga += .35 * win(t, T.cut1, T.hours, .1, .3);
    ga += .3 * win(t, T.hours, T.s4, .2, .2);
    ga += .45 * win(t, T.s4, T.black, .3, .05);
    ga += .35 * win(t, T.reveal, T.out6 + .6, .6, .4);
    ga += .3 * prog(t, T.final, T.final + 1) * (1 - prog(t, T.fade, DUR));
    const gz = t < T.cut1 ? lerp(1, 1.08, eio3(prog(t, T.colIn, T.cut1))) : 1 + (t % 20) * .004;
    grid(ga, gz);
    scene1(t); scene2(t); scene3(t); sceneHours(t); scene4(t);
    scene5(t); sceneDemo(t); sceneRoad(t); sceneProm(t); sceneArrive(t); sceneRdv(t);
  } else {
    ctx.fillStyle = '#000'; ctx.fillRect(-50, -50, W + 100, H + 100);
    scene5(t);
  }
  ctx.restore();
  const fl = Math.max(.9 * decay(t, T.reveal, 5), .5 * decay(t, T.cut1, 9), .75 * decay(t, T.final, 5), .5 * decay(t, T.intel, 10), .35 * decay(t, T.cut2, 9), .3 * decay(t, T.hours, 9));
  if (fl > .01) { ctx.fillStyle = `rgba(243,240,234,${fl})`; ctx.fillRect(0, 0, W, H); }
  if (black) { ctx.fillStyle = 'rgba(0,0,0,.35)'; ctx.fillRect(0, 0, W, H); }
  letterbox(t);
  vignette(.62);
  ctx.save();
  ctx.globalAlpha = .055; ctx.globalCompositeOperation = 'overlay';
  const gi = Math.floor(t * FPS);
  ctx.fillStyle = ctx.createPattern(GRAIN[gi % GRAIN.length], 'repeat');
  ctx.translate(-rnd(gi) * 256, -rnd(gi + 1) * 256);
  ctx.fillRect(0, 0, W + 256, H + 256);
  ctx.restore();
  const fade = Math.max(1 - prog(t, 0, .4), prog(t, T.fade, DUR - .3));
  if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
}

window.T = T;
window.MUSIC = MUSIC;
boot(renderFrame, DUR);
