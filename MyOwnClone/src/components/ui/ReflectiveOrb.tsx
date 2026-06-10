"use client";

import styles from "./ReflectiveOrb.module.css";

interface ReflectiveOrbProps {
  size?: number;
}

export default function ReflectiveOrb({ size = 90 }: ReflectiveOrbProps) {
  return (
    <div
      className={styles.wrapper}
      style={{ width: size + 30, height: size + 30 }}
    >
      <div
        className={styles.orb}
        style={{ width: size, height: size }}
      />
    </div>
  );
}
