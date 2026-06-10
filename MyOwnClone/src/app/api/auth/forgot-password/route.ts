import { NextResponse } from "next/server";
import { randomBytes } from "crypto";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";
import { sendLoginVerificationCode } from "@/lib/email";
import { normalizeEmail } from "@/lib/platform-admin";

const TOKEN_TTL_MINUTES = 30;

export async function POST(request: Request) {
  let payload: { email?: string } = {};
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON" }, { status: 400 });
  }

  const email = normalizeEmail(payload.email);
  if (!email) {
    return NextResponse.json({ error: "Email is required" }, { status: 400 });
  }

  // Always return success to avoid user enumeration. Only send the email
  // when the user actually exists.
  try {
    const user = await db.query.users.findFirst({
      where: (users, { eq }) => eq(users.email, email),
    });

    if (user) {
      const token = randomBytes(32).toString("hex");
      const expires = new Date(Date.now() + TOKEN_TTL_MINUTES * 60 * 1000);

      await db
        .insert(schema.verificationTokens)
        .values({
          identifier: `password-reset:${email}`,
          token,
          expires,
        })
        .onConflictDoUpdate({
          target: schema.verificationTokens.token,
          set: { expires },
        });

      const baseUrl = process.env.NEXTAUTH_URL ?? "http://localhost:3000";
      const url = `${baseUrl}/reset-password?token=${encodeURIComponent(token)}&email=${encodeURIComponent(email)}`;

      try {
        await sendLoginVerificationCode({ to: email, url });
      } catch (err) {
        console.error("Failed to send password reset email:", err);
        // Do not surface the error to the caller; the API contract is
        // "we'll handle it" so we don't leak whether the email exists.
      }
    }
  } catch (err) {
    console.error("forgot-password error:", err);
  }

  return NextResponse.json({ ok: true });
}
