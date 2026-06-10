import { type FC } from "react";
import ReflectiveOrb from "@/components/ui/ReflectiveOrb";

interface ChatOrbProps {
  size?: number;
}

/**
 * Esfera glassmorphic con halo multicolor pulsante y reflejos animados.
 * MyOwnClone hero orb — versión animada con CSS.
 */
export const ChatOrb: FC<ChatOrbProps> = ({ size = 56 }) => {
  return <ReflectiveOrb size={size} />;
};
