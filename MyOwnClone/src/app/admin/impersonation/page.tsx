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
import { useTranslations } from "next-intl";

interface ImpersonationEntry {
  id: string;
  admin_id: string;
  admin_email: string | null;
  tenant_id: string;
  tenant_name: string | null;
  started_at: string | null;
  ended_at: string | null;
  reason: string | null;
}

interface Pagination_ {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

interface ImpersonationResponse {
  items: ImpersonationEntry[];
  pagination: Pagination_;
}

function formatDate(iso: string | null) {
  if (!iso) return "—";
  return new Date(iso).toLocaleString("es-ES", {
    dateStyle: "short",
    timeStyle: "medium",
  });
}

export default function AdminImpersonationPage() {
  const t = useTranslations("admin");
  const [pagination, setPagination] = useState<Pagination_>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [search, setSearch] = useState("");

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (search) params.set("search", search);
    return params.toString();
  }, [pagination.page, pagination.limit, search]);

  const { data, loading, error, reload } = useAdminFetch<ImpersonationResponse>(
    `/api/admin/impersonation?${queryString}`,
  );

  const items = data?.items ?? [];
  const serverPagination = data?.pagination;
  const total = serverPagination?.total ?? 0;

  function resetPage() {
    setPagination((p) => ({ ...p, page: 1 }));
  }

  return (
    <div className="space-y-6">
      <PageHeader
        title={t("admin.impersonation.title")}
        subtitle={`${total} impersonation sessions recorded`}
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
            placeholder={t("admin.impersonation.searchPlaceholder")}
            className={fieldControlClass}
          />
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title="Error cargando impersonation log"
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
        <LoadingState label="Loading sessions..." rows={6} />
      ) : items.length === 0 ? (
        <EmptyState
          title={t("admin.impersonation.noSessions")}
          description="Impersonation sessions started by admins will appear here."
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">{t("admin.shell.breadcrumbAdmin")}</th>
                  <th className="px-4 py-2.5 text-left">{t("admin.common.tenant")}</th>
                  <th className="px-4 py-2.5 text-left">Inicio</th>
                  <th className="px-4 py-2.5 text-left">Fin</th>
                  <th className="px-4 py-2.5 text-left">{t("admin.reason")}</th>
                </tr>
              </thead>
              <tbody>
                {items.map((row) => (
                  <tr key={row.id} className="table-row">
                    <td className="px-4 py-3 text-[var(--text-secondary)]">
                      {row.admin_email ?? row.admin_id.slice(0, 8) + "…"}
                    </td>
                    <td className="px-4 py-3">
                      <span className="font-medium text-[var(--text-primary)]">
                        {row.tenant_name ?? row.tenant_id.slice(0, 8) + "…"}
                      </span>
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {formatDate(row.started_at)}
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {formatDate(row.ended_at)}
                    </td>
                    <td className="px-4 py-3 text-[var(--text-secondary)]">
                      {row.reason ?? "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <ul className="space-y-2 md:hidden">
            {items.map((row) => (
              <li key={row.id} className="card flex flex-col gap-2 py-3">
                <div className="flex items-center justify-between">
                  <span className="font-medium text-[var(--text-primary)]">
                    {row.tenant_name ?? "Tenant " + row.tenant_id.slice(0, 8)}
                  </span>
                  <span className="badge-warning text-[10px]">
                    {row.ended_at ? "Finalizada" : "Activa"}
                  </span>
                </div>
                <p className="text-xs text-[var(--text-secondary)]">
                  Admin: {row.admin_email ?? row.admin_id.slice(0, 8) + "…"}
                </p>
                {row.reason && (
                  <p className="text-xs text-[var(--text-muted)]">{row.reason}</p>
                )}
                <div className="flex justify-between text-[10px] text-[var(--text-muted)] font-mono">
                  <span>Inicio: {formatDate(row.started_at)}</span>
                  <span>Fin: {formatDate(row.ended_at)}</span>
                </div>
              </li>
            ))}
          </ul>
        </>
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
