import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleRecit } from '../styles.js';

// Hook : la dernière vidéo de la série — bilan et suite.
lancer('episodes/h33_rendezvous/voix.json', () => styleRecit({
  segs: ['hook', 'bilan', 'projet', 'suite', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'L’INTELLIGENCE DE L’ARMATURE',
  phrases: [
    { seg: 'hook', mot: 'dernière', texte: ['LA DERNIÈRE VIDÉO', 'DE LA SÉRIE.'], y: 380, gras: true, taille: 72, c: COL.cuivreC },
    { seg: 'bilan', mot: 'enrobage', texte: ['Enrobage. Ancrage.', 'Cadres. Trémies.', 'Poteaux courts.'], y: 340, taille: 64 },
    { seg: 'projet', mot: 'seule', texte: ['Et la poutre a commencé', 'à se dessiner toute seule.'], y: 390, taille: 58 },
  ],
  frise: { seg: 'suite', mot: 'poteaux', y: 580, etapes: ['POUTRE', 'POTEAUX', 'DALLES', 'SEMELLES', 'ESCALIERS'] },
}));
