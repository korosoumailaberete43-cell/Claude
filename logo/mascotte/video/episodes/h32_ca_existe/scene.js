import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleMessage } from '../styles2.js';

// Hook : « ça existe déjà » — la réponse de Tonton.
lancer('episodes/h32_ca_existe/voix.json', () => styleMessage({
  segs: ['hook', 'suspense', 'realite', 'notre', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'UN OUTIL DE CHEZ NOUS',
  titre: 'ON ME DIT SOUVENT ÇA.', tailleTitre: 64, de: 'Un commentaire',
  bulle: { seg: 'hook', mot: 'existe', texte: 'Ça existe déjà, votre truc.' },
  reponse: { seg: 'suspense', mot: 'ici', texte: 'Oui. Mais pas ici.' },
  bulleY: 290,
  puces: [
    { seg: 'realite', mot: 'chers', texte: 'CHERS ET LOURDS', y: 700, c: COL.rouge },
    { seg: 'realite', mot: 'habitudes', texte: 'PENSÉS POUR D’AUTRES HABITUDES', y: 770, c: COL.rouge },
    { seg: 'notre', mot: 'conventions', texte: 'NOS SECTIONS, NOS CONVENTIONS', y: 700, c: COL.signal },
  ],
}));
