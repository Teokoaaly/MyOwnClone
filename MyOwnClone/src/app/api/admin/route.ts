import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

// The canonical admin source-of-truth is the Flask backend; the catch-all
// proxy at /api/admin/[...path] forwards every platform_admin-gated call.
// This bare endpoint exists for backwards compatibility with any clients
// that still hit /api/admin (no path). It is a 404 by design.

export async function GET() {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }
  const user = await db.query.users.findFirst({
    where: eq(schema.users.email, session.user.email ?? ""),
  });
  if (user?.role !== "platform_admin") {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }
  return NextResponse.json(
    {
      error: "not_found",
      message:
        "Use /api/admin/<endpoint> (e.g. /api/admin/overview, /api/admin/tenants).",
    },
    { status: 404 },
  );
}
