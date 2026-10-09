import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : « 1 cm », le centimètre qui décide de tout.
lancer('episodes/h19_uncm/voix.json', () => styleChoc({
  segs: ['hook', 'suspense', 'quoi', 'effet', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'L’ENROBAGE SUR CHAQUE BARRE',
  impact: beg('hook'), choc: '1 cm', sousChoc: 'C’EST TOUT CE QUI SÉPARE…', tailleChoc: 230,
  lignes: [
    { seg: 'quoi', mot: 'enrobage', t: '1 cm D’ENROBAGE EN MOINS', c: COL.cuivreC },
    { seg: 'effet', mot: 'rouille', t: 'L’ACIER ROUILLE', c: COL.rouge },
    { seg: 'effet', mot: 'gonfle', t: 'IL GONFLE', c: COL.rouge },
    { seg: 'effet', mot: 'éclate', t: 'LE BÉTON ÉCLATE', c: COL.rouge },
  ],
  lignesY: 330,
  choc2: { seg: 'effet', mot: 'ans', texte: 'DIX ANS PLUS TARD.', sous: '', taille: 92, c: COL.chaux },
}));
