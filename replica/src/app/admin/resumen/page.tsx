"use client"

import { useState, useEffect } from "react"

interface AdminOverview {
  total_tenants: number
  active_tenants: number
  total_clones: number
  mrr_cents: number
  mrr_display: string
  total_costs_cents: number
  total_costs_display: string
  margin_cents: number
  margin_display: string
  plan_breakdown: Record<string, number>
}

export default function AdminResumenPage() {
  const [data, setData] = useState<AdminOverview | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch("/api/admin/overview")
      .then((r) => r.ok ? r.json() : null)
      .then(setData)
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="animate-spin h-6 w-6 border-2 border-purple-600 border-t-transparent rounded-full" />
      </div>
    )
  }

  if (!data) return <div className="p-8 text-gray-400">Error cargando datos</div>

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">Resumen de Plataforma</h1>
      <p className="text-sm text-gray-500 mb-8">Panel de control multi-tenant</p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <StatCard label="Tenants" value={data.total_tenants} subtitle={`${data.active_tenants} activos`} />
        <StatCard label="Clones activos" value={data.total_clones} />
        <StatCard label="Total costes" value={data.total_costs_display} subtitle="Últimos 30 días" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">MRR</h3>
          <p className="text-4xl font-bold text-green-600">{data.mrr_display}</p>
          <div className="mt-4 grid grid-cols-2 gap-4">
            <div>
              <p className="text-xs text-gray-500">Margen</p>
              <p className={`text-lg font-bold ${data.margin_cents >= 0 ? "text-green-600" : "text-red-600"}`}>
                {data.margin_display}
              </p>
            </div>
            <div>
              <p className="text-xs text-gray-500">Costes</p>
              <p className="text-lg font-bold text-gray-700 dark:text-gray-300">{data.total_costs_display}</p>
            </div>
          </div>
        </div>

        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <h3 className="font-semibold text-gray-900 dark:text-white mb-4">Planes</h3>
          <div className="space-y-3">
            {Object.entries(data.plan_breakdown).map(([plan, count]) => (
              <div key={plan} className="flex items-center justify-between">
                <span className="text-sm text-gray-700 dark:text-gray-300 capitalize">{plan}</span>
                <span className="text-sm font-semibold text-gray-900 dark:text-white">{count}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

function StatCard({ label, value, subtitle }: { label: string; value: string | number; subtitle?: string }) {
  return (
    <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
      <p className="text-sm text-gray-500">{label}</p>
      <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">{value}</p>
      {subtitle && <p className="mt-1 text-xs text-gray-400">{subtitle}</p>}
    </div>
  )
}
