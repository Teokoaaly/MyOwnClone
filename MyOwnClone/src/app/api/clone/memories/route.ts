import { and, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";

async function resolveCloneId(tenantId: string) {
  const clone = await db
    .select({ id: schema.cloneConfigs.id })
    .from(schema.cloneConfigs)
    .where(and(eq(schema.cloneConfigs.tenantId, tenantId), eq(schema.cloneConfigs.isActive, true)))
    .limit(1);
  return clone[0]?.id ?? null;
}

export async function GET(request: Request) {
  const session = await auth();
  const tenantId = session?.user?.tenantId;
  if (!session?.user || !tenantId) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const cloneId = await resolveCloneId(tenantId);
  if (!cloneId) {
    return NextResponse.json([], { status: 200 });
  }

  const url = new URL(request.url);
  const type = url.searchParams.get("type");
  const filters = [eq(schema.memories.cloneId, cloneId)];
  if (type) filters.push(eq(schema.memories.type, type as "memory" | "signature" | "template"));

  const rows = await db.select().from(schema.memories).where(and(...filters));
  return NextResponse.json(rows);
}

export async function POST(request: Request) {
  const session = await auth();
  const tenantId = session?.user?.tenantId;
  if (!session?.user || !tenantId) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const cloneId = await resolveCloneId(tenantId);
  if (!cloneId) {
    return NextResponse.json({ error: "No active clone" }, { status: 404 });
  }

  const payload = await request.json().catch(() => null);
  if (!payload?.title || !payload?.content) {
    return NextResponse.json({ error: "title and content are required" }, { status: 400 });
  }

  const memory = {
    id: crypto.randomUUID(),
    cloneId,
    type: payload.type ?? "memory",
    title: String(payload.title),
    content: String(payload.content),
    triggerCondition: payload.triggerCondition ? String(payload.triggerCondition) : null,
  };

  await db.insert(schema.memories).values(memory);
  return NextResponse.json(memory, { status: 201 });
}
