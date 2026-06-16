/**
 * Client-side clone resolution — fetches clones from API.
 *
 * The server sets an HttpOnly cookie for the proxy's use.
 * This module reads the clone ID from the API response body.
 *
 * Used by dashboard pages to resolve the active clone ID without relying on
 * the server-side DEFAULT_CLONE_ID env var.
 */
"use client";

const CLONE_ID_COOKIE = "moc_active_clone_id";

/**
 * Resolve the active clone ID for the current tenant.
 * Fetches from API - server sets HttpOnly cookie for proxy's use.
 * Clone ID is read from API response body since cookie is HttpOnly.
 */
export async function resolveActiveCloneId(): Promise<string | null> {
  try {
    const res = await fetch("/api/clone/clones");
    if (!res.ok) return null;
    const data = await res.json();

    // Response format: { activeCloneId: string, clones: [...] }
    if (data?.activeCloneId) {
      return data.activeCloneId;
    }

    // Fallback: check clones array directly
    if (Array.isArray(data?.clones) && data.clones.length > 0) {
      return data.clones[0].id;
    }
    if (Array.isArray(data) && data.length > 0) {
      return data[0].id;
    }
  } catch {
    // Silently fail — caller handles null
  }

  return null;
}

/**
 * Get the active clone ID from cookie.
 */
export function getCloneIdFromCookie(): string | null {
  if (typeof document === "undefined") return null;
  const match = document.cookie.match(new RegExp(`${CLONE_ID_COOKIE}=([^;]+)`));
  return match ? decodeURIComponent(match[1]) : null;
}

/**
 * Set the active clone ID cookie (30-day expiry).
 */
export function setCloneIdCookie(id: string): void {
  if (typeof document === "undefined") return;
  const expires = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toUTCString();
  const secure =
    typeof window !== "undefined" && window.location.protocol === "https:"
      ? "; Secure"
      : "";
  document.cookie = `${CLONE_ID_COOKIE}=${encodeURIComponent(id)}; expires=${expires}; path=/; SameSite=Lax${secure}`;
}

/**
 * Clear the active clone ID cookie.
 */
export function clearCloneIdCookie(): void {
  if (typeof document === "undefined") return;
  document.cookie = `${CLONE_ID_COOKIE}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/`;
}
