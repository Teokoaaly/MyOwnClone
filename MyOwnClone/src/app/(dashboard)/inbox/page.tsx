"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"

interface EmailListItem {
  id: string
  clone_id: string
  from_email?: string | null
  from_name?: string | null
  subject?: string | null
  body_text?: string | null
  status: string
  classification?: string | null
  has_draft: boolean
  received_at?: number | null
}

interface EmailDetail extends EmailListItem {
  body_html?: string | null
  draft_reply?: string | null
  labels?: string[]
}

const STATUS_FILTERS = [
  { id: "all", label: "Todos" },
  { id: "pending", label: "Pendientes" },
  { id: "sent", label: "Enviados" },
  { id: "discarded", label: "Descartados" },
]

const CLASS_COLORS: Record<string, string> = {
  consulta: "badge-trial",
  queja: "badge-error",
  venta: "badge-active",
  soporte: "badge-warning",
  otro: "badge-trial",
}

export default function InboxPage() {
  const { status: authStatus } = useSession()
  const router = useRouter()
  const [activeFilter, setActiveFilter] = useState("all")
  const [emails, setEmails] = useState<EmailListItem[]>([])
  const [selected, setSelected] = useState<EmailDetail | null>(null)
  const [loading, setLoading] = useState(true)
  const [detailLoading, setDetailLoading] = useState(false)
  const [draftText, setDraftText] = useState("")
  const [saving, setSaving] = useState(false)
  const [generating, setGenerating] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (authStatus === "unauthenticated") router.push("/login")
  }, [authStatus, router])

  const fetchList = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const params = new URLSearchParams()
      if (activeFilter !== "all") params.set("status", activeFilter)
      const res = await fetch(`/api/clone/inbox/list?${params}`)
      if (res.ok) {
        const data = await res.json()
        setEmails(Array.isArray(data) ? data : data.items ?? [])
      } else {
        throw new Error(`Error ${res.status}`)
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error al cargar")
    } finally {
      setLoading(false)
    }
  }, [activeFilter])

  useEffect(() => {
    fetchList()
  }, [fetchList])

  const selectEmail = async (id: string) => {
    setDetailLoading(true)
    try {
      const res = await fetch(`/api/clone/inbox/${id}`)
      if (res.ok) {
        const data: EmailDetail = await res.json()
        setSelected(data)
        setDraftText(data.draft_reply || "")
      }
    } catch {
      // Keep selection
    } finally {
      setDetailLoading(false)
    }
  }

  const generateDraft = async () => {
    if (!selected) return
    setGenerating(true)
    try {
      const res = await fetch(`/api/clone/inbox/${selected.id}/generate-draft`, {
        method: "POST",
      })
      if (res.ok) {
        const data = await res.json()
        setDraftText(data.body)
        setSelected({ ...selected, draft_reply: data.body })
      }
    } catch {
      setError("Error al generar borrador")
    } finally {
      setGenerating(false)
    }
  }

  const saveDraft = async () => {
    if (!selected) return
    setSaving(true)
    try {
      const res = await fetch(`/api/clone/inbox/${selected.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          draft_reply: draftText,
        }),
      })
      if (res.ok) {
        setSelected({ ...selected, draft_reply: draftText })
      }
    } catch {
      setError("Error al guardar")
    } finally {
      setSaving(false)
    }
  }

  const sendEmail = async () => {
    if (!selected || !draftText.trim()) return
    if (!confirm("¿Enviar esta respuesta al destinatario?")) return
    setSaving(true)
    try {
      const res = await fetch(`/api/clone/inbox/${selected.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ draft_reply: draftText, status: "sent" }),
      })
      if (res.ok) {
        setSelected(null)
        fetchList()
      }
    } catch {
      setError("Error al enviar")
    } finally {
      setSaving(false)
    }
  }

  const discardEmail = async () => {
    if (!selected) return
    if (!confirm("¿Descartar este email?")) return
    try {
      await fetch(`/api/clone/inbox/${selected.id}`, { method: "DELETE" })
      setSelected(null)
      fetchList()
    } catch {
      setError("Error al descartar")
    }
  }

  if (authStatus === "loading") {
    return <LoadingState label="Verificando sesión…" />
  }

  return (
    <div className="flex h-[calc(100vh-0px)] gap-4">
      {/* Sidebar list */}
      <div className="w-80 shrink-0 flex flex-col card !p-0 overflow-hidden">
        <div className="px-4 py-4 border-b border-[var(--border-soft)]">
          <h1 className="text-lg font-semibold text-[var(--text-primary)]">Inbox</h1>
        </div>

        {/* Filters */}
        <div className="px-3 py-2 flex gap-1 overflow-x-auto border-b border-[var(--border-soft)]">
          {STATUS_FILTERS.map((f) => (
            <button
              key={f.id}
              type="button"
              onClick={() => setActiveFilter(f.id)}
              aria-pressed={activeFilter === f.id}
              className={[
                "flex items-center gap-1 px-2.5 py-1.5 rounded-md text-xs font-medium whitespace-nowrap transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]",
                activeFilter === f.id
                  ? "bg-[var(--color-accent-warm)] text-white"
                  : "text-[var(--text-secondary)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)]",
              ].join(" ")}
            >
              {f.label}
            </button>
          ))}
        </div>

        {/* Email list */}
        <div className="flex-1 overflow-y-auto">
          {error ? (
            <div className="p-4">
              <ErrorState message={error} />
            </div>
          ) : loading ? (
            <div className="p-4">
              <LoadingState rows={4} />
            </div>
          ) : emails.length === 0 ? (
            <div className="p-4">
              <EmptyState
                title="No hay emails"
                description={
                  activeFilter !== "all"
                    ? `Sin emails en estado "${activeFilter}".`
                    : "Cuando lleguen correos a tu clon aparecerán aquí."
                }
              />
            </div>
          ) : (
            emails.map((email) => (
              <button
                key={email.id}
                type="button"
                onClick={() => selectEmail(email.id)}
                aria-current={selected?.id === email.id ? "true" : undefined}
                className={[
                  "w-full text-left px-4 py-3 border-b border-[var(--border-soft)] transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]",
                  selected?.id === email.id
                    ? "bg-[var(--surface-2)] border-l-2 border-l-[var(--color-accent-warm)]"
                    : "hover:bg-[var(--surface-2)]",
                ].join(" ")}
              >
                <div className="flex items-center justify-between gap-2">
                  <p className="text-sm font-medium text-[var(--text-primary)] truncate">
                    {email.from_name || email.from_email || "Desconocido"}
                  </p>
                  {email.classification && (
                    <span className={CLASS_COLORS[email.classification] || "badge-trial"}>
                      {email.classification}
                    </span>
                  )}
                </div>
                <p className="text-xs text-[var(--text-secondary)] truncate mt-0.5">
                  {email.subject || "(sin asunto)"}
                </p>
                <div className="flex items-center gap-2 mt-1">
                  {email.has_draft && (
                    <span className="text-[10px] text-[var(--color-accent-violet)] font-medium">
                      Borrador
                    </span>
                  )}
                  {email.status === "sent" && (
                    <span className="text-[10px] text-[var(--color-accent-green)] font-medium">
                      Enviado
                    </span>
                  )}
                  <span className="text-[10px] text-[var(--text-muted)] ml-auto">
                    {email.received_at
                      ? new Date(email.received_at * 1000).toLocaleDateString("es-ES")
                      : ""}
                  </span>
                </div>
              </button>
            ))
          )}
        </div>
      </div>

      {/* Detail panel */}
      <div className="flex-1 flex flex-col card !p-0 overflow-hidden">
        {!selected ? (
          <div className="flex-1 flex items-center justify-center text-center px-8">
            <div>
              <p className="text-base font-medium text-[var(--text-primary)]">
                Selecciona un email
              </p>
              <p className="mt-1 text-sm text-[var(--text-muted)]">
                El clon propone respuestas. Tú revisas y envías.
              </p>
            </div>
          </div>
        ) : detailLoading ? (
          <div className="flex-1 flex items-center justify-center">
            <LoadingState label="Cargando email…" rows={2} />
          </div>
        ) : (
          <>
            {/* Email header */}
            <div className="px-6 py-4 border-b border-[var(--border-soft)]">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1 min-w-0">
                  <h2 className="text-lg font-semibold text-[var(--text-primary)]">
                    {selected.subject || "(sin asunto)"}
                  </h2>
                  <p className="text-sm text-[var(--text-secondary)] mt-1">
                    De: <strong>{selected.from_name || selected.from_email}</strong>
                    {" · "}
                    {selected.received_at
                      ? new Date(selected.received_at * 1000).toLocaleString("es-ES")
                      : ""}
                  </p>
                  {selected.classification && (
                    <span className={`inline-block mt-2 ${CLASS_COLORS[selected.classification] || "badge-trial"}`}>
                      {selected.classification}
                    </span>
                  )}
                </div>
                <div className="flex gap-2">
                  <button
                    type="button"
                    onClick={discardEmail}
                    className="btn-secondary text-xs"
                  >
                    Descartar
                  </button>
                </div>
              </div>
            </div>

            {/* Email body */}
            <div className="px-6 py-4 border-b border-[var(--border-soft)] max-h-60 overflow-y-auto">
              <p className="text-sm text-[var(--text-secondary)] whitespace-pre-wrap">
                {selected.body_text || "(sin contenido)"}
              </p>
            </div>

            {/* Draft editor */}
            <div className="flex-1 flex flex-col p-6">
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-sm font-semibold text-[var(--text-primary)]">
                  Respuesta propuesta
                </h3>
                <button
                  type="button"
                  onClick={generateDraft}
                  disabled={generating}
                  className="btn-secondary text-xs disabled:opacity-50"
                >
                  {generating ? "Generando…" : "Generar con IA"}
                </button>
              </div>

              <textarea
                value={draftText}
                onChange={(e) => setDraftText(e.target.value)}
                rows={10}
                placeholder="La respuesta propuesta por el clon aparecerá aquí. Puedes editarla antes de enviar."
                className="flex-1 w-full px-4 py-3 text-sm rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] text-[var(--text-primary)] placeholder:text-[var(--text-muted)] focus:border-[var(--color-accent-warm)] focus:outline-none resize-none"
              />

              {error && (
                <p role="alert" className="mt-2 text-xs badge-error inline-block">{error}</p>
              )}

              <div className="flex gap-2 mt-4">
                <button
                  type="button"
                  onClick={sendEmail}
                  disabled={saving || !draftText.trim()}
                  className="btn-primary text-xs disabled:opacity-50"
                >
                  {saving ? "Enviando…" : "Enviar respuesta"}
                </button>
                <button
                  type="button"
                  onClick={saveDraft}
                  disabled={saving || !draftText.trim()}
                  className="btn-secondary text-xs disabled:opacity-50"
                >
                  Guardar borrador
                </button>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  )
}
