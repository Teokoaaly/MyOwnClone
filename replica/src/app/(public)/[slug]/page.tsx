import { ChatPanel } from '@/components/chat/ChatPanel'
import { headers } from 'next/headers'

interface PageProps {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ context?: string; silo?: string }>
}

export default async function ClonePage({ params, searchParams }: PageProps) {
  const { slug } = await params
  const { context, silo } = await searchParams
  const headersList = await headers()
  const contextId = context || headersList.get('x-myownclone-context-id') || undefined
  const defaultSilo = silo || 'teach'

  const cloneData = await fetchCloneConfig(slug)

  return (
    <main
      className="mx-auto flex h-dvh max-w-4xl flex-col px-4"
      style={{ background: "var(--bg-page)", color: "var(--text-primary)" }}
    >
      {/* Header */}
      <header
        className="flex items-center gap-4 border-b px-2 py-4"
        style={{ borderColor: "var(--border-soft)" }}
      >
        <div>
          <h1 className="text-xl font-semibold tracking-tight text-[var(--text-primary)]">
            {cloneData?.name || slug}
          </h1>
          {cloneData?.description && (
            <p className="text-sm text-[var(--text-muted)]">
              {cloneData.description}
            </p>
          )}
        </div>
      </header>

      {/* Chat area */}
      <ChatPanel slug={slug} initialSilo={defaultSilo} contextId={contextId} />
    </main>
  )
}

async function fetchCloneConfig(slug: string) {
  try {
    const apiUrl = process.env.MYOWNCLONE_API_URL || 'http://localhost:5001'
    const res = await fetch(`${apiUrl}/api/myownclone/clones/${slug}`, {
      cache: 'no-store',
    })
    if (!res.ok) return null
    return res.json()
  } catch {
    return null
  }
}
