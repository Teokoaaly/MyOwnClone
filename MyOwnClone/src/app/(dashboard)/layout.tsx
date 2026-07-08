import { ReactNode } from "react";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { Sidebar, type SidebarNavItem } from "@/components/dashboard/Sidebar";
import { SignOutButton } from "@/components/auth/SignOutButton";
import { CloneIdResolver } from "@/components/dashboard/CloneIdResolver";
import { LanguageSelector } from "@/components/ui/LanguageSelector";

export const dynamic = "force-dynamic";

export default async function DashboardLayout({
  children,
}: {
  children: ReactNode;
}) {
  const session = await auth();

  if (!session?.user) {
    redirect("/login");
  }

  const navItems: SidebarNavItem[] = [
    { href: "/resumen", label: "Overview", iconKey: "resumen", tooltip: "Overview" },
    { href: "/biblioteca", label: "Search", iconKey: "biblioteca", tooltip: "Library search", section: "playground" },
    { href: "/cerebro", label: "Crawl", iconKey: "cerebro", tooltip: "Memory crawl", section: "playground" },
    { href: "/inbox", label: "Extract", iconKey: "inbox", tooltip: "Inbox", section: "playground" },
    { href: "/productos", label: "Research", iconKey: "productos", tooltip: "Products", section: "playground" },
    { href: "/analiticas", label: "Usage", iconKey: "analiticas", tooltip: "Analytics", section: "management" },
    { href: "/planes", label: "Plans", iconKey: "facturacion", tooltip: "Plans", section: "management" },
    { href: "/facturacion", label: "Billing", iconKey: "facturacion", tooltip: "Billing", section: "management" },
    { href: "/settings", label: "Settings", iconKey: "configuracion", tooltip: "Settings", section: "management" },
    { href: "/configuracion", label: "API Keys", iconKey: "apiKeys", tooltip: "API Keys", section: "management" },
    { href: "/reuniones", label: "Team Settings", iconKey: "reuniones", tooltip: "Meetings", section: "management" },
  ];

  return (
    <div className="min-h-screen bg-[var(--bg-page)] px-3 py-3 md:px-8 md:py-8">
      <CloneIdResolver />
      <div className="app-shell mx-auto flex w-full max-w-[1720px] items-stretch overflow-hidden border border-[var(--border-soft)] md:min-h-[calc(100vh-4rem)]">
        <Sidebar
          navItems={navItems}
          user={session.user}
          signOutAction={<SignOutButton callbackUrl="/login" />}
          homeLabel="MyOwnClone"
          showSearch={false}
          showFreemiumCard
          footer={
            <div className="flex flex-col items-center gap-2">
              <LanguageSelector variant="sidebar" />
              <p className="text-[10px] text-[var(--text-muted)]">© 2026 MyOwnClone</p>
            </div>
          }
        />
        <main className="min-w-0 flex-1 bg-[var(--surface-1)] p-4 md:p-6">
          {children}
        </main>
      </div>
    </div>
  );
}
