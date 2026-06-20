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

interface CourtesyEntry {
  id: string;
  tenant_id: string;
  tenant_name: string | null;
  granted_by: string | null;
  amount_cents: number;
  reason: string | null;
  created_at: string | null;
}

interface Pagination_ {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

interface CourtesyResponse {
  items: CourtesyEntry[];
  pagination: Pagination_;
}

function formatEur(cents: number) {
  return `${(cents / 100).toFixed(2)}€`;
}

function formatDate(iso: string | null) {
  if (!iso) return "—";
  return new Date(iso).toLocaleString("es-ES", {
    dateStyle: "short",
    timeStyle: "medium",
  });
}

export default function AdminCourtesyPage() {
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

  const { data, loading, error, reload } = useAdminFetch<CourtesyResponse>(
    `/api/admin/courtesy?${queryString}`,
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
        title={t("courtesy.title")}
        subtitle={`${total} courtesy credits granted`}
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
            placeholder={t("courtesy.searchPlaceholder")}
            className={fieldControlClass}
          />
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title="Error cargando courtesy credits"
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
        <LoadingState label="Loading credits..." rows={6} />
      ) : items.length === 0 ? (
        <EmptyState
          title={t("courtesy.noCredits")}
          description="Courtesy credits granted to tenants will appear here."
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">{t("common.tenant")}</th>
                  <th className="px-4 py-2.5 text-right">Importe</th>
                  <th className="px-4 py-2.5 text-left">Otorgado por</th>
                  <th className="px-4 py-2.5 text-left">{t("reason")}</th>
                  <th className="px-4 py-2.5 text-left">Fecha</th>
                </tr>
              </thead>
              <tbody>
                {items.map((row) => (
                  <tr key={row.id} className="table-row">
                    <td className="px-4 py-3">
                      <span className="font-medium text-[var(--text-primary)]">
                        {row.tenant_name ?? row.tenant_id.slice(0, 8) + "…"}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-[var(--color-accent-green)]">
                      +{formatEur(row.amount_cents)}
                    </td>
                    <td className="px-4 py-3 text-[var(--text-secondary)]">
                      {row.granted_by ?? "—"}
                    </td>
                    <td className="px-4 py-3 text-[var(--text-secondary)]">
                      {row.reason ?? "—"}
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {formatDate(row.created_at)}
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
                  <span className="font-mono text-sm text-[var(--color-accent-green)]">
                    +{formatEur(row.amount_cents)}
                  </span>
                </div>
                {row.reason && (
                  <p className="text-xs text-[var(--text-secondary)]">
                    {row.reason}
                  </p>
                )}
                <div className="flex justify-between text-[10px] text-[var(--text-muted)]">
                  <span>{row.granted_by ?? "—"}</span>
                  <span>{formatDate(row.created_at)}</span>
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
