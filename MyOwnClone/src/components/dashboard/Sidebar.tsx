"use client";

import { type FC, type ReactNode, useState, useEffect, useCallback } from "react";
import { Sheet } from "@/components/ui/Sheet";
import { NavIcons } from "@/components/ui/dashboard-icons";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link, usePathname } from "@/i18n/navigation";

export type SidebarIconKey = keyof typeof NavIcons;

export interface SidebarNavItem {
  href: string;
  label: string;
  iconKey: SidebarIconKey;
  tooltip: string;
  badge?: string;
  /** Optional grouping. Items without a section render first (Overview). */
  section?: "playground" | "management" | "platform";
}

interface SidebarProps {
  navItems: SidebarNavItem[];
  user?: {
    name?: string | null;
    email?: string | null;
    image?: string | null;
  };
  signOutAction?: ReactNode;
  /** Optional override for the "logo" home link href. Defaults to "/resumen". */
  homeHref?: string;
  /** Optional override for the logo label. */
  homeLabel?: string;
  /** Whether to render the search field. Defaults to true. */
  showSearch?: boolean;
  /** Whether to render the "FREE TRIAL" freemium card. Defaults to false.
   *  TODO: Connect to real tenant.trial_ends_at data from the session. */
  showFreemiumCard?: boolean;
  /** Whether to render the user block at the bottom. Defaults to true. */
  showUserBlock?: boolean;
  /** Optional element rendered below the user block (e.g. a sign-out link). */
  footer?: ReactNode;
}

const SECTION_TITLES: Record<NonNullable<SidebarNavItem["section"]>, string> = {
  playground: "API PLAYGROUND",
  management: "MANAGEMENT",
  platform: "PLATFORM ADMIN",
};

export const Sidebar: FC<SidebarProps> = ({
  navItems,
  user,
  signOutAction,
  homeHref = "/resumen",
  homeLabel = "MyOwnClone",
  showSearch = true,
  showFreemiumCard = false,
  showUserBlock = true,
  footer,
}) => {
  const pathname = usePathname();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [trialDays, setTrialDays] = useState(null);
  const [trialPct, setTrialPct] = useState(50);

  useEffect(function() {
    if (!showFreemiumCard) return;
    fetch("/api/clone/billing", { credentials: "include" })
      .then(function(r) { return r.json(); })
      .then(function(b) {
        if (b.trial_ends_at) {
          const end = new Date(b.trial_ends_at);
          const now = new Date();
          const diff = Math.ceil((end - now) / 86400000);
          const d = Math.max(0, diff);
          setTrialDays(d);
          setTrialPct(Math.min(100, Math.max(0, Math.round((d / 14) * 100))));
        }
      })
      .catch(function() {});
  }, [showFreemiumCard]);

  const initials = user?.name
    ? user.name.charAt(0).toUpperCase()
    : user?.email?.charAt(0).toUpperCase() ?? "U";

  const root = navItems.filter((i) => !i.section);
  const groupedSections = (["playground", "management", "platform"] as const)
    .map((section) => ({
      section,
      items: navItems.filter((i) => i.section === section),
    }))
    .filter((s) => s.items.length > 0);

  const renderItem = (item: SidebarNavItem, closeOnClick = false) => {
    const isActive = pathname?.startsWith(item.href);
    const Icon = NavIcons[item.iconKey];

    return (
      <div key={item.href} className="relative">
        <Link
          href={item.href}
          title={item.tooltip}
          onClick={closeOnClick ? () => setMobileOpen(false) : undefined}
          className={[
            "flex h-10 items-center gap-3 rounded-lg px-3 text-sm transition duration-150",
            isActive ? "nav-item-active" : "nav-item-normal",
          ].join(" ")}
        >
          <Icon
            className={`h-[18px] w-[18px] shrink-0 ${
              isActive ? "text-[var(--color-accent-warm)]" : ""
            }`}
            weight="duotone"
          />
          <span className="truncate">{item.label}</span>
          {item.badge && (
            <span className="ml-auto px-1.5 py-0.5 text-[10px] font-semibold rounded-md bg-[rgba(234,88,12,0.12)] text-[var(--color-accent-warm)] leading-none">
              {item.badge}
            </span>
          )}
        </Link>
      </div>
    );
  };

  const closeMobile = useCallback(() => setMobileOpen(false), []);

  return (
    <>
      {/* ── Hamburger button (mobile only) ── */}
      <button
        type="button"
        aria-label="Open navigation menu"
        onClick={() => setMobileOpen(true)}
        className="md:hidden fixed top-3 left-3 z-30 h-9 w-9 rounded-lg flex items-center justify-center bg-[var(--bg-shell)] border border-[var(--border-soft)] text-[var(--text-primary)] hover:bg-[var(--surface-2)] transition-colors shadow-sm"
      >
        <svg
          className="h-5 w-5"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth={2}
          strokeLinecap="round"
          aria-hidden="true"
        >
          <line x1="4" x2="20" y1="6" y2="6" />
          <line x1="4" x2="20" y1="12" y2="12" />
          <line x1="4" x2="20" y1="18" y2="18" />
        </svg>
      </button>

      {/* ── Mobile sheet ── */}
      <Sheet
        open={mobileOpen}
        onClose={closeMobile}
        title="Main navigation"
        side="left"
        width="280px"
      >
        <div className="flex items-center justify-between px-5 pt-5 pb-4">
          <Link
            href={homeHref}
            onClick={closeMobile}
            className="flex items-center gap-2"
          >
            <AnimatedLogoMark size={26} pulseEveryMs={60000} />
            <span className="text-sm font-semibold tracking-wide text-[var(--text-primary)]">
              {homeLabel}
            </span>
          </Link>
          <DialogCloseButton onClick={closeMobile} />
        </div>

        {/* Search (mobile) */}
        {showSearch && (
          <div className="mx-4 px-3 py-1.5 rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)]">
            <span className="text-xs text-[var(--text-muted)]">Search…</span>
          </div>
        )}

        <nav className="flex-1 overflow-y-auto px-3 py-4">
          {root.length > 0 && (
            <div className="space-y-0.5">
              {root.map((item) => renderItem(item, true))}
            </div>
          )}

          {groupedSections.map((s, idx) => (
            <div
              key={s.section}
              className={
                idx === 0 && root.length === 0
                  ? "space-y-0.5"
                  : "mt-6 space-y-0.5"
              }
            >
              <p className="section-label px-3 mb-2">
                {SECTION_TITLES[s.section]}
              </p>
              {s.items.map((item) => renderItem(item, true))}
            </div>
          ))}
        </nav>

        {/* User block (mobile) */}
        {showUserBlock && user && (
          <div className="px-3 py-3 border-t border-[var(--border-soft)]">
            <div className="flex items-center gap-2.5">
              <div className="h-7 w-7 rounded-full bg-gradient-to-br from-[#F97316] to-[#FB923C] flex items-center justify-center text-white text-xs font-semibold shrink-0">
                {initials}
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-xs font-medium text-[var(--text-primary)] truncate">
                  {user.name ?? "User"}
                </p>
                <p className="text-[10px] text-[var(--text-muted)] truncate">
                  {user.email ?? ""}
                </p>
              </div>
              {signOutAction}
            </div>
          </div>
        )}

        {footer && (
          <div className="border-t border-[var(--border-soft)] px-3 py-3 text-[11px] text-[var(--text-muted)]">
            {footer}
          </div>
        )}
      </Sheet>

      {/* ── Desktop sidebar ── */}
      <aside
        className="hidden md:sticky md:top-0 md:flex md:h-[calc(100vh-4rem)] w-[250px] shrink-0 flex-col border-r border-[var(--border-soft)]"
        style={{ background: "var(--bg-sidebar)" }}
      >
        {/* Logo */}
        <div className="px-5 pt-5 pb-4">
          <Link href={homeHref} className="flex items-center gap-2">
            <AnimatedLogoMark size={26} pulseEveryMs={60000} />
            <span className="text-sm font-semibold tracking-wide text-[var(--text-primary)]">
              {homeLabel}
            </span>
          </Link>
        </div>

        {/* Search */}
        {showSearch && (
          <div className="mx-4 px-3 py-1.5 rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)]">
            <span className="text-xs text-[var(--text-muted)]">Search…</span>
          </div>
        )}

        {/* Nav */}
        <nav className="px-3 py-4">
          {/* Root items (Overview) */}
          {root.length > 0 && (
            <div className="space-y-0.5">{root.map((item) => renderItem(item))}</div>
          )}

          {/* Sections */}
          {groupedSections.map((s, idx) => (
            <div
              key={s.section}
              className={
                idx === 0 && root.length === 0
                  ? "space-y-0.5"
                  : "mt-6 space-y-0.5"
              }
            >
              <p className="section-label px-3 mb-2">
                {SECTION_TITLES[s.section]}
              </p>
              {s.items.map((item) => renderItem(item))}
            </div>
          ))}
        </nav>

        <div className="mt-auto">
          {/* FREE TRIAL card */}
          {showFreemiumCard && (
            <div className="px-3 pb-3">
              <div className="rounded-xl border border-[var(--border-soft)] bg-[linear-gradient(135deg,#fff_0%,#F4F9EC_55%,#F8FAFC_100%)] p-2 shadow-sm">
                <div className="mb-3 flex items-start justify-between gap-3">
                  <AnimatedLogoMark size={24} pulseEveryMs={60000} />
                  <span className="rounded bg-white/70 px-1.5 py-0.5 text-[9px] font-medium uppercase text-[var(--text-muted)]">
                    Free Trial
                  </span>
                </div>
                <div className="flex items-end justify-between gap-3">
                  <div>
                    <p className="text-[13px] font-semibold text-[var(--text-primary)]">MyOwnClone</p>
                    <p className="text-[11px] text-[var(--text-secondary)]">{trialDays == null ? "Free plan" : trialDays <= 0 ? "Trial ended" : trialDays + " days left"}</p>
                  </div>
                  <Link href="/planes" className="rounded-lg bg-[#4B5563] px-2.5 py-1.5 text-[11px] font-medium text-white shadow-sm">
                    Upgrade
                  </Link>
                </div>
                <div className="mt-2.5 h-1.5 rounded-full bg-[#E7E5E4]">
                  <div className="h-full rounded-full bg-[#1C1917]" style={{ width: trialPct + "%" }} />
                </div>
              </div>
            </div>
          )}

          {/* User */}
          {showUserBlock && user && (
            <div className="border-t border-[var(--border-soft)] px-3 py-3">
              <div className="flex items-center gap-2.5">
                <div className="h-7 w-7 rounded-full bg-gradient-to-br from-[#F97316] to-[#FB923C] flex items-center justify-center text-white text-xs font-semibold shrink-0">
                  {initials}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-xs font-medium text-[var(--text-primary)] truncate">
                    {user.name ?? "User"}
                  </p>
                  <p className="text-[10px] text-[var(--text-muted)] truncate">
                    {user.email ?? ""}
                  </p>
                </div>
                {signOutAction}
              </div>
            </div>
          )}

          {/* Footer slot */}
          {footer && (
            <div className="border-t border-[var(--border-soft)] px-3 py-3 text-[11px] text-[var(--text-muted)]">
              {footer}
            </div>
          )}
        </div>
      </aside>
    </>
  );
};

/** Small inline close button used inside the Radix Sheet. */
function DialogCloseButton({ onClick }: { onClick: () => void }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label="Close menu"
      className="h-8 w-8 rounded-md flex items-center justify-center text-[var(--text-muted)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)] transition-colors"
    >
      <span aria-hidden="true" className="text-lg leading-none">
        ×
      </span>
    </button>
  );
}
