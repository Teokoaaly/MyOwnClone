import { NextRequest, NextResponse } from "next/server";

const MYOWNCLONE_BACKEND = process.env.MYOWNCLONE_API_URL || "http://localhost:5001";

export async function POST(request: NextRequest) {
  try {
    const contentType = request.headers.get("content-type") || "";
    let body: BodyInit;

    if (contentType.includes("multipart/form-data")) {
      body = await request.formData();
    } else if (contentType.includes("application/json")) {
      body = JSON.stringify(await request.json());
    } else {
      body = await request.text();
    }

    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), 30000)

    const res = await fetch(`${MYOWNCLONE_BACKEND}/api/myownclone/public/inbound-email`, {
      method: "POST",
      headers: { "Content-Type": contentType },
      body,
      signal: controller.signal,
    });
    clearTimeout(timeoutId)

    return NextResponse.json(
      await res.json().catch(() => ({ status: "ok" })),
      { status: res.status },
    );
  } catch (error) {
    console.error("Inbound email proxy error:", error);
    if (error instanceof Error && error.name === "AbortError") {
      return NextResponse.json(
        { error: "Backend timeout", detail: "Request took too long" },
        { status: 504 }
      )
    }
    return NextResponse.json(
      { error: "Backend unreachable", detail: error instanceof Error ? error.message : String(error) },
      { status: 502 }
    );
  }
}
