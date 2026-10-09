import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleListe } from '../styles2.js';

// Hook : trois erreurs qui reviennent sur presque tous les plans.
lancer('episodes/h18_3erreurs/voix.json', () => styleListe({
  segs: ['hook', 'une', 'deux', 'trois', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LES VOIR AVANT LE CHANTIER',
  titre: '3 ERREURS', sousTitre: 'SUR 9 PLANS SUR 10', tailleTitre: 128,
  y0: 330, pas: 118,
  items: [
    { seg: 'une', mot: 'cadres', n: '1', texte: 'CADRES ESPACÉS PAREIL', sous: 'du début à la fin de la poutre' },
    { seg: 'deux', mot: 'chapeaux', n: '2', texte: 'CHAPEAUX OUBLIÉS', sous: 'au-dessus d’un appui' },
    { seg: 'trois', mot: 'ancrage', n: '3', texte: 'BARRE SANS ANCRAGE', sous: 'elle s’arrête net' },
  ],
}));
