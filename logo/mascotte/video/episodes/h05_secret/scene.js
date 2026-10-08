import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleChoc } from '../styles.js';

// Hook : « ×3 » — pourquoi certains bureaux d'études rendent trois fois plus de plans.
lancer('episodes/h05_secret/voix.json', () => styleChoc({
  segs: ['hook', 'suspense', 'reveal', 'explique', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'LE MÊME PLAN, EN QUELQUES SECONDES',
  impact: wt('hook', 'trois'),
  choc: '× 3', sousChoc: 'DE PLANS RENDUS.', tailleChoc: 230,
  lignes: [
    { seg: 'suspense', mot: 'travaillent', t: 'PAS PLUS D’HEURES', c: COL.beton },
    { seg: 'suspense', mot: 'nombreux', t: 'PAS PLUS DE MONDE', c: COL.beton },
    { seg: 'reveal', mot: 'arrêté', t: 'ILS ONT ARRÊTÉ', c: COL.chaux },
    { seg: 'reveal', mot: 'redessiner', t: 'DE REDESSINER', c: COL.cuivreC },
  ],
  lignesY: 330, lignesJusqu: ['explique', 'Parce'],
  compteur: { seg: 'explique', mot: 'logique', de: 1, a: 100, duree: 1.6, suffixe: ' ×', c: COL.signal, label: 'LA MÊME LOGIQUE', sous: 'seuls les chiffres changent' },
}));
