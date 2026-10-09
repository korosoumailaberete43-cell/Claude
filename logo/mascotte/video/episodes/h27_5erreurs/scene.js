import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleListe } from '../styles2.js';

// Hook : le classement des cinq erreurs les plus chères.
lancer('episodes/h27_5erreurs/voix.json', () => styleListe({
  segs: ['hook', 'cinq', 'trois', 'un', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'CELLE-LÀ NE SE RÉPARE PAS',
  titre: 'LES 5 ERREURS', sousTitre: 'LES PLUS CHÈRES', tailleTitre: 104,
  y0: 320, pas: 92,
  items: [
    { seg: 'cinq', mot: 'ancrages', n: '5', texte: 'ANCRAGES ABSENTS', taille: 40 },
    { seg: 'cinq', mot: 'répartis', n: '4', texte: 'CADRES MAL RÉPARTIS', taille: 40 },
    { seg: 'trois', mot: 'chapeaux', n: '3', texte: 'CHAPEAUX OUBLIÉS', taille: 40 },
    { seg: 'trois', mot: 'enrobage', n: '2', texte: 'ENROBAGE INSUFFISANT', taille: 40 },
    { seg: 'un', mot: 'côté', n: '1', texte: 'ACIER DU MAUVAIS CÔTÉ', sous: 'console, radier, soutènement', taille: 42 },
  ],
}));
