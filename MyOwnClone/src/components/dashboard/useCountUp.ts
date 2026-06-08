"use client";

import { useState, useEffect } from "react";

/**
 * Animates a number from 0 → target using cubic ease-out.
 * Respects prefers-reduced-motion (returns target immediately).
 */
export function useCountUp(target: number, duration = 900): number {
  const [value, setValue] = useState(0);

  useEffect(() => {
    // Respect reduced motion
    if (typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setValue(target);
      return;
    }

    let frame = 0;
    const totalFrames = Math.max(1, Math.round(duration / 16));

    function tick() {
      frame += 1;
      const progress = Math.min(frame / totalFrames, 1);
      // Cubic ease-out: 1 - (1-t)³
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(Math.round(target * eased));
      if (progress < 1) requestAnimationFrame(tick);
    }

    tick();
  }, [target, duration]);

  return value;
}
