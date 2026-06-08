"use client";

import type { SidebarNavItem } from "@/components/dashboard/Sidebar";
import { NavIcons } from "@/components/ui/dashboard-icons";
import { ArrowsCounterClockwise, Sparkle } from "@phosphor-icons/react";

export const ADMIN_NAV: SidebarNavItem[] = [
  {
    href: "/admin/resumen",
    label: "Overview",
    icon: NavIcons.resumen,
    tooltip: "Métricas de plataforma",
    section: "platform",
  },
  {
    href: "/admin/tenants",
    label: "Tenants",
    icon: NavIcons.productos,
    tooltip: "Gestionar tenants",
    section: "platform",
  },
  {
    href: "/admin/audit",
    label: "Audit log",
    icon: NavIcons.configuracion,
    tooltip: "Acciones sensibles",
    section: "platform",
  },
  {
    href: "/admin/impersonation",
    label: "Impersonation",
    icon: ArrowsCounterClockwise,
    tooltip: "Suplantar usuarios",
    section: "platform",
  },
  {
    href: "/admin/courtesy",
    label: "Courtesy",
    icon: Sparkle,
    tooltip: "Créditos de cortesía",
    section: "platform",
  },
  {
    href: "/admin/feedback",
    label: "Feedback",
    icon: NavIcons.inbox,
    tooltip: "Feedback de usuarios",
    section: "platform",
  },
];
