"use client";

import type { FC, ReactNode } from "react";

interface PageHeaderProps {
  /** Page title rendered as h1. */
  title: string;
  /** Optional subtitle / description under the title. */
  subtitle?: ReactNode;
  /** Optional right-aligned slot for actions, badges, or counters. */
  actions?: ReactNode;
  /** Layout mode. `split` puts actions on the right (md+); `stack` stacks everything vertically. */
  layout?: "split" | "stack";
}

const layoutClasses: Record<NonNullable<PageHeaderProps["layout"]>, string> = {
  split:
    "flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between",
  stack: "space-y-2",
};

/**
 * Standard page header used across admin pages. Replaces the
 * `<header><h1>…</h1><p>…</p></header>` block previously duplicated in
 * every admin page.
 */
export const PageHeader: FC<PageHeaderProps> = ({
  title,
  subtitle,
  actions,
  layout = "split",
}) => {
  return (
    <header className={layoutClasses[layout]}>
      <div>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          {title}
        </h1>
        {subtitle && (
          <p className="mt-1 text-sm text-[var(--text-muted)]">{subtitle}</p>
        )}
      </div>
      {actions && <div className="flex flex-wrap items-center gap-2">{actions}</div>}
    </header>
  );
};
