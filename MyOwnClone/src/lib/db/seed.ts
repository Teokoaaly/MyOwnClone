/**
 * Drizzle seed script — creates demo tenant, user, clone, and mode prompts.
 *
 * Usage:
 *   npx tsx src/lib/db/seed.ts
 *
 * Requires DATABASE_URL env var.
 */
import { drizzle } from "drizzle-orm/node-postgres";
import { eq } from "drizzle-orm";
import { Pool } from "pg";
import * as schema from "./schema";

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle(pool, { schema });

// Demo IDs — deterministic for reproducibility
const DEMO_TENANT_ID = "demo-tenant-001";
const DEMO_USER_ID = "demo-user-001";
const DEMO_CLONE_ID = "demo-clone-001";

async function main() {
  console.log("Seeding database...");

  // ── Tenant ──────────────────────────────────────────────────────────────
  const existingTenant = await db
    .select()
    .from(schema.tenants)
    .where(eq(schema.tenants.id, DEMO_TENANT_ID))
    .limit(1);

  if (existingTenant.length === 0) {
    await db.insert(schema.tenants).values({
      id: DEMO_TENANT_ID,
      slug: "demo",
      name: "Demo Tenant",
      plan: "pro",
      status: "active",
      subscriptionStatus: "active",
    } as any);
    console.log("  ✓ Created tenant: demo");
  } else {
    console.log("  ✓ Tenant already exists: demo");
  }

  // ── User (owner) ────────────────────────────────────────────────────────
  const existingUser = await db
    .select()
    .from(schema.users)
    .where(eq(schema.users.id, DEMO_USER_ID))
    .limit(1);

  if (existingUser.length === 0) {
    await db.insert(schema.users).values({
      id: DEMO_USER_ID,
      tenantId: DEMO_TENANT_ID,
      name: "Demo Admin",
      email: "admin@myownclone.com",
      role: "owner",
      status: "active",
      isPlatformAdmin: true,
    } as any);
    console.log("  ✓ Created user: admin@myownclone.com");
  } else {
    console.log("  ✓ User already exists: admin@myownclone.com");
  }

  // ── Clone Config ────────────────────────────────────────────────────────
  const existingClone = await db
    .select()
    .from(schema.cloneConfigs)
    .where(eq(schema.cloneConfigs.id, DEMO_CLONE_ID))
    .limit(1);

  if (existingClone.length === 0) {
    await db.insert(schema.cloneConfigs).values({
      id: DEMO_CLONE_ID,
      tenantId: DEMO_TENANT_ID,
      name: "Demo Clone",
      slug: "demo-clone",
      description: "A demo clone for testing",
      personality: "friendly",
      tone: "professional",
      language: "es",
      isActive: true,
    } as any);
    console.log("  ✓ Created clone: demo-clone");
  } else {
    console.log("  ✓ Clone already exists: demo-clone");
  }

  // ── Clone Mode Prompts ──────────────────────────────────────────────────
  const modes = [
    {
      mode: "pedagogy" as const,
      systemPrompt:
        "Eres un asistente educativo amigable. Explica conceptos de forma clara y didáctica, usando ejemplos prácticos.",
    },
    {
      mode: "support" as const,
      systemPrompt:
        "Eres un agente de soporte técnico. Resuelve dudas con paciencia y professionalism. Si no sabes la respuesta, escala a un humano.",
    },
    {
      mode: "sales" as const,
      systemPrompt:
        "Eres un asesor de ventas consultivo. Escucha las necesidades del cliente y recomienda soluciones relevantes sin ser agresivo.",
    },
  ];

  for (const { mode, systemPrompt } of modes) {
    const existing = await db
      .select()
      .from(schema.cloneModePrompts)
      .where(eq(schema.cloneModePrompts.cloneId, DEMO_CLONE_ID))
      .limit(1);

    const modeExists = existing.some((r) => r.mode === mode);

    if (!modeExists) {
      await db.insert(schema.cloneModePrompts).values({
        id: `${DEMO_CLONE_ID}-${mode}`,
        cloneId: DEMO_CLONE_ID,
        mode,
        systemPrompt,
        isActive: true,
      } as any);
      console.log(`  ✓ Created mode prompt: ${mode}`);
    } else {
      console.log(`  ✓ Mode prompt already exists: ${mode}`);
    }
  }

  console.log("\nSeeding complete!");
  console.log(`  Tenant ID:  ${DEMO_TENANT_ID}`);
  console.log(`  User ID:    ${DEMO_USER_ID}`);
  console.log(`  Clone ID:   ${DEMO_CLONE_ID}`);
  console.log(`  Email:      admin@myownclone.com`);
  console.log(`  (No password set — use magic link or create via UI)`);

  await pool.end();
}

main().catch((err) => {
  console.error("Seed failed:", err);
  process.exit(1);
});
