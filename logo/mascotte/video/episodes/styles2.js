// Deux styles supplémentaires + les dessins au trait des épisodes « loupe ».
import { W, H, COL, g, txt, slam, roundRect, glow, font, prog, win, lerp, eio, eoX, eoB, clamp, decay, rgba, wt, beg, end } from '../moteur.js';
import { finCivrebar, abonne, cuesFin, puce } from './commun.js';

// ================================================================ STYLE 6 — LISTE
// Un décompte : de gros numéros qui s'empilent, le dernier en rouge.
export function styleListe(cfg) {
  const segs = cfg.segs;
  const POSES = [['pointUp', 'surprised'], ['count', 'serious'], ['count', 'angry'], ['finger', 'angry'], ['cheer', 'happy'], ['wave', 'happy']];
  const KEYS = [[0, 'idle', 'happy'], ...segs.map((s, i) => [beg(s) - (i ? 0 : 0.1), ...POSES[Math.min(i, 5)]])];
  const CAMS = [[0, { az: 0, dist: 6.2, ty: 2.3, tx: 0 }], ...segs.map((s, i) => [beg(s), { az: (i % 2 ? -0.16 : 0.16), dist: 5.8 + (i % 2) * 0.5, ty: 2.35, tx: 0 }])];
  function scenes(t, front) {
    if (front) { abonne(t, wt(cfg.segFin, 'Abonne')); return; }
    // titre d'ouverture
    const t1 = wt(cfg.items[0].seg, cfg.items[0].mot) - 0.2;
    const a0 = win(t, beg(segs[0]) - 0.1, t1, 0.1, 0.25);
    if (a0 > 0) {
      slam(t, beg(segs[0]), cfg.titre, W / 2, 400, font(700, cfg.tailleTitre || 86), COL.chaux, { alpha: a0, stroke: 0 });
      if (cfg.sousTitre) slam(t, beg(segs[0]) + 0.5, cfg.sousTitre, W / 2, 520, font(600, 48), COL.cuivreC, { alpha: a0 });
    }
    // les entrées de la liste
    const a = win(t, t1, beg(cfg.segCiv) - 0.15, 0.2, 0.3);
    if (a > 0) {
      const ctx = g();
      cfg.items.forEach((it, i) => {
        const t0 = wt(it.seg, it.mot), k = prog(t, t0, t0 + 0.3);
        if (k <= 0) return;
        const y = (cfg.y0 || 300) + i * (cfg.pas || 112);
        const dernier = i === cfg.items.length - 1;
        ctx.save(); ctx.globalAlpha = a; ctx.translate(140, y); ctx.scale(lerp(1.2, 1, eoX(k)), lerp(1.2, 1, eoX(k)));
        txt(it.n, 0, 0, font(700, 82), dernier ? COL.rouge : COL.cuivre, { align: 'left' });
        txt(it.texte, 120, -16, font(700, it.taille || 46), dernier ? COL.chaux : COL.chaux, { align: 'left', stroke: 10 });
        if (it.sous) txt(it.sous, 120, 30, font(600, 32, 'Manrope'), COL.beton, { align: 'left' });
        ctx.restore();
      });
    }
    finCivrebar(t, cfg.segCiv, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg(segs[0]), type: 'slam' },
    ...cfg.items.map((it, i) => ({ t: wt(it.seg, it.mot), type: i === cfg.items.length - 1 ? 'boom' : 'tick' })),
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  const dernier = cfg.items[cfg.items.length - 1];
  return { KEYS, CAMS, scenes, CUES, flashes: [[wt(dernier.seg, dernier.mot), 0.4], [beg(cfg.segCiv) - 0.1, 0.5]] };
}

// ================================================================ STYLE 7 — MESSAGE
// Une bulle de message reçue, puis la réponse de Tonton.
export function styleMessage(cfg) {
  const segs = cfg.segs;
  const POSES = [['think', 'surprised'], ['explain', 'serious'], ['explain', 'think'], ['finger', 'serious'], ['cheer', 'happy'], ['wave', 'happy']];
  const KEYS = [[0, 'idle', 'happy'], ...segs.map((s, i) => [beg(s) - (i ? 0 : 0.1), ...POSES[Math.min(i, 5)]])];
  const CAMS = [[0, { az: 0, dist: 6.0, ty: 2.32, tx: 0 }], ...segs.map((s, i) => [beg(s), { az: (i % 2 ? 0.2 : -0.14), dist: 5.6 + (i % 3) * 0.4, ty: 2.33, tx: 0 }])];
  // bulle façon messagerie
  function bulle(t, t0, t1, texte, recue, yb) {
    const a = win(t, t0 - 0.2, t1, 0.25, 0.3);
    if (a <= 0) return;
    const ctx = g(), k = eoB(prog(t, t0 - 0.2, t0 + 0.4));
    ctx.save(); ctx.globalAlpha = a;
    ctx.font = font(600, 44, 'Manrope');
    // découpe le texte en lignes
    const max = 740, mots = texte.split(' '), lignes = []; let l = '';
    for (const m of mots) { const e = l ? l + ' ' + m : m; if (ctx.measureText(e).width > max && l) { lignes.push(l); l = m; } else l = e; }
    lignes.push(l);
    const h = 56 + lignes.length * 56, lg = Math.min(max + 60, Math.max(...lignes.map(x => ctx.measureText(x).width)) + 60);
    const x = recue ? 90 : W - 90 - lg, y = yb != null ? yb : (cfg.bulleY || 300);
    ctx.translate(x + lg / 2, y + h / 2); ctx.scale(lerp(0.88, 1, k), lerp(0.88, 1, k)); ctx.translate(-(x + lg / 2), -(y + h / 2));
    roundRect(x, y, lg, h, 28, recue ? '#1b2b3f' : COL.cuivre);
    lignes.forEach((s, i) => txt(s, x + 30, y + 72 + i * 56, font(600, 44, 'Manrope'), recue ? COL.chaux : COL.nuit, { align: 'left' }));
    txt(recue ? (cfg.de || 'Reçu') : 'Tonton', x + (recue ? 8 : lg - 8), y - 18, font(500, 26, 'Mono'), COL.beton, { align: recue ? 'left' : 'right', track: 3 });
    ctx.restore();
  }
  function scenes(t, front) {
    if (front) { abonne(t, wt(cfg.segFin, 'Abonne')); return; }
    const a0 = win(t, beg(segs[0]) - 0.1, wt(cfg.bulle.seg, cfg.bulle.mot) - 0.3, 0.1, 0.25);
    if (a0 > 0) slam(t, beg(segs[0]), cfg.titre, W / 2, 380, font(700, cfg.tailleTitre || 72), COL.chaux, { alpha: a0, stroke: 0 });
    bulle(t, wt(cfg.bulle.seg, cfg.bulle.mot), cfg.bulle.jusqu ? wt(cfg.bulle.jusqu[0], cfg.bulle.jusqu[1]) : beg(cfg.segCiv) - 0.15, cfg.bulle.texte, true);
    if (cfg.reponse) bulle(t, wt(cfg.reponse.seg, cfg.reponse.mot), beg(cfg.segCiv) - 0.15, cfg.reponse.texte, false, cfg.reponseY || (cfg.bulleY || 300) + 210);
    (cfg.puces || []).forEach(p => puce(t, wt(p.seg, p.mot), p.texte, W / 2, p.y || 640, p.c || COL.rouge, win(t, wt(p.seg, p.mot) - 0.2, beg(cfg.segCiv) - 0.15, 0.2, 0.3), 28));
    finCivrebar(t, cfg.segCiv, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg(segs[0]), type: 'slam' },
    { t: wt(cfg.bulle.seg, cfg.bulle.mot) - 0.2, type: 'blip' },
    ...(cfg.reponse ? [{ t: wt(cfg.reponse.seg, cfg.reponse.mot) - 0.2, type: 'blip' }] : []),
    ...(cfg.puces || []).map(p => ({ t: wt(p.seg, p.mot), type: 'pop' })),
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[beg(cfg.segCiv) - 0.1, 0.5]] };
}

// ================================================================ dessins au trait (zone y ≈ 280 → 660)
const BETON = '#5d6670';

// Poteau en élévation, bridé ou non par des allèges
export function dessinPoteau({ allèges = false, serre = 0 } = {}) {
  return (t, a) => {
    const ctx = g(), x0 = 455, y0 = 290, w = 170, h = 350;
    ctx.save(); ctx.globalAlpha = a;
    ctx.fillStyle = BETON; ctx.fillRect(x0, y0, w, h);
    ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x0, y0, w, h);
    if (allèges) {
      [[180, 340], [630, 340]].forEach(([ax, aw]) => {
        ctx.fillStyle = 'rgba(120,128,138,.5)'; ctx.fillRect(ax, y0 + 160, aw, 180);
        ctx.strokeStyle = rgba(COL.beton, .5); ctx.strokeRect(ax, y0 + 160, aw, 180);
      });
      txt('ALLÈGE', 300, y0 + 150, font(500, 24, 'Mono'), COL.beton, { track: 3, alpha: a });
      txt('ALLÈGE', 790, y0 + 150, font(500, 24, 'Mono'), COL.beton, { track: 3, alpha: a });
    }
    ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 8; ctx.lineCap = 'round';
    [x0 + 30, x0 + w - 30].forEach(x => { ctx.beginPath(); ctx.moveTo(x, y0 + 12); ctx.lineTo(x, y0 + h - 12); ctx.stroke(); });
    const pas = serre ? 22 : 46;
    ctx.strokeStyle = COL.chaux; ctx.lineWidth = 4;
    for (let y = y0 + 20; y <= y0 + h - 20; y += (serre && y < y0 + 170 ? pas : 46)) {
      ctx.beginPath(); ctx.moveTo(x0 + 16, y); ctx.lineTo(x0 + w - 16, y); ctx.stroke();
    }
    ctx.restore();
  };
}

// Poutre en élévation avec cadres à espacement réglable
export function dessinPoutreCadres({ pas = 92, serreAppuis = false } = {}) {
  return (t, a) => {
    const ctx = g(), x0 = 140, x1 = W - 140, y0 = 380, h = 165;
    ctx.save(); ctx.globalAlpha = a;
    ctx.fillStyle = BETON; ctx.fillRect(x0, y0, x1 - x0, h);
    ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x0, y0, x1 - x0, h);
    [x0 + 46, x1 - 46].forEach(x => {
      ctx.fillStyle = COL.beton; ctx.beginPath();
      ctx.moveTo(x, y0 + h); ctx.lineTo(x - 32, y0 + h + 46); ctx.lineTo(x + 32, y0 + h + 46); ctx.closePath(); ctx.fill();
    });
    ctx.strokeStyle = COL.cuivre; ctx.lineWidth = 8; ctx.lineCap = 'round';
    [y0 + 24, y0 + h - 24].forEach(y => { ctx.beginPath(); ctx.moveTo(x0 + 14, y); ctx.lineTo(x1 - 14, y); ctx.stroke(); });
    ctx.strokeStyle = COL.chaux; ctx.lineWidth = 4;
    if (serreAppuis) {
      [[x0 + 30, x0 + 230, 26], [x0 + 260, x1 - 260, 72], [x1 - 230, x1 - 30, 26]].forEach(([a0, a1, p]) => {
        for (let x = a0; x <= a1; x += p) { ctx.beginPath(); ctx.moveTo(x, y0 + 10); ctx.lineTo(x, y0 + h - 10); ctx.stroke(); }
      });
    } else {
      for (let x = x0 + 30; x <= x1 - 30; x += pas) { ctx.beginPath(); ctx.moveTo(x, y0 + 10); ctx.lineTo(x, y0 + h - 10); ctx.stroke(); }
    }
    ctx.restore();
  };
}

// Dalle vue de dessus, avec trémie éventuelle et renforts
export function dessinDalle({ tremie = false, renfort = false, sens = 0, appuis = false } = {}) {
  return (t, a) => {
    const ctx = g(), x0 = 130, y0 = appuis ? 346 : 300, w = W - 260, h = appuis ? 280 : 320;
    ctx.save(); ctx.globalAlpha = a;
    ctx.fillStyle = BETON; ctx.fillRect(x0, y0, w, h);
    ctx.strokeStyle = rgba(COL.beton, .7); ctx.lineWidth = 3; ctx.strokeRect(x0, y0, w, h);
    if (appuis) {   // les deux grands côtés sont appuyés
      ctx.fillStyle = 'rgba(185,190,196,.55)';
      ctx.fillRect(x0, y0 - 26, w, 26); ctx.fillRect(x0, y0 + h, w, 26);
      txt('APPUI', x0 + w / 2, y0 - 36, font(500, 22, 'Mono'), COL.beton, { track: 4, alpha: a });
      txt('APPUI', x0 + w / 2, y0 + h + 48, font(500, 22, 'Mono'), COL.beton, { track: 4, alpha: a });
    }
    ctx.lineCap = 'butt';
    const gros = 11, fin = 3;
    for (let y = y0 + 26; y < y0 + h; y += 44) {
      ctx.strokeStyle = sens === 1 ? COL.cuivre : rgba(COL.cuivre, sens ? .35 : 1);
      ctx.lineWidth = sens === 1 ? gros : (sens ? fin : 5);
      ctx.beginPath(); ctx.moveTo(x0 + 12, y); ctx.lineTo(x0 + w - 12, y); ctx.stroke();
    }
    for (let x = x0 + 30; x < x0 + w; x += 54) {
      ctx.strokeStyle = sens === 2 ? COL.cuivre : rgba(COL.cuivre, sens ? .35 : 1);
      ctx.lineWidth = sens === 2 ? gros : (sens ? fin : 5);
      ctx.beginPath(); ctx.moveTo(x, y0 + 12); ctx.lineTo(x, y0 + h - 12); ctx.stroke();
    }
    if (tremie) {
      const tx = x0 + w / 2 - 110, ty = y0 + h / 2 - 80;
      ctx.fillStyle = '#0d1b2c'; ctx.fillRect(tx, ty, 220, 160);
      ctx.strokeStyle = rgba(COL.beton, .8); ctx.lineWidth = 4; ctx.strokeRect(tx, ty, 220, 160);
      txt('TRÉMIE', tx + 110, ty + 95, font(500, 26, 'Mono'), COL.beton, { track: 3, alpha: a });
      if (renfort) {
        ctx.strokeStyle = COL.signal; ctx.lineWidth = 9; ctx.lineCap = 'round';
        ctx.strokeRect(tx - 22, ty - 22, 264, 204);
        [[[tx - 22, ty - 22], [tx - 100, ty - 90]], [[tx + 242, ty - 22], [tx + 320, ty - 90]],
         [[tx - 22, ty + 182], [tx - 100, ty + 250]], [[tx + 242, ty + 182], [tx + 320, ty + 250]]].forEach(([p, q]) => {
          ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(q[0], q[1]); ctx.stroke();
        });
      }
    }
    ctx.restore();
  };
}

// Tableau de nomenclature, avec une ligne en défaut
export function dessinNomenclature(lignes, iFaute) {
  return (t, a, { tRep } = {}) => {
    const ctx = g(), x0 = 140, y0 = 352, w = W - 280;
    ctx.save(); ctx.globalAlpha = a;
    lignes.forEach((l, i) => {
      const y = y0 + 20 + i * 60;
      const faute = tRep != null && t > tRep && i === iFaute;
      ctx.fillStyle = i % 2 ? 'rgba(255,255,255,.04)' : 'transparent'; ctx.fillRect(x0, y - 36, w, 56);
      txt(l[0], x0 + 18, y, font(500, 34, 'Mono'), faute ? COL.rouge : COL.beton, { align: 'left' });
      txt(l[1], x0 + w - 18, y, font(500, 34, 'Mono'), faute ? COL.rouge : COL.chaux, { align: 'right' });
    });
    ctx.strokeStyle = rgba(COL.beton, .25); ctx.lineWidth = 2;
    ctx.strokeRect(x0, y0 - 16, w, 20 + lignes.length * 60);
    ctx.restore();
  };
}
