"use client";

import { useState, useEffect } from "react";

export function LoginForm() {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [csrfToken, setCsrfToken] = useState("");

  // Fetch CSRF token on mount
  useEffect(() => {
    fetch("/api/auth/csrf", { credentials: "include" })
      .then((r) => r.json())
      .then((data) => setCsrfToken(data.csrfToken))
      .catch(() => {});
  }, []);

  function handleSubmit(e: React.FormEvent) {
    if (!csrfToken) {
      e.preventDefault();
      return;
    }
    setLoading(true);
    // Use native form submission — the browser handles redirect + cookies
  }

  return (
    <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-lg p-8">
      <form
        method="POST"
        action="/api/auth/callback/credentials?callbackUrl=%2Fresumen"
        onSubmit={handleSubmit}
        className="space-y-6"
      >
        <input type="hidden" name="csrfToken" value={csrfToken} />
        <input type="hidden" name="json" value="true" />
        <div>
          <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
            Correo electrónico
          </label>
          <input
            id="email"
            name="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="admin@myownclone.com"
            required
            className="w-full px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition-colors"
          />
        </div>
        <button
          type="submit"
          disabled={loading || !csrfToken}
          className="w-full py-3 px-4 text-white font-semibold bg-purple-600 hover:bg-purple-700 disabled:opacity-50 rounded-xl transition-colors"
        >
          {loading ? "Iniciando sesión..." : "Iniciar sesión"}
        </button>
      </form>

      <div className="mt-6 text-center text-sm text-gray-500">
        <p>Desarrollo: ingresa cualquier email para acceder</p>
      </div>
    </div>
  );
}
