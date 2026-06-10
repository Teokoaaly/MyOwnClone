import { NextRequest, NextResponse } from "next/server";

const BACKEND_URL = "http://127.0.0.1:5001";
const CLONE_ID = process.env.DEFAULT_CLONE_ID || "";

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

function findBackendPath(pathname: string): string | null {
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
    return `/console/api/myownclone/clones/${CLONE_ID}/analytics/${subpath}`;
  }

  // 4. Inbox
  if (sub === "inbox/list") {
    return `/console/api/myownclone/clones/${CLONE_ID}/inbox`;
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
    return `/console/api/myownclone/clones/${CLONE_ID}/memories`;
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

export async function middleware(request: NextRequest) {
  const { pathname, hostname } = request.nextUrl;

  // Skip Next.js internals
  if (pathname.startsWith("/_next") || pathname.startsWith("/favicon")) {
    return NextResponse.next();
  }

  // Tenant detection
  const tenantSlug = getTenantFromHost(hostname);
  if (tenantSlug) {
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-tenant-slug", tenantSlug);
    return NextResponse.next({
      request: { headers: requestHeaders },
    });
  }

  // Proxy API calls to Flask backend
  if (pathname.startsWith("/api/")) {
    const backendPath = findBackendPath(pathname);
    if (backendPath) {
      const search = request.nextUrl.search;
      const backendUrl = `${BACKEND_URL}${backendPath}${search}`;

      // Forward auth header if present
      const authHeader = request.headers.get("authorization") || "";
      const forwardedHeaders: Record<string, string> = {
        "Content-Type": "application/json",
        "X-API-Key": SERVICE_API_KEY,
      };
      if (authHeader) {
        forwardedHeaders["Authorization"] = authHeader;
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

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|widget.js).*)"],
};
