import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe, puce } from '../styles.js';

import { beam } from '../../moteur.js';

// Hook : « voilà ce que ça fait en 8 secondes » — la poutre se dessine sous tes yeux.
lancer('episodes/h13_huitsecondes/voix.json', () => styleLoupe({
  segs: ['hook', 'attente', 'demo', 'precision', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'TOUT EST COTÉ, PRÊT À IMPRIMER',
  loupe: {
    sans: true, cible: [0, 0], seg: 'demo', mot: 'barres', kicker: 'CIVREBAR AI · 8 SECONDES',
    dessin: (t, a) => {
      const t0 = wt('attente', 'écran'), t1 = wt('precision', 'échelle');
      beam(t, 130, 360, W - 260, 190, clamp((t - t0) / (t1 - t0)), a);
      const ctx = g();
      // chrono de 8 secondes qui s'écoule pendant le tracé
      const s = Math.min(8, Math.max(0, (t - t0) / (t1 - t0) * 8));
      txt(s.toFixed(1).replace('.', ',') + ' s', W - 150, 318, font(700, 40, 'Mono'), COL.signal, { align: 'right', alpha: a, track: 2 });
      [['barres', 'BARRES', COL.cuivreC, 215], ['chapeaux', 'CHAPEAUX', COL.chaux, 420], ['cadres', 'CADRES', COL.chaux, 620], ['cotes', 'COTES', COL.signal, 825]]
        .forEach(([w, s2, c, x]) => {
          const k = prog(t, wt('demo', w), wt('demo', w) + 0.25);
          if (k <= 0) return;
          ctx.save(); ctx.globalAlpha = a; ctx.translate(x, 625); ctx.scale(k, k);
          txt('✓ ' + s2, 0, 0, font(700, 30), c); ctx.restore();
        });
    },
    puces: [{ seg: 'precision', mot: 'imprimer', texte: '✓ À L’ÉCHELLE, COTÉ, PRÊT À IMPRIMER', x: W / 2, y: 690, c: COL.vert }],
  },
}));
