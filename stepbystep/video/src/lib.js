// ---------------------------------------------------------------------------------------------
// Boîte à outils commune : courbes d'animation, SVG, décor (plan d'architecte + poussière d'or),
// logo animable, textes révélés par masque et transition « escalier ».
// ---------------------------------------------------------------------------------------------
const W = 1920, H = 1080, NS = 'http://www.w3.org/2000/svg';
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const P = (t, a, d) => clamp((t - a) / d);              // progression 0→1 entre a et a+d
const mix = (a, b, x) => a + (b - a) * x;
const E = {
  lin: x => x,
  inQuad: x => x * x,
  inCubic: x => x * x * x,
  outCubic: x => 1 - Math.pow(1 - x, 3),
  outQuart: x => 1 - Math.pow(1 - x, 4),
  outQuint: x => 1 - Math.pow(1 - x, 5),
  outExpo: x => (x >= 1 ? 1 : 1 - Math.pow(2, -10 * x)),
  inExpo: x => (x <= 0 ? 0 : Math.pow(2, 10 * x - 10)),
  inOutCubic: x => (x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
  inOutQuart: x => (x < .5 ? 8 * x ** 4 : 1 - Math.pow(-2 * x + 2, 4) / 2),
  inOutExpo: x => (x <= 0 ? 0 : x >= 1 ? 1 : x < .5 ? Math.pow(2, 20 * x - 10) / 2 : (2 - Math.pow(2, -20 * x + 10)) / 2),
  inOutSine: x => -(Math.cos(Math.PI * x) - 1) / 2,
  outBack: (x, s = 1.70158) => 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2),
};
// ressort amorti : s = secondes écoulées depuis le départ
const spring = (s, zeta = .42, f = 2.4) => {
  if (s <= 0) return 0;
  const w = 2 * Math.PI * f, wd = w * Math.sqrt(1 - zeta * zeta);
  return 1 - Math.exp(-zeta * w * s) * (Math.cos(wd * s) + (zeta * w / wd) * Math.sin(wd * s));
};
function rng(seed) {
  return () => {
    seed = seed + 0x6D2B79F5 | 0;
    let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

function el(tag, attrs = {}, parent = null, html = null) {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (html != null) e.innerHTML = html;
  if (parent) parent.appendChild(e);
  return e;
}
function div(css, parent, html = '') {
  const d = document.createElement('div');
  d.className = 'abs';
  d.style.cssText = css;
  d.innerHTML = html;
  parent.appendChild(d);
  return d;
}
const set = (e, attrs) => { for (const k in attrs) e.setAttribute(k, attrs[k]); };
const root = document.getElementById('root');

// ------------------------------------------------------------------------------------ scène SVG
const svg = el('svg', { width: W, height: H, viewBox: `0 0 ${W} ${H}` }, root);
const defs = el('defs', {}, svg, `
  <radialGradient id="spot" cx="50%" cy="46%" r="65%">
    <stop offset="0" stop-color="#26221A"/><stop offset=".45" stop-color="#17150F"/><stop offset="1" stop-color="#0B0B0B"/>
  </radialGradient>
  <radialGradient id="vign" cx="50%" cy="50%" r="75%">
    <stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".78"/>
  </radialGradient>
  <radialGradient id="dust"><stop offset="0" stop-color="#FFE9A0" stop-opacity="1"/>
    <stop offset=".35" stop-color="${C.or_}" stop-opacity=".55"/><stop offset="1" stop-color="${C.or_}" stop-opacity="0"/></radialGradient>
  <radialGradient id="spark"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".25" stop-color="#FFF1B8"/>
    <stop offset=".6" stop-color="${C.or_}" stop-opacity=".45"/><stop offset="1" stop-color="${C.or_}" stop-opacity="0"/></radialGradient>
  <radialGradient id="gspark"><stop offset="0" stop-color="#EFFFE0"/><stop offset=".3" stop-color="#9BE06A"/>
    <stop offset="1" stop-color="${C.vert}" stop-opacity="0"/></radialGradient>
  <radialGradient id="grid-reveal" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#fff"/><stop offset=".7" stop-color="#fff" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <pattern id="grid-s" width="48" height="48" patternUnits="userSpaceOnUse">
    <path d="M48 0H0V48" fill="none" stroke="${C.or_}" stroke-width="1" opacity=".55"/></pattern>
  <pattern id="grid-l" width="240" height="240" patternUnits="userSpaceOnUse">
    <path d="M240 0H0V240" fill="none" stroke="${C.or_}" stroke-width="1.6"/>
    <path d="M0 0l10 0M0 0l0 10" stroke="${C.or_}" stroke-width="3"/></pattern>
  <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFF8DC" stop-opacity="0"/>
    <stop offset=".5" stop-color="#FFF8DC" stop-opacity=".95"/><stop offset="1" stop-color="#FFF8DC" stop-opacity="0"/></linearGradient>
  <radialGradient id="halo"><stop offset="0" stop-color="${C.or_}" stop-opacity=".5"/><stop offset=".4" stop-color="${C.or_}" stop-opacity=".18"/>
    <stop offset="1" stop-color="${C.or_}" stop-opacity="0"/></radialGradient>
  <filter id="bloom" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="14" result="b"/>
    <feColorMatrix in="b" type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 .55 0" result="g"/>
    <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="160%">
    <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity=".6"/></filter>
`);

// ------------------------------------------------------------------------------------ décor
function makeBackdrop(parent, seed = 7, n = 70) {
  const g = el('g', {}, parent);
  el('rect', { width: W, height: H, fill: 'url(#spot)' }, g);
  const glow = el('ellipse', { cx: W / 2, cy: H * .44, rx: 900, ry: 620, fill: 'url(#halo)', opacity: 0 }, g);
  // plan d'architecte (clin d'œil aux formations AutoCAD / Revit)
  const mask = el('mask', { id: 'm-grid' + seed }, defs);
  const mc = el('circle', { cx: W / 2, cy: H / 2, r: 0, fill: 'url(#grid-reveal)' }, mask);
  const grid = el('g', { mask: `url(#m-grid${seed})` }, g);
  const gs = el('rect', { x: -480, y: -480, width: W + 960, height: H + 960, fill: 'url(#grid-s)', opacity: .05 }, grid);
  const gl = el('rect', { x: -480, y: -480, width: W + 960, height: H + 960, fill: 'url(#grid-l)', opacity: .07 }, grid);
  // poussière d'or
  const r = rng(seed), motes = [];
  const mg = el('g', {}, g);
  for (let i = 0; i < n; i++) {
    const depth = r();
    motes.push({
      x: r() * W, y: r() * H, z: depth, sp: 8 + 26 * depth, ph: r() * 6.28, tw: .6 + r() * 1.6,
      e: el('circle', { r: 2 + depth * 7, fill: 'url(#dust)' }, mg),
    });
  }
  return {
    g, gridGroup: grid,
    update(t, o = {}) {
      const reveal = o.reveal ?? 1, gridA = o.grid ?? 1, dust = o.dust ?? 1, cam = o.cam ?? { x: 0, y: 0 };
      set(mc, { r: 1500 * E.outCubic(reveal) });
      set(grid, { transform: `translate(${(-cam.x * .35 - t * 6) % 240} ${(-cam.y * .35 - t * 3) % 240})`, opacity: gridA });
      set(glow, { opacity: (o.glow ?? 0) * .28, cx: o.gx ?? W / 2, cy: o.gy ?? H * .44 });
      for (const m of motes) {
        const y = ((m.y - t * m.sp - cam.y * m.z * .6) % (H + 80) + H + 80) % (H + 80) - 40;
        const x = m.x + Math.sin(t * .5 + m.ph) * 24 * m.z - cam.x * m.z * .6;
        const a = (.25 + .75 * (.5 + .5 * Math.sin(t * m.tw * 2 + m.ph))) * (.25 + .6 * m.z) * dust;
        set(m.e, { cx: x, cy: y, opacity: a });
      }
    },
  };
}
function makeVignette(parent) { return el('rect', { width: W, height: H, fill: 'url(#vign)', 'pointer-events': 'none' }, parent); }

// ------------------------------------------------------------------------------------ logo animable
// Toutes les coordonnées sont celles du logo d'origine (repère 1280 px).
function makeLogo(parent, id = 'lg') {
  const g = el('g', {}, parent);
  const glowG = el('g', { filter: 'url(#bloom)' }, g);

  // fil doré, tracé progressivement
  el('linearGradient', { id: id + 'fg', gradientUnits: 'userSpaceOnUse', x1: 0, y1: 400, x2: 0, y2: 790 }, defs,
    `<stop offset="0" stop-color="${C.or_}"/><stop offset=".55" stop-color="${C.or_}" stop-opacity=".55"/><stop offset="1" stop-color="${C.or_}" stop-opacity="0"/>`);
  const fil1 = el('path', { d: 'M503 192.5 H1010 A70 70 0 0 1 1080 262.5 V420', fill: 'none', stroke: C.or_, 'stroke-width': 13, pathLength: 1, 'stroke-dasharray': '1 1' }, glowG);
  const fil2 = el('path', { d: 'M1080 419 V790', fill: 'none', stroke: `url(#${id}fg)`, 'stroke-width': 13, pathLength: 1, 'stroke-dasharray': '1 1' }, glowG);
  const filEnd = el('path', { d: 'M1071 770 H1087 A8 8 0 0 1 1071 770 Z', fill: '#fff', opacity: 0 }, g);
  const spark = el('circle', { r: 46, fill: 'url(#spark)', opacity: 0 }, g);

  // marches
  const steps = LOGO.marches.map(([x, y]) => {
    const w = LOGO.marcheDroite - x;
    const sg = el('g', {}, glowG);
    const r = el('rect', { x, y, width: w, height: LOGO.marcheH, fill: C.or_ }, sg);
    const cp = el('clipPath', { id: `${id}c${x}` }, defs);
    el('rect', { x, y, width: w, height: LOGO.marcheH }, cp);
    const sheenG = el('g', { 'clip-path': `url(#${id}c${x})` }, sg);
    const sheen = el('rect', { x: 0, y: y - 10, width: 180, height: LOGO.marcheH + 20, fill: 'url(#sheen)', opacity: 0 }, sheenG);
    return { x, y, w, g: sg, r, sheen };
  });

  // coche
  const cocheG = el('g', {}, g);
  const burst = el('circle', { cx: 889.5, cy: 277.5, r: 45, fill: 'none', stroke: C.vert, 'stroke-width': 6, opacity: 0 }, cocheG);
  const gsp = el('circle', { cx: 889.5, cy: 277.5, r: 120, fill: 'url(#gspark)', opacity: 0 }, cocheG);
  const ring = el('circle', { cx: 889.5, cy: 277.5, r: 45, fill: 'none', stroke: C.vert, 'stroke-width': 9.5, pathLength: 1, 'stroke-dasharray': '1 1', transform: 'rotate(-90 889.5 277.5)' }, cocheG);
  const tickG = el('g', {}, cocheG);
  el('path', { d: 'M851 284 Q855 276 863 277 L876.5 293 Q902 256 940 233 Q906 266 882 307 Q877 314 870 309 Z', fill: C.vert }, tickG);
  const rays = [];
  for (let i = 0; i < 10; i++) {
    const a = i / 10 * Math.PI * 2 + .3;
    rays.push({ a, e: el('line', { stroke: i % 2 ? C.or_ : C.vert, 'stroke-width': 5, 'stroke-linecap': 'round', opacity: 0 }, cocheG) });
  }

  // toque (mortier)
  const toqueG = el('g', {}, g, LOGO.toque);
  // éclats à l'atterrissage de la toque
  const dustR = rng(99), puffs = [];
  for (let i = 0; i < 16; i++) puffs.push({ a: Math.PI + dustR() * Math.PI * 1.0 - .1, v: 90 + dustR() * 160, s: 3 + dustR() * 6,
    e: el('circle', { r: 5, fill: 'url(#spark)', opacity: 0 }, g) });

  // lettres
  const letters = LOGO.letters.map(p => {
    const lg = el('g', {}, g, p);
    lg.firstChild.setAttribute('fill', '#FFFFFF');
    const bb = { cx: 0, cy: 0 };
    return { g: lg, bb };
  });
  const tildes = LOGO.tildes.map(p => { const e = el('g', {}, g, p); const path = e.firstChild; set(path, { pathLength: 1, 'stroke-dasharray': '1 1' }); return path; });
  const livre = el('g', {}, g, LOGO.livre.join(''));

  // reflet lumineux qui balaie le logo
  const shineMask = el('mask', { id: id + 'sm' }, defs);
  el('linearGradient', { id: id + 'sg', x1: 0, y1: 0, x2: 1, y2: 0 }, defs,
    '<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>');
  const shineBand = el('rect', { x: -400, y: -200, width: 260, height: 1700, fill: `url(#${id}sg)`, transform: 'rotate(18)' }, shineMask);
  const shine = el('g', { mask: `url(#${id}sm)`, opacity: 0 }, g);
  LOGO.marches.forEach(([x, y]) => el('rect', { x, y, width: LOGO.marcheDroite - x, height: LOGO.marcheH, fill: '#FFF9E3' }, shine));
  el('path', { d: 'M503 192.5 H1010 A70 70 0 0 1 1080 262.5 V420', fill: 'none', stroke: '#FFF9E3', 'stroke-width': 13 }, shine);

  requestAnimationFrame(() => {});
  letters.forEach(l => { const b = l.g.getBBox(); l.bb = { cx: b.x + b.width / 2, cy: b.y + b.height / 2, y1: b.y + b.height }; });
  // ligne de base commune par mot (bas du S / du B), pour que p et y ne « tombent » pas
  letters.forEach((l, i) => { l.bb.base = letters[i < 4 ? 0 : i < 8 ? 4 : i < 10 ? 8 : i].bb.y1; });

  return {
    g, steps, letters,
    // chaque paramètre est une progression 0→1 (ou un temps local en s pour les ressorts)
    fil(p1, p2) {
      set(fil1, { 'stroke-dashoffset': 1 - p1 }); set(fil2, { 'stroke-dashoffset': 1 - p2 });
      set(filEnd, { opacity: clamp((p2 - .9) * 10) });
      // étincelle en tête de tracé
      const drawing = p1 > 0 && p2 < 1;
      if (drawing) {
        const pt = p1 < 1 ? fil1.getPointAtLength(fil1.getTotalLength() * p1) : { x: 1080, y: 419 + 371 * p2 };
        set(spark, { cx: pt.x, cy: pt.y, opacity: p1 < 1 ? 1 : 1 - p2 });
      } else set(spark, { opacity: 0 });
    },
    step(i, p, sheenP = 0) {           // i = 0 (haute) … 4 (basse)
      const s = steps[i], e = E.outExpo(p);
      const w = s.w * e;
      set(s.r, { x: LOGO.marcheDroite - w, width: Math.max(0, w), opacity: clamp(p * 8) });
      set(s.g, { transform: `translate(0 ${(1 - E.outCubic(clamp(p * 1.4))) * -26})` });
      set(s.sheen, { x: mix(s.x - 260, LOGO.marcheDroite + 80, E.inOutSine(sheenP)), opacity: sheenP > 0 && sheenP < 1 ? .75 : 0 });
    },
    coche(ringP, tickS, burstP) {       // tickS : secondes depuis l'apparition de la coche
      set(ring, { 'stroke-dashoffset': 1 - E.inOutCubic(ringP), opacity: ringP > 0 ? 1 : 0 });
      const k = tickS > 0 ? spring(tickS, .35, 2.6) : 0;
      set(tickG, { transform: `translate(889.5 277.5) scale(${k}) translate(-889.5 -277.5)`, opacity: tickS > 0 ? 1 : 0 });
      const b = E.outCubic(burstP);
      set(burst, { r: 45 + 110 * b, opacity: burstP > 0 && burstP < 1 ? (1 - b) * .9 : 0, 'stroke-width': 8 * (1 - b) + 1 });
      set(gsp, { opacity: burstP > 0 ? Math.sin(Math.PI * clamp(burstP * 1.2)) * .8 : 0 });
      rays.forEach(({ a, e }) => {
        const r0 = 60 + 70 * b, r1 = r0 + 34 * (1 - b);
        set(e, { x1: 889.5 + Math.cos(a) * r0, y1: 277.5 + Math.sin(a) * r0, x2: 889.5 + Math.cos(a) * r1, y2: 277.5 + Math.sin(a) * r1,
          opacity: burstP > 0 && burstP < 1 ? 1 - b : 0 });
      });
    },
    toque(fallP, landS) {               // chute (0→1) puis ressort d'atterrissage
      const f = E.inCubic(fallP);
      const y = (1 - f) * -760, rot = (1 - E.outCubic(fallP)) * -38, x = (1 - f) * -60;
      let sq = 1;
      if (landS > 0) sq = 1 - .09 * Math.exp(-landS * 7) * Math.cos(landS * 24);
      set(toqueG, { transform: `translate(${x} ${y}) rotate(${rot} 360 300) translate(360 390) scale(${2 - sq} ${sq}) translate(-360 -390)`,
        opacity: fallP > 0 ? clamp(fallP * 4) : 0 });
      puffs.forEach(p => {
        const u = clamp(landS / .7);
        const d = E.outCubic(u) * p.v;
        set(p.e, { cx: 380 + Math.cos(p.a) * d * 1.6, cy: 392 + Math.sin(p.a) * d * .55, r: p.s * (1 - u * .6),
          opacity: landS > 0 && u < 1 ? (1 - u) : 0 });
      });
    },
    letter(i, p) {
      const l = letters[i], e = E.outBack(p, 1.3);
      const sc = mix(.4, 1, E.outCubic(p));
      set(l.g, { transform: `translate(${l.bb.cx} ${l.bb.base + (1 - e) * 70}) scale(${sc}) translate(${-l.bb.cx} ${-l.bb.base})`, opacity: clamp(p * 2.5) });
    },
    academy(i, p) {                      // i = 0..6 : lettres d'ACADEMY qui s'écartent
      const l = letters[10 + i], e = E.outExpo(p);
      const dx = (l.bb.cx - 638) * (1 - e) * -.55;
      set(l.g, { transform: `translate(${dx} 0)`, opacity: clamp(p * 2) });
    },
    extras(p) {
      tildes.forEach(t => set(t, { 'stroke-dashoffset': 1 - E.inOutCubic(p) }));
      const e = E.outBack(clamp(p * 1.3), 2);
      set(livre, { transform: `translate(638 1136) scale(${e}) translate(-638 -1136)`, opacity: clamp(p * 3) });
    },
    shine(p) {
      set(shine, { opacity: p > 0 && p < 1 ? 1 : 0 });
      set(shineBand, { x: mix(-200, 1500, E.inOutSine(p)) });
    },
    textAlpha(a) { letters.forEach(l => l.g.style.opacity = a); tildes.forEach(t => t.style.opacity = a); livre.style.opacity = a; },
  };
}

// ------------------------------------------------------------------------------------ textes HTML
// Ligne de texte révélée par un masque (le texte monte de sous une ligne invisible).
function maskLine(parent, css, html) {
  const m = div(css, parent);
  m.classList.add('mask');
  m.innerHTML = `<span>${html}</span>`;
  return {
    m, s: m.firstChild,
    reveal(p, out = 0) {
      const y = (1 - E.outExpo(p)) * 110 - E.inExpo(out) * 110;
      this.s.style.transform = `translateY(${y}%)`;
      this.m.style.visibility = p > 0 && out < 1 ? 'visible' : 'hidden';
    },
  };
}

// ------------------------------------------------------------------------------------ transition « escalier »
// Cinq bandes or traversent l'écran de droite à gauche, l'une après l'autre, de bas en haut
// (on gravit les marches). À p = 0,5 l'écran est entièrement couvert : on change de scène.
function makeStairWipe(parent) {
  const g = el('g', {}, parent), bars = [], h = H / 5, S = .035, D = 1 - 4 * S;
  for (let i = 0; i < 5; i++) {
    const y = H - (i + 1) * h;
    bars.push({
      r: el('rect', { y: y - 1, height: h + 2, fill: i % 2 ? '#EDBD12' : C.or_ }, g),
      l: el('rect', { y: y + h - 5, height: 5, fill: '#000', opacity: .18 }, g),
    });
  }
  return {
    update(p) {
      bars.forEach((b, i) => {
        const u = clamp((p - i * S) / D);
        const a = E.inOutQuart(clamp(u / .4)), d = E.inOutQuart(clamp((u - .6) / .4));
        const x = W * (1 - a), w = Math.max(0, W * (a - d));
        set(b.r, { x, width: w }); set(b.l, { x, width: w });
      });
    },
  };
}
