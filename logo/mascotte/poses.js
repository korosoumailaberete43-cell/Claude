// Répertoire officiel des poses et expressions de Tonton Ferraille.
// À réutiliser tel quel dans chaque vidéo : tonton.setPose({ ...POSES.idle, ...POSES.point }).
// Angles en radians. r* = bras droit, l* = bras gauche ; rX < 0 lève le bras vers l'avant,
// rZ < 0 l'écarte vers l'extérieur ; rElbow < 0 plie le coude.
export const POSES = {
  idle: { rX: 0, rZ: 0.12, rElbow: -0.1, lX: 0.05, lZ: -0.18, lElbow: -1.35 },
  point: { rX: -1.45, rZ: 0.1, rElbow: -0.05, headNod: 0.04 },
  explain: { rX: -0.95, rZ: -0.35, rElbow: -0.9, headTilt: 0.05 },
  think: { rX: -1.25, rZ: 0.55, rElbow: -2.25, headTilt: 0.14, headNod: -0.12 },
  angry: { rX: 0.05, rZ: -0.3, rElbow: -0.25, lZ: -0.28, bow: 0.07, headNod: 0.1 },
  cheer: { rX: 0, rZ: -2.55, rElbow: -0.3, lX: 0, lZ: 2.45, lElbow: -0.35, headNod: -0.14 },
  pointUp: { rX: -2.55, rZ: 0.3, rElbow: -0.2, headNod: -0.22, headTurn: 0.12 },
  count: { rX: -1.2, rZ: -0.2, rElbow: -1.0, headTilt: -0.06 },
  lookSignal: { rX: -1.1, rZ: -0.7, rElbow: -0.6, headTurn: -0.45, headNod: -0.18 },
  finger: { rX: -2.25, rZ: -0.15, rElbow: -1.25, headNod: 0.06 },
  cross: { rX: -0.6, rZ: 0.7, rElbow: -1.9, lX: -0.6, lZ: -0.7, lElbow: -1.9, headNod: 0.05 },
  salute: { rX: -2.35, rZ: 0.75, rElbow: -2.15 },
  wave: { rX: -0.2, rZ: -2.3, rElbow: -0.45 },
};

// brow : + levés / − froncés · browAngle : + colère · lid : 0 ouvert → 1 fermé
// lookX/lookY : regard · mouth : 'smile' | 'frown' | 'open' · open : ouverture
export const EXPR = {
  happy: { brow: 0.2, mouth: 'smile' },
  surprised: { brow: 0.95, mouth: 'open', open: 1.25, lid: -0.15 },
  angry: { brow: -0.4, browAngle: 0.45, mouth: 'frown', lid: 0.3 },
  think: { brow: 0.3, browAngle: -0.2, mouth: 'frown', lookX: 0.6, lookY: 0.8 },
  serious: { brow: -0.1, browAngle: 0.25, mouth: 'smile' },
  proud: { brow: 0.35, mouth: 'smile', lid: 0.2 },
};
