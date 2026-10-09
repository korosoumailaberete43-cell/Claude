import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleMessage } from '../styles2.js';

// Hook : un message reçu d'un ingénieur, et la réponse de Tonton.
lancer('episodes/h17_message/voix.json', () => styleMessage({
  segs: ['hook', 'message', 'pourquoi', 'verite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'TU CHANGES LES VALEURS, LE PLAN SUIT',
  titre: 'UN INGÉNIEUR M’A ÉCRIT ÇA.', tailleTitre: 62, de: 'Un ingénieur',
  bulle: { seg: 'message', mot: 'refait', texte: 'J’ai refait le même plan trois fois en une semaine.' },
  reponse: { seg: 'verite', mot: 'chaque', texte: 'Et à chaque fois, tout est à reprendre.' },
  bulleY: 290,
  puces: [
    { seg: 'pourquoi', mot: 'section', texte: 'LA SECTION A CHANGÉ', y: 690, c: COL.rouge },
    { seg: 'pourquoi', mot: 'charge', texte: 'PUIS LA PORTÉE, PUIS LA CHARGE', y: 760, c: COL.rouge },
  ],
}));
