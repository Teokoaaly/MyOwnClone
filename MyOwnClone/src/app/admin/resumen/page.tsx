"use client";

import dynamic from "next/dynamic";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { PageHeader } from "@/components/admin/PageHeader";
import { useAdminFetch } from "@/components/admin/useAdminFetch";

const AdminCharts = dynamic(
  () => import("@/components/admin/AdminCharts").then((mod) => mod.AdminCharts),
  {
    ssr: false,
    loading: () => (
      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <div className="card lg:col-span-2">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-sm font-semibold text-[var(--text-primary)]">
              MRR · Costs · Margin (30d)
            </h2>
          </div>
          <div className="flex h-60 items-center justify-center">
            <LoadingState label="Loading charts..." />
          </div>
        </div>
        <div className="card">
          <h2 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Plan distribution
          </h2>
          <div className="flex h-52 items-center justify-center">
            <LoadingState label="Loading charts..." />
          </div>
        </div>
      </div>
    ),
  }
);

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

const PLAN_LABEL: Record<string, string> = {
  free: "Free Plan",
  pro: "Pro Plan",
  enterprise: "Enterprise",
};

const PLAN_COLOR: Record<string, string> = {
  free: "#06B6D4",
  pro: "#EA580C",
  enterprise: "#059669",
};

const FINANCE_COLORS = {
  mrr: "#10B981",
  costs: "#F97316",
  margin: "#2563EB",
  marginNeg: "#DC2626",
};
export default function AdminResumenPage() {
  const { data, loading, error, reload } = useAdminFetch<AdminOverview>(
    "/api/admin/overview",
  );


  if (loading) {
    return <LoadingState label="Loading overview..." rows={4} />;
  }

  if (error || !data) {
    return (
      <ErrorState
        title="Could not load overview"
        message={error ?? "No data"}
        action={
          <button
            type="button"
            onClick={reload}
            className="btn-secondary text-xs"
          >
            Try again
          </button>
        }
      />
    );
  }

  const statCards = [
    {
      label: "Total tenants",
      value: data.total_tenants,
      subtitle: `${data.active_tenants} active`,
    },
    {
      label: "Active clones",
      value: data.total_clones,
      subtitle: "In production",
    },
    {
      label: "MRR",
      value: data.mrr_display,
      subtitle: `${data.mrr_cents.toLocaleString("en-US")} cents`,
    },
    {
      label: "Costs (30d)",
      value: data.total_costs_display,
      subtitle: "Last 30 days",
    },
  ];

  return (
    <div className="space-y-6">
      <PageHeader
        title="Platform Overview"
        subtitle={
          <>
            Aggregated platform metrics · generated{" "}
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

<AdminCharts data={data} />
    </div>
  );
}
