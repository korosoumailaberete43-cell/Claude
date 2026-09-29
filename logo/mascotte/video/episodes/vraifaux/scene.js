// Épisode « Vrai ou faux ? » : plus d'acier = plus solide ?
import { lancer, W, COL, g, txt, slam, panelBox, font, prog, win, lerp, eio, clamp, rgba, wt, beg, end } from '../../moteur.js';
import { rebours, puce, tampon, titreSerie, finCivrebar, abonne, cuesFin } from '../commun.js';

// Coupe surchargée : barres serrées, le béton ne passe plus
function coupeDense(x, y, w, h, a, t, t0) {
  const ctx = g();
  ctx.save(); ctx.globalAlpha = a;
  ctx.fillStyle = '#5d6670'; ctx.fillRect(x, y, w, h); ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x, y, w, h);
  ctx.strokeStyle = COL.chaux; ctx.lineWidth = 5; ctx.strokeRect(x + 24, y + 24, w - 48, h - 48);
  const r = 15, cols = 5;
  for (let row = 0; row < 3; row++) for (let i = 0; i < cols; i++) {
    const bx = x + 24 + r + 4 + i * (w - 48 - 2 * r - 8) / (cols - 1), by = y + h - 24 - r - 4 - row * (2 * r + 2);
    ctx.fillStyle = COL.cuivre; ctx.beginPath(); ctx.arc(bx, by, r, 0, 7); ctx.fill();
  }
  for (let i = 0; i < 2; i++) { const bx = x + 24 + r + 4 + i * (w - 48 - 2 * r - 8); ctx.beginPath(); ctx.arc(bx, y + 24 + r + 4, r, 0, 7); ctx.fill(); }
  // vides (nids de cailloux) sous les barres
  const k = prog(t, t0, t0 + 0.4);
  ctx.globalAlpha = a * k; ctx.fillStyle = '#1b2230';
  [[0.3, 0.52], [0.62, 0.48], [0.48, 0.6]].forEach(([u, v]) => { ctx.beginPath(); ctx.ellipse(x + w * u, y + h * v, 20, 12, 0.3, 0, 7); ctx.fill(); });
  ctx.restore();
}
// Poutre qui se fissure d'un coup
function rupture(x, y, w, h, a, t, t0) {
  const ctx = g(), k = prog(t, t0, t0 + 0.25);
  ctx.save(); ctx.globalAlpha = a;
  const sh = k > 0 && k < 1 ? Math.sin(t * 90) * 4 : 0;
  ctx.translate(sh, 0);
  ctx.fillStyle = '#5d6670'; ctx.fillRect(x, y, w, h); ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x, y, w, h);
  ctx.fillStyle = COL.beton;
  [x + 20, x + w - 20].forEach(px => { ctx.beginPath(); ctx.moveTo(px, y + h); ctx.lineTo(px - 24, y + h + 36); ctx.lineTo(px + 24, y + h + 36); ctx.closePath(); ctx.fill(); });
  if (k > 0) {
    ctx.strokeStyle = COL.rouge; ctx.lineWidth = 6; ctx.lineJoin = 'round';
    const pts = [[0.5, 0], [0.46, 0.25], [0.55, 0.45], [0.47, 0.7], [0.53, 1]];
    ctx.beginPath(); pts.slice(0, 1 + Math.ceil(k * 4)).forEach(([u, v], i) => (i ? ctx.lineTo : ctx.moveTo).call(ctx, x + w * u, y + h * v)); ctx.stroke();
  }
  ctx.restore();
}

lancer('episodes/vraifaux/voix.json', () => {
  const tAtt = end('attente'), tRep = beg('reponse');
  const KEYS = [
    [0, 'idle', 'happy'],
    [beg('accroche') - 0.1, 'pointUp', 'surprised'],
    [beg('affirmation'), 'explain', 'happy'],
    [beg('attente'), 'think', 'think'],
    [tAtt + 0.2, 'cross', 'think'],
    [tRep - 0.1, 'finger', 'angry'],
    [beg('explication'), 'explain', 'serious'],
    [wt('explication', 'Pire'), 'finger', 'angry'],
    [beg('regle'), 'count', 'proud'],
    [beg('civrebar') - 0.1, 'cheer', 'happy'],
    [wt('civrebar', 'aide'), 'pointUp', 'proud'],
    [beg('fin'), 'wave', 'happy'],
  ];
  const CAMS = [
    [0, { az: 0, dist: 6.4, ty: 2.3, tx: 0 }],
    [beg('accroche'), { az: 0.1, dist: 5.8, ty: 2.35, tx: 0 }],
    [beg('affirmation'), { az: -0.15, dist: 6.4, ty: 2.25, tx: 0 }],
    [tRep, { az: 0, dist: 5.2, ty: 2.4, tx: 0 }],
    [beg('explication'), { az: 0.2, dist: 6.4, ty: 2.25, tx: 0 }],
    [beg('regle'), { az: -0.15, dist: 6.2, ty: 2.3, tx: 0 }],
    [beg('civrebar'), { az: 0.15, dist: 6.6, ty: 2.25, tx: 0 }],
    [beg('fin'), { az: 0, dist: 6.2, ty: 2.3, tx: 0 }],
  ];
  function scenes(t, front) {
    if (front) { abonne(t, wt('fin', 'Abonne')); return; }
    titreSerie(t, beg('accroche') - 0.05, beg('affirmation') + 0.05, 'LE QUIZ DU CHANTIER', 'VRAI OU FAUX ?', COL.cuivreC, 104);
    // l'affirmation, puis le compte à rebours à droite
    const a = panelBox(t, beg('affirmation'), tRep + 0.05);
    if (a > 0) {
      const lines = ['« Plus on met', 'd’acier, plus la', 'poutre est', 'solide. »'];
      lines.forEach((l, i) => {
        const k = prog(t, beg('affirmation') + i * 0.35, beg('affirmation') + i * 0.35 + 0.3);
        txt(l, 140 + (1 - eio(k)) * 30, 360 + i * 76, font(700, 58), i === 3 ? COL.cuivreC : COL.chaux, { align: 'left', alpha: a * k });
      });
    }
    rebours(t, beg('attente') + 0.2, 3, 850, 450, 90);
    tampon(t, tRep - 0.05, 'FAUX', W / 2, 470, COL.rouge, 150, -0.12, win(t, tRep - 0.05, beg('explication') + 0.1, 0.05, 0.3));
    // explication : deux dessins côte à côte
    const b = panelBox(t, beg('explication'), end('explication') + 0.2);
    if (b > 0) {
      coupeDense(165, 280, 240, 270, b, t, wt('explication', 'passe'));
      puce(t, wt('explication', 'passe'), 'LE BÉTON PASSE MAL', 285, 615, COL.rouge, b, 24);
      const kr = prog(t, wt('explication', 'Pire') - 0.2, wt('explication', 'Pire') + 0.2);
      if (kr > 0) {
        rupture(560, 360, 380, 110, b * kr, t, wt('explication', 'casser'));
        puce(t, wt('explication', 'coup'), 'RUPTURE BRUTALE', 750, 560, COL.rouge, b, 24);
        puce(t, wt('explication', 'prévenir'), 'SANS PRÉVENIR', 750, 620, COL.rouge, b, 24);
      }
    }
    // la règle
    const c = win(t, beg('regle') - 0.05, beg('civrebar') - 0.1, 0.2, 0.3);
    if (c > 0) {
      slam(t, wt('regle', 'bonne'), 'LA BONNE QUANTITÉ', W / 2, 380, font(700, 76), COL.chaux, { alpha: c });
      slam(t, wt('regle', 'endroit') - 0.3, 'AU BON ENDROIT', W / 2, 500, font(700, 76), COL.cuivreC, { alpha: c });
      puce(t, wt('regle', 'endroit') + 0.2, '✓ BON FERRAILLAGE', W / 2, 610, COL.vert, c, 30);
    }
    finCivrebar(t, 'civrebar', 'BIENTÔT DANS AUTOCAD');
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg('accroche') + 0.1, type: 'slam' },
    { t: beg('affirmation'), type: 'whoosh' },
    ...[0, 1, 2].map(i => ({ t: beg('attente') + 0.2 + i, type: 'tick' })),
    { t: tRep - 0.05, type: 'stamp' }, { t: tRep, type: 'error' },
    { t: beg('explication'), type: 'whoosh' }, { t: wt('explication', 'passe'), type: 'pop' },
    { t: wt('explication', 'casser'), type: 'slam' }, { t: wt('explication', 'coup'), type: 'error' },
    { t: wt('regle', 'bonne'), type: 'slam' }, { t: wt('regle', 'endroit') - 0.3, type: 'slam' }, { t: wt('regle', 'endroit') + 0.2, type: 'chime' },
    { t: beg('civrebar') - 0.9, type: 'riser' },
    ...cuesFin('civrebar', 'fin'),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[beg('civrebar') - 0.1, 0.5], [tRep - 0.05, 0.3]] };
});
