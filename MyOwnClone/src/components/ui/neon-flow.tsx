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
        // Build URL at runtime to avoid Turbopack static analysis
        const url = ["https://cdn.jsdelivr.net/npm/threejs-components",
                     "@0.0.19/build/cursors/tubes1.min.js"].join("/");
        const module = await import(/* @vite-ignore */ url);
        if (cancelled) return;

        const TubesCursor = module.default;
        if (typeof TubesCursor !== "function") return;

        const app = TubesCursor(canvas, {
          tubes: {
            colors: ["#f967fb", "#53bc28", "#6958d5"],
            lights: {
              intensity: 200,
              colors: ["#83f36e", "#fe8a2e", "#ff008a", "#60aed5"],
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
    return new Array(count)
      .fill(0)
      .map(
        () =>
          "#" +
          Math.floor(Math.random() * 16777215)
            .toString(16)
            .padStart(6, "0")
      );
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
      style={{ background: "#0a0a0a" }}
    >
      <canvas
        ref={canvasRef}
        className="absolute inset-0 w-full h-full block"
        style={{ touchAction: "none" }}
      />
      <div className="relative z-10 w-full">{children}</div>
    </div>
  );
}

export default TubesBackground;
