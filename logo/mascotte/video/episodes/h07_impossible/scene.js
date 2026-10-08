import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleRecit } from '../styles.js';

// Hook : « on m'a dit que c'était impossible » — le récit du projet, en bandes cinéma.
lancer('episodes/h07_impossible/voix.json', () => styleRecit({
  segs: ['hook', 'suspense', 'histoire', 'etat', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'L’INTELLIGENCE DE L’ARMATURE',
  phrases: [
    { seg: 'hook', mot: 'On', texte: ['« On m’a dit', 'que c’était', 'impossible. »'], y: 330, taille: 84 },
    { seg: 'suspense', mot: 'outil', texte: ['Un outil de ferraillage', 'fait ici. Par nous.'], y: 380, taille: 64 },
    { seg: 'histoire', mot: 'acheté', texte: ['PAS ACHETÉ.', 'PAS COPIÉ.'], y: 380, gras: true, taille: 76, c: COL.cuivreC },
    { seg: 'histoire', mot: 'ligne', texte: ['Écrit ligne par ligne,', 'pour nos chantiers.'], y: 390, taille: 60 },
  ],
  frise: { seg: 'etat', mot: 'poutre', y: 580, etapes: ['POUTRE', 'POTEAUX', 'DALLES', 'SEMELLES', 'ESCALIERS'] },
}));
