"use client";

import { useMemo } from "react";
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

const PLAN_COLOR: Record<string, string> = {
  trial: "#06B6D4",
  basic: "#2563EB",
  pro: "#EA580C",
  scale: "#8B5CF6",
  enterprise: "#059669",
};

const FINANCE_COLORS = {
  mrr: "#10B981",
  costs: "#F97316",
  margin: "#2563EB",
  marginNeg: "#DC2626",
};

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

interface AdminChartsProps {
  data: AdminOverview;
}

export function AdminCharts({ data }: AdminChartsProps) {
  const planPieData = useMemo(() => {
    return Object.entries(data.plan_breakdown)
      .filter(([, count]) => count > 0)
      .map(([plan, count]) => ({
        name: plan.charAt(0).toUpperCase() + plan.slice(1),
        value: count,
        color: PLAN_COLOR[plan] ?? "#94A3B8",
      }));
  }, [data.plan_breakdown]);

  const financeBarData = useMemo(() => {
    return [
      {
        name: "Finance (30d)",
        MRR: data.mrr_cents,
        Costs: data.total_costs_cents,
        Margin: data.margin_cents,
      },
    ];
  }, [data]);

  const hasPlanData =
    Object.keys(data.plan_breakdown).length > 0 &&
    Object.values(data.plan_breakdown).some((v) => v > 0);

  const totalPlans = planPieData.reduce((sum, p) => sum + p.value, 0);

  return (
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
            ***REMOVED***ll={FINANCE_COLORS.mrr}
              radius={[4, 4, 0, 0]}
              name="Revenue"
            />
            <Bar
              dataKey="Costs"
            ***REMOVED***ll={FINANCE_COLORS.costs}
              radius={[4, 4, 0, 0]}
              name="Costs"
            />
            <Bar
              dataKey="Margin"
            ***REMOVED***ll={
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
  );
}
