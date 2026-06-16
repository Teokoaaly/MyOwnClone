/**
 * Shared hook for clone ID management.
 * Single source of truth for clone ID resolution and caching.
 *
 * Provides a consistent interface across the app for:
 * - Resolving active clone ID
 * - Cookie-based caching
 * - Loading states
 */
"use client";

import { useEffect, useState, useCallback } from "react";
import {
  resolveActiveCloneId,
  getCloneIdFromCookie,
  setCloneIdCookie,
  clearCloneIdCookie,
} from "@/lib/clone-resolver";

export interface UseCloneIdOptions {
  /** Skip initial cookie check and always fetch from API */
  forceRefresh?: boolean;
  /** Callback fired when clone ID is resolved */
  onResolved?: (cloneId: string | null) => void;
}

export interface UseCloneIdReturn {
  /** The resolved clone ID, or null if not yet resolved */
  cloneId: string | null;
  /** Whether the clone ID is being fetched */
  loading: boolean;
  /** Manually trigger a refresh of the clone ID */
  refresh: () => Promise<void>;
  /** Clear the cached clone ID from cookie */
  clear: () => void;
}

/**
 * Hook to resolve and cache the active clone ID for the current tenant.
 *
 * @example
 * // Basic usage
 * const { cloneId, loading } = useCloneId();
 *
 * @example
 * // With force refresh
 * const { cloneId, loading, refresh } = useCloneId({ forceRefresh: true });
 */
export function useCloneId(options: UseCloneIdOptions = {}): UseCloneIdReturn {
  const { forceRefresh = false, onResolved } = options;

  const [cloneId, setCloneId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  const resolve = useCallback(async () => {
    setLoading(true);
    let id: string | null = null;

    if (!forceRefresh) {
      // Check cookie first (synchronous)
      id = getCloneIdFromCookie();
    }

    if (!id) {
      // Fetch from API and cache
      id = await resolveActiveCloneId();
    }

    setCloneId(id);
    setLoading(false);
    onResolved?.(id);

    return id;
  }, [forceRefresh, onResolved]);

  const clear = useCallback(() => {
    clearCloneIdCookie();
    setCloneId(null);
  }, []);

  useEffect(() => {
    resolve();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return { cloneId, loading, refresh: resolve, clear };
}

/**
 * Set the active clone ID in cookie directly.
 * Useful when you have a specific clone ID to cache.
 */
export function setCloneId(id: string): void {
  setCloneIdCookie(id);
}

/**
 * Get the active clone ID from cookie synchronously.
 * Returns null if not cached.
 */
export function getCloneId(): string | null {
  return getCloneIdFromCookie();
}

/**
 * Clear the active clone ID from cookie.
 */
export function clearCloneId(): void {
  clearCloneIdCookie();
}
