"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { useSession } from "next-auth/react";
import { AnimatePresence, motion } from "framer-motion";
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
import { ChatPanel } from "@/components/chat/ChatPanel";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link, useRouter } from "@/i18n/navigation";
import { setCloneIdCookie } from "@/lib/clone-resolver";

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

interface CloneListItem {
  id: string;
  slug: string;
  name: string;
}

const fallbackBars = [14, 18, 22, 16, 28, 36, 54, 48, 60, 42, 30, 26, 18, 22, 34, 28, 20, 18, 24, 16];
const COLLAPSED_BOX_HEIGHT = 188;
const ACTIVE_CHAT_BOX_HEIGHT = 420;

export default function DashboardResumenPage() {
  const { status } = useSession();
  const router = useRouter();
  const [overview, setOverview] = useState<AnalyticsOverview | null>(null);
  const [recentInbox, setRecentInbox] = useState<InboxListItem[]>([]);
  const [clones, setClones] = useState<CloneListItem[]>([]);
  const [activeChatQuery, setActiveChatQuery] = useState("");
  const [chatSessionKey, setChatSessionKey] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login");
  }, [status, router]);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const clonesRes = await fetch("/api/clone/clones");
      const cloneData = clonesRes.ok ? await clonesRes.json() : [];
      const resolvedClones = Array.isArray(cloneData) ? cloneData : cloneData.clones ?? [];
      setClones(resolvedClones);

      if (resolvedClones[0]?.id) {
        setCloneIdCookie(resolvedClones[0].id);
      }

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
      setError(e instanceof Error ? e.message : "Error loading data");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const activeClone = clones[0] ?? null;

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

  const startInlineChat = useCallback(() => {
    const trimmed = activeChatQuery.trim();
    if (trimmed.length === 0) return;
    if (!activeClone?.slug) {
      router.push("/onboarding");
      return;
    }

    setChatSessionKey((current) => current + 1);
  }, [activeChatQuery, activeClone?.slug, router]);

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
    <div className="mx-auto flex max-w-[1440px] flex-col">
      <header className="mb-5 shrink-0">
        <div>
          <h1 className="text-[28px] font-semibold leading-tight tracking-[-0.01em] text-[var(--text-primary)]">
            MyOwnClone Command Center
          </h1>
          <p className="mt-2 text-sm text-[var(--text-muted)]">
            Train your AI clone, manage its knowledge, review conversations, and monitor growth from one focused workspace.
          </p>
        </div>
      </header>

      {clones.length === 0 && (
        <OnboardingBanner completedSteps={1} totalSteps={4} />
      )}

      <section className="mb-5 shrink-0">
        <p className="section-label mb-3">Get Started</p>
        <div className="grid grid-cols-1 gap-3 lg:grid-cols-[1.2fr_1fr_1fr]">
          <Link href="/configuracion" className="console-strip">
            <div className="console-icon text-[#0EA5E9]">
              <Key weight="duotone" />
            </div>
            <div className="min-w-0">
              <p className="text-sm font-medium text-[var(--text-primary)]">API Keys</p>
              <p className="text-xs text-[var(--text-muted)]">Connect your workspace in 5 min</p>
            </div>
            <span className="ml-auto truncate font-mono text-sm text-[#0284C7]">
              Open keys
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

      <section className="rounded-2xl border border-[var(--border-soft)] bg-white px-4 py-5 shadow-sm md:px-8 md:py-6">
        <div className="mx-auto flex max-w-[980px] flex-col overflow-visible pb-3">
          <div className="flex flex-col items-center text-center">
            <AnimatedLogoMark size={40} />
            <h2 className="mt-2 text-[26px] font-semibold text-[var(--text-secondary)] md:text-[28px]">
              What do you want to build or query?
            </h2>
          </div>

          <motion.div
            animate={{ height: chatSessionKey > 0 ? ACTIVE_CHAT_BOX_HEIGHT : COLLAPSED_BOX_HEIGHT }}
            transition={{ duration: 0.42, ease: [0.22, 1, 0.36, 1] }}
            className="mx-auto mt-4 w-full max-w-[860px] overflow-hidden rounded-2xl border border-[var(--border-medium)] bg-white text-left shadow-[0_14px_32px_rgba(15,23,42,0.08)]"
          >
            {activeClone?.slug && chatSessionKey > 0 ? (
              <ChatPanel
                key={`${activeClone.slug}-${chatSessionKey}`}
                slug={activeClone.slug}
                initialSilo="teach"
                initialQuery={chatSessionKey > 0 ? activeChatQuery : undefined}
                mode="inline"
                emptyState={{
                  title: `Consulta ${activeClone.name} desde aqui`,
                  description: "La conversacion permanece en este mismo espacio y usa la base de conocimiento de tu clon.",
                }}
                onReset={() => {
                  setActiveChatQuery("");
                  setChatSessionKey(0);
                }}
              />
            ) : (
              <form
                className="flex h-full flex-col p-3 md:p-4"
                onSubmit={(event) => {
                  event.preventDefault();
                  startInlineChat();
                }}
              >
                <textarea
                  rows={2}
                  aria-label="AI query"
                  value={activeChatQuery}
                  onChange={(event) => setActiveChatQuery(event.target.value)}
                  placeholder="Ask your clone something from its knowledge base..."
                  className="min-h-[40px] w-full resize-none bg-transparent text-sm text-[var(--text-primary)] outline-none placeholder:text-[var(--text-muted)]"
                />
                <div className="mt-auto flex items-center justify-between pt-1.5">
                  <div className="flex items-center gap-1.5">
                    <button type="button" className="prompt-tool" aria-label="Search">
                      <MagnifyingGlass />
                    </button>
                    <button
                      type="button"
                      className="prompt-tool"
                      aria-label="Fast mode"
                      onClick={() => setActiveChatQuery((current) => current || "Find the fastest way to launch my AI clone workflow.")}
                    >
                      <Lightning weight="fill" />
                    </button>
                    <button
                      type="button"
                      className="prompt-tool"
                      aria-label="Templates"
                      onClick={() => setActiveChatQuery("Create a workflow that ingests content, answers customer questions, and flags gaps.")}
                    >
                      <SquaresFour />
                    </button>
                  </div>
                  <button type="submit" className="prompt-send" aria-label="Send query">
                    <PaperPlaneRight />
                  </button>
                </div>
              </form>
            )}
          </motion.div>

          <AnimatePresence initial={false}>
            {chatSessionKey === 0 ? (
              <motion.div
                key="recent-queries"
                initial={{ opacity: 0, y: 18, height: 0, marginTop: 0 }}
                animate={{ opacity: 1, y: 0, height: "auto", marginTop: 14 }}
                exit={{ opacity: 0, y: 10, height: 0, marginTop: 0 }}
                transition={{ duration: 0.42, ease: [0.22, 1, 0.36, 1] }}
                className="w-full overflow-hidden"
              >
                <div className="mx-auto flex max-w-[980px] flex-col">
                {activeClone && (
                  <p className="mb-2 text-xs text-[var(--text-muted)]">
                    Queries will run against <span className="font-medium text-[var(--text-primary)]">{activeClone.name}</span>.
                  </p>
                )}
                <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-[var(--text-muted)]">
                  Your Recent Query
                </p>
                {recentInbox.length === 0 ? (
                  <div className="grid grid-cols-1 gap-2.5 md:grid-cols-3">
                    {[
                      "Extract product data from nike.com Schema: title, price, availability, reviews",
                      "Create extraction schema for blog articles Fields: headline, author, publish_date, content",
                      "Research latest AI compliance regulations Region: EU Output: structured summary",
                    ].map((query) => (
                      <RecentQueryCard key={query} query={query} onSelect={setActiveChatQuery} />
                    ))}
                  </div>
                ) : (
                  <div className="grid grid-cols-1 gap-2.5 md:grid-cols-3">
                    {recentInbox.slice(0, 3).map((item) => (
                      <RecentQueryCard
                        key={item.id}
                        query={`${item.subject ?? "Inbox request"} ${item.from_email ? `from ${item.from_email}` : ""}`}
                        onSelect={setActiveChatQuery}
                      />
                    ))}
                  </div>
                )}
                </div>
              </motion.div>
            ) : null}
          </AnimatePresence>

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
      className="min-h-[92px] rounded-xl border border-[var(--border-soft)] bg-white p-2 text-left text-[13px] leading-snug text-[var(--text-secondary)] shadow-sm transition hover:border-[var(--border-medium)] hover:text-[var(--text-primary)]"
    >
      <MagnifyingGlass className="mb-1.5 h-4 w-4 text-[var(--text-muted)]" />
      <span className="line-clamp-3">{query}</span>
    </button>
  );
}
