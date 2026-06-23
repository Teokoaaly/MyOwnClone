"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "@/i18n/navigation";

interface UseAdminFetchResult<T> {
  /** Last successful payload, or `null` until the first successful fetch. */
  data: T | null;
  /** `true` while a fetch is in flight. Starts as `true`. */
  loading: boolean;
  /** Human-readable error message, or `null`. Cleared on every new fetch. */
  error: string | null;
  /** Bump the internal counter to force a re-fetch with the same URL. */
  reload: () => void;
}

/**
 * Standard GET helper for `/api/admin/*` endpoints used by every admin
 * page. It:
 *
 * - Re-fetches whenever `url` changes.
 * - Cancels stale responses when the effect re-runs or the component unmounts.
 * - Redirects to `/login` on 401 / 403 (the page is unauthenticated or no
 *   longer has the platform_admin role).
 * - Surfaces other backend errors via `error`.
 *
 * Pass `url: null` to skip fetching (e.g. when a required id is not yet
 * available).
 */
export function useAdminFetch<T>(
  url: string | null,
): UseAdminFetchResult<T> {
  const router = useRouter();
  const redirectedRef = useRef(false);
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [reloadCount, setReloadCount] = useState<number>(0);

  useEffect(() => {
    if (url === null) {
      setLoading(false);
      return;
    }
    let cancelled = false;
    setLoading(true);
    setError(null);

    fetch(url, { cache: "no-store", credentials: "include" })
      .then((res) => {
        if (res.status === 401 || res.status === 403) {
          if (!redirectedRef.current) {
            redirectedRef.current = true;
            router.replace("/login");
          }
          return null;
        }
        if (!res.ok) {
          throw new Error(`Backend error ${res.status}`);
        }
        return res.json() as Promise<T>;
      })
      .then((payload) => {
        if (cancelled || payload === null || payload === undefined) return;
        setData(payload);
      })
      .catch((err: unknown) => {
        if (cancelled) return;
        setError(err instanceof Error ? err.message : "Error");
      })
      .finally(() => {
        if (cancelled) return;
        setLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [router, url, reloadCount]);

  return {
    data,
    loading,
    error,
    reload: () => setReloadCount((n) => n + 1),
  };
}
