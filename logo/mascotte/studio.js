// Studio de rendu de Tonton : scène, lumières de figurine, caméra, rendu vers image.
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { createTonton } from './tonton.js';

export function createStudio(w, h, { ground = true, ombres = 2048 } = {}) {
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(w, h);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.setClearColor(0x000000, 0);

  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.35;

  const key = new THREE.DirectionalLight(0xfff1e0, 2.4);
  key.position.set(2.2, 4.5, 3.2); key.castShadow = true;
  key.shadow.mapSize.set(ombres, ombres); key.shadow.radius = 6; key.shadow.bias = -0.0004;
  Object.assign(key.shadow.camera, { left: -2, right: 2, top: 3.2, bottom: -0.5, near: 0.5, far: 12 });
  scene.add(key);
  const rim = new THREE.DirectionalLight(0x9fe8f0, 0.8); rim.position.set(-3, 3, -3); scene.add(rim);
  const fill = new THREE.DirectionalLight(0xffd9b8, 0.5); fill.position.set(-3, 1.5, 3); scene.add(fill);

  if (ground) {
    const g = new THREE.Mesh(new THREE.CircleGeometry(3, 64), new THREE.ShadowMaterial({ opacity: 0.28 }));
    g.rotation.x = -Math.PI / 2; g.receiveShadow = true; scene.add(g);
  }

  const tonton = createTonton();
  scene.add(tonton.root);
  const camera = new THREE.PerspectiveCamera(28, w / h, 0.1, 50);

  function shot({ az = 0, el = 0.12, dist = 7.2, target = [0, 1.25, 0], fov = 28 } = {}) {
    camera.fov = fov; camera.updateProjectionMatrix();
    camera.position.set(target[0] + Math.sin(az) * Math.cos(el) * dist, target[1] + Math.sin(el) * dist, target[2] + Math.cos(az) * Math.cos(el) * dist);
    camera.lookAt(...target);
    renderer.render(scene, camera);
    return renderer.domElement.toDataURL('image/png');
  }
  return { renderer, scene, camera, tonton, shot };
}
