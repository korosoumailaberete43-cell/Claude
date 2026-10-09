import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleProvoc } from '../styles.js';

// Hook : qui signe ce plan ? Pas la machine.
lancer('episodes/h29_signature/voix.json', () => styleProvoc({
  segs: ['hook', 'suspense', 'verite', 'responsabilite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'TOI, TU DÉCIDES',
  bandeau: 'QUI SIGNE CE PLAN ?', tailleBandeau: 70,
  finBandeau: ['suspense', 'Pas'],
  verdict: { seg: 'suspense', mot: 'Pas', texte: 'PAS ELLE', taille: 130, y: 430, jusqu: 'verite' },
  mots: [
    { seg: 'verite', mot: 'calcule', texte: 'ELLE CALCULE', c: COL.beton, taille: 58 },
    { seg: 'verite', mot: 'vérifie', texte: 'ELLE PROPOSE, ELLE VÉRIFIE', c: COL.beton, taille: 52 },
    { seg: 'verite', mot: 'porte', texte: 'MAIS ELLE NE PORTE RIEN', c: COL.chaux, taille: 58 },
    { seg: 'responsabilite', mot: 'nom', texte: 'C’EST UN NOM EN BAS DU PLAN', c: COL.cuivreC, taille: 50 },
    { seg: 'responsabilite', mot: 'logiciel', texte: 'PAS UN LOGICIEL.', c: COL.signal, taille: 62 },
  ],
  motsY: 320,
}));
