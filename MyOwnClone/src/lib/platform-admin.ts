import type { Session } from "next-auth";

const PLATFORM_ADMIN_EMAIL =
  process.env.PLATFORM_ADMIN_EMAIL || process.env.ADMIN_LOGIN_EMAIL || "";
const PLATFORM_ADMIN_PASSWORD_HASH =
  process.env.PLATFORM_ADMIN_PASSWORD_HASH ||
  process.env.ADMIN_LOGIN_PASSWORD_HASH ||
  "";
const BCRYPT_HASH_RE = /^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$/;

export function normalizeEmail(value: string | null | undefined): string {
  return (value ?? "").trim().toLowerCase();
}

export function hasPlatformAdminEnvCredentials(): boolean {
  return Boolean(
    PLATFORM_ADMIN_EMAIL &&
      PLATFORM_ADMIN_PASSWORD_HASH &&
      BCRYPT_HASH_RE.test(PLATFORM_ADMIN_PASSWORD_HASH),
  );
}

export function getPlatformAdminEmail(): string {
  return normalizeEmail(PLATFORM_ADMIN_EMAIL);
}

export function getPlatformAdminPasswordHash(): string {
  return PLATFORM_ADMIN_PASSWORD_HASH;
}

export function isPlatformAdminEnvMisconfigured(): boolean {
  if (!PLATFORM_ADMIN_EMAIL && !PLATFORM_ADMIN_PASSWORD_HASH) {
    return false;
  }
  if (!PLATFORM_ADMIN_EMAIL || !PLATFORM_ADMIN_PASSWORD_HASH) {
    return false;
  }
  return !BCRYPT_HASH_RE.test(PLATFORM_ADMIN_PASSWORD_HASH);
}

export function isPlatformAdminSession(session: Session | null | undefined): boolean {
  if (!session?.user) return false;

  const role = (session.user as Session["user"] & { role?: string }).role;
  if (role !== "platform_admin") return false;

  const configuredEmail = getPlatformAdminEmail();
  if (!configuredEmail) return true;

  return normalizeEmail(session.user.email) === configuredEmail;
}
