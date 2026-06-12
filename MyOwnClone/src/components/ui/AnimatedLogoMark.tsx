"use client";

import { useEffect, useState } from "react";
import styles from "./AnimatedLogoMark.module.css";

interface AnimatedLogoMarkProps {
  size?: number;
  cycle?: boolean;
  pulseEveryMs?: number;
}

export default function AnimatedLogoMark({
  size = 42,
  cycle = false,
  pulseEveryMs,
}: AnimatedLogoMarkProps) {
  const [pulseActive, setPulseActive] = useState(false);

  useEffect(() => {
    if (!pulseEveryMs || pulseEveryMs <= 0) return;

    const intervalId = window.setInterval(() => {
      setPulseActive(true);
      window.setTimeout(() => setPulseActive(false), 5200);
    }, pulseEveryMs);

    return () => {
      window.clearInterval(intervalId);
    };
  }, [pulseEveryMs]);

  return (
    <div
      className={`${styles.logoMark} ${cycle || pulseActive ? styles.cycle : ""}`}
      aria-label="MyOwnClone logo"
      style={{ width: size, height: size }}
    >
      <span className={`${styles.piece} ${styles.topLeft}`} />
      <span className={`${styles.piece} ${styles.topRight}`} />
      <span className={`${styles.piece} ${styles.bottomLeft}`} />
      <span className={`${styles.piece} ${styles.bottomRight}`} />
    </div>
  );
}
