"use client";

import { type FC, useEffect, useId, useRef } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import type { IconProps } from "@phosphor-icons/react";
import { ThemeToggle } from "@/components/ui/ThemeToggle";

export interface MobileNavItem {
  href: string;
  label: string;
  icon: React.ComponentType<IconProps>;
}

interface MobileNavProps {
  open: boolean;
  onClose: () => void;
  items: MobileNavItem[];
  /** Brand label shown at the top of the drawer. */
  brand?: string;
  /** Optional link shown below the nav. */
  footer?: React.ReactNode;
}

const FOCUSABLE_SELECTOR =
  'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

export const MobileNav: FC<MobileNavProps> = ({
  open,
  onClose,
  items,
  brand = "MyOwnClone",
  footer,
}) => {
  const pathname = usePathname();
  const brandId = useId();
  const drawerRef = useRef<HTMLElement | null>(null);
  const previouslyFocusedRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (!open) return;

    // Remember who had focus before the drawer opened so we can restore
    // it on close.
    previouslyFocusedRef.current =
      document.activeElement instanceof HTMLElement
        ? document.activeElement
        : null;

    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.stopPropagation();
        onClose();
        return;
      }
      if (e.key !== "Tab" || !drawerRef.current) return;
      const focusables = Array.from(
        drawerRef.current.querySelectorAll<HTMLElement>(FOCUSABLE_SELECTOR),
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
      ***REMOVED***rst.focus();
      }
    };
    window.addEventListener("keydown", handler, true);

    // Prevent body scroll while the drawer is open.
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";

    // Move initial focus to the first focusable inside the drawer so
    // keyboard users land in the dialog immediately.
    queueMicrotask(() => {
      if (!drawerRef.current) return;
      const first = drawerRef.current.querySelector<HTMLElement>(
        FOCUSABLE_SELECTOR,
      );
      if (first) first.focus();
    });

    return () => {
      window.removeEventListener("keydown", handler, true);
      document.body.style.overflow = prev;
      const previous = previouslyFocusedRef.current;
      if (previous && document.body.contains(previous)) {
        previous.focus();
      }
    };
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div className="md:hidden" role="dialog" aria-modal="true" aria-labelledby={brandId}>
      <div
        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden="true"
      />
      <aside
        ref={drawerRef}
        className="fixed inset-y-0 left-0 z-50 flex w-[280px] flex-col border-r border-[var(--border-soft)] shadow-[0_24px_64px_rgba(15,23,42,0.18)] outline-none"
        style={{ background: "var(--bg-sidebar)" }}
        tabIndex={-1}
      >
        <div className="flex items-center justify-between px-5 pt-5 pb-4">
          <span
            id={brandId}
            className="text-sm font-semibold tracking-wide text-[var(--text-primary)]"
          >
            {brand}
          </span>
          <button
            type="button"
            onClick={onClose}
            aria-label="Cerrar menú"
            className="h-8 w-8 rounded-md flex items-center justify-center text-[var(--text-muted)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]"
          >
            <span aria-hidden="true">×</span>
          </button>
        </div>

        <nav className="flex-1 overflow-y-auto px-3 py-2" aria-label="Navegación principal">
          {items.map((item) => {
            const isActive = pathname?.startsWith(item.href);
            const Icon = item.icon;
            return (
              <Link
                key={item.href}
                href={item.href}
                onClick={onClose}
                aria-current={isActive ? "page" : undefined}
                className={[
                  "flex h-11 items-center gap-3 rounded-lg px-3 text-sm transition duration-150 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]",
                  isActive
                    ? "nav-item-active"
                    : "nav-item-normal",
                ].join(" ")}
              >
                <Icon className="h-[18px] w-[18px] shrink-0" weight="duotone" aria-hidden="true" />
                <span className="truncate">{item.label}</span>
              </Link>
            );
          })}
        </nav>

        <div className="border-t border-[var(--border-soft)] px-4 py-3 flex items-center justify-between">
          <span className="text-[11px] text-[var(--text-muted)]">Tema</span>
          <ThemeToggle showLabel />
        </div>

        {footer && (
          <div className="border-t border-[var(--border-soft)] px-4 py-3 text-[11px] text-[var(--text-muted)]">
            {footer}
          </div>
        )}
      </aside>
    </div>
  );
};
