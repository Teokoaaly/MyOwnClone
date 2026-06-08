"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

interface Memory {
  id: string
  clone_id: string
  type: "memory" | "signature" | "template"
  content: string
  trigger_condition?: string | null
  priority: number
  created_at: number
  updated_at?: number | null
}

type TabType = "memory" | "signature" | "template"

const TABS: { id: TabType; label: string; emoji: string; desc: string }[] = [
  {
    id: "memory",
    label: "Memorias",
    emoji: "🧠",
    desc: "Fragmentos de información que tu clon recordará siempre. Datos clave, políticas o información personal.",
  },
  {
    id: "signature",
    label: "Firmas",
    emoji: "✍️",
    desc: "Formato HTML que se aplicará al final de los emails enviados por tu clon.",
  },
  {
    id: "template",
    label: "Plantillas",
    emoji: "📋",
    desc: "Respuestas predefinidas que tu clon usará cuando se cumplan ciertas condiciones.",
  },
]

const EXAMPLE_CONTENT: Record<TabType, string> = {
  memory: "Mi curso completo de marketing digital incluye 12 módulos, desde fundamentos hasta estrategias avanzadas de conversión.",
  signature: '<div style="font-family: Arial; color: #666;">\n  <p>Saludos cordiales,</p>\n  <p><strong>[Nombre del creador]</strong></p>\n  <p style="font-size:12px;">[Cargo] | [Web]</p>\n</div>',
  template: "Gracias por tu interés en el curso. Actualmente ofrecemos un descuento del 20% para nuevos estudiantes usando el código BIENVENIDA20.",
}

export default function CerebroPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [activeTab, setActiveTab] = useState<TabType>("memory")
  const [memories, setMemories] = useState<Memory[]>([])
  const [loading, setLoading] = useState(true)
  const [editing, setEditing] = useState<Memory | null>(null)
  const [formContent, setFormContent] = useState("")
  const [formTrigger, setFormTrigger] = useState("")
  const [formPriority, setFormPriority] = useState(0)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/login")
    }
  }, [status, router])

  const fetchMemories = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetch(
        `/api/clone/memories?type=${activeTab}`
      )
      if (res.ok) {
        setMemories(await res.json())
      }
    } catch {
      // Empty state handled below
    } finally {
      setLoading(false)
    }
  }, [activeTab])

  useEffect(() => {
    fetchMemories()
  }, [fetchMemories])

  const resetForm = () => {
    setEditing(null)
    setFormContent("")
    setFormTrigger("")
    setFormPriority(0)
    setError(null)
  }

  const startNew = () => {
    resetForm()
  }

  const startEdit = (m: Memory) => {
    setEditing(m)
    setFormContent(m.content)
    setFormTrigger(m.trigger_condition || "")
    setFormPriority(m.priority)
    setError(null)
  }

  const save = async () => {
    if (!formContent.trim()) return
    setSaving(true)
    setError(null)
    try {
      const url = editing
        ? `/api/clone/memories/${editing.id}`
        : "/api/clone/memories"
      const method = editing ? "PUT" : "POST"
      const res = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          type: activeTab,
          content: formContent,
          trigger_condition: formTrigger || null,
          priority: formPriority,
        }),
      })
      if (!res.ok) throw new Error("Error al guardar")
      resetForm()
      fetchMemories()
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error desconocido")
    } finally {
      setSaving(false)
    }
  }

  const remove = async (id: string) => {
    if (!confirm("¿Eliminar este elemento?")) return
    try {
      await fetch(`/api/clone/memories/${id}`, { method: "DELETE" })
      fetchMemories()
    } catch {
      // Ignore
    }
  }

  if (status === "loading") {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="flex gap-1">
          <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:0ms]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:150ms]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:300ms]" />
        </div>
      </div>
    )
  }

  const activeTabInfo = TABS.find((t) => t.id === activeTab)!

  return (
    <div className="p-8">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Cerebro
          </h1>
          <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
            {activeTabInfo.desc}
          </p>
        </div>
      </div>

      <div className="flex gap-2 mb-6">
        {TABS.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              activeTab === tab.id
                ? "bg-purple-600 text-white shadow-lg shadow-purple-600/25"
                : "bg-white dark:bg-gray-900 text-gray-600 dark:text-gray-400 border border-gray-200 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800"
            }`}
          >
            <span>{tab.emoji}</span>
            {tab.label}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-3">
          {loading ? (
            <div className="text-center py-12 text-gray-400">Cargando...</div>
          ) : memories.length === 0 ? (
            <div className="text-center py-12 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800">
              <p className="text-gray-400">
                No hay {activeTabInfo.label.toLowerCase()} todavía.
              </p>
            </div>
          ) : (
            memories.map((m) => (
              <div
                key={m.id}
                className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-4 group"
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex-1 min-w-0">
                    <p className="text-sm text-gray-900 dark:text-white whitespace-pre-wrap">
                      {m.content}
                    </p>
                    {m.trigger_condition && (
                      <p className="mt-1 text-xs text-purple-600 dark:text-purple-400">
                        Gatillo: {m.trigger_condition}
                      </p>
                    )}
                    <p className="mt-2 text-xs text-gray-400">
                      Prioridad: {m.priority} ·{" "}
                      {new Date(m.created_at * 1000).toLocaleDateString("es-ES")}
                    </p>
                  </div>
                  <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                    <button
                      onClick={() => startEdit(m)}
                      className="p-1 text-gray-400 hover:text-purple-600 text-xs"
                    >
                      ✏️
                    </button>
                    <button
                      onClick={() => remove(m.id)}
                      className="p-1 text-gray-400 hover:text-red-500 text-xs"
                    >
                      🗑️
                    </button>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>

        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-5 sticky top-8">
          <h3 className="font-semibold text-gray-900 dark:text-white text-sm mb-4">
            {editing ? "Editar" : "Nueva"} {activeTabInfo.label.slice(0, -1)}
          </h3>

          <div className="space-y-3">
            <div>
              <label className="block text-xs font-medium text-gray-600 dark:text-gray-400 mb-1">
                Contenido
              </label>
              <textarea
                value={formContent}
                onChange={(e) => setFormContent(e.target.value)}
                rows={5}
                placeholder={
                  activeTab === "memory"
                    ? "Información que el clon debe recordar..."
                    : activeTab === "signature"
                    ? "<div>Firma HTML...</div>"
                    : "Texto de la respuesta automática..."
                }
                className="w-full px-3 py-2 text-sm border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none resize-none"
              />
            </div>

            {activeTab === "template" && (
              <div>
                <label className="block text-xs font-medium text-gray-600 dark:text-gray-400 mb-1">
                  Palabras clave (gatillo)
                </label>
                <input
                  type="text"
                  value={formTrigger}
                  onChange={(e) => setFormTrigger(e.target.value)}
                  placeholder="ej: descuento, precio, oferta"
                  className="w-full px-3 py-2 text-sm border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none"
                />
              </div>
            )}

            <div>
              <label className="block text-xs font-medium text-gray-600 dark:text-gray-400 mb-1">
                Prioridad
              </label>
              <select
                value={formPriority}
                onChange={(e) => setFormPriority(Number(e.target.value))}
                className="w-full px-3 py-2 text-sm border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none"
              >
                <option value={0}>0 — Normal</option>
                <option value={1}>1 — Alta</option>
                <option value={2}>2 — Urgente</option>
                <option value={3}>3 — Crítica</option>
              </select>
            </div>

            {error && (
              <p className="text-xs text-red-500 bg-red-50 dark:bg-red-950 rounded-lg px-3 py-2">
                {error}
              </p>
            )}

            <div className="flex gap-2 pt-2">
              <button
                onClick={save}
                disabled={saving || !formContent.trim()}
                className="flex-1 px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {saving ? "Guardando..." : editing ? "Actualizar" : "Crear"}
              </button>
              {editing && (
                <button
                  onClick={resetForm}
                  className="px-4 py-2 text-sm text-gray-600 dark:text-gray-400 border border-gray-200 dark:border-gray-700 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800"
                >
                  Cancelar
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
