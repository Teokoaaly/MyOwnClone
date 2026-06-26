import { and, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const session = await auth();
  const tenantId = session?.user?.tenantId;
  if (!session?.user || !tenantId) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id } = await params;
  const rows = await db
    .select()
    .from(schema.products)
    .innerJoin(schema.cloneConfigs, eq(schema.products.cloneId, schema.cloneConfigs.id))
    .where(and(eq(schema.products.cloneId, id), eq(schema.cloneConfigs.tenantId, tenantId)));

  return NextResponse.json(rows.map((row) => row.products));
}
