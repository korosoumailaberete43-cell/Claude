import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : on cherche dix personnes. Appel à candidatures.
lancer('episodes/h30_testeurs/voix.json', () => styleChoc({
  segs: ['hook', 'qui', 'quoi', 'gain', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'ÉCRIS « TESTEUR »',
  impact: beg('hook'), choc: '10', sousChoc: 'PERSONNES. PAS UNE DE PLUS.', tailleChoc: 260,
  lignes: [
    { seg: 'qui', mot: 'spectateurs', t: 'PAS DES SPECTATEURS', c: COL.rouge },
    { seg: 'qui', mot: 'dessinent', t: 'DES GENS QUI DESSINENT', c: COL.chaux },
    { seg: 'quoi', mot: 'franchement', t: 'TU NOUS DIS CE QUI NE VA PAS', c: COL.chaux },
    { seg: 'gain', mot: 'influence', t: 'ACCÈS + INFLUENCE SUR L’OUTIL', c: COL.signal },
  ],
  lignesY: 330,
}));
