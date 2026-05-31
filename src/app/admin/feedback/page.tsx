"use client";

import { useState, useEffect } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";

interface FeedbackEntry {
  id: string;
  message: string;
  rating?: number;
  userId?: string;
  createdAt: string;
}

export default function AdminFeedbackPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [feedback, setFeedback] = useState<FeedbackEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [search, setSearch] = useState("");

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login");
  }, [status, router]);

  useEffect(() => {
    if (status !== "authenticated") return;

    async function fetchFeedback() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch("/api/admin/feedback");
        if (!res.ok) throw new Error(`Error ${res.status}`);
        const data = await res.json();
        setFeedback(Array.isArray(data) ? data : data.feedback || []);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : "Error al cargar el feedback"
        );
      } finally {
        setLoading(false);
      }
    }

    fetchFeedback();
  }, [status]);

  const filtered = feedback.filter((f) =>
    f.message.toLowerCase().includes(search.toLowerCase())
  );

  if (status === "loading" || loading) {
    return (
      <div className="p-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-8">
          Feedback de Plataforma
        </h1>
        <div className="flex h-64 items-center justify-center">
          <div className="flex gap-1">
            <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600" />
            <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:150ms]" />
            <span className="h-2 w-2 animate-bounce rounded-full bg-purple-600 [animation-delay:300ms]" />
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-8">
          Feedback de Plataforma
        </h1>
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-red-200 dark:border-red-800 p-6">
          <div className="text-center py-12">
            <p className="text-red-600 dark:text-red-400 font-medium">
              Error al cargar el feedback
            </p>
            <p className="mt-1 text-sm text-gray-500">{error}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-8">
        Feedback de Plataforma
      </h1>

      {feedback.length === 0 ? (
        <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
          <div className="text-center py-12">
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center">
              <svg
                className="w-8 h-8 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"
                />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              No hay feedback todavía
            </h3>
            <p className="mt-2 text-gray-500 dark:text-gray-400">
              El feedback de los usuarios aparecerá aquí.
            </p>
          </div>
        </div>
      ) : (
        <>
          <div className="mb-4">
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Buscar feedback..."
              className="w-full max-w-md px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white text-sm focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none"
            />
          </div>

          <div className="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 overflow-hidden">
            <table className="w-full">
              <thead>
                <tr className="border-b border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-gray-900">
                  <th className="text-left px-4 py-3 text-xs font-medium text-gray-500 uppercase">
                    Mensaje
                  </th>
                  <th className="text-left px-4 py-3 text-xs font-medium text-gray-500 uppercase">
                    Rating
                  </th>
                  <th className="text-left px-4 py-3 text-xs font-medium text-gray-500 uppercase">
                    Fecha
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200 dark:divide-gray-800">
                {filtered.map((entry) => (
                  <tr key={entry.id}>
                    <td className="px-4 py-3 text-sm text-gray-700 dark:text-gray-300 max-w-md truncate">
                      {entry.message}
                    </td>
                    <td className="px-4 py-3 text-sm text-gray-700 dark:text-gray-300">
                      {entry.rating !== undefined
                        ? `${entry.rating}/5`
                        : "—"}
                    </td>
                    <td className="px-4 py-3 text-sm text-gray-500">
                      {new Date(entry.createdAt).toLocaleDateString("es-ES", {
                        year: "numeric",
                        month: "short",
                        day: "numeric",
                      })}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            {filtered.length === 0 && search && (
              <div className="text-center py-8 text-sm text-gray-500">
                No se encontraron resultados para &quot;{search}&quot;
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}
