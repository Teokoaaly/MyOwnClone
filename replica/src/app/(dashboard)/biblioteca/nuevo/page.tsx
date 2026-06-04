"use client"

import { useState, useEffect, Suspense } from "react"
import { useSession } from "next-auth/react"
import { useRouter, useSearchParams } from "next/navigation"

const SILOS = [
  { id: "teach", label: "Pedagogía", emoji: "📚" },
  { id: "support", label: "Soporte", emoji: "💬" },
  { id: "sales", label: "Ventas", emoji: "🛒" },
]

const TYPE_LABELS: Record<string, string> = {
  pdf: "Subir PDF",
  youtube: "Enlace de YouTube",
  text: "Escribir texto",
  web: "Página web",
  interview: "Entrevista AI",
}

function NuevoContentPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const searchParams = useSearchParams()
  const tipo = searchParams.get("tipo") || "text"

  const [silo, setSilo] = useState("teach")
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(false)

  if (status === "loading") return <div className="flex h-64 items-center justify-center"><div className="flex gap-1"><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:150ms]" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:300ms]" /></div></div>
  if (status === "unauthenticated") { router.push("/login"); return null }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
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

      if (res.ok) {
        setSuccess(true)
      }
    } catch {
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <button onClick={() => router.back()} className="mb-4 text-sm text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">← Volver a la biblioteca</button>
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">{TYPE_LABELS[tipo] || "Nuevo contenido"}</h1>
      <p className="mt-1 text-gray-500 dark:text-gray-400">Añade contenido al conocimiento de tu clon.</p>

      {success ? (
        <div className="mt-8 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-8 text-center">
          <div className="text-4xl mb-4">✅</div>
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Contenido añadido</h3>
          <p className="mt-2 text-gray-500 dark:text-gray-400">El contenido se está procesando. Tu clon podrá usarlo en unos minutos.</p>
          <button onClick={() => router.push("/biblioteca")} className="mt-6 px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors">Volver a la biblioteca</button>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="mt-6 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Silo de contenido</label>
            <div className="flex gap-2">
              {SILOS.map((s) => (
                <button key={s.id} type="button" onClick={() => setSilo(s.id)} className={`flex items-center gap-1.5 px-4 py-2 rounded-lg text-sm font-medium border transition-all ${silo === s.id ? "border-purple-600 bg-purple-50 dark:bg-purple-950 text-purple-600" : "border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400 hover:border-gray-300"}`}>
                  {s.emoji} {s.label}
                </button>
              ))}
            </div>
          </div>

          {tipo === "pdf" && (
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Archivo PDF</label>
              <input type="file" accept=".pdf,.doc,.docx,.txt" className="w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-purple-600 file:text-white hover:file:bg-purple-700" />
            </div>
          )}

          {(tipo === "youtube" || tipo === "web") && (
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">URL</label>
              <input type="url" placeholder={tipo === "youtube" ? "https://youtube.com/watch?v=..." : "https://ejemplo.com/articulo"} className="w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none" />
            </div>
          )}

          {tipo === "text" && (
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Contenido</label>
              <textarea rows={8} placeholder="Pega o escribe el contenido aquí..." className="w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none resize-none" />
            </div>
          )}

          {tipo === "interview" && (
            <div className="bg-purple-50 dark:bg-purple-950 rounded-xl p-4 border border-purple-200 dark:border-purple-800">
              <p className="text-sm text-purple-800 dark:text-purple-300">🎙️ La entrevista AI es una conversación con tu clon donde él te hará preguntas para extraer tu conocimiento automáticamente.</p>
              <p className="mt-2 text-xs text-purple-600 dark:text-purple-400">Esta funcionalidad estará disponible próximamente.</p>
            </div>
          )}

          <div className="pt-2">
            <button type="submit" disabled={loading || tipo === "interview"} className="px-6 py-3 bg-purple-600 text-white font-medium rounded-xl hover:bg-purple-700 transition-colors disabled:opacity-50">
              {loading ? "Procesando..." : tipo === "interview" ? "Próximamente" : "Añadir contenido"}
            </button>
          </div>
        </form>
      )}
    </div>
  )
}

export default function NuevoPage() {
  return (
    <Suspense fallback={<div className="flex h-64 items-center justify-center"><div className="flex gap-1"><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:150ms]" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:300ms]" /></div></div>}>
      <NuevoContentPage />
    </Suspense>
  )
}
