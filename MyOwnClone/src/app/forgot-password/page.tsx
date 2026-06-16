"use client";

import { useState } from "react";
import { Link } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

export default function ForgotPasswordPage() {
  const t = useTranslations("auth");
  void t;
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
        setError(data.error ?? "Error al enviar el enlace. Intenta de nuevo.");
        return;
      }

      setSent(true);
    } catch {
      setError("Error de conexión. Intenta de nuevo.");
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
            Revisa tu correo
          </h1>
          <p className="mt-2 text-sm text-[var(--text-muted)]">
            Si la dirección está registrada, hemos enviado un enlace para
            restablecer tu contraseña a{" "}
            <strong className="text-[var(--text-primary)]">{email}</strong>.
          </p>
          <p className="mt-4 text-xs text-[var(--text-muted)]">
            El enlace caduca en 30 minutos. Si no ves el correo, revisa la
            carpeta de spam.
          </p>
          <Link
            href="/login"
            className="btn-primary mt-6 inline-block text-sm"
          >
            Volver a iniciar sesión
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
          ¿Olvidaste tu contraseña?
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          Te enviaremos un enlace para que puedas crear una nueva.
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
              Correo electrónico
            </label>
            <input
              id="forgot-email"
              name="email"
              type="email"
              required
              autoComplete="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="tu@email.com"
              className="w-full rounded-xl border border-[var(--border-medium)] bg-[var(--surface-2)] px-4 py-3 text-sm text-[var(--text-primary)] outline-none transition focus:ring-2"
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="btn-primary w-full py-3 text-sm font-semibold disabled:opacity-50"
          >
            {loading ? "Enviando…" : "Enviar enlace"}
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-[var(--text-muted)]">
          <Link
            href="/login"
            className="font-medium underline decoration-[var(--color-accent-violet)] underline-offset-4 hover:opacity-80"
            style={{ color: "var(--text-primary)" }}
          >
            Volver a iniciar sesión
          </Link>
        </p>
      </div>
    </main>
  );
}
