import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';
import { dessinNomenclature } from '../styles2.js';

// Hook : le tableau que personne ne lit, et qui part à l'atelier.
lancer('episodes/h20_nomenclature/voix.json', () => styleLoupe({
  segs: ['hook', 'suspense', 'role', 'risque', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'DESSIN ET NOMENCLATURE D’ACCORD',
  loupe: {
    seg: 'risque', mot: 'double', tZoom: ['role', 'repères'], cible: [540, 440], depart: [900, 320],
    kicker: 'PERSONNE NE LE REGARDE',
    dessin: dessinNomenclature([['Repère 1', '3 HA20 — 5,60 m'], ['Repère 2', '2 HA14 — 5,60 m'],
                                ['Repère 2', '28 HA8 — cadres'], ['Repère 4', '6 HA10 — épingles'],
                                ['Total', '4 repères']], 2),
    puces: [
      { seg: 'role', mot: 'longueurs', texte: 'IL NE VOIT QUE ÇA', x: W / 2, y: 700, c: COL.signal },
      { seg: 'risque', mot: 'arrête', texte: 'UN REPÈRE EN DOUBLE → CHANTIER À L’ARRÊT', x: W / 2, y: 700, c: COL.rouge },
    ],
  },
}));
