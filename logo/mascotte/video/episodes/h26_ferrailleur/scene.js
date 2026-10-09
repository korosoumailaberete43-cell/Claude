import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleRecit } from '../styles.js';

// Hook : celui qui pose la barre ne verra jamais ta poutre.
lancer('episodes/h26_ferrailleur/voix.json', () => styleRecit({
  segs: ['hook', 'suspense', 'realite', 'conseil', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'UN PLAN, UNE LECTURE',
  phrases: [
    { seg: 'hook', mot: 'Le', texte: ['Le ferrailleur', 'ne verra jamais', 'ta poutre.'], y: 330, taille: 76 },
    { seg: 'suspense', mot: 'plan', texte: ['IL NE VERRA', 'QUE TON PLAN.'], y: 380, gras: true, taille: 72, c: COL.cuivreC },
    { seg: 'realite', mot: 'pluie', texte: ['Debout, sur le chantier,', 'parfois sous la pluie.'], y: 390, taille: 58 },
    { seg: 'conseil', mot: 'interprété', texte: ['CE QUI EST AMBIGU', 'SERA INTERPRÉTÉ.'], y: 380, gras: true, taille: 66, c: COL.signal },
  ],
}));
