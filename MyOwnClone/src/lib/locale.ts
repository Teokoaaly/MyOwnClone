/**
 * Front-end locale helpers.
 *
 * The visitor's preferred language is stored in the ``moc_locale`` cookie
 * (set by POST /console/api/myownclone/me/locale) and respected by the
 * Flask backend for every subsequent request. The front-end itself is
 * already translated through next-intl (configured in
 * ``src/i18n/request.ts``); this module is the bridge that keeps the
 * back-end and the front-end in sync.
 */

export const LOCALE_COOKIE_NAME = "moc_locale";

/** Backend URL used for the locale endpoints. */
const BACKEND_ORIGIN =
  (typeof process !== "undefined" && process.env.NEXT_PUBLIC_API_URL) ||
  "http://127.0.0.1:5001";

export interface LocaleInfo {
  locale: string;
  supported: string[];
  default: string;
  cookie_name?: string;
}

/**
 * Read the locale cookie. Returns ``null`` if it is not set.
 * Safe to call on the server during render.
 */
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

/**
 * Fetch the current locale from the backend (which resolves the
 * cookie / X-Locale / Accept-Language priority for us).
 */
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

/**
 * Persist the chosen locale on the backend. The backend sets a cookie
 * that the front-end can also read directly via ``readLocaleCookie``.
 */
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

/**
 * Canonical display labels for each locale the UI knows about. Keep
 * this in sync with the backend ``SUPPORTED_LOCALES`` tuple.
 */
export const LOCALE_LABELS: Record<string, string> = {
  en: "English",
  es: "Español",
};