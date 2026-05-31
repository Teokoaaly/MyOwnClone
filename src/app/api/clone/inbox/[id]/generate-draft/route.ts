import { NextRequest, NextResponse } from "next/server"
import { auth } from "@/lib/auth"

const DIFY_BACKEND = process.env.DIFY_API_URL || "http://localhost:5001"

export async function POST(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
  const session = await auth()
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const { id } = await params
  const url = `${DIFY_BACKEND}/console/api/clonify/inbox/${id}/generate-draft`
  const cookieHeader = request.headers.get("cookie") || ""

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const res = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Cookie: cookieHeader,
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
