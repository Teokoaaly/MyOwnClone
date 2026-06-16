import { NextResponse, type NextRequest } from "next/server";

/**
 * Locale detection middleware.
 *
 * Resolution order (highest priority first):
 *   1. Cookie `myownclone_locale` if present and valid.
 *   2. `Accept-Language` header (best match against the supported set).
 *   3. Default locale (`en`).
 *
 * The resolved locale is exposed to the rest of the app (server
 * components, server actions, `request.ts`) via the
 * `x-locale` request header. The current `request.ts` /
 * `app/layout.tsx` already consume that header, so this middleware
 * is a drop-in addition with no further wiring required.
 *
 * The cookie is set on every response so that anonymous users
 * detected via `Accept-Language` get their preference persisted.
 */
const SUPPORTED_LOCALES = ["es", "en"] as const;
type SupportedLocale = (typeof SUPPORTED_LOCALES)[number];
const DEFAULT_LOCALE: SupportedLocale = "en";
const COOKIE_NAME = "myownclone_locale";
const HEADER_NAME = "x-locale";
const COOKIE_MAX_AGE = 60 * 60 * 24 * 365; // 1 year

function isSupported(value: string | null | undefined): value is SupportedLocale {
  return typeof value === "string" && (SUPPORTED_LOCALES as readonly string[]).includes(value);
}

function resolveFromAcceptLanguage(header: string | null): SupportedLocale {
  if (!header) return DEFAULT_LOCALE;
  // Accept-Language can list several entries with quality scores
  // (e.g. "es-ES,es;q=0.9,en;q=0.8"). Parse and pick the best match.
  const candidates = header
    .split(",")
    .map((part) => {
      const [tag, ...params] = part.trim().split(";");
      const qParam = params.find((p) => p.trim().startsWith("q="));
      const q = qParam ? Number(qParam.split("=")[1]) : 1;
      return { tag: tag.toLowerCase(), q: Number.isFinite(q) ? q : 0 };
    })
    .filter((c) => c.tag.length > 0)
    .sort((a, b) => b.q - a.q);

  for (const { tag } of candidates) {
    // Exact match: "es", "en".
    if (isSupported(tag)) return tag;
    // Prefix match: "es-es" -> "es".
    const base = tag.split("-")[0];
    if (isSupported(base)) return base;
  }
  return DEFAULT_LOCALE;
}

function resolveLocale(request: NextRequest): SupportedLocale {
  const cookie = request.cookies.get(COOKIE_NAME)?.value;
  if (isSupported(cookie)) return cookie;
  return resolveFromAcceptLanguage(request.headers.get("accept-language"));
}

export function middleware(request: NextRequest) {
  const locale = resolveLocale(request);

  // Forward the resolved locale downstream by rewriting headers on
  // the incoming request, then build the response and persist the
  // cookie so subsequent visits are stable.
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set(HEADER_NAME, locale);

  const response = NextResponse.next({ request: { headers: requestHeaders } });

  // Only set the cookie when the user did not have one already
  // (avoid clobbering explicit choices) or when the value differs.
  const existing = request.cookies.get(COOKIE_NAME)?.value;
  if (existing !== locale) {
    response.cookies.set({
      name: COOKIE_NAME,
      value: locale,
      maxAge: COOKIE_MAX_AGE,
      sameSite: "lax",
      path: "/",
    });
  }

  return response;
}

export const config = {
  // Match everything except Next.js internals and static assets.
  // We need the header on every request because the layout reads
  // it via `headers()` server-side.
  matcher: ["/((?!_next|api|_vercel|.*\\..*).*)"],
};
