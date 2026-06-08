"use client";

import { type FC, type ReactNode } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import type { IconProps } from "@phosphor-icons/react";

export interface SidebarNavItem {
  href: string;
  label: string;
  icon: React.ComponentType<IconProps>;
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
  /** Whether to render the "FREE TRAIL" freemium card. Defaults to true. */
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
  showFreemiumCard = true,
  showUserBlock = true,
  footer,
}) => {
  const pathname = usePathname();
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

  const renderItem = (item: SidebarNavItem) => {
    const isActive = pathname?.startsWith(item.href);
    const Icon = item.icon;

    return (
      <div key={item.href} className="relative">
        <Link
          href={item.href}
          title={item.tooltip}
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

  return (
    <aside
      className="w-[220px] shrink-0 flex flex-col border-r border-[var(--border-soft)]"
      style={{ background: "var(--bg-sidebar)" }}
    >
      {/* Logo */}
      <div className="px-5 pt-5 pb-4">
        <Link href={homeHref} className="flex items-center gap-2">
          <div className="h-7 w-7 rounded-lg bg-black text-white flex items-center justify-center text-[11px] font-bold">
            M
          </div>
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
      <nav className="flex-1 px-3 py-4 overflow-y-auto">
        {/* Root items (Overview) */}
        {root.length > 0 && <div className="space-y-0.5">{root.map(renderItem)}</div>}

        {/* Sections */}
        {groupedSections.map((s, idx) => (
          <div key={s.section} className={idx === 0 && root.length === 0 ? "space-y-0.5" : "mt-6 space-y-0.5"}>
            <p className="section-label px-3 mb-2">{SECTION_TITLES[s.section]}</p>
            {s.items.map(renderItem)}
          </div>
        ))}
      </nav>

      {/* FREE TRAIL card */}
      {showFreemiumCard && (
        <div className="px-3 pb-3">
          <div className="rounded-2xl border border-[var(--border-soft)] bg-[var(--surface-2)] p-4">
            <div className="flex items-center justify-between mb-2">
              <div className="h-7 w-7 rounded-lg bg-black text-white flex items-center justify-center text-[10px] font-bold">
                M
              </div>
              <span className="text-[9px] font-semibold tracking-[0.14em] text-[var(--text-muted)]">
                FREE TRIAL
              </span>
            </div>
            <p className="text-sm font-semibold text-[var(--text-primary)]">
              MyOwnClone
            </p>
            <p className="text-[11px] text-[var(--text-muted)] mb-3">
              7 days left
            </p>
            <button
              type="button"
              className="w-full rounded-full bg-black text-white text-xs font-medium py-2 hover:opacity-90 transition-opacity"
            >
              Upgrade
            </button>
            <div className="mt-3 h-1 rounded-full bg-[var(--border-medium)] overflow-hidden">
              <div className="h-full w-[14%] bg-black rounded-full" />
            </div>
          </div>
        </div>
      )}

      {/* User */}
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

      {/* Footer slot */}
      {footer && (
        <div className="px-3 py-3 border-t border-[var(--border-soft)] text-[11px] text-[var(--text-muted)]">
          {footer}
        </div>
      )}
    </aside>
  );
};
