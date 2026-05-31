import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

export async function GET() {
  const session = await auth();

  if (!session?.user) {
    return NextResponse.json({ error: "No autorizado" }, { status: 401 });
  }

  const user = await db.query.users.findFirst({
    where: eq(schema.users.email, session.user.email!),
  });

  if (user?.role !== "platform_admin") {
    return NextResponse.json(
      { error: "Acceso denegado" },
      { status: 403 }
    );
  }

  const tenants = await db.query.tenants.findMany();
  return NextResponse.json({ tenants });
}
