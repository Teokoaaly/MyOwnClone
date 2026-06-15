import { ReactNode } from "react";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { CloneIdResolver } from "@/components/dashboard/CloneIdResolver";
import { SignOutButton } from "@/components/auth/SignOutButton";
import { Link } from "@/i18n/navigation";

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

  return (
    <div className="min-h-screen bg-[var(--bg-page)]">
      <CloneIdResolver />
      {/* Top bar — minimal, no box */}
      <header className="sticky top-0 z-20 flex h-14 items-center justify-between border-b border-[var(--border-soft)] bg-[var(--bg-shell)] px-4 md:px-8">
        <Link href="/resumen" className="flex items-center gap-2.5 text-sm font-semibold text-[var(--text-primary)]">
          MyOwnClone
        </Link>
        <div className="flex items-center gap-3 text-xs text-[var(--text-muted)]">
          <span className="hidden sm:inline">{session.user?.email}</span>
          <SignOutButton callbackUrl="/login" />
        </div>
      </header>
      <main className="mx-auto max-w-5xl px-4 py-8 md:px-8">
        {children}
      </main>
    </div>
  );
}
