"use client";

/**
 * NeonTubesBackground — animated neon "tubes" background (three.js, r184).
 *
 * Replaces the previous WebGL ShaderBackground on the landing page.
 * Slot-in compatible: renders a <canvas> with the exact same layer classes
 * the old background used, so the existing `.moc-local-landing canvas`
 * tinting rule (src/app/page.tsx) keeps applying automatically.
 *
 * Effect (proprietary reimplementation; NOT threejs-components, whose
 * tubes1 effect is CC BY-NC-SA 4.0 / NonCommercial):
 *   - A handful of glowing tubes following animated CatmullRom curves
 *     (organic plasma-like motion via layered sines/cosines).
 *   - Colored point lights drifting through the scene.
 *   - "Glow" achieved with additive-blended tube geometry so the neon
 *     halo reads without a post-processing composer (which would break
 *     the transparent background the landing relies on).
 *   - Subtle parallax: lights ease toward the pointer position.
 *
 * Honours `prefers-reduced-motion` (renders a single static frame, no RAF).
 */

import { useEffect, useRef } from "react";
import * as THREE from "three";

// ---- Tunable palette (edit freely; no other landing changes required) ----
const TUBE_COLORS = ["#f967fb", "#53bc28", "#6958d5", "#33c9ff"];
const LIGHT_COLORS = ["#83f36e", "#fe8a2e", "#ff008a", "#60aed5"];
const TUBE_COUNT = TUBE_COLORS.length; // one tube per color
const CURVE_POINTS = 24; // control points along each tube path
const TUBE_SEGMENTS = 200; // geometry resolution along the path
const TUBE_RADIAL = 12; // geometry resolution around the tube
const TUBE_RADIUS = 0.14; // base tube radius
const CURSOR_PARALLAX = 0.9; // how strongly lights follow the pointer (0..1)

type Tube = {
  curve: THREE.CatmullRomCurve3;
  core: THREE.Mesh<THREE.TubeGeometry, THREE.MeshBasicMaterial>;
  glow: THREE.Mesh<THREE.TubeGeometry, THREE.MeshBasicMaterial>;
  seeds: { py: number; pz: number; fy: number; fz: number; ph: number };
};

function makeTubeMaterial(color: THREE.Color, opacity: number): THREE.MeshBasicMaterial {
  return new THREE.MeshBasicMaterial({
    color,
    transparent: true,
    opacity,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
}

function buildTube(hex: string, index: number): Tube {
  const color = new THREE.Color(hex);
  const points: THREE.Vector3[] = [];
  for (let i = 0; i < CURVE_POINTS; i++) {
    const t = i / (CURVE_POINTS - 1);
    const x = (t - 0.5) * 22;
    const y = Math.sin(t * Math.PI * 2 + index) * 2.5;
    const z = (index - TUBE_COUNT / 2) * 3 + Math.cos(t * Math.PI * 2) * 1.5;
    points.push(new THREE.Vector3(x, y, z));
  }
  const curve = new THREE.CatmullRomCurve3(points, false, "catmullrom", 0.5);

  // Bright thin core + soft fat glow, both additive → neon look without bloom.
  const coreGeom = new THREE.TubeGeometry(curve, TUBE_SEGMENTS, TUBE_RADIUS * 0.55, TUBE_RADIAL, false);
  const glowGeom = new THREE.TubeGeometry(curve, TUBE_SEGMENTS, TUBE_RADIUS * 2.4, TUBE_RADIAL, false);

  const core = new THREE.Mesh(coreGeom, makeTubeMaterial(color.clone().multiplyScalar(2.2), 0.95));
  const glow = new THREE.Mesh(glowGeom, makeTubeMaterial(color.clone(), 0.22));

  const seeds = {
    py: 0.31 + index * 0.17,
    pz: 0.19 + index * 0.11,
    fy: 0.27 + index * 0.05,
    fz: 0.21 + index * 0.06,
    ph: index * 1.7,
  };
  return { curve, core, glow, seeds };
}

function rebuildTubeGeometry(tube: Tube) {
  tube.core.geometry.dispose();
  tube.core.geometry = new THREE.TubeGeometry(tube.curve, TUBE_SEGMENTS, TUBE_RADIUS * 0.55, TUBE_RADIAL, false);
  tube.glow.geometry.dispose();
  tube.glow.geometry = new THREE.TubeGeometry(tube.curve, TUBE_SEGMENTS, TUBE_RADIUS * 2.4, TUBE_RADIAL, false);
}

const NeonTubesBackground = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    // Feature-detect WebGL without claiming the context ourselves;
    // three.js must create the context with its own flags.
    const testGl = document.createElement("canvas").getContext("webgl2") ||
      document.createElement("canvas").getContext("webgl");
    if (!testGl) {
      console.warn("NeonTubesBackground: WebGL not supported.");
      return;
    }

    const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // ---- Renderer (transparent so the landing base shows through) ----
    const renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
      powerPreference: "high-performance",
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setClearColor(0x000000, 0); // fully transparent

    // ---- Scene & camera ----
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(55, 1, 0.1, 100);
    camera.position.set(0, 0, 14);

    // ---- Tubes ----
    const tubes: Tube[] = [];
    for (let i = 0; i < TUBE_COUNT; i++) {
      const tube = buildTube(TUBE_COLORS[i % TUBE_COLORS.length], i);
      scene.add(tube.glow); // glow behind core
      scene.add(tube.core);
      tubes.push(tube);
    }

    // ---- Colored point lights (for any future PBR; basic mats are self-lit) ----
    const lights = LIGHT_COLORS.map((c, i) => {
      const light = new THREE.PointLight(new THREE.Color(c), 40, 60, 1.6);
      light.position.set((i - 1.5) * 6, (i % 2 === 0 ? 1 : -1) * 3, 4);
      scene.add(light);
      return light;
    });

    // ---- Pointer parallax ----
    const pointer = new THREE.Vector2(0, 0);
    const target = new THREE.Vector2(0, 0);
    const onPointerMove = (e: PointerEvent) => {
      target.x = (e.clientX / window.innerWidth) * 2 - 1;
      target.y = -((e.clientY / window.innerHeight) * 2 - 1);
    };
    window.addEventListener("pointermove", onPointerMove, { passive: true });

    // ---- Resize (sets renderer + drawing buffer to real viewport size) ----
    const resize = () => {
      const w = window.innerWidth;
      const h = window.innerHeight;
      renderer.setSize(w, h, false); // false: don't override CSS size
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    };
    window.addEventListener("resize", resize);
    resize(); // ensure non-zero size before first frame

    // ---- Animation ----
    const clock = new THREE.Clock();
    let rafId = 0;

    const animateTube = (tube: Tube, time: number) => {
      const { curve, seeds } = tube;
      const pts = curve.points;
      const n = pts.length;
      for (let i = 0; i < n; i++) {
        const t = i / (n - 1);
        const wx = t * Math.PI * 2;
        pts[i].x = (t - 0.5) * 22;
        pts[i].y =
          Math.sin(wx * seeds.fy + time * seeds.py + seeds.ph) * 3.0 +
          Math.sin(wx * seeds.fy * 0.5 + time * 0.4) * 1.2;
        pts[i].z = Math.cos(wx * seeds.fz + time * seeds.pz + seeds.ph) * 2.2;
      }
      rebuildTubeGeometry(tube);
    };

    const renderFrame = () => {
      const time = clock.getElapsedTime();

      pointer.x += (target.x - pointer.x) * 0.05;
      pointer.y += (target.y - pointer.y) * 0.05;

      camera.position.x += (pointer.x * 2.2 - camera.position.x) * 0.04;
      camera.position.y += (pointer.y * 1.6 - camera.position.y) * 0.04;
      camera.lookAt(scene.position);

      lights.forEach((light, i) => {
        const phase = time * 0.3 + i * 1.3;
        light.position.x = Math.cos(phase) * 7 + pointer.x * CURSOR_PARALLAX * 3;
        light.position.y = Math.sin(phase * 1.1) * 4 + pointer.y * CURSOR_PARALLAX * 3;
        light.position.z = 4 + Math.sin(phase * 0.7) * 2;
      });

      for (const tube of tubes) animateTube(tube, time);

      renderer.render(scene, camera);
    };

    if (prefersReduced) {
      renderFrame();
    } else {
      const loop = () => {
        renderFrame();
        rafId = window.requestAnimationFrame(loop);
      };
      rafId = window.requestAnimationFrame(loop);
    }

    // ---- Cleanup (no GPU leaks) ----
    return () => {
      window.cancelAnimationFrame(rafId);
      window.removeEventListener("resize", resize);
      window.removeEventListener("pointermove", onPointerMove);
      for (const tube of tubes) {
        tube.core.geometry.dispose();
        tube.core.material.dispose();
        tube.glow.geometry.dispose();
        tube.glow.material.dispose();
      }
      renderer.dispose();
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="pointer-events-none fixed inset-0 z-0 h-full w-full"
      aria-hidden="true"
    />
  );
};

export default NeonTubesBackground;
