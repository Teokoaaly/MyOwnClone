import { NextRequest, NextResponse } from "next/server"
import { auth } from "@/lib/auth"

const MYOWNCLONE_BACKEND = process.env.MYOWNCLONE_API_URL || "http://localhost:5001"

async function proxyToMyOwnClone(request: NextRequest, path: string, method: string) {
  const session = await auth()
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const url = `${MYOWNCLONE_BACKEND}/console/api/myownclone/${path}`
  const cookieHeader = request.headers.get("cookie") || ""

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const body = method !== "GET" ? await request.json().catch(() => null) : undefined
    const res = await fetch(url, {
      method,
      headers: {
        "Content-Type": "application/json",
        Cookie: cookieHeader,
      },
      body: body ? JSON.stringify(body) : undefined,
      signal: controller.signal,
    })
    clearTimeout(timeoutId)
    const data = await res.json().catch(() => null)
    return NextResponse.json(data, { status: res.status })
  } catch (err) {
    clearTimeout(timeoutId)
    if (err instanceof Error && err.name === "AbortError") {
      return NextResponse.json(
        { error: "Backend timeout", detail: "Request took too long" },
        { status: 504 }
      )
    }
    return NextResponse.json(
      { error: "Backend unreachable", detail: err instanceof Error ? err.message : String(err) },
      { status: 502 }
    )
  }
}

export async function GET(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
  return proxyToMyOwnClone(request, `inbox/${(await params).id}?${new URL(request.url).searchParams.toString()}`, "GET")
}

export async function PUT(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
  return proxyToMyOwnClone(request, `inbox/${(await params).id}`, "PUT")
}

export async function DELETE(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
  return proxyToMyOwnClone(request, `inbox/${(await params).id}`, "DELETE")
}
