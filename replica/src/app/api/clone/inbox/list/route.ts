import { NextRequest, NextResponse } from "next/server"
import { auth } from "@/lib/auth"

const MYOWNCLONE_BACKEND = process.env.MYOWNCLONE_API_URL || "http://localhost:5001"

async function proxyToMyOwnClone(request: NextRequest, path: string) {
  const session = await auth()
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const url = `${MYOWNCLONE_BACKEND}/console/api/myownclone/${path}`
  const cookieHeader = request.headers.get("cookie") || ""

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const body = request.method !== "GET" ? await request.json().catch(() => null) : undefined
    const res = await fetch(url, {
      method: request.method,
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

export async function GET(request: NextRequest) {
  const session = await auth()
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  // Get user's clone_id from backend - use first clone for now
  const clonesRes = await fetch(`${MYOWNCLONE_BACKEND}/console/api/myownclone/clones`, {
    headers: {
      Cookie: request.headers.get("cookie") || "",
    },
  })

  if (!clonesRes.ok) {
    return NextResponse.json({ error: "Failed to get clones" }, { status: clonesRes.status })
  }

  const clones = await clonesRes.json()
  if (!clones || clones.length === 0) {
    return NextResponse.json({ error: "No clone found for user" }, { status: 404 })
  }

  const cloneId = clones[0].id
  return proxyToMyOwnClone(request, `clones/${cloneId}/inbox?${new URL(request.url).searchParams.toString()}`)
}
