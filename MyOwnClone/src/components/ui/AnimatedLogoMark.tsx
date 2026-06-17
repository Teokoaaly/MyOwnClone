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
  const sizeClass =
    size <= 20
      ? styles.size20
      : size <= 22
        ? styles.size22
        : size <= 24
          ? styles.size24
          : size <= 26
            ? styles.size26
            : size <= 40
              ? styles.size40
              : styles.size42;

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
      className={`${styles.logoMark} ${sizeClass} ${cycle || pulseActive ? styles.cycle : ""}`}
      aria-label="MyOwnClone logo"
    >
      <span className={`${styles.piece} ${styles.topLeft}`} />
      <span className={`${styles.piece} ${styles.topRight}`} />
      <span className={`${styles.piece} ${styles.bottomLeft}`} />
      <span className={`${styles.piece} ${styles.bottomRight}`} />
    </div>
  );
}
