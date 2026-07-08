import type { SidebarNavItem } from "@/components/dashboard/Sidebar";

export const ADMIN_NAV: SidebarNavItem[] = [
  {
    href: "/admin/resumen",
    label: "Overview",
    iconKey: "resumen",
    tooltip: "Platform metrics",
    section: "platform",
  },
  {
    href: "/admin/tenants",
    label: "Tenants",
    iconKey: "productos",
    tooltip: "Manage tenants",
    section: "platform",
  },
  {
    href: "/admin/monitoring",
    label: "Monitoring",
    iconKey: "configuracion",
    tooltip: "System monitoring and ingestion status",
    section: "platform",
  },
  {
    href: "/admin/ia-modelos",
    label: "AI Models",
    iconKey: "apiKeys",
    tooltip: "Manage AI models and assignments",
    section: "platform",
  },
];
