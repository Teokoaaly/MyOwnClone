"use client";

import { useState } from "react";
import { Link } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

export default function ForgotPasswordPage() {
  const t = useTranslations("forgotPassword")
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [sent, setSent] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const res = await fetch("/api/auth/forgot-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        setError(data.error ?? t("errorSending"));
        return;
      }

      setSent(true);
    } catch {
      setError(t("connectionError"));
    } finally {
      setLoading(false);
    }
  }

  if (sent) {
    return (
      <main
        className="flex min-h-screen items-center justify-center px-4 py-12"
        style={{ background: "var(--bg-page)" }}
      >
        <div className="w-full max-w-md card text-center">
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            {t("checkEmail")}
          </h1>
          <p className="mt-2 text-sm text-[var(--text-muted)]">
            {t("checkEmailDesc", { email })}
          </p>
          <p className="mt-4 text-xs text-[var(--text-muted)]">
            {t("linkExpires")}
          </p>
          <Link
            href="/login"
            className="btn-primary mt-6 inline-block text-sm"
          >
            {t("backToLogin")}
          </Link>
        </div>
      </main>
    );
  }

  return (
    <main
      className="flex min-h-screen items-center justify-center px-4 py-12"
      style={{ background: "var(--bg-page)" }}
    >
      <div className="w-full max-w-md card">
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          {t("title")}
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          {t("description")}
        </p>

        {error && (
          <div
            role="alert"
            className="mt-4 rounded-lg p-3 text-sm"
            style={{
              background: "var(--surface-2)",
              border: "1px solid var(--color-accent-pink)",
              color: "var(--text-primary)",
            }}
          >
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="mt-6 space-y-4" noValidate>
          <div>
            <label
              htmlFor="forgot-email"
              className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
            >
              {t("emailLabel")}
            </label>
            <input
              id="forgot-email"
              name="email"
              type="email"
              required
              autoComplete="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder={t("emailPlaceholder")}
              className="w-full rounded-xl border border-[var(--border-medium)] bg-[var(--surface-2)] px-4 py-3 text-sm text-[var(--text-primary)] outline-none transition focus:ring-2"
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="btn-primary w-full py-3 text-sm font-semibold disabled:opacity-50"
          >
            {loading ? t("sending") : t("sendLink")}
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-[var(--text-muted)]">
          <Link
            href="/login"
            className="font-medium underline decoration-[var(--color-accent-violet)] underline-offset-4 hover:opacity-80"
            style={{ color: "var(--text-primary)" }}
          >
            {t("backToLogin")}
          </Link>
        </p>
      </div>
    </main>
  );
}
