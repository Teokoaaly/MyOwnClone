"use client";

import { useCountUp } from "./useCountUp";
import type { IconProps } from "@phosphor-icons/react";
import { type FC } from "react";

interface StatsCardProps {
  icon: React.ComponentType<IconProps>;
  label: string;
  value: number;
  suffix?: string;
  emptyLabel?: string;
}

export const StatsCard: FC<StatsCardProps> = ({
  icon: Icon,
  label,
  value,
  suffix = "",
  emptyLabel,
}) => {
  const animated = useCountUp(value);
  const isEmpty = value === 0;

  return (
    <div className="card transition-all duration-180 hover:shadow-md">
      {/* Icon */}
      <div className={`mb-3 ${isEmpty ? "text-[var(--text-muted)]" : "text-[var(--color-accent-warm)]"}`}>
        <Icon className="h-6 w-6" weight="duotone" />
      </div>

      {/* Value */}
      <p className="stat-value">
        <span className="font-mono">{isEmpty ? 0 : animated}</span>
        <span className="text-lg text-[var(--text-muted)] ml-0.5">{suffix}</span>
      </p>

      {/* Label */}
      <p className="stat-label mt-1">{label}</p>

      {/* Empty state */}
      {isEmpty && emptyLabel && (
        <p className="mt-2 text-xs text-[var(--text-muted)]">{emptyLabel}</p>
      )}
    </div>
  );
};