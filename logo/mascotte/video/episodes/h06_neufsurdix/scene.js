import { lancer, W, COL, g, txt, font, prog, lerp, eio, clamp, rgba, decay, wt, beg, end } from '../../moteur.js';
import { styleLoupe } from '../styles.js';

// Hook : « 9 sur 10 ratent cette erreur » — la loupe va chercher les cadres régulièrement espacés.
lancer('episodes/h06_neufsurdix/voix.json', () => styleLoupe({
  segs: ['hook', 'question', 'reponse', 'regle', 'civrebar', 'fin'],
  segCiv: 'civrebar', segFin: 'fin', badge: 'ESPACEMENT CALCULÉ, ZONE PAR ZONE',
  loupe: {
    seg: 'reponse', mot: 'espacés', tZoom: ['question', 'bien'], cible: [240, 470], depart: [880, 330],
    kicker: '9 INGÉNIEURS SUR 10 LA RATENT',
    dessin: (t, a, { tRep }) => {
      const ctx = g(), x0 = 130, x1 = W - 130, y0 = 390, h = 160;
      ctx.save(); ctx.globalAlpha = a;
      ctx.fillStyle = '#5d6670'; ctx.fillRect(x0, y0, x1 - x0, h);
      ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x0, y0, x1 - x0, h);
      [x0 + 42, x1 - 42].forEach(x => { ctx.fillStyle = COL.beton; ctx.beginPath(); ctx.moveTo(x, y0 + h); ctx.lineTo(x - 32, y0 + h + 46); ctx.lineTo(x + 32, y0 + h + 46); ctx.closePath(); ctx.fill(); });
      ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 7;
      [y0 + 24, y0 + h - 24].forEach(y => { ctx.beginPath(); ctx.moveTo(x0 + 14, y); ctx.lineTo(x1 - 14, y); ctx.stroke(); });
      // cadres tous identiques : c'est là l'erreur
      const n = 15;
      for (let i = 0; i < n; i++) {
        const x = x0 + 34 + (x1 - x0 - 68) * i / (n - 1);
        const k = clamp((t - beg('question') + 0.4 - i * 0.03) / 0.2);
        if (k <= 0) continue;
        const faute = t > tRep && (i < 3 || i > n - 4);
        ctx.strokeStyle = faute ? COL.rouge : COL.chaux; ctx.lineWidth = faute ? 6 : 4; ctx.globalAlpha = a * k;
        ctx.beginPath(); ctx.moveTo(x, y0 + 10); ctx.lineTo(x, y0 + h - 10); ctx.stroke();
      }
      ctx.restore();
    },
    puces: [
      { seg: 'reponse', mot: 'fin', texte: 'MÊME ESPACEMENT PARTOUT', x: W / 2, y: 596, c: COL.rouge },
      { seg: 'regle', mot: 'serrer', texte: 'AUX APPUIS → IL FAUT SERRER', x: W / 2, y: 656, c: COL.signal },
    ],
  },
}));
