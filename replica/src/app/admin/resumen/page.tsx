"use client";

import { useMemo } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { BarChart, ChartLegend } from "@/components/ui/BarChart";
import { PageHeader } from "@/components/admin/PageHeader";
import { useAdminFetch } from "@/components/admin/useAdminFetch";

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

const PLAN_COLOR: Record<string, string> = {
  trial: "#06B6D4",
  basic: "#2563EB",
  pro: "#EA580C",
  scale: "#8B5CF6",
  enterprise: "#059669",
};

export default function AdminResumenPage() {
  const { data, loading, error, reload } = useAdminFetch<AdminOverview>(
    "/api/admin/overview",
  );

  const planRows = useMemo(() => {
    if (!data) return [];
    return Object.entries(data.plan_breakdown).map(([plan, count]) => ({
      label: PLAN_LABEL_ES[plan] ?? plan,
      values: [
        {
          label: plan,
          value: count,
          color: PLAN_COLOR[plan] ?? "#94A3B8",
        },
      ],
    }));
  }, [data]);

  const financeRows = useMemo(() => {
    if (!data) return [];
    return [
      {
        label: "MRR",
        values: [{ label: "MRR", value: data.mrr_cents, color: "#10B981" }],
      },
      {
        label: "Costes",
        values: [
          { label: "Costes", value: data.total_costs_cents, color: "#F97316" },
        ],
      },
      {
        label: "Margen",
        values: [
          {
            label: "Margen",
            value: data.margin_cents,
            color: data.margin_cents >= 0 ? "#2563EB" : "#DC2626",
          },
        ],
      },
    ];
  }, [data]);

  if (loading) {
    return <LoadingState label="Cargando resumen…" rows={4} />;
  }

  if (error || !data) {
    return (
      <ErrorState
        title="No se pudo cargar el resumen"
        message={error ?? "Sin datos"}
        action={
          <button
            type="button"
            onClick={reload}
            className="btn-secondary text-xs"
          >
            Reintentar
          </button>
        }
      />
    );
  }

  const statCards = [
    {
      label: "Tenants totales",
      value: data.total_tenants,
      subtitle: `${data.active_tenants} activos`,
    },
    {
      label: "Clones activos",
      value: data.total_clones,
      subtitle: "En producción",
    },
    {
      label: "MRR",
      value: data.mrr_display,
      subtitle: `${data.mrr_cents.toLocaleString("es-ES")} cents`,
    },
    {
      label: "Costes (30d)",
      value: data.total_costs_display,
      subtitle: "Últimos 30 días",
    },
  ];

  const hasPlanData =
    Object.keys(data.plan_breakdown).length > 0 &&
    Object.values(data.plan_breakdown).some((v) => v > 0);

  return (
    <div className="space-y-6">
      <PageHeader
        title="Platform Overview"
        subtitle={
          <>
            Métricas agregadas de la plataforma · generado{" "}
            <span className="font-mono">{data.generated_at}</span>
          </>
        }
      />

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {statCards.map((s) => (
          <div key={s.label} className="card">
            <div className="stat-label">{s.label}</div>
            <div className="stat-value mt-2">{s.value}</div>
            {s.subtitle && (
              <div className="mt-1 text-xs text-[var(--text-muted)]">
                {s.subtitle}
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <div className="card lg:col-span-2">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-sm font-semibold text-[var(--text-primary)]">
              MRR · Costes · Margen (30d)
            </h2>
            <span className="text-xs text-[var(--text-muted)]">en cents</span>
          </div>
          <BarChart data={financeRows} unit="¢" height={240} />
          <div className="mt-3 flex flex-wrap items-center justify-between gap-3">
            <ChartLegend
              items={[
                { label: "Ingresos", color: "#10B981" },
                { label: "Costes", color: "#F97316" },
                {
                  label: "Margen",
                  color: data.margin_cents >= 0 ? "#2563EB" : "#DC2626",
                },
              ]}
            />
            <div
              className={`text-base font-semibold ${
                data.margin_cents >= 0
                  ? "text-[var(--color-accent-green)]"
                  : "text-[var(--color-accent-pink)]"
              }`}
            >
              Margen: {data.margin_display}
            </div>
          </div>
        </div>

        <div className="card">
          <h2 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Distribución de planes
          </h2>
          {!hasPlanData ? (
            <p className="text-xs text-[var(--text-muted)]">
              Sin datos de planes todavía.
            </p>
          ) : (
            <>
              <BarChart
                data={planRows}
                height={180}
                max={Math.max(...Object.values(data.plan_breakdown), 1) * 1.2}
              />
              <ul className="mt-3 space-y-1.5">
                {Object.entries(data.plan_breakdown).map(([plan, count]) => (
                  <li
                    key={plan}
                    className="flex items-center justify-between text-xs"
                  >
                    <span className="flex items-center gap-1.5 text-[var(--text-secondary)]">
                      <span
                        className="h-2 w-2 rounded-full"
                        style={{ background: PLAN_COLOR[plan] ?? "#94A3B8" }}
                      />
                      {PLAN_LABEL_ES[plan] ?? plan}
                    </span>
                    <span className="font-mono font-semibold text-[var(--text-primary)]">
                      {count}
                    </span>
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
