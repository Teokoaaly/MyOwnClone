"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import Link from "next/link"

interface AnalyticsOverview {
  total_conversations: number
  total_messages: number
  questions_answered: number
  gaps_count: number
}

export default function DashboardResumenPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchData = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetch("/api/clone/analytics/overview")
      if (res.ok) {
        setOverview(await res.json())
      }
    } catch {
      // Empty state
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchData()
  }, [fetchData])

  const shortcuts = [
    { href: "/biblioteca", label: "Subir contenido", emoji: "📚", desc: "PDFs, YouTube, texto", color: "from-purple-600 to-pink-600" },
    { href: "/cerebro", label: "Añadir memoria", emoji: "🧠", desc: "Datos que el clon recordará", color: "from-blue-600 to-cyan-600" },
    { href: "/inbox", label: "Revisar inbox", emoji: "📧", desc: "Emails pendientes de respuesta", color: "from-amber-600 to-orange-600" },
    { href: "/analiticas", label: "Ver analíticas", emoji: "📈", desc: "Preguntas, gaps, costes", color: "from-green-600 to-emerald-600" },
  ]

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
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          ¡Bienvenido{session?.user?.name ? `, ${session.user.name}` : ""}!
        </h1>
        <p className="mt-1 text-gray-500 dark:text-gray-400">
          Gestiona tu clon de IA y descubre cómo interactúan tus clientes.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white dark:bg-gray-900 rounded-xl p-6 border border-gray-200 dark:border-gray-800">
          <p className="text-sm font-medium text-gray-500 dark:text-gray-400">
            Conversaciones
          </p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">
            {overview?.total_conversations ?? 0}
          </p>
          <p className="mt-1 text-xs text-gray-400">Últimos 30 días</p>
        </div>
        <div className="bg-white dark:bg-gray-900 rounded-xl p-6 border border-gray-200 dark:border-gray-800">
          <p className="text-sm font-medium text-gray-500 dark:text-gray-400">
            Mensajes
          </p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">
            {overview?.total_messages ?? 0}
          </p>
          <p className="mt-1 text-xs text-gray-400">
            <Link href="/biblioteca" className="text-purple-600 hover:text-purple-500">
              Subir contenido →
            </Link>
          </p>
        </div>
        <div className="bg-white dark:bg-gray-900 rounded-xl p-6 border border-gray-200 dark:border-gray-800">
          <p className="text-sm font-medium text-gray-500 dark:text-gray-400">
            Preguntas respondidas
          </p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">
            {overview?.questions_answered ?? "--"}
          </p>
          <p className="mt-1 text-xs text-gray-400">
            {overview?.questions_answered != null ? "Últimos 30 días" : "Sin datos aún"}
          </p>
        </div>
      </div>

      <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
        Acciones rápidas
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {shortcuts.map((s) => (
          <Link
            key={s.href}
            href={s.href}
            className="group relative overflow-hidden rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-5 hover:shadow-lg transition-all"
          >
            <div className={`absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl ${s.color} opacity-10 rounded-bl-full`} />
            <div className="relative">
              <span className="text-2xl">{s.emoji}</span>
              <h3 className="mt-3 font-semibold text-gray-900 dark:text-white text-sm">
                {s.label}
              </h3>
              <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">
                {s.desc}
              </p>
            </div>
          </Link>
        ))}
      </div>

      <div className="mt-8 bg-gradient-to-r from-purple-600/5 to-pink-600/5 rounded-xl border border-purple-400/10 p-6">
        <div className="flex gap-3 items-start">
          <span className="text-2xl">🚀</span>
          <div>
            <h3 className="font-semibold text-gray-900 dark:text-white text-sm">
              Empieza a construir tu clon
            </h3>
            <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
              Sube contenido a la biblioteca, configura la personalidad de tu clon
              y comparte tu enlace público para empezar a recibir consultas 24/7.
            </p>
            <div className="mt-3 flex gap-3">
              <Link
                href="/biblioteca"
                className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors"
              >
                Subir primer contenido
              </Link>
              <Link
                href="/configuracion"
                className="px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-400 border border-gray-200 dark:border-gray-700 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
              >
                Configurar clon
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
