"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import {
  ArrowSquareOut,
  ChartBar,
  FileDoc,
  Globe,
  Key,
  Lightning,
  MagnifyingGlass,
  PaperPlaneRight,
  SquaresFour,
} from "@phosphor-icons/react";
import { EmptyState } from "@/components/ui/EmptyState";
import { ErrorState } from "@/components/ui/ErrorState";
import { LoadingState } from "@/components/ui/LoadingState";
import { OnboardingBanner } from "@/components/dashboard/OnboardingBanner";
import ReflectiveOrb from "@/components/ui/ReflectiveOrb";

interface AnalyticsOverview {
  total_conversations: number;
  total_messages: number;
  questions_answered: number;
  gaps_count: number;
  active_sessions?: number;
  automation_rate?: number;
  clones_count?: number;
}

interface InboxListItem {
  id: string;
  subject: string | null;
  from_email: string | null;
  status: string;
  received_at: number | null;
}

const fallbackBars = [14, 18, 22, 16, 28, 36, 54, 48, 60, 42, 30, 26, 18, 22, 34, 28, 20, 18, 24, 16];

export default function DashboardResumenPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null);
  const [recentInbox, setRecentInbox] = useState<InboxListItem[]>([]);
  const [clonesCount, setClonesCount] = useState<number | null>(null);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login");
  }, [status, router]);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [overviewRes, inboxRes, clonesRes] = await Promise.allSettled([
        fetch("/api/clone/analytics/overview"),
        fetch("/api/clone/inbox/list?limit=3"),
        fetch("/api/clone/clones"),
      ]);

      if (overviewRes.status === "fulfilled" && overviewRes.value.ok) {
        setOverview(await overviewRes.value.json());
      }
      if (inboxRes.status === "fulfilled" && inboxRes.value.ok) {
        const data = await inboxRes.value.json();
        setRecentInbox(Array.isArray(data) ? data : data.items ?? []);
      }
      if (clonesRes.status === "fulfilled" && clonesRes.value.ok) {
        const data = await clonesRes.value.json();
        const clones = Array.isArray(data) ? data : data.clones ?? [];
        setClonesCount(clones.length);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error loading data");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const usageBars = useMemo(() => {
    const conversations = overview?.total_conversations ?? 0;
    const questions = overview?.questions_answered ?? 0;
    const gaps = overview?.gaps_count ?? 0;
    if (conversations === 0 && questions === 0 && gaps === 0) return fallbackBars;
    return fallbackBars.map((bar, index) => {
      const pulse = index % 3 === 0 ? conversations : index % 3 === 1 ? questions : gaps;
      return Math.max(10, Math.min(64, bar + pulse * 3));
    });
  }, [overview]);

  if (status === "loading" || loading) {
    return <LoadingState label="Loading dashboard..." rows={4} />;
  }

  if (error) {
    return (
      <ErrorState
        message={error}
        action={
          <button type="button" onClick={fetchData} className="btn-secondary text-xs">
            Try again
          </button>
        }
      />
    );
  }

  return (
    <div className="mx-auto max-w-[1440px]">
      <header className="mb-7 flex items-start justify-between gap-4">
        <div>
          <h1 className="text-[28px] font-semibold leading-tight tracking-[-0.01em] text-[var(--text-primary)]">
            MyOwnClone Command Center
          </h1>
          <p className="mt-2 text-sm text-[var(--text-muted)]">
            Train your AI clone, manage its knowledge, review conversations, and monitor growth from one focused workspace.
          </p>
        </div>
        <div className="hidden h-9 w-9 shrink-0 overflow-hidden rounded-full border border-[var(--border-soft)] bg-[var(--surface-2)] md:block">
          {session?.user?.image ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img src={session.user.image} alt="" className="h-full w-full object-cover" />
          ) : (
            <div className="flex h-full w-full items-center justify-center text-xs font-semibold text-[var(--text-primary)]">
              {session?.user?.name?.charAt(0) ?? "U"}
            </div>
          )}
        </div>
      </header>

      {clonesCount !== null && clonesCount === 0 && (
        <OnboardingBanner completedSteps={1} totalSteps={4} />
      )}

      <section className="mb-7">
        <p className="section-label mb-3">Get Started</p>
        <div className="grid grid-cols-1 gap-3 lg:grid-cols-[1.2fr_1fr_1fr]">
          <Link href="/configuracion" className="console-strip">
            <div className="console-icon text-[#0EA5E9]">
              <Key weight="duotone" />
            </div>
            <div className="min-w-0">
              <p className="text-sm font-medium text-[var(--text-primary)]">API Key</p>
              <p className="text-xs text-[var(--text-muted)]">Get started in 5 min</p>
            </div>
            <span className="ml-auto truncate font-mono text-sm text-[#0284C7]">
              Manage keys
            </span>
          </Link>

          <Link href="/analiticas" className="console-strip">
            <div className="console-icon text-[#EF4444]">
              <ChartBar weight="duotone" />
            </div>
            <div>
              <p className="text-sm font-medium text-[var(--text-primary)]">Usage</p>
              <p className="text-xs text-[var(--text-muted)]">Past 30 Days</p>
            </div>
            <div className="ml-auto flex h-9 items-end gap-1">
              {usageBars.map((bar, index) => (
                <span
                  key={`${bar}-${index}`}
                  className={index >= 6 && index <= 9 ? "bg-[#22B8CF]" : "bg-[#E7E5E4]"}
                  style={{ height: `${bar}%`, width: 4, borderRadius: 3 }}
                />
              ))}
            </div>
          </Link>

          <div className="grid grid-cols-2 overflow-hidden rounded-xl border border-[var(--border-soft)] bg-white shadow-sm">
            <Link href="/biblioteca" className="console-link">
              <FileDoc className="text-[#2563EB]" weight="duotone" />
              Docs
              <ArrowSquareOut className="ml-auto" />
            </Link>
            <Link href="/cerebro" className="console-link border-l border-[var(--border-soft)]">
              <Globe className="text-[#DC2626]" weight="duotone" />
              Agent Toolkit
              <ArrowSquareOut className="ml-auto" />
            </Link>
          </div>
        </div>
      </section>

      <section className="rounded-2xl border border-[var(--border-soft)] bg-white px-4 py-10 shadow-sm md:px-8 md:py-16">
        <div className="mx-auto flex max-w-[760px] flex-col items-center text-center">
          <div className="mb-6">
            <ReflectiveOrb size={68} />
          </div>
          <h2 className="text-2xl font-semibold text-[var(--text-secondary)] md:text-[28px]">
            What do you want to build or query?
          </h2>

          <form
            className="mt-7 w-full rounded-xl border border-[var(--border-medium)] bg-white p-3 text-left shadow-[0_14px_32px_rgba(15,23,42,0.08)]"
            onSubmit={(event) => {
              event.preventDefault();
              const trimmed = query.trim();
              if (trimmed.length === 0) return;
              router.push(`/biblioteca?query=${encodeURIComponent(trimmed)}`);
            }}
          >
            <textarea
              rows={4}
              aria-label="AI query"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Ask about endpoints, schema design, or workflow orchestration..."
              className="min-h-[92px] w-full resize-none bg-transparent text-sm text-[var(--text-primary)] outline-none placeholder:text-[var(--text-muted)]"
            />
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-1.5">
                <button type="button" className="prompt-tool" aria-label="Search">
                  <MagnifyingGlass />
                </button>
                <button
                  type="button"
                  className="prompt-tool"
                  aria-label="Fast mode"
                  onClick={() => setQuery((current) => current || "Find the fastest way to launch my AI clone workflow.")}
                >
                  <Lightning weight="fill" />
                </button>
                <button
                  type="button"
                  className="prompt-tool"
                  aria-label="Templates"
                  onClick={() => setQuery("Create a workflow that ingests content, answers customer questions, and flags gaps.")}
                >
                  <SquaresFour />
                </button>
              </div>
              <button type="submit" className="prompt-send" aria-label="Send query">
                <PaperPlaneRight />
              </button>
            </div>
          </form>

          <div className="mt-8 w-full text-left">
            <p className="section-label mb-3">Your Recent Query</p>
            {recentInbox.length === 0 ? (
              <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
                {[
                  "Extract product data from nike.com Schema: title, price, availability, reviews",
                  "Create extraction schema for blog articles Fields: headline, author, publish_date, content",
                  "Research latest AI compliance regulations Region: EU Output: structured summary",
                ].map((query) => (
                  <RecentQueryCard key={query} query={query} onSelect={setQuery} />
                ))}
              </div>
            ) : (
              <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
                {recentInbox.slice(0, 3).map((item) => (
                  <RecentQueryCard
                    key={item.id}
                    query={`${item.subject ?? "Inbox request"} ${item.from_email ? `from ${item.from_email}` : ""}`}
                    onSelect={setQuery}
                  />
                ))}
              </div>
            )}
          </div>

          {overview === null && (
            <div className="mt-8 w-full">
              <EmptyState
                title="No analytics yet"
                description="When your clone starts receiving activity, this dashboard will update automatically."
              />
            </div>
          )}
        </div>
      </section>
    </div>
  );
}

function RecentQueryCard({
  query,
  onSelect,
}: {
  query: string;
  onSelect: (query: string) => void;
}) {
  return (
    <button
      type="button"
      onClick={() => onSelect(query)}
      className="rounded-xl border border-[var(--border-soft)] bg-white p-4 text-left text-sm leading-snug text-[var(--text-secondary)] shadow-sm transition hover:border-[var(--border-medium)] hover:text-[var(--text-primary)]"
    >
      <MagnifyingGlass className="mb-4 h-4 w-4 text-[var(--text-muted)]" />
      {query}
    </button>
  );
}
