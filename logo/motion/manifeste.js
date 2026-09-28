// CivRebar AI — « Manifeste » : typographie cinétique sur fond Blanc chaux, calée sur 120 bpm.
// 1080x1920, 30 s. Chaque mot tombe sur un temps ; la tour se construit étage par étage.
const DUR = 30;
const CX = W / 2;
const BG = COL.chaux, INK = COL.nuit;
const CU_TXT = '#9A5526', SI_TXT = '#0B7480'; // cuivre et signal lisibles sur fond clair (charte)
const B = n => 1.0 + n * .5; // temps n (120 bpm)

const T = {
  wipe: .25, pairs: [[B(0), B(1)], [B(2), B(3)], [B(4), B(5)]], mille: B(6), fois: B(7),
  rien: 6.0, tout: 8.0, calcule: 8.5, tower: 10.0, ouvrage: 12.5,
  maint: 14.2, intel: 15.0, net: 16.0, verbs: [16.5, 17.5, 18.5], sans: 20.0, signe: 20.9,
  logo: 22.0, clang: 23.5, letters: 24.0, rule: 24.5, ai: 24.8, tagline: 25.3, bientot: 26.8, fade: 29.2,
};
const chords = [];
for (let a = 1.0, i = 0; a < 22 - .01; a += 2, i++) chords.push([['Dm', 'Bb', 'F', 'C'][i % 4], a, Math.min(a + 2, 22)]);
const MUSIC = {
  chords, bass: [[1.0, 6.0], [8.0, 14.0], [16.0, 20.0]], arp: [[16.0, 20.0]],
  kick: [[1.0, 6.0, .4], [8.0, 14.0, .42], [16.0, 20.0, .42]],
  clap: [[2.0, 6.0, .3], [8.0, 14.0, .3], [16.0, 20.0, .3]], hat: [[1.0, 6.0, .12], [8.0, 14.0, .12], [16.0, 20.0, .12]],
  final: T.logo,
};

// ------------------------------------------------------------ repères sonores
cue(T.wipe, 'whoosh', 1);
T.pairs.forEach(([a, b]) => { cue(a, 'pop', .8); cue(b, 'slam', .9); shakeAt(b, 8); });
cue(T.mille, 'slam', 1); shakeAt(T.mille, 10); cue(T.fois, 'slam', 1.1); shakeAt(T.fois, 12);
for (let i = 0; i < 30; i++) cue(T.mille + .1 + i * .06, 'tick', .25);
cue(T.rien, 'impact', .7); cue(T.rien + .1, 'chime', .4);
cue(T.tout, 'whoosh', .5); cue(T.calcule, 'slam', 1.1); shakeAt(T.calcule, 12);
for (let i = 0; i < 5; i++) { cue(T.tower + i * .5, 'slam', .6); shakeAt(T.tower + i * .5 + .15, 6); }
cue(T.ouvrage, 'chime', .5);
cue(T.maint - .2, 'whoosh', .7); cue(T.intel, 'slam', 1); cue(T.intel, 'glitch', .4); shakeAt(T.intel, 10);
T.verbs.forEach(v => { cue(v, 'slam', .75); shakeAt(v, 6); });
cue(T.sans, 'impact', .6); cue(T.sans + .1, 'chime', .5);
cue(T.logo - .6, 'suck', .8); cue(T.logo, 'boom', 1.2); shakeAt(T.logo, 14);
cue(T.logo + .05, 'draw', .8);
cue(T.clang, 'clang', 1); shakeAt(T.clang, 8);
for (let i = 0; i < 8; i++) cue(T.letters + i * .06, 'tick', .5);
cue(T.rule, 'tick', .8); cue(T.ai, 'pop', 1);
cue(T.tagline, 'chime', .7); cue(T.bientot, 'blip', .8);

// ------------------------------------------------------------ outils de scène
function inkText(s, x, y, f, color, alpha = 1, align = 'center') {
  if (alpha <= 0) return;
  ctx.save(); ctx.globalAlpha = alpha; setFont(f); ctx.textAlign = align; ctx.fillStyle = color; ctx.fillText(s, x, y); ctx.restore();
}
// Fond inversé (Nuit) pour les respirations
function invert(t, a, b) { return t >= a && t < b; }
function paperGrid(alpha) {
  ctx.save(); ctx.strokeStyle = rgba(INK, .06 * alpha); ctx.lineWidth = 1;
  for (let x = 0; x <= W; x += 54) { ctx.beginPath(); ctx.moveTo(x + .5, 0); ctx.lineTo(x + .5, H); ctx.stroke(); }
  for (let y = 0; y <= H; y += 54) { ctx.beginPath(); ctx.moveTo(0, y + .5); ctx.lineTo(W, y + .5); ctx.stroke(); }
  ctx.restore();
}

// ------------------------------------------------------------ scènes
function sceneWipe(t) {
  // une barre cuivre tranche l'écran en diagonale et ouvre le papier
  const k = eio3(prog(t, T.wipe, T.wipe + .6));
  if (t >= T.wipe + .6) return;
  ctx.save(); ctx.fillStyle = '#000'; ctx.fillRect(0, 0, W, H);
  ctx.translate(CX, H / 2); ctx.rotate(-Math.PI / 4);
  const open = k * 2400;
  ctx.fillStyle = BG; ctx.fillRect(-1600, -open / 2, 3200, open);
  ctx.fillStyle = COL.cuivre;
  const L = eo3(prog(t, T.wipe - .1, T.wipe + .25)) * 3200;
  ctx.fillRect(-1600, -open / 2 - 12, L, 24); ctx.fillRect(1600 - L, open / 2 - 12, L, 24);
  ctx.restore();
}
function scenePairs(t) {
  const words = [['UNE', 'BARRE.'], ['UN', 'CADRE.'], ['UNE', 'COTE.']];
  T.pairs.forEach(([a, b], i) => {
    if (t < a || t >= a + 1) return;
    const kb = prog(t, b, b + .3);
    // dessin associé, derrière le mot
    ctx.save(); ctx.lineCap = 'butt';
    if (i === 0) {
      ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 26;
      const L = eoX(prog(t, a, a + .35)) * 900;
      ctx.beginPath(); ctx.moveTo(CX - 450, 1180); ctx.lineTo(CX - 450 + L, 1180); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(CX - 450, 1180 - 13); ctx.lineTo(CX - 450, 1180 - 13 - 90 * eo3(prog(t, a + .3, a + .5))); ctx.stroke();
    } else if (i === 1) {
      ctx.strokeStyle = INK; ctx.lineWidth = 14; ctx.lineJoin = 'round';
      drawPolyPartial([[CX - 260, 1060], [CX + 260, 1060], [CX + 260, 1360], [CX - 260, 1360], [CX - 260, 1060], [CX - 200, 1000]], 520 * 2 + 300 * 2 + 85, eo3(prog(t, a, a + .5)));
    } else {
      ctx.strokeStyle = INK; ctx.lineWidth = 4;
      const L = eoX(prog(t, a, a + .4));
      ctx.beginPath(); ctx.moveTo(CX - 420 * L, 1200); ctx.lineTo(CX + 420 * L, 1200); ctx.stroke();
      [-1, 1].forEach(s => { const x = CX + s * 420 * L; ctx.beginPath(); ctx.moveTo(x - 16, 1216); ctx.lineTo(x + 16, 1184); ctx.moveTo(x, 1150); ctx.lineTo(x, 1250); ctx.stroke(); });
      inkText('5,40 m', CX, 1275, F('500 # Mono', 44, 2), SI_TXT, prog(t, a + .3, a + .5));
    }
    ctx.restore();
    const ka = prog(t, a, a + .2);
    ctx.save(); ctx.globalAlpha = ka; setFont(F('300 # Sora', 96, 6)); ctx.textAlign = 'center'; ctx.fillStyle = INK;
    ctx.fillText(words[i][0], CX, 700 + (1 - eoX(ka)) * 40); ctx.restore();
    slam(t, words[i][1], CX, 920, F('700 # Sora', 210, -6), b, i === 0 ? COL.cuivre : INK);
  });
}
function sceneMille(t) {
  if (t < T.mille || t >= T.rien) return;
  // mille petits cadres qui remplissent l'écran
  const n = Math.floor(1000 * eo3(prog(t, T.mille, T.mille + 1.8)));
  const cols = 25, cw = W / cols, rh = 48;
  ctx.save(); ctx.strokeStyle = rgba(INK, .22); ctx.lineWidth = 2;
  for (let i = 0; i < n; i++) {
    const c = i % cols, r = Math.floor(i / cols), x = c * cw + cw * .22, y = r * rh + 4;
    ctx.strokeRect(x, y, cw * .56, rh * .7);
  }
  ctx.restore();
  ctx.save(); ctx.fillStyle = rgba(BG, .9); ctx.fillRect(0, 640, W, 560); ctx.restore();
  slam(t, 'MILLE', CX, 860, F('700 # Sora', 230, -6), T.mille, INK);
  slam(t, 'FOIS.', CX, 1080, F('700 # Sora', 230, -6), T.fois, COL.cuivre);
  inkText('× ' + String(Math.max(1, n)).padStart(4, '0'), CX, 1170, F('500 # Mono', 44, 4), SI_TXT);
}
function sceneRien(t) {
  if (!invert(t, T.rien, T.tout)) return;
  ctx.fillStyle = INK; ctx.fillRect(-50, -50, W + 100, H + 100);
  const f = F('italic 400 # Serif', 150, 0);
  reveal(t, 'Rien n’y est', CX, 900, f, { t0: T.rien, st: .03, dur: .6, mode: 'blur', color: COL.chaux });
  reveal(t, 'décoratif.', CX, 1050, f, { t0: T.rien + .4, st: .03, dur: .6, mode: 'blur', color: COL.cuivreC });
}
function sceneTout(t) {
  if (t < T.tout || t >= T.tower) return;
  const out = prog(t, T.tower - .3, T.tower);
  reveal(t, 'Tout y est', CX, 880, F('600 # Sora', 130, -3), { t0: T.tout, st: .03, dur: .4, mode: 'rise', color: INK, alpha: 1 - out });
  slam(t, 'calculé.', CX, 1060, F('700 # Sora', 190, -6), T.calcule, COL.cuivre, 'center', 1 - out);
  ctx.save(); ctx.globalAlpha = 1 - out; ctx.fillStyle = COL.cuivre;
  ctx.fillRect(CX - 300, 1120, 600 * eo3(prog(t, T.calcule + .2, T.calcule + .6)), 8); ctx.restore();
}
const FLOORS = ['SEMELLES', 'POTEAUX', 'POUTRES', 'DALLES', 'ESCALIERS'];
function sceneTower(t) {
  if (t < T.tower || t >= T.maint + .8) return;
  const z = 1 - .55 * eio3(prog(t, T.maint - .2, T.maint + .6));
  const a = 1 - prog(t, T.maint + .2, T.maint + .7);
  ctx.save(); ctx.globalAlpha = a;
  ctx.translate(CX, 1500); ctx.scale(z, z); ctx.translate(-CX, -1500);
  FLOORS.forEach((s, i) => {
    const t0 = T.tower + i * .5;
    const k = prog(t, t0 - .2, t0);
    if (k <= 0) return;
    const y = 1450 - i * 170, drop = (1 - eoBack(k)) * -600;
    // poteaux cuivre entre les dalles
    if (i > 0) {
      ctx.fillStyle = COL.cuivre;
      [-300, -100, 100, 300].forEach(dx => ctx.fillRect(CX + dx - 6, y + drop + 20, 12, 30));
    }
    ctx.fillStyle = INK; ctx.fillRect(CX - 360, y + drop - 130, 720, 150);
    setFont(F('600 # Sora', 60, 10)); ctx.textAlign = 'center'; ctx.fillStyle = COL.chaux;
    ctx.fillText(s, CX + 5, y + drop - 33);
    setFont(F('500 # Mono', 20, 3)); ctx.textAlign = 'left'; ctx.fillStyle = COL.cuivreC;
    ctx.fillText('N' + String(i).padStart(2, '0'), CX - 340, y + drop - 100);
  });
  ctx.restore();
  reveal(t, 'Tout l’ouvrage.', CX, 470, F('600 # Sora', 96, -2), { t0: T.ouvrage, st: .03, dur: .4, mode: 'rise', color: INK, alpha: a });
}
function sceneIntel(t) {
  if (t < T.maint || t >= T.sans) return;
  // réseau Signal
  if (t >= T.net) {
    ctx.save();
    for (let i = 0; i < 60; i++) {
      const x = 54 * (1 + Math.floor(rnd(i * 3.1) * 19)), y = 54 * (4 + Math.floor(rnd(i * 7.7) * 28));
      const k = eoBack(prog(t, T.net + rnd(i) * 1.5, T.net + rnd(i) * 1.5 + .3));
      if (k <= 0) continue;
      const j = (i * 7 + 3) % 60, x2 = 54 * (1 + Math.floor(rnd(j * 3.1) * 19)), y2 = 54 * (4 + Math.floor(rnd(j * 7.7) * 28));
      const kl = eo3(prog(t, T.net + .3 + rnd(i) * 1.5, T.net + 1 + rnd(i) * 1.5));
      ctx.strokeStyle = rgba(SI_TXT, .35); ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x, y + (y2 - y) * kl); ctx.lineTo(x + (x2 - x) * clamp(kl * 2 - 1), y + (y2 - y) * kl); ctx.stroke();
      ctx.fillStyle = i % 5 ? SI_TXT : COL.signal;
      ctx.beginPath(); ctx.arc(x, y, 7 * k, 0, 7); ctx.fill();
    }
    ctx.restore();
  }
  const out = prog(t, T.net + .2, T.net + .45);
  reveal(t, 'Et maintenant,', CX, 860, F('300 # Sora', 100, -1), { t0: T.maint, st: .03, dur: .4, mode: 'rise', color: INK, alpha: 1 - out });
  slam(t, 'l’intelligence.', CX, 1010, F('700 # Sora', 136, -4), T.intel, SI_TXT, 'center', 1 - out);
  const verbs = ['vérifie.', 'quantifie.', 'assiste.'];
  T.verbs.forEach((v, i) => {
    if (t < v || t >= (T.verbs[i + 1] || T.sans)) return;
    ctx.save(); ctx.fillStyle = BG; ctx.fillRect(0, 780, W, 330); ctx.restore();
    inkText('qui', CX, 870, F('300 # Sora', 90, 0), INK, prog(t, v, v + .15));
    slam(t, verbs[i], CX, 1040, F('700 # Sora', 170, -5), v, i === 2 ? COL.cuivre : INK);
  });
}
function sceneSans(t) {
  if (!invert(t, T.sans, T.logo)) return;
  ctx.fillStyle = INK; ctx.fillRect(-50, -50, W + 100, H + 100);
  const f = F('italic 400 # Serif', 100, 0);
  reveal(t, 'sans jamais remplacer', CX, 880, f, { t0: T.sans + .1, st: .025, dur: .6, mode: 'blur', color: COL.chaux });
  reveal(t, 'celui qui signe le plan.', CX, 1010, f, { t0: T.signe, st: .025, dur: .6, mode: 'blur', color: COL.cuivreC });
}
function sceneLogo(t) {
  if (t < T.logo - .05) return;
  const cx = CX, cy = 860, S = 1.66;
  const tr = symInLockupV(cx, cy, S);
  const [nx, ny] = symPt(tr, NODE.x, NODE.y);
  FX_BLEND = 'source-over';
  ring(t, T.logo, nx, ny, 1400, 1.2, COL.cuivre, 8);
  ring(t, T.logo + .1, nx, ny, 900, 1.3, SI_TXT, 3);
  sparks(t, T.clang, 60, ...symPt(tr, 210, 220), 77, [COL.cuivre, CU_TXT, INK], .7);
  FX_BLEND = 'lighter';
  const pb = eio3(prog(t, T.logo + .1, T.logo + 1.3));
  const pr = eoX(prog(t, T.clang - .3, T.clang));
  drawSymbol(tr, { bar: pb, rel: pr, node: eoBack(prog(t, T.logo, T.logo + .35)), barColor: INK });
  const letters = VG.map((_, i) => prog(t, T.letters + i * .06, T.letters + i * .06 + .5));
  drawWordmarkV(t, cx, cy, S, { letters, rule: prog(t, T.rule, T.rule + .35), ai: prog(t, T.ai, T.ai + .2), word: INK });
  reveal(t, 'L’intelligence de l’armature.', CX, 1300, F('italic 400 # Serif', 62, .5), { t0: T.tagline, st: .03, dur: .6, mode: 'blur', color: rgba(INK, .75) });
  const kb = prog(t, T.bientot, T.bientot + .4);
  inkText('BIENTÔT DANS AUTOCAD', CX + 6, 1420, F('500 # Mono', 30, 12), CU_TXT, kb);
  ctx.save(); ctx.globalAlpha = kb; ctx.fillStyle = COL.cuivre; ctx.fillRect(CX - 40, 1450, 80, 3); ctx.restore();
}

// ------------------------------------------------------------ rendu
function renderFrame(t) {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over'; ctx.filter = 'none';
  ctx.fillStyle = BG; ctx.fillRect(0, 0, W, H);
  const [sx, sy] = shake(t);
  ctx.save(); ctx.translate(sx, sy);
  paperGrid(1);
  scenePairs(t); sceneMille(t); sceneRien(t); sceneTout(t); sceneTower(t); sceneIntel(t); sceneSans(t); sceneLogo(t);
  ctx.restore();
  // éclair d'inversion sur les changements de fond
  const fl = Math.max(.6 * decay(t, T.rien, 12), .6 * decay(t, T.tout, 12), .6 * decay(t, T.sans, 12), .5 * decay(t, T.logo, 8));
  if (fl > .01) { ctx.fillStyle = `rgba(255,255,255,${fl})`; ctx.fillRect(0, 0, W, H); }
  sceneWipe(t);
  vignette(.18);
  ctx.save();
  ctx.globalAlpha = .06; ctx.globalCompositeOperation = 'multiply';
  const gi = Math.floor(t * FPS);
  ctx.fillStyle = ctx.createPattern(GRAIN[gi % GRAIN.length], 'repeat');
  ctx.translate(-rnd(gi) * 256, -rnd(gi + 1) * 256);
  ctx.fillRect(0, 0, W + 256, H + 256);
  ctx.restore();
  const fade = prog(t, T.fade, DUR - .2);
  if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
}

window.T = T;
window.MUSIC = MUSIC;
boot(renderFrame, DUR);
