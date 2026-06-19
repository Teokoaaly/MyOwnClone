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
  const scriptId = useRef("tubes-script-" + Math.random().toString(36).slice(2));

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    let cancelled = false;

    // Load the script as a classic script tag (not module)  
    const existingScript = document.getElementById(scriptId.current);
    if (existingScript) {
      initTubesIfReady();
      return;
    }

    const script = document.createElement("script");
    script.id = scriptId.current;
    script.src = "https://cdn.jsdelivr.net/npm/threejs-components@0.0.19/build/cursors/tubes1.min.js";
    script.async = true;

    script.onload = () => {
      if (!cancelled) initTubesIfReady();
    };
    script.onerror = (e) => {
      console.error("TubesBackground: script load failed", e);
    };

    document.head.appendChild(script);

    function initTubesIfReady() {
      // Check various places the library might expose itself
      const TubesCursor =
        (window as any).TubesCursor ||
        (window as any).default?.TubesCursor ||
        (window as any).default;

      if (typeof TubesCursor !== "function") {
        console.warn("TubesCursor not found. Window keys with 'ube':",
          Object.keys(window).filter(k => k.toLowerCase().includes("ube")));
        return;
      }

      const container = containerRef.current;
      if (container && canvas) {
        canvas.width = container.clientWidth || window.innerWidth;
        canvas.height = container.clientHeight || window.innerHeight;
      }

      try {
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
        console.log("TubesBackground: loaded");
      } catch (err) {
        console.error("TubesBackground init error:", err);
      }
    }

    return () => {
      cancelled = true;
    };
  }, []);

  const randomColors = useCallback((count: number) => {
    const warm = ["#ea580c", "#f97316", "#c2410c", "#fbbf24", "#f59e0b", "#d97706", "#fb923c", "#fdba74"];
    return new Array(count).fill(0).map(() => warm[Math.floor(Math.random() * warm.length)]);
  }, []);

  const handleClick = () => {
    if (!enableClickInteraction || !tubesRef.current) return;
    tubesRef.current.tubes.setColors(randomColors(3));
    tubesRef.current.tubes.setLightsColors(randomColors(4));
  };

  return (
    <div ref={containerRef} className={cn("relative w-full min-h-screen overflow-hidden", className)} onClick={handleClick}>
      <canvas ref={canvasRef} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", display: "block", touchAction: "none", zIndex: 1 }} />
      <div style={{ position: "relative", zIndex: 10, width: "100%" }}>{children}</div>
    </div>
  );
}

export default TubesBackground;
