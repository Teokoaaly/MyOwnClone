import { NextRequest, NextResponse } from "next/server"

const DIFY_BACKEND = process.env.DIFY_API_URL || "http://localhost:5001"
const ADMIN_TOKEN = process.env.PLATFORM_ADMIN_TOKEN || ""

export async function GET(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  const { path } = await params
  const endpoint = path.join("/")
  const searchParams = new URL(request.url).searchParams.toString()

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const url = `${DIFY_BACKEND}/console/api/clonify/admin/${endpoint}${searchParams ? `?${searchParams}` : ""}`
    const res = await fetch(url, {
      headers: {
        "Content-Type": "application/json",
        Cookie: request.headers.get("cookie") || "",
      },
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

export async function POST(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  const { path } = await params
  const endpoint = path.join("/")
  const body = await request.json().catch(() => ({}))

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const res = await fetch(`${DIFY_BACKEND}/console/api/clonify/admin/${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Cookie: request.headers.get("cookie") || "",
      },
      body: JSON.stringify(body),
      signal: controller.signal,
    })
    clearTimeout(timeoutId)
    return NextResponse.json(await res.json().catch(() => null), { status: res.status })
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
