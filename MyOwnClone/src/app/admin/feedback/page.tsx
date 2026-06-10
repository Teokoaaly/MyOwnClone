"use client";

import { useMemo, useState } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { EmptyState } from "@/components/ui/EmptyState";
import { PageHeader } from "@/components/admin/PageHeader";
import { Field, fieldControlClass } from "@/components/admin/Field";
import { FilterBar } from "@/components/admin/FilterBar";
import { Pagination } from "@/components/admin/Pagination";
import { useAdminFetch } from "@/components/admin/useAdminFetch";

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

interface Pagination_ {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

interface FeedbackResponse {
  items: AdminFeedback[];
  pagination: Pagination_;
}

const RATING_OPTIONS = [
  { value: "", label: "Todas" },
  { value: "up", label: "Positivas" },
  { value: "down", label: "Negativas" },
];

export default function AdminFeedbackPage() {
  const [pagination, setPagination] = useState<Pagination_>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
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

  const { data, loading, error, reload } = useAdminFetch<FeedbackResponse>(
    `/api/admin/feedback?${queryString}`,
  );

  const feedback = data?.items ?? [];
  const serverPagination = data?.pagination;
  const total = serverPagination?.total ?? 0;

  function resetPage() {
    setPagination((p) => ({ ...p, page: 1 }));
  }

  return (
    <div className="space-y-6">
      <PageHeader
        title="Feedback de plataforma"
        subtitle={`${total} respuestas de los usuarios`}
      />

      <FilterBar>
        <Field label="Search" fill>
          <input
            type="text"
            value={search}
            onChange={(e) => {
              resetPage();
              setSearch(e.target.value);
            }}
            placeholder="Comentario o nombre de clon…"
            className={fieldControlClass}
          />
        </Field>
        <Field label="Valoración">
          <select
            value={rating}
            onChange={(e) => {
              resetPage();
              setRating(e.target.value);
            }}
            className={fieldControlClass}
          >
            {RATING_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title="Error cargando feedback"
          message={error}
          action={
            <button
              type="button"
              onClick={reload}
              className="btn-secondary text-xs"
            >
              Reintentar
            </button>
          }
        />
      ) : loading ? (
        <LoadingState label="Loading feedback..." rows={4} />
      ) : feedback.length === 0 ? (
        <EmptyState
          title="No feedback yet"
          description="Las respuestas de los usuarios aparecerán aquí."
        />
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
                    {f.comment ?? (
                      <em className="text-[var(--text-faint)]">
                        (sin comentario)
                      </em>
                    )}
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

      {serverPagination && (
        <Pagination
          page={serverPagination.page}
          pages={serverPagination.pages}
          onPrev={() =>
            setPagination((p) => ({ ...p, page: Math.max(1, p.page - 1) }))
          }
          onNext={() => setPagination((p) => ({ ...p, page: p.page + 1 }))}
        />
      )}
    </div>
  );
}
