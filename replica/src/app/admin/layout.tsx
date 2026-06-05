import { ReactNode } from "react";
import Link from "next/link";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

const NAV_ITEMS = [
  { href: "/admin/resumen", label: "Resumen" },
  { href: "/admin/tenants", label: "Tenants" },
  { href: "/admin/feedback", label: "Feedback" },
];

export default async function AdminLayout({
  children,
}: {
  children: ReactNode;
}) {
  const session = await auth();
  if (!session?.user) redirect("/login");

  const user = await db.query.users.findFirst({
    where: eq(schema.users.email, session.user.email!),
  });
  if (user?.role !== "platform_admin") {
    redirect("/login");
  }

  return (
    <div
      className="min-h-screen p-3 md:p-6"
      style={{
        background: `
          radial-gradient(circle at 8% 8%, rgba(249, 115, 22, 0.22), transparent 34%),
          radial-gradient(circle at 90% 85%, rgba(236, 72, 153, 0.16), transparent 34%),
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
        <aside
          className="hidden md:flex w-[220px] shrink-0 flex-col border-r p-5"
          style={{
            background: "var(--bg-sidebar)",
            borderColor: "var(--border-soft)",
          }}
        >
          <Link href="/admin/resumen" className="text-lg font-semibold tracking-wide text-[var(--text-primary)]">
            MyOwnClone
          </Link>
          <div className="mt-1 text-[10px] uppercase tracking-widest text-[var(--text-muted)]">
            Platform Admin
          </div>

          <nav className="mt-8 space-y-1">
            {NAV_ITEMS.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="flex h-11 items-center rounded-lg px-3 text-sm text-[var(--text-secondary)] transition hover:bg-[rgba(15,23,42,0.04)] hover:text-[var(--text-primary)]"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          <div className="mt-auto pt-6">
            <Link
              href="/resumen"
              className="text-xs text-[var(--text-muted)] hover:text-[var(--text-primary)]"
            >
              ← Volver al dashboard
            </Link>
          </div>
        </aside>

        <div className="flex min-w-0 flex-1 flex-col">
          <header
            className="flex h-[64px] shrink-0 items-center justify-between border-b px-4 md:h-[72px] md:px-6"
            style={{
              background: "var(--bg-topbar)",
              borderColor: "var(--border-soft)",
            }}
          >
            <div className="text-sm text-[var(--text-muted)]">
              MyOwnClone /{" "}
              <span className="font-medium text-[var(--text-primary)]">Admin</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="hidden text-xs text-[var(--text-muted)] sm:inline">
                {user.email}
              </span>
              <span className="badge-active">Admin</span>
            </div>
          </header>

          <main className="min-w-0 flex-1 overflow-y-auto p-4 md:p-6">
            {children}
          </main>
        </div>
      </div>
    </div>
  );
}
