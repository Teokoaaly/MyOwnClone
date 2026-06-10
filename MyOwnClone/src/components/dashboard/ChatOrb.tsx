import { type FC } from "react";

interface ChatOrbProps {
  size?: number;
}

/**
 * Esfera glassmorphic con halo multicolor pulsante.
 * MyOwnClone hero orb.
 */
export const ChatOrb: FC<ChatOrbProps> = ({ size = 56 }) => {
  return (
    <div
      className="relative inline-block"
      style={{ width: size, height: size }}
    >
      {/* Glow difuso multicolor */}
      <div
        className="absolute inset-0 rounded-full blur-2xl opacity-70 animate-pulse"
        style={{
          background:
            "conic-gradient(from 0deg, #FCA5A5, #FCD34D, #86EFAC, #93C5FD, #C4B5FD, #FCA5A5)",
        }}
      />
      {/* Esfera glassmorphic */}
      <div
        className="absolute inset-2 rounded-full"
        style={{
          background:
            "radial-gradient(circle at 30% 30%, rgba(255,255,255,0.95), rgba(255,255,255,0.6) 40%, rgba(255,255,255,0.2) 70%, transparent)",
          boxShadow:
            "inset 0 4px 12px rgba(255,255,255,0.8), 0 0 24px rgba(0,0,0,0.06)",
        }}
      />
    </div>
  );
};
