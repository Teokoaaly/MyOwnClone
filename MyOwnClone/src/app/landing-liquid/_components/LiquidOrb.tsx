import styles from "../page.module.css";

export function LiquidOrb() {
  return (
    <svg
      aria-hidden="true"
      className={styles.orb}
      data-testid="liquid-orb"
      fill="none"
      focusable="false"
      viewBox="0 0 640 640"
    >
      <defs>
        <radialGradient id="orbCore" cx="36%" cy="26%" r="74%">
          <stop stopColor="#FFFFFF" stopOpacity="0.92" />
          <stop offset="0.2" stopColor="#A8D7FF" stopOpacity="0.9" />
          <stop offset="0.56" stopColor="#319AFF" stopOpacity="0.82" />
          <stop offset="1" stopColor="#0069D9" stopOpacity="0.3" />
        </radialGradient>
        <linearGradient id="orbRing" x1="84" x2="536" y1="80" y2="558">
          <stop stopColor="#FFFFFF" stopOpacity="0.9" />
          <stop offset="0.46" stopColor="#60B1FF" stopOpacity="0.14" />
          <stop offset="1" stopColor="#FFFFFF" stopOpacity="0.54" />
        </linearGradient>
        <filter id="orbBlur" height="160%" width="160%" x="-30%" y="-30%">
          <feGaussianBlur stdDeviation="18" />
        </filter>
      </defs>
      <circle cx="320" cy="320" fill="#60B1FF" filter="url(#orbBlur)" opacity="0.44" r="238" />
      <circle cx="320" cy="320" fill="url(#orbCore)" r="214" />
      <circle cx="320" cy="320" r="204" stroke="url(#orbRing)" strokeWidth="8" />
      <ellipse cx="262" cy="211" fill="#FFFFFF" opacity="0.58" rx="88" ry="44" transform="rotate(-32 262 211)" />
      <path d="M121 374c69 80 189 119 308 80 49-16 87-45 117-81" stroke="#FFFFFF" strokeLinecap="round" strokeOpacity="0.42" strokeWidth="18" />
    </svg>
  );
}
