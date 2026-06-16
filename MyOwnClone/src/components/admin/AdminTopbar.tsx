"use client";

import type { FC } from "react";
import { useTranslations } from "next-intl";
import { SignOutButton } from "@/components/auth/SignOutButton";

interface AdminTopbarProps {
  /** Logged-in admin's email, shown on sm+ screens. */
  email: string;
}

/**
 * Topbar rendered at the top of every admin page inside the {@link
 * AdminShell}. Carries the breadcrumb, the admin's email and the role
 * badge. Kept presentational so it stays a server-component-friendly
 * drop-in.
 */
export const AdminTopbar: FC<AdminTopbarProps> = ({ email }) => {
  const t = useTranslations("admin.shell");
  return (
    <header
      className="flex h-[64px] shrink-0 items-center justify-between border-b px-4 md:h-[72px] md:px-6"
      style={{
        background: "var(--bg-topbar)",
        borderColor: "var(--border-soft)",
      }}
    >
      <div className="text-sm text-[var(--text-muted)]">
        {t("breadcrumbBrand")} /{" "}
        <span className="font-medium text-[var(--text-primary)]">{t("breadcrumbAdmin")}</span>
      </div>
      <div className="flex items-center gap-2">
        <span className="hidden text-xs text-[var(--text-muted)] sm:inline">
          {email}
        </span>
        <span className="badge-active">{t("adminBadge")}</span>
        <SignOutButton
          callbackUrl="/login"
          showLabel
          className="ml-1 flex items-center gap-1.5 rounded-md px-2 py-1 text-[11px] font-medium text-[var(--text-muted)] transition hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] disabled:opacity-50"
        />
      </div>
    </header>
  );
};
