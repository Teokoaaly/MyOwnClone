import { and, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";

export async function GET() {
  const session = await auth();
  const tenantId = session?.user?.tenantId;
  if (!session?.user || !tenantId) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const clones = await db
    .select({
      id: schema.cloneConfigs.id,
      name: schema.cloneConfigs.name,
      slug: schema.cloneConfigs.slug,
      isActive: schema.cloneConfigs.isActive,
      createdAt: schema.cloneConfigs.createdAt,
    })
    .from(schema.cloneConfigs)
    .where(and(eq(schema.cloneConfigs.tenantId, tenantId), eq(schema.cloneConfigs.isActive, true)));

  return NextResponse.json(clones);
}

export async function POST(request: Request) {
  const session = await auth();
  const tenantId = session?.user?.tenantId;
  if (!session?.user || !tenantId) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const payload = await request.json().catch(() => null);
  if (!payload?.name || !payload?.slug) {
    return NextResponse.json({ error: "name and slug are required" }, { status: 400 });
  }

  const clone = {
    id: crypto.randomUUID(),
    tenantId,
    name: String(payload.name),
    slug: String(payload.slug),
    description: payload.description ? String(payload.description) : null,
    avatarUrl: null,
    personalityTone: null,
    language: "es",
    customDomain: null,
    activeModes: ["pedagogy"],
    isActive: true,
  };

  await db.insert(schema.cloneConfigs).values(clone);
  return NextResponse.json(clone, { status: 201 });
}
