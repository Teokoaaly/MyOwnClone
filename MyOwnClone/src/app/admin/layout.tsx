import { ReactNode } from "react";
import { redirect } from "next/navigation";
import Link from "next/link";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { Sidebar } from "@/components/dashboard/Sidebar";
import { ADMIN_NAV } from "@/lib/nav-admin";

export default async function AdminLayout({
  children,
}: {
  children: ReactNode;
}) {
  const session = await auth();
  if (!session?.user) redirect("/login");

  // Confirm role in DB to avoid trusting a stale session.
  const user = await db.query.users.findFirst({
    where: eq(schema.users.email, session.user.email ?? ""),
  });
  if (user?.role !== "platform_admin") {
    redirect("/login");
  }

  const email = user.email ?? session.user.email ?? "";

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
          navItems={ADMIN_NAV}
          user={{
            name: user.name ?? session.user.name ?? "Admin",
            email,
          }}
          homeHref="/admin/resumen"
          homeLabel="MyOwnClone Admin"
          showSearch={false}
          showFreemiumCard={false}
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
                {email}
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
