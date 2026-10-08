// Éléments graphiques communs aux épisodes de Tonton (zone haute y ≈ 230 → 670, Tonton en bas).
import { W, COL, g, txt, slam, roundRect, glow, lockup, prog, win, lerp, eoB, eoX, eio, clamp, decay, rgba, font, wt, beg, end } from '../moteur.js';

// Titre de série : petit sur-titre + grand mot
export function titreSerie(t, t0, t1, kicker, titre, couleur = COL.cuivreC, taille = 132) {
  const a = win(t, t0, t1, 0.15, 0.3);
  if (a <= 0) return;
  const k = eoX(prog(t, t0, t0 + 0.5));
  txt(kicker, W / 2, 300, font(500, 34, 'Mono'), COL.signal, { track: 8, alpha: a * k });
  slam(t, t0 + 0.15, titre, W / 2, 470, font(700, taille), couleur, { alpha: a });
}

// Compte à rebours circulaire (n secondes à partir de t0)
export function rebours(t, t0, n, x = W / 2, y = 450, r = 150) {
  const a = win(t, t0, t0 + n + 0.2, 0.2, 0.25);
  if (a <= 0) return;
  const ctx = g(), el = clamp((t - t0) / n);
  const reste = Math.max(1, Math.ceil(n - (t - t0)));
  ctx.save(); ctx.globalAlpha = a;
  ctx.lineWidth = r * 0.11; ctx.strokeStyle = rgba(COL.beton, .18); ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.stroke();
  ctx.strokeStyle = COL.cuivre; ctx.lineCap = 'round'; ctx.beginPath(); ctx.arc(x, y, r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * (1 - el)); ctx.stroke();
  const pulse = 1 + 0.18 * decay(t, t0 + (n - reste), 5);
  ctx.translate(x, y); ctx.scale(pulse, pulse);
  txt(String(reste), 0, r * 0.35, font(700, r), COL.chaux);
  ctx.restore();
}

// Coupe de poutre : béton + cadre + 4 barres. cover = enrobage visuel en px (0 = barres collées au coffrage)
export function coupe(x, y, w, h, { cover = 30, a = 1, cadre = COL.chaux, barres = COL.cuivre, epais = 6, hl = 0 } = {}) {
  const ctx = g();
  ctx.save(); ctx.globalAlpha = a;
  roundRect(x, y, w, h, 6, '#5d6670', rgba(COL.beton, .7), 3);
  // grain du béton
  for (let i = 0; i < 70; i++) {
    const px = x + ((i * 97) % 100) / 100 * w, py = y + ((i * 61) % 100) / 100 * h;
    ctx.fillStyle = 'rgba(30,36,44,.35)'; ctx.beginPath(); ctx.arc(px, py, 2 + (i % 3), 0, 7); ctx.fill();
  }
  const r = 17, c = cover;
  ctx.strokeStyle = hl ? COL.signal : cadre; ctx.lineWidth = epais + hl * 4;
  if (hl) { ctx.shadowColor = COL.signal; ctx.shadowBlur = 24 * hl; }
  ctx.beginPath(); ctx.roundRect(x + c, y + c, w - 2 * c, h - 2 * c, 14); ctx.stroke();
  ctx.shadowBlur = 0;
  [[x + c + r + epais / 2, y + c + r + epais / 2], [x + w - c - r - epais / 2, y + c + r + epais / 2], [x + c + r + epais / 2, y + h - c - r - epais / 2], [x + w - c - r - epais / 2, y + h - c - r - epais / 2]].forEach(([bx, by]) => {
    ctx.fillStyle = barres; ctx.beginPath(); ctx.arc(bx, by, r, 0, 7); ctx.fill();
    ctx.fillStyle = 'rgba(255,255,255,.25)'; ctx.beginPath(); ctx.arc(bx - 5, by - 5, 6, 0, 7); ctx.fill();
  });
  ctx.restore();
}

// Cercle rouge qui entoure une zone (dessin progressif)
export function entoure(t, t0, x, y, rx, ry, a = 1) {
  const k = clamp((t - t0) / 0.45);
  if (k <= 0 || a <= 0) return;
  const ctx = g();
  ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = COL.rouge; ctx.lineWidth = 9; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.ellipse(x, y, rx, ry, -0.12, -0.6, -0.6 + Math.PI * 2.1 * eio(k)); ctx.stroke(); ctx.restore();
}

// Tampon « VRAI » / « FAUX » / « ✓ »
export function tampon(t, t0, s, x, y, couleur, taille = 120, rot = -0.14, a = 1) {
  const k = prog(t, t0, t0 + 0.22);
  if (k <= 0 || a <= 0) return;
  const ctx = g(), sc = lerp(2.4, 1, eoX(k));
  ctx.save(); ctx.globalAlpha = a * clamp(k * 3); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(sc, sc);
  ctx.font = font(700, taille); ctx.letterSpacing = '8px';
  const w = ctx.measureText(s).width + 70;
  roundRect(-w / 2, -taille * 0.78, w, taille * 1.12, 22, rgba(couleur, .12), couleur, 10);
  txt(s, 0, taille * 0.2, font(700, taille), couleur, { track: 8 });
  ctx.restore();
}

// Fin commune : logo CivRebar AI + badge, puis bouton d'abonnement
export function finCivrebar(t, segCiv, badge = 'BIENTÔT DANS AUTOCAD') {
  const t0 = beg(segCiv) - 0.1;
  const a = win(t, t0, 1e9, 0.3, 0.3);
  if (a <= 0) return;
  const k = eoB(prog(t, t0, t0 + 0.6)), ctx = g();
  glow(W / 2, 340, 420, COL.signal, 0.18 * a);
  ctx.save(); ctx.translate(W / 2, 330); ctx.scale(k * 0.95, k * 0.95); ctx.translate(-W / 2, -330); lockup(W / 2, 330, 1, a); ctx.restore();
  const kb = prog(t, t0 + 0.9, t0 + 1.2);
  if (kb > 0) { // le cadre s'ajuste à la longueur du badge
    ctx.save(); ctx.globalAlpha = a * kb;
    const taille = badge.length > 30 ? 26 : 30;
    ctx.font = font(700, taille); ctx.letterSpacing = '3px';
    const lb = Math.min(W - 120, ctx.measureText(badge).width + 60);
    roundRect(W / 2 - lb / 2, 560, lb, 62, 31, null, COL.cuivre, 3);
    txt(badge, W / 2, 602, font(700, taille), COL.cuivreC, { track: 3 });
    ctx.restore();
  }
}
export function abonne(t, tb) {
  const k = prog(t, tb, tb + 0.35);
  if (k <= 0) return;
  const ctx = g(), press = decay(t, tb + 0.9, 7);
  ctx.save(); ctx.translate(W / 2, 1420); ctx.scale(eoB(k) * (1 - press * 0.08), eoB(k) * (1 - press * 0.08));
  roundRect(-250, -60, 500, 120, 60, t > tb + 0.9 ? COL.acier : COL.cuivre);
  txt(t > tb + 0.9 ? '✓ ABONNÉ' : '+ ABONNE-TOI', 0, 16, font(700, 46), t > tb + 0.9 ? COL.chaux : COL.nuit, { track: 1 });
  ctx.restore();
  if (t > tb + 0.5 && t < tb + 1.4) {
    const kk = eio(prog(t, tb + 0.5, tb + 0.9));
    const x = lerp(W / 2 + 320, W / 2 + 120, kk), y = lerp(1560, 1450, kk);
    ctx.save(); ctx.fillStyle = COL.chaux; ctx.strokeStyle = COL.nuit; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.arc(x, y, 26 - press * 6, 0, 7); ctx.fill(); ctx.stroke(); ctx.restore();
  }
}
// Sons communs de fin
export const cuesFin = (segCiv, segFin) => [
  { t: beg(segCiv) - 0.1, type: 'boom' }, { t: beg(segCiv) + 0.8, type: 'pop' },
  { t: wt(segFin, 'Abonne'), type: 'pop' }, { t: wt(segFin, 'Abonne') + 0.9, type: 'click' },
];
export { end };

// Étiquette arrondie qui apparaît avec un rebond (centrée en x, y)
export function puce(t, t0, s, x, y, couleur, a = 1, taille = 34) {
  const k = prog(t, t0, t0 + 0.3);
  if (k <= 0 || a <= 0) return;
  const ctx = g();
  ctx.save(); ctx.globalAlpha = a; ctx.translate(x, y); ctx.scale(eoB(k), eoB(k));
  ctx.font = font(700, taille); ctx.letterSpacing = '1px';
  const w = ctx.measureText(s).width + taille * 1.3, h = taille * 1.75;
  roundRect(-w / 2, -h / 2, w, h, h / 2, rgba(couleur, .16), couleur, 3);
  txt(s, 0, taille * 0.36, font(700, taille), couleur, { track: 1 });
  ctx.restore();
}
