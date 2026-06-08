"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

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
  const { data: session, status } = useSession()
  const router = useRouter()
  const [cloneId, setCloneId] = useState<string | null>(null)
  const [meetingTypes, setMeetingTypes] = useState<MeetingType[]>([])
  const [availability, setAvailability] = useState<Availability[]>([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState<"meeting" | "availability" | null>(null)
  const [saving, setSaving] = useState(false)

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
      if (mtRes.ok) setMeetingTypes(await mtRes.json())
      if (avRes.ok) setAvailability(await avRes.json())
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
      }
    } catch {
      // Error
    } finally {
      setSaving(false)
    }
  }

  const createAvailability = async () => {
    if (!cloneId) return
    setSaving(true)
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
      }
    } catch {
      // Error
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

  return (
    <div className="p-8">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
            Reuniones
          </h1>
          <p className="mt-1 text-gray-500 dark:text-gray-400">
            Configura tipos de reunión y tu disponibilidad semanal.
          </p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => setShowForm(showForm === "meeting" ? null : "meeting")}
            className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors"
          >
            + Tipo de reunión
          </button>
          <button
            onClick={() => setShowForm(showForm === "availability" ? null : "availability")}
            className="px-4 py-2 border border-gray-300 dark:border-gray-700 text-gray-700 dark:text-gray-300 text-sm font-medium rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
          >
            + Disponibilidad
          </button>
        </div>
      </div>

      {showForm === "meeting" && (
        <div className="mb-6 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">Nuevo tipo de reunión</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Nombre</label>
              <input type="text" value={formName} onChange={(e) => setFormName(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Duración (min)</label>
              <input type="number" value={formDuration} onChange={(e) => setFormDuration(Number(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Precio (céntimos)</label>
              <input type="number" value={formPrice} onChange={(e) => setFormPrice(Number(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Color</label>
              <input type="color" value={formColor} onChange={(e) => setFormColor(e.target.value)}
                className="h-10 w-full rounded-lg border border-gray-300 dark:border-gray-700 cursor-pointer" />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Descripción</label>
              <input type="text" value={formDesc} onChange={(e) => setFormDesc(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
          </div>
          <div className="mt-4 flex gap-2">
            <button onClick={createMeetingType} disabled={saving}
              className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50">
              {saving ? "Creando..." : "Crear"}
            </button>
            <button onClick={() => setShowForm(null)}
              className="px-4 py-2 text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
              Cancelar
            </button>
          </div>
        </div>
      )}

      {showForm === "availability" && (
        <div className="mb-6 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">Nueva disponibilidad</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Día</label>
              <select value={formDay} onChange={(e) => setFormDay(Number(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm">
                {DAYS.map((d, i) => <option key={i} value={i}>{d}</option>)}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Buffer (min)</label>
              <input type="number" value={formBuffer} onChange={(e) => setFormBuffer(Number(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Hora inicio</label>
              <input type="time" value={formStart} onChange={(e) => setFormStart(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Hora fin</label>
              <input type="time" value={formEnd} onChange={(e) => setFormEnd(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
          </div>
          <div className="mt-4 flex gap-2">
            <button onClick={createAvailability} disabled={saving}
              className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50">
              {saving ? "Creando..." : "Crear"}
            </button>
            <button onClick={() => setShowForm(null)}
              className="px-4 py-2 text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
              Cancelar
            </button>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">Tipos de reunión</h3>
          {meetingTypes.length === 0 ? (
            <p className="text-sm text-gray-500 dark:text-gray-400 text-center py-8">
              No hay tipos de reunión configurados.
            </p>
          ) : (
            <div className="space-y-3">
              {meetingTypes.map((mt) => (
                <div key={mt.id} className="flex items-center justify-between p-3 rounded-lg border border-gray-200 dark:border-gray-800">
                  <div className="flex items-center gap-3">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: mt.color }} />
                    <div>
                      <p className="text-sm font-medium text-gray-900 dark:text-white">{mt.name}</p>
                      <p className="text-xs text-gray-500 dark:text-gray-400">
                        {mt.duration_minutes} min · {mt.price_cents > 0 ? `${(mt.price_cents / 100).toFixed(2)}€` : "Gratis"}
                      </p>
                    </div>
                  </div>
                  {!mt.active && (
                    <span className="text-xs px-2 py-0.5 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-500">
                      Inactivo
                    </span>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">Disponibilidad semanal</h3>
          {availability.length === 0 ? (
            <p className="text-sm text-gray-500 dark:text-gray-400 text-center py-8">
              No hay horarios de disponibilidad configurados.
            </p>
          ) : (
            <div className="space-y-2">
              {availability.map((av) => (
                <div key={av.id} className="flex items-center justify-between p-3 rounded-lg border border-gray-200 dark:border-gray-800">
                  <span className="text-sm font-medium text-gray-900 dark:text-white">
                    {DAYS[av.day_of_week]}
                  </span>
                  <span className="text-sm text-gray-500 dark:text-gray-400">
                    {av.start_time?.slice(0, 5)} — {av.end_time?.slice(0, 5)}
                  </span>
                  <span className="text-xs text-gray-400">
                    +{av.buffer_minutes}min buffer
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
