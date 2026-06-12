"use client"

export const dynamic = "force-dynamic"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { EmptyState } from "@/components/ui/EmptyState"
import { ErrorState } from "@/components/ui/ErrorState"
import { ThemeToggle } from "@/components/ui/ThemeToggle"
import { useRouter } from "@/i18n/navigation"

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
  teach: "Teaching",
  support: "Support",
  sales: "Sales",
}

const TONE_OPTIONS = [
  { value: "formal", label: "Formal" },
  { value: "informal", label: "Informal" },
  { value: "cercano", label: "Friendly" },
  { value: "técnico", label: "Technical" },
]

export default function SettingsPage() {
  const { status } = useSession()
  const router = useRouter()
  const [clone, setClone] = useState<CloneConfig | null>(null)
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const [name, setName] = useState("")
  const [slug, setSlug] = useState("")
  const [description, setDescription] = useState("")
  const [tone, setTone] = useState("")
  const [prompts, setPrompts] = useState<Record<string, string>>({})

  const slugify = (value: string) =>
    value
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "")

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
      setSlug(c.slug || "")
      setDescription(c.description || "")
      setTone(c.personality_tone || "formal")
      const promptMap: Record<string, string> = {}
      if (c.mode_prompts) {
        for (const p of c.mode_prompts) {
          promptMap[p.mode] = p.system_prompt
        }
      }
      setPrompts(promptMap)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error loading settings")
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
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${clone.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, description, personality_tone: tone }),
      })
      if (!res.ok) throw new Error(`Error ${res.status}`)
      setSaved(true)
      setTimeout(() => setSaved(false), 2000)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error saving settings")
    } finally {
      setSaving(false)
    }
  }

  const createClone = async () => {
    const cleanName = name.trim()
    const cleanSlug = slugify(slug || cleanName)
    if (!cleanName || !cleanSlug) return
    setSaving(true)
    setSaved(false)
    setError(null)
    try {
      const res = await fetch("/api/clone/clones", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: cleanName,
          slug: cleanSlug,
          description,
          personality_tone: tone || "formal",
          language: "es",
          active_modes: ["teach", "support", "sales"],
          is_active: true,
        }),
      })
      if (!res.ok) {
        const body = await res.json().catch(() => ({}))
        throw new Error(body.error ?? `Error ${res.status}`)
      }
      await fetchClone()
      setSaved(true)
      setTimeout(() => setSaved(false), 2000)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error creating clone")
    } finally {
      setSaving(false)
    }
  }

  const savePrompt = async (mode: string) => {
    if (!clone) return
    setSaving(true)
    setSaved(false)
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${clone.id}/prompts`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          mode,
          system_prompt: prompts[mode] || "",
          is_active: true,
        }),
      })
      if (!res.ok) throw new Error(`Error ${res.status}`)
      setSaved(true)
      setTimeout(() => setSaved(false), 2000)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error saving prompt")
    } finally {
      setSaving(false)
    }
  }

  if (status === "loading" || loading) {
    return <LoadingState label="Loading settings..." rows={3} />
  }

  if (!clone) {
    return (
      <div className="space-y-6">
        <header>
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            Settings
          </h1>
        </header>
        {error && <ErrorState message={error} />}
        <div className="card max-w-2xl">
          <EmptyState
            title="No clone found"
            description="Create your first clone to start configuring the workspace."
          />
          <div className="mt-6 space-y-4">
            <div>
              <label className="stat-label" htmlFor="new-clone-name">Name</label>
              <input
                id="new-clone-name"
                type="text"
                value={name}
                onChange={(e) => {
                  setName(e.target.value)
                  setSlug(slugify(e.target.value))
                }}
                placeholder="MyOwnClone"
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="new-clone-slug">Public slug</label>
              <input
                id="new-clone-slug"
                type="text"
                value={slug}
                onChange={(e) => setSlug(slugify(e.target.value))}
                placeholder="myownclone"
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="new-clone-description">Description</label>
              <textarea
                id="new-clone-description"
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="mt-1 w-full resize-none rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <button
              type="button"
              onClick={createClone}
              disabled={saving || !name.trim() || !slug.trim()}
              className="btn-primary text-xs disabled:opacity-50"
            >
              {saving ? "Creating..." : "Create clone"}
            </button>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Settings
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Customize your clone: name, personality, tone, and prompts by mode.
        </p>
      </header>

      {saved && (
        <div
          role="status"
          aria-live="polite"
          className="rounded-lg border border-[var(--color-accent-green)]/30 bg-[var(--color-accent-green)]/10 px-4 py-3 text-sm text-[var(--color-accent-green)]"
        >
          Changes saved successfully.
        </div>
      )}

      {error && <ErrorState message={error} />}

      <div className="space-y-4">
        <div className="card">
          <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Appearance
          </h3>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-[var(--text-primary)]">Theme</p>
              <p className="text-xs text-[var(--text-muted)]">
                Light or dark. Saved in this browser.
              </p>
            </div>
            <ThemeToggle showLabel />
          </div>
        </div>

        <div className="card">
          <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Clone identity
          </h3>
          <div className="space-y-4">
            <div>
              <label className="stat-label" htmlFor="cfg-name">Name</label>
              <input
                id="cfg-name"
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="cfg-slug">Public slug</label>
              <input
                id="cfg-slug"
                type="text"
                value={clone.slug}
                disabled
                className="mt-1 w-full cursor-not-allowed rounded-lg border border-[var(--border-soft)] bg-[var(--surface-3)] px-3 py-2 text-sm text-[var(--text-muted)]"
              />
              <p className="mt-1 font-mono text-[10px] text-[var(--text-muted)]">
                {clone.slug}.myownclone.com
              </p>
            </div>
            <div>
              <label className="stat-label" htmlFor="cfg-desc">Description</label>
              <textarea
                id="cfg-desc"
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="mt-1 w-full resize-none rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="cfg-tone">Tone</label>
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
              {saving ? "Saving..." : "Save changes"}
            </button>
          </div>
        </div>

        <div className="card">
          <h3 className="mb-2 text-sm font-semibold text-[var(--text-primary)]">
            Mode prompts
          </h3>
          <p className="mb-4 text-xs text-[var(--text-muted)]">
            Define how your clone behaves in each mode. These prompts are used as the base system instructions.
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
                  className="mt-1 w-full resize-none rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 font-mono text-xs text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
                />
                <div className="mt-2 flex justify-end">
                  <button
                    type="button"
                    onClick={() => savePrompt(mode)}
                    disabled={saving}
                    className="btn-secondary text-xs disabled:opacity-50"
                  >
                    {saving ? "Saving..." : "Save prompt"}
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
