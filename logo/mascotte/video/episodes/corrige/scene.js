// Épisode « Tonton corrige » : l'enrobage oublié.
import { lancer, W, COL, g, txt, slam, panelBox, font, prog, win, lerp, eio, clamp, wt, beg, end } from '../../moteur.js';
import { coupe, entoure, rebours, puce, finCivrebar, abonne, cuesFin } from '../commun.js';

lancer('episodes/corrige/voix.json', ({ DUR }) => {
  const tAtt = end('question'), tRep = beg('reponse');
  const tBon = wt('regle', 'deux') - 0.1;
  const KEYS = [
    [0, 'idle', 'happy'],
    [beg('accroche') - 0.1, 'finger', 'surprised'],
    [wt('accroche', 'Regarde'), 'point', 'serious'],
    [beg('question'), 'think', 'think'],
    [wt('question', 'laisse'), 'count', 'happy'],
    [tAtt + 0.2, 'cross', 'think'],
    [tRep - 0.1, 'point', 'angry'],
    [beg('regle'), 'explain', 'serious'],
    [tBon, 'explain', 'proud'],
    [beg('civrebar') - 0.1, 'cheer', 'happy'],
    [wt('civrebar', 'appliqué'), 'pointUp', 'proud'],
    [beg('fin'), 'wave', 'happy'],
  ];
  const CAMS = [
    [0, { az: 0, dist: 6.4, ty: 2.3, tx: 0 }],
    [beg('accroche'), { az: 0.05, dist: 5.6, ty: 2.35, tx: 0 }],
    [beg('question'), { az: 0.2, dist: 6.4, ty: 2.25, tx: 0 }],
    [tRep, { az: -0.05, dist: 5.4, ty: 2.35, tx: 0 }],
    [beg('regle'), { az: -0.2, dist: 6.4, ty: 2.25, tx: 0 }],
    [beg('civrebar'), { az: 0.15, dist: 6.6, ty: 2.25, tx: 0 }],
    [beg('fin'), { az: 0, dist: 6.2, ty: 2.3, tx: 0 }],
  ];
  function scenes(t, front) {
    if (front) { abonne(t, wt('fin', 'Abonne')); return; }
    // STOP !
    const as = win(t, beg('accroche') - 0.1, wt('accroche', 'Regarde') + 0.1, 0.1, 0.25);
    slam(t, beg('accroche'), 'STOP !', W / 2, 470, font(700, 170), COL.rouge, { alpha: as });
    // le plan à corriger
    const t0 = wt('accroche', 'Regarde') + 0.1, t1 = beg('civrebar') - 0.1;
    const a = panelBox(t, t0, t1);
    if (a > 0) {
      const bon = eio(prog(t, tBon, tBon + 0.7));
      txt(bon > 0.5 ? 'CORRIGÉ' : 'TROUVE L’ERREUR', 130, 300, font(500, 28, 'Mono'), bon > 0.5 ? COL.vert : COL.signal, { align: 'left', track: 6, alpha: a });
      txt('COUPE A-A · POUTRE 25×40', 950, 300, font(500, 22, 'Mono'), COL.beton, { align: 'right', track: 2, alpha: a });
      const cx = 410, cy = 330, cw = 260, ch = 310;
      coupe(cx, cy, cw, ch, { cover: lerp(0, 34, bon), a });
      // réponse : cercle rouge autour de la barre collée au coffrage
      const ar = a * (1 - bon);
      entoure(t, tRep + 0.15, cx + 22, cy + ch - 22, 48, 48, ar);
      puce(t, wt('reponse', 'enrobage') - 0.1, '0 cm D’ENROBAGE', 225, 440, COL.rouge, ar, 28);
      puce(t, wt('regle', 'rouille'), 'ROUILLE', 225, 520, COL.rouge, ar, 28);
      puce(t, wt('regle', 'éclate'), 'ÉCLATEMENT', 225, 600, COL.rouge, ar, 28);
      // cote d'enrobage
      if (bon > 0) {
        const ctx = g(); ctx.save(); ctx.globalAlpha = a * bon; ctx.strokeStyle = COL.signal; ctx.lineWidth = 3;
        const y = cy + ch + 0, x0 = cx + cw - 34, x1 = cx + cw;
        ctx.beginPath(); ctx.moveTo(x0, cy + ch - 60); ctx.lineTo(x0, y + 22); ctx.moveTo(x1, cy + ch - 60); ctx.lineTo(x1, y + 22); ctx.moveTo(x0 - 10, y + 14); ctx.lineTo(x1 + 10, y + 14); ctx.stroke();
        ctx.restore();
        puce(t, tBon + 0.3, '✓ 2,5 à 3 cm', 835, 440, COL.vert, a, 30);
        puce(t, wt('regle', 'exposition'), 'SELON L’EXPOSITION', 835, 530, COL.signal, a, 24);
      }
    }
    // compte à rebours pendant le silence (à droite de la coupe)
    rebours(t, tAtt + 0.15, 3, 835, 470, 95);
    finCivrebar(t, 'civrebar', 'ENROBAGE AUTOMATIQUE');
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg('accroche'), type: 'slam' }, { t: wt('accroche', 'Regarde') + 0.1, type: 'whoosh' },
    ...[0, 1, 2].map(i => ({ t: tAtt + 0.15 + i, type: 'tick' })),
    { t: tRep, type: 'error' }, { t: tRep + 0.15, type: 'draw' }, { t: wt('reponse', 'enrobage') - 0.1, type: 'pop' },
    { t: wt('regle', 'rouille'), type: 'error' }, { t: wt('regle', 'éclate'), type: 'error' },
    { t: tBon, type: 'shine' }, { t: tBon + 0.3, type: 'chime' }, { t: wt('regle', 'exposition'), type: 'blip' },
    { t: beg('civrebar') - 0.9, type: 'riser' },
    ...cuesFin('civrebar', 'fin'),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[beg('civrebar') - 0.1, 0.5]], signalVisible: t => t > beg('question') };
});
