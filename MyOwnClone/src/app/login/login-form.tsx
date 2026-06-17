"use client";

import { useState, useEffect } from "react";
import { getSession, signIn } from "next-auth/react";
import { Link, useRouter } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

export function LoginForm() {
  const t = useTranslations("auth")
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Clean credentials from URL if someone navigated with them exposed
  useEffect(() => {
    if (typeof window === "undefined") return;
    const params = new URLSearchParams(window.location.search);
    if (params.has("email") || params.has("password")) {
      window.history.replaceState(null, "", window.location.pathname);
    }
  }, []);


  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const result = await signIn("credentials", {
        email,
        password,
        redirect: false,
        callbackUrl: "/resumen",
      });

      if (result?.error) {
        setError(t("invalidCredentials"));
        setLoading(false);
        return;
      }

      // Decide destination based on the resulting session role
      const session = await getSession();
      const role = (session?.user as { role?: string } | undefined)?.role;
      router.replace(role === "platform_admin" ? "/admin/resumen" : "/resumen");
    } catch {
      setError(t("connectionError"));
      setLoading(false);
    }
  }

  return (
    <div
      className="rounded-2xl p-8"
      style={{
        background: "var(--bg-shell)",
        boxShadow:
          "0 1px 2px rgba(15, 23, 42, 0.04), 0 24px 64px rgba(15, 23, 42, 0.10)",
      }}
    >
      <form method="POST" onSubmit={handleSubmit} className="space-y-6" noValidate>
        {error && (
          <div
            role="alert"
            className="rounded-lg p-3 text-sm"
            style={{
              background: "var(--surface-2)",
              border: "1px solid var(--color-accent-pink)",
              color: "var(--text-primary)",
            }}
          >
            {error}
          </div>
        )}
        <div>
          <label
            htmlFor="login-email"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            {t("emailLabel")}
          </label>
          <input
            id="login-email"
            name="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder={t("emailPlaceholder")}
            required
            autoComplete="email"
            className="w-full rounded-xl border px-4 py-3 text-sm outline-none transition focus:ring-2"
            style={{
              background: "var(--surface-2)",
              borderColor: "var(--border-medium)",
              color: "var(--text-primary)",
            }}
          />
        </div>
        <div>
          <label
            htmlFor="login-password"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            {t("passwordLabel")}
          </label>
          <input
            id="login-password"
            name="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder={t("passwordPlaceholder")}
            required
            autoComplete="current-password"
            className="w-full rounded-xl border px-4 py-3 text-sm outline-none transition focus:ring-2"
            style={{
              background: "var(--surface-2)",
              borderColor: "var(--border-medium)",
              color: "var(--text-primary)",
            }}
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="btn-primary w-full py-3 text-sm font-semibold disabled:opacity-50 flex items-center justify-center"
        >
          {loading ? t("signingIn") : t("signIn")}
        </button>
      </form>

      <div className="mt-6">
        <p className="text-center text-sm text-[var(--text-muted)] mb-4">
          {t("orContinue")}
        </p>
        <button
          type="button"
          onClick={() => signIn("google", { callbackUrl: "/resumen" })}
          aria-label={t("googleButton")}
          className="mt-4 flex w-full items-center justify-center gap-3 rounded-xl border px-4 py-3 font-semibold transition"
          style={{
            borderColor: "var(--border-medium)",
            color: "var(--text-primary)",
            background: "var(--bg-shell)",
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.background = "var(--surface-2)";
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.background = "var(--bg-shell)";
          }}
        >
          <svg className="h-5 w-5" viewBox="0 0 24 24" aria-hidden="true">
            <path
              fill="#4285F4"
              d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"
            />
            <path
              fill="#34A853"
              d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
            />
            <path
              fill="#FBBC05"
              d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
            />
            <path
              fill="#EA4335"
              d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
            />
          </svg>
          {t("googleButton")}
        </button>
      </div>

      <p className="mt-4 text-center text-sm text-[var(--text-muted)]">
        <Link
          href="/forgot-password"
          className="font-medium underline decoration-[var(--color-accent-violet)] underline-offset-4 hover:opacity-80"
          style={{ color: "var(--text-primary)" }}
        >
          {t("forgotPassword")}
        </Link>
      </p>
    </div>
  );
}
