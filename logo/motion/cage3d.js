// CivRebar AI — « Construction 3D » : une cage d'armatures de poteau s'assemble sous une caméra
// en orbite, le béton est coulé, puis le logo. 1080x1920, 30 s. Projection 3D faite main.
const DUR = 30;
const CX = W / 2;

const T = {
  ground: .3, mesh: 1.0, bars: 3.0, stirrups: [6.0, 11.6], labels: 12.3, pour: [15.2, 18.4], push: 18.7,
  logo: 20.0, clang: 21.5, letters: 21.9, rule: 22.4, ai: 22.7, tagline: 23.3, sub: 25.0, bientot: 26.5, fade: 28.8,
};
const MUSIC = {
  chords: [['Dm', .3, 4.3], ['Bb', 4.3, 8.3], ['F', 8.3, 12.3], ['C', 12.3, 16.3], ['Dm', 16.3, T.logo]],
  bass: [[6.0, T.logo]], arp: [[6.0, 15.0]], kick: [[8.3, 15.0, .3]], hat: [[8.3, 15.0, .1]],
  riser: [16.0, T.logo], final: T.logo,
};

// ------------------------------------------------------------ géométrie (unités ≈ px, y vers le haut)
const MESH = [];
for (let i = 0; i < 6; i++) { const c = -120 + i * 48; MESH.push([[-135, -62, c], [135, -62, c]], [[c, -56, -135], [c, -56, 135]]); }
const BARS = [[-45, -45], [45, -45], [45, 45], [-45, 45]].map(([x, z]) => {
  const hx = Math.sign(x) * 70, hz = Math.sign(z) * 70;
  return [[x + hx, -62, z + hz], [x, -62, z], [x, 660, z]];
});
const STIRY = [];
{ let y = 25; while (y <= 600) { STIRY.push(y); y += (y < 150 || y > 470) ? 25 : 50; } }
const stirDt = (T.stirrups[1] - T.stirrups[0]) / STIRY.length;

// ------------------------------------------------------------ repères sonores
cue(T.ground, 'swell', .5);
MESH.forEach((_, i) => cue(T.mesh + i * .16, 'tick', .45));
BARS.forEach((_, i) => { cue(T.bars + i * .45, 'draw', .45); cue(T.bars + i * .45 + .7, 'clang', .35); });
STIRY.forEach((_, i) => cue(T.stirrups[0] + i * stirDt + .3, 'tick', .6));
cue(T.labels, 'blip', .6); cue(T.labels + .6, 'blip', .6); cue(T.labels + 1.2, 'blip', .6);
cue(T.pour[0], 'whoosh', .8); cue(T.pour[0] + .2, 'draw', .6);
cue(T.push, 'whoosh', 1);
cue(T.logo, 'boom', 1.4); shakeAt(T.logo, 20);
cue(T.logo + .05, 'draw', .9);
cue(T.clang, 'clang', 1.1); shakeAt(T.clang, 8);
for (let i = 0; i < 8; i++) cue(T.letters + i * .06, 'tick', .5);
cue(T.rule, 'tick', .8); cue(T.ai, 'glitch', .7); cue(T.ai, 'slam', .6);
cue(T.tagline, 'chime', .7); cue(T.sub, 'chime', .4); cue(T.bientot, 'glitch', .45); cue(T.bientot, 'blip', .7);
[.6, 6.2, 12.2, 15.2].forEach(a => cue(a, 'pop', .6));

// ------------------------------------------------------------ caméra
function camera(t) {
  const push = eio3(prog(t, T.push, T.logo));
  return {
    th: .55 + .2 * t + .8 * push, ph: lerp(.42, .9, push), ty: lerp(lerp(230, 300, prog(t, 0, 15)), 640, push),
    zoom: lerp(1.0, 4, ei3(push)) * lerp(1.6, 1.38, eio3(prog(t, 0, 14))), f: 1500, D: 1500, cy: 1150,
  };
}
function P(cam, [x, y, z]) {
  y -= cam.ty;
  const c = Math.cos(cam.th), s = Math.sin(cam.th);
  const x1 = x * c + z * s, z1 = -x * s + z * c;
  const cp = Math.cos(cam.ph), sp = Math.sin(cam.ph);
  const y2 = y * cp - z1 * sp, z2 = y * sp + z1 * cp;
  const k = cam.f / (cam.D - z2) * cam.zoom;
  return [CX + x1 * k, cam.cy - y2 * k, k, z2];
}
function line3(cam, pts, color, w, alpha = 1) {
  ctx.save(); ctx.strokeStyle = color; ctx.globalAlpha = alpha; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  let q = P(cam, pts[0]);
  for (let i = 1; i < pts.length; i++) {
    const r = P(cam, pts[i]);
    ctx.lineWidth = w * (q[2] + r[2]) / 2;
    ctx.beginPath(); ctx.moveTo(q[0], q[1]); ctx.lineTo(r[0], r[1]); ctx.stroke();
    q = r;
  }
  ctx.restore();
}
const lerp3 = (a, b, k) => [lerp(a[0], b[0], k), lerp(a[1], b[1], k), lerp(a[2], b[2], k)];
function partial(pts, k) {
  // polyligne 3D tronquée à la fraction k de sa longueur
  const seg = [];
  let L = 0;
  for (let i = 1; i < pts.length; i++) { const d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1], pts[i][2] - pts[i - 1][2]); seg.push(d); L += d; }
  let rem = L * k;
  const out = [pts[0]];
  for (let i = 1; i < pts.length && rem > 0; i++) {
    const u = Math.min(1, rem / seg[i - 1]);
    out.push(lerp3(pts[i - 1], pts[i], u)); rem -= seg[i - 1];
  }
  return out;
}
// Boîte de béton translucide (faces triées de la plus lointaine à la plus proche)
function box(cam, x0, x1, y0, y1, z0, z1, alpha) {
  if (y1 <= y0 || alpha <= 0) return;
  const v = [[x0, y0, z0], [x1, y0, z0], [x1, y0, z1], [x0, y0, z1], [x0, y1, z0], [x1, y1, z0], [x1, y1, z1], [x0, y1, z1]];
  const faces = [[0, 1, 5, 4, .9], [1, 2, 6, 5, .75], [2, 3, 7, 6, .9], [3, 0, 4, 7, .75], [4, 5, 6, 7, 1.15]];
  const pv = v.map(p => P(cam, p));
  faces.map(f => ({ f, d: (pv[f[0]][3] + pv[f[1]][3] + pv[f[2]][3] + pv[f[3]][3]) / 4 }))
    .sort((a, b) => a.d - b.d)
    .forEach(({ f }) => {
      const sh = f[4];
      ctx.save(); ctx.globalAlpha = alpha;
      ctx.fillStyle = `rgb(${Math.round(185 * sh * .55)},${Math.round(190 * sh * .55)},${Math.round(196 * sh * .58)})`;
      ctx.strokeStyle = rgba(COL.beton, .5); ctx.lineWidth = 1.2;
      ctx.beginPath(); f.slice(0, 4).forEach((i, j) => (j ? ctx.lineTo : ctx.moveTo).call(ctx, pv[i][0], pv[i][1])); ctx.closePath();
      ctx.fill(); ctx.stroke();
      ctx.restore();
    });
}

// ------------------------------------------------------------ scène 3D
function sceneCage(t) {
  if (t >= T.logo + .05) return;
  const cam = camera(t);
  // sol quadrillé
  const ga = prog(t, T.ground, T.ground + 1.2);
  ctx.save();
  for (let i = -10; i <= 10; i++) {
    const c = i * 60, a = ga * .35 * (1 - Math.abs(i) / 11);
    line3(cam, [[-600, -80, c], [600, -80, c]], rgba(COL.beton, 1), .8, a * .5);
    line3(cam, [[c, -80, -600], [c, -80, 600]], rgba(COL.beton, 1), .8, a * .5);
  }
  ctx.restore();
  // coffrage de la semelle (contour au sol)
  line3(cam, [[-150, -80, -150], [150, -80, -150], [150, -80, 150], [-150, -80, 150], [-150, -80, -150]], COL.signal, 1.6, .6 * ga);
  // nappe de la semelle
  MESH.forEach((m, i) => {
    const k = eo3(prog(t, T.mesh + i * .16, T.mesh + i * .16 + .45));
    if (k > 0) line3(cam, partial(m, k), COL.cuivre, 9);
  });
  // barres longitudinales (montent du sol)
  BARS.forEach((b, i) => {
    const k = eio3(prog(t, T.bars + i * .45, T.bars + i * .45 + .9));
    if (k <= 0) return;
    line3(cam, partial(b, k), COL.cuivre, 10);
    if (k < 1) { const tip = P(cam, partial(b, k).slice(-1)[0]); glow(tip[0], tip[1], 70, COL.cuivreC, .8); }
  });
  // cadres qui descendent un à un
  STIRY.forEach((y, i) => {
    const t0 = T.stirrups[0] + i * stirDt, k = eo3(prog(t, t0, t0 + .35));
    if (k <= 0) return;
    const yy = y + (1 - k) * 260, h = 52;
    line3(cam, [[-h, yy, -h], [h, yy, -h], [h, yy, h], [-h, yy, h], [-h, yy, -h], [-h + 18, yy, -h - 12]], COL.chaux, 4.5, clamp(k * 3) * .95);
    const fl = decay(t, t0 + .3, 10);
    if (fl > .02) { const q = P(cam, [0, y, 0]); glow(q[0], q[1], 120 * q[2], COL.signal, fl * .6); }
  });
  // béton coulé
  const lv = lerp(-80, 600, eio3(prog(t, T.pour[0], T.pour[1])));
  if (t >= T.pour[0]) {
    const a = .42 * prog(t, T.pour[0], T.pour[0] + .3);
    box(cam, -150, 150, -80, Math.min(lv, 0), -150, 150, a);
    box(cam, -60, 60, 0, Math.min(lv, 600), -60, 60, a);
  }
  // étiquettes
  const labels = [
    [[45, 540, 45], '4 HA16', COL.cuivreC, 0],
    [[52, 300, -52], 'Cadres HA8 e=15', COL.chaux, .6],
    [[150, -80, 150], 'Semelle 1,20 m', COL.beton, 1.2],
  ];
  const la = 1 - prog(t, T.pour[0] - .3, T.pour[0]);
  labels.forEach(([p, s, c, d]) => {
    const k = prog(t, T.labels + d, T.labels + d + .35);
    if (k <= 0 || la <= 0) return;
    const [x, y] = P(cam, p), side = 1;
    const lx = Math.max(x + 60, 690), ly = y - 40;
    ctx.save(); ctx.globalAlpha = k * la;
    ctx.strokeStyle = rgba(COL.beton, .8); ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(x, y, 5, 0, 7); ctx.fillStyle = c; ctx.fill();
    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(lx, ly); ctx.lineTo(lx + side * 30 * eo3(k), ly); ctx.stroke();
    setFont(F('500 # Mono', 26, 1)); ctx.textAlign = 'left'; ctx.fillStyle = c;
    ctx.fillText(s, lx + side * 40, ly + 9);
    ctx.restore();
  });
  // titres
  const f = F('600 # Sora', 96, -2);
  const titles = [[.6, 5.6, 'Barre', 'après barre.'], [6.2, 11.8, 'Cadre', 'après cadre.'], [12.2, 14.9, 'Jusqu’au', 'dernier détail.'], [15.2, 18.6, 'Puis', 'le béton.']];
  titles.forEach(([a, b, l1, l2]) => {
    if (t < a || t >= b) return;
    const out = prog(t, b - .35, b);
    ctx.save(); if (out > 0) ctx.filter = `blur(${(out * 14).toFixed(1)}px)`;
    reveal(t, l1, CX, 380, f, { t0: a, st: .03, dur: .45, mode: 'rise', color: COL.chaux, alpha: 1 - out });
    reveal(t, l2, CX, 490, f, { t0: a + .25, st: .03, dur: .45, mode: 'rise', color: COL.cuivre, alpha: 1 - out });
    ctx.restore();
  });
}
// ------------------------------------------------------------ logo
function sceneLogo(t) {
  if (t < T.logo) return;
  const cx = CX, cy = 820, S = 1.66;
  const tr = symInLockupV(cx, cy, S);
  const [nx, ny] = symPt(tr, NODE.x, NODE.y);
  const breathe = .5 + .5 * Math.sin((t - T.logo) * 2.6);
  glow(CX, cy, 800, COL.acier, .55);
  glow(nx, ny, 110 + 260 * decay(t, T.logo, 1.6) + 25 * breathe, COL.signal, .3 + .6 * decay(t, T.logo, 1.2));
  ring(t, T.logo, nx, ny, 1600, 1.3, COL.signal, 10);
  ring(t, T.logo + .12, nx, ny, 1000, 1.5, COL.cuivre, 4);
  sparks(t, T.logo, 140, nx, ny, 41, [COL.signal, COL.chaux, COL.cuivreC]);
  flare(nx, ny, decay(t, T.logo, 2.2), 1800);
  const pb = eio3(prog(t, T.logo + .1, T.logo + 1.3));
  const pr = eoX(prog(t, T.clang - .3, T.clang));
  drawSymbol(tr, { bar: pb, rel: pr, node: eoBack(prog(t, T.logo, T.logo + .35)), nodeGlow: 18 + 20 * breathe, glowBar: 4, glowRel: 20 * decay(t, T.clang, 1.2) + 3 });
  if (pb > 0 && pb < 1) { const p = EL_BAR.getPointAtLength(LEN_BAR * pb), [px, py] = symPt(tr, p.x, p.y); glow(px, py, 90, COL.chaux, .9); }
  sparks(t, T.clang, 60, ...symPt(tr, 210, 220), 77, [COL.cuivreC, COL.cuivre, COL.chaux], .8);
  const letters = VG.map((_, i) => prog(t, T.letters + i * .06, T.letters + i * .06 + .5));
  const aiG = t >= T.ai && t < T.ai + .4 ? 1 - prog(t, T.ai, T.ai + .4) : 0;
  drawWordmarkV(t, cx, cy, S, { letters, rule: prog(t, T.rule, T.rule + .35), ai: t >= T.ai ? 1 : 0, aiGlitch: aiG });
  reveal(t, 'L’intelligence de l’armature.', CX, 1240, F('italic 400 # Serif', 60, .5), { t0: T.tagline, st: .03, dur: .6, mode: 'blur', color: COL.beton });
  const fs = F('500 # Manrope', 38, .2);
  reveal(t, 'Le ferraillage assisté par IA,', CX, 1340, fs, { t0: T.sub, st: .015, dur: .5, mode: 'blur', color: COL.chaux });
  reveal(t, 'directement dans AutoCAD.', CX, 1392, fs, { t0: T.sub + .3, st: .015, dur: .5, mode: 'blur', color: COL.chaux });
  if (t >= T.bientot) {
    const fl = t < T.bientot + .5 ? (rnd(Math.floor(t * FPS)) > .45 ? 1 : .15) : 1;
    ctx.save(); ctx.globalAlpha = fl;
    setFont(F('500 # Mono', 40, 24)); ctx.textAlign = 'center'; ctx.fillStyle = COL.cuivre;
    ctx.fillText('BIENTÔT', CX + 12, 1480);
    ctx.restore();
  }
}

// ------------------------------------------------------------ rendu
function renderFrame(t) {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over'; ctx.filter = 'none';
  ctx.fillStyle = COL.nuit; ctx.fillRect(0, 0, W, H);
  glow(CX, 1000, 900, COL.acier, .5);
  const [sx, sy] = shake(t);
  ctx.save(); ctx.translate(sx, sy);
  if (t >= T.logo) grid(.3 * prog(t, T.logo, T.logo + .8));
  sceneCage(t); sceneLogo(t);
  ctx.restore();
  const fl = Math.max(.95 * decay(t, T.logo, 4.5), .9 * ei3(prog(t, T.logo - .5, T.logo)) * (t < T.logo ? 1 : 0));
  if (fl > .01) { ctx.fillStyle = `rgba(243,240,234,${fl})`; ctx.fillRect(0, 0, W, H); }
  vignette(.6);
  ctx.save();
  ctx.globalAlpha = .055; ctx.globalCompositeOperation = 'overlay';
  const gi = Math.floor(t * FPS);
  ctx.fillStyle = ctx.createPattern(GRAIN[gi % GRAIN.length], 'repeat');
  ctx.translate(-rnd(gi) * 256, -rnd(gi + 1) * 256);
  ctx.fillRect(0, 0, W + 256, H + 256);
  ctx.restore();
  const fade = Math.max(1 - prog(t, 0, .4), prog(t, T.fade, DUR - .2));
  if (fade > 0) { ctx.fillStyle = `rgba(0,0,0,${fade})`; ctx.fillRect(0, 0, W, H); }
}

window.T = T;
window.MUSIC = MUSIC;
boot(renderFrame, DUR);
