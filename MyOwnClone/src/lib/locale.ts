/**
 * Front-end locale helpers.
 *
 * The visitor's preferred language is stored in the ``moc_locale`` cookie
 * (set by POST /console/api/myownclone/me/locale) and respected by the
 * Flask backend for every subsequent request.
 */

export const LOCALE_COOKIE_NAME = "moc_locale";

const BACKEND_ORIGIN =
  (typeof process !== "undefined" && process.env.NEXT_PUBLIC_API_URL) ||
  "http://127.0.0.1:5001";

export interface LocaleInfo {
  locale: string;
  supported: string[];
  default: string;
  cookie_name?: string;
}

export function readLocaleCookie(cookieHeader?: string): string | null {
  const source = cookieHeader ?? "";
  if (!source) return null;
  const parts = source.split(/;\s*/);
  for (const part of parts) {
    const eq = part.indexOf("=");
    if (eq === -1) continue;
    const name = part.slice(0, eq).trim();
    if (name === LOCALE_COOKIE_NAME) {
      const value = part.slice(eq + 1).trim();
      return value || null;
    }
  }
  return null;
}

export async function fetchBackendLocale(): Promise<LocaleInfo | null> {
  try {
    const res = await fetch(`${BACKEND_ORIGIN}/console/api/myownclone/me/locale`, {
      cache: "no-store",
      credentials: "include",
    });
    if (!res.ok) return null;
    return (await res.json()) as LocaleInfo;
  } catch {
    return null;
  }
}

export async function setBackendLocale(
  locale: string,
): Promise<LocaleInfo | null> {
  try {
    const res = await fetch(`${BACKEND_ORIGIN}/console/api/myownclone/me/locale`, {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ locale }),
    });
    if (!res.ok) return null;
    return (await res.json()) as LocaleInfo;
  } catch {
    return null;
  }
}

export const LOCALE_LABELS: Record<string, string> = {
  en: "English",
  es: "Español",
};
