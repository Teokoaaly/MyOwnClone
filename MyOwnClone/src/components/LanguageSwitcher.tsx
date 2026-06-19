"use client";

import { type FC, useState, useEffect, useRef, useCallback } from "react";
import { useRouter } from "next/navigation";
import { useTranslations } from "next-intl";

type Locale = "es" | "en";

const COOKIE_NAME = "myownclone_locale";
const COOKIE_MAX_AGE = 60 * 60 * 24 * 365; // 1 year

function readCookie(name: string): string | null {
  if (typeof document === "undefined") return null;
  const match = document.cookie.match(
    new RegExp("(?:^|; )" + name.replace(/([.0*|{}()[\]\\/+^])/g, "\\$1") + "=([^;]*)"),
  );
  return match ? decodeURIComponent(match[1]) : null;
}

function setCookie(name: string, value: string, maxAge: number): void {
  if (typeof document === "undefined") return;
  document.cookie = name + "=" + encodeURIComponent(value) + "; Max-Age=" + maxAge + "; Path=/; SameSite=Lax";
}
function setLocaleCookies(locale: string) {
  setCookie(COOKIE_NAME, locale, COOKIE_MAX_AGE);
  setCookie("NEXT_LOCALE", locale, COOKIE_MAX_AGE);
}

export interface LanguageSwitcherProps {
  className?: string;
}

export const LanguageSwitcher: FC<LanguageSwitcherProps> = ({ className }) => {
  const router = useRouter();
  const t = useTranslations("common");
  const [open, setOpen] = useState(false);
  const [current, setCurrent] = useState<Locale>("en");
  const containerRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const cookie = readCookie(COOKIE_NAME);
    if (cookie === "es" || cookie === "en") {
      setCurrent(cookie);
    }
  }, []);

  const close = useCallback(() => setOpen(false), []);

  useEffect(() => {
    if (!open) return;
    function onDown(e: MouseEvent) {
      if (!containerRef.current) return;
      if (containerRef.current.contains(e.target as Node)) return;
      close();
    }
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, [open, close]);

  useEffect(() => {
    if (!open) return;
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") close();
    }
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open, close]);

  const select = (next: Locale) => {
    if (next === current) {
      close();
      return;
    }
    setLocaleCookies(next);
    setCurrent(next);
    close();
    router.refresh();
  };

  const label =
    current === "es" ? t("languageSwitcher.spanish") : t("languageSwitcher.english");

  return (
    <div ref={containerRef} className={"relative inline-block text-left " + (className ?? "")}>
      <button
        type="button"
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-label={t("languageSwitcher.label")}
        onClick={() => setOpen((v) => !v)}
        className="inline-flex items-center gap-1.5 rounded-md border border-[var(--border-soft)] bg-[var(--surface-2)] px-2.5 py-1.5 text-xs font-medium text-[var(--text-primary)] hover:bg-[var(--surface-3)] transition-colors"
      >
        <svg
          aria-hidden="true"
          className="h-3.5 w-3.5"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth={2}
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <circle cx="12" cy="12" r="10" />
          <path d="M2 12h20" />
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
        </svg>
        <span>{label}</span>
        <svg
          aria-hidden="true"
          className={"h-3 w-3 transition-transform " + (open ? "rotate-180" : "")}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth={2}
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </button>

      {open && (
        <ul
          role="listbox"
          aria-label={t("languageSwitcher.label")}
          className="absolute right-0 top-full mt-1 min-w-[140px] rounded-md border border-[var(--border-soft)] bg-[var(--bg-shell)] py-1 shadow-lg z-50"
        >
          <li>
            <button
              type="button"
              role="option"
              aria-selected={current === "en"}
              onClick={() => select("en")}
              className={
                "w-full text-left px-3 py-1.5 text-xs transition-colors " +
                (current === "en"
                  ? "bg-[var(--surface-2)] text-[var(--text-primary)] font-semibold"
                  : "text-[var(--text-secondary)] hover:bg-[var(--surface-2)]")
              }
            >
              {t("languageSwitcher.english")}
            </button>
          </li>
          <li>
            <button
              type="button"
              role="option"
              aria-selected={current === "es"}
              onClick={() => select("es")}
              className={
                "w-full text-left px-3 py-1.5 text-xs transition-colors " +
                (current === "es"
                  ? "bg-[var(--surface-2)] text-[var(--text-primary)] font-semibold"
                  : "text-[var(--text-secondary)] hover:bg-[var(--surface-2)]")
              }
            >
              {t("languageSwitcher.spanish")}
            </button>
          </li>
        </ul>
      )}
    </div>
  );
};

export default LanguageSwitcher;
