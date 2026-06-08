"use client";

import { useState } from "react";
import { getSession, signIn } from "next-auth/react";

export function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");

    const result = await signIn("credentials", {
      email,
      password,
      redirect: false,
      callbackUrl: "/resumen",
    });

    if (result?.error) {
      setError("Email o contraseña incorrectos.");
      setLoading(false);
    } else if (result?.ok) {
      const session = await getSession();
      const role = (session?.user as { role?: string } | undefined)?.role;
      window.location.href = role === "platform_admin" ? "/admin/resumen" : "/resumen";
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
      <form onSubmit={handleSubmit} className="space-y-6" noValidate>
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
            Correo electrónico
          </label>
          <input
            id="login-email"
            name="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="admin@myownclone.com"
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
            Contraseña
          </label>
          <input
            id="login-password"
            name="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="••••••••"
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
          className="btn-primary w-full py-3 text-sm font-semibold disabled:opacity-50"
        >
          {loading ? "Iniciando sesión..." : "Iniciar sesión"}
        </button>
      </form>
    </div>
  );
}
