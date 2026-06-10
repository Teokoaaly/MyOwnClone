"use client";

import { useState } from "react";
import { signOut } from "next-auth/react";
import { SignOut as SignOutIcon } from "@phosphor-icons/react";
import { useRouter } from "@/i18n/navigation";

interface SignOutButtonProps {
  callbackUrl?: string;
  className?: string;
  showLabel?: boolean;
}

export function SignOutButton({
  callbackUrl = "/login",
  className,
  showLabel = false,
}: SignOutButtonProps) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  async function handleClick() {
    setLoading(true);
    try {
      await signOut({ callbackUrl, redirect: false });
    } finally {
      router.push(callbackUrl);
      router.refresh();
    }
  }

  return (
    <button
      type="button"
      onClick={handleClick}
      disabled={loading}
      aria-label={showLabel ? undefined : "Cerrar sesión"}
      title="Cerrar sesión"
      className={
        className ??
        "flex items-center justify-center rounded-md p-1.5 text-[var(--text-muted)] transition hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] disabled:opacity-50"
      }
    >
      <SignOutIcon size={16} weight="bold" />
      {showLabel && (
        <span className="ml-1.5 text-[11px] font-medium">
          {loading ? "Saliendo…" : "Cerrar sesión"}
        </span>
      )}
    </button>
  );
}
