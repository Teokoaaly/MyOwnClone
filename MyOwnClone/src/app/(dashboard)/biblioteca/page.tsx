"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"
import { StatusBadge } from "@/components/ui/StatusBadge"

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
  { type: "pdf", label: "Subir PDF", desc: "Documentos PDF, Word, Excel" },
  { type: "youtube", label: "Enlace de YouTube", desc: "Transcripción automática de vídeos" },
  { type: "text", label: "Escribir texto", desc: "Pega o escribe contenido directamente" },
  { type: "web", label: "Página web", desc: "Extraer texto de una URL" },
  { type: "interview", label: "Entrevista AI", desc: "El clon te entrevista para extraer tu conocimiento" },
]

const SILO_BADGES: Record<string, { label: string; kind: "active" | "trial" | "warning" }> = {
  teach: { label: "Pedagogía", kind: "trial" },
  support: { label: "Soporte", kind: "warning" },
  sales: { label: "Ventas", kind: "active" },
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
  }, [])

  useEffect(() => {
    fetchSources()
  }, [fetchSources])

  if (status === "loading" || loading) {
    return <LoadingState label="Cargando biblioteca…" rows={4} />
  }

  if (error) {
    return (
      <ErrorState
        message={error}
        action={
          <button type="button" onClick={fetchSources} className="btn-secondary text-xs">
            Reintentar
          </button>
        }
      />
    )
  }

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Biblioteca de Contenido
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Sube contenido para entrenar a tu clon: PDFs, vídeos de YouTube, texto, y más.
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
            Contenido subido
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
              title="Aún no hay contenido"
              description="Sube tu primer PDF, enlace de YouTube o escribe texto directamente para empezar a entrenar a tu clon."
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
                      {source.silo} · {source.status} · {source.wordCount.toLocaleString("es-ES")} palabras
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
