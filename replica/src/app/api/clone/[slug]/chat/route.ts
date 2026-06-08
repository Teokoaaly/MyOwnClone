import { NextRequest } from 'next/server'

const MYOWNCLONE_BACKEND_URL = process.env.MYOWNCLONE_API_URL || 'http://localhost:5001'

// Allowed silos
const ALLOWED_SILOS = new Set(['teach', 'sales', 'support'])

// Max message body length (characters)
const MAX_MESSAGE_LENGTH = 4000

// In-memory rate limiter: 10 requests per minute per IP+slug
const rateLimitMap = new Map<string, { count: number; resetAt: number }>()
const RATE_LIMIT_MAX = 10
const RATE_LIMIT_WINDOW_MS = 60_000

function getClientIp(request: NextRequest): string {
  return (
    request.headers.get('x-forwarded-for')?.split(',')[0]?.trim() ||
    request.headers.get('x-real-ip') ||
    'unknown'
  )
}

function checkRateLimit(key: string): boolean {
  const now = Date.now()
  const entry = rateLimitMap.get(key)

  if (!entry || now > entry.resetAt) {
    rateLimitMap.set(key, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS })
    return true
  }

  if (entry.count >= RATE_LIMIT_MAX) {
    return false
  }

  entry.count++
  return true
}

// Periodic cleanup of expired entries every 5 minutes
if (typeof setInterval !== 'undefined') {
  setInterval(() => {
    const now = Date.now()
    for (const [key, entry] of rateLimitMap) {
      if (now > entry.resetAt) {
        rateLimitMap.delete(key)
      }
    }
  }, 300_000)
}

export async function POST(
  request: NextRequest,
  { params }: { params: Promise<{ slug: string }> },
) {
  const { slug } = await params

  // --- Rate limiting ---
  const ip = getClientIp(request)
  const rateLimitKey = `${ip}:${slug}`
  if (!checkRateLimit(rateLimitKey)) {
    return Response.json(
      { error: 'Too many requests. Please wait before sending another message.' },
      { status: 429 },
    )
  }

  const body = await request.json()

  const { message, silo = 'teach', context_id = null, conversation_id = null } = body

  // --- Validate message ---
  if (!message || typeof message !== 'string') {
    return Response.json({ error: 'message is required' }, { status: 400 })
  }

  // --- Validate message length ---
  if (message.length > MAX_MESSAGE_LENGTH) {
    return Response.json(
      { error: `message exceeds maximum length of ${MAX_MESSAGE_LENGTH} characters` },
      { status: 400 },
    )
  }

  // --- Validate silo ---
  if (!ALLOWED_SILOS.has(silo)) {
    return Response.json(
      { error: `invalid silo: "${silo}". Allowed values: ${Array.from(ALLOWED_SILOS).join(', ')}` },
      { status: 400 },
    )
  }

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 30000)

  try {
    const backendRes = await fetch(`${MYOWNCLONE_BACKEND_URL}/api/myownclone/public/clones/${slug}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Forwarded-For': request.headers.get('x-forwarded-for') || 'unknown',
        'X-Real-IP': request.headers.get('x-real-ip') || 'unknown',
      },
      body: JSON.stringify({
        message,
        silo,
        context_id,
        conversation_id,
      }),
      signal: controller.signal,
    })
    clearTimeout(timeoutId)

    if (!backendRes.ok) {
      const errText = await backendRes.text()
      return Response.json(
        { error: `Backend error: ${backendRes.status}`, detail: errText },
        { status: backendRes.status },
      )
    }

    return new Response(backendRes.body, {
      headers: {
        'Content-Type': backendRes.headers.get('content-type') || 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
      },
    })
  } catch (err) {
    clearTimeout(timeoutId)
    if (err instanceof Error && err.name === 'AbortError') {
      return Response.json(
        { error: 'Backend timeout', detail: 'Request took too long' },
        { status: 504 },
      )
    }
    return Response.json(
      { error: 'Failed to reach backend', detail: err instanceof Error ? err.message : String(err) },
      { status: 502 },
    )
  }
}
