import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { db, schema } from "@/lib/db";
import { and, eq, gt } from "drizzle-orm";
import { normalizeEmail } from "@/lib/platform-admin";

const MIN_PASSWORD_LENGTH = 8;

export async function POST(request: Request) {
  let payload: { token?: string; email?: string; password?: string } = {};
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON" }, { status: 400 });
  }

  const token = payload.token?.trim();
  const email = normalizeEmail(payload.email);
  const password = payload.password ?? "";

  if (!token || !email || !password) {
    return NextResponse.json(
      { error: "Token, email and password are required" },
      { status: 400 },
    );
  }

  if (password.length < MIN_PASSWORD_LENGTH) {
    return NextResponse.json(
      { error: `La contraseña debe tener al menos ${MIN_PASSWORD_LENGTH} caracteres.` },
      { status: 400 },
    );
  }

  try {
    const identifier = `password-reset:${email}`;
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

    const user = await db.query.users.findFirst({
      where: (users, { eq }) => eq(users.email, email),
    });

    if (!user) {
      return NextResponse.json(
        { error: "El enlace no es válido o ha caducado." },
        { status: 400 },
      );
    }

    const passwordHash = await bcrypt.hash(password, 12);
    await db
      .update(schema.users)
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      .set({ passwordHash, updatedAt: now } as any)
      .where(eq(schema.users.id, user.id));

    // One-shot: delete the token so it cannot be reused.
    await db
      .delete(schema.verificationTokens)
      .where(
        and(
          eq(schema.verificationTokens.identifier, identifier),
          eq(schema.verificationTokens.token, token),
        ),
      );

    return NextResponse.json({ ok: true });
  } catch (err) {
    console.error("reset-password error:", err);
    return NextResponse.json(
      { error: "Error al restablecer la contraseña." },
      { status: 500 },
    );
  }
}
