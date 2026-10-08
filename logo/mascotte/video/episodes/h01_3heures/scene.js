import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : « 3 HEURES » tombe à l'écran, puis le compteur monte à 30 journées par an.
lancer('episodes/h01_3heures/voix.json', () => styleChoc({
  segs: ['hook', 'suspense', 'reveal', 'chiffre', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'BIENTÔT DANS AUTOCAD',
  impact: wt('hook', 'heures'),
  choc: '3 HEURES', sousChoc: 'HIER. SANS T’EN RENDRE COMPTE.',
  lignes: [
    { seg: 'reveal', mot: 'barres', t: 'DES BARRES', c: COL.cuivreC },
    { seg: 'reveal', mot: 'cadres', t: 'DES CADRES', c: COL.chaux },
    { seg: 'reveal', mot: 'cotes', t: 'DES COTES', c: COL.signal },
    { seg: 'reveal', mot: 'main', t: 'À LA MAIN.', c: COL.rouge },
  ],
  lignesY: 330, lignesJusqu: ['chiffre', 'Sur'],
  compteur: { seg: 'chiffre', mot: 'année', de: 1, a: 30, duree: 1.9, label: 'JOURNÉES PAR AN', sous: 'perdues à dessiner' },
}));
