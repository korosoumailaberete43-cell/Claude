import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : un seul trait oublié… et la facture qui suit.
lancer('episodes/h02_millions/voix.json', () => styleChoc({
  segs: ['hook', 'suspense', 'histoire', 'verite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LA RÈGLE, SUR CHAQUE BARRE',
  impact: wt('hook', 'trait'),
  choc: 'UN TRAIT', sousChoc: 'OUBLIÉ SUR LE PLAN.', tailleChoc: 160,
  lignes: [
    { seg: 'histoire', mot: 'enrobage', t: 'ENROBAGE TROP FAIBLE', c: COL.rouge },
    { seg: 'histoire', mot: 'espacé', t: 'CADRE MAL ESPACÉ', c: COL.rouge },
    { seg: 'histoire', mot: 'écran', t: 'INVISIBLE À L’ÉCRAN', c: COL.beton },
    { seg: 'histoire', mot: 'chantier', t: 'VISIBLE SUR LE CHANTIER', c: COL.chaux },
  ],
  lignesY: 320, lignesJusqu: ['verite', 'Et'],
  choc2: { seg: 'verite', mot: 'millions', texte: 'DES MILLIONS.', sous: 'PLUS DES HEURES…', taille: 136 },
}));
