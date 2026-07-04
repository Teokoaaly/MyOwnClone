"use client";

import { type FC } from "react";
import { usePathname, useRouter } from "@/i18n/navigation";

interface AdminSwitchProps {
  /** "admin" = desde dashboard hacia admin; "dashboard" = desde admin hacia dashboard */
  target: "admin" | "dashboard";
}

/**
 * AdminSwitch — botón toggle para alternar entre dashboard y backend admin.
 *
 * SOLO visible para platform_admin (el layout lo renderiza condicionalmente).
 * NO altera la landing ni el diseño existente del dashboard.
 */
export const AdminSwitch: FC<AdminSwitchProps> = ({ target }) => {
  const router = useRouter();
  const pathname = usePathname();

  const isAdminView = pathname?.startsWith("/admin") ?? false;

  const label = target === "admin" ? "Vista Backend" : "Vista Dashboard";
  const href = target === "admin" ? "/admin/resumen" : "/resumen";
  const icon = target === "admin" ? "🛠" : "←";

  return (
    <button
      onClick={() => router.push(href)}
      className="flex w-full items-center gap-2 rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-xs font-medium text-[var(--text-secondary)] transition-colors hover:bg-[var(--surface-3)] hover:text-[var(--text-primary)]"
      aria-label={label}
    >
      <span aria-hidden="true">{icon}</span>
      <span>{label}</span>
    </button>
  );
};