import { NextResponse } from "next/server";
import { db, schema } from "@/lib/db";
import { and, eq, gt } from "drizzle-orm";
import { normalizeEmail } from "@/lib/platform-admin";

const IDENTIFIER_PREFIX = "magic-link:";

export async function POST(request: Request) {
  let payload: { token?: string; email?: string } = {};
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON" }, { status: 400 });
  }

  const token = payload.token?.trim();
  const email = normalizeEmail(payload.email);

  if (!token || !email) {
    return NextResponse.json(
      { error: "Token and email are required" },
      { status: 400 },
    );
  }

  try {
    const identifier = `${IDENTIFIER_PREFIX}${email}`;
    const now = new Date();

    const stored = await db.query.verificationTokens.findFirst({
      where: and(
        eq(schema.verificationTokens.identifier, identifier),
        eq(schema.verificationTokens.token, token),
        gt(schema.verificationTokens.expires, now),
      ),
    });

    if (!stored) {
      return NextResponse.json(
        { error: "El enlace no es válido o ha caducado." },
        { status: 400 },
      );
    }

    // One-shot: delete the token so it cannot be reused.
    await db
      .delete(schema.verificationTokens)
      .where(
        and(
          eq(schema.verificationTokens.identifier, identifier),
          eq(schema.verificationTokens.token, token),
        ),
      );

    return NextResponse.json({ ok: true, email });
  } catch (err) {
    console.error("verify-email error:", err);
    return NextResponse.json(
      { error: "Error al verificar el correo." },
      { status: 500 },
    );
  }
}
