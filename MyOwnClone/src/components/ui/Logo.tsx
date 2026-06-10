import AnimatedLogoMark from "./AnimatedLogoMark";

interface LogoProps {
  size?: number;
  showText?: boolean;
  className?: string;
}

export default function Logo({ size = 26, showText = true, className = "" }: LogoProps) {
  return (
    <div
      className={className}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: size > 20 ? "10px" : "6px",
      }}
    >
      <div style={{ width: size, height: size }}>
        <AnimatedLogoMark />
      </div>
      {showText && (
        <span
          style={{
            fontSize: Math.max(size * 0.88, 14),
            fontWeight: 700,
            letterSpacing: "-0.04em",
          }}
        >
          MyOwnClone
        </span>
      )}
    </div>
  );
}
