"use client";

export const dynamic = "force-dynamic"

import { useState } from "react";
import { signIn } from "next-auth/react";
import { useRouter } from "@/i18n/navigation";

export function SignupForm() {
  const router = useRouter();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [sent, setSent] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const result = await signIn("resend", {
        email,
        name,
        redirect: false,
        callbackUrl: "/resumen",
      });

      if (result?.error) {
        setError("Error sending the link. Try again.");
      } else {
        setSent(true);
      }
    } catch {
      setError("Connection error. Try again.");
    } finally {
      setLoading(false);
    }
  }

  if (sent) {
    return (
      <div
        className="rounded-2xl p-8 text-center"
        style={{
          background: "var(--bg-shell)",
          boxShadow:
            "0 1px 2px rgba(15, 23, 42, 0.04), 0 24px 64px rgba(15, 23, 42, 0.10)",
        }}
      >
        <div
          className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full"
          style={{ background: "var(--surface-2)" }}
        >
          <svg
            aria-hidden="true"
            className="h-8 w-8"
            style={{ color: "var(--color-accent-violet)" }}
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
            />
          </svg>
        </div>
        <h2 className="text-xl font-semibold text-[var(--text-primary)]">
          Check your email
        </h2>
        <p className="mt-2 text-[var(--text-secondary)]">
          We sent a sign-in link to{" "}
          <strong className="text-[var(--text-primary)]">{email}</strong>
        </p>
        <p className="mt-4 text-sm text-[var(--text-muted)]">
          Click the link in the email to activate your account automatically.
        </p>
      </div>
    );
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
              color: "var(--text-primary)",
              border: "1px solid var(--color-accent-pink)",
            }}
          >
            {error}
          </div>
        )}
        <div>
          <label
            htmlFor="register-name"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            Full name
          </label>
          <input
            id="register-name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Your name"
            required
            autoComplete="name"
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
            htmlFor="register-email"
            className="mb-1 block text-sm font-medium text-[var(--text-primary)]"
          >
            Email address
          </label>
          <input
            id="register-email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="you@email.com"
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
        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-xl px-4 py-3 font-semibold text-white transition disabled:opacity-50"
          style={{ background: "var(--color-accent-violet)" }}
        >
          {loading ? "Sending..." : "Create account"}
        </button>
      </form>

      <div className="mt-6">
        <div className="relative">
          <div className="absolute inset-0 flex items-center">
            <div
              className="w-full border-t"
              style={{ borderColor: "var(--border-soft)" }}
            />
          </div>
          <div className="relative flex justify-center text-sm">
            <span
              className="px-2 text-[var(--text-muted)]"
              style={{ background: "var(--bg-shell)" }}
            >
              or continue with
            </span>
          </div>
        </div>
        <button
          type="button"
          onClick={() => signIn("google", { callbackUrl: "/resumen" })}
          aria-label="Continue with Google"
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
          Continue with Google
        </button>
      </div>

      <p className="mt-6 text-center text-sm text-[var(--text-muted)]">
        Already have an account?{" "}
        <button
          type="button"
          onClick={() => router.push("/login")}
          className="font-medium underline decoration-[var(--color-accent-violet)] underline-offset-4 hover:opacity-80"
          style={{ color: "var(--text-primary)" }}
        >
          Sign in
        </button>
      </p>
    </div>
  );
}
