import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';
import { dessinDalle } from '../styles2.js';

// Hook : une dalle percée après coup, sans renfort.
lancer('episodes/h22_tremie/voix.json', () => styleLoupe({
  segs: ['hook', 'suspense', 'probleme', 'regle', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LES RENFORTS AVEC LA DALLE',
  loupe: {
    seg: 'probleme', mot: 'coupe', tZoom: ['suspense', 'renforcé'], cible: [540, 460], depart: [900, 330],
    kicker: 'PERCÉE APRÈS COUP',
    dessin: (t, a) => dessinDalle({ tremie: true, renfort: t > wt('regle', 'chevêtre') })(t, a),
    puces: [
      { seg: 'probleme', mot: 'rien', texte: 'UNE BARRE COUPÉE NE PORTE PLUS RIEN', x: W / 2, y: 700, c: COL.rouge },
      { seg: 'regle', mot: 'diagonale', texte: 'CHEVÊTRE + DIAGONALES AUX ANGLES', x: W / 2, y: 700, c: COL.signal },
    ],
  },
}));
