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
  const containerRef = useRef<HTMLDivElement>(null);

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
        if (typeof TubesCursor !== "function") {
          console.warn("TubesCursor not found, got:", typeof module.default, Object.keys(module));
          return;
        }

        // Ensure canvas has proper size before init
        const container = containerRef.current;
        if (container) {
          canvas.width = container.clientWidth;
          canvas.height = container.clientHeight;
        }

        const app = TubesCursor(canvas, {
          tubes: {
            colors: ["#ea580c", "#f97316", "#c2410c"],
            lights: {
              intensity: 200,
              colors: ["#fbbf24", "#f59e0b", "#ea580c", "#fdba74"],
            },
          },
        });
        tubesRef.current = app;
        console.log("TubesBackground: loaded successfully");
      } catch (err) {
        console.error("TubesBackground load error:", err);
      }
    };

    init();
    return () => {
      cancelled = true;
    };
  }, []);

  const randomColors = useCallback((count: number) => {
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
      ref={containerRef}
      className={cn("relative w-full min-h-screen overflow-hidden", className)}
      onClick={handleClick}
    >
      <canvas
        ref={canvasRef}
        style={{
          position: "absolute",
          inset: 0,
          width: "100%",
          height: "100%",
          display: "block",
          touchAction: "none",
          zIndex: 1,
        }}
      />
      <div style={{ position: "relative", zIndex: 10, width: "100%" }}>
        {children}
      </div>
    </div>
  );
}

export default TubesBackground;
