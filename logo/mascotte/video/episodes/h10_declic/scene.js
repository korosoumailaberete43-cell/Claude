import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleRecit } from '../styles.js';

// Hook : « j'ai cru que j'étais lent » — la confession qui mène au déclic.
lancer('episodes/h10_declic/voix.json', () => styleRecit({
  segs: ['hook', 'suspense', 'compte', 'declic', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'BIENTÔT DANS AUTOCAD',
  phrases: [
    { seg: 'hook', mot: 'Pendant', texte: ['« Pendant des années,', 'j’ai cru que', 'j’étais lent. »'], y: 320, taille: 78 },
    { seg: 'suspense', mot: 'compté', texte: ['Jusqu’au jour', 'où j’ai compté.'], y: 380, taille: 70 },
    { seg: 'compte', mot: 'quatre-vingts', texte: ['80 % DU TEMPS', 'C’EST DU DESSIN.'], y: 370, gras: true, taille: 82, c: COL.cuivreC },
    { seg: 'compte', mot: 'calcul', texte: ['Pas du calcul.'], y: 420, taille: 64, c: COL.beton },
    { seg: 'declic', mot: 'problème', texte: ['LE PROBLÈME,', 'CE N’ÉTAIT PAS MOI.'], y: 370, gras: true, taille: 70 },
    { seg: 'declic', mot: 'outil', texte: ['C’ÉTAIT L’OUTIL.'], y: 420, gras: true, taille: 80, c: COL.signal },
  ],
}));
