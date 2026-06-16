"use client"

import { useEffect, useState } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { useRouter } from "@/i18n/navigation"
import { setCloneIdCookie } from "@/lib/clone-resolver"
import { useTranslations } from "next-intl";

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

interface CloneSummary {
  id: string
  slug: string
  name: string
}

export default function OnboardingPage() {
  const t = useTranslations("onboarding_dashboard");
  const { status } = useSession()
  const router = useRouter()
  const [step, setStep] = useState(0)
  const [name, setName] = useState("")
  const [slug, setSlug] = useState("")
  const [tone, setTone] = useState("formal")
  const [language, setLanguage] = useState("en")
  const [loading, setLoading] = useState(false)
  const [bootstrapping, setBootstrapping] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/login")
      return
    }

    if (status !== "authenticated") return

    let cancelled = false

    async function loadExistingClones() {
      try {
        const res = await fetch("/api/clone/clones")
        if (!res.ok) {
          if (!cancelled) setBootstrapping(false)
          return
        }

        const data = await res.json().catch(() => [])
        const clones = (Array.isArray(data) ? data : data?.clones ?? []) as CloneSummary[]

        if (cancelled) return

        if (clones.length > 0) {
          setCloneIdCookie(clones[0].id)
          router.replace("/resumen")
          router.refresh()
          return
        }

        setBootstrapping(false)
      } catch {
        if (!cancelled) setBootstrapping(false)
      }
    }

    loadExistingClones()

    return () => {
      cancelled = true
    }
  }, [status, router])

  if (status === "loading" || bootstrapping) {
    return (
      <main className="flex min-h-[calc(100vh-6rem)] items-center justify-center">
        <LoadingState label="Preparing your workspace..." />
      </main>
    )
  }
  if (status === "unauthenticated") {
    return null
  }

  const generateSlug = (n: string) =>
    n.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")

  const getSuggestedSlug = (currentSlug: string, attempt: number) => {
    const normalized = currentSlug || generateSlug(name) || "my-clone"
    if (attempt <= 1) return `${normalized}-2`
    return `${normalized}-${attempt + 1}`
  }

  const canNext = () => {
    if (step === 0) return name.length >= 2
    return true
  }

  const handleCreate = async () => {
    setLoading(true)
    setError("")
    try {
      let nextSlug = slug || generateSlug(name)
      let lastError = "Error creating clone"

      for (let attempt = 0; attempt < 4; attempt += 1) {
        const res = await fetch("/api/clone/clones", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name,
            slug: nextSlug,
            language,
            personality_tone: tone,
            active_modes: ["teach", "support", "sales"],
          }),
        })

        if (res.ok) {
          const data = await res.json().catch(() => ({}))
          const createdCloneId =
            data?.clone?.id ||
            data?.id ||
            data?.source?.cloneId ||
            null

          if (createdCloneId) {
            setCloneIdCookie(createdCloneId)
          }

          setSlug(nextSlug)
          router.replace("/resumen")
          router.refresh()
          return
        }

        const data = await res.json().catch(() => ({}))
        lastError = data.error || "Error creating clone"

        if (res.status !== 409 || !String(lastError).includes("slug")) {
          throw new Error(lastError)
        }

        nextSlug = getSuggestedSlug(nextSlug, attempt + 1)
      }

      setSlug(nextSlug)
      throw new Error(`That public URL was already taken. Try "${nextSlug}".`)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error creating clone")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-lg py-8">
      <div className="mb-6">
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Set up your first clone
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Create an AI assistant that represents you.
        </p>
      </div>

      <ol aria-label="Setup steps" className="mb-8 flex gap-2">
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
        <h2 className="text-lg font-semibold text-[var(--text-primary)]">
          {STEPS[step].title}
        </h2>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          {STEPS[step].subtitle}
        </p>

        {error && (
          <div role="alert" className="mt-4 badge-error inline-block">
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
                <label className="stat-label" htmlFor="ob-slug">{t("onboarding_dashboard.public_url")}</label>
                <input
                  id="ob-slug"
                  type="text"
                  value={slug}
                  onChange={(e) => setSlug(generateSlug(e.target.value))}
                  placeholder="johns-assistant"
                  className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 font-mono text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
                />
                {slug && (
                  <p className="mt-1 font-mono text-xs text-[var(--text-muted)]">
                    {slug}.myownclone.com
                  </p>
                )}
              </div>
            </div>
          )}

          {step === 1 && (
            <div className="grid grid-cols-2 gap-3" role="radiogroup" aria-label={t("onboarding_dashboard.tone")}>
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
            <div className="grid grid-cols-2 gap-3" role="radiogroup" aria-label={t("onboarding_dashboard.language")}>
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
                <dt className="text-[var(--text-muted)]">{t("onboarding_dashboard.tone")}</dt>
                <dd className="font-medium text-[var(--text-primary)]">
                  {TONES.find(t => t.value === tone)?.label}
                </dd>
              </div>
              <div className="flex justify-between text-sm">
                <dt className="text-[var(--text-muted)]">{t("onboarding_dashboard.language")}</dt>
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

      <button
        type="button"
        onClick={() => router.push("/resumen")}
        className="mt-4 text-xs text-[var(--text-muted)] hover:text-[var(--text-primary)]"
      >
        Skip for now
      </button>
    </div>
  )
}
