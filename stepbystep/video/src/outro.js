// ---------------------------------------------------------------------------------------------
// OUTRO (20 s, calée sur l'écran de fin YouTube)
//  A  0,0 – 3,3 s  « Bravo ! » : les marches se construisent, la coche se valide, confettis
//  B  3,3 – 8,6 s  3 gestes sur 3 marches montantes (J'aime · Commentaire · Abonnement + clic)
//  C  8,6 – 20 s   écran de fin : 2 emplacements vidéo, rond « S'abonner », bandeau WhatsApp
// ---------------------------------------------------------------------------------------------
const WA = 2.90, WB = 8.20, WD = .85;         // départs des transitions escalier
const SW_A = WA + WD / 2, SW_B = WB + WD / 2;  // instants où l'écran est couvert
const END = CFG.duree;

const ICON = {
  like: '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/>',
  bubble: '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
  bell: '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
  play: '<path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/>',
  list: '<path d="M3 6h13M3 12h9M3 18h9"/><path d="M16 12.5v7l5.5-3.5z" fill="currentColor"/>',
  phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
};
const icon = (k, size, color, sw = 1.9) =>
  `<svg viewBox="0 0 24 24" width="${size}" height="${size}" fill="none" stroke="${color}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round" style="position:static;color:${color};overflow:visible">${ICON[k]}</svg>`;

// ================================================================ décor commun
const bd = makeBackdrop(svg, 23, 80);

// ================================================================ SCÈNE A — Bravo
const sceneA = el('g', {}, svg);
const SA = .66, LXA = 560 - 673 * SA, LYA = 548 - 491 * SA;
const lgA = el('g', { transform: `translate(${LXA} ${LYA}) scale(${SA})` }, sceneA);
const lg = makeLogo(lgA, 'o');
lg.textAlpha(0);
// confettis (physique simple et déterministe)
const conf = [], cr = rng(5);
const confG = el('g', {}, sceneA);
const CX = LXA + 889.5 * SA, CY = LYA + 277.5 * SA;
const palette = [C.or_, C.or_, '#FFE27A', C.ivoire, '#E9B80F', C.vert];
for (let i = 0; i < 110; i++) {
  const a = -Math.PI / 2 + (cr() - .5) * 2.3, v = 700 + cr() * 900;
  conf.push({ vx: Math.cos(a) * v * 1.25, vy: Math.sin(a) * v, rot: cr() * 360, vr: (cr() - .5) * 900, fl: 4 + cr() * 8, ph: cr() * 6,
    d: cr() * .25, w: 10 + cr() * 12, h: 6 + cr() * 7,
    e: el('rect', { width: 10, height: 6, fill: palette[i % palette.length], opacity: 0 }, confG) });
}
const A = div('left:0;top:0;width:1920px;height:1080px', root);
const aK = maskLine(A, `left:1010px;top:352px;font:700 26px Comfortaa;letter-spacing:10px;color:${C.or_}`, 'FIN DE LA LEÇON');
const aT = maskLine(A, 'left:1000px;top:392px;font:700 168px/1.1 Quicksand;color:#FAF7F0;padding-bottom:10px', `Bravo<span style="color:${C.or_}"> !</span>`);
const aS = maskLine(A, 'left:1008px;top:600px;font:600 46px/1.3 Nunito;color:#E6DFD1', 'Vous venez de franchir une étape.');
const aL = div(`left:1010px;top:690px;width:420px;height:4px;border-radius:2px;background:linear-gradient(90deg,${C.or_},transparent);transform-origin:0 50%`, A);

// ================================================================ SCÈNE B — 3 gestes
const B = div('left:0;top:0;width:1920px;height:1080px;display:none', root);
const bK = maskLine(B, `left:0;width:1920px;text-align:center;top:118px;font:700 26px Comfortaa;letter-spacing:10px;color:${C.or_}`, 'AVANT DE PARTIR');
const bT = maskLine(B, 'left:0;width:1920px;text-align:center;top:160px;font:600 70px/1.25 Quicksand;color:#FAF7F0;padding-bottom:8px',
  `Aidez-nous à grandir, <span style="color:${C.or_}">étape par étape</span>`);
const CARDS = [
  { ic: 'like', n: '01', t: 'Aimez la vidéo', s: 'si elle vous a été utile' },
  { ic: 'bubble', n: '02', t: 'Posez vos questions', s: 'en commentaire' },
  { ic: 'bell', n: '03', t: 'Abonnez-vous', s: 'et activez la cloche', hot: true },
];
const cardEls = CARDS.map((c, i) => {
  const x = 222 + i * 510, bottom = 920 - i * 70, h = 360, w = 456;
  const step = div(`left:${x - 12}px;top:${bottom + 18}px;width:${w + 24}px;height:22px;border-radius:4px;background:${C.or_};transform-origin:100% 50%;box-shadow:0 0 30px rgba(245,197,24,.35)`, B);
  const riser = div(`left:${x + w + 12 - 4}px;top:${bottom + 40}px;width:4px;height:${60 + i * 70}px;background:linear-gradient(${C.or_},transparent);transform-origin:50% 0`, B);
  const bg = c.hot ? `linear-gradient(160deg,#FFD84A,${C.or_} 55%,#E3B10C)` : 'linear-gradient(160deg,#252320,#191816)';
  const fg = c.hot ? '#111111' : '#FAF7F0', sub = c.hot ? '#3A3000' : '#BDB6A8';
  const card = div(`left:${x}px;top:${bottom - h}px;width:${w}px;height:${h}px;border-radius:30px;background:${bg};
    border:1.5px solid ${c.hot ? 'rgba(255,255,255,.35)' : 'rgba(245,197,24,.28)'};box-shadow:0 30px 60px rgba(0,0,0,.55);transform-origin:50% 100%`, B, `
    <div class="abs" style="left:34px;top:30px;font:700 24px Comfortaa;letter-spacing:4px;color:${c.hot ? '#5A4800' : C.or_}">${c.n}</div>
    <div class="abs ic" style="left:${w / 2 - 70}px;top:52px;width:140px;height:140px;border-radius:50%;
      background:${c.hot ? '#111111' : 'rgba(245,197,24,.10)'};border:3px solid ${c.hot ? '#111111' : C.or_};display:flex;align-items:center;justify-content:center">
      <div class="ico" style="display:flex">${icon(c.ic, 70, c.hot ? C.or_ : '#FAF7F0', 1.8)}</div>
      ${c.ic === 'bubble' ? `<div class="dots abs" style="left:48px;top:61px;width:44px;display:flex;justify-content:space-between">${'<i style="display:block;width:8px;height:8px;border-radius:50%;background:#FAF7F0"></i>'.repeat(3)}</div>` : ''}
    </div>
    <div class="abs" style="left:0;width:${w}px;top:222px;text-align:center;font:700 44px Quicksand;color:${fg}">${c.t}</div>
    <div class="abs" style="left:0;width:${w}px;top:282px;text-align:center;font:600 30px Nunito;color:${sub}">${c.s}</div>
    ${c.hot ? `<div class="badge abs" style="right:-22px;top:-22px;width:76px;height:76px;border-radius:50%;background:${C.vert};border:5px solid #111;display:flex;align-items:center;justify-content:center">
      <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" style="position:static"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>
      <div class="ripple abs" style="left:${w / 2 - 60}px;top:300px;width:120px;height:120px;border-radius:50%;border:4px solid #111;opacity:0"></div>` : ''}`);
  return { card, step, riser, ico: card.querySelector('.ico'), dots: [...card.querySelectorAll('.dots i')],
    badge: card.querySelector('.badge'), ripple: card.querySelector('.ripple'), x, w, bottom, h };
});
// curseur de souris
const cursor = div('left:0;top:0;width:64px;height:64px;filter:drop-shadow(0 8px 14px rgba(0,0,0,.6))', B,
  `<svg viewBox="0 0 24 24" width="64" height="64" style="position:static"><path d="M4.5 2.5l15 9.2-6.6 1.3 3.9 7.3-2.9 1.5-3.9-7.3-4.9 4.5z" fill="#fff" stroke="#111" stroke-width="1.3" stroke-linejoin="round"/></svg>`);

// ================================================================ SCÈNE C — écran de fin
const Cn = div('left:0;top:0;width:1920px;height:1080px;display:none', root);
const hz = div('left:710px;top:52px;width:500px', Cn, LOGO.horizontal.replace('<svg ', '<svg style="position:static;width:500px;height:auto" '));
const FR = [
  { x: 232, lab: 'Vidéo suivante', ic: 'play', ph: 'Votre prochaine étape' },
  { x: 1048, lab: 'Toute la formation', ic: 'list', ph: 'La formation complète' },
];
const frY = 262, frW = 640, frH = 360;
const frames = FR.map((f, i) => {
  const lab = maskLine(Cn, `left:${f.x}px;top:${frY - 56}px;font:700 24px Comfortaa;letter-spacing:6px;color:${C.or_};text-transform:uppercase`,
    `<span style="display:inline-flex;vertical-align:-5px;margin-right:12px">${icon(f.ic, 28, C.or_, 2.2)}</span>${f.lab}`);
  const box = div(`left:${f.x}px;top:${frY}px;width:${frW}px;height:${frH}px;border-radius:22px;overflow:hidden;
    background:radial-gradient(120% 120% at 30% 20%,#23211C,#141412);border:2px solid rgba(245,197,24,.45);box-shadow:0 30px 70px rgba(0,0,0,.6)`, Cn, `
    <div class="abs" style="inset:0;background:repeating-linear-gradient(0deg,transparent 0 47px,rgba(245,197,24,.05) 47px 48px),repeating-linear-gradient(90deg,transparent 0 47px,rgba(245,197,24,.05) 47px 48px)"></div>
    <div class="abs" style="left:${frW / 2 - 52}px;top:${frH / 2 - 78}px;width:104px;height:104px;border-radius:50%;border:3px solid rgba(250,247,240,.35);display:flex;align-items:center;justify-content:center">${icon(f.ic, 48, 'rgba(250,247,240,.55)', 2)}</div>
    <div class="abs" style="left:0;width:${frW}px;top:${frH / 2 + 44}px;text-align:center;font:600 28px Nunito;color:rgba(250,247,240,.45)">${f.ph}</div>
    <div class="sw abs" style="top:-20%;height:140%;width:180px;background:linear-gradient(90deg,transparent,rgba(255,240,190,.10),transparent);transform:skewX(-20deg)"></div>`);
  return { lab, box, sw: box.querySelector('.sw') };
});
// rond « S'abonner » (emplacement de l'élément Abonnement YouTube)
const subCY = 770, subR = 100;
const subRing = div(`left:${960 - subR}px;top:${subCY - subR}px;width:${subR * 2}px;height:${subR * 2}px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,#2A2823,#141412);border:4px solid ${C.or_};display:flex;align-items:center;justify-content:center;box-shadow:0 0 50px rgba(245,197,24,.25)`, Cn,
  `<div style="transform:scale(1.15)">${LOGO.horizontal ? '' : ''}${icon('bell', 74, C.or_, 1.8)}</div>`);
const pulses = [0, 1].map(() => div(`left:${960 - subR}px;top:${subCY - subR}px;width:${subR * 2}px;height:${subR * 2}px;border-radius:50%;border:3px solid ${C.or_};opacity:0`, Cn));
const subL = maskLine(Cn, `right:${1920 - 960 + subR + 44}px;top:${subCY - 44}px;text-align:right;font:700 60px Quicksand;color:#FAF7F0`, 'Abonnez-vous');
const subRt = maskLine(Cn, `left:${960 + subR + 44}px;top:${subCY - 40}px;font:600 32px/1.25 Nunito;color:#CFC8BA`, 'pour ne manquer<br>aucune étape');
// bandeau WhatsApp
const band = div(`left:360px;top:930px;width:1200px;height:92px;border-radius:46px;background:linear-gradient(90deg,#1E1D1A,#262420);
  border:2px solid rgba(245,197,24,.6);display:flex;align-items:center;gap:22px;padding:0 34px 0 14px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.5)`, Cn, `
  <div style="flex:none;width:66px;height:66px;border-radius:50%;background:${C.or_};display:flex;align-items:center;justify-content:center">${icon('phone', 34, '#111111', 2.2)}</div>
  <div style="font:600 31px Nunito;color:#FAF7F0;white-space:nowrap">Formation complète <span style="color:${C.or_}">+</span> attestation</div>
  <div style="flex:1"></div>
  <div style="font:700 25px Comfortaa;letter-spacing:3px;color:#BDB6A8">WHATSAPP</div>
  <div style="font:800 40px Nunito;color:${C.or_};white-space:nowrap">${CFG.tel}</div>
  <div class="sw abs" style="left:0;top:-20%;height:140%;width:220px;background:linear-gradient(90deg,transparent,rgba(255,240,190,.16),transparent);transform:skewX(-20deg)"></div>`);
const bandSw = band.querySelector('.sw');

// ================================================================ calque supérieur
const topL = el('svg', { width: W, height: H, viewBox: `0 0 ${W} ${H}` }, root);
makeVignette(topL);
const wipeA = makeStairWipe(topL), wipeB = makeStairWipe(topL);
const fade = el('rect', { width: W, height: H, fill: '#000', opacity: 0 }, topL);

const vis = (e, on) => { e.style.display = on ? 'block' : 'none'; };
const pop = (e, p, from = .6) => {                     // apparition avec ressort
  const k = spring(p, .45, 2.2);
  e.style.transform = `translateY(${(1 - Math.min(1, k)) * 60}px) scale(${mix(from, 1, k)})`;
  e.style.opacity = clamp(p * 5);
};

function renderAt(t) {
  const inA = t < SW_A, inB = t >= SW_A && t < SW_B, inC = t >= SW_B;
  bd.update(t, { reveal: P(t, 0, 1.4), grid: .8, dust: P(t, 0, 1), glow: inA ? .8 : inC ? .55 : .7,
    gx: inA ? 560 : 960, gy: inA ? 540 : 560, cam: { x: 0, y: 0 } });

  // ------------------------------------------------ A
  sceneA.style.visibility = inA ? 'visible' : 'hidden'; vis(A, inA);
  if (inA) {
    lg.fil(E.inOutCubic(P(t, .05, .55)), E.outCubic(P(t, .5, .5)));
    for (let k = 0; k < 5; k++) lg.step(4 - k, P(t, .12 + k * .1, .5), P(t, .5 + k * .05, .7));
    lg.coche(P(t, .62, .3), t - .86, P(t, .86, .7));
    lg.toque(0, -1);
    lg.shine(P(t, 1.4, 1.1));
    const zoom = 1 + .03 * E.outCubic(P(t, 0, 3));
    set(lgA, { transform: `translate(560 540) scale(${zoom}) translate(-560 -540) translate(${LXA} ${LYA}) scale(${SA})` });
    conf.forEach(c => {
      const s = t - .9 - c.d * .15;
      if (s <= 0) { set(c.e, { opacity: 0 }); return; }
      const drag = 1.8, ex = (1 - Math.exp(-drag * s)) / drag;
      const x = CX + c.vx * ex, y = CY + c.vy * ex + 520 * (s - ex) / drag * 1.9 + 60 * s * s;
      const flip = Math.cos(s * c.fl + c.ph);
      set(c.e, { x: -c.w / 2, y: -c.h / 2, width: c.w, height: c.h, opacity: clamp(2.6 - s),
        transform: `translate(${x + Math.sin(s * 3 + c.ph) * 18} ${y}) rotate(${c.rot + c.vr * s}) scale(1 ${flip})` });
    });
    aK.reveal(P(t, .95, .7)); aT.reveal(P(t, 1.02, .8)); aS.reveal(P(t, 1.22, .8));
    aL.style.transform = `scaleX(${E.outExpo(P(t, 1.45, 1))})`;
  }

  // ------------------------------------------------ B
  vis(B, inB);
  if (inB) {
    bK.reveal(P(t, SW_A + .05, .7)); bT.reveal(P(t, SW_A + .12, .8));
    cardEls.forEach((c, i) => {
      const t0 = SW_A + .45 + i * .42, s = t - t0;
      c.step.style.transform = `scaleX(${E.outExpo(P(t, t0 - .12, .6))})`;
      c.riser.style.transform = `scaleY(${E.outCubic(P(t, t0 + .1, .6))})`;
      pop(c.card, Math.max(0, s));
      // micro-animations des icônes
      if (i === 0) { const k = s > .25 ? Math.exp(-(s - .25) * 3.2) * Math.sin((s - .25) * 16) : 0; c.ico.style.transform = `rotate(${-18 * k}deg) scale(${1 + .12 * Math.abs(k)})`; }
      if (i === 1) c.dots.forEach((d, j) => { d.style.transform = `translateY(${-6 * Math.max(0, Math.sin((t - j * .15) * 7))}px)`; d.style.opacity = s > .3 ? 1 : 0; });
    });
    // curseur → clic sur « Abonnez-vous »
    const c3 = cardEls[2], tx = c3.x + c3.w / 2 + 10, ty = c3.bottom - 70;
    const mvp = E.inOutCubic(P(t, 5.55, 1.0));
    const cx = mix(1990, tx, mvp), cy = mix(1160, ty, mvp) - Math.sin(Math.PI * mvp) * 90;
    const click = 6.62, press = t > click && t < click + .16 ? .86 : 1;
    cursor.style.transform = `translate(${cx}px,${cy}px) scale(${press})`;
    cursor.style.opacity = t < 8.0 ? 1 : 1 - P(t, 8.0, .2);
    const cs = t - click;
    c3.card.style.transform += cs > 0 && cs < .5 ? ` scale(${1 - .04 * Math.sin(Math.PI * clamp(cs / .25))})` : '';
    c3.ripple.style.opacity = cs > 0 ? (1 - E.outCubic(clamp(cs / .6))) * .8 : 0;
    c3.ripple.style.transform = `scale(${1 + 2.2 * E.outCubic(clamp(cs / .6))})`;
    c3.badge.style.transform = `scale(${cs > .05 ? spring(cs - .05, .4, 2.6) : 0})`;
    const bs = t - (click + .05);          // la cloche sonne
    const ring = bs > 0 ? Math.exp(-bs * 2.4) * Math.sin(bs * 26) : 0;
    c3.ico.style.transform = `rotate(${24 * ring}deg)`;
    c3.ico.style.transformOrigin = '50% 12%';
  }

  // ------------------------------------------------ C
  vis(Cn, inC);
  if (inC) {
    const t0 = SW_B + .05;
    pop(hz, t - t0, .85);
    frames.forEach((f, i) => {
      f.lab.reveal(P(t, t0 + .35 + i * .12, .7));
      pop(f.box, Math.max(0, t - (t0 + .2 + i * .14)), .8);
      const sp = ((t - t0 - 1.4 - i * .5) % 3.6) / 1.1;           // reflet périodique
      f.sw.style.left = `${mix(-260, frW + 80, clamp(sp))}px`;
    });
    pop(subRing, Math.max(0, t - (t0 + .55)), .3);
    subL.reveal(P(t, t0 + .7, .8)); subRt.reveal(P(t, t0 + .8, .8));
    pulses.forEach((p, i) => {
      const u = ((t - t0 - 1.2 - i * 1) % 2) / 2;
      const on = t > t0 + 1.2 + i;
      p.style.opacity = on ? (1 - u) * .6 : 0; p.style.transform = `scale(${1 + .45 * E.outCubic(u)})`;
    });
    pop(band, Math.max(0, t - (t0 + .9)), .9);
    const bsp = ((t - t0 - 2.2) % 4) / 1.3;
    bandSw.style.left = `${mix(-300, 1250, clamp(bsp))}px`;
  }

  wipeA.update(P(t, WA, WD));
  wipeB.update(P(t, WB, WD));
  set(fade, { opacity: E.inOutSine(P(t, END - .7, .7)) });
}
window.renderAt = renderAt;
window.DUREE = END;
renderAt(0);
