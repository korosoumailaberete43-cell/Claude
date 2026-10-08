import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleDuel } from '../styles.js';

// Hook : une poutre précise, le spectateur devine le temps, le chrono tranche.
lancer('episodes/h08_devine/voix.json', () => styleDuel({
  segs: ['hook', 'compte', 'verdict', 'twist', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'BARRES · CADRES · COTES · REPÈRES',
  titre: '30 × 60', sousTitre: 'PORTÉE 5,40 m — COMBIEN DE TEMPS ?', tailleTitre: 150,
  duel: {
    seg: 'verdict', mot: 'main', segAuto: 'twist', motAuto: 'si', vitesse: 520, stopAuto: 8,
    etapes: [
      { seg: 'verdict', mot: 'Entre', nom: 'Tracer' },
      { seg: 'verdict', mot: 'trente', nom: 'Ferrailler' },
      { seg: 'verdict', mot: 'heure', nom: 'Coter' },
      { seg: 'verdict', mot: 'tromper', nom: 'Vérifier' },
    ],
    verdictG: '30 à 60 MIN', verdictD: 'UN CAFÉ',
  },
}));
