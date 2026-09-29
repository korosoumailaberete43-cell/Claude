// Tonton Ferraille — mascotte 3D de CivRebar AI (Three.js), construite en formes simples façon figurine.
// Réutilisable : createTonton() rend une marionnette articulée ; setPose() et setExpression()
// la font jouer dans n'importe quelle scène. Couleurs = charte CivRebar.
import * as THREE from 'three';

export const C = {
  nuit: 0x0B1624, acier: 0x1C2B3D, cuivre: 0xC8773F, cuivreC: 0xE3A56C, signal: 0x35D0DE,
  beton: 0xB9BEC4, chaux: 0xF3F0EA, peau: 0x6E4127, peauF: 0x4E2C19, gris: 0x8E8C88, botte: 0x3A2A1E,
};

// ------------------------------------------------------------ matières
const mat = (color, o = {}) => new THREE.MeshPhysicalMaterial({ color, roughness: 0.55, metalness: 0, ...o });
const M = {
  peau: mat(C.peau, { roughness: 0.62, sheen: 0.4, sheenColor: 0x9a6040 }),
  levres: mat(C.peauF, { roughness: 0.5 }),
  chemise: mat(C.chaux, { roughness: 0.8 }),
  gilet: mat(C.cuivre, { roughness: 0.6 }),
  bande: mat(0xE8E8E4, { roughness: 0.25, metalness: 0.2, emissive: 0x404040, emissiveIntensity: 0.25 }),
  pantalon: mat(C.acier, { roughness: 0.85 }),
  botte: mat(C.botte, { roughness: 0.7 }),
  semelle: mat(0x15100c, { roughness: 0.9 }),
  casque: mat(C.nuit, { roughness: 0.4, clearcoat: 0.6, clearcoatRoughness: 0.4 }),
  blanc: mat(0xffffff, { roughness: 0.2 }),
  pupille: mat(0x120c08, { roughness: 0.15, clearcoat: 1 }),
  poil: mat(C.gris, { roughness: 0.9 }),
  plan: mat(0xE4ECF2, { roughness: 0.75 }),
  metre: mat(0xF2B42E, { roughness: 0.4, clearcoat: 0.6 }),
  noir: mat(0x1b1b1b, { roughness: 0.5 }),
  signal: new THREE.MeshStandardMaterial({ color: C.signal, emissive: C.signal, emissiveIntensity: 2.2, roughness: 0.2 }),
};

// ------------------------------------------------------------ formes
function mesh(geo, m, parent, pos = [0, 0, 0], scale = [1, 1, 1], rot = [0, 0, 0]) {
  const o = new THREE.Mesh(geo, m);
  o.position.set(...pos); o.scale.set(...scale); o.rotation.set(...rot);
  o.castShadow = true; o.receiveShadow = true;
  parent.add(o);
  return o;
}
const sph = (r, s = 48) => new THREE.SphereGeometry(r, s, s / 2 + 8);
const cap = (r, len) => new THREE.CapsuleGeometry(r, len, 12, 32);
const grp = (parent, pos = [0, 0, 0]) => { const g = new THREE.Group(); g.position.set(...pos); parent.add(g); return g; };

// Texture dessinée sur un canvas (logo, lettrage du gilet)
function canvasTex(w, h, draw) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}
// Le « R façonné » officiel (tracés du SVG de la charte)
function drawLogo(g, x, y, s, bar = '#F3F0EA') {
  g.save(); g.translate(x, y); g.scale(s, s); g.translate(-125, -135);
  g.lineWidth = 20; g.lineJoin = 'round'; g.lineCap = 'butt';
  g.strokeStyle = '#C8773F'; g.stroke(new Path2D('M120 160 L180 220 H210'));
  g.strokeStyle = bar; g.stroke(new Path2D('M50 230 V90 A50 50 0 0 1 100 40 H120 A60 60 0 0 1 120 160 H100 A20 20 0 0 1 85.86 125.86 L105.86 105.86'));
  g.fillStyle = '#35D0DE'; g.beginPath(); g.arc(100, 140, 7, 0, 7); g.fill();
  g.restore();
}
// Pièce courbe (portion de sphère) pour poser un décor sur une surface arrondie
function patch(r, phiC, phiW, thC, thW, tex, parent, pos, scale) {
  const geo = new THREE.SphereGeometry(r, 32, 16, phiC - phiW / 2, phiW, thC - thW / 2, thW);
  const m = new THREE.MeshStandardMaterial({ map: tex, transparent: true, roughness: 0.4, polygonOffset: true, polygonOffsetFactor: -4 });
  const o = new THREE.Mesh(geo, m); o.position.set(...pos); o.scale.set(...scale); parent.add(o);
  return o;
}
// Dans SphereGeometry : x = -cos(phi)·sin(θ), z = sin(phi)·sin(θ) → l'avant (+z) est à phi = π/2
const FRONT = Math.PI / 2, BACK = -Math.PI / 2;

export function createTonton() {
  const root = new THREE.Group();
  const P = {};

  // ---------------------------------------------------- jambes et bassin
  const hips = grp(root, [0, 0.8, 0]); P.hips = hips;
  for (const s of [-1, 1]) {
    const leg = grp(hips, [s * 0.16, -0.02, 0]); P[s < 0 ? 'legR' : 'legL'] = leg;
    mesh(cap(0.135, 0.42), M.pantalon, leg, [0, -0.33, 0]);
    const boot = grp(leg, [0, -0.72, 0.03]);
    mesh(new THREE.BoxGeometry(0.25, 0.14, 0.36, 4, 4, 4), M.botte, boot, [0, 0, 0.04]);
    mesh(sph(0.125), M.botte, boot, [0, 0.03, 0.14], [1, 0.75, 1]);
    mesh(new THREE.BoxGeometry(0.27, 0.04, 0.4), M.semelle, boot, [0, -0.07, 0.05]);
  }
  mesh(sph(0.3), M.pantalon, hips, [0, 0, 0], [1.25, 0.62, 1.0]);
  // ceinture + mètre ruban
  mesh(new THREE.TorusGeometry(0.34, 0.035, 12, 48), M.noir, hips, [0, 0.13, 0], [1.08, 1, 0.88], [Math.PI / 2, 0, 0]);
  const metre = grp(hips, [0.35, 0.02, 0.12]);
  mesh(new THREE.BoxGeometry(0.13, 0.13, 0.07, 3, 3, 3), M.metre, metre, [0, 0, 0], [1, 1, 1], [0, 0.5, 0]);
  mesh(new THREE.CylinderGeometry(0.035, 0.035, 0.075, 24), M.noir, metre, [0.02, 0, 0.02], [1, 1, 1], [Math.PI / 2, 0, 0.5]);

  // ---------------------------------------------------- torse, chemise, gilet
  const torso = grp(hips, [0, 0.1, 0]); P.torso = torso;
  mesh(sph(0.4), M.chemise, torso, [0, 0.36, 0], [1.08, 1.12, 0.9]);         // ventre et poitrine
  // gilet ouvert devant (on voit la chemise)
  const gilet = new THREE.SphereGeometry(0.418, 48, 24, FRONT + 0.34, Math.PI * 2 - 0.68, 0.42, 1.95);
  mesh(gilet, new THREE.MeshPhysicalMaterial({ color: C.cuivre, roughness: 0.6, side: THREE.DoubleSide }), torso, [0, 0.36, 0], [1.1, 1.13, 0.93]);
  for (const th of [1.55, 1.9]) {   // bandes réfléchissantes
    const b = new THREE.SphereGeometry(0.424, 48, 4, FRONT + 0.36, Math.PI * 2 - 0.72, th, 0.09);
    mesh(b, new THREE.MeshPhysicalMaterial({ color: 0xE8E8E4, roughness: 0.25, metalness: 0.2, emissive: 0x505050, emissiveIntensity: 0.3, side: THREE.DoubleSide }), torso, [0, 0.36, 0], [1.1, 1.13, 0.93]);
  }
  // lettrage CIVREBAR au dos, logo sur la poitrine
  const dos = canvasTex(1024, 256, (g, w, h) => {
    g.clearRect(0, 0, w, h);
    g.font = '600 150px Sora, Arial'; g.letterSpacing = '22px'; g.textAlign = 'center'; g.textBaseline = 'middle';
    g.fillStyle = '#0B1624'; g.fillText('CIVREBAR', w / 2, h / 2 + 8);
  });
  patch(0.43, BACK, 1.9, 1.22, 0.42, dos, torso, [0, 0.36, 0], [1.1, 1.13, 0.93]);
  const poitrine = canvasTex(256, 256, (g, w, h) => { g.clearRect(0, 0, w, h); g.fillStyle = '#0B1624'; g.beginPath(); g.arc(128, 128, 120, 0, 7); g.fill(); drawLogo(g, 128, 128, 0.62); });
  patch(0.43, FRONT - 0.62, 0.42, 1.2, 0.34, poitrine, torso, [0, 0.36, 0], [1.1, 1.13, 0.93]);

  // ---------------------------------------------------- bras
  for (const s of [-1, 1]) {
    const side = s < 0 ? 'R' : 'L';
    const sh = grp(torso, [s * 0.44, 0.6, 0]); P['shoulder' + side] = sh;
    mesh(sph(0.13), M.chemise, sh, [0, -0.02, 0], [1.1, 1, 1]);            // manche courte
    mesh(cap(0.1, 0.18), M.chemise, sh, [0, -0.16, 0]);
    mesh(cap(0.085, 0.16), M.peau, sh, [0, -0.3, 0]);
    const el = grp(sh, [0, -0.4, 0]); P['elbow' + side] = el;
    mesh(cap(0.08, 0.22), M.peau, el, [0, -0.13, 0]);
    const hand = grp(el, [0, -0.33, 0]); P['hand' + side] = hand;
    mesh(sph(0.1), M.peau, hand, [0, 0, 0], [1, 1.1, 0.85]);
    mesh(sph(0.045), M.peau, hand, [-s * 0.08, 0.03, 0.04], [1, 1.3, 1]);   // pouce
  }
  // plan roulé sous le bras gauche
  const plan = grp(P.elbowL, [0.02, -0.08, 0.05]); P.plan = plan;
  mesh(new THREE.CylinderGeometry(0.075, 0.075, 0.66, 32), M.plan, plan, [0, 0, 0], [1, 1, 1], [Math.PI / 2 - 0.25, 0, 0.1]);
  mesh(new THREE.CylinderGeometry(0.078, 0.078, 0.05, 32), M.gilet, plan, [0, 0, 0], [1, 1, 1], [Math.PI / 2 - 0.25, 0, 0.1]);

  // ---------------------------------------------------- tête
  const neck = grp(torso, [0, 0.72, 0]);
  mesh(new THREE.CylinderGeometry(0.12, 0.14, 0.14, 24), M.peau, neck, [0, 0.02, 0]);
  const head = grp(neck, [0, 0.42, 0]); P.head = head;
  mesh(sph(0.42), M.peau, head, [0, 0, 0], [1, 0.97, 0.96]);
  mesh(sph(0.3), M.peau, head, [0, -0.17, 0.08], [1.18, 0.8, 1.05]);        // joues et mâchoire
  for (const s of [-1, 1]) mesh(sph(0.075), M.peau, head, [s * 0.41, -0.02, 0], [0.6, 1, 0.8]);   // oreilles
  mesh(sph(0.085), M.peau, head, [0, -0.04, 0.42], [1.2, 0.95, 1]);         // nez
  for (const s of [-1, 1]) mesh(sph(0.03), M.levres, head, [s * 0.045, -0.07, 0.46]);          // narines
  // yeux
  P.eyes = [];
  for (const s of [-1, 1]) {
    const e = grp(head, [s * 0.15, 0.06, 0.34]);
    mesh(sph(0.085), M.blanc, e, [0, 0, 0], [1, 1.12, 0.7]);
    const pup = grp(e, [0, 0, 0.05]);
    mesh(sph(0.047), M.pupille, pup, [0, 0, 0], [1, 1.1, 0.6]);
    mesh(sph(0.012), new THREE.MeshBasicMaterial({ color: 0xffffff }), pup, [0.015, 0.02, 0.025]);
    // paupière (peau) : descend pour cligner ou froncer
    const lid = new THREE.Mesh(new THREE.SphereGeometry(0.09, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2), M.peau);
    lid.rotation.x = -1.35; lid.scale.set(1.02, 1.12, 0.78); e.add(lid);
    P.eyes.push({ e, pup, lid });
  }
  // sourcils, moustache, favoris gris
  P.brows = [];
  for (const s of [-1, 1]) {
    const b = grp(head, [s * 0.15, 0.2, 0.37]);
    mesh(cap(0.025, 0.12), M.poil, b, [0, 0, 0], [1, 1, 0.8], [0, 0, Math.PI / 2]);
    P.brows.push(b);
  }
  const mous = grp(head, [0, -0.13, 0.43]); P.mous = mous;
  for (const s of [-1, 1]) mesh(cap(0.034, 0.12), M.poil, mous, [s * 0.07, -0.005, 0], [1, 1, 0.8], [0, 0, s * (Math.PI / 2 - 0.38)]);
  for (const s of [-1, 1]) mesh(cap(0.03, 0.12), M.poil, head, [s * 0.39, 0.03, -0.02], [1, 1, 1], [0.15, 0, 0]);
  // bouche : sourire (arc), ouverte (disque sombre)
  const mouth = grp(head, [0, -0.25, 0.395]); P.mouth = mouth;
  P.smile = mesh(new THREE.TorusGeometry(0.075, 0.018, 12, 32, Math.PI), M.levres, mouth, [0, 0.04, 0], [1, 0.8, 1], [0, 0, Math.PI]);
  P.open = mesh(sph(0.07), new THREE.MeshStandardMaterial({ color: 0x2a0e08, roughness: 0.6 }), mouth, [0, 0.01, -0.01], [1.1, 0.8, 0.5]);
  P.open.visible = false;
  // crayon sur l'oreille droite
  const crayon = grp(head, [-0.43, 0.08, 0.05]);
  mesh(new THREE.CylinderGeometry(0.018, 0.018, 0.24, 12), M.metre, crayon, [0, 0, 0], [1, 1, 1], [Math.PI / 2 - 0.3, 0, 0.3]);

  // ---------------------------------------------------- casque avec le logo
  const casque = grp(head, [0, 0.25, -0.02]); P.casque = casque;
  mesh(new THREE.SphereGeometry(0.46, 64, 32, 0, Math.PI * 2, 0, Math.PI / 2), M.casque, casque, [0, 0, 0], [0.98, 0.8, 1.02]);
  mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.03, 64), M.casque, casque, [0, 0.005, 0.06], [1, 1, 1.12]);
  mesh(new THREE.BoxGeometry(0.07, 0.05, 0.8, 2, 2, 8), M.casque, casque, [0, 0.34, 0.02], [1, 1, 1], [0, 0, 0]);
  const logo = canvasTex(512, 512, (g, w, h) => { g.clearRect(0, 0, w, h); drawLogo(g, 256, 256, 1.55); });
  patch(0.468, FRONT, 0.9, 0.95, 0.72, logo, casque, [0, 0, 0], [0.98, 0.8, 1.02]);

  // ---------------------------------------------------- Signal, le compagnon lumineux (l'IA)
  const signal = new THREE.Group(); P.signal = signal;
  const core = new THREE.Mesh(sph(0.075, 32), M.signal); signal.add(core);
  const halo = new THREE.Sprite(new THREE.SpriteMaterial({
    map: canvasTex(128, 128, (g, w) => { const r = g.createRadialGradient(64, 64, 0, 64, 64, 64); r.addColorStop(0, 'rgba(53,208,222,0.9)'); r.addColorStop(0.35, 'rgba(53,208,222,0.35)'); r.addColorStop(1, 'rgba(53,208,222,0)'); g.fillStyle = r; g.fillRect(0, 0, w, w); }),
    blending: THREE.AdditiveBlending, depthWrite: false,
  }));
  halo.scale.set(0.55, 0.55, 1); signal.add(halo);
  const light = new THREE.PointLight(C.signal, 0.5, 1.0, 2); signal.add(light);
  signal.position.set(0.85, 2.3, 0.45);
  root.add(signal);

  // ---------------------------------------------------- pilotage
  function setPose(p = {}) {
    const d = (k, v = 0) => (p[k] == null ? v : p[k]);
    hips.rotation.y = d('turn'); torso.rotation.z = d('lean'); torso.rotation.x = d('bow');
    head.rotation.set(d('headNod'), d('headTurn'), d('headTilt'));
    P.shoulderR.rotation.set(d('rX', 0), 0, d('rZ', 0.12)); P.elbowR.rotation.x = d('rElbow', -0.1);
    P.shoulderL.rotation.set(d('lX', 0.05), 0, d('lZ', -0.18)); P.elbowL.rotation.x = d('lElbow', -1.35);
    P.legR.rotation.x = d('legR'); P.legL.rotation.x = d('legL');
    root.position.y = d('bounce');
  }
  function setExpression(x = {}) {
    const brow = x.brow || 0;          // + levés (surpris), − froncés (fâché)
    const angle = x.browAngle || 0;    // + intérieur baissé (colère)
    P.brows.forEach((b, i) => { const s = i === 0 ? -1 : 1; b.position.y = 0.2 + brow * 0.05; b.rotation.z = s * angle; });
    const lid = x.lid == null ? 0 : x.lid;   // 0 ouvert → 1 fermé
    P.eyes.forEach(({ lid: l, pup }) => { l.rotation.x = -1.35 + lid * 1.25; pup.position.x = (x.lookX || 0) * 0.025; pup.position.y = (x.lookY || 0) * 0.025; });
    const m = x.mouth || 'smile';
    P.smile.visible = m === 'smile' || m === 'frown';
    P.smile.rotation.z = m === 'frown' ? 0 : Math.PI;
    P.smile.position.y = m === 'frown' ? -0.04 : 0.04;
    P.open.visible = m === 'open';
    P.open.scale.set(1.1, 0.8 * (x.open || 1), 0.5);
    P.mous.rotation.z = (x.mousTilt || 0);
  }
  setPose(); setExpression();
  return { root, parts: P, setPose, setExpression };
}
