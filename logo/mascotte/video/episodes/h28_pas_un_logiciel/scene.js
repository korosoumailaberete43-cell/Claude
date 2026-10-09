import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleProvoc } from '../styles.js';

// Hook : on aurait pu faire un logiciel. On a fait l'inverse.
lancer('episodes/h28_pas_un_logiciel/voix.json', () => styleProvoc({
  segs: ['hook', 'suspense', 'pourquoi', 'choix', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'TU NE QUITTES PAS TON DESSIN',
  bandeau: 'PAS UN LOGICIEL', sousBandeau: 'DE PLUS.', tailleBandeau: 86,
  finBandeau: ['pourquoi', 'Parce'],
  mots: [
    { seg: 'pourquoi', mot: 'licence', texte: 'UNE LICENCE DE PLUS', barre: true, taille: 58 },
    { seg: 'pourquoi', mot: 'apprentissage', texte: 'UN APPRENTISSAGE DE PLUS', barre: true, taille: 58 },
    { seg: 'pourquoi', mot: 'format', texte: 'UN FORMAT DE PLUS', barre: true, taille: 58 },
    { seg: 'choix', mot: 'AutoCAD', texte: 'DANS AUTOCAD.', c: COL.signal, taille: 76 },
    { seg: 'choix', mot: 'ouvert', texte: 'CELUI QUE TU AS DÉJÀ OUVERT.', c: COL.cuivreC, taille: 44 },
  ],
  motsY: 330,
}));
