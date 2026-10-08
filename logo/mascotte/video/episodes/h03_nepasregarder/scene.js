import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleProvoc } from '../styles.js';

// Hook : un bandeau rouge « NE REGARDE PAS » — l'interdit qui donne envie de rester.
lancer('episodes/h03_nepasregarder/voix.json', () => styleProvoc({
  segs: ['hook', 'suspense', 'probleme', 'reveal', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'IL TRAVAILLE PENDANT QUE TU RÉFLÉCHIS',
  bandeau: 'NE REGARDE PAS', sousBandeau: 'SI TU DESSINES ENCORE À LA MAIN',
  finBandeau: ['probleme', 'Barre'],
  mots: [
    { seg: 'probleme', mot: 'Barre', texte: 'BARRE PAR BARRE', barre: true },
    { seg: 'probleme', mot: 'Cadre', texte: 'CADRE PAR CADRE', barre: true },
    { seg: 'probleme', mot: 'Cote', texte: 'COTE PAR COTE', barre: true },
    { seg: 'probleme', mot: 'Poutre', texte: 'POUTRE APRÈS POUTRE', barre: true },
    { seg: 'reveal', mot: 'ordinateur', texte: 'ET L’ORDINATEUR ?', c: COL.signal, taille: 60 },
    { seg: 'reveal', mot: 'rien', texte: 'IL NE FAIT RIEN.', c: COL.cuivreC, taille: 60 },
  ],
  motsY: 300,
}));
