// Cinq styles de vidéos « hook » pour Tonton Ferraille (format court, 25–30 s).
// Chaque épisode déclare un style + son contenu ; le style construit KEYS, CAMS, scenes et CUES.
import { W, H, COL, g, txt, slam, roundRect, glow, font, prog, win, lerp, eio, eoX, eoB, clamp, decay, rgba, rnd, wt, beg, end } from '../moteur.js';
import { coupe, entoure, puce, tampon, finCivrebar, abonne, cuesFin, rebours } from './commun.js';

// ---------------------------------------------------------------- briques communes
// Voile de couleur plein écran : donne son ambiance à chaque style
function voile(couleur, a) {
  if (a <= 0) return;
  const ctx = g(); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = couleur; ctx.fillRect(0, 0, W, H); ctx.restore();
}
// Secousse : décalage amorti après un impact
function secousse(t, t0, force = 14, r = 9) {
  const d = decay(t, t0, r);
  if (d < 0.01) return 0;
  g().translate(Math.sin((t - t0) * 70) * force * d, Math.cos((t - t0) * 61) * force * d * 0.6);
  return d;
}
// Bandes cinéma (haut et bas) : format « récit »
function bandes(a, h = 150) {
  if (a <= 0) return;
  const ctx = g(); ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = '#04080f';
  ctx.fillRect(0, 0, W, h); ctx.fillRect(0, H - h, W, h); ctx.restore();
}
// Texte sur plusieurs lignes, centré, qui apparaît ligne par ligne
function blocLignes(t, lignes, y0, interligne, taille, a, couleurs = []) {
  lignes.forEach((l, i) => {
    const [texte, t0] = l;
    const k = prog(t, t0, t0 + 0.28);
    if (k <= 0) return;
    const ctx = g(); ctx.save();
    ctx.translate(W / 2, y0 + i * interligne); ctx.scale(lerp(1.25, 1, eoX(k)), lerp(1.25, 1, eoX(k)));
    txt(texte, 0, 0, font(700, taille), couleurs[i] || COL.chaux, { alpha: a * clamp(k * 3), stroke: 14 });
    ctx.restore();
  });
}
// Compteur qui défile de « de » à « a »
function compteur(t, t0, t1, de, a_, x, y, taille, couleur, alpha = 1, suffixe = '') {
  const k = eio(prog(t, t0, t1));
  const v = Math.round(lerp(de, a_, k));
  const ctx = g(); ctx.save();
  const pop = 1 + 0.12 * decay(t, t1, 7);
  ctx.translate(x, y); ctx.scale(pop, pop);
  txt(v.toLocaleString('fr-FR') + suffixe, 0, 0, font(700, taille), couleur, { alpha, stroke: 16 });
  ctx.restore();
}
// Barre de progression horizontale
function jauge(x, y, w, h, k, couleur, a, fond = 'rgba(185,190,196,.18)') {
  const ctx = g(); ctx.save(); ctx.globalAlpha = a;
  roundRect(x, y, w, h, h / 2, fond);
  if (k > 0) roundRect(x, y, Math.max(h, w * clamp(k)), h, h / 2, couleur);
  ctx.restore();
}
// Chronomètre numérique mm:ss
function chrono(t, t0, vitesse, x, y, taille, couleur, a, stop = 1e9) {
  const s = Math.min(Math.max(0, t - t0), stop) * vitesse;
  const txtv = `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
  txt(txtv, x, y, font(700, taille, 'Mono'), couleur, { alpha: a, track: 2 });
}

// Poses par défaut : un style donne une intention par segment
const POSE_DEF = {
  choc: [['point', 'surprised'], ['think', 'think'], ['finger', 'angry'], ['explain', 'serious'], ['cheer', 'happy'], ['wave', 'happy']],
  duel: [['pointUp', 'happy'], ['count', 'think'], ['explain', 'serious'], ['point', 'proud'], ['cheer', 'happy'], ['wave', 'happy']],
  loupe: [['finger', 'surprised'], ['think', 'think'], ['point', 'angry'], ['explain', 'serious'], ['cheer', 'happy'], ['wave', 'happy']],
  provoc: [['finger', 'angry'], ['cross', 'serious'], ['explain', 'angry'], ['point', 'serious'], ['cheer', 'happy'], ['wave', 'happy']],
  recit: [['explain', 'serious'], ['think', 'think'], ['count', 'proud'], ['explain', 'proud'], ['cheer', 'happy'], ['wave', 'happy']],
};
// Construit KEYS et CAMS à partir de la liste des segments
function base(style, segs, camOverride = {}) {
  const def = POSE_DEF[style];
  const KEYS = [[0, 'idle', 'happy'], ...segs.map((s, i) => [beg(s) - (i ? 0 : 0.1), def[Math.min(i, def.length - 1)][0], def[Math.min(i, def.length - 1)][1]])];
  const vues = { choc: [0.05, 5.4, 2.4], duel: [0.18, 6.5, 2.25], loupe: [-0.12, 5.8, 2.35], provoc: [0, 5.2, 2.4], recit: [-0.2, 6.2, 2.3] };
  const [azB, dB, tyB] = vues[style];
  const CAMS = [[0, { az: azB, dist: dB + 0.6, ty: tyB, tx: 0 }], ...segs.map((s, i) => {
    const o = camOverride[s] || {};
    return [beg(s), { az: o.az != null ? o.az : azB * (i % 2 ? -1 : 1) + (i % 3) * 0.08, dist: o.dist || dB + (i % 2) * 0.5, ty: o.ty || tyB, tx: 0 }];
  })];
  return { KEYS, CAMS };
}
const finCommune = (t, segCiv, segFin, badge) => { finCivrebar(t, segCiv, badge); };

// ================================================================ STYLE 1 — CHOC
// Un chiffre énorme qui tombe, un compteur qui s'emballe, fond rouge sourd.
export function styleChoc(cfg) {
  const segs = cfg.segs, { KEYS, CAMS } = base('choc', segs);
  const tImp = cfg.impact != null ? cfg.impact : beg(segs[0]) + 0.1;
  function scenes(t, front) {
    if (front) { abonne(t, wt(cfg.segFin, 'Abonne')); return; }
    voile(COL.rouge, 0.1 * win(t, beg(segs[1]) - 0.2, beg(cfg.segCiv) - 0.2, 0.4, 0.4));
    // 1. le mot-choc
    const finChoc = cfg.chocJusqu ? wt(cfg.chocJusqu[0], cfg.chocJusqu[1])
      : (cfg.lignes ? wt(cfg.lignes[0].seg, cfg.lignes[0].mot) - 0.15 : beg(segs[2]));
    const a1 = win(t, tImp - 0.1, finChoc, 0.1, 0.3);
    if (a1 > 0) {
      const ctx = g(); ctx.save(); secousse(t, tImp);
      slam(t, tImp, cfg.choc, W / 2, 400, font(700, cfg.tailleChoc || 190), COL.chaux, { alpha: a1, stroke: 0 });
      if (cfg.sousChoc) slam(t, tImp + 0.45, cfg.sousChoc, W / 2, 530, font(700, 54), COL.rouge, { alpha: a1 });
      ctx.restore();
    }
    // 2. le compteur qui monte
    if (cfg.compteur) {
      const c = cfg.compteur, t0 = wt(c.seg, c.mot), a2 = win(t, t0 - 0.3, c.jusqu ? beg(c.jusqu) : beg(cfg.segCiv) - 0.2, 0.25, 0.3);
      if (a2 > 0) {
        glow(W / 2, 400, 420, COL.rouge, 0.22 * a2);
        compteur(t, t0, t0 + (c.duree || 1.3), c.de, c.a, W / 2, 420, 180, c.c || COL.rouge, a2, c.suffixe || '');
        txt(c.label, W / 2, 530, font(700, 46), COL.chaux, { alpha: a2, track: 2 });
        if (c.sous) txt(c.sous, W / 2, 600, font(600, 34, 'Manrope'), COL.beton, { alpha: a2 });
      }
    }
    // 3. les lignes de constat
    if (cfg.lignes) {
      const l0 = cfg.lignes[0], fin3 = cfg.lignesJusqu ? wt(cfg.lignesJusqu[0], cfg.lignesJusqu[1]) : beg(cfg.segCiv) - 0.15;
      const a3 = win(t, wt(l0.seg, l0.mot) - 0.3, fin3, 0.25, 0.3);
      if (a3 > 0) blocLignes(t, cfg.lignes.map(l => [l.t, wt(l.seg, l.mot)]), cfg.lignesY || 360, 96, 62, a3, cfg.lignes.map(l => l.c || COL.chaux));
    }
    // 4. second coup de massue (facultatif)
    if (cfg.choc2) {
      const c2 = cfg.choc2, t2 = wt(c2.seg, c2.mot);
      const a4 = win(t, t2 - 0.25, c2.jusqu ? beg(c2.jusqu) - 0.15 : beg(cfg.segCiv) - 0.15, 0.2, 0.3);
      if (a4 > 0) {
        const ctx = g(); ctx.save(); secousse(t, t2);
        if (c2.sous) slam(t, t2 - 0.2, c2.sous, W / 2, 330, font(700, 54), COL.beton, { alpha: a4 });
        glow(W / 2, 460, 400, COL.rouge, 0.22 * a4);
        slam(t, t2, c2.texte, W / 2, 490, font(700, c2.taille || 150), c2.c || COL.rouge, { alpha: a4, stroke: 0 });
        ctx.restore();
      }
    }
    finCommune(t, cfg.segCiv, cfg.segFin, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: tImp, type: 'slam' }, { t: tImp + 0.45, type: 'error' },
    ...(cfg.choc2 ? [{ t: wt(cfg.choc2.seg, cfg.choc2.mot) - 0.6, type: 'riser' }, { t: wt(cfg.choc2.seg, cfg.choc2.mot), type: 'boom' }] : []),
    ...(cfg.compteur ? [{ t: wt(cfg.compteur.seg, cfg.compteur.mot), type: 'riser' }, { t: wt(cfg.compteur.seg, cfg.compteur.mot) + (cfg.compteur.duree || 1.3), type: 'boom' }] : []),
    ...(cfg.lignes || []).map(l => ({ t: wt(l.seg, l.mot), type: 'tick' })),
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[tImp, 0.55], ...(cfg.choc2 ? [[wt(cfg.choc2.seg, cfg.choc2.mot), 0.45]] : []), [beg(cfg.segCiv) - 0.1, 0.5]] };
}

// ================================================================ STYLE 2 — DUEL
// Écran coupé en deux : la main contre CivRebar, deux chronos qui courent.
export function styleDuel(cfg) {
  const segs = cfg.segs, { KEYS, CAMS } = base('duel', segs);
  const tStart = wt(cfg.duel.seg, cfg.duel.mot);
  const tAuto = wt(cfg.duel.segAuto, cfg.duel.motAuto);
  function scenes(t, front) {
    if (front) { abonne(t, wt(cfg.segFin, 'Abonne')); return; }
    const a = win(t, tStart - 0.3, beg(cfg.segCiv) - 0.1, 0.3, 0.3);
    if (a > 0) {
      const ctx = g(); ctx.save(); ctx.globalAlpha = a;
      const y0 = 250, h = 430, mid = W / 2;
      roundRect(60, y0, mid - 90, h, 24, 'rgba(40,20,20,.92)', rgba(COL.rouge, .5), 2);
      roundRect(mid + 30, y0, mid - 90, h, 24, 'rgba(14,34,44,.92)', rgba(COL.signal, .5), 2);
      ctx.restore();
      txt('À LA MAIN', 60 + (mid - 90) / 2, y0 + 56, font(700, 38), COL.rouge, { alpha: a, track: 3 });
      txt('CIVREBAR AI', mid + 30 + (mid - 90) / 2, y0 + 56, font(700, 38), COL.signal, { alpha: a, track: 3 });
      // chronos
      const cxG = 60 + (mid - 90) / 2, cxD = mid + 30 + (mid - 90) / 2;
      chrono(t, tStart, cfg.duel.vitesse || 110, cxG, y0 + 185, 86, COL.chaux, a, tAuto + 1.0 - tStart);
      chrono(t, tAuto, 1, cxD, y0 + 185, 86, COL.chaux, a * prog(t, tAuto - 0.1, tAuto + 0.1), cfg.duel.stopAuto || 8);
      if (t < tAuto) txt('—:—', cxD, y0 + 185, font(700, 86, 'Mono'), rgba(COL.beton, .35), { alpha: a, track: 2 });
      // étapes cochées à gauche, d'un coup à droite
      (cfg.duel.etapes || []).forEach((e, i) => {
        const k = prog(t, wt(e.seg, e.mot), wt(e.seg, e.mot) + 0.25);
        txt((k > 0 ? '✓ ' : '· ') + e.nom, 100, y0 + 265 + i * 48, font(600, 32, 'Manrope'), k > 0 ? COL.chaux : rgba(COL.beton, .4), { align: 'left', alpha: a });
        const kd = prog(t, tAuto + 0.15 + i * 0.08, tAuto + 0.3 + i * 0.08);
        txt((kd > 0 ? '✓ ' : '· ') + e.nom, mid + 70, y0 + 265 + i * 48, font(600, 32, 'Manrope'), kd > 0 ? COL.signal : rgba(COL.beton, .4), { align: 'left', alpha: a });
      });
      // verdict
      const kv = prog(t, tAuto + 1.0, tAuto + 1.3);
      if (kv > 0) {
        puce(t, tAuto + 1.0, cfg.duel.verdictG, cxG, y0 + h + 58, COL.rouge, a, 30);
        puce(t, tAuto + 1.1, cfg.duel.verdictD, cxD, y0 + h + 58, COL.vert, a, 30);
      }
    }
    // défi d'ouverture
    const ad = win(t, beg(segs[0]) - 0.1, tStart - 0.25, 0.1, 0.25);
    if (ad > 0) {
      slam(t, beg(segs[0]), cfg.titre, W / 2, 400, font(700, cfg.tailleTitre || 96), COL.chaux, { alpha: ad, stroke: 0 });
      if (cfg.sousTitre) slam(t, beg(segs[0]) + 0.5, cfg.sousTitre, W / 2, 510, font(600, 46), COL.cuivreC, { alpha: ad });
    }
    finCommune(t, cfg.segCiv, cfg.segFin, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg(segs[0]), type: 'slam' }, { t: tStart - 0.25, type: 'whoosh' },
    ...(cfg.duel.etapes || []).map(e => ({ t: wt(e.seg, e.mot), type: 'tick' })),
    { t: tAuto, type: 'draw' }, { t: tAuto + 1.0, type: 'chime' },
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[tAuto, 0.4], [beg(cfg.segCiv) - 0.1, 0.5]] };
}

// ================================================================ STYLE 3 — LOUPE
// Un plan, une loupe qui glisse vers le détail, le cercle rouge, le verdict.
export function styleLoupe(cfg) {
  const segs = cfg.segs, { KEYS, CAMS } = base('loupe', segs);
  const tRep = wt(cfg.loupe.seg, cfg.loupe.mot);
  const tZoom = cfg.loupe.tZoom ? wt(cfg.loupe.tZoom[0], cfg.loupe.tZoom[1]) : tRep - 1.2;
  function scenes(t, front) {
    if (front) { abonne(t, wt(cfg.segFin, 'Abonne')); return; }
    const a = win(t, beg(segs[0]) + 0.2, beg(cfg.segCiv) - 0.1, 0.3, 0.3);
    if (a > 0) {
      const ctx = g(); ctx.save(); ctx.globalAlpha = a;
      roundRect(70, 240, W - 140, 440, 26, 'rgba(18,31,48,.95)', 'rgba(185,190,196,.22)', 2);
      ctx.restore();
      txt(cfg.loupe.kicker || 'REGARDE BIEN', 110, 300, font(500, 26, 'Mono'), COL.signal, { align: 'left', track: 6, alpha: a });
      cfg.loupe.dessin(t, a, { tRep, tZoom });
      // loupe qui glisse puis se fige sur la cible
      const kl = cfg.loupe.sans ? 0 : prog(t, tZoom, tZoom + 0.8);
      if (kl > 0 && t < beg(cfg.segCiv) - 0.3) {
        const [cx, cy] = cfg.loupe.cible;
        const x = lerp(cfg.loupe.depart ? cfg.loupe.depart[0] : 900, cx, eio(kl));
        const y = lerp(cfg.loupe.depart ? cfg.loupe.depart[1] : 300, cy, eio(kl));
        const r = lerp(60, 110, eio(kl));
        ctx.save(); ctx.globalAlpha = a;
        ctx.strokeStyle = COL.chaux; ctx.lineWidth = 7; ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.stroke();
        ctx.lineWidth = 11; ctx.beginPath(); ctx.moveTo(x + r * 0.72, y + r * 0.72); ctx.lineTo(x + r * 1.35, y + r * 1.35); ctx.stroke();
        ctx.restore();
        entoure(t, tRep, cx, cy, r * 0.92, r * 0.92, a * prog(t, tRep, tRep + 0.2));
      }
      (cfg.loupe.puces || []).forEach((p, i) => puce(t, wt(p.seg, p.mot), p.texte, p.x || 270, p.y || (620 + i * 0), p.c || COL.rouge, a, 26));
    }
    finCommune(t, cfg.segCiv, cfg.segFin, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg(segs[0]), type: 'slam' }, { t: beg(segs[0]) + 0.2, type: 'whoosh' },
    ...(cfg.loupe.sans ? [] : [{ t: tZoom, type: 'suck' }, { t: tRep, type: 'error' }]),
    ...(cfg.loupe.puces || []).map(p => ({ t: wt(p.seg, p.mot), type: 'pop' })),
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[tRep, 0.35], [beg(cfg.segCiv) - 0.1, 0.5]] };
}

// ================================================================ STYLE 4 — PROVOC
// Typographie plein écran, bandeaux rouges, mots barrés : on secoue le spectateur.
export function styleProvoc(cfg) {
  const segs = cfg.segs, { KEYS, CAMS } = base('provoc', segs);
  function scenes(t, front) {
    if (front) { abonne(t, wt(cfg.segFin, 'Abonne')); return; }
    voile('#2a0d0d', 0.35 * win(t, beg(segs[0]) - 0.2, beg(cfg.segCiv) - 0.3, 0.3, 0.5));
    // bandeau d'ouverture
    const a0 = win(t, beg(segs[0]) - 0.1, cfg.finBandeau ? wt(cfg.finBandeau[0], cfg.finBandeau[1]) : beg(segs[2]), 0.1, 0.3);
    if (a0 > 0) {
      const ctx = g(); ctx.save(); secousse(t, beg(segs[0]));
      ctx.save(); ctx.globalAlpha = a0 * 0.95; ctx.translate(W / 2, 390); ctx.rotate(-0.035);
      ctx.fillStyle = COL.rouge; ctx.fillRect(-W / 2 - 40, -72, W + 80, 144); ctx.restore();
      slam(t, beg(segs[0]), cfg.bandeau, W / 2, 412, font(700, cfg.tailleBandeau || 82), COL.chaux, { alpha: a0, stroke: 0 });
      if (cfg.sousBandeau) slam(t, beg(segs[0]) + 0.55, cfg.sousBandeau, W / 2, 560, font(700, 52), COL.cuivreC, { alpha: a0 });
      ctx.restore();
    }
    // mots empilés, certains barrés
    if (cfg.mots) {
      const m0 = cfg.mots[0], a1 = win(t, wt(m0.seg, m0.mot) - 0.3, beg(cfg.segCiv) - 0.15, 0.25, 0.3);
      if (a1 > 0) cfg.mots.forEach((m, i) => {
        const t0 = wt(m.seg, m.mot), k = prog(t, t0, t0 + 0.26);
        if (k <= 0) return;
        const y = (cfg.motsY || 330) + i * 92, ctx = g();
        ctx.save(); ctx.translate(W / 2, y); ctx.scale(lerp(1.3, 1, eoX(k)), lerp(1.3, 1, eoX(k)));
        txt(m.texte, 0, 0, font(700, m.taille || 68), m.c || COL.chaux, { alpha: a1 * clamp(k * 3), stroke: 14 });
        if (m.barre) { // trait rouge qui raye le mot
          const kb = prog(t, t0 + 0.3, t0 + 0.6);
          if (kb > 0) {
            ctx.strokeStyle = COL.rouge; ctx.lineWidth = 10; ctx.lineCap = 'round'; ctx.globalAlpha = a1;
            ctx.font = font(700, m.taille || 68); const w = ctx.measureText(m.texte).width;
            ctx.beginPath(); ctx.moveTo(-w / 2 - 14, -16); ctx.lineTo(-w / 2 - 14 + (w + 28) * eio(kb), -16); ctx.stroke();
          }
        }
        ctx.restore();
      });
    }
    // réponse tranchée (grand mot unique)
    if (cfg.verdict) {
      const tv = wt(cfg.verdict.seg, cfg.verdict.mot);
      tampon(t, tv, cfg.verdict.texte, W / 2, cfg.verdict.y || 430, cfg.verdict.c || COL.rouge, cfg.verdict.taille || 150, -0.1,
        win(t, tv - 0.05, cfg.verdict.jusqu ? beg(cfg.verdict.jusqu) : beg(cfg.segCiv) - 0.2, 0.05, 0.3));
    }
    finCommune(t, cfg.segCiv, cfg.segFin, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg(segs[0]), type: 'slam' }, { t: beg(segs[0]) + 0.55, type: 'error' },
    ...(cfg.mots || []).map(m => ({ t: wt(m.seg, m.mot), type: m.barre ? 'scratch' : 'tick' })),
    ...(cfg.verdict ? [{ t: wt(cfg.verdict.seg, cfg.verdict.mot), type: 'stamp' }] : []),
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[beg(segs[0]), 0.4], [beg(cfg.segCiv) - 0.1, 0.5]] };
}

// ================================================================ STYLE 5 — RÉCIT
// Bandes cinéma, phrases en serif, montée lente : on raconte le projet.
export function styleRecit(cfg) {
  const segs = cfg.segs, { KEYS, CAMS } = base('recit', segs);
  function scenes(t, front) {
    if (front) {
      bandes(win(t, 0.2, beg(cfg.segCiv) - 0.2, 0.5, 0.4) * 0.92);
      abonne(t, wt(cfg.segFin, 'Abonne'));
      return;
    }
    voile('#060d18', 0.45 * win(t, 0.2, beg(cfg.segCiv) - 0.3, 0.5, 0.5));
    // phrases en serif qui se succèdent
    (cfg.phrases || []).forEach((p, i) => {
      const t0 = wt(p.seg, p.mot);
      const t1 = i + 1 < cfg.phrases.length ? wt(cfg.phrases[i + 1].seg, cfg.phrases[i + 1].mot) : beg(cfg.segCiv) - 0.15;
      const a = win(t, t0 - 0.15, t1, 0.35, 0.35);
      if (a <= 0) return;
      const k = eio(prog(t, t0 - 0.15, t0 + 0.9));
      const ctx = g(); ctx.save(); ctx.translate(W / 2, (p.y || 420) - 18 * (1 - k)); ctx.scale(lerp(0.97, 1, k), lerp(0.97, 1, k));
      (p.texte || []).forEach((l, j) => txt(l, 0, j * (p.interligne || 88), font(p.gras ? 700 : 'italic 400', p.taille || 76, p.gras ? 'Sora' : 'Serif'), p.c || COL.chaux, { alpha: a }));
      ctx.restore();
    });
    // frise d'étapes (optionnelle)
    if (cfg.frise) {
      const f = cfg.frise, t0 = wt(f.seg, f.mot), a = win(t, t0 - 0.2, beg(cfg.segCiv) - 0.15, 0.3, 0.3);
      if (a > 0) {
        const x0 = 150, x1 = W - 150, y = f.y || 560, ctx = g();
        ctx.save(); ctx.globalAlpha = a; ctx.lineWidth = 8;
        ctx.strokeStyle = rgba(COL.beton, .25); ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
        const k = eio(prog(t, t0, t0 + 1.6));
        ctx.strokeStyle = COL.cuivre; ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x0 + (x1 - x0) * k, y); ctx.stroke();
        f.etapes.forEach((e, i) => {
          const x = x0 + (x1 - x0) * i / (f.etapes.length - 1), ki = clamp((k * (f.etapes.length - 1)) - i + 0.4);
          ctx.fillStyle = ki > 0.5 ? (i === 0 ? COL.cuivre : COL.chaux) : COL.acier;
          ctx.beginPath(); ctx.arc(x, y, 18, 0, 7); ctx.fill();
          txt(e, x, y + (i % 2 ? 58 : -40), font(700, 26), ki > 0.5 ? COL.chaux : rgba(COL.beton, .5), { alpha: a });
        });
        ctx.restore();
      }
    }
    finCommune(t, cfg.segCiv, cfg.segFin, cfg.badge);
  }
  const CUES = [
    { t: 0.15, type: 'pop' }, { t: beg(segs[0]), type: 'swell' },
    ...(cfg.phrases || []).map(p => ({ t: wt(p.seg, p.mot), type: 'blip' })),
    ...(cfg.frise ? [{ t: wt(cfg.frise.seg, cfg.frise.mot), type: 'draw' }] : []),
    { t: beg(cfg.segCiv) - 0.9, type: 'riser' }, ...cuesFin(cfg.segCiv, cfg.segFin),
  ];
  return { KEYS, CAMS, scenes, CUES, flashes: [[beg(cfg.segCiv) - 0.1, 0.5]] };
}

export { voile, secousse, bandes, compteur, jauge, chrono, blocLignes, coupe, puce, entoure, tampon, rebours };
