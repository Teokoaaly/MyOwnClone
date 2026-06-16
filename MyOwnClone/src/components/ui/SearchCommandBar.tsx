"use client";

import {
  type FC,
  type ReactNode,
  useCallback,
  useEffect,
  useId,
  useMemo,
  useRef,
  useState,
} from "react";
import { Link, useRouter } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

/**
 * Cmd-K style command palette. Searches across:
 *   1. The static dashboard nav (always available, instant).
 *   2. The user's clones, memories, products and meeting types via
 *      the existing /api/clone/* endpoints.
 *
 * Keyboard:
 *   - Cmd+K (macOS) / Ctrl+K (others): open.
 *   - ↑ / ↓: move selection.
 *   - Enter: navigate to the selected result (or run the first
 *     result if there is no selection yet).
 *   - Esc: close.
 *   - The dialog implements a focus trap identical to the global
 *     Modal (Tab/Shift+Tab cycle, focus restore on close).
 */

type StaticKind = "page";

type DynamicKind = "clone" | "memory" | "product" | "meeting";

type ResultKind = StaticKind | DynamicKind;

interface BaseResult {
  id: string;
  title: string;
  subtitle?: string;
  kind: ResultKind;
  href: string;
  icon: string; // emoji or short label, displayed as decorative
}

interface SearchCommandBarProps {
  /** Static nav entries shown above dynamic results. */
  pages: Array<{ href: string; label: string; icon: string }>;
}

const KIND_LABEL: Record<ResultKind, string> = {
  page: "Pages",
  clone: "Clones",
  memory: "Memories",
  product: "Products",
  meeting: "Meetings",
};

const FOCUSABLE_SELECTOR =
  'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

function asArray<T = unknown>(v: unknown): T[] {
  if (Array.isArray(v)) return v as T[];
  if (v && typeof v === "object" && Array.isArray((v as { items?: unknown }).items)) {
    return (v as { items: T[] }).items;
  }
  return [];
}

function score(haystack: string, needle: string): number {
  if (!needle) return 1;
  const h = haystack.toLowerCase();
  const n = needle.toLowerCase();
  if (h === n) return 1000;
  if (h.startsWith(n)) return 500;
  const idx = h.indexOf(n);
  if (idx === -1) return 0;
  return 100 - idx;
}

export const SearchCommandBar: FC<SearchCommandBarProps> = ({ pages }) => {
  const t = useTranslations("search");
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [activeIdx, setActiveIdx] = useState(0);
  const [loading, setLoading] = useState(false);
  const [clones, setClones] = useState<Array<{ id: string; name: string; slug: string }>>([]);
  const [memories, setMemories] = useState<Array<{ id: string; content: string; type: string }>>([]);
  const [products, setProducts] = useState<Array<{ id: string; name: string; description?: string | null }>>([]);
  const [meetings, setMeetings] = useState<Array<{ id: string; name: string; duration_minutes: number }>>([]);

  const inputRef = useRef<HTMLInputElement | null>(null);
  const listRef = useRef<HTMLUListElement | null>(null);
  const dialogRef = useRef<HTMLDivElement | null>(null);
  const titleId = useId();
  const previouslyFocusedRef = useRef<HTMLElement | null>(null);

  const close = useCallback(() => {
    setOpen(false);
    setQuery("");
    setActiveIdx(0);
  }, []);

  // Build static results.
  const staticResults: BaseResult[] = useMemo(
    () =>
      pages.map((p) => ({
        id: `page:${p.href}`,
        title: p.label,
        kind: "page" as const,
        href: p.href,
        icon: p.icon,
      })),
    [pages],
  );

  // Build dynamic results from the four resources.
  const dynamicResults: BaseResult[] = useMemo(() => {
    const out: BaseResult[] = [];
    for (const c of clones) {
      out.push({
        id: `clone:${c.id}`,
        title: c.name,
        subtitle: c.slug,
        kind: "clone",
        href: `/resumen?clone=${c.slug}`,
        icon: "🧬",
      });
    }
    for (const m of memories) {
      const trimmed = m.content.length > 60 ? `${m.content.slice(0, 60)}…` : m.content;
      out.push({
        id: `memory:${m.id}`,
        title: trimmed,
        subtitle: m.type,
        kind: "memory",
        href: "/cerebro",
        icon: "🧠",
      });
    }
    for (const p of products) {
      out.push({
        id: `product:${p.id}`,
        title: p.name,
        subtitle: p.description ?? undefined,
        kind: "product",
        href: "/productos",
        icon: "📦",
      });
    }
    for (const mt of meetings) {
      out.push({
        id: `meeting:${mt.id}`,
        title: mt.name,
        subtitle: `${mt.duration_minutes} min`,
        kind: "meeting",
        href: "/reuniones",
        icon: "📅",
      });
    }
    return out;
  }, [clones, memories, products, meetings]);

  // Filter and group results by query.
  const grouped = useMemo(() => {
    const all: Array<BaseResult & { _score: number }> = [...staticResults, ...dynamicResults].map(
      (r) => ({
        ...r,
        _score: Math.max(
          score(r.title, query),
          r.subtitle ? score(r.subtitle, query) : 0,
        ),
      }),
    );
    const filtered = all
      .filter((r) => r._score > 0)
      .sort((a, b) => b._score - a._score)
      .slice(0, 20);

    const groups: Array<{ kind: ResultKind; items: BaseResult[] }> = [];
    const byKind = new Map<ResultKind, BaseResult[]>();
    for (const r of filtered) {
      const arr = byKind.get(r.kind) ?? [];
      arr.push(r);
      byKind.set(r.kind, arr);
    }
    // Stable group order matching KIND_LABEL keys.
    (Object.keys(KIND_LABEL) as ResultKind[]).forEach((k) => {
      const arr = byKind.get(k);
      if (arr && arr.length > 0) groups.push({ kind: k, items: arr });
    });
    return groups;
  }, [staticResults, dynamicResults, query]);

  // Flatten for keyboard nav.
  const flat = useMemo(() => grouped.flatMap((g) => g.items), [grouped]);

  // Reset selection when the result list changes.
  useEffect(() => {
    setActiveIdx(0);
  }, [query, open]);

  // Open via ⌘K / Ctrl+K from anywhere on the page.
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setOpen((o) => !o);
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, []);

  // Fetch dynamic data when the dialog opens (cheap: a single round
  // of parallel GETs, cached in state for the session).
  useEffect(() => {
    if (!open || clones.length > 0) return;
    let cancelled = false;
    setLoading(true);
    (async () => {
      try {
        const [cRes, mRes, productsRes, meetingsRes] = await Promise.allSettled([
          fetch("/api/clone/clones").then((r) => (r.ok ? r.json() : [])),
          fetch("/api/clone/memories?type=memory").then((r) => (r.ok ? r.json() : [])),
          fetch("/api/clone/clones").then(async (r) => {
            if (!r.ok) return [];
            const arr = asArray<{ id: string }>(await r.json());
            if (arr.length === 0) return [];
            return fetch(`/api/clone/clones/${arr[0].id}/products`).then((r) =>
              r.ok ? r.json() : [],
            );
          }),
          fetch("/api/clone/clones").then(async (r) => {
            if (!r.ok) return [];
            const arr = asArray<{ id: string }>(await r.json());
            if (arr.length === 0) return [];
            return fetch(`/api/clone/clones/${arr[0].id}/meeting-types`).then((r) =>
              r.ok ? r.json() : [],
            );
          }),
        ]);
        if (cancelled) return;
        if (cRes.status === "fulfilled") {
          setClones(asArray<{ id: string; name: string; slug: string }>(cRes.value));
        }
        if (mRes.status === "fulfilled") {
          setMemories(asArray<{ id: string; content: string; type: string }>(mRes.value));
        }
        if (productsRes.status === "fulfilled") {
          setProducts(
            asArray<{ id: string; name: string; description?: string | null }>(productsRes.value),
          );
        }
        if (meetingsRes.status === "fulfilled") {
          setMeetings(
            asArray<{ id: string; name: string; duration_minutes: number }>(meetingsRes.value),
          );
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [open, clones.length]);

  // Focus trap + keydown handler for the dialog (same pattern as
  // the global Modal component).
  useEffect(() => {
    if (!open) return;
    previouslyFocusedRef.current =
      document.activeElement instanceof HTMLElement ? document.activeElement : null;
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.stopPropagation();
        close();
        return;
      }
      if (e.key === "ArrowDown") {
        e.preventDefault();
        if (flat.length > 0) setActiveIdx((i) => (i + 1) % flat.length);
        return;
      }
      if (e.key === "ArrowUp") {
        e.preventDefault();
        if (flat.length > 0) setActiveIdx((i) => (i - 1 + flat.length) % flat.length);
        return;
      }
      if (e.key === "Enter") {
        const target = flat[activeIdx] ?? flat[0];
        if (target) {
          e.preventDefault();
          close();
          router.push(target.href);
        }
        return;
      }
      if (e.key !== "Tab" || !dialogRef.current) return;
      const focusables = Array.from(
        dialogRef.current.querySelectorAll<HTMLElement>(FOCUSABLE_SELECTOR),
      ).filter((el) => !el.hasAttribute("disabled") && el.tabIndex !== -1);
      if (focusables.length === 0) {
        e.preventDefault();
        return;
      }
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      const active = document.activeElement as HTMLElement | null;
      if (e.shiftKey && active === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && active === last) {
        e.preventDefault();
        first.focus();
      }
    };
    window.addEventListener("keydown", handler, true);
    queueMicrotask(() => inputRef.current?.focus());
    return () => {
      window.removeEventListener("keydown", handler, true);
      const previous = previouslyFocusedRef.current;
      if (previous && document.body.contains(previous)) previous.focus();
    };
  }, [open, flat, activeIdx, close, router]);

  // Scroll the active item into view when it changes.
  useEffect(() => {
    const el = listRef.current?.querySelector<HTMLLIElement>(
      `[data-result-idx="${activeIdx}"]`,
    );
    el?.scrollIntoView({ block: "nearest" });
  }, [activeIdx]);

  if (!open) {
    // Still render a trigger button so users without a keyboard can
    // discover the feature. The dialog itself stays unmounted.
    return <SearchTrigger onOpen={() => setOpen(true)} t={t} />;
  }

  let runningIdx = -1;
  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-[10vh] p-4">
      <div
        className="absolute inset-0 bg-black/30 backdrop-blur-sm"
        onClick={close}
        aria-hidden="true"
      />
      <div
        ref={dialogRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        tabIndex={-1}
        className="relative w-full max-w-xl overflow-hidden rounded-2xl border border-[var(--border-soft)] bg-[var(--bg-shell)] shadow-[0_24px_64px_rgba(15,23,42,0.18)] outline-none"
      >
        <h2 id={titleId} className="sr-only">
          Search
        </h2>
        <div className="flex items-center gap-2 border-b border-[var(--border-soft)] px-4 py-3">
          <span aria-hidden="true" className="text-[var(--text-muted)]">🔍</span>
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search pages, clones, memories, products, meetings..."
            aria-label="Search"
            aria-controls="cmdk-results"
            aria-activedescendant={
              flat[activeIdx] ? `cmdk-result-${activeIdx}` : undefined
            }
            className="flex-1 bg-transparent text-sm text-[var(--text-primary)] placeholder:text-[var(--text-muted)] focus:outline-none"
          />
          <kbd className="hidden sm:inline-block rounded border border-[var(--border-soft)] px-1.5 py-0.5 font-mono text-[10px] text-[var(--text-muted)]">
            Esc
          </kbd>
        </div>
        <ul
          id="cmdk-results"
          ref={listRef}
          role="listbox"
          className="max-h-[60vh] overflow-y-auto p-2"
        >
          {flat.length === 0 ? (
            <li className="px-3 py-8 text-center text-sm text-[var(--text-muted)]">
              {loading
                ? "Loading..."
                : query
                ? `No results for "${query}"`
                : "Start typing to search."}
            </li>
          ) : (
            grouped.map((g) => {
              return (
                <li key={g.kind} role="presentation">
                  <div className="section-label px-2 pt-2 pb-1">
                    {KIND_LABEL[g.kind]}
                  </div>
                  <ul role="group">
                    {g.items.map((r) => {
                      runningIdx += 1;
                      const idx = runningIdx;
                      const isActive = idx === activeIdx;
                      return (
                        <li
                          key={r.id}
                          id={`cmdk-result-${idx}`}
                          data-result-idx={idx}
                          role="option"
                          aria-selected={isActive}
                          onMouseEnter={() => setActiveIdx(idx)}
                          className={[
                            "flex items-center gap-3 rounded-md px-2 py-2 cursor-pointer",
                            isActive
                              ? "bg-[var(--surface-2)]"
                              : "hover:bg-[var(--surface-2)]",
                          ].join(" ")}
                        >
                          <Link
                            href={r.href}
                            onClick={(e) => {
                              // The default <Link> navigation will fire.
                              // We also close the dialog so the next
                              // paint shows the new page.
                              e.preventDefault();
                              close();
                              router.push(r.href);
                            }}
                            className="flex flex-1 items-center gap-3 min-w-0"
                          >
                            <span aria-hidden="true" className="shrink-0 text-base">
                              {r.icon}
                            </span>
                            <div className="min-w-0 flex-1">
                              <p className="truncate text-sm text-[var(--text-primary)]">
                                {r.title}
                              </p>
                              {r.subtitle && (
                                <p className="truncate text-xs text-[var(--text-muted)]">
                                  {r.subtitle}
                                </p>
                              )}
                            </div>
                            {isActive && (
                              <span className="hidden sm:inline-block font-mono text-[10px] text-[var(--text-muted)]">
                                ↵
                              </span>
                            )}
                          </Link>
                        </li>
                      );
                    })}
                  </ul>
                </li>
              );
            })
          )}
        </ul>
        <div className="flex items-center justify-between border-t border-[var(--border-soft)] px-4 py-2 text-[10px] text-[var(--text-muted)]">
          <div className="flex items-center gap-3">
            <span>
              <kbd className="font-mono">↑</kbd>{" "}
              <kbd className="font-mono">↓</kbd> to navigate
            </span>
            <span>
              <kbd className="font-mono">↵</kbd> to open
            </span>
            <span>
              <kbd className="font-mono">Esc</kbd> to close
            </span>
          </div>
          <span>
            <kbd className="font-mono">⌘K</kbd> from anywhere
          </span>
        </div>
      </div>
    </div>
  );
};

/**
 * Small button that lives in the topbar and opens the command bar.
 * Always rendered (the parent component decides when to mount the
 * dialog, which is on the user gesture).
 */
const SearchTrigger: FC<{ onOpen: () => void; t: (k: string) => string }> = ({ onOpen, t }) => (
  <button
    type="button"
    onClick={onOpen}
    aria-label={t("search.openSearch")}
    className="flex items-center gap-2 rounded-md border border-[var(--border-soft)] bg-[var(--surface-1)] px-3 py-1.5 text-xs text-[var(--text-muted)] hover:bg-[var(--surface-2)] hover:text-[var(--text-secondary)] transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]"
  >
    <span aria-hidden="true">🔍</span>
    <span className="hidden sm:inline">{t("search.search")}</span>
    <kbd className="hidden sm:inline-block rounded border border-[var(--border-soft)] px-1 py-0.5 font-mono text-[10px]">
      ⌘K
    </kbd>
  </button>
);

/**
 * Tiny presentational wrapper for the empty/no-results message.
 * Kept as a typed element so the parent does not have to import
 * `ReactNode` separately.
 */
export type { ReactNode };
