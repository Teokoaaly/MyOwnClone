"use client"

import { useState, useEffect } from "react"

interface AdminTenant {
  id: string
  name: string
  plan: string | null
  status: string | null
  subscription_status: string | null
  created_at: number | null
}

export default function AdminTenantsPage() {
  const [tenants, setTenants] = useState<AdminTenant[]>([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState("")

  useEffect(() => {
    const params = new URLSearchParams()
    if (search) params.set("search", search)
    fetch(`/api/admin/tenants?${params}`)
      .then((r) => r.ok ? r.json() : [])
      .then(setTenants)
      .finally(() => setLoading(false))
  }, [search])

  return (
    <div className="p-8">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Tenants</h1>
          <p className="text-sm text-gray-500">Gestiona todas las cuentas de la plataforma</p>
        </div>
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Buscar tenant..."
          className="px-4 py-2 text-sm border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 outline-none w-64"
        />
      </div>

      {loading ? (
        <div className="flex h-64 items-center justify-center">
          <div className="animate-spin h-6 w-6 border-2 border-purple-600 border-t-transparent rounded-full" />
        </div>
      ) : tenants.length === 0 ? (
        <div className="text-center py-16 text-gray-400">No se encontraron tenants</div>
      ) : (
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 overflow-hidden">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-gray-800/50">
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase">Nombre</th>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase">Plan</th>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase">Estado</th>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500 uppercase">Suscripción</th>
                <th className="text-right px-6 py-3 text-xs font-medium text-gray-500 uppercase">Creado</th>
              </tr>
            </thead>
            <tbody>
              {tenants.map((t) => (
                <tr key={t.id} className="border-b border-gray-100 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800/30">
                  <td className="px-6 py-4 text-sm font-medium text-gray-900 dark:text-white">{t.name}</td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400 capitalize">{t.plan || "básico"}</td>
                  <td className="px-6 py-4 text-sm">
                    <span className={`px-2 py-0.5 text-xs rounded-full font-medium ${
                      t.status === "normal" ? "bg-green-100 dark:bg-green-950 text-green-700 dark:text-green-300" : "bg-gray-100 dark:bg-gray-800 text-gray-500"
                    }`}>
                      {t.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">{t.subscription_status || "—"}</td>
                  <td className="px-6 py-4 text-sm text-right text-gray-400">
                    {t.created_at ? new Date(t.created_at * 1000).toLocaleDateString("es-ES") : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}
