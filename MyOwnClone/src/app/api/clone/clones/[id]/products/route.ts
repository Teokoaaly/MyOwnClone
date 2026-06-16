import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { NextResponse, NextRequest } from "next/server";
import { auth } from "@/lib/auth";

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

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth();
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id } = await params;

  // Validate clone belongs to authenticated tenant (IDOR prevention)
  const tenantId = session.user.tenantId;
  if (tenantId && !(await validateCloneOwnership(id, tenantId))) {
    return NextResponse.json(
      { error: "Forbidden: clone not accessible" },
      { status: 403 }
    );
  }

  try {
    const products = await db.query.products.findMany({
      where: (p, { eq, and }) => and(eq(p.cloneId, id)),
      columns: {
        id: true,
        name: true,
        description: true,
      },
    });

    return NextResponse.json(products);
  } catch (error) {
    console.error("Error fetching products:", error);
    return NextResponse.json({ error: "Failed to fetch products" }, { status: 500 });
  }
}
