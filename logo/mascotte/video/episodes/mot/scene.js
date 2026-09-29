// Épisode « Le mot du chantier » : le cadre.
import { lancer, W, COL, g, txt, slam, panelBox, font, prog, win, lerp, eio, eoB, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { coupe, puce, titreSerie, finCivrebar, abonne, cuesFin } from '../commun.js';

// Élévation de poutre : cadres serrés près des appuis, espacés au centre
function elevation(t, t0, a, hl) {
  const ctx = g(), x0 = 140, x1 = W - 140, y0 = 390, h = 150;
  ctx.save(); ctx.globalAlpha = a;
  ctx.fillStyle = '#5d6670'; ctx.fillRect(x0, y0, x1 - x0, h);
  ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x0, y0, x1 - x0, h);
  // appuis
  [x0 + 40, x1 - 40].forEach(x => { ctx.fillStyle = COL.beton; ctx.beginPath(); ctx.moveTo(x, y0 + h); ctx.lineTo(x - 34, y0 + h + 50); ctx.lineTo(x + 34, y0 + h + 50); ctx.closePath(); ctx.fill(); });
  // barres filantes
  ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 7;
  [y0 + 22, y0 + h - 22].forEach(y => { ctx.beginPath(); ctx.moveTo(x0 + 14, y); ctx.lineTo(x1 - 14, y); ctx.stroke(); });
  // cadres : espacement croissant vers le centre (symétrique)
  const xs = []; let d = 0, s = 22;
  while (x0 + 30 + d < (x0 + x1) / 2 - 10) { xs.push(d); d += s; s = Math.min(s * 1.28, 70); }
  const all = [...xs.map(v => x0 + 30 + v), ...xs.map(v => x1 - 30 - v)];
  all.forEach((x, i) => {
    const k = clamp((t - t0 - (i % xs.length) * 0.05) / 0.2);
    if (k <= 0) return;
    const near = Math.abs(x - x0) < 170 || Math.abs(x - x1) < 170;
    ctx.strokeStyle = near && hl > 0 ? COL.signal : COL.chaux; ctx.lineWidth = near && hl > 0 ? 4 + hl * 2 : 4;
    ctx.globalAlpha = a * k;
    ctx.beginPath(); ctx.moveTo(x, y0 + 10); ctx.lineTo(x, y0 + 10 + (h - 20) * k); ctx.stroke();
  });
  ctx.restore();
}

lancer('episodes/mot/voix.json', () => {
  const KEYS = [
    [0, 'idle', 'happy'],
    [beg('accroche') - 0.1, 'pointUp', 'happy'],
    [wt('accroche', 'cadre') - 0.2, 'cheer', 'surprised'],
    [beg('definition'), 'explain', 'proud'],
    [beg('role'), 'count', 'happy'],
    [wt('role', 'effort'), 'finger', 'serious'],
    [beg('astuce'), 'think', 'think'],
    [wt('astuce', 'serre'), 'explain', 'proud'],
    [beg('civrebar') - 0.1, 'cheer', 'happy'],
    [wt('civrebar', 'espacements'), 'pointUp', 'proud'],
    [beg('fin'), 'wave', 'happy'],
  ];
  const CAMS = [
    [0, { az: 0, dist: 6.4, ty: 2.3, tx: 0 }],
    [beg('accroche'), { az: -0.1, dist: 5.8, ty: 2.35, tx: 0 }],
    [beg('definition'), { az: 0.2, dist: 6.4, ty: 2.25, tx: 0 }],
    [beg('role'), { az: -0.15, dist: 6.2, ty: 2.3, tx: 0 }],
    [beg('astuce'), { az: 0.1, dist: 6.6, ty: 2.25, tx: 0 }],
    [beg('civrebar'), { az: 0.15, dist: 6.6, ty: 2.25, tx: 0 }],
    [beg('fin'), { az: 0, dist: 6.2, ty: 2.3, tx: 0 }],
  ];
  function scenes(t, front) {
    if (front) { abonne(t, wt('fin', 'Abonne')); return; }
    titreSerie(t, beg('accroche'), beg('definition') + 0.05, 'LE MOT DU CHANTIER', '');
    slam(t, wt('accroche', 'cadre') - 0.1, 'LE CADRE', W / 2, 500, font(700, 150), COL.cuivreC, { alpha: win(t, beg('accroche'), beg('definition') + 0.05, 0.1, 0.3) });
    // définition + rôle : coupe à gauche, texte à droite
    const a = panelBox(t, beg('definition'), end('role') + 0.2);
    if (a > 0) {
      const hl = 0.5 + 0.5 * Math.sin(t * 5);
      const kh = prog(t, wt('definition', 'fermée'), wt('definition', 'fermée') + 0.3);
      coupe(150, 280, 250, 340, { cover: 30, a, hl: kh * hl });
      txt('CADRE', 275, 655, font(500, 22, 'Mono'), COL.signal, { track: 4, alpha: a * kh });
      const ad = a * (1 - prog(t, beg('role') - 0.1, beg('role') + 0.2));
      const k1 = prog(t, wt('definition', 'armature'), wt('definition', 'armature') + 0.3);
      const k2 = prog(t, wt('definition', 'entoure'), wt('definition', 'entoure') + 0.3);
      txt('ARMATURE', 460, 380, font(700, 58), COL.chaux, { align: 'left', alpha: ad * k1 });
      txt('FERMÉE', 460, 450, font(700, 58), COL.cuivreC, { align: 'left', alpha: ad * kh });
      txt('qui entoure les barres', 460, 530, font(600, 38, 'Manrope'), COL.beton, { align: 'left', alpha: ad * k2 });
      const ar = a * prog(t, beg('role') - 0.1, beg('role') + 0.2);
      [['place', '① TIENT LES BARRES', 'EN PLACE', 330], ['tranchant', '② REPREND L’EFFORT', 'TRANCHANT', 490]].forEach(([w, l1, l2, y]) => {
        const k = prog(t, wt('role', w) - 0.3, wt('role', w));
        txt(l1, 450, y + 30, font(700, 40), COL.chaux, { align: 'left', alpha: ar * k });
        txt(l2, 450 + 58, y + 80, font(700, 40), COL.cuivreC, { align: 'left', alpha: ar * k });
      });
    }
    // astuce : élévation, cadres serrés aux appuis
    const b = panelBox(t, beg('astuce'), beg('civrebar') - 0.1);
    if (b > 0) {
      txt('PRÈS DES APPUIS', 130, 300, font(500, 28, 'Mono'), COL.signal, { align: 'left', track: 6, alpha: b });
      const hl = prog(t, wt('astuce', 'serre') - 0.1, wt('astuce', 'serre') + 0.3);
      elevation(t, beg('astuce') + 0.3, b, hl);
      puce(t, wt('astuce', 'serre'), 'SERRÉ', 230, 350, COL.signal, b, 26);
      puce(t, wt('astuce', 'serre') + 0.1, 'SERRÉ', W - 230, 350, COL.signal, b, 26);
      puce(t, wt('astuce', 'serre') + 0.3, 'ESPACÉ', W / 2, 350, COL.beton, b, 26);
      const ke = prog(t, wt('astuce', 'effort'), wt('astuce', 'effort') + 0.3);
      txt('EFFORT TRANCHANT MAXIMAL AUX APPUIS', W / 2, 640, font(700, 28), COL.cuivreC, { track: 1, alpha: b * ke });
    }
    finCivrebar(t, 'civrebar', 'CADRES AUTOMATIQUES');
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg('accroche'), type: 'whoosh' }, { t: wt('accroche', 'cadre') - 0.1, type: 'slam' },
    { t: beg('definition'), type: 'whoosh' }, { t: wt('definition', 'fermée'), type: 'shine' },
    { t: wt('role', 'place') - 0.3, type: 'tick' }, { t: wt('role', 'tranchant') - 0.3, type: 'tick' },
    { t: beg('astuce'), type: 'whoosh' }, { t: beg('astuce') + 0.3, type: 'draw' }, { t: wt('astuce', 'serre'), type: 'chime' },
    { t: beg('civrebar') - 0.9, type: 'riser' },
    ...cuesFin('civrebar', 'fin'),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[beg('civrebar') - 0.1, 0.5], [wt('accroche', 'cadre') - 0.1, 0.35]] };
});
