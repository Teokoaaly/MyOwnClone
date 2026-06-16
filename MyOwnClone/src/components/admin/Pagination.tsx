"use client";

import type { FC } from "react";
import { useTranslations } from "next-intl";

interface PaginationProps {
  /** Current page (1-indexed). */
  page: number;
  /** Total number of pages. */
  pages: number;
  /** Called when the user clicks "previous". */
  onPrev: () => void;
  /** Called when the user clicks "next". */
  onNext: () => void;
  /** Layout. `spread` shows "Page X of Y" on the left + buttons on the right.
   *  `compact` shows buttons + page indicator on the right. */
  layout?: "spread" | "compact";
}

const buttonClass = "btn-secondary text-xs disabled:opacity-40";

/**
 * Standard pagination control. Replaces the duplicated
 * `Previous` / `Next` blocks previously inlined in
 * admin/tenants and admin/audit pages.
 */
export const Pagination: FC<PaginationProps> = ({
  page,
  pages,
  onPrev,
  onNext,
  layout = "compact",
}) => {
  const t = useTranslations("admin.common");
  if (pages <= 1) return null;

  const buttons = (
    <div className="flex items-center gap-2 text-xs text-[var(--text-muted)]">
      <button
        type="button"
        disabled={page <= 1}
        onClick={onPrev}
        className={buttonClass}
      >
        {t("previous")}
      </button>
      <span>
        {t("pageXofY", { page, pages })}
      </span>
      <button
        type="button"
        disabled={page >= pages}
        onClick={onNext}
        className={buttonClass}
      >
        {t("next")}
      </button>
    </div>
  );

  if (layout === "spread") {
    return (
      <div className="flex items-center justify-between text-xs text-[var(--text-muted)]">
        <span>
          {t("pageOf", { page, pages })}
        </span>
        {buttons}
      </div>
    );
  }

  return <div className="flex justify-end">{buttons}</div>;
};
