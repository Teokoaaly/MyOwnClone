"use client";

export const dynamic = "force-dynamic"


import { useState, useEffect, useCallback } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import {
  StatsCard,
  QuickActionCard,
  OnboardingBanner,
  HeaderBreadcrumb,
} from "@/components/dashboard";
import { ShortcutIcons } from "@/components/ui/dashboard-icons";
import { LoadingState } from "@/components/ui/LoadingState";
import { EmptyState } from "@/components/ui/EmptyState";
import { ErrorState } from "@/components/ui/ErrorState";
import { BarChart, ChartLegend } from "@/components/ui/BarChart";

interface AnalyticsOverview {
  total_conversations: number;
  total_messages: number;
  questions_answered: number;
  gaps_count: number;
  active_sessions?: number;
  automation_rate?: number;
  /** When the overview endpoint doesn't return these, we use 0. */
  clones_count?: number;
}

interface InboxListItem {
  id: string;
  subject: string | null;
  from_email: string | null;
  status: string;
  received_at: number | null;
}

export default function DashboardResumenPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null);
  const [recentInbox, setRecentInbox] = useState<InboxListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login");
  }, [status, router]);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [overviewRes, inboxRes] = await Promise.allSettled([
        fetch("/api/clone/analytics/overview"),
        fetch("/api/clone/inbox/list?limit=3"),
      ]);

      if (overviewRes.status === "fulfilled" && overviewRes.value.ok) {
        setOverview(await overviewRes.value.json());
      }
      if (inboxRes.status === "fulfilled" && inboxRes.value.ok) {
        const data = await inboxRes.value.json();
        setRecentInbox(Array.isArray(data) ? data : data.items ?? []);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error cargando datos");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  if (status === "loading" || loading) {
    return <LoadingState label="Cargando resumen…" rows={4} />;
  }

  if (error) {
    return (
      <ErrorState
        message={error}
        action={
          <button
            type="button"
            onClick={fetchData}
            className="btn-secondary text-xs"
          >
            Reintentar
          </button>
        }
      />
    );
  }

  const stats = [
    {
      icon: ShortcutIcons.upload,
      label: "AI Clones",
      value: overview?.clones_count ?? 0,
      emptyLabel: "No clones yet",
    },
    {
      icon: ShortcutIcons.analytics,
      label: "Active Sessions",
      value: overview?.active_sessions ?? 0,
      emptyLabel: "No active sessions",
    },
    {
      icon: ShortcutIcons.analytics,
      label: "Automation Rate",
      value: overview?.automation_rate ?? 0,
      suffix: "%",
      emptyLabel: "Awaiting data",
    },
  ];

  const quickActions = [
    {
      href: "/biblioteca",
      icon: ShortcutIcons.upload,
      label: "Upload Content",
      description: "PDFs, YouTube, text and more",
      iconColor: "text-[var(--color-accent-warm)]",
    },
    {
      href: "/cerebro",
      icon: ShortcutIcons.memory,
      label: "Train Memory",
      description: "Data your clone will remember",
      iconColor: "text-[var(--color-accent-cyan)]",
    },
    {
      href: "/inbox",
      icon: ShortcutIcons.inbox,
      label: "Review Inbox",
      description: "Pending email responses",
      iconColor: "text-[var(--color-accent-violet)]",
    },
    {
      href: "/analiticas",
      icon: ShortcutIcons.analytics,
      label: "View Analytics",
      description: "Questions, gaps and costs",
      iconColor: "text-[var(--color-accent-green)]",
    },
  ];

  // Sparkline-ish chart for the last 30 days. We synthesise a 7-bar
  // view of `total_conversations`, `questions_answered`, `gaps_count`.
  const sparkData = [
    {
      label: "Conversations",
      values: [
        { label: "Conversations", value: overview?.total_conversations ?? 0, color: "#EA580C" },
      ],
    },
    {
      label: "Questions",
      values: [
        { label: "Questions", value: overview?.questions_answered ?? 0, color: "#0891B2" },
      ],
    },
    {
      label: "Gaps",
      values: [
        { label: "Gaps", value: overview?.gaps_count ?? 0, color: "#8B5CF6" },
      ],
    },
  ];

  const sparkMax = Math.max(
    1,
    overview?.total_conversations ?? 0,
    overview?.questions_answered ?? 0,
    overview?.gaps_count ?? 0,
  );

  return (
    <div className="space-y-8">
      {/* Header */}
      <HeaderBreadcrumb
        title="Workspace Overview"
        breadcrumbs={["MyOwnClone", "Dashboard"]}
        user={{
          name: session?.user?.name,
          email: session?.user?.email,
          image: session?.user?.image ?? undefined,
        }}
        action={
          <Link href="/configuracion" className="btn-primary text-xs">
            Create Clone
          </Link>
        }
      />

      {/* Stats row */}
      <section>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {stats.map((s) => (
            <StatsCard
              key={s.label}
              icon={s.icon}
              label={s.label}
              value={s.value}
              suffix={"suffix" in s ? s.suffix : undefined}
              emptyLabel={s.emptyLabel}
            />
          ))}
        </div>
      </section>

      {/* Activity chart */}
      <section className="card">
        <div className="mb-4 flex items-center justify-between">
          <h2 className="text-sm font-semibold text-[var(--text-primary)]">
            Actividad últimos 30 días
          </h2>
          <span className="text-xs text-[var(--text-muted)]">totales acumulados</span>
        </div>
        {overview === null ||
        (overview.total_conversations === 0 &&
          overview.questions_answered === 0 &&
          overview.gaps_count === 0) ? (
          <EmptyState
            title="Sin actividad todavía"
            description="Cuando tu clon empiece a recibir conversaciones, verás aquí el resumen."
          />
        ) : (
          <>
            <BarChart data={sparkData} height={200} max={sparkMax * 1.2} />
            <div className="mt-3">
              <ChartLegend
                items={[
                  { label: "Conversations", color: "#EA580C" },
                  { label: "Questions", color: "#0891B2" },
                  { label: "Gaps", color: "#8B5CF6" },
                ]}
              />
            </div>
          </>
        )}
      </section>

      {/* Inbox preview */}
      <section className="card">
        <div className="mb-4 flex items-center justify-between">
          <h2 className="text-sm font-semibold text-[var(--text-primary)]">
            Inbox reciente
          </h2>
          <Link
            href="/inbox"
            className="text-xs text-[var(--color-accent-warm)] hover:underline"
          >
            Ver todo →
          </Link>
        </div>
        {recentInbox.length === 0 ? (
          <EmptyState
            title="Bandeja vacía"
            description="Los correos que lleguen a tu clon aparecerán aquí."
          />
        ) : (
          <ul className="space-y-2">
            {recentInbox.slice(0, 3).map((item) => (
              <li
                key={item.id}
                className="flex items-center justify-between rounded-lg border border-[var(--border-soft)] bg-[var(--surface-1)] px-3 py-2 hover:border-[var(--border-medium)] transition-colors"
              >
                <div className="min-w-0 flex-1">
                  <p className="truncate text-sm font-medium text-[var(--text-primary)]">
                    {item.subject ?? "(sin asunto)"}
                  </p>
                  <p className="truncate text-xs text-[var(--text-muted)]">
                    {item.from_email ?? "—"}
                  </p>
                </div>
                <span className="ml-3 shrink-0 font-mono text-[10px] text-[var(--text-muted)]">
                  {item.received_at
                    ? new Date(item.received_at * 1000).toLocaleDateString("es-ES")
                    : "—"}
                </span>
              </li>
            ))}
          </ul>
        )}
      </section>

      {/* Quick actions */}
      <section>
        <h2 className="section-label mb-3">Quick Actions</h2>
        <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
          {quickActions.map((action) => (
            <QuickActionCard
              key={action.href}
              href={action.href}
              icon={action.icon}
              label={action.label}
              description={action.description}
              iconColor={action.iconColor}
            />
          ))}
        </div>
      </section>

      {/* Onboarding banner */}
      <OnboardingBanner completedSteps={0} totalSteps={4} />
    </div>
  );
}
