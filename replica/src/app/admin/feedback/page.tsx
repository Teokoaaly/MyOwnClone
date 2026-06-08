"use client";

import { useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";

interface AdminFeedback {
  id: string;
  clone_id: string;
  clone_name: string | null;
  tenant_id: string | null;
  tenant_name: string | null;
  rating: "up" | "down";
  comment: string | null;
  created_at: string | null;
}

interface Pagination {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

const RATING_OPTIONS = [
  { value: "", label: "Todas" },
  { value: "up", label: "Positivas" },
  { value: "down", label: "Negativas" },
];

export default function AdminFeedbackPage() {
  const router = useRouter();
  const [feedback, setFeedback] = useState<AdminFeedback[]>([]);
  const [pagination, setPagination] = useState<Pagination>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [rating, setRating] = useState("");
  const [search, setSearch] = useState("");

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (rating) params.set("rating", rating);
    if (search) params.set("search", search);
    return params.toString();
  }, [pagination.page, pagination.limit, rating, search]);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(`/api/admin/feedback?${queryString}`, { cache: "no-store" })
      .then((res) => {
        if (res.status === 401) {
          router.push("/login");
          return null;
        }
        if (!res.ok) throw new Error(`Backend error ${res.status}`);
        return res.json();
      })
      .then((data) => {
        if (!data || cancelled) return;
        setFeedback(data.items ?? []);
        setPagination(
          data.pagination ?? { page: 1, limit: 20, total: 0, pages: 0 },
        );
      })
      .catch((err) => {
        if (!cancelled) setError(err.message ?? "Error");
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [queryString, router]);

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Feedback de plataforma
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          {pagination.total} respuestas de los usuarios
        </p>
      </header>

      <div className="card flex flex-col gap-3 sm:flex-row sm:items-end">
        <div className="flex-1">
          <label className="stat-label">Buscar</label>
          <input
            type="text"
            value={search}
            onChange={(e) => {
              setPagination((p) => ({ ...p, page: 1 }));
              setSearch(e.target.value);
            }}
            placeholder="Comentario o nombre de clon…"
            className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
          />
        </div>
        <div>
          <label className="stat-label">Valoración</label>
          <select
            value={rating}
            onChange={(e) => {
              setPagination((p) => ({ ...p, page: 1 }));
              setRating(e.target.value);
            }}
            className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
          >
            {RATING_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {error ? (
        <div className="card border-red-200 bg-red-50/40">
          <p className="text-sm font-medium text-red-700">Error cargando feedback</p>
          <p className="mt-1 text-xs text-red-600">{error}</p>
        </div>
      ) : loading ? (
        <div className="card flex h-48 items-center justify-center">
          <div className="flex gap-1">
            <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)]" />
            <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:150ms]" />
            <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:300ms]" />
          </div>
        </div>
      ) : feedback.length === 0 ? (
        <div className="card text-center">
          <div className="mx-auto mb-3 flex h-12 w-12 items-center justify-center rounded-full bg-[var(--surface-2)]">
            <svg
              className="h-6 w-6 text-[var(--text-muted)]"
            ***REMOVED***ll="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"
              />
            </svg>
          </div>
          <p className="text-sm font-medium text-[var(--text-primary)]">
            Sin feedback todavía
          </p>
          <p className="mt-1 text-xs text-[var(--text-muted)]">
            Las respuestas de los usuarios aparecerán aquí.
          </p>
        </div>
      ) : (
        <div className="card overflow-hidden p-0">
          <table className="w-full text-sm">
            <thead className="table-header">
              <tr>
                <th className="px-4 py-2.5 text-left">Tenant / Clon</th>
                <th className="px-4 py-2.5 text-left">Comentario</th>
                <th className="px-4 py-2.5 text-left">Rating</th>
                <th className="px-4 py-2.5 text-left">Fecha</th>
              </tr>
            </thead>
            <tbody>
              {feedback.map((f) => (
                <tr key={f.id} className="table-row">
                  <td className="px-4 py-3">
                    <div className="font-medium text-[var(--text-primary)]">
                      {f.tenant_name ?? "—"}
                    </div>
                    {f.clone_name && (
                      <div className="text-xs text-[var(--text-muted)]">
                        {f.clone_name}
                      </div>
                    )}
                  </td>
                  <td className="px-4 py-3 text-[var(--text-secondary)]">
                    {f.comment ?? <em className="text-[var(--text-faint)]">(sin comentario)</em>}
                  </td>
                  <td className="px-4 py-3">
                    {f.rating === "up" ? (
                      <span className="badge-active">Positiva</span>
                    ) : (
                      <span className="badge-error">Negativa</span>
                    )}
                  </td>
                  <td className="px-4 py-3 text-xs text-[var(--text-muted)]">
                    {f.created_at
                      ? new Date(f.created_at).toLocaleString("es-ES", {
                          dateStyle: "short",
                          timeStyle: "short",
                        })
                      : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {pagination.pages > 1 && (
        <div className="flex items-center justify-end gap-2 text-xs text-[var(--text-muted)]">
          <button
            type="button"
            disabled={pagination.page <= 1}
            onClick={() => setPagination((p) => ({ ...p, page: p.page - 1 }))}
            className="btn-secondary text-xs disabled:opacity-40"
          >
            ← Anterior
          </button>
          <span>
            {pagination.page} / {pagination.pages}
          </span>
          <button
            type="button"
            disabled={pagination.page >= pagination.pages}
            onClick={() => setPagination((p) => ({ ...p, page: p.page + 1 }))}
            className="btn-secondary text-xs disabled:opacity-40"
          >
            Siguiente →
          </button>
        </div>
      )}
    </div>
  );
}
