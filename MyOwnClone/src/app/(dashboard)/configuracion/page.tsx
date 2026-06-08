"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import { LoadingState } from "@/components/ui/LoadingState"
import { EmptyState } from "@/components/ui/EmptyState"
import { ThemeToggle } from "@/components/ui/ThemeToggle"

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
  const { status } = useSession()
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
    return <LoadingState label="Cargando configuración…" rows={3} />
  }

  if (!clone) {
    return (
      <div className="space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            Configuración
          </h1>
        </header>
        <EmptyState
          title="No se encontró ningún clon"
          description="Crea tu primer clon para empezar a configurar el workspace."
        />
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Configuración
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Personaliza tu clon: nombre, personalidad, tono y prompts por modo.
        </p>
      </header>

      {saved && (
        <div
          role="status"
          aria-live="polite"
          className="rounded-lg border border-[var(--color-accent-green)]/30 bg-[var(--color-accent-green)]/10 px-4 py-3 text-sm text-[var(--color-accent-green)]"
        >
          Cambios guardados correctamente.
        </div>
      )}

      <div className="space-y-4">
        {/* Preferences: theme */}
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">
            Apariencia
          </h3>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-[var(--text-primary)]">Tema</p>
              <p className="text-xs text-[var(--text-muted)]">
                Claro u oscuro. Se guarda en este navegador.
              </p>
            </div>
            <ThemeToggle showLabel />
          </div>
        </div>

        {/* Identity */}
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">
            Identidad del clon
          </h3>
          <div className="space-y-4">
            <div>
              <label className="stat-label" htmlFor="cfg-name">Nombre</label>
              <input
                id="cfg-name"
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="cfg-slug">Slug público</label>
              <input
                id="cfg-slug"
                type="text"
                value={clone.slug}
                disabled
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-3)] px-3 py-2 text-sm text-[var(--text-muted)] cursor-not-allowed"
              />
              <p className="mt-1 text-[10px] text-[var(--text-muted)] font-mono">
                {clone.slug}.myownclone.com
              </p>
            </div>
            <div>
              <label className="stat-label" htmlFor="cfg-desc">Descripción</label>
              <textarea
                id="cfg-desc"
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none resize-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="cfg-tone">Tono</label>
              <select
                id="cfg-tone"
                value={tone}
                onChange={(e) => setTone(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              >
                {TONE_OPTIONS.map((opt) => (
                  <option key={opt.value} value={opt.value}>
                    {opt.label}
                  </option>
                ))}
              </select>
            </div>
            <button
              type="button"
              onClick={saveProfile}
              disabled={saving}
              className="btn-primary text-xs disabled:opacity-50"
            >
              {saving ? "Guardando…" : "Guardar cambios"}
            </button>
          </div>
        </div>

        {/* Mode prompts */}
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-2">
            Prompts por modo
          </h3>
          <p className="text-xs text-[var(--text-muted)] mb-4">
            Define cómo se comporta tu clon en cada modo. Estos prompts se usan como sistema base para las respuestas.
          </p>
          <div className="space-y-4">
            {["teach", "support", "sales"].map((mode) => (
              <div key={mode}>
                <label className="stat-label" htmlFor={`cfg-prompt-${mode}`}>{SILO_LABELS[mode] || mode}</label>
                <textarea
                  id={`cfg-prompt-${mode}`}
                  rows={4}
                  value={prompts[mode] || ""}
                  onChange={(e) =>
                    setPrompts((prev) => ({ ...prev, [mode]: e.target.value }))
                  }
                  className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none resize-none font-mono text-xs"
                />
                <div className="mt-2 flex justify-end">
                  <button
                    type="button"
                    onClick={() => savePrompt(mode)}
                    disabled={saving}
                    className="btn-secondary text-xs disabled:opacity-50"
                  >
                    {saving ? "Guardando…" : "Guardar prompt"}
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
