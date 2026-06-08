"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

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
  { id: "all", label: "Todos", emoji: "📬" },
  { id: "pending", label: "Pendientes", emoji: "📨" },
  { id: "sent", label: "Enviados", emoji: "✅" },
  { id: "discarded", label: "Descartados", emoji: "🗑️" },
]

const CLASS_COLORS: Record<string, string> = {
  consulta: "bg-blue-100 text-blue-700 dark:bg-blue-950 dark:text-blue-300",
  queja: "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300",
  venta: "bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300",
  soporte: "bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300",
  otro: "bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300",
}

export default function InboxPage() {
  const { data: session, status: authStatus } = useSession()
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
    try {
      const params = new URLSearchParams()
      if (activeFilter !== "all") params.set("status", activeFilter)
      const res = await fetch(`/api/clone/inbox/list?${params}`)
      if (res.ok) setEmails(await res.json())
    } catch {
      // Empty
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
          status: undefined,
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
    return <div className="flex h-64 items-center justify-center"><div className="animate-spin h-6 w-6 border-2 border-purple-600 border-t-transparent rounded-full" /></div>
  }

  return (
    <div className="flex h-[calc(100vh-0px)]">
      {/* Sidebar list */}
      <div className="w-80 border-r border-gray-200 dark:border-gray-800 flex flex-col">
        <div className="px-4 py-4 border-b border-gray-200 dark:border-gray-800">
          <h1 className="text-lg font-bold text-gray-900 dark:text-white">Inbox</h1>
        </div>

        {/* Filters */}
        <div className="px-3 py-2 flex gap-1 overflow-x-auto">
          {STATUS_FILTERS.map((f) => (
            <button
              key={f.id}
              onClick={() => setActiveFilter(f.id)}
              className={`flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition-colors ${
                activeFilter === f.id
                  ? "bg-purple-600 text-white"
                  : "text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800"
              }`}
            >
              <span>{f.emoji}</span>
              {f.label}
            </button>
          ))}
        </div>

        {/* Email list */}
        <div className="flex-1 overflow-y-auto">
          {loading ? (
            <div className="text-center py-12 text-gray-400 text-sm">Cargando...</div>
          ) : emails.length === 0 ? (
            <div className="text-center py-12 px-4">
              <p className="text-2xl mb-2">📭</p>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                No hay emails{activeFilter !== "all" ? ` "${activeFilter}"` : ""}
              </p>
            </div>
          ) : (
            emails.map((email) => (
              <button
                key={email.id}
                onClick={() => selectEmail(email.id)}
                className={`w-full text-left px-4 py-3 border-b border-gray-100 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-colors ${
                  selected?.id === email.id ? "bg-purple-50 dark:bg-purple-950/20 border-l-2 border-l-purple-600" : ""
                }`}
              >
                <div className="flex items-center justify-between gap-2">
                  <p className="text-sm font-medium text-gray-900 dark:text-white truncate">
                    {email.from_name || email.from_email || "Desconocido"}
                  </p>
                  {email.classification && (
                    <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-medium whitespace-nowrap ${CLASS_COLORS[email.classification] || ""}`}>
                      {email.classification}
                    </span>
                  )}
                </div>
                <p className="text-xs text-gray-600 dark:text-gray-400 truncate mt-0.5">
                  {email.subject || "(sin asunto)"}
                </p>
                <div className="flex items-center gap-2 mt-1">
                  {email.has_draft && (
                    <span className="text-[10px] text-purple-600 font-medium">✍️ Borrador</span>
                  )}
                  {email.status === "sent" && (
                    <span className="text-[10px] text-green-600 font-medium">✅ Enviado</span>
                  )}
                  <span className="text-[10px] text-gray-400 ml-auto">
                    {email.received_at ? new Date(email.received_at * 1000).toLocaleDateString("es-ES") : ""}
                  </span>
                </div>
              </button>
            ))
          )}
        </div>
      </div>

      {/* Detail panel */}
      <div className="flex-1 flex flex-col bg-white dark:bg-gray-900">
        {!selected ? (
          <div className="flex-1 flex items-center justify-center text-center px-8">
            <div>
              <p className="text-4xl mb-3">📧</p>
              <p className="text-lg font-medium text-gray-900 dark:text-white">
                Selecciona un email
              </p>
              <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
                El clon propone respuestas. Tú revisas y envías.
              </p>
            </div>
          </div>
        ) : detailLoading ? (
          <div className="flex-1 flex items-center justify-center">
            <div className="animate-spin h-6 w-6 border-2 border-purple-600 border-t-transparent rounded-full" />
          </div>
        ) : (
          <>
            {/* Email header */}
            <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-800">
              <div className="flex items-start justify-between gap-4">
                <div className="flex-1 min-w-0">
                  <h2 className="text-lg font-semibold text-gray-900 dark:text-white">
                    {selected.subject || "(sin asunto)"}
                  </h2>
                  <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                    De: <strong>{selected.from_name || selected.from_email}</strong>
                    {" · "}
                    {selected.received_at
                      ? new Date(selected.received_at * 1000).toLocaleString("es-ES")
                      : ""}
                  </p>
                  {selected.classification && (
                    <span className={`inline-block mt-2 text-xs px-2 py-0.5 rounded-full font-medium ${CLASS_COLORS[selected.classification] || ""}`}>
                      {selected.classification}
                    </span>
                  )}
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={discardEmail}
                    className="px-3 py-1.5 text-xs text-red-600 border border-red-200 dark:border-red-800 rounded-lg hover:bg-red-50 dark:hover:bg-red-950"
                  >
                    🗑️ Descartar
                  </button>
                </div>
              </div>
            </div>

            {/* Email body */}
            <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-800 max-h-60 overflow-y-auto">
              <p className="text-sm text-gray-700 dark:text-gray-300 whitespace-pre-wrap">
                {selected.body_text || "(sin contenido)"}
              </p>
            </div>

            {/* Draft editor */}
            <div className="flex-1 flex flex-col p-6">
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-sm font-semibold text-gray-900 dark:text-white">
                  ✍️ Respuesta propuesta
                </h3>
                <button
                  onClick={generateDraft}
                  disabled={generating}
                  className="px-3 py-1.5 text-xs font-medium text-purple-600 border border-purple-200 dark:border-purple-800 rounded-lg hover:bg-purple-50 dark:hover:bg-purple-950 disabled:opacity-50 transition-colors"
                >
                  {generating ? "Generando..." : "🤖 Generar con IA"}
                </button>
              </div>

              <textarea
                value={draftText}
                onChange={(e) => setDraftText(e.target.value)}
                rows={10}
                placeholder="La respuesta propuesta por el clon aparecerá aquí. Puedes editarla antes de enviar."
                className="flex-1 w-full px-4 py-3 text-sm border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none resize-none"
              />

              {error && (
                <p className="mt-2 text-xs text-red-500">{error}</p>
              )}

              <div className="flex gap-2 mt-4">
                <button
                  onClick={sendEmail}
                  disabled={saving || !draftText.trim()}
                  className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  {saving ? "Enviando..." : "📤 Enviar respuesta"}
                </button>
                <button
                  onClick={saveDraft}
                  disabled={saving || !draftText.trim()}
                  className="px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-400 border border-gray-200 dark:border-gray-700 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 disabled:opacity-50 transition-colors"
                >
                  💾 Guardar borrador
                </button>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  )
}
