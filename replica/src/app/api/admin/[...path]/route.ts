import { NextRequest, NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { eq } from "drizzle-orm";

const MYOWNCLONE_BACKEND =
  process.env.MYOWNCLONE_API_URL || "http://localhost:5001";
const PLATFORM_ADMIN_TOKEN = process.env.PLATFORM_ADMIN_TOKEN || "";

async function authorizeAdmin(): Promise<
  | { ok: true }
  | { ok: false; status: number; error: string }
> {
  const session = await auth();
  if (!session?.user) {
    return { ok: false, status: 401, error: "Unauthorized" };
  }

  // Confirm role in DB to avoid trusting a stale session.
  const user = await db.query.users.findFirst({
    where: eq(schema.users.email, session.user.email ?? ""),
  });
  if (user?.role !== "platform_admin") {
    return { ok: false, status: 403, error: "Platform admin role required" };
  }
  return { ok: true };
}

function buildHeaders(request: NextRequest): Record<string, string> {
  const headers: Record<string, string> = {
    Cookie: request.headers.get("cookie") || "",
  };
  if (PLATFORM_ADMIN_TOKEN) {
    headers["X-Admin-Token"] = PLATFORM_ADMIN_TOKEN;
  }
  return headers;
}

async function proxyRequest(
  request: NextRequest,
  method: "GET" | "POST" | "PATCH" | "DELETE",
  pathParts: string[],
): Promise<NextResponse> {
  const authz = await authorizeAdmin();
  if (authz.ok === false) {
    return NextResponse.json(
      { error: authz.error },
      { status: authz.status },
    );
  }

  const endpoint = pathParts.join("/");
  const url = `${MYOWNCLONE_BACKEND}/console/api/myownclone/admin/${endpoint}`;

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 30_000);

  let body: string | undefined;
  if (method !== "GET" && method !== "DELETE") {
    try {
      body = await request.text();
    } catch {
      body = undefined;
    }
  }
  const searchParams =
    method === "GET" ? new URL(request.url).searchParams.toString() : "";
  const finalUrl = searchParams ? `${url}?${searchParams}` : url;

  try {
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
      ...buildHeaders(request),
    };
    const res = await fetch(finalUrl, {
      method,
      headers,
      body,
      signal: controller.signal,
      redirect: "manual",
    });
    clearTimeout(timeoutId);

    const text = await res.text();
    const data = text ? safeParse(text) : null;
    return NextResponse.json(data ?? null, { status: res.status });
  } catch (err) {
    clearTimeout(timeoutId);
    if (err instanceof Error && err.name === "AbortError") {
      return NextResponse.json(
        { error: "Backend timeout", detail: "Request took too long" },
        { status: 504 },
      );
    }
    return NextResponse.json(
      {
        error: "Backend unreachable",
        detail: err instanceof Error ? err.message : String(err),
      },
      { status: 502 },
    );
  }
}

function safeParse(text: string): unknown {
  try {
    return JSON.parse(text);
  } catch {
    return { _raw: text };
  }
}

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ path: string[] }> },
): Promise<NextResponse> {
  const { path } = await params;
  return proxyRequest(request, "GET", path);
}

export async function POST(
  request: NextRequest,
  { params }: { params: Promise<{ path: string[] }> },
): Promise<NextResponse> {
  const { path } = await params;
  return proxyRequest(request, "POST", path);
}

export async function PATCH(
  request: NextRequest,
  { params }: { params: Promise<{ path: string[] }> },
): Promise<NextResponse> {
  const { path } = await params;
  return proxyRequest(request, "PATCH", path);
}
