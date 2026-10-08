import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';

// Hook : « regarde bien cette barre » — la loupe s'approche sur un crochet trop court.
lancer('episodes/h11_zoom/voix.json', () => styleLoupe({
  segs: ['hook', 'zoom', 'detail', 'consequence', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'ANCRAGES À LA BONNE LONGUEUR',
  loupe: {
    seg: 'detail', mot: 'court', tZoom: ['zoom', 'Encore'], cible: [790, 480], depart: [280, 330],
    kicker: 'REGARDE BIEN CETTE BARRE',
    dessin: (t, a, { tRep }) => {
      const ctx = g(), x0 = 150, x1 = W - 150, y = 480;
      ctx.save(); ctx.globalAlpha = a;
      // la barre filante et son crochet d'extrémité (trop court)
      ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 16; ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1 - 60, y); ctx.stroke();
      const trop = t > tRep;
      ctx.beginPath(); ctx.moveTo(x1 - 60, y); ctx.lineTo(x1 - 60, y - (trop ? 42 : 42)); ctx.stroke();
      // cote de l'ancrage demandé, en pointillés
      if (trop) {
        ctx.setLineDash([10, 10]); ctx.strokeStyle = COL.signal; ctx.lineWidth = 4;
        ctx.beginPath(); ctx.moveTo(x1 - 60, y - 42); ctx.lineTo(x1 - 60, y - 120); ctx.stroke(); ctx.setLineDash([]);
        txt('MANQUE 2 cm', x1 - 80, y - 140, font(700, 30), COL.rouge, { align: 'right', alpha: a, track: 1 });
      }
      txt('CROCHET D’ANCRAGE', x0, y + 90, font(500, 26, 'Mono'), COL.beton, { align: 'left', alpha: a, track: 3 });
      ctx.restore();
    },
    puces: [
      { seg: 'consequence', mot: 'papier', texte: 'INVISIBLE SUR LE PAPIER', x: W / 2, y: 596, c: COL.beton },
      { seg: 'consequence', mot: 'glisse', texte: 'SOUS CHARGE : LA BARRE GLISSE', x: W / 2, y: 656, c: COL.rouge },
    ],
  },
}));
