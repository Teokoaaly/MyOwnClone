import styles from "./AnimatedLogoMark.module.css";

interface AnimatedLogoMarkProps {
  size?: number;
  cycle?: boolean;
}

export default function AnimatedLogoMark({ size = 42, cycle = false }: AnimatedLogoMarkProps) {
  return (
    <div
      className={`${styles.logoMark} ${cycle ? styles.cycle : ""}`}
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
