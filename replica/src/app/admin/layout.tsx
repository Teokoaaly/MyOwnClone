import { ReactNode } from "react";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { AdminShell } from "@/components/admin/AdminShell";
import { AdminTopbar } from "@/components/admin/AdminTopbar";

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
    <AdminShell
      user={{
        name: user.name ?? session.user.name ?? "Admin",
        email,
      }}
    >
      <AdminTopbar email={email} />
      <main className="min-w-0 flex-1 overflow-y-auto p-4 md:p-6">
        {children}
      </main>
    </AdminShell>
  );
}
