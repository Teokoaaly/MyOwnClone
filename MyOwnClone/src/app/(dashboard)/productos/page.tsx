"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { EmptyState } from "@/components/ui/EmptyState"

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
  const { status } = useSession()
  const router = useRouter()
  const [cloneId, setCloneId] = useState<string | null>(null)
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

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
      if (res.ok) {
        const data = await res.json()
        setProducts(Array.isArray(data) ? data : data.items ?? [])
      }
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
    setError(null)
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
    return <LoadingState label="Loading products..." rows={3} />
  }

  return (
    <div className="space-y-6">
      <header className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            Products
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            Manage products and services your clone can recommend in sales mode.
          </p>
        </div>
        <button
          type="button"
          onClick={() => setShowForm(!showForm)}
          className="btn-primary text-xs"
        >
          {showForm ? "Cancel" : "+ Add product"}
        </button>
      </header>

      {showForm && (
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] text-sm mb-4">New product</h3>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="md:col-span-2">
              <label className="stat-label" htmlFor="pr-name">Name</label>
              <input
                id="pr-name"
                type="text"
                value={formName}
                onChange={(e) => setFormName(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div className="md:col-span-2">
              <label className="stat-label" htmlFor="pr-desc">Description</label>
              <textarea
                id="pr-desc"
                rows={3}
                value={formDesc}
                onChange={(e) => setFormDesc(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none resize-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="pr-price">Price (cents)</label>
              <input
                id="pr-price"
                type="number"
                value={formPrice}
                onChange={(e) => setFormPrice(e.target.value)}
                placeholder="9900 = 99.00€"
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="pr-priority">Priority</label>
              <input
                id="pr-priority"
                type="number"
                value={formPriority}
                onChange={(e) => setFormPriority(Number(e.target.value))}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div className="md:col-span-2">
              <label className="stat-label" htmlFor="pr-url">Product URL</label>
              <input
                id="pr-url"
                type="url"
                value={formUrl}
                onChange={(e) => setFormUrl(e.target.value)}
                placeholder="https://yourdomain.com/product"
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
          </div>
          {error && <div className="mt-3"><ErrorState message={error} /></div>}
          <div className="mt-4 flex gap-2">
            <button
              type="button"
              onClick={createProduct}
              disabled={saving}
              className="btn-primary text-xs disabled:opacity-50"
            >
              {saving ? "Creating..." : "Create product"}
            </button>
            <button type="button" onClick={() => setShowForm(false)} className="btn-secondary text-xs">
              Cancel
            </button>
          </div>
        </div>
      )}

      {products.length === 0 ? (
        <EmptyState
          title="No products"
          description="Add products or services so your clone can recommend them during sales-mode conversations."
        />
      ) : (
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {products.map((p) => (
            <div key={p.id} className="card hover:border-[var(--border-medium)] transition-colors">
              <div className="flex items-start justify-between gap-2 mb-2">
                <h3 className="font-semibold text-[var(--text-primary)] text-sm">{p.name}</h3>
                {!p.active && (
                  <span className="badge-warning">Inactive</span>
                )}
              </div>
              {p.description && (
                <p className="text-xs text-[var(--text-muted)] mb-3 line-clamp-2">{p.description}</p>
              )}
              <div className="flex items-center justify-between">
                {p.price_cents != null && (
                  <span className="text-sm font-semibold text-[var(--color-accent-warm)] font-mono">
                    {(p.price_cents / 100).toFixed(2)}€
                  </span>
                )}
                {p.url && (
                  <a
                    href={p.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs text-[var(--color-accent-blue)] hover:underline truncate max-w-[150px]"
                  >
                    View product <span aria-hidden="true">↗</span>
                    <span className="sr-only">(opens in a new tab)</span>
                  </a>
                )}
              </div>
              <div className="mt-2 text-[10px] text-[var(--text-muted)] font-mono">
                Priority: {p.priority}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
