"use client";

import { useState } from "react";
import { getSession, signIn } from "next-auth/react";
import { Link, useRouter } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

export function LoginForm() {
  const t = useTranslations("auth");
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

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
        setError("Invalid email or password.");
        setLoading(false);
        return;
      }

      const session = await getSession();
      const role = (session?.user as { role?: string } | undefined)?.role;
      router.replace(role === "platform_admin" ? "/admin/resumen" : "/resumen");
    } catch {
      setError("Connection error. Try again.");
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-5" noValidate>
      {error && (
        <div
          role="alert"
          className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700"
        >
          {error}
        </div>
      )}

      {/* Email */}
      <div>
        <label
          htmlFor="login-email"
          className="mb-1.5 block text-sm font-medium text-stone-700"
        >
          Email address
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
          className="w-full rounded-xl border border-stone-200 bg-stone-50 px-4 py-3 text-sm text-stone-900 placeholder:text-stone-400 outline-none transition focus:border-orange-400 focus:ring-2 focus:ring-orange-100"
        />
      </div>

      {/* Password */}
      <div>
        <label
          htmlFor="login-password"
          className="mb-1.5 block text-sm font-medium text-stone-700"
        >
          Password
        </label>
        <input
          id="login-password"
          name="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;"
          required
          autoComplete="current-password"
          className="w-full rounded-xl border border-stone-200 bg-stone-50 px-4 py-3 text-sm text-stone-900 placeholder:text-stone-400 outline-none transition focus:border-orange-400 focus:ring-2 focus:ring-orange-100"
        />
      </div>

      {/* Submit */}
      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-xl bg-stone-900 py-3 text-sm font-semibold text-white transition-all hover:bg-stone-800 disabled:opacity-50 active:scale-[0.98]"
      >
        {loading ? "Signing in..." : "Sign in"}
      </button>

      {/* Divider */}
      <div className="relative">
        <div className="absolute inset-0 flex items-center">
          <div className="w-full border-t border-stone-200" />
        </div>
        <div className="relative flex justify-center text-sm">
          <span className="bg-white px-3 text-stone-400">
            or continue with
          </span>
        </div>
      </div>

      {/* Google */}
      <button
        type="button"
        onClick={() => signIn("google", { callbackUrl: "/resumen" })}
        aria-label={t("continue_with_google")}
        className="flex w-full items-center justify-center gap-3 rounded-xl border border-stone-200 bg-white py-3 text-sm font-semibold text-stone-700 transition hover:bg-stone-50 active:scale-[0.98]"
      >
        <svg className="h-5 w-5" viewBox="0 0 24 24" aria-hidden="true">
          <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" />
          <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
          <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
          <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
        </svg>
        Continue with Google
      </button>

      {/* Forgot password */}
      <p className="text-center text-sm">
        <Link
          href="/forgot-password"
          className="font-medium text-stone-500 underline underline-offset-4 hover:text-stone-700"
        >
          Forgot your password?
        </Link>
      </p>
    </form>
  );
}
