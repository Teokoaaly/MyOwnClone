import { ReactNode } from "react";
import Link from "next/link";
import { auth } from "@/lib/auth";
import { NavIcons } from "@/components/ui/dashboard-icons";
import { DashboardTopbarSearch } from "@/components/dashboard/DashboardTopbarSearch";

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

  const navItems = [
    { href: "/resumen", label: "Overview", icon: NavIcons.resumen },
    { href: "/biblioteca", label: "Library", icon: NavIcons.biblioteca },
    { href: "/cerebro", label: "Memory", icon: NavIcons.cerebro },
    { href: "/inbox", label: "Inbox", icon: NavIcons.inbox },
    { href: "/productos", label: "Products", icon: NavIcons.productos },
    { href: "/reuniones", label: "Meetings", icon: NavIcons.reuniones },
    { href: "/analiticas", label: "Analytics", icon: NavIcons.analiticas },
    { href: "/facturacion", label: "Billing", icon: NavIcons.facturacion },
    { href: "/configuracion", label: "Settings", icon: NavIcons.configuracion },
  ];

  return (
    <div
      className="flex min-h-screen"
      style={{
        background: `
          radial-gradient(circle at 8% 8%, rgba(245, 220, 200, 0.55), transparent 42%),
          radial-gradient(circle at 92% 88%, rgba(220, 200, 230, 0.45), transparent 42%),
          var(--bg-page)
        `,
      }}
    >
      <aside
        className="hidden md:flex w-64 flex-col border-r border-[var(--border-soft)] bg-[var(--bg-shell)]"
        style={{ minHeight: "100vh" }}
      >
        <div className="flex items-center gap-3 px-6 py-5 border-b border-[var(--border-soft)]">
          <div className="h-8 w-8 rounded-lg bg-black flex items-center justify-center text-white text-sm font-bold">
            M
          </div>
          <span className="text-lg font-semibold text-[var(--text-primary)]">
            MyOwnClone
          </span>
        </div>
        <nav className="flex-1 overflow-y-auto px-3 py-4">
          <div className="space-y-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className="flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium text-[var(--text-secondary)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] transition-colors"
                >
                  <Icon
                    className="h-5 w-5 shrink-0"
                    weight="duotone"
                  />
                  {item.label}
                </Link>
              );
            })}
          </div>
        </nav>
        <div className="border-t border-[var(--border-soft)] px-4 py-4">
          <div className="flex items-center gap-3">
            <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-[var(--color-accent-warm)] text-white text-sm font-bold">
              {session.user.name?.charAt(0) ?? "U"}
            </div>
            <div className="flex-1 min-w-0">
              <p className="truncate text-sm font-medium text-[var(--text-primary)]">
                {session.user.name}
              </p>
              <p className="truncate text-xs text-[var(--text-muted)]">
                {session.user.email}
              </p>
            </div>
          </div>
        </div>
      </aside>

      <div className="flex-1 min-w-0">
        <header
          className="flex h-[56px] shrink-0 items-center justify-between border-b border-[var(--border-soft)] bg-[var(--bg-topbar)] px-4 md:h-[72px] md:px-6"
        >
          <div className="text-sm text-[var(--text-muted)]">
            MyOwnClone / Dashboard
          </div>
          <div className="flex items-center gap-3">
            <DashboardTopbarSearch />
            <Link
              href="/configuracion"
              className="btn-secondary text-xs"
            >
              Settings
            </Link>
          </div>
        </header>
        <main className="min-w-0 flex-1 overflow-y-auto p-4 md:p-6">
          {children}
        </main>
      </div>
    </div>
  );
}
