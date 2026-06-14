"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"
import { useRouter } from "@/i18n/navigation"

interface MeetingType {
  id: string
  name: string
  duration_minutes: number
  price_cents: number
  description: string | null
  color: string
  active: boolean
}

interface Availability {
  id: string
  day_of_week: number
  start_time: string
  end_time: string
  buffer_minutes: number
}

const DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

export default function ReunionesPage() {
  const { status } = useSession()
  const router = useRouter()
  const [cloneId, setCloneId] = useState<string | null>(null)
  const [meetingTypes, setMeetingTypes] = useState<MeetingType[]>([])
  const [availability, setAvailability] = useState<Availability[]>([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState<"meeting" | "availability" | null>(null)
  const [saving, setSaving] = useState(false)
  const [mutatingId, setMutatingId] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const [formName, setFormName] = useState("")
  const [formDuration, setFormDuration] = useState(30)
  const [formPrice, setFormPrice] = useState(0)
  const [formDesc, setFormDesc] = useState("")
  const [formColor, setFormColor] = useState("#6366f1")
  const [formDay, setFormDay] = useState(1)
  const [formStart, setFormStart] = useState("09:00")
  const [formEnd, setFormEnd] = useState("17:00")
  const [formBuffer, setFormBuffer] = useState(15)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchData = useCallback(async () => {
    if (status !== "authenticated") return

    setLoading(true)
    setError(null)
    try {
      const clonesRes = await fetch("/api/clone/clones")
      if (!clonesRes.ok) throw new Error(`Error ${clonesRes.status}`)
      const clones = await clonesRes.json()
      if (clones.length === 0) return
      const cid = clones[0].id
      setCloneId(cid)

      const [mtRes, avRes] = await Promise.all([
        fetch(`/api/clone/clones/${cid}/meeting-types`),
        fetch(`/api/clone/clones/${cid}/availability`),
      ])
      if (!mtRes.ok) throw new Error(`Error ${mtRes.status}`)
      if (!avRes.ok) throw new Error(`Error ${avRes.status}`)
      if (mtRes.ok) {
        const data = await mtRes.json()
        setMeetingTypes(Array.isArray(data) ? data : data.items ?? [])
      }
      if (avRes.ok) {
        const data = await avRes.json()
        setAvailability(Array.isArray(data) ? data : data.items ?? [])
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Could not load meetings")
    } finally {
      setLoading(false)
    }
  }, [status])

  useEffect(() => {
    if (status === "authenticated") {
      fetchData()
    }
  }, [status, fetchData])

  const createMeetingType = async () => {
    if (!cloneId || !formName.trim()) return
    setSaving(true)
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${cloneId}/meeting-types`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: formName,
          duration_minutes: formDuration,
          price_cents: formPrice,
          description: formDesc || null,
          color: formColor,
          active: true,
        }),
      })
      if (res.ok) {
        setShowForm(null)
        setFormName("")
        setFormDuration(30)
        setFormPrice(0)
        setFormDesc("")
        fetchData()
      } else {
        throw new Error(`Error ${res.status}`)
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error")
    } finally {
      setSaving(false)
    }
  }

  const updateMeetingType = async (meetingType: MeetingType, changes: Partial<MeetingType>) => {
    if (!cloneId) return
    setMutatingId(meetingType.id)
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${cloneId}/meeting-types/${meetingType.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...meetingType, ...changes }),
      })
      if (!res.ok) throw new Error(`Error ${res.status}`)
      const updated = await res.json()
      setMeetingTypes((items) => items.map((item) => item.id === updated.id ? updated : item))
    } catch (e) {
      setError(e instanceof Error ? e.message : "Could not update meeting type")
    } finally {
      setMutatingId(null)
    }
  }

  const deleteMeetingType = async (meetingType: MeetingType) => {
    if (!cloneId) return
    setMutatingId(meetingType.id)
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${cloneId}/meeting-types/${meetingType.id}`, {
        method: "DELETE",
      })
      if (!res.ok) throw new Error(`Error ${res.status}`)
      const result = await res.json()
      if (result.deactivated) {
        setMeetingTypes((items) => items.map((item) => item.id === meetingType.id ? { ...item, active: false } : item))
      } else {
        setMeetingTypes((items) => items.filter((item) => item.id !== meetingType.id))
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Could not delete meeting type")
    } finally {
      setMutatingId(null)
    }
  }

  const deleteAvailability = async (slot: Availability) => {
    if (!cloneId) return
    setMutatingId(slot.id)
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${cloneId}/availability/${slot.id}`, {
        method: "DELETE",
      })
      if (!res.ok) throw new Error(`Error ${res.status}`)
      setAvailability((items) => items.filter((item) => item.id !== slot.id))
    } catch (e) {
      setError(e instanceof Error ? e.message : "Could not delete availability")
    } finally {
      setMutatingId(null)
    }
  }

  const createAvailability = async () => {
    if (!cloneId) return
    setSaving(true)
    setError(null)
    try {
      const res = await fetch(`/api/clone/clones/${cloneId}/availability`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          day_of_week: formDay,
          start_time: formStart,
          end_time: formEnd,
          buffer_minutes: formBuffer,
        }),
      })
      if (res.ok) {
        setShowForm(null)
        fetchData()
      } else {
        throw new Error(`Error ${res.status}`)
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error")
    } finally {
      setSaving(false)
    }
  }

  if (status === "loading" || loading) {
    return <LoadingState label="Loading meetings..." rows={3} />
  }

  return (
    <div className="space-y-6">
      <header className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            Meetings
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Configure meeting types and weekly availability.
          </p>
        </div>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={() => setShowForm(showForm === "meeting" ? null : "meeting")}
            className="btn-primary text-xs"
          >
            + Meeting type
          </button>
          <button
            type="button"
            onClick={() => setShowForm(showForm === "availability" ? null : "availability")}
            className="btn-secondary text-xs"
          >
            + Availability
          </button>
        </div>
      </header>

      {showForm === "meeting" && (
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">New meeting type</h3>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div>
              <label className="stat-label" htmlFor="mt-name">Name</label>
              <input
                id="mt-name"
                type="text"
                value={formName}
                onChange={(e) => setFormName(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="mt-duration">Duration (min)</label>
              <input
                id="mt-duration"
                type="number"
                value={formDuration}
                onChange={(e) => setFormDuration(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="mt-price">Price (cents)</label>
              <input
                id="mt-price"
                type="number"
                value={formPrice}
                onChange={(e) => setFormPrice(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="mt-color">Color</label>
              <input
                id="mt-color"
                type="color"
                value={formColor}
                onChange={(e) => setFormColor(e.target.value)}
                className="mt-1 h-10 w-full rounded-lg border border-[var(--border-soft)] cursor-pointer"
              />
            </div>
            <div className="md:col-span-2">
              <label className="stat-label" htmlFor="mt-desc">Description</label>
              <input
                id="mt-desc"
                type="text"
                value={formDesc}
                onChange={(e) => setFormDesc(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
          </div>
          {error && <div className="mt-3"><ErrorState message={error} /></div>}
          <div className="mt-4 flex gap-2">
            <button
              type="button"
              onClick={createMeetingType}
              disabled={saving}
              className="btn-primary text-xs disabled:opacity-50"
            >
              {saving ? "Creating..." : "Create"}
            </button>
            <button type="button" onClick={() => setShowForm(null)} className="btn-secondary text-xs">
              Cancel
            </button>
          </div>
        </div>
      )}

      {showForm === "availability" && (
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">New availability</h3>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div>
              <label className="stat-label" htmlFor="av-day">Day</label>
              <select
                id="av-day"
                value={formDay}
                onChange={(e) => setFormDay(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              >
                {DAYS.map((d, i) => <option key={i} value={i}>{d}</option>)}
              </select>
            </div>
            <div>
              <label className="stat-label" htmlFor="av-buffer">Buffer (min)</label>
              <input
                id="av-buffer"
                type="number"
                value={formBuffer}
                onChange={(e) => setFormBuffer(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="av-start">Start time</label>
              <input
                id="av-start"
                type="time"
                value={formStart}
                onChange={(e) => setFormStart(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="av-end">End time</label>
              <input
                id="av-end"
                type="time"
                value={formEnd}
                onChange={(e) => setFormEnd(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
          </div>
          {error && <div className="mt-3"><ErrorState message={error} /></div>}
          <div className="mt-4 flex gap-2">
            <button
              type="button"
              onClick={createAvailability}
              disabled={saving}
              className="btn-primary text-xs disabled:opacity-50"
            >
              {saving ? "Creating..." : "Create"}
            </button>
            <button type="button" onClick={() => setShowForm(null)} className="btn-secondary text-xs">
              Cancel
            </button>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">Meeting types</h3>
          {error && !showForm && <div className="mb-3"><ErrorState message={error} /></div>}
          {meetingTypes.length === 0 ? (
            <EmptyState
              title="No meeting types"
              description="Create the first one with the button above."
            />
          ) : (
            <ul className="space-y-2">
              {meetingTypes.map((mt) => (
                <li
                  key={mt.id}
                  className="flex items-center justify-between rounded-lg border border-[var(--border-soft)] p-3"
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <div className="h-3 w-3 rounded-full shrink-0" style={{ backgroundColor: mt.color }} />
                    <div className="min-w-0">
                      <p className="text-sm font-medium text-[var(--text-primary)] truncate">{mt.name}</p>
                      <p className="text-xs text-[var(--text-muted)]">
                        {mt.duration_minutes} min · {mt.price_cents > 0 ? `${(mt.price_cents / 100).toFixed(2)}€` : "Free"}
                      </p>
                    </div>
                  </div>
                  <div className="flex shrink-0 items-center gap-2">
                    {!mt.active && <span className="badge-warning">Inactive</span>}
                    <button
                      type="button"
                      onClick={() => updateMeetingType(mt, { active: !mt.active })}
                      disabled={mutatingId === mt.id}
                      className="btn-secondary px-2 py-1 text-[11px] disabled:opacity-50"
                    >
                      {mt.active ? "Disable" : "Enable"}
                    </button>
                    <button
                      type="button"
                      onClick={() => deleteMeetingType(mt)}
                      disabled={mutatingId === mt.id}
                      className="btn-secondary px-2 py-1 text-[11px] disabled:opacity-50"
                    >
                      Delete
                    </button>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">Weekly availability</h3>
          {availability.length === 0 ? (
            <EmptyState
              title="No schedules"
              description="Configure your availability with the button above."
            />
          ) : (
            <ul className="space-y-2">
              {availability.map((av) => (
                <li
                  key={av.id}
                  className="flex items-center justify-between rounded-lg border border-[var(--border-soft)] p-3"
                >
                  <span className="text-sm font-medium text-[var(--text-primary)]">
                    {DAYS[av.day_of_week]}
                  </span>
                  <span className="font-mono text-sm text-[var(--text-secondary)]">
                    {av.start_time?.slice(0, 5)} — {av.end_time?.slice(0, 5)}
                  </span>
                  <span className="text-xs text-[var(--text-muted)] font-mono">
                    +{av.buffer_minutes}min buffer
                  </span>
                  <button
                    type="button"
                    onClick={() => deleteAvailability(av)}
                    disabled={mutatingId === av.id}
                    className="btn-secondary px-2 py-1 text-[11px] disabled:opacity-50"
                  >
                    Delete
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  )
}
