import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleRecit } from '../styles.js';

// Hook : le premier outil de ferraillage pensé ici — fierté et feuille de route.
lancer('episodes/h14_afrique/voix.json', () => styleRecit({
  segs: ['hook', 'fierte', 'preuve', 'suite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'SOIS LÀ AU LANCEMENT',
  phrases: [
    { seg: 'hook', mot: 'premier', texte: ['LE PREMIER OUTIL', 'DE FERRAILLAGE', 'PENSÉ ICI.'], y: 320, gras: true, taille: 70, c: COL.cuivreC },
    { seg: 'fierte', mot: 'traduction', texte: ['Pas une traduction.', 'Pas une version allégée.'], y: 380, taille: 60 },
    { seg: 'fierte', mot: 'vrai', texte: ['LE VRAI.'], y: 430, gras: true, taille: 110, c: COL.chaux },
    { seg: 'preuve', mot: 'sections', texte: ['Nos sections. Nos aciers.', 'Nos habitudes. Nos délais.'], y: 390, taille: 58 },
  ],
  frise: { seg: 'suite', mot: 'poutre', y: 580, etapes: ['POUTRE', 'POTEAUX', 'DALLES', 'SEMELLES', 'ESCALIERS'] },
}));
