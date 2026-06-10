/**
 * Hook to resolve and cache the active clone ID for the current tenant.
 * Sets a cookie that the middleware reads for proxying API calls.
 */
"use client";

import { useEffect, useState } from "react";
import {
  resolveActiveCloneId,
  getCloneIdFromCookie,
} from "@/lib/clone-resolver";

export function useActiveCloneId() {
  const [cloneId, setCloneId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check cookie first (synchronous)
    const cached = getCloneIdFromCookie();
    if (cached) {
      setCloneId(cached);
      setLoading(false);
      return;
    }

    // Fetch from API and cache
    resolveActiveCloneId().then((id) => {
      setCloneId(id);
      setLoading(false);
    });
  }, []);

  return { cloneId, loading };
}
