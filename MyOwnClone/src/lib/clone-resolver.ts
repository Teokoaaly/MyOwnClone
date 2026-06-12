/**
 * Client-side clone resolution — fetches clones from API and caches in cookie.
 *
 * Used by dashboard pages to resolve the active clone ID without relying on
 * the server-side DEFAULT_CLONE_ID env var.
 */
"use client";

const CLONE_ID_COOKIE = "moc_active_clone_id";

/**
 * Resolve the active clone ID for the current tenant.
 * Checks cookie first, then fetches from API and caches.
 */
export async function resolveActiveCloneId(): Promise<string | null> {
  // Check cookie first
  const cached = getCloneIdFromCookie();
  if (cached) return cached;

  try {
    const res = await fetch("/api/clone/clones");
    if (!res.ok) return null;
    const clones = await res.json();

    if (Array.isArray(clones) && clones.length > 0) {
      const id = clones[0].id;
      setCloneIdCookie(id);
      return id;
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
