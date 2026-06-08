"use client";

import { usePathname } from "next/navigation";
import { SearchCommandBar } from "@/components/ui/SearchCommandBar";

/**
 * Client wrapper around `SearchCommandBar` so the dashboard
 * server-component layout can mount it. Renders the search bar in
 * the topbar — which already shows on the (dashboard) route group
 * — and forwards a static list of pages.
 */
const DASHBOARD_PAGES: Array<{ href: string; label: string; icon: string }> = [
  { href: "/resumen", label: "Resumen", icon: "📊" },
  { href: "/biblioteca", label: "Biblioteca", icon: "📚" },
  { href: "/cerebro", label: "Cerebro", icon: "🧠" },
  { href: "/inbox", label: "Inbox", icon: "📥" },
  { href: "/productos", label: "Productos", icon: "📦" },
  { href: "/reuniones", label: "Reuniones", icon: "📅" },
  { href: "/analiticas", label: "Analíticas", icon: "📈" },
  { href: "/facturacion", label: "Facturación", icon: "💳" },
  { href: "/configuracion", label: "Configuración", icon: "⚙️" },
  { href: "/admin", label: "Admin", icon: "🛠" },
];

export const DashboardTopbarSearch = () => {
  // The trigger lives in the topbar; reading the pathname here is
  // not strictly necessary today, but keeps the door open for
  // per-page suggestions in the future.
  usePathname();
  return <SearchCommandBar pages={DASHBOARD_PAGES} />;
};
