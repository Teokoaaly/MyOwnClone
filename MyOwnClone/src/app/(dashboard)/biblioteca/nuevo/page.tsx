"use client"

export const dynamic = "force-dynamic"


import { useState, Suspense, useCallback, useEffect } from "react"
import { useSession } from "next-auth/react"
import { useSearchParams } from "next/navigation"
import { LoadingState } from "@/components/ui/LoadingState"
import { useRouter } from "@/i18n/navigation"

const SILOS = [
  { id: "teach", label: "Teaching" },
  { id: "support", label: "Support" },
  { id: "sales", label: "Sales" },
] as const

const TYPE_LABELS: Record<string, string> = {
  pdf: "Upload PDF",
  youtube: "YouTube link",
  text: "Write text",
  web: "Web page",
  interview: "AI interview",
}

function CheckIcon({
  className,
  style,
}: {
  className?: string
  style?: React.CSSProperties
}) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      strokeWidth={2}
      stroke="currentColor"
      className={className}
      style={style}
      aria-hidden="true"
    >
      <path strokeLinecap="round" strokeLinejoin="round" d="m4.5 12.75 6 6 9-13.5" />
    </svg>
  )
}

function NuevoContentPage() {
  const { status } = useSession()
  const router = useRouter()
  const searchParams = useSearchParams()
  const tipo = searchParams.get("tipo") || "text"

  const [silo, setSilo] = useState("teach")
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(false)
  const [error, setError] = useState("")

  const handleBack = useCallback(() => {
    if (window.history.length > 1) router.back()
    else router.push("/biblioteca")
  }, [router])

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/login")
    }
  }, [router, status])

  if (status === "loading") {
    return <LoadingState label="Loading..." rows={4} />
  }
  if (status === "unauthenticated") {
    return null
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError("")
    try {
      const form = e.target as HTMLFormElement
      const formData = new FormData(form)
      formData.append("silo", silo)
      formData.append("type", tipo)

      const res = await fetch("/api/clone/sources", {
        method: "POST",
        body: formData,
        credentials: "include",
      })

      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        throw new Error(data.error || "Could not add this content right now.")
      }
      setSuccess(true)
    } catch {
      setError(
        "Could not add this content right now. Check the fields and try again."
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="mx-auto max-w-2xl p-8">
      <button
        type="button"
        onClick={handleBack}
        className="mb-4 text-sm text-[var(--text-muted)] hover:text-[var(--text-primary)]"
      >
        <span aria-hidden="true">←</span> Back to library
      </button>
      <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
        {TYPE_LABELS[tipo] || "New content"}
      </h1>
      <p className="mt-1 text-sm text-[var(--text-muted)]">
        Add content to your clone's knowledge.
      </p>

      {error && (
        <div role="alert" className="mt-4 badge-error inline-block">
          {error}
        </div>
      )}

      {success ? (
        <div
          className="mt-8 rounded-xl p-8 text-center"
          style={{
            background: "var(--bg-shell)",
            border: "1px solid var(--border-soft)",
          }}
        >
          <div
            className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full"
            style={{ background: "var(--color-accent-green)" }}
            aria-hidden="true"
          >
            <CheckIcon className="h-6 w-6" style={{ color: "#FFFFFF" }} />
          </div>
          <h2 className="text-lg font-semibold text-[var(--text-primary)]">
            Content added
          </h2>
          <p className="mt-2 text-sm text-[var(--text-muted)]">
            The content is being processed. Your clone will be able to use it in a few minutes.
          </p>
          <button
            type="button"
            onClick={() => router.push("/biblioteca")}
            className="mt-6 rounded-xl px-4 py-2 text-sm font-medium text-white transition"
            style={{ background: "var(--color-accent-violet)" }}
            onMouseEnter={(e) => {
              e.currentTarget.style.background = "var(--color-accent-pink)"
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.background = "var(--color-accent-violet)"
            }}
          >
            Back to library
          </button>
        </div>
      ) : (
        <form
          onSubmit={handleSubmit}
          className="mt-6 space-y-4 rounded-xl p-6"
          style={{
            background: "var(--bg-shell)",
            border: "1px solid var(--border-soft)",
          }}
          noValidate
        >
          <fieldset>
            <legend className="mb-2 block text-sm font-medium text-[var(--text-primary)]">
              Content silo
            </legend>
            <div className="flex gap-2" role="radiogroup" aria-label="Content silo">
              {SILOS.map((s) => {
                const isActive = silo === s.id
                return (
                  <button
                    key={s.id}
                    type="button"
                    role="radio"
                    aria-checked={isActive}
                    onClick={() => setSilo(s.id)}
                    className="flex items-center gap-1.5 rounded-lg border px-4 py-2 text-sm font-medium transition focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-violet)]"
                    style={
                      isActive
                        ? {
                            borderColor: "var(--color-accent-violet)",
                            background: "var(--surface-2)",
                            color: "var(--color-accent-violet)",
                          }
                        : {
                            borderColor: "var(--border-soft)",
                            color: "var(--text-secondary)",
                          }
                    }
                  >
                    {s.label}
                  </button>
                )
              })}
            </div>
          </fieldset>

          {tipo === "pdf" && (
            <div>
              <label
                htmlFor="source-file"
                className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
              >
                PDF file
              </label>
              <input
                id="source-file"
                name="file"
                type="file"
                accept=".pdf,.doc,.docx,.txt"
                className="w-full rounded-xl border px-4 py-3 text-sm transition focus:ring-2"
                style={{
                  background: "var(--surface-2)",
                  borderColor: "var(--border-medium)",
                  color: "var(--text-primary)",
                }}
              />
            </div>
          )}

          {(tipo === "youtube" || tipo === "web") && (
            <div>
              <label
                htmlFor="source-url"
                className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
              >
                URL
              </label>
              <input
                id="source-url"
                name="url"
                type="url"
                placeholder={tipo === "youtube" ? "https://youtube.com/watch?v=..." : "https://example.com/article"}
                className="w-full rounded-xl border px-4 py-3 text-sm outline-none transition focus:ring-2"
                style={{
                  background: "var(--surface-2)",
                  borderColor: "var(--border-medium)",
                  color: "var(--text-primary)",
                }}
              />
            </div>
          )}

          {tipo === "text" && (
            <div>
              <label
                htmlFor="source-content"
                className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
              >
                Content
              </label>
              <textarea
                id="source-content"
                name="content"
                rows={8}
                placeholder="Paste or write the content here..."
                className="w-full resize-none rounded-xl border px-4 py-3 text-sm outline-none transition focus:ring-2"
                style={{
                  background: "var(--surface-2)",
                  borderColor: "var(--border-medium)",
                  color: "var(--text-primary)",
                }}
              />
            </div>
          )}

          {tipo === "interview" && (
            <div
              className="rounded-xl p-4"
              style={{
                background: "var(--surface-2)",
                border: "1px solid var(--color-accent-violet)",
              }}
              role="status"
            >
              <p className="text-sm text-[var(--text-primary)]">
                The AI interview is a conversation with your clone where it asks
                questions to extract your knowledge automatically.
              </p>
              <p className="mt-2 text-xs text-[var(--text-muted)]">
                This feature will be available soon.
              </p>
            </div>
          )}

          <div className="pt-2">
            <button
              type="submit"
              disabled={loading || tipo === "interview"}
              className="rounded-xl px-6 py-3 text-sm font-medium text-white transition disabled:opacity-50"
              style={{ background: "var(--color-accent-violet)" }}
              onMouseEnter={(e) => {
                if (!e.currentTarget.disabled) {
                  e.currentTarget.style.background = "var(--color-accent-pink)"
                }
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.background = "var(--color-accent-violet)"
              }}
            >
              {loading
                ? "Processing..."
                : tipo === "interview"
                ? "Coming soon"
                : "Add content"}
            </button>
          </div>
        </form>
      )}
    </main>
  )
}

export default function NuevoPage() {
  return (
    <Suspense fallback={<LoadingState label="Loading..." rows={4} />}>
      <NuevoContentPage />
    </Suspense>
  )
}
