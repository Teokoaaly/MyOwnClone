"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"
import { StatusBadge } from "@/components/ui/StatusBadge"
import { Link, useRouter } from "@/i18n/navigation"

interface Source {
  id: string
  title: string
  type: string
  status: string
  silo: string
  wordCount: number
  createdAt: string
}

const CONTENT_TYPES = [
  { type: "pdf", label: "Upload PDF", desc: "PDF, Word, and Excel documents" },
  { type: "youtube", label: "YouTube link", desc: "Automatic video transcription" },
  { type: "text", label: "Write text", desc: "Paste or write content directly" },
  { type: "web", label: "Web page", desc: "Extract text from a URL" },
  { type: "interview", label: "AI interview", desc: "Your clone interviews you to extract your knowledge" },
]

const SILO_BADGES: Record<string, { label: string; kind: "active" | "trial" | "warning" }> = {
  teach: { label: "Teaching", kind: "trial" },
  support: { label: "Support", kind: "warning" },
  sales: { label: "Sales", kind: "active" },
};

export default function BibliotecaPage() {
  const { status } = useSession()
  const router = useRouter()
  const [sources, setSources] = useState<Source[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchSources = useCallback(async () => {
    if (status !== "authenticated") return

    setLoading(true)
    setError(null)
    try {
      const res = await fetch("/api/clone/sources")
      if (res.ok) {
        const data = await res.json()
        setSources(Array.isArray(data) ? data : data.items ?? [])
      } else {
        throw new Error(`Error ${res.status}`)
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error")
    } finally {
      setLoading(false)
    }
  }, [status])

  useEffect(() => {
    if (status === "authenticated") {
      fetchSources()
    }
  }, [status, fetchSources])

  if (status === "loading" || loading) {
    return <LoadingState label="Loading library..." rows={4} />
  }

  if (error) {
    return (
      <ErrorState
        message={error}
        action={
          <button type="button" onClick={fetchSources} className="btn-secondary text-xs">
            Try again
          </button>
        }
      />
    )
  }

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Content Library
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Upload content to train your clone: PDFs, YouTube videos, text, and more.
        </p>
      </header>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5">
        {CONTENT_TYPES.map((ct) => (
          <Link
            key={ct.type}
            href={`/biblioteca/nuevo?tipo=${ct.type}`}
            className="card hover:border-[var(--border-medium)] transition-colors flex flex-col"
          >
            <h3 className="text-sm font-semibold text-[var(--text-primary)]">
              {ct.label}
            </h3>
            <p className="mt-1 text-xs text-[var(--text-muted)] flex-1">
              {ct.desc}
            </p>
          </Link>
        ))}
      </div>

      <div className="card !p-0 overflow-hidden">
        <div className="px-4 py-3 border-b border-[var(--border-soft)] flex items-center justify-between">
          <h2 className="text-sm font-semibold text-[var(--text-primary)]">
            Uploaded content
          </h2>
          <div className="flex gap-2">
            {Object.entries(SILO_BADGES).map(([k, v]) => (
              <StatusBadge key={k} kind={v.kind} label={v.label} />
            ))}
          </div>
        </div>

        {sources.length === 0 ? (
          <div className="p-4">
            <EmptyState
              title="No content yet"
              description="Upload your first PDF, YouTube link, or direct text to start training your clone."
            />
          </div>
        ) : (
          <ul className="divide-y divide-[var(--border-soft)]">
            {sources.map((source) => (
              <li
                key={source.id}
                className="px-4 py-3 flex items-center justify-between hover:bg-[var(--surface-2)] transition-colors"
              >
                <div className="flex items-center gap-3 min-w-0">
                  <div className="min-w-0">
                    <p className="text-sm font-medium text-[var(--text-primary)] truncate">
                      {source.title}
                    </p>
                    <p className="text-xs text-[var(--text-muted)]">
                      {source.silo} · {source.status} · {source.wordCount.toLocaleString("en-US")} words
                    </p>
                  </div>
                </div>
                <span className="text-xs text-[var(--text-muted)] shrink-0">
                  {new Date(source.createdAt).toLocaleDateString("es-ES")}
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}
