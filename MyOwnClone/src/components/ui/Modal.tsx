"use client";

import {
  type FC,
  type ReactNode,
  useEffect,
  useId,
  useRef,
} from "react";

interface ModalProps {
  open: boolean;
  onClose: () => void;
  title: string;
  children: ReactNode;
  footer?: ReactNode;
  /** Optional max-width in Tailwind class. Defaults to max-w-md. */
  size?: "sm" | "md" | "lg";
  /** Accessible label for the close button. Defaults to "Close". */
  closeLabel?: string;
}

const SIZE_CLASS: Record<NonNullable<ModalProps["size"]>, string> = {
  sm: "max-w-sm",
  md: "max-w-md",
  lg: "max-w-2xl",
};

const FOCUSABLE_SELECTOR =
  'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

export const Modal: FC<ModalProps> = ({
  open,
  onClose,
  title,
  children,
  footer,
  size = "md",
  closeLabel = "Close",
}) => {
  const titleId = useId();
  const dialogRef = useRef<HTMLDivElement | null>(null);
  const previouslyFocusedRef = useRef<HTMLElement | null>(null);

  // Close on Escape + focus trap (Tab/Shift+Tab) + initial focus
  // management + focus restoration on close.
  useEffect(() => {
    if (!open) return;

    // Remember who had focus before the modal opened so we can restore
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
      ***REMOVED***rst.focus();
      }
    };
    window.addEventListener("keydown", handler, true);

    // Move initial focus to the dialog itself (it is the labelledby
    // container) so screen readers announce the title immediately.
    // We do this in a microtask so React has flushed the dialog node
    // into the DOM.
    queueMicrotask(() => {
      if (!dialogRef.current) return;
      const first = dialogRef.current.querySelector<HTMLElement>(
        FOCUSABLE_SELECTOR,
      );
      if (first) {
      ***REMOVED***rst.focus();
      } else {
        dialogRef.current.focus();
      }
    });

    return () => {
      window.removeEventListener("keydown", handler, true);
      const previous = previouslyFocusedRef.current;
      if (previous && document.body.contains(previous)) {
        previous.focus();
      }
    };
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4"
      // The dialog itself is a child <div>, the outer <div> is just
      // the centering wrapper. The dialog <div> is the one that needs
      // the role/aria.
    >
      <div
        className="absolute inset-0 bg-black/30 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden="true"
      />
      <div
        ref={dialogRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        tabIndex={-1}
        className={`relative w-full ${SIZE_CLASS[size]} rounded-2xl border border-[var(--border-soft)] bg-[var(--bg-shell)] shadow-[0_24px_64px_rgba(15,23,42,0.18)] outline-none`}
      >
        <div className="flex items-center justify-between border-b border-[var(--border-soft)] px-5 py-3">
          <h2
            id={titleId}
            className="text-sm font-semibold text-[var(--text-primary)]"
          >
            {title}
          </h2>
          <button
            type="button"
            aria-label={closeLabel}
            onClick={onClose}
            className="h-7 w-7 rounded-md text-[var(--text-muted)] hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] flex items-center justify-center focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]"
          >
            <span aria-hidden="true">×</span>
          </button>
        </div>
        <div className="p-5">{children}</div>
        {footer && (
          <div className="flex items-center justify-end gap-2 border-t border-[var(--border-soft)] px-5 py-3">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
};
