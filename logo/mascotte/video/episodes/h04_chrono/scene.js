import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleDuel } from '../styles.js';

// Hook : une poutre, deux méthodes, deux chronos qui courent côte à côte.
lancer('episodes/h04_chrono/voix.json', () => styleDuel({
  segs: ['hook', 'defi', 'main', 'auto', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LE PLAN, DANS AUTOCAD',
  titre: 'UNE POUTRE.', sousTitre: 'DEUX MÉTHODES. UN CHRONO.', tailleTitre: 104,
  duel: {
    seg: 'main', mot: 'main', segAuto: 'auto', motAuto: 'donnes', vitesse: 320, stopAuto: 8,
    etapes: [
      { seg: 'main', mot: 'coffrage', nom: 'Coffrage' },
      { seg: 'main', mot: 'barres', nom: 'Barres' },
      { seg: 'main', mot: 'cadres', nom: 'Cadres' },
      { seg: 'main', mot: 'cotes', nom: 'Cotes' },
      { seg: 'main', mot: 'repères', nom: 'Repères' },
    ],
    verdictG: '40 MINUTES', verdictD: '8 SECONDES',
  },
}));
