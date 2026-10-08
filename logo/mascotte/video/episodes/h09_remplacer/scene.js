import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleProvoc } from '../styles.js';

// Hook : la question qui fâche — « l'IA va-t-elle remplacer l'ingénieur ? » Réponse : NON.
lancer('episodes/h09_remplacer/voix.json', () => styleProvoc({
  segs: ['hook', 'suspense', 'non', 'pourquoi', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'ELLE PREND TON TRAVAIL RÉPÉTITIF',
  bandeau: 'L’IA VA-T-ELLE', sousBandeau: 'REMPLACER L’INGÉNIEUR ?', tailleBandeau: 78,
  finBandeau: ['non', 'Non'],
  verdict: { seg: 'non', mot: 'Non', texte: 'NON', taille: 190, y: 420, jusqu: 'pourquoi' },
  mots: [
    { seg: 'pourquoi', mot: 'calcule', texte: 'LA MACHINE CALCULE', c: COL.beton, taille: 60 },
    { seg: 'pourquoi', mot: 'porte', texte: 'MAIS ELLE NE PORTE RIEN', c: COL.chaux, taille: 60 },
    { seg: 'pourquoi', mot: 'décide', texte: 'L’INGÉNIEUR DÉCIDE', c: COL.cuivreC, taille: 64 },
    { seg: 'pourquoi', mot: 'signe', texte: 'ET IL SIGNE.', c: COL.signal, taille: 64 },
  ],
  motsY: 330,
}));
