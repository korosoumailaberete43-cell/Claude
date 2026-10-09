import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';
import { dessinPoteau } from '../styles2.js';

// Hook : « ce poteau va casser » — la loupe montre les cadres trop espacés sur la partie libre.
lancer('episodes/h15_poteaucourt/voix.json', () => styleLoupe({
  segs: ['hook', 'suspense', 'cause', 'effet', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'CADRES RESSERRÉS OÙ IL FAUT',
  loupe: {
    seg: 'effet', mot: 'concentre', tZoom: ['cause', 'allèges'], cible: [540, 400], depart: [880, 600],
    kicker: 'CE POTEAU VA CASSER', dessin: dessinPoteau({ allèges: true }),
    puces: [
      { seg: 'cause', mot: 'quarante', texte: '40 cm DE HAUTEUR LIBRE', x: W / 2, y: 690, c: COL.signal },
      { seg: 'effet', mot: 'énorme', texte: 'EFFORT TRANCHANT ÉNORME', x: W / 2, y: 690, c: COL.rouge },
    ],
  },
}));
