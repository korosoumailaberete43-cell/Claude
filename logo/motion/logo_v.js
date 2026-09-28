// CivRebar AI — logo vertical (symbole au-dessus de CIVREBAR / AI), repris du SVG officiel.
// Couleurs : o.word = nom (Blanc chaux sur fond sombre, Nuit sur fond clair) ; filet et AI toujours Cuivre.
const VG = LOGO_V.word.glyphs.map(g => ({ dx: g.dx, p: new Path2D(g.d) }));
const VAI = LOGO_V.ai.glyphs.map(g => ({ dx: g.dx, p: new Path2D(g.d) }));
const VC = { x: 246.5, y: 201.5 }; // centre du logo vertical
const symInLockupV = (cx, cy, S) => ({ ox: cx + (156.49 - .75 * 5 - VC.x) * S, oy: cy + (-.75 * 10 - VC.y) * S, s: .75 * S });
function drawWordmarkV(t, cx, cy, S, o) {
  ctx.save();
  ctx.translate(cx, cy); ctx.scale(S, S); ctx.translate(-VC.x, -VC.y);
  ctx.globalAlpha = o.alpha == null ? 1 : o.alpha;
  const w = LOGO_V.word, sw = w.sc;
  ctx.save();
  ctx.beginPath(); ctx.rect(-50, w.ty - 740 * sw - 4, 600, 740 * sw + 10); ctx.clip();
  VG.forEach((g, i) => {
    const k = o.letters[i];
    if (k <= 0) return;
    ctx.save();
    ctx.translate(w.tx + g.dx, w.ty + (1 - eoX(k)) * 70);
    ctx.scale(sw, -sw); ctx.fillStyle = o.word || COL.chaux; ctx.fill(g.p);
    ctx.restore();
  });
  ctx.restore();
  if (o.rule > 0) {
    const L = 80 * eo3(o.rule);
    ctx.fillStyle = COL.cuivre; ctx.fillRect(206.49 + 40 - L / 2, 321.1, L, 3);
  }
  if (o.ai > 0) {
    const a = LOGO_V.ai, g = o.aiGlitch || 0, fr = Math.floor(t * FPS);
    const drawAI = (color, dx, al) => {
      ctx.save(); ctx.globalAlpha *= al;
      ctx.translate(a.tx + dx, a.ty);
      VAI.forEach(q => { ctx.save(); ctx.translate(q.dx, 0); ctx.scale(a.sc, -a.sc); ctx.fillStyle = color; ctx.fill(q.p); ctx.restore(); });
      ctx.restore();
    };
    if (g > .01) {
      ctx.save(); ctx.globalCompositeOperation = 'lighter';
      drawAI(COL.signal, -8 - 12 * g * rnd(fr), .8 * g);
      drawAI('#d0343a', 8 + 10 * g * rnd(fr + 1), .6 * g);
      ctx.restore();
      drawAI(COL.cuivre, (rnd(fr + 5) - .5) * 20 * g, rnd(fr + 9) > .25 * g ? 1 : .2);
    } else drawAI(COL.cuivre, 0, o.ai);
  }
  ctx.restore();
}
const FULL = { letters: VG.map(() => 1), rule: 1, ai: 1 };
