"use client";

import React, { useEffect, useRef, useCallback } from "react";

interface TubesBackgroundProps {
  children?: React.ReactNode;
  className?: string;
  enableClickInteraction?: boolean;
}

function cn(...classes: (string | undefined | null | false)[]): string {
  return classes.filter(Boolean).join(" ");
}

export function TubesBackground({
  children,
  className,
  enableClickInteraction = true,
}: TubesBackgroundProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const tubesRef = useRef<any>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    let cancelled = false;

    const init = async () => {
      try {
        const url = ["https://cdn.jsdelivr.net/npm/threejs-components",
                     "@0.0.19/build/cursors/tubes1.min.js"].join("/");
        const module = await import(/* @vite-ignore */ url);
        if (cancelled) return;

        const TubesCursor = module.default;
        if (typeof TubesCursor !== "function") return;

        const app = TubesCursor(canvas, {
          tubes: {
            colors: ["#ea580c", "#f97316", "#c2410c"],
            lights: {
              intensity: 80,
              colors: ["#fbbf24", "#f59e0b", "#ea580c", "#fdba74"],
            },
          },
        });
        tubesRef.current = app;
      } catch (err) {
        console.warn("TubesBackground: failed to load", err);
      }
    };

    init();
    return () => {
      cancelled = true;
    };
  }, []);

  const randomColors = useCallback((count: number) => {
    // Warm palette that matches #e8e2dd
    const warm = ["#ea580c", "#f97316", "#c2410c", "#fbbf24", "#f59e0b", "#d97706", "#fb923c", "#fdba74"];
    return new Array(count)
      .fill(0)
      .map(() => warm[Math.floor(Math.random() * warm.length)]);
  }, []);

  const handleClick = () => {
    if (!enableClickInteraction || !tubesRef.current) return;
    tubesRef.current.tubes.setColors(randomColors(3));
    tubesRef.current.tubes.setLightsColors(randomColors(4));
  };

  return (
    <div
      className={cn("relative w-full min-h-screen overflow-hidden z-0", className)}
      onClick={handleClick}
      style={{ background: "transparent" }}
    >
      <canvas
        ref={canvasRef}
        className="absolute inset-0 w-full h-full block pointer-events-none"
        style={{ touchAction: "none", opacity: 0.35, mixBlendMode: "multiply" as any }}
      />
      <div className="relative z-10 w-full">{children}</div>
    </div>
  );
}

export default TubesBackground;
