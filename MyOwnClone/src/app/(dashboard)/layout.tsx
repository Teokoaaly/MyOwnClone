import { ReactNode } from "react";
import { auth } from "@/lib/auth";
import { Sidebar, type SidebarNavItem } from "@/components/dashboard/Sidebar";

export const dynamic = "force-dynamic";

export default async function DashboardLayout({
  children,
}: {
  children: ReactNode;
}) {
  const session = await auth();

  if (!session?.user) {
    return <>{children}</>;
  }

  const navItems: SidebarNavItem[] = [
    { href: "/resumen", label: "Overview", iconKey: "resumen", tooltip: "Overview" },
    { href: "/biblioteca", label: "Search", iconKey: "biblioteca", tooltip: "Library search", section: "playground" },
    { href: "/cerebro", label: "Crawl", iconKey: "cerebro", tooltip: "Memory crawl", section: "playground" },
    { href: "/inbox", label: "Extract", iconKey: "inbox", tooltip: "Inbox", section: "playground" },
    { href: "/productos", label: "Research", iconKey: "productos", tooltip: "Products", section: "playground" },
    { href: "/analiticas", label: "Usage", iconKey: "analiticas", tooltip: "Analytics", section: "management" },
    { href: "/facturacion", label: "Billing", iconKey: "facturacion", tooltip: "Billing", section: "management" },
    { href: "/configuracion", label: "API Keys", iconKey: "configuracion", tooltip: "Settings", section: "management" },
    { href: "/reuniones", label: "Team Settings", iconKey: "reuniones", tooltip: "Meetings", section: "management" },
  ];

  return (
    <div className="min-h-screen bg-[var(--bg-page)] px-3 py-3 md:px-8 md:py-8">
      <div className="app-shell mx-auto flex min-h-[calc(100vh-1.5rem)] w-full max-w-[1720px] overflow-hidden border border-white/70 md:min-h-[calc(100vh-4rem)]">
        <Sidebar
          navItems={navItems}
          user={session.user}
          homeLabel="MyOwnClone"
          showSearch={false}
          showFreemiumCard
          footer={
            <div className="space-y-3">
              <a href="/configuracion" className="block text-[var(--text-secondary)] hover:text-[var(--text-primary)]">
                Settings
              </a>
              <a href="/configuracion" className="block text-[var(--text-secondary)] hover:text-[var(--text-primary)]">
                Support
              </a>
              <p className="pt-2 text-[10px] text-[var(--text-muted)]">© 2026 MyOwnClone</p>
            </div>
          }
        />
        <main className="min-w-0 flex-1 overflow-y-auto bg-[var(--surface-1)] p-4 md:p-6">
          {children}
        </main>
      </div>
    </div>
  );
}
