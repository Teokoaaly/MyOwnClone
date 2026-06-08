import { NextRequest } from 'next/server'

const MYOWNCLONE_BACKEND_URL = process.env.MYOWNCLONE_API_URL || 'http://localhost:5001'

export async function POST(
  request: NextRequest,
  { params }: { params: Promise<{ slug: string }> },
) {
  const { slug } = await params
  const body = await request.json()

  const { message, silo = 'teach', context_id = null, conversation_id = null } = body

  if (!message || typeof message !== 'string') {
    return Response.json({ error: 'message is required' }, { status: 400 })
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
