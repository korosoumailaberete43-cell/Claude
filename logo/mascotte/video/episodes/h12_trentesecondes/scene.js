import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : un compte à rebours de 30 secondes — « à la fin, tu sauras pourquoi ».
lancer('episodes/h12_trentesecondes/voix.json', () => styleChoc({
  segs: ['hook', 'constat', 'conséquence', 'reponse', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LE FERRAILLAGE, DANS AUTOCAD',
  impact: wt('hook', 'trente'),
  choc: '30 SECONDES', sousChoc: 'ET TU SAURAS POURQUOI.', tailleChoc: 132,
  lignes: [
    { seg: 'constat', mot: 'Afrique', t: 'ICI, ON CONSTRUIT VITE', c: COL.chaux },
    { seg: 'constat', mot: 'main', t: 'ET ON FERRAILLE À LA MAIN', c: COL.cuivreC },
    { seg: 'conséquence', mot: 'perdues', t: 'DES HEURES PERDUES', c: COL.rouge },
    { seg: 'conséquence', mot: 'chantier', t: 'DES ERREURS SUR LE CHANTIER', c: COL.rouge },
  ],
  lignesY: 330, lignesJusqu: ['reponse', 'Alors'],
  choc2: { seg: 'reponse', mot: 'écrit', texte: 'L’OUTIL QUI MANQUAIT', sous: 'ALORS ON A ÉCRIT…', taille: 86, c: COL.cuivreC },
}));
