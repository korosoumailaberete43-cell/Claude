import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : « 80 % » tombe à l'écran.
lancer('episodes/h16_80pourcent/voix.json', () => styleChoc({
  segs: ['hook', 'suspense', 'detail', 'verite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'IL PREND LE DESSIN',
  impact: beg('hook'), choc: '80 %', sousChoc: 'DE TON TEMPS. POUR RIEN.', tailleChoc: 220,
  lignes: [
    { seg: 'detail', mot: 'dessin', t: 'DU DESSIN', c: COL.rouge },
    { seg: 'detail', mot: 'calcul', t: 'PAS DU CALCUL', c: COL.chaux },
    { seg: 'verite', mot: 'métier', t: 'LE CALCUL : TON MÉTIER', c: COL.chaux },
    { seg: 'verite', mot: 'main-d', t: 'LE DESSIN : DE LA MAIN-D’ŒUVRE', c: COL.cuivreC },
  ],
  lignesY: 340,
}));
