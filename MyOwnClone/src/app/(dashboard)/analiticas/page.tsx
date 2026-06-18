"use client"

import { useState, useEffect, useCallback } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { EmptyState } from "@/components/ui/EmptyState"
import { useRouter } from "@/i18n/navigation"
import { useTranslations } from "next-intl";

export const dynamic = "force-dynamic"

// Plan token limits
const PLAN_TOKEN_LIMITS: Record<string, number> = {
  free: 2_000,
  pro: 20_000,
  enterprise: 100_000,
  custom: 100_000,
};
const DEFAULT_TOKEN_LIMIT = 2000;
const AVG_TOKENS_PER_MESSAGE = 200;

interface BillingSummary {
  plan: string | null;
  subscription_status?: string | null;
}

interface AnalyticsOverview {
  total_conversations: number
  total_messages: number
  questions_answered: number
  gaps_count: number
}

interface TopQuestion {
  question: string
  count: number
}

interface Gap {
  id: string
  question: string
  count: number
  suggested_source: string | null
  status: string
}

interface CostBreakdown {
  clone_response_cents: number
  content_ingestion_cents: number
  platform_ops_cents: number
  total_cents: number
}

function formatEur(cents: number) {
  return `${(cents / 100).toFixed(2)}€`
}

export default function AnaliticasPage() {
  const t = useTranslations("analytics");
  void t;
  const { status } = useSession()
  const router = useRouter()
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null)
  const [topQuestions, setTopQuestions] = useState<TopQuestion[]>([])
  const [gaps, setGaps] = useState<Gap[]>([])
  const [costs, setCosts] = useState<CostBreakdown | null>(null)
  const [billing, setBilling] = useState<BillingSummary | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  const fetchData = useCallback(async () => {
    setLoading(true)
    try {
      const [ov, tq, g, co, bi] = await Promise.all([
        fetch("/api/clone/analytics/overview").then((r) => r.ok ? r.json() : null),
        fetch("/api/clone/analytics/top-questions").then((r) => r.ok ? r.json() : []),
        fetch("/api/clone/analytics/gaps").then((r) => r.ok ? r.json() : []),
        fetch("/api/clone/analytics/costs").then((r) => r.ok ? r.json() : null),
        fetch("/api/clone/billing").then((r) => r.ok ? r.json() : null),
      ])
      setOverview(ov)
      setTopQuestions(tq)
      setGaps(g)
      setCosts(co)
      setBilling(bi)
    } catch {
      // Empty states
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchData()
  }, [fetchData])

  if (status === "loading" || loading) {
    return <LoadingState label="Loading analytics..." rows={4} />
  }

  const hasData =
    overview &&
    (overview.total_conversations > 0 ||
      overview.questions_answered > 0 ||
      overview.gaps_count > 0)

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Analytics
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Understand how users interact with your clone.
        </p>
      </header>
      {/* Token usage progress bar */}
      {(() => {
        const plan = billing?.plan || "free";
        const limit = PLAN_TOKEN_LIMITS[plan] || DEFAULT_TOKEN_LIMIT;
        const estTokens = (overview?.total_messages ?? 0) * AVG_TOKENS_PER_MESSAGE;
        const pct = Math.min(100, Math.round((estTokens / limit) * 100));
        const barColor = pct > 90
          ? "var(--color-accent-red,#DC2626)"
          : pct > 70
            ? "var(--color-accent-amber,#F59E0B)"
            : "var(--color-accent-green,#10B981)";

        return (
          <div className="card mb-6">
            <div className="flex items-center justify-between mb-2">
              <h3 className="font-semibold text-[var(--text-primary)] text-sm">
                Token usage
              </h3>
              <span className="text-xs text-[var(--text-muted)] font-mono">
                {estTokens.toLocaleString("es-ES")} / {limit.toLocaleString("es-ES")}
              </span>
            </div>
            <div className="w-full h-3 bg-[var(--surface-2)] rounded-full overflow-hidden">
              <div
                className="h-full rounded-full transition-all duration-700 ease-out"
                style={{ width: `${pct}%`, backgroundColor: barColor }}
              />
            </div>
            <div className="flex items-center justify-between mt-2">
              <span className="text-[11px] text-[var(--text-muted)]">
                {plan.charAt(0).toUpperCase() + plan.slice(1)} plan &middot; ~{AVG_TOKENS_PER_MESSAGE} tok/msg
              </span>
              <span className="text-[11px] font-mono font-medium" style={{ color: barColor }}>
                {pct}%
              </span>
            </div>
          </div>
        );
      })()}

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard label="Conversations" value={overview?.total_conversations ?? 0} />
        <StatCard label="Messages" value={overview?.total_messages ?? 0} />
        <StatCard label="Answered questions" value={overview?.questions_answered ?? 0} />
        <StatCard
          label="Knowledge gaps"
          value={overview?.gaps_count ?? 0}
          highlight={!!overview?.gaps_count && overview.gaps_count > 0}
        />
      </div>

      {!hasData ? (
        <EmptyState
          title="No data yet"
          description="Frequent questions, gaps, and costs will appear once your clone starts receiving conversations."
        />
      ) : (
        <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
          <div className="card">
            <h3 className="font-semibold text-[var(--text-primary)] mb-4">
              Frequent questions
            </h3>
            {topQuestions.length === 0 ? (
              <p className="text-sm text-[var(--text-muted)] py-4">
                Your most frequent questions will appear here once queries start coming in.
              </p>
            ) : (
              <ul className="space-y-3">
                {topQuestions.map((q, i) => (
                  <li key={i} className="flex items-center justify-between">
                    <p className="text-sm text-[var(--text-secondary)] truncate flex-1 mr-4">
                      {q.question}
                    </p>
                    <span className="badge-trial font-mono">
                      {q.count}
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </div>

          <div className="card">
            <h3 className="font-semibold text-[var(--text-primary)] mb-4">
              Knowledge gaps
            </h3>
            {gaps.length === 0 ? (
              <p className="text-sm text-[var(--text-muted)] py-4">
                Questions your clone could not answer. Add content to cover them.
              </p>
            ) : (
              <ul className="space-y-3">
                {gaps.map((g) => (
                  <li
                    key={g.id}
                    className="flex items-start gap-3 rounded-lg bg-[var(--surface-2)] p-3"
                  >
                    <span aria-hidden="true" className="text-[var(--color-accent-amber)] mt-0.5">⚠</span>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm text-[var(--text-secondary)]">
                        {g.question}
                      </p>
                      <p className="mt-1 font-mono text-[10px] text-[var(--text-muted)]">
                        {g.count} times · {g.status === "open" ? "Pending" : "Resolved"}
                      </p>
                    </div>
                    <button
                      onClick={() => router.push("/biblioteca")}
                      className="text-xs text-[var(--color-accent-warm)] hover:underline whitespace-nowrap"
                    >
                      + Content
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      )}

      {costs && (
        <div className="card">
          <h3 className="font-semibold text-[var(--text-primary)] mb-4">
            Current month costs
          </h3>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            <CostCard
              label="Clone responses"
              cents={costs.clone_response_cents}
              note="Billable to tenant"
            />
            <CostCard
              label="Content ingestion"
              cents={costs.content_ingestion_cents}
              note="Billable to tenant"
            />
            <CostCard
              label="Internal operations"
              cents={costs.platform_ops_cents}
              note="Paid by the platform"
            />
          </div>
          <div className="mt-4 pt-4 border-t border-[var(--border-soft)] flex items-center justify-between">
            <span className="text-sm font-medium text-[var(--text-secondary)]">
              Month total
            </span>
            <span className="stat-value text-xl">
              {formatEur(costs.total_cents)}
            </span>
          </div>
        </div>
      )}
    </div>
  )
}

function StatCard({ label, value, highlight }: { label: string; value: number; highlight?: boolean }) {
  return (
    <div className={["card", highlight ? "border-[var(--color-accent-amber)]/40" : ""].join(" ")}>
      <div className="stat-label">{label}</div>
      <div
        className={[
          "stat-value mt-2",
          highlight ? "text-[var(--color-accent-amber)]" : "",
        ].join(" ")}
      >
        {value.toLocaleString("es-ES")}
      </div>
    </div>
  )
}

function CostCard({ label, cents, note }: { label: string; cents: number; note: string }) {
  return (
    <div>
      <div className="stat-label">{label}</div>
      <div className="stat-value mt-1 text-2xl">{formatEur(cents)}</div>
      <p className="text-[10px] text-[var(--text-muted)] font-mono mt-1">{note}</p>
    </div>
  )
}
