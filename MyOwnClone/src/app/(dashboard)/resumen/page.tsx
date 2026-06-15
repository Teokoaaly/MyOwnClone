"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { useSession } from "next-auth/react";
import { AnimatePresence, motion } from "framer-motion";
import {
  ChartBar,
  FileDoc,
  Globe,
  Key,
  Lightning,
  MagnifyingGlass,
  PaperPlaneRight,
  SquaresFour,
  Envelope,
  CalendarCheck,
  Brain,
  ShoppingBag,
  ChartLine,
  Gear,
  CreditCard,
} from "@phosphor-icons/react";
import { EmptyState } from "@/components/ui/EmptyState";
import { ErrorState } from "@/components/ui/ErrorState";
import { LoadingState } from "@/components/ui/LoadingState";
import { OnboardingBanner } from "@/components/dashboard/OnboardingBanner";
import { ChatPanel } from "@/components/chat/ChatPanel";
import ReflectiveOrb from "@/components/ui/ReflectiveOrb";
import { useRouter } from "@/i18n/navigation";
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

type Section = "clone" | "inbox" | "analytics" | "settings";

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
  const [activeSection, setActiveSection] = useState<Section>("clone");

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
        fetch("/api/clone/inbox/list?limit=5"),
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

  const tabs: { key: Section; label: string; icon: React.ReactNode }[] = [
    { key: "clone", label: "Clone", icon: <Brain /> },
    { key: "inbox", label: "Inbox", icon: <Envelope /> },
    { key: "analytics", label: "Analytics", icon: <ChartLine /> },
    { key: "settings", label: "Settings", icon: <Gear /> },
  ];

  const stats = [
    { label: "Conversations", value: overview?.total_conversations ?? 0, icon: <Brain /> },
    { label: "Messages", value: overview?.total_messages ?? 0, icon: <Envelope /> },
    { label: "Answered", value: overview?.questions_answered ?? 0, icon: <CalendarCheck /> },
    { label: "Gaps", value: overview?.gaps_count ?? 0, icon: <ChartBar /> },
  ];

  if (status === "loading" || loading) {
    return <LoadingState label="Loading..." rows={3} />;
  }

  if (error) {
    return (
      <ErrorState
        message={error}
        action={
          <button type="button" onClick={fetchData} className="text-sm text-[var(--color-accent-violet)] hover:underline">
            Try again
          </button>
        }
      />
    );
  }

  return (
    <div className="flex flex-col gap-8">
      {/* Hero — no box */}
      <header className="flex flex-col items-center text-center pt-4">
        <ReflectiveOrb size={44} />
        <h1 className="mt-3 text-[28px] font-semibold leading-tight tracking-[-0.01em] text-[var(--text-primary)]">
          MyOwnClone
        </h1>
        <p className="mt-2 max-w-lg text-sm text-[var(--text-muted)]">
          Train your AI clone, manage knowledge, review conversations, and monitor growth — all in one place.
        </p>
      </header>

      {clones.length === 0 && (
        <OnboardingBanner completedSteps={1} totalSteps={4} />
      )}

      {/* Stats — flat row, no cards */}
      {overview && (
        <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
          {stats.map((stat) => (
            <div key={stat.label} className="flex items-center gap-3 py-2">
              <span className="text-[var(--text-muted)]">{stat.icon}</span>
              <div>
                <p className="text-2xl font-semibold text-[var(--text-primary)]">{stat.value}</p>
                <p className="text-xs text-[var(--text-muted)]">{stat.label}</p>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Dynamic Tabs — no box, just underline */}
      <nav className="flex gap-6 border-b border-[var(--border-soft)]">
        {tabs.map((tab) => (
          <button
            key={tab.key}
            type="button"
            onClick={() => setActiveSection(tab.key)}
            className={`flex items-center gap-2 pb-2.5 text-sm transition ${
              activeSection === tab.key
                ? "border-b-2 border-[var(--color-accent-violet)] text-[var(--color-accent-violet)] font-medium"
                : "text-[var(--text-muted)] hover:text-[var(--text-primary)]"
            }`}
          >
            {tab.icon}
            {tab.label}
          </button>
        ))}
      </nav>

      {/* Content sections — flat, no boxes */}
      <AnimatePresence mode="wait">
        {activeSection === "clone" && (
          <motion.section
            key="clone"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.2 }}
            className="flex flex-col gap-6"
          >
            {/* Chat input — clean, no box */}
            <div className="flex flex-col items-center">
              {activeClone?.slug && chatSessionKey > 0 ? (
                <div className="w-full max-w-[860px]">
                  <ChatPanel
                    key={`${activeClone.slug}-${chatSessionKey}`}
                    slug={activeClone.slug}
                    initialSilo="teach"
                    initialQuery={chatSessionKey > 0 ? activeChatQuery : undefined}
                    mode="inline"
                    emptyState={{
                      title: `Ask ${activeClone.name}`,
                      description: "Your clone answers from its knowledge base.",
                    }}
                    onReset={() => {
                      setActiveChatQuery("");
                      setChatSessionKey(0);
                    }}
                  />
                </div>
              ) : (
                <form
                  className="w-full max-w-[860px]"
                  onSubmit={(event) => {
                    event.preventDefault();
                    startInlineChat();
                  }}
                >
                  <div className="flex items-end gap-3">
                    <textarea
                      rows={2}
                      aria-label="AI query"
                      value={activeChatQuery}
                      onChange={(event) => setActiveChatQuery(event.target.value)}
                      placeholder="Ask your clone something..."
                      className="min-h-[48px] w-full resize-none border-b border-[var(--border-soft)] bg-transparent pb-2 text-sm text-[var(--text-primary)] outline-none placeholder:text-[var(--text-muted)] focus:border-[var(--color-accent-violet)]"
                    />
                    <button
                      type="submit"
                      className="flex h-10 w-10 items-center justify-center rounded-full bg-[var(--color-accent-violet)] text-white transition hover:opacity-90"
                      aria-label="Send"
                    >
                      <PaperPlaneRight weight="fill" />
                    </button>
                  </div>
                  <div className="mt-3 flex gap-2">
                    {["Extract product data", "Research AI compliance", "Create blog extractor"].map((q) => (
                      <button
                        key={q}
                        type="button"
                        onClick={() => setActiveChatQuery(q)}
                        className="text-xs text-[var(--text-muted)] hover:text-[var(--text-primary)] transition"
                      >
                        {q}
                      </button>
                    ))}
                  </div>
                </form>
              )}
            </div>

            {/* Quick links */}
            <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
              {[
                { label: "API Keys", icon: <Key />, href: "/configuracion" },
                { label: "Library", icon: <FileDoc />, href: "/biblioteca" },
                { label: "Crawl", icon: <Globe />, href: "/cerebro" },
                { label: "Products", icon: <ShoppingBag />, href: "/productos" },
              ].map((link) => (
                <a
                  key={link.label}
                  href={link.href}
                  className="flex items-center gap-2.5 py-2.5 px-1 text-sm text-[var(--text-secondary)] hover:text-[var(--color-accent-violet)] transition"
                >
                  <span className="text-[var(--text-muted)]">{link.icon}</span>
                  {link.label}
                </a>
              ))}
            </div>
          </motion.section>
        )}

        {activeSection === "inbox" && (
          <motion.section
            key="inbox"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.2 }}
            className="flex flex-col gap-3"
          >
            {recentInbox.length === 0 ? (
              <EmptyState title="No inbox items" description="Emails sent to your clone will appear here." />
            ) : (
              recentInbox.map((item) => (
                <div key={item.id} className="flex items-start gap-3 py-3 border-b border-[var(--border-soft)]">
                  <Envelope className="mt-0.5 text-[var(--text-muted)]" />
                  <div className="min-w-0 flex-1">
                    <p className="text-sm font-medium text-[var(--text-primary)] truncate">
                      {item.subject || "(no subject)"}
                    </p>
                    <p className="text-xs text-[var(--text-muted)]">{item.from_email} &middot; {item.status}</p>
                  </div>
                </div>
              ))
            )}
          </motion.section>
        )}

        {activeSection === "analytics" && (
          <motion.section
            key="analytics"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.2 }}
          >
            {overview ? (
              <div className="flex flex-col gap-6">
                <div className="flex items-end gap-1 h-40">
                  {usageBars.map((bar, index) => (
                    <span
                      key={index}
                      className="flex-1 bg-[var(--color-accent-violet)] rounded-t"
                      style={{ height: `${bar}%`, opacity: 0.3 + (bar / 100) * 0.7 }}
                    />
                  ))}
                </div>
                <div className="grid grid-cols-3 gap-4 text-center">
                  <div>
                    <p className="text-xs text-[var(--text-muted)]">Automation Rate</p>
                    <p className="text-lg font-semibold text-[var(--text-primary)]">
                      {overview.automation_rate ?? "--"}%
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-[var(--text-muted)]">Active Sessions</p>
                    <p className="text-lg font-semibold text-[var(--text-primary)]">
                      {overview.active_sessions ?? "--"}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-[var(--text-muted)]">Clones</p>
                    <p className="text-lg font-semibold text-[var(--text-primary)]">
                      {overview.clones_count ?? clones.length}
                    </p>
                  </div>
                </div>
              </div>
            ) : (
              <EmptyState title="No analytics yet" description="Activity will appear here once your clone starts receiving traffic." />
            )}
          </motion.section>
        )}

        {activeSection === "settings" && (
          <motion.section
            key="settings"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.2 }}
            className="flex flex-col gap-4"
          >
            {[
              { label: "API Keys", href: "/configuracion", icon: <Key /> },
              { label: "Billing", href: "/facturacion", icon: <CreditCard /> },
              { label: "Team Settings", href: "/reuniones", icon: <Gear /> },
              { label: "Usage", href: "/analiticas", icon: <ChartLine /> },
            ].map((item) => (
              <a
                key={item.label}
                href={item.href}
                className="flex items-center gap-3 py-3 border-b border-[var(--border-soft)] text-sm text-[var(--text-secondary)] hover:text-[var(--color-accent-violet)] transition"
              >
                <span className="text-[var(--text-muted)]">{item.icon}</span>
                {item.label}
              </a>
            ))}
          </motion.section>
        )}
      </AnimatePresence>
    </div>
  );
}
