"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

interface AnalyticsOverview {
  total_conversations: number
  total_messages: number
  questions_answered: number
  gaps_count: number
}

interface TopQuestion {
  question: string
  count: number
}

interface Gap {
  id: string
  question: string
  count: number
  suggested_source: string | null
  status: string
}

interface CostBreakdown {
  clone_response_cents: number
  content_ingestion_cents: number
  platform_ops_cents: number
  total_cents: number
}

export default function AnaliticasPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null)
  const [topQuestions, setTopQuestions] = useState<TopQuestion[]>([])
  const [gaps, setGaps] = useState<Gap[]>([])
  const [costs, setCosts] = useState<CostBreakdown | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchData = useCallback(async () => {
    setLoading(true)
    try {
      const [ov, tq, g, co] = await Promise.all([
        fetch("/api/clone/analytics/overview").then((r) => r.ok ? r.json() : null),
        fetch("/api/clone/analytics/top-questions").then((r) => r.ok ? r.json() : []),
        fetch("/api/clone/analytics/gaps").then((r) => r.ok ? r.json() : []),
        fetch("/api/clone/analytics/costs").then((r) => r.ok ? r.json() : null),
      ])
      setOverview(ov)
      setTopQuestions(tq)
      setGaps(g)
      setCosts(co)
    } catch {
      // Empty states
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchData()
  }, [fetchData])

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
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Analíticas
        </h1>
        <p className="mt-1 text-gray-500 dark:text-gray-400">
          Descubre cómo interactúan los usuarios con tu clon.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <StatCard label="Conversaciones" value={overview?.total_conversations ?? 0} />
        <StatCard label="Mensajes" value={overview?.total_messages ?? 0} />
        <StatCard label="Preguntas respondidas" value={overview?.questions_answered ?? 0} />
        <StatCard label="Gaps de conocimiento" value={overview?.gaps_count ?? 0} highlight={!!overview?.gaps_count && overview.gaps_count > 0} />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">
            Preguntas frecuentes
          </h3>
          {topQuestions.length === 0 ? (
            <p className="text-sm text-gray-400 py-4">
              Las preguntas más frecuentes aparecerán aquí cuando empieces a recibir consultas.
            </p>
          ) : (
            <div className="space-y-3">
              {topQuestions.map((q, i) => (
                <div key={i} className="flex items-center justify-between">
                  <p className="text-sm text-gray-700 dark:text-gray-300 truncate flex-1 mr-4">
                    {q.question}
                  </p>
                  <span className="text-xs font-medium text-purple-600 bg-purple-50 dark:bg-purple-950 px-2 py-1 rounded-full whitespace-nowrap">
                    {q.count}
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">
            Gaps de conocimiento
          </h3>
          {gaps.length === 0 ? (
            <p className="text-sm text-gray-400 py-4">
              Preguntas que tu clon no pudo responder. Añade contenido para cubrirlas.
            </p>
          ) : (
            <div className="space-y-3">
              {gaps.map((g) => (
                <div
                  key={g.id}
                  className="flex items-start gap-3 p-3 rounded-lg bg-amber-50 dark:bg-amber-950/30"
                >
                  <span className="text-amber-500 mt-0.5">⚠️</span>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm text-gray-700 dark:text-gray-300">
                      {g.question}
                    </p>
                    <p className="text-xs text-gray-400 mt-1">
                      {g.count} veces · {g.status === "open" ? "Pendiente" : "Resuelto"}
                    </p>
                  </div>
                  <button
                    onClick={() => router.push("/biblioteca")}
                    className="text-xs text-purple-600 hover:text-purple-500 whitespace-nowrap"
                  >
                    + Contenido
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {costs && (
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">
            Costes del mes actual
          </h3>
          <div className="grid grid-cols-3 gap-4">
            <div>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Respuestas del clon
              </p>
              <p className="mt-1 text-lg font-bold text-gray-900 dark:text-white">
                {(costs.clone_response_cents / 100).toFixed(2)}€
              </p>
              <p className="text-xs text-gray-400">Facturable al tenant</p>
            </div>
            <div>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Ingestión de contenido
              </p>
              <p className="mt-1 text-lg font-bold text-gray-900 dark:text-white">
                {(costs.content_ingestion_cents / 100).toFixed(2)}€
              </p>
              <p className="text-xs text-gray-400">Facturable al tenant</p>
            </div>
            <div>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                Operaciones internas
              </p>
              <p className="mt-1 text-lg font-bold text-gray-900 dark:text-white">
                {(costs.platform_ops_cents / 100).toFixed(2)}€
              </p>
              <p className="text-xs text-gray-400">Lo paga la plataforma</p>
            </div>
          </div>
          <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-800 flex justify-between items-center">
            <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
              Total del mes
            </span>
            <span className="text-xl font-bold text-gray-900 dark:text-white">
              {(costs.total_cents / 100).toFixed(2)}€
            </span>
          </div>
        </div>
      )}
    </div>
  )
}

function StatCard({ label, value, highlight }: { label: string; value: number; highlight?: boolean }) {
  return (
    <div className={`bg-white dark:bg-gray-900 rounded-xl border p-6 ${highlight ? "border-amber-400/40" : "border-gray-200 dark:border-gray-800"}`}>
      <p className="text-sm text-gray-500 dark:text-gray-400">{label}</p>
      <p className={`mt-2 text-3xl font-bold ${highlight ? "text-amber-600" : "text-gray-900 dark:text-white"}`}>
        {value.toLocaleString("es-ES")}
      </p>
    </div>
  )
}
