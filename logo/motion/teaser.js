// CivRebar AI — teaser motion design paysage (1920x1080, 30 i/s, 52 s).
// Tout est déterministe : renderFrame(t) dessine l'image de l'instant t.
// Les repères sonores (CUES) et le plan musical (MUSIC) sont exportés pour sound.py.
const DUR = 52;

// Temps clés
const T = {
  beats: [0.9, 2.4, 3.9],
  beamIn: 5.4, stirrups: 7.0, milliers: 8.6, slams: [10.3, 10.95, 11.6], cut1: 12.5,
  rien: 13.0, tout: 15.5, calcule: 16.25, warp: 17.2, s4: 19.0,
  etsi: 19.3, devenait: 20.5, intel: 22.2, black: 25.0, reveal: 26.2,
  clang: 28.15, lockup: 30.0, letters: 30.55, divider: 31.1, ai: 31.55, tagline: 32.6,
  up: 35.2, qc: 35.9, arrive: 37.0, sub: 38.2, ticker: 39.4, out6: 42.4,
  cut2: 43.2, rdv: 43.4, bientot: 45.4, final: 47.6, fade: 50.6,
};

// Battements de cœur (lub-dub)
T.beats.forEach(b => { cue(b, 'heart', 1); cue(b + .24, 'heart', .6); });
cue(0.0, 'drone', 1);
// Frappe clavier
const TYPE_LINES = [
  { s: '> PROJET CONFIDENTIEL', t0: .5, cps: 22 },
  { s: '> ANALYSE DU PLAN EN COURS', t0: 1.8, cps: 24 },
  { s: '> CHARGEMENT', t0: 3.2, cps: 24 },
];
TYPE_LINES.forEach(L => { for (let i = 0; i < L.s.length; i++) if (L.s[i] !== ' ') cue(L.t0 + i / L.cps, 'key', .5 + .3 * rnd(i + L.t0)); });
cue(5.0, 'whoosh', .9);
cue(T.beamIn, 'draw', .6);
// Cadres de la poutre
const STIR = [];
{ let x = 300; while (x <= 1620) { STIR.push(x); x += (x < 660 || x > 1260) ? 36 : 72; } }
STIR.forEach((x, i) => cue(T.stirrups + i * (1.5 / STIR.length), 'tick', .45));
cue(T.milliers, 'swell', .6);
T.slams.forEach((s, i) => { cue(s, 'slam', i === 2 ? 1.1 : .9); shakeAt(s, i === 2 ? 14 : 9); });
cue(T.cut1, 'impact', .8); shakeAt(T.cut1, 8);
cue(T.rien, 'chime', .5);
cue(T.calcule, 'slam', 1.1); shakeAt(T.calcule, 12);
cue(16.5, 'riser', 1);
cue(T.warp, 'whoosh', 1.2);
cue(T.s4, 'impact', .5);
cue(T.intel, 'glitch', 1.1); cue(T.intel, 'slam', .9); shakeAt(T.intel, 16);
[23.1, 23.9, 24.35, 24.6, 24.8].forEach((g, i) => cue(g, 'glitch', .5 + i * .12));
cue(25.55, 'suck', 1.2);
cue(T.reveal, 'boom', 1.4); shakeAt(T.reveal, 26);
cue(T.reveal + .05, 'draw', 1);
cue(T.clang, 'clang', 1.2); shakeAt(T.clang, 10);
cue(T.reveal + .3, 'music', 1);
cue(T.lockup - .15, 'whoosh', .7);
for (let i = 0; i < 8; i++) cue(T.letters + i * .06, 'tick', .55);
cue(T.divider, 'tick', .8);
cue(T.ai, 'glitch', .8); cue(T.ai + .02, 'slam', .7); shakeAt(T.ai, 6);
cue(T.tagline, 'chime', .8);
cue(T.up - .1, 'whoosh', .6);
cue(T.qc, 'swell', .5);
cue(T.arrive, 'boom', .9); shakeAt(T.arrive, 12);
cue(T.sub, 'chime', .45);
for (let i = 0; i < 5; i++) cue(T.ticker + i * .42, 'blip', .7);
cue(T.out6, 'whoosh', .6);
cue(T.cut2, 'impact', .9); shakeAt(T.cut2, 8);
cue(T.rdv + .9, 'shine', .8);
cue(T.bientot, 'glitch', .45); cue(T.bientot, 'blip', .7);
cue(46.9, 'suck', .8);
cue(T.final, 'boom', 1.5); shakeAt(T.final, 18);
cue(T.final + .9, 'chime', .9);
TENSION.push([23.8, 25]);
// Plan musical (lu par sound.py)
const MUSIC = {
  drone: [0, 25], pedal: [12.5, 25], riser: [16.5, 25],
  chords: [['Dm', 26.4, 30.5], ['Bb', 30.5, 34.5], ['F', 34.5, 38.5], ['C', 38.5, 43.2]],
  bass: [[30.5, 43.2]], arp: [[34.5, 43.2]], kick: [[34.5, 38.5, .28], [38.5, 43.1, .45]],
  suspense: [43.2, 47.6], suspenseHearts: [44.0, 45.5, 47.0], final: 47.6,
};

// ------------------------------------------------------------ logo horizontal
const GLYPHS = LOGO.word.glyphs.map(g => ({ dx: g.dx, p: new Path2D(g.d) }));
const AIG = LOGO.ai.glyphs.map(g => ({ dx: g.dx, p: new Path2D(g.d) }));
const LC = { x: 643, y: 125 }; // centre optique du logo horizontal

const symInLockup = (cx, cy, S) => ({ ox: cx + (-5 - LC.x) * S, oy: cy + (-10 - LC.y) * S, s: S });
// Nom « CIVREBAR | AI » ; o.letters = [0..1] par lettre, o.divider, o.ai, o.aiGlitch
function drawWordmark(t, cx, cy, S, o) {
  ctx.save();
  ctx.translate(cx, cy); ctx.scale(S, S); ctx.translate(-LC.x, -LC.y);
  ctx.globalAlpha = o.alpha == null ? 1 : o.alpha;
  // CIVREBAR
  ctx.save();
  ctx.beginPath(); ctx.rect(200, 60, 900, 118); ctx.clip();
  GLYPHS.forEach((g, i) => {
    const k = o.letters[i];
    if (k <= 0) return;
    const e = eoX(k);
    ctx.save();
    ctx.translate(LOGO.word.tx + g.dx, LOGO.word.ty + (1 - e) * 115);
    ctx.scale(.118, -.118);
    ctx.fillStyle = COL.chaux; ctx.fill(g.p);
    ctx.restore();
  });
  ctx.restore();
  // Filet cuivre
  if (o.divider > 0) {
    const h = 98.14 * eo3(o.divider), cyD = 80.93 + 98.14 / 2;
    ctx.fillStyle = COL.cuivre; ctx.fillRect(1085.58, cyD - h / 2, 3, h);
  }
  // AI
  if (o.ai > 0) {
    const g = o.aiGlitch || 0, fr = Math.floor(t * FPS);
    const drawAI = (color, dx, dy, a) => {
      ctx.save(); ctx.globalAlpha *= a;
      ctx.translate(LOGO.ai.tx + dx, LOGO.ai.ty + dy);
      AIG.forEach(q => { ctx.save(); ctx.translate(q.dx, 0); ctx.scale(.118, -.118); ctx.fillStyle = color; ctx.fill(q.p); ctx.restore(); });
      ctx.restore();
    };
    if (g > .01) {
      ctx.save(); ctx.globalCompositeOperation = 'lighter';
      drawAI(COL.signal, -10 - 18 * g * rnd(fr), 0, .8 * g);
      drawAI('#d0343a', 10 + 14 * g * rnd(fr + 1), 0, .6 * g);
      ctx.restore();
      drawAI(COL.cuivre, (rnd(fr + 5) - .5) * 30 * g, 0, o.ai * (rnd(fr + 9) > .25 * g ? 1 : .2));
    } else drawAI(COL.cuivre, 0, 0, o.ai);
  }
  ctx.restore();
}

// ------------------------------------------------------------ éléments de scène
// Tracés « circuit » en Signal (scène 4)
const TRACES = [];
for (let i = 0; i < 44; i++) {
  const a = (i / 44) * Math.PI * 2 + rnd(i) * .3;
  let x = W / 2 + Math.cos(a) * 330, y = H / 2 + Math.sin(a) * 200;
  x = Math.round(x / 48) * 48; y = Math.round(y / 48) * 48;
  const pts = [[x, y]];
  const steps = 6 + Math.floor(rnd(i + 50) * 9);
  for (let s = 0; s < steps; s++) {
    const horiz = rnd(i * 31 + s) > .45;
    const len = 48 * (1 + Math.floor(rnd(i * 17 + s) * 4));
    if (horiz) x += Math.sign(Math.cos(a) || 1) * len; else y += Math.sign(Math.sin(a) || 1) * len;
    pts.push([x, y]);
  }
  let L = 0; for (let k = 1; k < pts.length; k++) L += Math.hypot(pts[k][0] - pts[k - 1][0], pts[k][1] - pts[k - 1][1]);
  TRACES.push({ pts, L, delay: rnd(i + 7) * .9 });
}
// ------------------------------------------------------------ scène 1 : veille (0 → 5.4)
function scene1(t) {
  const cx = W / 2, cy = 470;
  const a = win(t, .3, 5.6, .5, .5);
  if (a <= 0) return;
  let pulse = 0;
  T.beats.forEach(b => { pulse += decay(t, b, 9) + .6 * decay(t, b + .24, 11); });
  // Anneaux de battement
  T.beats.forEach(b => ring(t, b, cx, cy, 380, 1.4, COL.signal, 3));
  // Point : se transforme en trait horizontal à 5.0
  const st = eio3(prog(t, 5.0, 5.45));
  ctx.save(); ctx.globalAlpha = a;
  glow(cx, cy, 70 + pulse * 110, COL.signal, .35 + pulse * .4);
  if (st <= 0) {
    ctx.fillStyle = COL.signal; ctx.shadowColor = COL.signal; ctx.shadowBlur = 20 + pulse * 30;
    ctx.beginPath(); ctx.arc(cx, cy, 7 + pulse * 5, 0, Math.PI * 2); ctx.fill();
  } else {
    const half = st * W * .6;
    ctx.fillStyle = COL.signal; ctx.shadowColor = COL.signal; ctx.shadowBlur = 25;
    ctx.fillRect(cx - half, cy - 3 * (1 - st) - 1.5, half * 2, 3 + 6 * (1 - st));
  }
  ctx.restore();
  flare(cx, cy, st * (1 - prog(t, 5.3, 5.6)) * .9, 1900);
  // Phrase
  reveal(t, 'Chaque ouvrage cache une ossature.', cx, 640, F('300 # Sora', 58, 1), {
    t0: 2.7, st: .035, dur: .7, mode: 'blur', color: COL.chaux, alpha: 1 - prog(t, 4.8, 5.2),
  });
  // Terminal
  const ta = 1 - prog(t, 4.9, 5.3);
  TYPE_LINES.forEach((L, j) => {
    const n = Math.floor(clamp((t - L.t0) * L.cps, 0, L.s.length));
    if (n <= 0) return;
    let s = L.s.slice(0, n);
    if (j === 2 && n === L.s.length) {
      const pct = Math.floor(100 * eio3(prog(t, 3.8, 4.7)));
      const bars = Math.floor(pct / 5);
      s += '  [' + '■'.repeat(bars) + '·'.repeat(20 - bars) + '] ' + String(pct).padStart(3, ' ') + '%';
    }
    ctx.save(); ctx.globalAlpha = ta * .85;
    setFont(F('400 # Mono', 19, 1)); ctx.textAlign = 'left';
    ctx.fillStyle = j === 0 ? COL.cuivreC : COL.beton;
    ctx.fillText(s, 140, 812 + j * 34);
    const blink = Math.floor(t * 3) % 2 === 0;
    const last = TYPE_LINES.reduce((m, q, idx) => (t >= q.t0 ? idx : m), 0);
    if (j === last && blink) { const w = ctx.measureText(s).width; ctx.fillStyle = COL.signal; ctx.fillRect(140 + w + 6, 796 + j * 34, 11, 20); }
    ctx.restore();
  });
  // Mentions de coin
  ctx.save(); ctx.globalAlpha = ta * .5 * prog(t, .6, 1.2);
  setFont(F('400 # Mono', 15, 3)); ctx.fillStyle = COL.beton; ctx.textAlign = 'right';
  ctx.fillText('RÉF. 00-CR  ·  NE PAS DIFFUSER', W - 140, 200);
  ctx.restore();
}

// ------------------------------------------------------------ scène 2 : la poutre (5.4 → 12.5)
function scene2(t) {
  const a = win(t, T.beamIn, T.cut1, .4, .25);
  if (a <= 0) return;
  const zoom = lerp(1, 1.12, eio3(prog(t, T.beamIn, T.cut1)));
  const dim = lerp(1, .38, eo3(prog(t, T.slams[0] - .2, T.slams[0] + .3)));
  ctx.save();
  ctx.globalAlpha = a * dim;
  ctx.translate(W / 2, H / 2); ctx.scale(zoom, zoom); ctx.translate(-W / 2 - 20 * prog(t, 5.4, 12.5), -H / 2);
  const X0 = 240, X1 = 1680, Y0 = 430, Y1 = 650;
  // Béton : contour + poteaux
  const pc = eo3(prog(t, 5.5, 6.6));
  ctx.strokeStyle = rgba(COL.beton, .75); ctx.lineWidth = 2;
  ctx.setLineDash([2 * (X1 - X0 + Y1 - Y0) * pc, 5000]);
  ctx.strokeRect(X0, Y0, X1 - X0, Y1 - Y0); ctx.setLineDash([]);
  const pp = eo3(prog(t, 6.0, 6.8));
  [[X0, X0 + 70], [X1 - 70, X1]].forEach(([a0, a1]) => {
    ctx.strokeRect(a0, Y1, a1 - a0, 130 * pp);
    ctx.save(); ctx.beginPath(); ctx.rect(a0, Y1, a1 - a0, 130 * pp); ctx.clip();
    ctx.strokeStyle = rgba(COL.beton, .3); ctx.lineWidth = 1;
    for (let k = -140; k < 140; k += 14) { ctx.beginPath(); ctx.moveTo(a0 + k, Y1 + 140); ctx.lineTo(a0 + k + 140, Y1); ctx.stroke(); }
    ctx.restore();
  });
  // Barres longitudinales (cuivre) avec crochets
  const bars = [
    { y: 462, t0: 5.9, hook: 1 }, { y: 618, t0: 6.2, hook: -1 },
  ];
  bars.forEach(b => {
    const k = eo3(prog(t, b.t0, b.t0 + 1.1));
    if (k <= 0) return;
    const pts = [[X0 + 40, b.y + b.hook * 60], [X0 + 40, b.y], [X1 - 40, b.y], [X1 - 40, b.y + b.hook * 60]];
    const L = 120 + (X1 - X0 - 80);
    ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 6; ctx.lineJoin = 'round';
    ctx.shadowColor = rgba(COL.cuivre, .6); ctx.shadowBlur = 12;
    const tip = drawPolyPartial(pts, L, k);
    ctx.shadowBlur = 0;
    if (k < 1) glow(tip[0], tip[1], 40, COL.cuivreC, .9);
  });
  // Cadres
  STIR.forEach((x, i) => {
    const t0 = T.stirrups + i * (1.5 / STIR.length);
    const k = eoX(prog(t, t0, t0 + .18));
    if (k <= 0) return;
    ctx.strokeStyle = rgba(COL.chaux, .85); ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(x, 450); ctx.lineTo(x, 450 + (630 - 450) * k); ctx.stroke();
    const fl = decay(t, t0, 12);
    if (fl > .02) glow(x, 540, 50, COL.signal, fl * .7);
  });
  // Cotes & repères
  const ca = eo3(prog(t, 8.1, 8.8));
  if (ca > 0) {
    ctx.globalAlpha = a * dim * ca;
    setFont(F('500 # Mono', 18, 1)); ctx.fillStyle = COL.beton; ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 1.2;
    // cote générale
    ctx.beginPath(); ctx.moveTo(X0 + 70, 740); ctx.lineTo(X1 - 70, 740); ctx.stroke();
    [X0 + 70, X1 - 70].forEach(x => { ctx.beginPath(); ctx.moveTo(x - 7, 747); ctx.lineTo(x + 7, 733); ctx.moveTo(x, 725); ctx.lineTo(x, 755); ctx.stroke(); });
    ctx.textAlign = 'center'; ctx.fillStyle = COL.nuit; ctx.fillRect(W / 2 - 80, 726, 160, 28);
    ctx.fillStyle = COL.chaux; ctx.fillText('L = 5,40 m', W / 2, 747);
    ctx.textAlign = 'left';
    const lead = (x0, y0, x1, y1, s, c) => { ctx.strokeStyle = rgba(COL.beton, .7); ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.lineTo(x1 + 30, y1); ctx.stroke(); ctx.fillStyle = c; ctx.fillText(s, x1 + 38, y1 + 6); ctx.beginPath(); ctx.arc(x0, y0, 3.5, 0, 7); ctx.fill(); };
    lead(520, 462, 560, 380, '2 HA14', COL.cuivreC);
    lead(1300, 618, 1340, 700, '3 HA20', COL.cuivreC);
    lead(900, 470, 960, 380, 'Cadres HA8 — e = 15 cm', COL.chaux);
    setFont(F('500 # Mono', 16, 3)); ctx.fillStyle = COL.signal;
    ctx.fillText('POUTRE P1 — 30 × 60', X0, 405 - 40);
  }
  ctx.restore();
  // Textes
  reveal(t, 'Des milliers de barres.', W / 2, 250, F('600 # Sora', 78, -1), {
    t0: T.milliers, st: .03, dur: .55, mode: 'rise', color: COL.chaux, alpha: a * (1 - prog(t, 12.0, 12.4)),
  });
  const words = ['Choisies.', 'Pliées.', 'Placées.'], f = F('700 # Sora', 84, -1);
  setFont(f);
  const ws = words.map(w => ctx.measureText(w).width), gap = 56, tot = ws.reduce((s, v) => s + v, 0) + gap * 2;
  let x = W / 2 - tot / 2;
  words.forEach((w, i) => {
    slam(t, w, x + ws[i] / 2, 900, f, T.slams[i], i === 2 ? COL.cuivre : COL.chaux, 'center', a * (1 - prog(t, 12.1, 12.45)));
    x += ws[i] + gap;
  });
}

// ------------------------------------------------------------ scène 3 : le calcul (12.5 → 19)
const DATA = ['HA12', 'HA16', 'HA20', 'HA8 e=15', 'As = 4,52 cm²', 'c = 3 cm', 'L = 5,40 m', 'ELU', 'ELS', 'M = 124 kN·m', 'V = 86 kN', 'fc28 = 25 MPa', 'fe 500', '×24', 'ls = 50Ø', 'e = 20 cm', '30 × 60', 'Ø10', 'HA25', 'σ ≤ 0,6 fc28'];
function scene3(t) {
  const a = win(t, T.cut1, T.s4, .15, .35);
  if (a <= 0) return;
  const ph = (t - T.cut1) * .085 + .75 * Math.pow(Math.max(0, t - T.warp), 2);
  const fast = clamp((t - T.warp) * 1.2);
  ctx.save();
  for (let i = 0; i < 120; i++) {
    const ang = rnd(i * 1.7) * Math.PI * 2, z0 = rnd(i * 2.3 + 9);
    const d = (z0 + ph) % 1;
    const dd = d * d;
    const dist = 90 + Math.pow(d, 2.2) * 1250;
    const sc = .4 + dd * 2.6;
    const x = W / 2 + Math.cos(ang) * dist * 1.25, y = H / 2 + Math.sin(ang) * dist * .8;
    const al = a * clamp(d * 5) * (1 - clamp((d - .85) * 6)) * .55;
    if (al <= .01) continue;
    const col = i % 7 === 0 ? COL.cuivreC : i % 11 === 0 ? COL.signal : COL.beton;
    if (fast > 0) {
      const d2 = Math.max(0, d - .06 * fast), dist2 = 90 + Math.pow(d2, 2.2) * 1250;
      ctx.strokeStyle = rgba(col, al * fast); ctx.lineWidth = 1 + sc;
      ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(W / 2 + Math.cos(ang) * dist2 * 1.25, H / 2 + Math.sin(ang) * dist2 * .8); ctx.stroke();
    }
    ctx.globalAlpha = al * (1 - fast * .6);
    setFont(F('500 # Mono', Math.round(17 * sc), 1)); ctx.textAlign = 'center'; ctx.fillStyle = col;
    ctx.fillText(DATA[i % DATA.length], x, y);
    ctx.globalAlpha = 1;
  }
  ctx.restore();
  // voile central pour la lisibilité
  const g = ctx.createRadialGradient(W / 2, H / 2, 0, W / 2, H / 2, 620);
  g.addColorStop(0, rgba(COL.nuit, .92 * a)); g.addColorStop(1, rgba(COL.nuit, 0));
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  reveal(t, 'Rien n’y est décoratif.', W / 2, 560, F('italic 400 # Serif', 118, 0), {
    t0: T.rien, st: .04, dur: .8, mode: 'blur', color: COL.chaux, alpha: a * (1 - prog(t, 15.0, 15.4)),
  });
  // « Tout y est calculé. »
  const out = prog(t, 17.9, 18.6), f = F('600 # Sora', 104, -2);
  setFont(f);
  const w1 = ctx.measureText('Tout y est ').width, w2 = ctx.measureText('calculé.').width;
  const x0 = W / 2 - (w1 + w2) / 2;
  ctx.save();
  ctx.translate(W / 2, 555); ctx.scale(1 + out * .6, 1 + out * .6); ctx.translate(-W / 2, -555);
  if (out > 0) ctx.filter = `blur(${(out * 18).toFixed(1)}px)`;
  reveal(t, 'Tout y est', x0, 590, f, { t0: T.tout, st: .035, dur: .5, mode: 'rise', color: COL.chaux, align: 'left', alpha: a * (1 - out) });
  slam(t, 'calculé.', x0 + w1 + w2 / 2, 590, f, T.calcule, COL.cuivre, 'center', a * (1 - out));
  ctx.restore();
}

// ------------------------------------------------------------ scène 4 : la question (19 → 25)
function scene4(t) {
  if (t < T.s4 || t >= T.black) return;
  const a = prog(t, T.s4, T.s4 + .3);
  // tracés Signal
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
      // impulsion qui circule
      const pk = ((t - T.intel) * .7 + tr.delay) % 1;
      if (k >= 1 && i % 3 === 0) { const q = drawPolyPartialPoint(tr.pts, tr.L, pk); glow(q[0], q[1], 26, COL.signal, .8); }
    });
    ctx.restore();
    const g = ctx.createRadialGradient(W / 2, H / 2, 0, W / 2, H / 2, 700);
    g.addColorStop(0, rgba(COL.nuit, .95)); g.addColorStop(1, rgba(COL.nuit, 0));
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  }
  const outQ = prog(t, 21.85, 22.15);
  const fq = F('300 # Sora', 92, -1);
  ctx.save();
  if (outQ > 0) ctx.filter = `blur(${(outQ * 14).toFixed(1)}px)`;
  reveal(t, 'Et si l’armature', W / 2, 470, fq, { t0: T.etsi, st: .04, dur: .6, mode: 'rise', color: COL.chaux, alpha: a * (1 - outQ) });
  reveal(t, 'devenait…', W / 2, 590, fq, { t0: T.devenait, st: .05, dur: .6, mode: 'rise', color: COL.chaux, alpha: a * (1 - outQ) });
  ctx.restore();
  if (t >= T.intel) {
    let g = t < T.intel + .25 ? .9 * (1 - prog(t, T.intel, T.intel + .25)) : 0;
    [23.1, 23.9, 24.35, 24.6, 24.8].forEach(b => { if (t >= b && t < b + .1) g = Math.max(g, .45); });
    g = Math.max(g, Math.pow(prog(t, 24.3, 25), 2) * .9);
    const sc = 1 + .05 * eo3(prog(t, T.intel, 25));
    glow(W / 2, 540, 700, COL.signal, .10 + .05 * Math.sin(t * 6));
    ctx.save(); ctx.translate(W / 2, 540); ctx.scale(sc, sc); ctx.translate(-W / 2, -540);
    glitchText(t, 'intelligente ?', W / 2, 600, F('700 # Sora', 176, -4), COL.signal, g, 3, clamp((t - T.intel) * 10));
    ctx.restore();
  }
}
// ------------------------------------------------------------ scène 5+ : révélation du logo
const TR_INTRO = { ox: W / 2 - 125 * 2.1, oy: H / 2 - 135 * 2.1 + 10, s: 2.1 };
function logoState(t) {
  // position / échelle du logo horizontal au fil du temps
  let cx = W / 2, cy = 520, S = 1.05;
  const up = eio3(prog(t, T.up, T.up + .9));
  cy = lerp(cy, 250, up); S = lerp(S, .58, up);
  return { cx, cy, S };
}
function scene5(t) {
  if (t < 25.5 || t >= 43.1) return;
  // pré-lueur du nœud pendant le noir
  if (t < T.reveal) {
    const k = prog(t, 25.55, T.reveal);
    const [nx, ny] = symPt(TR_INTRO, NODE.x, NODE.y);
    glow(nx, ny, 30 + ei3(k) * 160, COL.signal, ei3(k) * .9);
    ctx.save(); ctx.fillStyle = rgba(COL.signal, ei3(k));
    ctx.beginPath(); ctx.arc(nx, ny, 2 + ei3(k) * 12, 0, 7); ctx.fill(); ctx.restore();
    return;
  }
  const out = prog(t, T.out6, T.out6 + .5);
  const A = 1 - out;
  const L = logoState(t);
  const k = eio3(prog(t, T.lockup, T.lockup + 1.0));
  const TL = symInLockup(L.cx, L.cy, L.S);
  const tr = { ox: lerp(TR_INTRO.ox, TL.ox, k), oy: lerp(TR_INTRO.oy, TL.oy, k), s: lerp(TR_INTRO.s, TL.s, k) };
  const [nx, ny] = symPt(tr, NODE.x, NODE.y);
  // halo de fond
  glow(W / 2, L.cy, 900, COL.acier, .55 * A);
  const breathe = .5 + .5 * Math.sin((t - T.reveal) * 2.6);
  glow(nx, ny, 120 + 260 * decay(t, T.reveal, 1.6) + 30 * breathe, COL.signal, (.35 + .6 * decay(t, T.reveal, 1.2)) * A);
  // anneaux, étincelles
  ring(t, T.reveal, nx, ny, 1400, 1.3, COL.signal, 10);
  ring(t, T.reveal + .12, nx, ny, 1000, 1.5, COL.chaux, 4);
  ring(t, T.reveal + .3, nx, ny, 700, 1.4, COL.cuivre, 3);
  sparks(t, T.reveal, 140, nx, ny, 11, [COL.signal, COL.chaux, COL.cuivreC, COL.signal]);
  flare(nx, ny, decay(t, T.reveal, 2.2) * 1.0, 2400);
  // tracé du symbole
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
  // nom
  const letters = GLYPHS.map((_, i) => prog(t, T.letters + i * .06, T.letters + i * .06 + .55));
  const aiG = t >= T.ai && t < T.ai + .45 ? 1 - prog(t, T.ai, T.ai + .45) : 0;
  drawWordmark(t, L.cx, L.cy, L.S, {
    alpha: A, letters, divider: prog(t, T.divider, T.divider + .35),
    ai: t >= T.ai ? 1 : 0, aiGlitch: aiG,
  });
  // signature
  reveal(t, 'L’intelligence de l’armature.', W / 2, L.cy + 190, F('italic 400 # Serif', 54, .5), {
    t0: T.tagline, st: .03, dur: .7, mode: 'blur', color: COL.beton, alpha: 1 - prog(t, T.up - .3, T.up + .1),
  });
  // scène 6 : l'annonce
  const f1 = F('600 # Sora', 100, -2);
  reveal(t, 'Quelque chose de grand', W / 2, 560, f1, { t0: T.qc, st: .03, dur: .55, mode: 'rise', color: COL.chaux, alpha: A });
  slam(t, 'arrive.', W / 2, 690, F('700 # Sora', 128, -3), T.arrive, COL.cuivre, 'center', A);
  glow(W / 2, 650, 500, COL.cuivre, .25 * decay(t, T.arrive, 2) * A);
  reveal(t, 'Le ferraillage assisté par IA, directement dans AutoCAD.', W / 2, 800, F('500 # Manrope', 34, .2), {
    t0: T.sub, st: .012, dur: .6, mode: 'blur', color: COL.beton, alpha: A,
  });
  // téléscripteur
  const items = ['POUTRES', 'POTEAUX', 'DALLES', 'SEMELLES', 'ESCALIERS'];
  const ft = F('500 # Mono', 24, 5);
  setFont(ft);
  const sep = '   ·   ';
  const full = items.join(sep);
  const totW = ctx.measureText(full).width;
  let x = W / 2 - totW / 2;
  items.forEach((it, i) => {
    const t0 = T.ticker + i * .42;
    const k = prog(t, t0, t0 + .25);
    setFont(ft);
    const w = ctx.measureText(it).width;
    if (k > 0) {
      const hot = decay(t, t0, 3);
      ctx.save(); ctx.globalAlpha = A * k;
      ctx.fillStyle = rgba(COL.signal, .14 * hot); ctx.fillRect(x - 12, 900 - 28, w + 14, 40);
      ctx.fillStyle = hot > .3 ? COL.signal : COL.beton; ctx.textAlign = 'left';
      ctx.fillText(it, x, 900);
      if (i < items.length - 1) { ctx.fillStyle = COL.cuivre; ctx.fillText(sep, x + w, 900); }
      ctx.restore();
    }
    x += w + ctx.measureText(sep).width;
  });
}

// ------------------------------------------------------------ scène 7 : rendez-vous (43.2 → 52)
function scene7(t) {
  if (t < T.cut2) return;
  const out = prog(t, 46.9, 47.4);
  const f = F('600 # Sora', 124, -3);
  ctx.save();
  if (out > 0) { ctx.filter = `blur(${(out * 20).toFixed(1)}px)`; }
  const y = lerp(560, 520, eio3(prog(t, T.bientot - .2, T.bientot + .4)));
  reveal(t, 'Soyez au rendez-vous.', W / 2, y, f, { t0: T.rdv, st: .03, dur: .6, mode: 'rise', color: COL.chaux, alpha: 1 - out });
  ctx.restore();
  // reflet qui balaie le texte
  const sk = prog(t, T.rdv + .9, T.rdv + 1.9);
  if (sk > 0 && sk < 1 && out <= 0) {
    setFont(f); const w = ctx.measureText('Soyez au rendez-vous.').width;
    const sx = W / 2 - w / 2 - 200 + (w + 400) * eio3(sk);
    const g = ctx.createLinearGradient(sx - 140, 0, sx + 140, 0);
    g.addColorStop(0, 'rgba(255,255,255,0)'); g.addColorStop(.5, 'rgba(255,255,255,.95)'); g.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.save(); ctx.fillStyle = g; ctx.textAlign = 'center'; ctx.fillText('Soyez au rendez-vous.', W / 2, y);
    ctx.globalCompositeOperation = 'lighter'; ctx.globalAlpha = .5; ctx.fillStyle = g; ctx.fillText('Soyez au rendez-vous.', W / 2, y);
    ctx.restore();
  }
  // BIENTÔT
  if (t >= T.bientot) {
    const fl = t < T.bientot + .5 ? (rnd(Math.floor(t * FPS)) > .45 ? 1 : .15) : 1;
    ctx.save(); ctx.globalAlpha = fl * (1 - out);
    if (out > 0) ctx.filter = `blur(${(out * 20).toFixed(1)}px)`;
    setFont(F('500 # Mono', 40, 30)); ctx.textAlign = 'center'; ctx.fillStyle = COL.cuivre;
    ctx.fillText('BIENTÔT', W / 2 + 15, 650);
    ctx.fillStyle = rgba(COL.cuivre, .6);
    ctx.fillRect(W / 2 - 330, 636, 110 * eo3(prog(t, T.bientot, T.bientot + .6)), 2);
    ctx.fillRect(W / 2 + 330 - 110 * eo3(prog(t, T.bientot, T.bientot + .6)), 636, 110 * eo3(prog(t, T.bientot, T.bientot + .6)), 2);
    ctx.restore();
  }
  // Logo final
  if (t >= T.final - .05) {
    const k = eo3(prog(t, T.final, T.final + .9));
    const S = lerp(1.14, 1.0, k), cx = W / 2, cy = 470;
    const tr = symInLockup(cx, cy, S);
    const [nx, ny] = symPt(tr, NODE.x, NODE.y);
    glow(W / 2, cy, 900, COL.acier, .6 * k);
    const breathe = .5 + .5 * Math.sin((t - T.final) * 2.6);
    glow(nx, ny, 110 + 300 * decay(t, T.final, 1.8) + 25 * breathe, COL.signal, .35 + .6 * decay(t, T.final, 1.3));
    ring(t, T.final, nx, ny, 1500, 1.4, COL.signal, 10);
    ring(t, T.final + .1, nx, ny, 1100, 1.6, COL.cuivre, 4);
    flare(nx, ny, decay(t, T.final, 2.2), 2600);
    sparks(t, T.final, 110, nx, ny, 311, [COL.signal, COL.chaux, COL.cuivreC]);
    ctx.save();
    if (k < 1) ctx.filter = `blur(${((1 - k) * 12).toFixed(1)}px)`;
    drawSymbol(tr, { alpha: k, bar: 1, rel: 1, node: 1, nodeGlow: 18 + 20 * breathe, glowBar: 4, glowRel: 3 });
    drawWordmark(t, cx, cy, S, { alpha: k, letters: GLYPHS.map(() => 1), divider: 1, ai: 1 });
    ctx.restore();
    reveal(t, 'L’intelligence de l’armature.', W / 2, cy + 185, F('italic 400 # Serif', 54, .5), {
      t0: T.final + .8, st: .03, dur: .7, mode: 'blur', color: COL.beton,
    });
    const ka = prog(t, T.final + 1.6, T.final + 2.3);
    ctx.save(); ctx.globalAlpha = ka * .9;
    setFont(F('500 # Mono', 20, 8)); ctx.textAlign = 'center'; ctx.fillStyle = COL.cuivreC;
    ctx.fillText('BIENTÔT DISPONIBLE  ·  PLUGIN AUTOCAD', W / 2, cy + 300);
    ctx.restore();
  }
}

// ------------------------------------------------------------ rendu
function letterbox(t) {
  let h;
  if (t < T.reveal) h = 112 + 46 * eio3(prog(t, 23.8, 25)) - 112 * (1 - eo3(prog(t, 0, .01)));
  else h = 158 * (1 - eoX(prog(t, T.reveal, T.reveal + .7)));
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
    // grille de plan : présente selon la scène
    let ga = 0;
    ga += .9 * win(t, T.beamIn - .2, T.cut1, .6, .2);
    ga += .35 * win(t, T.cut1, T.s4, .1, .3);
    ga += .45 * win(t, T.s4, T.black, .3, .05);
    ga += .35 * win(t, T.reveal, 43.1, .6, .4);
    ga += .3 * prog(t, T.final, T.final + 1) * (1 - prog(t, T.fade, DUR));
    const gz = t < T.cut1 ? lerp(1, 1.12, eio3(prog(t, T.beamIn, T.cut1))) : 1 + (t % 20) * .004;
    grid(ga, gz);
    scene1(t); scene2(t); scene3(t); scene4(t); scene5(t); scene7(t);
  } else {
    ctx.fillStyle = '#000'; ctx.fillRect(-50, -50, W + 100, H + 100);
    scene5(t);
  }
  ctx.restore();
  // flashs
  const fl = Math.max(.9 * decay(t, T.reveal, 5), .5 * decay(t, T.cut1, 9), .75 * decay(t, T.final, 5), .5 * decay(t, T.intel, 10), .35 * decay(t, T.cut2, 9));
  if (fl > .01) { ctx.fillStyle = `rgba(243,240,234,${fl})`; ctx.fillRect(0, 0, W, H); }
  // noir complet entre la question et la révélation
  if (black) {
    ctx.fillStyle = 'rgba(0,0,0,.35)'; ctx.fillRect(0, 0, W, H);
  }
  letterbox(t);
  vignette(.62);
  // grain
  ctx.save();
  ctx.globalAlpha = .055; ctx.globalCompositeOperation = 'overlay';
  const gi = Math.floor(t * FPS);
  ctx.fillStyle = ctx.createPattern(GRAIN[gi % GRAIN.length], 'repeat');
  ctx.translate(-rnd(gi) * 256, -rnd(gi + 1) * 256);
  ctx.fillRect(0, 0, W + 256, H + 256);
  ctx.restore();
  // ouverture / fermeture au noir
  const fade = Math.max(1 - prog(t, 0, .4), prog(t, T.fade, DUR - .3));
  if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
}

window.T = T;
window.MUSIC = MUSIC;
boot(renderFrame, DUR);
