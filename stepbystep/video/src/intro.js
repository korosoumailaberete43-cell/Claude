// ---------------------------------------------------------------------------------------------
// INTRO — « on commence à monter ».
// Fil doré → 5 marches (de bas en haut) → coche verte → la toque se pose → le nom → slogan
// (ou titre du cours) → transition escalier vers la vidéo.
// ---------------------------------------------------------------------------------------------
const T = {                    // horloge (secondes)
  grid: 0.05, fil1: 0.30, fil2: 0.95, step0: 0.90, stepGap: 0.16,
  ring: 2.02, tick: 2.30, cap: 2.46, capLand: 2.98,
  word: 3.12, academy: 3.52, extras: 3.85, shine: 4.10,
};
const TITRE = CFG.mode === 'titre';
const WIPE = CFG.duree - 1.05;       // début de la transition de sortie

const bd = makeBackdrop(svg, 11, 80);
const cam = el('g', {}, svg);
const S0 = .70;                      // échelle du logo (repère 1280 → écran)
const logoWrap = el('g', {}, cam);
const lg = makeLogo(logoWrap, 'i');

// slogan
const slogan = TITRE ? [] : [
  maskLine(root, 'left:0;width:1920px;top:872px;text-align:center;font:500 46px/1.25 Quicksand;color:#F3EEE3;letter-spacing:.5px',
    'La progression, <span style="color:' + C.or_ + '">étape par étape.</span>'),
];
const sloganLine = TITRE ? document.createElement('div') : div(`left:${960 - 170}px;top:950px;height:3px;width:340px;background:linear-gradient(90deg,transparent,${C.or_},transparent);transform-origin:50% 50%`, root);

// bloc titre (version « titre du cours »), mise en page reprise de la miniature officielle
let kicker, titres = [], lecon, lecBar;
if (TITRE) {
  const n = CFG.titre.length, fs = CFG.titre.some(l => l.length > 12) ? 118 : 138;
  const blockH = 58 + n * fs * 1.08 + 70 + 60, y0 = Math.round(505 - blockH / 2);
  kicker = maskLine(root, `left:132px;top:${y0}px;font:700 27px Comfortaa;letter-spacing:9px;text-transform:uppercase;color:${C.or_}`, CFG.kicker);
  CFG.titre.forEach((l, i) => titres.push(maskLine(root,
    `left:124px;top:${y0 + 58 + i * fs * 1.08}px;font:600 ${fs}px/1.12 Quicksand;color:#FAF7F0;white-space:nowrap;padding-bottom:12px`, l)));
  const ty = y0 + 58 + n * fs * 1.08 + 48;
  lecBar = div(`left:132px;top:${ty + 8}px;width:6px;height:46px;background:${C.or_};transform-origin:50% 100%`, root);
  lecon = maskLine(root, `left:160px;top:${ty}px;font:700 40px/1.5 Nunito;color:#E6DFD1`, CFG.lecon);
}
const topL = el('svg', { width: W, height: H, viewBox: `0 0 ${W} ${H}` }, root);   // calque au-dessus des textes
const vign = makeVignette(topL);
const wipe = makeStairWipe(topL);
// fondu final vers le noir (coupe franche possible sur la vidéo qui suit)
const black = el('rect', { width: W, height: H, fill: '#0B0B0B', opacity: 0 }, topL);

function renderAt(t) {
  // --- caméra : léger travelling arrière + respiration
  const pull = E.outCubic(P(t, 0, 4.4));
  let sc = mix(1.16, 1.0, pull) * (1 + .012 * P(t, 4.4, 3));
  let cx = 0, cy = mix(40, 0, pull);
  // version titre : le symbole glisse à droite, le nom s'efface
  const mv = TITRE ? E.inOutExpo(P(t, 4.05, 1.0)) : 0;
  const S = S0 * mix(1, 1.04, mv);
  const LX = mix(960 - 616 * S0, 1452 - 616 * S, mv);
  const LY = mix(92 - 93 * S0, 520 - 441 * S, mv);
  set(logoWrap, { transform: `translate(${LX} ${LY}) scale(${S})` });
  set(cam, { transform: `translate(960 520) scale(${sc}) translate(-960 -520) translate(${cx} ${cy})` });

  bd.update(t, { reveal: P(t, T.grid, 1.8), grid: 1 - .45 * P(t, 3, 2), dust: P(t, 0, 1.5), glow: E.outCubic(P(t, 2.3, 1.2)), gx: LX + 700 * S, gy: LY + 520 * S, cam: { x: LX * .05, y: cy } });

  // --- fil
  lg.fil(E.inOutCubic(P(t, T.fil1, .78)), E.outCubic(P(t, T.fil2, .6)));
  // --- marches : de la plus basse (4) à la plus haute (0)
  for (let k = 0; k < 5; k++) {
    const i = 4 - k, t0 = T.step0 + k * T.stepGap;
    lg.step(i, P(t, t0, .55), P(t, t0 + .28 + (4 - k) * .02, .75));
  }
  // --- coche
  lg.coche(P(t, T.ring, .36), t - T.tick, P(t, T.tick, .7));
  // --- toque
  lg.toque(P(t, T.cap, T.capLand - T.cap), t - T.capLand);
  // --- nom
  const order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];      // Step · Step · By
  const seq = [0, 1, 2, 3, 8, 9, 4, 5, 6, 7];        // on lit : Step · By · Step
  seq.forEach((li, k) => lg.letter(li, P(t, T.word + k * .035, .55)));
  for (let i = 0; i < 7; i++) lg.academy(i, P(t, T.academy + Math.abs(i - 3) * .03, .7));
  lg.extras(P(t, T.extras, .55));
  lg.shine(P(t, T.shine, 1.0));
  if (TITRE) lg.textAlpha(1 - E.outCubic(P(t, 4.0, .45)));

  // --- slogan / titre
  if (!TITRE) {
    slogan[0].reveal(P(t, 4.2, .8), P(t, WIPE - .1, .35));
    const u = E.outExpo(P(t, 4.45, .9)) * (1 - E.inExpo(P(t, WIPE - .1, .35)));
    sloganLine.style.transform = `scaleX(${u})`; sloganLine.style.opacity = u;
  } else {
    const out = P(t, WIPE - .12, .35);
    kicker.reveal(P(t, 4.45, .8), out);
    titres.forEach((l, i) => l.reveal(P(t, 4.6 + i * .12, .9), out));
    const b = E.outExpo(P(t, 5.0, .7)) * (1 - E.inExpo(out));
    lecBar.style.transform = `scaleY(${b})`;
    lecon.reveal(P(t, 5.05, .8), out);
  }

  // --- sortie
  const wp = P(t, WIPE, .85);
  wipe.update(wp);
  const gone = wp >= .5;
  cam.style.visibility = gone ? 'hidden' : 'visible';
  root.querySelectorAll('.mask').forEach(m => { if (gone) m.style.visibility = 'hidden'; });
  sloganLine.style.visibility = gone ? 'hidden' : 'visible';
  if (lecBar) lecBar.style.visibility = gone ? 'hidden' : 'visible';
  bd.g.style.opacity = gone ? 0 : 1;
  set(black, { opacity: t < .02 ? 1 : 0 });
}
window.renderAt = renderAt;
window.DUREE = CFG.duree;
renderAt(0);
