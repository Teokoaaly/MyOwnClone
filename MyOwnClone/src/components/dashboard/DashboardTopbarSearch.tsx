"use client";

import { SearchCommandBar } from "@/components/ui/SearchCommandBar";
import { usePathname } from "@/i18n/navigation";

/**
 * Client wrapper around `SearchCommandBar` so the dashboard
 * server-component layout can mount it. Renders the search bar in
 * the topbar — which already shows on the (dashboard) route group
 * — and forwards a static list of pages.
 */
const DASHBOARD_PAGES: Array<{ href: string; label: string; icon: string }> = [
  { href: "/resumen", label: "Overview", icon: "📊" },
  { href: "/biblioteca", label: "Library", icon: "📚" },
  { href: "/cerebro", label: "Memory", icon: "🧠" },
  { href: "/inbox", label: "Inbox", icon: "📥" },
  { href: "/productos", label: "Products", icon: "📦" },
  { href: "/reuniones", label: "Meetings", icon: "📅" },
  { href: "/analiticas", label: "Analytics", icon: "📈" },
  { href: "/facturacion", label: "Billing", icon: "💳" },
  { href: "/settings", label: "Settings", icon: "⚙️" },
  { href: "/admin", label: "Admin", icon: "🛠" },
];

export const DashboardTopbarSearch = () => {
  // The trigger lives in the topbar; reading the pathname here is
  // not strictly necessary today, but keeps the door open for
  // per-page suggestions in the future.
  usePathname();
  return <SearchCommandBar pages={DASHBOARD_PAGES} />;
};
