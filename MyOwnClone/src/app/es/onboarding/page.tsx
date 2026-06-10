"use client"

import { useState } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { useRouter } from "@/i18n/navigation"

const STEPS = [
  { id: "name", title: "Clone name", subtitle: "What should your assistant be called?" },
  { id: "personality", title: "Personality", subtitle: "Choose your clone's tone" },
  { id: "language", title: "Language", subtitle: "Which language should it speak?" },
  { id: "confirm", title: "Confirm", subtitle: "Review and create your clone" },
]

const TONES = [
  { value: "formal", label: "Formal", emoji: "👔" },
  { value: "informal", label: "Informal", emoji: "👋" },
  { value: "cercano", label: "Friendly", emoji: "🤝" },
  { value: "técnico", label: "Technical", emoji: "🔧" },
]

const LANGUAGES = [
  { value: "es", label: "Spanish", emoji: "🇪🇸" },
  { value: "en", label: "English", emoji: "🇬🇧" },
]

export default function OnboardingPage() {
  const { status } = useSession()
  const router = useRouter()
  const [step, setStep] = useState(0)
  const [name, setName] = useState("")
  const [slug, setSlug] = useState("")
  const [tone, setTone] = useState("formal")
  const [language, setLanguage] = useState("es")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  if (status === "loading") {
    return (
      <main className="flex min-h-screen items-center justify-center" style={{ background: "var(--bg-page)" }}>
        <LoadingState label="Checking session..." />
      </main>
    )
  }
  if (status === "unauthenticated") {
    router.push("/login")
    return null
  }

  const generateSlug = (n: string) =>
    n.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")

  const canNext = () => {
    if (step === 0) return name.length >= 2
    return true
  }

  const handleCreate = async () => {
    setLoading(true)
    setError("")
    try {
      const finalSlug = slug || generateSlug(name)
      const res = await fetch("/api/clone/clones", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          slug: finalSlug,
          language,
          personality_tone: tone,
          active_modes: ["teach", "support", "sales"],
        }),
      })
      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        throw new Error(data.error || "Error creating clone")
      }
      router.push("/resumen")
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error creating clone")
    } finally {
      setLoading(false)
    }
  }

  return (
    <main
      className="flex min-h-screen flex-col items-center justify-center px-4 py-8"
      style={{ background: "var(--bg-page)" }}
    >
      <div className="w-full max-w-lg">
        <ol
          aria-label="Setup steps"
          className="mb-8 flex gap-2"
        >
          {STEPS.map((s, i) => {
            const isDone = i < step
            const isCurrent = i === step
            return (
              <li
                key={s.id}
                aria-current={isCurrent ? "step" : undefined}
                className="flex-1"
              >
                <span
                  className="block h-1.5 rounded-full transition-colors"
                  style={{
                    background: i <= step
                      ? "var(--color-accent-warm)"
                      : "var(--surface-3)",
                  }}
                />
                <span className="sr-only">
                  {s.title}
                  {isDone ? " (completed)" : isCurrent ? " (current)" : ""}
                </span>
              </li>
            )
          })}
        </ol>

        <div className="card">
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            {STEPS[step].title}
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            {STEPS[step].subtitle}
          </p>

          {error && (
            <div
              role="alert"
              className="mt-4 badge-error inline-block"
            >
              {error}
            </div>
          )}

          <div className="mt-6">
            {step === 0 && (
              <div className="space-y-4">
                <div>
                  <label className="stat-label" htmlFor="ob-name">Clone name</label>
                  <input
                    id="ob-name"
                    type="text"
                    value={name}
                    onChange={(e) => {
                      setName(e.target.value)
                      setSlug(generateSlug(e.target.value))
                    }}
                    placeholder="Example: John's Assistant"
                    className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
                  />
                </div>
                <div>
                  <label className="stat-label" htmlFor="ob-slug">Public URL</label>
                  <input
                    id="ob-slug"
                    type="text"
                    value={slug}
                    onChange={(e) => setSlug(generateSlug(e.target.value))}
                    placeholder="asistente-de-juan"
                    className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none font-mono text-sm"
                  />
                  {slug && (
                    <p className="mt-1 text-xs text-[var(--text-muted)] font-mono">
                      {slug}.myownclone.com
                    </p>
                  )}
                </div>
              </div>
            )}

            {step === 1 && (
              <div className="grid grid-cols-2 gap-3" role="radiogroup" aria-label="Tone">
                {TONES.map((t) => {
                  const selected = tone === t.value
                  return (
                    <button
                      key={t.value}
                      type="button"
                      role="radio"
                      aria-checked={selected}
                      onClick={() => setTone(t.value)}
                      className={[
                        "flex flex-col items-center gap-2 p-4 rounded-xl border-2 transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]",
                        selected
                          ? "border-[var(--color-accent-warm)] bg-[var(--surface-2)]"
                          : "border-[var(--border-soft)] hover:border-[var(--border-medium)]",
                      ].join(" ")}
                    >
                      <span aria-hidden="true" className="text-2xl">{t.emoji}</span>
                      <span className="text-sm font-medium text-[var(--text-primary)]">{t.label}</span>
                    </button>
                  )
                })}
              </div>
            )}

            {step === 2 && (
              <div className="grid grid-cols-2 gap-3" role="radiogroup" aria-label="Language">
                {LANGUAGES.map((l) => {
                  const selected = language === l.value
                  return (
                    <button
                      key={l.value}
                      type="button"
                      role="radio"
                      aria-checked={selected}
                      onClick={() => setLanguage(l.value)}
                      className={[
                        "flex flex-col items-center gap-2 p-4 rounded-xl border-2 transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]",
                        selected
                          ? "border-[var(--color-accent-warm)] bg-[var(--surface-2)]"
                          : "border-[var(--border-soft)] hover:border-[var(--border-medium)]",
                      ].join(" ")}
                    >
                      <span aria-hidden="true" className="text-2xl">{l.emoji}</span>
                      <span className="text-sm font-medium text-[var(--text-primary)]">{l.label}</span>
                    </button>
                  )
                })}
              </div>
            )}

            {step === 3 && (
              <dl className="space-y-3 rounded-xl border border-[var(--border-soft)] p-4">
                <div className="flex justify-between text-sm">
                  <dt className="text-[var(--text-muted)]">Name</dt>
                  <dd className="font-medium text-[var(--text-primary)]">{name}</dd>
                </div>
                <div className="flex justify-between text-sm">
                  <dt className="text-[var(--text-muted)]">URL</dt>
                  <dd className="font-mono font-medium text-[var(--text-primary)]">
                    {slug || generateSlug(name)}
                  </dd>
                </div>
                <div className="flex justify-between text-sm">
                  <dt className="text-[var(--text-muted)]">Tone</dt>
                  <dd className="font-medium text-[var(--text-primary)]">
                    {TONES.find(t => t.value === tone)?.label}
                  </dd>
                </div>
                <div className="flex justify-between text-sm">
                  <dt className="text-[var(--text-muted)]">Language</dt>
                  <dd className="font-medium text-[var(--text-primary)]">
                    {language === "es" ? "Spanish" : "English"}
                  </dd>
                </div>
              </dl>
            )}
          </div>

          <div className="mt-8 flex justify-between">
            {step > 0 ? (
              <button
                type="button"
                onClick={() => setStep(step - 1)}
                className="btn-secondary text-xs"
              >
                ← Back
              </button>
            ) : (
              <div />
            )}
            {step < 3 ? (
              <button
                type="button"
                onClick={() => setStep(step + 1)}
                disabled={!canNext()}
                className="btn-primary text-xs disabled:opacity-50"
              >
                Next
              </button>
            ) : (
              <button
                type="button"
                onClick={handleCreate}
                disabled={loading}
                className="btn-primary text-xs disabled:opacity-50"
              >
                {loading ? "Creating..." : "Create my clone"}
              </button>
            )}
          </div>
        </div>
      </div>
    </main>
  )
}
