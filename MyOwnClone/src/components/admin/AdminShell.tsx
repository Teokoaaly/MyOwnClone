"use client";

import { type FC, type ReactNode } from "react";
import { Sidebar, type SidebarNavItem } from "@/components/dashboard/Sidebar";
import { NavIcons } from "@/components/ui/dashboard-icons";
import Link from "next/link";

const adminNavItems: SidebarNavItem[] = [
  {
    href: "/admin/resumen",
    label: "Overview",
    icon: NavIcons.resumen,
    tooltip: "Platform metrics",
    section: "platform",
  },
  {
    href: "/admin/tenants",
    label: "Tenants",
    icon: NavIcons.productos,
    tooltip: "Manage tenant accounts",
    section: "platform",
  },
  {
    href: "/admin/feedback",
    label: "Feedback",
    icon: NavIcons.inbox,
    tooltip: "User feedback across the platform",
    section: "platform",
  },
  {
    href: "/admin/audit",
    label: "Audit log",
    icon: NavIcons.configuracion,
    tooltip: "Sensitive admin actions",
    section: "platform",
  },
];

interface AdminShellProps {
  user?: { name?: string | null; email?: string | null };
  children: ReactNode;
}

export const AdminShell: FC<AdminShellProps> = ({ user, children }) => {
  return (
    <div
      className="min-h-screen p-3 md:p-6"
      style={{
        background: `
          radial-gradient(circle at 8% 8%, rgba(249, 115, 22, 0.18), transparent 34%),
          radial-gradient(circle at 90% 85%, rgba(236, 72, 153, 0.14), transparent 34%),
          linear-gradient(135deg, #E7E1DE 0%, #D6D0CD 100%)
        `,
      }}
    >
      <div
        className="mx-auto flex max-w-[1680px] overflow-hidden rounded-[18px] border md:rounded-[22px] md:min-h-[calc(100vh-48px)]"
        style={{
          background: "var(--bg-shell)",
          borderColor: "rgba(15,23,42,0.10)",
          boxShadow: "0 40px 120px rgba(15,23,42,0.18)",
          minHeight: "calc(100vh - 24px)",
        }}
      >
        <Sidebar
          navItems={adminNavItems}
          homeHref="/admin/resumen"
          homeLabel="MyOwnClone Admin"
          showSearch={false}
          showFreemiumCard={false}
          showUserBlock={!!user}
          user={user}
          footer={
            <Link
              href="/resumen"
              className="hover:text-[var(--text-primary)] transition-colors"
            >
              ← Volver al dashboard
            </Link>
          }
        />

        <div className="flex min-w-0 flex-1 flex-col">
          {children}
        </div>
      </div>
    </div>
  );
};
