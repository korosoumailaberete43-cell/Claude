import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleDuel } from '../styles.js';

// Hook : un poteau, deux méthodes, deux chronos.
lancer('episodes/h31_duel_poteau/voix.json', () => styleDuel({
  segs: ['hook', 'defi', 'main', 'auto', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LE POTEAU ARRIVE BIENTÔT',
  titre: 'UN POTEAU.', sousTitre: '30 × 30 — QUATRE NIVEAUX', tailleTitre: 112,
  duel: {
    seg: 'main', mot: 'main', segAuto: 'auto', motAuto: 'donnes', vitesse: 300, stopAuto: 9,
    etapes: [
      { seg: 'main', mot: 'fût', nom: 'Fût' },
      { seg: 'main', mot: 'barres', nom: 'Barres' },
      { seg: 'main', mot: 'zone', nom: 'Cadres par zone' },
      { seg: 'main', mot: 'recouvrements', nom: 'Recouvrements' },
      { seg: 'main', mot: 'cotes', nom: 'Cotes' },
    ],
    verdictG: '30 MINUTES', verdictD: 'QUELQUES SECONDES',
  },
}));
