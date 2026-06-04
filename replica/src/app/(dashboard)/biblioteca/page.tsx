"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import Link from "next/link"

interface Source {
  id: string
  title: string
  type: string
  status: string
  silo: string
  wordCount: number
  createdAt: string
}

const CONTENT_TYPES = [
  {
    type: "pdf",
    label: "Subir PDF",
    emoji: "📄",
    desc: "Documentos PDF, Word, Excel",
    color: "border-red-400/30 hover:border-red-400 bg-red-500/5",
  },
  {
    type: "youtube",
    label: "Enlace de YouTube",
    emoji: "🎥",
    desc: "Transcripción automática de vídeos",
    color: "border-blue-400/30 hover:border-blue-400 bg-blue-500/5",
  },
  {
    type: "text",
    label: "Escribir texto",
    emoji: "✍️",
    desc: "Pega o escribe contenido directamente",
    color: "border-green-400/30 hover:border-green-400 bg-green-500/5",
  },
  {
    type: "web",
    label: "Página web",
    emoji: "🌐",
    desc: "Extraer texto de una URL",
    color: "border-amber-400/30 hover:border-amber-400 bg-amber-500/5",
  },
  {
    type: "interview",
    label: "Entrevista AI",
    emoji: "🎙️",
    desc: "El clon te entrevista para extraer tu conocimiento",
    color: "border-purple-400/30 hover:border-purple-400 bg-purple-500/5",
  },
]

const SILOS = [
  { id: "teach", label: "Pedagogía", emoji: "📚" },
  { id: "support", label: "Soporte", emoji: "💬" },
  { id: "sales", label: "Ventas", emoji: "🛒" },
]

export default function BibliotecaPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [sources, setSources] = useState<Source[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchSources = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetch("/api/clone/sources")
      if (res.ok) {
        setSources(await res.json())
      }
    } catch {
      // Empty state
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchSources()
  }, [fetchSources])

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
            Biblioteca de Contenido
          </h1>
          <p className="mt-1 text-gray-500 dark:text-gray-400">
            Sube contenido para entrenar a tu clon: PDFs, vídeos de YouTube, texto, y más.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-5 gap-4 mb-8">
        {CONTENT_TYPES.map((ct) => (
          <Link
            key={ct.type}
            href={`/biblioteca/nuevo?tipo=${ct.type}`}
            className={`group rounded-xl border p-5 transition-all ${ct.color}`}
          >
            <div className="text-3xl mb-3">{ct.emoji}</div>
            <h3 className="font-semibold text-gray-900 dark:text-white text-sm">
              {ct.label}
            </h3>
            <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">
              {ct.desc}
            </p>
          </Link>
        ))}
      </div>

      <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800">
        <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between">
          <h2 className="font-semibold text-gray-900 dark:text-white text-sm">
            Contenido subido
          </h2>
          <div className="flex gap-2">
            {SILOS.map((s) => (
              <span
                key={s.id}
                className="inline-flex items-center gap-1 px-2 py-1 text-xs rounded-md border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400"
              >
                {s.emoji} {s.label}
              </span>
            ))}
          </div>
        </div>

        {sources.length === 0 ? (
          <div className="text-center py-12">
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-purple-100 dark:bg-purple-900 flex items-center justify-center">
              <svg className="w-8 h-8 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Aún no hay contenido
            </h3>
            <p className="mt-2 text-gray-500 dark:text-gray-400 max-w-sm mx-auto">
              Sube tu primer PDF, enlace de YouTube o escribe texto directamente para empezar a entrenar a tu clon.
            </p>
          </div>
        ) : (
          <div className="divide-y divide-gray-100 dark:divide-gray-800">
            {sources.map((source) => (
              <div
                key={source.id}
                className="px-6 py-4 flex items-center justify-between hover:bg-gray-50 dark:hover:bg-gray-800/50"
              >
                <div className="flex items-center gap-3">
                  <span className="text-xl">
                    {source.type === "pdf" ? "📄" : source.type === "youtube" ? "🎥" : source.type === "text" ? "✍️" : source.type === "web" ? "🌐" : "📁"}
                  </span>
                  <div>
                    <p className="text-sm font-medium text-gray-900 dark:text-white">
                      {source.title}
                    </p>
                    <p className="text-xs text-gray-400">
                      {source.silo} · {source.status} · {source.wordCount} palabras
                    </p>
                  </div>
                </div>
                <span className="text-xs text-gray-400">
                  {new Date(source.createdAt).toLocaleDateString("es-ES")}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="mt-8 bg-gradient-to-r from-purple-600/10 to-pink-600/10 rounded-xl border border-purple-400/20 p-6">
        <div className="flex gap-4 items-start">
          <div className="text-3xl">💡</div>
          <div>
            <h3 className="font-semibold text-gray-900 dark:text-white">
              Consejo para mejores resultados
            </h3>
            <p className="mt-1 text-sm text-gray-600 dark:text-gray-400">
              Organiza tu contenido por silos: material del curso en Pedagogía,
              FAQs en Soporte, y catálogo de productos en Ventas. Así cada respuesta
              del clon será más precisa y contextual.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
