"use client";

import { useMemo } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { PageHeader } from "@/components/admin/PageHeader";
import { useAdminFetch } from "@/components/admin/useAdminFetch";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
} from "recharts";

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

  const planPieData = useMemo(() => {
    if (!data) return [];
    return Object.entries(data.plan_breakdown)
      .filter(([, count]) => count > 0)
      .map(([plan, count]) => ({
        name: PLAN_LABEL[plan] ?? plan,
        value: count,
        color: PLAN_COLOR[plan] ?? "#94A3B8",
      }));
  }, [data]);

  const financeBarData = useMemo(() => {
    if (!data) return [];
    return [
      {
        name: "Finance (30d)",
        MRR: data.mrr_cents,
        Costs: data.total_costs_cents,
        Margin: data.margin_cents,
      },
    ];
  }, [data]);

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

  const hasPlanData =
    Object.keys(data.plan_breakdown).length > 0 &&
    Object.values(data.plan_breakdown).some((v) => v > 0);

  const totalPlans = planPieData.reduce((sum, p) => sum + p.value, 0);

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

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        {/* MRR · Costs · Margin BarChart */}
        <div className="card lg:col-span-2">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-sm font-semibold text-[var(--text-primary)]">
              MRR · Costs · Margin (30d)
            </h2>
            <span className="text-xs text-[var(--text-muted)]">in cents</span>
          </div>
          <ResponsiveContainer width="100%" height={240}>
            <BarChart
              data={financeBarData}
              margin={{ top: 5, right: 20, left: 20, bottom: 5 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border-soft)" />
              <XAxis
                dataKey="name"
                tick={{ fontSize: 11, fill: "var(--text-muted)" }}
              />
              <YAxis
                tick={{ fontSize: 11, fill: "var(--text-muted)" }}
                tickFormatter={(v: number) =>
                  v >= 1000 ? `${(v / 1000).toFixed(1)}k` : String(v)
                }
              />
              <Tooltip
                contentStyle={{
                  background: "var(--surface-2)",
                  border: "1px solid var(--border-soft)",
                  borderRadius: 8,
                  fontSize: 12,
                }}
                formatter={(value: any) => [
                  `${Number(value).toLocaleString("en-US")} ¢`,
                ]}
              />
              <Legend
                wrapperStyle={{ fontSize: 11 }}
                iconType="circle"
              />
              <Bar
                dataKey="MRR"
                fill={FINANCE_COLORS.mrr}
                radius={[4, 4, 0, 0]}
                name="Revenue"
              />
              <Bar
                dataKey="Costs"
                fill={FINANCE_COLORS.costs}
                radius={[4, 4, 0, 0]}
                name="Costs"
              />
              <Bar
                dataKey="Margin"
                fill={
                  data.margin_cents >= 0
                    ? FINANCE_COLORS.margin
                    : FINANCE_COLORS.marginNeg
                }
                radius={[4, 4, 0, 0]}
                name="Margin"
              />
            </BarChart>
          </ResponsiveContainer>
          <div className="mt-3 flex flex-wrap items-center justify-between gap-3">
            <div className="flex flex-wrap gap-3 text-[11px] text-[var(--text-muted)]">
              <span className="flex items-center gap-1">
                <span
                  className="h-2 w-2 rounded-full"
                  style={{ background: FINANCE_COLORS.mrr }}
                />
                Revenue
              </span>
              <span className="flex items-center gap-1">
                <span
                  className="h-2 w-2 rounded-full"
                  style={{ background: FINANCE_COLORS.costs }}
                />
                Costs
              </span>
              <span className="flex items-center gap-1">
                <span
                  className="h-2 w-2 rounded-full"
                  style={{
                    background:
                      data.margin_cents >= 0
                        ? FINANCE_COLORS.margin
                        : FINANCE_COLORS.marginNeg,
                  }}
                />
                Margin
              </span>
            </div>
            <div
              className={`text-base font-semibold ${
                data.margin_cents >= 0
                  ? "text-[var(--color-accent-green)]"
                  : "text-[var(--color-accent-pink)]"
              }`}
            >
              Margin: {data.margin_display}
            </div>
          </div>
        </div>

        {/* Plan Distribution PieChart */}
        <div className="card">
          <h2 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Plan distribution
          </h2>
          {!hasPlanData ? (
            <p className="text-xs text-[var(--text-muted)]">
              No plan data yet.
            </p>
          ) : (
            <>
              <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                  <Pie
                    data={planPieData}
                    cx="50%"
                    cy="50%"
                    innerRadius={50}
                    outerRadius={80}
                    paddingAngle={3}
                    dataKey="value"
                    stroke="none"
                  >
                    {planPieData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip
                    contentStyle={{
                      background: "var(--surface-2)",
                      border: "1px solid var(--border-soft)",
                      borderRadius: 8,
                      fontSize: 12,
                    }}
                    formatter={(value: any, name: any) => [
                      `${value} (${totalPlans > 0 ? ((Number(value) / totalPlans) * 100).toFixed(0) : 0}%)`,
                      name,
                    ]}
                  />
                </PieChart>
              </ResponsiveContainer>
              <ul className="mt-3 space-y-1.5">
                {planPieData.map((plan) => (
                  <li
                    key={plan.name}
                    className="flex items-center justify-between text-xs"
                  >
                    <span className="flex items-center gap-1.5 text-[var(--text-secondary)]">
                      <span
                        className="h-2 w-2 rounded-full"
                        style={{ background: plan.color }}
                      />
                      {plan.name}
                    </span>
                    <span className="font-mono font-semibold text-[var(--text-primary)]">
                      {plan.value}
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
