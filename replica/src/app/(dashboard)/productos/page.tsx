"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

interface Product {
  id: string
  name: string
  description: string | null
  price_cents: number | null
  url: string | null
  image_url: string | null
  priority: number
  active: boolean
}

export default function ProductosPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [cloneId, setCloneId] = useState<string | null>(null)
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [saving, setSaving] = useState(false)

  const [formName, setFormName] = useState("")
  const [formDesc, setFormDesc] = useState("")
  const [formPrice, setFormPrice] = useState("")
  const [formUrl, setFormUrl] = useState("")
  const [formPriority, setFormPriority] = useState(0)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchProducts = useCallback(async () => {
    setLoading(true)
    try {
      const clonesRes = await fetch("/api/clone/clones")
      if (!clonesRes.ok) return
      const clones = await clonesRes.json()
      if (clones.length === 0) return
      const cid = clones[0].id
      setCloneId(cid)

      const res = await fetch(`/api/clone/clones/${cid}/products`)
      if (res.ok) setProducts(await res.json())
    } catch {
      // Empty state
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchProducts()
  }, [fetchProducts])

  const createProduct = async () => {
    if (!cloneId || !formName.trim()) return
    setSaving(true)
    try {
      const res = await fetch(`/api/clone/clones/${cloneId}/products`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: formName,
          description: formDesc || null,
          price_cents: formPrice ? Number(formPrice) : null,
          url: formUrl || null,
          priority: formPriority,
          active: true,
        }),
      })
      if (res.ok) {
        setShowForm(false)
        setFormName("")
        setFormDesc("")
        setFormPrice("")
        setFormUrl("")
        setFormPriority(0)
        fetchProducts()
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
            Productos
          </h1>
          <p className="mt-1 text-gray-500 dark:text-gray-400">
            Gestiona los productos y servicios que tu clon puede recomendar en modo ventas.
          </p>
        </div>
        <button
          onClick={() => setShowForm(!showForm)}
          className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors"
        >
          + Añadir producto
        </button>
      </div>

      {showForm && (
        <div className="mb-6 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">Nuevo producto</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Nombre</label>
              <input type="text" value={formName} onChange={(e) => setFormName(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Descripción</label>
              <textarea rows={3} value={formDesc} onChange={(e) => setFormDesc(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none resize-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Precio (céntimos)</label>
              <input type="number" value={formPrice} onChange={(e) => setFormPrice(e.target.value)}
                placeholder="9900 = 99.00€"
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Prioridad</label>
              <input type="number" value={formPriority} onChange={(e) => setFormPriority(Number(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">URL del producto</label>
              <input type="url" value={formUrl} onChange={(e) => setFormUrl(e.target.value)}
                placeholder="https://tudominio.com/producto"
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none text-sm" />
            </div>
          </div>
          <div className="mt-4 flex gap-2">
            <button onClick={createProduct} disabled={saving}
              className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50">
              {saving ? "Creando..." : "Crear producto"}
            </button>
            <button onClick={() => setShowForm(false)}
              className="px-4 py-2 text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
              Cancelar
            </button>
          </div>
        </div>
      )}

      <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
        {products.length === 0 ? (
          <div className="text-center py-12">
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center">
              <svg className="w-8 h-8 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              No hay productos
            </h3>
            <p className="mt-2 text-gray-500 dark:text-gray-400 max-w-sm mx-auto">
              Añade tus productos o servicios para que tu clon pueda recomendarlos durante las conversaciones en modo ventas.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {products.map((p) => (
              <div key={p.id} className="rounded-xl border border-gray-200 dark:border-gray-800 p-4 hover:shadow-md transition-shadow">
                <div className="flex items-start justify-between mb-2">
                  <h3 className="font-semibold text-gray-900 dark:text-white text-sm">{p.name}</h3>
                  {!p.active && (
                    <span className="text-xs px-2 py-0.5 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-500">
                      Inactivo
                    </span>
                  )}
                </div>
                {p.description && (
                  <p className="text-xs text-gray-500 dark:text-gray-400 mb-3 line-clamp-2">{p.description}</p>
                )}
                <div className="flex items-center justify-between">
                  {p.price_cents != null && (
                    <span className="text-sm font-bold text-purple-600 dark:text-purple-400">
                      {(p.price_cents / 100).toFixed(2)}€
                    </span>
                  )}
                  {p.url && (
                    <a href={p.url} target="_blank" rel="noopener noreferrer"
                      className="text-xs text-blue-600 dark:text-blue-400 hover:underline truncate max-w-[150px]">
                      Ver producto →
                    </a>
                  )}
                </div>
                <div className="mt-2 text-xs text-gray-400">
                  Prioridad: {p.priority}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
