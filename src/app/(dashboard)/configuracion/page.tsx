"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

interface CloneConfig {
  id: string
  tenant_id: string
  name: string
  slug: string
  description: string | null
  avatar_url: string | null
  personality_tone: string | null
  language: string
  active_modes: string[]
  is_active: boolean
  mode_prompts: ModePrompt[]
}

interface ModePrompt {
  id: string
  mode: string
  system_prompt: string
  is_active: boolean
}

const SILO_LABELS: Record<string, string> = {
  teach: "Pedagogía",
  support: "Soporte",
  sales: "Ventas",
}

const TONE_OPTIONS = [
  { value: "formal", label: "Formal" },
  { value: "informal", label: "Informal" },
  { value: "cercano", label: "Cercano" },
  { value: "técnico", label: "Técnico" },
]

export default function ConfiguracionPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [clone, setClone] = useState<CloneConfig | null>(null)
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)

  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [tone, setTone] = useState("")
  const [prompts, setPrompts] = useState<Record<string, string>>({})

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchClone = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetch("/api/clone/clones")
      if (!res.ok) return
      const clones = await res.json()
      if (clones.length === 0) return
      const c = clones[0]
      setClone(c)
      setName(c.name || "")
      setDescription(c.description || "")
      setTone(c.personality_tone || "formal")
      const promptMap: Record<string, string> = {}
      if (c.mode_prompts) {
        for (const p of c.mode_prompts) {
          promptMap[p.mode] = p.system_prompt
        }
      }
      setPrompts(promptMap)
    } catch {
      // Empty state
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchClone()
  }, [fetchClone])

  const saveProfile = async () => {
    if (!clone) return
    setSaving(true)
    setSaved(false)
    try {
      await fetch(`/api/clone/clones/${clone.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description, personality_tone: tone }),
      })
      setSaved(true)
      setTimeout(() => setSaved(false), 2000)
    } catch {
      // Error state handled silently
    } finally {
      setSaving(false)
    }
  }

  const savePrompt = async (mode: string) => {
    if (!clone) return
    setSaving(true)
    setSaved(false)
    try {
      await fetch(`/api/clone/clones/${clone.id}/prompts`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          mode,
          system_prompt: prompts[mode] || "",
          is_active: true,
        }),
      })
      setSaved(true)
      setTimeout(() => setSaved(false), 2000)
    } catch {
      // Error state
    } finally {
      setSaving(false)
    }
  }

  if (status === "loading" || loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="flex gap-1">
          <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:150ms]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:300ms]" />
        </div>
      </div>
    )
  }

  if (!clone) {
    return (
      <div className="p-8 text-center text-gray-500 dark:text-gray-400">
        <p className="text-lg">No se encontró ningún clon.</p>
        <p className="mt-2 text-sm">Crea tu primer clon para empezar.</p>
      </div>
    )
  }

  return (
    <div className="p-8">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Configuración
        </h1>
        <p className="mt-1 text-gray-500 dark:text-gray-400">
          Personaliza tu clon: nombre, personalidad, tono y prompts por modo.
        </p>
      </div>

      {saved && (
        <div className="mb-4 rounded-lg border border-green-800 bg-green-950/50 px-4 py-3 text-sm text-green-300">
          Cambios guardados correctamente.
        </div>
      )}

      <div className="space-y-6">
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Identidad del clon
          </h3>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Nombre
              </label>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Slug público
              </label>
              <input
                type="text"
                value={clone.slug}
                disabled
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-100 dark:bg-gray-800/50 text-gray-500 dark:text-gray-400 outline-none cursor-not-allowed"
              />
              <p className="mt-1 text-xs text-gray-400">
                {clone.slug}.replica.tudominio.com
              </p>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Descripción
              </label>
              <textarea
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none resize-none"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Tono
              </label>
              <select
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none"
              >
                {TONE_OPTIONS.map((opt) => (
                  <option key={opt.value} value={opt.value}>
                    {opt.label}
                  </option>
                ))}
              </select>
            </div>
            <button
              onClick={saveProfile}
              disabled={saving}
              className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50"
            >
              {saving ? "Guardando..." : "Guardar cambios"}
            </button>
          </div>
        </div>

        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Prompts por modo
          </h3>
          <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">
            Define cómo se comporta tu clon en cada modo. Estos prompts se usan como sistema base para las respuestas.
          </p>
          <div className="space-y-4">
            {["teach", "support", "sales"].map((mode) => (
              <div key={mode}>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                  {SILO_LABELS[mode] || mode}
                </label>
                <textarea
                  rows={4}
                  value={prompts[mode] || ""}
                  onChange={(e) =>
                    setPrompts((prev) => ({ ...prev, [mode]: e.target.value }))
                  }
                  className="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none resize-none font-mono text-xs"
                />
                <div className="mt-2 flex justify-end">
                  <button
                    onClick={() => savePrompt(mode)}
                    disabled={saving}
                    className="px-3 py-1.5 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 text-xs font-medium rounded-lg border border-gray-200 dark:border-gray-700 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors disabled:opacity-50"
                  >
                    {saving ? "Guardando..." : "Guardar prompt"}
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
