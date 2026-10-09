import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';
import { dessinPoutreCadres } from '../styles2.js';

// Hook : des cadres tous les 40 cm — deux problèmes d'un coup.
lancer('episodes/h23_cadres/voix.json', () => styleLoupe({
  segs: ['hook', 'suspense', 'un', 'deux', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'ESPACEMENT CALCULÉ ZONE PAR ZONE',
  loupe: {
    seg: 'un', mot: 'fissure', tZoom: ['suspense', 'problème'], cible: [300, 460], depart: [880, 330],
    kicker: 'CADRES TOUS LES 40 cm',
    dessin: (t, a) => dessinPoutreCadres({ pas: 150, serreAppuis: t > wt('civrebar', 'calcule') })(t, a),
    puces: [
      { seg: 'un', mot: 'rencontre', texte: 'LA FISSURE PASSE ENTRE DEUX CADRES', x: W / 2, y: 700, c: COL.rouge },
      { seg: 'deux', mot: 'appuis', texte: 'ET L’EFFORT EST MAXIMAL AUX APPUIS', x: W / 2, y: 700, c: COL.rouge },
    ],
  },
}));
