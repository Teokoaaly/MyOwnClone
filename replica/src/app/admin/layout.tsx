import { ReactNode } from "react";
import Link from "next/link";
import { auth } from "@/lib/auth";
import { redirect } from "next/navigation";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

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

  const navItems = [
    { href: "/admin/resumen", label: "Resumen" },
    { href: "/admin/tenants", label: "Tenants" },
    { href: "/admin/feedback", label: "Feedback" },
  ];

  return (
    <div className="flex h-screen bg-gray-50 dark:bg-gray-950">
      <aside className="w-56 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col">
        <div className="px-5 py-4 border-b border-gray-200 dark:border-gray-800">
          <Link
            href="/admin/resumen"
            className="text-lg font-bold text-purple-600"
          >
            Admin Platform
          </Link>
        </div>
        <nav className="flex-1 px-3 py-4 space-y-1">
          {navItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="flex items-center px-3 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            >
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="px-4 py-3 border-t border-gray-200 dark:border-gray-800">
          <Link
            href="/resumen"
            className="text-sm text-gray-500 hover:text-gray-700 dark:hover:text-gray-300"
          >
            Volver al dashboard
          </Link>
        </div>
      </aside>
      <main className="flex-1 overflow-y-auto">{children}</main>
    </div>
  );
}
