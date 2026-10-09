import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';
import { dessinDalle } from '../styles2.js';
import { rebours } from '../commun.js';

// Hook : un test de 3 secondes sur le sens de portée d'une dalle.
lancer('episodes/h21_quizsens/voix.json', () => {
  const ep = styleLoupe({
    segs: ['hook', 'question', 'reponse', 'pourquoi', 'civrebar', 'fin'],
    segCiv: 'civrebar', segFin: 'fin', badge: 'TOUJOURS LA PORTÉE RÉELLE',
    loupe: {
      sans: true, cible: [0, 0], seg: 'reponse', mot: 'trois', kicker: 'DALLE 3 m × 6 m · DEUX APPUIS',
      dessin: (t, a) => dessinDalle({ appuis: true, sens: t > wt('reponse', 'trois') ? 2 : 0 })(t, a),
      puces: [{ seg: 'reponse', mot: 'trois', texte: '→ DANS LE SENS DES 3 m', x: W / 2, y: 690, c: COL.vert }],
    },
  });
  const scenesBase = ep.scenes;
  ep.scenes = (t, front) => { scenesBase(t, front); if (!front) rebours(t, end('question') + 0.1, 3, W / 2, 470, 110); };
  ep.CUES = [...ep.CUES, ...[0, 1, 2].map(i => ({ t: end('question') + 0.1 + i, type: 'tick' }))];
  return ep;
});
