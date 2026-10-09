import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleRecit } from '../styles.js';

// Hook : deux heures du matin, la même poutre pour la troisième fois.
lancer('episodes/h25_deuxheures/voix.json', () => styleRecit({
  segs: ['hook', 'scene', 'raison', 'verite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'BIENTÔT DANS AUTOCAD',
  phrases: [
    { seg: 'hook', mot: 'Il', texte: ['Il est deux heures', 'du matin.'], y: 380, taille: 78 },
    { seg: 'scene', mot: 'redessines', texte: ['Tu redessines', 'la même poutre.'], y: 370, taille: 72 },
    { seg: 'scene', mot: 'troisième', texte: ['POUR LA TROISIÈME FOIS.'], y: 430, gras: true, taille: 56, c: COL.cuivreC },
    { seg: 'raison', mot: 'cinq', texte: ['Parce que la section', 'a bougé de 5 cm.'], y: 380, taille: 64 },
    { seg: 'verite', mot: 'métier', texte: ['CE N’EST PAS ÇA,', 'TON MÉTIER.'], y: 380, gras: true, taille: 76, c: COL.signal },
  ],
}));
