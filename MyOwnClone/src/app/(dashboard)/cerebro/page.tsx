"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"
import { useRouter } from "@/i18n/navigation"

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

const TABS: { id: TabType; label: string; singular: string; desc: string }[] = [
  {
    id: "memory",
    label: "Memories",
    singular: "Memory",
    desc: "Information fragments your clone should always remember. Key facts, policies, or personal context.",
  },
  {
    id: "signature",
    label: "Signatures",
    singular: "Signature",
    desc: "HTML format applied to the end of emails sent by your clone.",
  },
  {
    id: "template",
    label: "Templates",
    singular: "Template",
    desc: "Predefined responses your clone uses when specific conditions are met.",
  },
]

export default function CerebroPage() {
  const { status } = useSession()
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
      const res = await fetch(`/api/clone/memories?type=${activeTab}`)
      if (res.ok) {
        const data = await res.json()
        setMemories(Array.isArray(data) ? data : data.items ?? [])
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
      if (!res.ok) throw new Error("Error saving item")
      resetForm()
      fetchMemories()
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error")
    } finally {
      setSaving(false)
    }
  }

  const remove = async (id: string) => {
    if (!confirm("Delete this item?")) return
    try {
      await fetch(`/api/clone/memories/${id}`, { method: "DELETE" })
      fetchMemories()
    } catch {
      // Ignore
    }
  }

  if (status === "loading") {
    return <LoadingState label="Checking session..." />
  }

  if (loading) {
    return <LoadingState label="Loading memory..." rows={4} />
  }

  const activeTabInfo = TABS.find((t) => t.id === activeTab)!

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Memory
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          {activeTabInfo.desc}
        </p>
      </header>

      <div className="flex gap-2 overflow-x-auto">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={activeTab === tab.id}
              aria-controls={`tabpanel-${tab.id}`}
              onClick={() => setActiveTab(tab.id)}
              className={[
                "flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-colors whitespace-nowrap focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]",
                activeTab === tab.id
                  ? "tab-active"
                  : "border border-[var(--border-soft)] bg-[var(--surface-1)] text-[var(--text-secondary)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)]",
              ].join(" ")}
            >
              {tab.label}
            </button>
          ))}
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-3">
          {memories.length === 0 ? (
            <EmptyState
              title={`No ${activeTabInfo.label.toLowerCase()} yet`}
              description="Create the first one with the form on the right."
            />
          ) : (
            memories.map((m) => (
              <div
                key={m.id}
                className="card group py-3"
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex-1 min-w-0">
                    <p className="text-sm text-[var(--text-primary)] whitespace-pre-wrap">
                      {m.content}
                    </p>
                    {m.trigger_condition && (
                      <p className="mt-1 text-xs text-[var(--color-accent-violet)]">
                        Trigger: {m.trigger_condition}
                      </p>
                    )}
                    <p className="mt-2 text-xs text-[var(--text-muted)] font-mono">
                      Priority: {m.priority} ·{" "}
                      {new Date(m.created_at * 1000).toLocaleDateString("es-ES")}
                    </p>
                  </div>
                  <div className="flex gap-1 transition-opacity">
                    <button
                      type="button"
                      onClick={() => {
                        setEditing(m)
                        setFormContent(m.content)
                        setFormTrigger(m.trigger_condition || "")
                        setFormPriority(m.priority)
                        setError(null)
                      }}
                      className="btn-secondary text-xs"
                    >
                      Edit
                    </button>
                    <button
                      type="button"
                      onClick={() => remove(m.id)}
                      className="btn-secondary text-xs hover:text-[var(--color-accent-warm)]"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>

        <div className="card sticky top-4 self-start">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">
            {editing ? "Edit" : "New"} {activeTabInfo.singular}
          </h3>

          <div className="space-y-3">
            <div>
              <label className="stat-label" htmlFor="cb-content">Content</label>
              <textarea
                id="cb-content"
                value={formContent}
                onChange={(e) => setFormContent(e.target.value)}
                rows={5}
                placeholder={
                  activeTab === "memory"
                    ? "Information the clone should remember..."
                    : activeTab === "signature"
                    ? "<div>HTML signature...</div>"
                    : "Automatic response text..."
                }
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none resize-none"
              />
            </div>

            {activeTab === "template" && (
              <div>
                <label className="stat-label" htmlFor="cb-trigger">Trigger keywords</label>
                <input
                  id="cb-trigger"
                  type="text"
                  value={formTrigger}
                  onChange={(e) => setFormTrigger(e.target.value)}
                  placeholder="ex: discount, price, offer"
                  className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
                />
              </div>
            )}

            <div>
              <label className="stat-label" htmlFor="cb-priority">Priority</label>
              <select
                id="cb-priority"
                value={formPriority}
                onChange={(e) => setFormPriority(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              >
                <option value={0}>0 - Normal</option>
                <option value={1}>1 - High</option>
                <option value={2}>2 - Urgent</option>
                <option value={3}>3 - Critical</option>
              </select>
            </div>

            {error && (
              <ErrorState title="Error" message={error} />
            )}

            <div className="flex gap-2 pt-2">
              <button
                type="button"
                onClick={save}
                disabled={saving || !formContent.trim()}
                className="btn-primary text-xs flex-1 disabled:opacity-50"
              >
                {saving ? "Saving..." : editing ? "Update" : "Create"}
              </button>
              {editing && (
                <button
                  type="button"
                  onClick={resetForm}
                  className="btn-secondary text-xs"
                >
                  Cancel
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
