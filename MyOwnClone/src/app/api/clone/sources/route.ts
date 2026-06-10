import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { NextResponse, NextRequest } from "next/server";
import { auth } from "@/lib/auth";

/**
 * Resolve the active clone ID from cookie or env var fallback.
 */
function getCloneIdFromRequest(request: NextRequest): string | null {
  const cookieCloneId = request.cookies.get("moc_active_clone_id")?.value;
  if (cookieCloneId) return cookieCloneId;
  return process.env.DEFAULT_CLONE_ID || null;
}

export async function GET(request: NextRequest) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const cloneId = getCloneIdFromRequest(request);
  if (!cloneId) {
    return NextResponse.json(
      { error: "No clone configured. Create a clone first." },
      { status: 404 }
    );
  }

  try {
    const items = await db
      .select()
      .from(schema.sources)
      .where(eq(schema.sources.cloneId, cloneId));

    // Format the records so they match the UI contract.
    const formatted = items.map((item) => ({
      id: item.id,
      title: item.title,
      type: item.type,
      status: item.status,
      silo: (item.metadata as any)?.silo || "teach",
      wordCount: 150, // stub para simplicidad
      createdAt: item.createdAt.toISOString(),
    }));

    return NextResponse.json(formatted);
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

export async function POST(request: NextRequest) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const cloneId = getCloneIdFromRequest(request);
  if (!cloneId) {
    return NextResponse.json(
      { error: "No clone configured. Create a clone first." },
      { status: 404 }
    );
  }

  try {
    const formData = await request.formData();
    const silo = (formData.get("silo") as string) || "teach";
    const type = (formData.get("type") as string) || "text";
    const content = (formData.get("content") as string) || "";
    const url = (formData.get("url") as string) || "";
    const file = formData.get("file") as File | null;

    let title = "New content";
    if (type === "text") {
      title = content.substring(0, 30) || "Text content";
    } else if (type === "youtube" || type === "web") {
      title = url || "Web link";
    } else if (type === "pdf" && file) {
      title = file.name;
    }

    const newSource = {
      id: crypto.randomUUID(),
      cloneId,
      type: type as any,
      title,
      url: url || null,
      status: "ready" as any,
      metadata: { silo },
    };

    await db.insert(schema.sources).values(newSource);

    return NextResponse.json({ success: true, source: newSource });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
