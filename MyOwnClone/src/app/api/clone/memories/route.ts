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

/**
 * Validate that a clone belongs to the given tenant.
 * Returns true if the clone is owned by the tenant, false otherwise.
 */
async function validateCloneOwnership(cloneId: string, tenantId: string): Promise<boolean> {
  const clone = await db.query.cloneConfigs.findFirst({
    where: (clones, { eq }) => eq(clones.id, cloneId),
    columns: { tenantId: true },
  });
  return clone?.tenantId === tenantId;
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

  // Validate clone belongs to authenticated tenant (IDOR prevention)
  const tenantId = session.user.tenantId;
  if (tenantId && !(await validateCloneOwnership(cloneId, tenantId))) {
    return NextResponse.json(
      { error: "Forbidden: clone not accessible" },
      { status: 403 }
    );
  }

  const { searchParams } = new URL(request.url);
  const typeFilter = searchParams.get("type");

  try {
    // Build where clause for memories
    const whereClause = typeFilter
      ? (memories: any, { eq }: any) => eq(memories.cloneId, cloneId)
      : (memories: any, { eq }: any) => eq(memories.cloneId, cloneId);

    const memories = await db.query.memories.findMany({
      where: (m, { eq, and }) => {
        const conditions = [eq(m.cloneId, cloneId)];
        if (typeFilter) {
          conditions.push(eq(m.type, typeFilter as "memory" | "signature" | "template"));
        }
        return and(...conditions);
      },
      columns: {
        id: true,
        content: true,
        type: true,
      },
      limit: 50,
    });

    return NextResponse.json(memories);
  } catch (error) {
    console.error("Error fetching memories:", error);
    return NextResponse.json({ error: "Failed to fetch memories" }, { status: 500 });
  }
}
