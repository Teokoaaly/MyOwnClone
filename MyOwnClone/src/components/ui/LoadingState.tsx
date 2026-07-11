"use client";

import type { FC, ReactNode } from "react";

interface LoadingStateProps {
  /** Optional label shown beneath the skeleton, e.g. "Loading tenants…". */
  label?: string;
  /** Number of skeleton rows to render when used as a list. */
  rows?: number;
  /** Optional extra children rendered after the skeletons. */
  children?: ReactNode;
}

export const LoadingState: FC<LoadingStateProps> = ({
  label,
  rows = 3,
  children,
}) => {
  return (
    <div
      role="status"
      aria-live="polite"
      className="card flex flex-col items-center justify-center gap-3 py-10"
    >
      <div className="flex items-center gap-1">
        <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)]" />
        <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:150ms]" />
        <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:300ms]" />
      </div>
      {label && (
        <p className="text-xs text-[var(--text-muted)]">{label}</p>
      )}
      {rows > 0 && (
        <div className="w-full max-w-md space-y-2 mt-3">
          {Array.from({ length: rows }).map((_, i) => (
            <div
              key={i}
              className="h-3 w-full rounded bg-[var(--surface-2)]"
              style={{ width: `${100 - i * 10}%` }}
            />
          ))}
        </div>
      )}
      {children}
    </div>
  );
};
