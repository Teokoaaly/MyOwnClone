import { NextRequest, NextResponse } from "next/server";

function getTenantFromHost(hostname: string): string | null {
  if (hostname === "localhost" || hostname.startsWith("localhost:")) return null;
  const parts = hostname.split(".");
  if (parts.length >= 3 && parts[1] === "replica") {
    return parts[0];
  }
  return null;
}

export async function middleware(request: NextRequest) {
  const { pathname, hostname } = request.nextUrl;

  // Skip static files
  if (pathname.startsWith("/_next") || pathname.startsWith("/favicon")) {
    return NextResponse.next();
  }

  const tenantSlug = getTenantFromHost(hostname);
  if (tenantSlug) {
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-tenant-slug", tenantSlug);
    return NextResponse.next({
      request: { headers: requestHeaders },
    });
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|widget.js).*)"],
};
