"use client";

import { useEffect, useState, useTransition } from "react";
import { Globe } from "@phosphor-icons/react";
import { useLocale } from "next-intl";
import {
  LOCALE_LABELS,
  setBackendLocale,
  type LocaleInfo,
} from "@/lib/locale";

/**
 * Compact language selector used in the dashboard sidebar and the
 * public header. The choice is persisted server-side via
 * ``POST /console/api/myownclone/me/locale`` so the backend respects
 * the same language on every request.
 */
export function LanguageSelector({ variant = "sidebar" }: { variant?: "sidebar" | "header" }) {
  const current = useLocale();
  const [supported, setSupported] = useState<string[]>(["en", "es"]);
  const [value, setValue] = useState<string>(current);
  const [isPending, startTransition] = useTransition();
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/me/locale", { cache: "no-store" });
        if (!res.ok) return;
        const data = (await res.json()) as LocaleInfo;
        if (cancelled || !data?.supported?.length) return;
        setSupported(data.supported);
        if (data.locale && data.locale !== value) {
          setValue(data.locale);
        }
      } catch {
        // Silent: defaults are good enough.
      }
    })();
    return () => {
      cancelled = true;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function onChange(newLocale: string) {
    if (newLocale === value) return;
    setValue(newLocale);
    setError(null);
    startTransition(async () => {
      try {
        const result = await setBackendLocale(newLocale);
        if (!result) {
          setError("Could not persist language on the server.");
          return;
        }
        window.location.reload();
      } catch {
        setError("Could not persist language on the server.");
      }
    });
  }

  const baseClass =
    "flex items-center gap-2 rounded-md border border-[var(--border-soft)] bg-[var(--surface-2)] px-2.5 py-1.5 text-xs text-[var(--text-primary)] hover:bg-[var(--surface-1)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-warm)]";

  return (
    <label className={variant === "sidebar" ? baseClass : `${baseClass} w-auto`}>
      <Globe size={14} aria-hidden="true" />
      <span className="sr-only">Language</span>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={isPending}
        aria-label="Select language"
        className="bg-transparent text-xs focus:outline-none disabled:opacity-50"
      >
        {supported.map((loc) => (
          <option key={loc} value={loc}>
            {LOCALE_LABELS[loc] ?? loc.toUpperCase()}
          </option>
        ))}
      </select>
      {error && (
        <span role="alert" className="ml-1 text-[10px] text-red-500">
          {error}
        </span>
      )}
    </label>
  );
}
