"use client"

import { useState } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

const STEPS = [
  { id: "name", title: "Nombre del clon", subtitle: "¿Cómo se llamará tu asistente?" },
  { id: "personality", title: "Personalidad", subtitle: "Elige el tono de tu clon" },
  { id: "language", title: "Idioma", subtitle: "¿En qué idioma hablará?" },
  { id: "confirm", title: "Confirmar", subtitle: "Revisa y crea tu clon" },
]

const TONES = [
  { value: "formal", label: "Formal", emoji: "👔" },
  { value: "informal", label: "Informal", emoji: "👋" },
  { value: "cercano", label: "Cercano", emoji: "🤝" },
  { value: "técnico", label: "Técnico", emoji: "🔧" },
]

export default function OnboardingPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [step, setStep] = useState(0)
  const [name, setName] = useState("")
  const [slug, setSlug] = useState("")
  const [tone, setTone] = useState("formal")
  const [language, setLanguage] = useState("es")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  if (status === "loading") return <div className="flex h-screen items-center justify-center"><div className="flex gap-1"><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:150ms]" /><span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:300ms]" /></div></div>
  if (status === "unauthenticated") { router.push("/login"); return null }

  const generateSlug = (n: string) => n.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")

  const canNext = () => {
    if (step === 0) return name.length >= 2
    if (step === 1) return true
    if (step === 2) return true
    return true
  }

  const handleCreate = async () => {
    setLoading(true)
    setError("")
    try {
      const finalSlug = slug || generateSlug(name)
      const res = await fetch("/api/clone/clones", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          slug: finalSlug,
          language,
          personality_tone: tone,
          active_modes: ["teach", "support", "sales"],
        }),
      })
      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        throw new Error(data.error || "Error al crear el clon")
      }
      router.push("/dashboard/resumen")
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error al crear el clon")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-950 flex flex-col items-center justify-center px-4 py-8">
      <div className="w-full max-w-lg">
        <div className="mb-8 flex gap-2">
          {STEPS.map((s, i) => (
            <div key={s.id} className={`flex-1 h-1.5 rounded-full transition-colors ${i <= step ? "bg-purple-600" : "bg-gray-200 dark:bg-gray-700"}`} />
          ))}
        </div>

        <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-lg p-8">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">{STEPS[step].title}</h1>
          <p className="mt-1 text-gray-500 dark:text-gray-400 text-sm">{STEPS[step].subtitle}</p>

          {error && <div className="mt-4 rounded-lg border border-red-800 bg-red-950/50 px-4 py-3 text-sm text-red-300">{error}</div>}

          <div className="mt-6">
            {step === 0 && (
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Nombre del clon</label>
                  <input type="text" value={name} onChange={(e) => { setName(e.target.value); setSlug(generateSlug(e.target.value)) }} placeholder="Ej: Asistente de Juan" className="w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">URL público</label>
                  <input type="text" value={slug} onChange={(e) => setSlug(generateSlug(e.target.value))} placeholder="asistente-de-juan" className="w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none font-mono text-sm" />
                  {slug && <p className="mt-1 text-xs text-gray-400">{slug}.replica.tudominio.com</p>}
                </div>
              </div>
            )}

            {step === 1 && (
              <div className="grid grid-cols-2 gap-3">
                {TONES.map((t) => (
                  <button key={t.value} onClick={() => setTone(t.value)} className={`flex flex-col items-center gap-2 p-4 rounded-xl border-2 transition-all ${tone === t.value ? "border-purple-600 bg-purple-50 dark:bg-purple-950" : "border-gray-200 dark:border-gray-700 hover:border-gray-300"}`}>
                    <span className="text-2xl">{t.emoji}</span>
                    <span className="text-sm font-medium text-gray-900 dark:text-white">{t.label}</span>
                  </button>
                ))}
              </div>
            )}

            {step === 2 && (
              <div className="grid grid-cols-2 gap-3">
                {[{ value: "es", label: "Español", emoji: "🇪🇸" }, { value: "en", label: "English", emoji: "🇬🇧" }].map((l) => (
                  <button key={l.value} onClick={() => setLanguage(l.value)} className={`flex flex-col items-center gap-2 p-4 rounded-xl border-2 transition-all ${language === l.value ? "border-purple-600 bg-purple-50 dark:bg-purple-950" : "border-gray-200 dark:border-gray-700 hover:border-gray-300"}`}>
                    <span className="text-2xl">{l.emoji}</span>
                    <span className="text-sm font-medium text-gray-900 dark:text-white">{l.label}</span>
                  </button>
                ))}
              </div>
            )}

            {step === 3 && (
              <div className="space-y-4">
                <div className="rounded-xl border border-gray-200 dark:border-gray-800 p-4 space-y-2">
                  <div className="flex justify-between text-sm"><span className="text-gray-500">Nombre</span><span className="text-gray-900 dark:text-white font-medium">{name}</span></div>
                  <div className="flex justify-between text-sm"><span className="text-gray-500">URL</span><span className="text-gray-900 dark:text-white font-medium font-mono">{slug || generateSlug(name)}</span></div>
                  <div className="flex justify-between text-sm"><span className="text-gray-500">Tono</span><span className="text-gray-900 dark:text-white font-medium">{TONES.find(t => t.value === tone)?.label}</span></div>
                  <div className="flex justify-between text-sm"><span className="text-gray-500">Idioma</span><span className="text-gray-900 dark:text-white font-medium">{language === "es" ? "Español" : "English"}</span></div>
                </div>
              </div>
            )}
          </div>

          <div className="mt-8 flex justify-between">
            {step > 0 ? (
              <button onClick={() => setStep(step - 1)} className="px-4 py-2 text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">← Atrás</button>
            ) : <div />}
            {step < 3 ? (
              <button onClick={() => setStep(step + 1)} disabled={!canNext()} className="px-6 py-2 bg-purple-600 text-white text-sm font-medium rounded-xl hover:bg-purple-700 transition-colors disabled:opacity-50">Siguiente</button>
            ) : (
              <button onClick={handleCreate} disabled={loading} className="px-6 py-2 bg-purple-600 text-white text-sm font-medium rounded-xl hover:bg-purple-700 transition-colors disabled:opacity-50">{loading ? "Creando..." : "Crear mi clon"}</button>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
