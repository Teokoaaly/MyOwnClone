"use client";

import { Suspense, useState } from "react";
import { useSearchParams } from "next/navigation";
import { Link, useRouter } from "@/i18n/navigation";

function ResetPasswordForm() {
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
          Enlace no válido
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          Falta el token o el email. Solicita un nuevo enlace desde la página
          de recuperación.
        </p>
        <Link
          href="/forgot-password"
          className="btn-primary mt-6 inline-block text-sm"
        >
          Solicitar nuevo enlace
        </Link>
      </div>
    );
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    if (password.length < 8) {
      setError("La contraseña debe tener al menos 8 caracteres.");
      return;
    }
    if (password !== confirm) {
      setError("Las contraseñas no coinciden.");
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
        setError(data.error ?? "No se pudo restablecer la contraseña.");
        return;
      }

      setSuccess(true);
      setTimeout(() => router.push("/login"), 1500);
    } catch {
      setError("Error de conexión. Intenta de nuevo.");
    } finally {
      setLoading(false);
    }
  }

  if (success) {
    return (
      <div className="w-full max-w-md card text-center">
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Contraseña actualizada
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          Te estamos redirigiendo al inicio de sesión…
        </p>
        <Link
          href="/login"
          className="btn-primary mt-6 inline-block text-sm"
        >
          Iniciar sesión
        </Link>
      </div>
    );
  }

  return (
    <div className="w-full max-w-md card">
      <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
        Restablecer contraseña
      </h1>
      <p className="mt-2 text-sm text-[var(--text-muted)]">
        Para <strong className="text-[var(--text-primary)]">{email}</strong>,
        elige una nueva contraseña.
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
            Nueva contraseña
          </label>
          <input
            id="reset-password"
            type="password"
            required
            autoComplete="new-password"
            minLength={8}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Mínimo 8 caracteres"
            className="w-full rounded-xl border border-[var(--border-medium)] bg-[var(--surface-2)] px-4 py-3 text-sm text-[var(--text-primary)] outline-none transition focus:ring-2"
          />
        </div>
        <div>
          <label
            htmlFor="reset-confirm"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            Confirmar contraseña
          </label>
          <input
            id="reset-confirm"
            type="password"
            required
            autoComplete="new-password"
            minLength={8}
            value={confirm}
            onChange={(e) => setConfirm(e.target.value)}
            placeholder="Repite la contraseña"
            className="w-full rounded-xl border border-[var(--border-medium)] bg-[var(--surface-2)] px-4 py-3 text-sm text-[var(--text-primary)] outline-none transition focus:ring-2"
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="btn-primary w-full py-3 text-sm font-semibold disabled:opacity-50"
        >
          {loading ? "Guardando…" : "Restablecer contraseña"}
        </button>
      </form>
    </div>
  );
}

export default function ResetPasswordPage() {
  return (
    <main
      className="flex min-h-screen items-center justify-center px-4 py-12"
      style={{ background: "var(--bg-page)" }}
    >
      <Suspense
        fallback={
          <div className="text-sm text-[var(--text-muted)]">Cargando…</div>
        }
      >
        <ResetPasswordForm />
      </Suspense>
    </main>
  );
}
