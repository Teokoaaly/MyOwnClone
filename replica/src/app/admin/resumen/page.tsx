"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

interface AdminOverview {
  total_tenants: number;
  active_tenants: number;
  total_clones: number;
  mrr_cents: number;
  mrr_display: string;
  total_costs_cents: number;
  total_costs_display: string;
  margin_cents: number;
  margin_display: string;
  plan_breakdown: Record<string, number>;
  generated_at: string;
}

const PLAN_LABEL_ES: Record<string, string> = {
  trial: "Trial",
  basic: "Básico",
  pro: "Pro",
  scale: "Escala",
  enterprise: "Enterprise",
};

export default function AdminResumenPage() {
  const router = useRouter();
  const [data, setData] = useState<AdminOverview | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    async function load() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch("/api/admin/overview", { cache: "no-store" });
        if (res.status === 401) {
          router.push("/login");
          return;
        }
        if (!res.ok) {
          throw new Error(`Backend error ${res.status}`);
        }
        const payload = (await res.json()) as AdminOverview;
        if (!cancelled) setData(payload);
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : "Error cargando datos");
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    }
    load();
    return () => {
      cancelled = true;
    };
  }, [router]);

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="flex gap-1">
          <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:150ms]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:300ms]" />
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="card border-red-200 bg-red-50/40">
        <p className="text-sm font-medium text-red-700">No se pudo cargar el resumen</p>
        <p className="mt-1 text-xs text-red-600">{error ?? "Sin datos"}</p>
      </div>
    );
  }

  const statCards = [
    { label: "Tenants totales", value: data.total_tenants, subtitle: `${data.active_tenants} activos` },
    { label: "Clones activos", value: data.total_clones, subtitle: "En producción" },
    { label: "MRR", value: data.mrr_display, subtitle: `${data.mrr_cents} cents` },
    { label: "Costes (30d)", value: data.total_costs_display, subtitle: "Últimos 30 días" },
  ];

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Platform Overview
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Métricas agregadas de la plataforma · generado{" "}
          <span className="font-mono">{data.generated_at}</span>
        </p>
      </header>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {statCards.map((s) => (
          <div key={s.label} className="card">
            <div className="stat-label">{s.label}</div>
            <div className="stat-value mt-2">{s.value}</div>
            {s.subtitle && (
              <div className="mt-1 text-xs text-[var(--text-muted)]">{s.subtitle}</div>
            )}
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <div className="card lg:col-span-2">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-sm font-semibold text-[var(--text-primary)]">Margin</h2>
            <span className="text-xs text-[var(--text-muted)]">MRR − Costes (30d)</span>
          </div>
          <div className="flex items-end gap-6">
            <div>
              <div className="stat-value text-[36px]">
                <span
                  className={
                    data.margin_cents >= 0
                      ? "text-[var(--color-accent-green)]"
                      : "text-red-500"
                  }
                >
                  {data.margin_display}
                </span>
              </div>
              <div className="text-xs text-[var(--text-muted)]">
                {data.margin_cents >= 0 ? "Margen positivo" : "Margen negativo"}
              </div>
            </div>
            <div className="grid grid-cols-2 gap-6 text-sm">
              <div>
                <div className="stat-label">Ingresos</div>
                <div className="font-mono text-base text-[var(--text-primary)]">
                  {data.mrr_display}
                </div>
              </div>
              <div>
                <div className="stat-label">Costes</div>
                <div className="font-mono text-base text-[var(--text-primary)]">
                  {data.total_costs_display}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="card">
          <h2 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Planes contratados
          </h2>
          <div className="space-y-3">
            {Object.entries(data.plan_breakdown).map(([plan, count]) => (
              <div key={plan} className="flex items-center justify-between">
                <span className="text-sm text-[var(--text-secondary)]">
                  {PLAN_LABEL_ES[plan] ?? plan}
                </span>
                <span className="font-mono text-sm font-semibold text-[var(--text-primary)]">
                  {count}
                </span>
              </div>
            ))}
            {Object.keys(data.plan_breakdown).length === 0 && (
              <div className="text-xs text-[var(--text-muted)]">
                Sin datos de planes todavía.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
