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
    href: "/admin/ia-modelos",
    label: "AI models",
    iconKey: "cerebro",
    tooltip: "Runtime assignments · Balancer · Embeddings · Costs",
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
];
