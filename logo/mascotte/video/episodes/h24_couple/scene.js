import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : deux matériaux que tout oppose, et qui tiennent ensemble.
lancer('episodes/h24_couple/voix.json', () => styleChoc({
  segs: ['hook', 'beton', 'acier', 'magie', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'TOUT LE FERRAILLAGE REPOSE LÀ-DESSUS',
  impact: beg('hook'), choc: 'BÉTON + ACIER', sousChoc: 'ÇA N’AURAIT JAMAIS DÛ MARCHER.', tailleChoc: 96,
  lignes: [
    { seg: 'beton', mot: 'écrase', t: 'BÉTON : ÉCRASER, OUI', c: COL.chaux },
    { seg: 'beton', mot: 'tire', t: 'TIRER, NON', c: COL.rouge },
    { seg: 'acier', mot: 'tire', t: 'ACIER : TIRER, OUI', c: COL.chaux },
    { seg: 'acier', mot: 'rouille', t: 'MAIS IL FLAMBE ET IL ROUILLE', c: COL.rouge },
  ],
  lignesY: 330, lignesJusqu: ['magie', 'pourtant'],
  choc2: { seg: 'magie', mot: 'pareil', texte: 'ILS S’ALLONGENT PAREIL.', sous: 'EN CHAUFFANT…', taille: 78, c: COL.signal },
}));
