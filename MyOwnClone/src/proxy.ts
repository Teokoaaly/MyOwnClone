import { NextRequest, NextResponse } from "next/server";
import { getToken } from "next-auth/jwt";
import { routing } from "@/i18n/routing";

const BACKEND_URL = "http://127.0.0.1:5001";
const LOCALE_HEADER = "x-locale";
const LOCALIZED_APP_ROUTES = new Set(["/es/onboarding", "/es/verificar"]);

/**
 * Extract the active clone ID from the moc_active_clone_id cookie.
 * Falls back to DEFAULT_CLONE_ID env var for backward compatibility.
 */
function getCloneId(request: NextRequest): string {
  const cookieCloneId = request.cookies.get("moc_active_clone_id")?.value;
  if (cookieCloneId) return cookieCloneId;
  return process.env.DEFAULT_CLONE_ID || "";
}

// Service-to-service API key for authenticating proxy requests to the Flask backend.
// Must match the value checked in Flask's login_required decorator (X-API-Key header).
// In production, set SERVICE_API_KEY in .env.local to a strong random value.
const SERVICE_API_KEY = process.env.SERVICE_API_KEY ?? "dev-api-key-for-proxy";

// Map frontend API paths to backend paths (legacy / admin / auth)
const ROUTE_MAP: Record<string, string> = {
  "/api/admin/overview": "/console/api/myownclone/admin/overview",
  "/api/admin/tenants": "/console/api/myownclone/admin/tenants",
  "/api/admin/impersonate": "/console/api/myownclone/admin/impersonate",
  "/api/admin/courtesy-account": "/console/api/myownclone/admin/courtesy-account",
  "/api/clones": "/console/api/myownclone/clones",
  "/api/plans": "/console/api/myownclone/plans",
  "/api/stripe/checkout": "/console/api/myownclone/stripe/checkout",
  "/api/stripe/billing": "/console/api/myownclone/stripe/billing",
  "/api/feedback": "/console/api/myownclone/feedback",
  "/api/inbox": "/console/api/myownclone/inbox",
  "/api/auth/login": "/console/api/auth/login",
};

function getTenantFromHost(hostname: string): string | null {
  if (hostname === "localhost" || hostname.startsWith("localhost:")) return null;
  const parts = hostname.split(".");
  if (parts.length >= 3 && parts[1] === "replica") {
    return parts[0];
  }
  return null;
}

function findBackendPath(pathname: string, request: NextRequest): string | null {
  // Ignoramos la biblioteca de contenidos (sources), que se resolverá localmente en Next.js
  if (pathname === "/api/clone/sources" || pathname.startsWith("/api/clone/sources/")) {
    return null;
  }

  // Si no empieza con /api/clone/ pero está en el ROUTE_MAP original, lo usamos
  if (!pathname.startsWith("/api/clone/")) {
    if (ROUTE_MAP[pathname]) return ROUTE_MAP[pathname];
    for (const [prefix, mappedPrefix] of Object.entries(ROUTE_MAP)) {
      if (pathname.startsWith(prefix + "/")) {
        return mappedPrefix + pathname.slice(prefix.length);
      }
    }
    return null;
  }

  // Rutas con el prefijo /api/clone/
  const sub = pathname.slice("/api/clone/".length); // ej. "analytics/overview", "clones", "clones/xxx/products"

  // 1. Clones directos (ej. /api/clone/clones)
  if (sub === "clones") {
    return "/console/api/myownclone/clones";
  }

  // 2. Clones específicos con ID en el path
  if (sub.startsWith("clones/")) {
    // sub es "clones/<clone_id>/..."
    return `/console/api/myownclone/${sub}`;
  }

  // 3. Analytics
  if (sub.startsWith("analytics/")) {
    const subpath = sub.slice("analytics/".length);
    const cloneId = getCloneId(request);
    return `/console/api/myownclone/clones/${cloneId}/analytics/${subpath}`;
  }

  // 4. Inbox
  if (sub === "inbox/list") {
    const cloneId = getCloneId(request);
    return `/console/api/myownclone/clones/${cloneId}/inbox`;
  }
  if (sub.startsWith("inbox/")) {
    const parts = sub.split("/"); // ["inbox", "<id>", "generate-draft"?]
    const emailId = parts[1];
    if (parts.length > 2 && parts[2] === "generate-draft") {
      return `/console/api/myownclone/inbox/${emailId}/generate-draft`;
    }
    return `/console/api/myownclone/inbox/${emailId}`;
  }

  // 5. Memories
  if (sub === "memories") {
    const cloneId = getCloneId(request);
    return `/console/api/myownclone/clones/${cloneId}/memories`;
  }
  if (sub.startsWith("memories/")) {
    const memoryId = sub.slice("memories/".length);
    return `/console/api/myownclone/memories/${memoryId}`;
  }

  // 6. Stripe / Planes / Billing
  if (sub === "plans") {
    return "/console/api/myownclone/plans";
  }
  if (sub === "billing") {
    return "/console/api/myownclone/stripe/billing";
  }
  if (sub === "stripe/checkout") {
    return "/console/api/myownclone/stripe/checkout";
  }

  return null;
}

export async function proxy(request: NextRequest) {
  const { pathname, hostname } = request.nextUrl;
  const forwardedLocale = request.headers.get(LOCALE_HEADER);

  // Skip Next.js internals
  if (pathname.startsWith("/_next") || pathname.startsWith("/favicon")) {
    return NextResponse.next();
  }

  const localeMatch = routing.locales.find(
    (candidate) =>
      pathname === `/${candidate}` || pathname.startsWith(`/${candidate}/`),
  );
  const normalizedPathname = localeMatch
    ? pathname.slice(localeMatch.length + 1) || "/"
    : pathname;

  // Tenant detection
  const tenantSlug = getTenantFromHost(hostname);
  if (tenantSlug) {
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-tenant-slug", tenantSlug);
    requestHeaders.set(LOCALE_HEADER, localeMatch ?? forwardedLocale ?? routing.defaultLocale);
    return NextResponse.next({
      request: { headers: requestHeaders },
    });
  }

  // Proxy API calls to Flask backend
  if (pathname.startsWith("/api/")) {
    const backendPath = findBackendPath(pathname, request);
    if (backendPath) {
      const search = request.nextUrl.search;
      const backendUrl = `${BACKEND_URL}${backendPath}${search}`;
      const token = await getToken({
        req: request,
        secret: process.env.AUTH_SECRET || process.env.NEXTAUTH_SECRET,
      });

      // Forward auth header if present
      const authHeader = request.headers.get("authorization") || "";
      const forwardedHeaders: Record<string, string> = {
        "Content-Type": "application/json",
        "X-API-Key": SERVICE_API_KEY,
      };
      if (authHeader) {
        forwardedHeaders["Authorization"] = authHeader;
      }
      if (token?.id) {
        forwardedHeaders["X-User-Id"] = String(token.id);
      }
      if (token?.email) {
        forwardedHeaders["X-User-Email"] = String(token.email);
      }
      if ((token as any)?.role) {
        forwardedHeaders["X-User-Role"] = String((token as any).role);
      }
      if ((token as any)?.tenantId) {
        forwardedHeaders["X-Tenant-Id"] = String((token as any).tenantId);
      }

      try {
        const response = await fetch(backendUrl, {
          method: request.method,
          headers: forwardedHeaders,
          body: request.method !== "GET" && request.method !== "HEAD"
            ? await request.text()
            : undefined,
        });

        const data = await response.json();
        return NextResponse.json(data, { status: response.status });
      } catch {
        return NextResponse.json(
          { error: "Backend unavailable" },
          { status: 502 },
        );
      }
    }
  }

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set(LOCALE_HEADER, localeMatch ?? forwardedLocale ?? routing.defaultLocale);

  if (localeMatch && !LOCALIZED_APP_ROUTES.has(pathname)) {
    const rewriteUrl = request.nextUrl.clone();
    rewriteUrl.pathname = normalizedPathname;
    return NextResponse.rewrite(rewriteUrl, {
      request: { headers: requestHeaders },
    });
  }

  return NextResponse.next({
    request: { headers: requestHeaders },
  });
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|widget.js).*)"],
};
