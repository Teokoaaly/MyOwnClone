import { NextRequest, NextResponse } from "next/server"
import { auth } from "@/lib/auth"
import { checkLimit, type PlanName } from "@/lib/quotas"

const MYOWNCLONE_BACKEND = process.env.MYOWNCLONE_API_URL || "http://localhost:5001"
const CLONE_ID = process.env.DEFAULT_CLONE_ID || ""

export async function GET(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  return proxy(request, await params)
}

export async function POST(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  return proxy(request, await params)
}

export async function PUT(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  return proxy(request, await params)
}

export async function DELETE(request: NextRequest, { params }: { params: Promise<{ path: string[] }> }) {
  return proxy(request, await params)
}

async function proxy(request: NextRequest, params: { path: string[] }) {
  const session = await auth()
  if (!session?.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const path = params.path.join("/")

  if (path.includes("chat") && request.method === "POST") {
    const plan = (process.env.DEFAULT_PLAN || "trial") as PlanName
    const { allowed, limit } = checkLimit(plan, "conversationsPerDay", 0)
    if (!allowed) {
      return NextResponse.json(
        { error: `Límite de conversaciones diarias alcanzado (${limit}/día). Actualiza tu plan.` },
        { status: 429 }
      )
    }
  }

  if (path.startsWith("memories") || path.startsWith("analytics")) {
    if (!CLONE_ID) {
      return NextResponse.json(
        { error: "DEFAULT_CLONE_ID not configured" },
        { status: 500 }
      )
    }
  }

  let url = `${MYOWNCLONE_BACKEND}/console/api/myownclone`

  if (path.startsWith("memories")) {
    const memoryId = params.path[1]
    if (memoryId && params.path.length > 1) {
      url += `/memories/${memoryId}`
    } else {
      url += `/clones/${CLONE_ID}/memories`
      const searchParams = new URL(request.url).searchParams
      const type = searchParams.get("type")
      if (type) url += `?type=${type}`
    }
  } else if (path.startsWith("analytics")) {
    const subPath = params.path.slice(1).join("/")
    url += `/clones/${CLONE_ID}/analytics/${subPath}`
  } else {
    url += `/${path}`
  }

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const body = request.method !== "GET" ? await request.json().catch(() => null) : undefined
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
    }
    const cookieHeader = request.headers.get("cookie")
    if (cookieHeader) headers["Cookie"] = cookieHeader

    const res = await fetch(url, {
      method: request.method,
      headers,
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
