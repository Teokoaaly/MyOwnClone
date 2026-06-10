/**
 * Clone resolution helpers — replaces DEFAULT_CLONE_ID with dynamic tenant-based lookup.
 */
import { eq, and } from "drizzle-orm";
import { db } from "./index";
import * as schema from "./schema";

/**
 * Resolve the first active clone for a given tenant.
 * Returns the clone ID or null if none exists.
 */
export async function resolveCloneForTenant(tenantId: string): Promise<string | null> {
  const [clone] = await db
    .select({ id: schema.cloneConfigs.id })
    .from(schema.cloneConfigs)
    .where(
      and(
        eq(schema.cloneConfigs.tenantId, tenantId),
        eq(schema.cloneConfigs.isActive, true)
      )
    )
    .limit(1);

  return clone?.id ?? null;
}

/**
 * Resolve clone by slug for a given tenant.
 */
export async function resolveCloneBySlug(
  tenantId: string,
  slug: string
): Promise<string | null> {
  const [clone] = await db
    .select({ id: schema.cloneConfigs.id })
    .from(schema.cloneConfigs)
    .where(
      and(
        eq(schema.cloneConfigs.tenantId, tenantId),
        eq(schema.cloneConfigs.slug, slug)
      )
    )
    .limit(1);

  return clone?.id ?? null;
}

/**
 * Get all active clones for a tenant.
 */
export async function getClonesForTenant(tenantId: string) {
  return db
    .select({
      id: schema.cloneConfigs.id,
      name: schema.cloneConfigs.name,
      slug: schema.cloneConfigs.slug,
    })
    .from(schema.cloneConfigs)
    .where(
      and(
        eq(schema.cloneConfigs.tenantId, tenantId),
        eq(schema.cloneConfigs.isActive, true)
      )
    );
}
