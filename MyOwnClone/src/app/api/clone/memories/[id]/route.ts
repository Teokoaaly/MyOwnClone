import { and, eq } from "drizzle-orm";
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";

function updatePayload(payload: Record<string, unknown>) {
  return {
    ...(payload.title !== undefined ? { title: String(payload.title) } : {}),
    ...(payload.content !== undefined ? { content: String(payload.content) } : {}),
    ...(payload.type !== undefined ? { type: payload.type as "memory" | "signature" | "template" } : {}),
    ...(payload.triggerCondition !== undefined
      ? { triggerCondition: payload.triggerCondition ? String(payload.triggerCondition) : null }
      : {}),
    updatedAt: new Date(),
  };
}

export async function PUT(
  request: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const session = await auth();
  const tenantId = session?.user?.tenantId;
  if (!session?.user || !tenantId) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id } = await params;
  const payload = await request.json().catch(() => null);
  if (!payload) {
    return NextResponse.json({ error: "Invalid payload" }, { status: 400 });
  }

  const rows = await db
    .update(schema.memories)
    .set(updatePayload(payload))
    .where(
      and(
        eq(schema.memories.id, id),
        eq(schema.memories.cloneId, schema.cloneConfigs.id),
      ),
    );

  return NextResponse.json({ ok: true, rows });
}

export async function DELETE(
  _request: Request,
  { params }: { params: Promise<{ id: string }> },
) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id } = await params;
  await db.delete(schema.memories).where(eq(schema.memories.id, id));
  return NextResponse.json({ ok: true });
}
