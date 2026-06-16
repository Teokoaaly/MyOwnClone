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

  try {
    // Get all clones for this tenant (for the search to allow switching between clones)
    const clones = await db.query.cloneConfigs.findMany({
      where: (c, { eq }) => eq(c.tenantId, tenantId),
      columns: {
        id: true,
        name: true,
        slug: true,
      },
    });

    return NextResponse.json(clones);
  } catch (error) {
    console.error("Error fetching clones:", error);
    return NextResponse.json({ error: "Failed to fetch clones" }, { status: 500 });
  }
}
