"use client";

import React, { useEffect, useRef, useState, useCallback } from "react";
import { cn } from "@/lib/utils";

const CDN_URL = "https://cdn.jsdelivr.net/npm/threejs-components@0.0.19/build/cursors/tubes1.min.js";

interface TubesBackgroundProps {
  children?: React.ReactNode;
  className?: string;
  enableClickInteraction?: boolean;
}

export function TubesBackground({
  children,
  className,
  enableClickInteraction = true,
}: TubesBackgroundProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const tubesRef = useRef<any>(null);

  useEffect(() => {
    let mounted = true;
    const canvas = canvasRef.current;
    if (!canvas) return;

    // Use Function constructor to avoid Next.js static analysis
    const dynamicImport = new Function("url", "return import(url)");

    dynamicImport(CDN_URL)
      .then((module: any) => {
        if (!mounted) return;
        const TubesCursor = module.default || module;
        if (typeof TubesCursor !== "function") {
          console.warn("TubesCursor not a function:", typeof TubesCursor);
          return;
        }
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
      })
      .catch((error: any) => {
        console.error("Failed to load TubesCursor:", error);
      });

    return () => {
      mounted = false;
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
    const colors = randomColors(3);
    const lightsColors = randomColors(4);
    tubesRef.current.tubes.setColors(colors);
    tubesRef.current.tubes.setLightsColors(lightsColors);
  };

  return (
    <div
      className={cn("relative w-full min-h-screen overflow-hidden", className)}
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
