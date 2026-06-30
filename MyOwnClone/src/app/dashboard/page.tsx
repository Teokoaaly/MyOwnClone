import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { isPlatformAdminSession } from "@/lib/platform-admin";

export const dynamic = "force-dynamic";

export default async function DashboardAliasPage(): Promise<never> {
  const session = await auth();

  if (!session?.user) {
    redirect("/login");
  }

  redirect(isPlatformAdminSession(session) ? "/admin/resumen" : "/resumen");
}
