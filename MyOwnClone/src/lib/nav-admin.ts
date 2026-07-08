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
    href: "/admin/audit",
    label: "Audit log",
    iconKey: "configuracion",
    tooltip: "Sensitive actions",
    section: "platform",
  },
  {
    href: "/admin/impersonation",
    label: "Impersonation",
    iconKey: "impersonation",
    tooltip: "Impersonate users",
    section: "platform",
  },
  {
    href: "/admin/courtesy",
    label: "Courtesy",
    iconKey: "courtesy",
    tooltip: "Courtesy credits",
    section: "platform",
  },
  {
    href: "/admin/feedback",
    label: "Feedback",
    iconKey: "inbox",
    tooltip: "Feedback de usuarios",
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
