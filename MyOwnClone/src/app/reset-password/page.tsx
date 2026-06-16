"use client";

import { Suspense, useState } from "react";
import { useSearchParams } from "next/navigation";
import { Link, useRouter } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

function ResetPasswordForm() {
  const t = useTranslations("resetPassword")
  const searchParams = useSearchParams();
  const router = useRouter();
  const token = searchParams.get("token") ?? "";
  const email = searchParams.get("email") ?? "";

  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  if (!token || !email) {
    return (
      <div className="w-full max-w-md card text-center">
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          {t("invalidLink")}
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          {t("missingTokenEmail")}
        </p>
        <Link
          href="/forgot-password"
          className="btn-primary mt-6 inline-block text-sm"
        >
          {t("requestNewLink")}
        </Link>
      </div>
    );
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    if (password.length < 12) {
      setError(t("passwordMinLength"));
      return;
    }
    if (!/[a-z]/.test(password) || !/[A-Z]/.test(password) || !/[0-9]/.test(password) || !/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
      setError(t("passwordRequirements"));
      return;
    }
    if (password !== confirm) {
      setError(t("passwordsMismatch"));
      return;
    }

    setLoading(true);
    try {
      const res = await fetch("/api/auth/reset-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token, email, password }),
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        setError(data.error ?? t("errorResetting"));
        return;
      }

      setSuccess(true);
      setTimeout(() => router.push("/login"), 1500);
    } catch {
      setError(t("connectionError"));
    } finally {
      setLoading(false);
    }
  }

  if (success) {
    return (
      <div className="w-full max-w-md card text-center">
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          {t("passwordUpdated")}
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          {t("redirecting")}
        </p>
        <Link
          href="/login"
          className="btn-primary mt-6 inline-block text-sm"
        >
          {t("goToLogin")}
        </Link>
      </div>
    );
  }

  return (
    <div className="w-full max-w-md card">
      <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
        {t("title")}
      </h1>
      <p className="mt-2 text-sm text-[var(--text-muted)]">
        {t("description", { email })}
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
            htmlFor="reset-password"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            {t("passwordLabel")}
          </label>
          <input
            id="reset-password"
            type="password"
            required
            autoComplete="new-password"
            minLength={12}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder={t("passwordPlaceholder")}
            className="w-full rounded-xl border border-[var(--border-medium)] bg-[var(--surface-2)] px-4 py-3 text-sm text-[var(--text-primary)] outline-none transition focus:ring-2"
          />
        </div>
        <div>
          <label
            htmlFor="reset-confirm"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            {t("confirmLabel")}
          </label>
          <input
            id="reset-confirm"
            type="password"
            required
            autoComplete="new-password"
            minLength={12}
            value={confirm}
            onChange={(e) => setConfirm(e.target.value)}
            placeholder={t("confirmPlaceholder")}
            className="w-full rounded-xl border border-[var(--border-medium)] bg-[var(--surface-2)] px-4 py-3 text-sm text-[var(--text-primary)] outline-none transition focus:ring-2"
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="btn-primary w-full py-3 text-sm font-semibold disabled:opacity-50"
        >
          {loading ? t("saving") : t("reset")}
        </button>
      </form>
    </div>
  );
}

export default function ResetPasswordPage() {
  const t = useTranslations("resetPassword")
  return (
    <main
      className="flex min-h-screen items-center justify-center px-4 py-12"
      style={{ background: "var(--bg-page)" }}
    >
      <Suspense
        fallback={
          <div className="text-sm text-[var(--text-muted)]">{t("loading")}</div>
        }
      >
        <ResetPasswordForm />
      </Suspense>
    </main>
  );
}
