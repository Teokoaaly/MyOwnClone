"use client";

import { type FC } from "react";
import { useTheme } from "./ThemeProvider";

interface ThemeToggleProps {
  /** Show label next to the icon. Defaults to false (icon only). */
  showLabel?: boolean;
}

export const ThemeToggle: FC<ThemeToggleProps> = ({ showLabel = false }) => {
  const { theme, toggle } = useTheme();
  const isDark = theme === "dark";

  return (
    <button
      type="button"
      onClick={toggle}
      aria-label={isDark ? "Cambiar a modo claro" : "Cambiar a modo oscuro"}
      title={isDark ? "Modo claro" : "Modo oscuro"}
      className={
        showLabel
          ? "btn-secondary text-xs"
          : "h-8 w-8 rounded-md flex items-center justify-center text-[var(--text-muted)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] transition-colors"
      }
    >
      {isDark ? (
        <svg
          className="h-4 w-4"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth={2}
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <circle cx="12" cy="12" r="4" />
          <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41" />
        </svg>
      ) : (
        <svg
          className="h-4 w-4"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth={2}
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
        </svg>
      )}
      {showLabel && <span>{isDark ? "Claro" : "Oscuro"}</span>}
    </button>
  );
};
