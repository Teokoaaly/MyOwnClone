"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"

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

const DAYS = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

export default function ReunionesPage() {
  const { status } = useSession()
  const router = useRouter()
  const [cloneId, setCloneId] = useState<string | null>(null)
  const [meetingTypes, setMeetingTypes] = useState<MeetingType[]>([])
  const [availability, setAvailability] = useState<Availability[]>([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState<"meeting" | "availability" | null>(null)
  const [saving, setSaving] = useState(false)
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
    setLoading(true)
    try {
      const clonesRes = await fetch("/api/clone/clones")
      if (!clonesRes.ok) return
      const clones = await clonesRes.json()
      if (clones.length === 0) return
      const cid = clones[0].id
      setCloneId(cid)

      const [mtRes, avRes] = await Promise.all([
        fetch(`/api/clone/clones/${cid}/meeting-types`),
        fetch(`/api/clone/clones/${cid}/availability`),
      ])
      if (mtRes.ok) {
        const data = await mtRes.json()
        setMeetingTypes(Array.isArray(data) ? data : data.items ?? [])
      }
      if (avRes.ok) {
        const data = await avRes.json()
        setAvailability(Array.isArray(data) ? data : data.items ?? [])
      }
    } catch {
      // Empty states
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchData()
  }, [fetchData])

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
    return <LoadingState label="Cargando reuniones…" rows={3} />
  }

  return (
    <div className="space-y-6">
      <header className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            Reuniones
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Configura tipos de reunión y tu disponibilidad semanal.
          </p>
        </div>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={() => setShowForm(showForm === "meeting" ? null : "meeting")}
            className="btn-primary text-xs"
          >
            + Tipo de reunión
          </button>
          <button
            type="button"
            onClick={() => setShowForm(showForm === "availability" ? null : "availability")}
            className="btn-secondary text-xs"
          >
            + Disponibilidad
          </button>
        </div>
      </header>

      {showForm === "meeting" && (
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">Nuevo tipo de reunión</h3>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div>
              <label className="stat-label" htmlFor="mt-name">Nombre</label>
              <input
                id="mt-name"
                type="text"
                value={formName}
                onChange={(e) => setFormName(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="mt-duration">Duración (min)</label>
              <input
                id="mt-duration"
                type="number"
                value={formDuration}
                onChange={(e) => setFormDuration(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="mt-price">Precio (céntimos)</label>
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
              <label className="stat-label" htmlFor="mt-desc">Descripción</label>
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
              {saving ? "Creando…" : "Crear"}
            </button>
            <button type="button" onClick={() => setShowForm(null)} className="btn-secondary text-xs">
              Cancelar
            </button>
          </div>
        </div>
      )}

      {showForm === "availability" && (
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">Nueva disponibilidad</h3>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div>
              <label className="stat-label" htmlFor="av-day">Día</label>
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
              <label className="stat-label" htmlFor="av-start">Hora inicio</label>
              <input
                id="av-start"
                type="time"
                value={formStart}
                onChange={(e) => setFormStart(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="av-end">Hora fin</label>
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
              {saving ? "Creando…" : "Crear"}
            </button>
            <button type="button" onClick={() => setShowForm(null)} className="btn-secondary text-xs">
              Cancelar
            </button>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">Tipos de reunión</h3>
          {meetingTypes.length === 0 ? (
            <EmptyState
              title="No hay tipos de reunión"
              description="Crea el primero con el botón de arriba."
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
                        {mt.duration_minutes} min · {mt.price_cents > 0 ? `${(mt.price_cents / 100).toFixed(2)}€` : "Gratis"}
                      </p>
                    </div>
                  </div>
                  {!mt.active && (
                    <span className="badge-warning">Inactivo</span>
                  )}
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">Disponibilidad semanal</h3>
          {availability.length === 0 ? (
            <EmptyState
              title="No hay horarios"
              description="Configura tu disponibilidad con el botón de arriba."
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
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  )
}
