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

interface AuditEntry {
  id: string;
  actor_id: string;
  action: string;
  target_type: string | null;
  target_id: string | null;
  reason: string | null;
  metadata: Record<string, unknown> | null;
  ip_address: string | null;
  user_agent: string | null;
  created_at: string | null;
}

interface Pagination_ {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

interface AuditResponse {
  items: AuditEntry[];
  pagination: Pagination_;
}

const ACTION_OPTIONS = [
  { value: "", label: "Todas las acciones" },
  { value: "impersonation_started", label: "Impersonation started" },
  { value: "impersonation_stopped", label: "Impersonation stopped" },
  { value: "tenant_updated", label: "Tenant updated" },
  { value: "tenant_created", label: "Tenant created" },
];

function actionBadge(action: string) {
  if (action.startsWith("impersonation_started")) return "badge-warning";
  if (action.startsWith("impersonation_stopped")) return "badge-active";
  if (action.startsWith("tenant_updated")) return "badge-trial";
  if (action.startsWith("tenant_created")) return "badge-violet";
  return "badge-trial";
}

function formatDate(iso: string | null) {
  if (!iso) return "—";
  return new Date(iso).toLocaleString("es-ES", {
    dateStyle: "short",
    timeStyle: "medium",
  });
}

function formatMetadata(meta: Record<string, unknown> | null) {
  if (!meta) return "—";
  try {
    return JSON.stringify(meta);
  } catch {
    return "—";
  }
}

export default function AdminAuditPage() {
  const t = useTranslations("admin");
  const [pagination, setPagination] = useState<Pagination_>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [action, setAction] = useState("");
  const [actor, setActor] = useState("");
  const [target, setTarget] = useState("");

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (action) params.set("action", action);
    if (actor) params.set("actor_id", actor);
    if (target) params.set("target_id", target);
    return params.toString();
  }, [pagination.page, pagination.limit, action, actor, target]);

  const { data, loading, error, reload } = useAdminFetch<AuditResponse>(
    `/api/admin/audit-log?${queryString}`,
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
        title={t("audit_log")}
        subtitle={`${total} acciones registradas en la plataforma`}
      />

      <FilterBar>
        <Field label="Acción" fill>
          <select
            value={action}
            onChange={(e) => {
              resetPage();
              setAction(e.target.value);
            }}
            className={fieldControlClass}
          >
            {ACTION_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </Field>
        <Field label="Actor ID">
          <input
            type="text"
            value={actor}
            onChange={(e) => {
              resetPage();
              setActor(e.target.value);
            }}
            placeholder="uuid…"
            className={fieldControlClass}
          />
        </Field>
        <Field label="Target ID">
          <input
            type="text"
            value={target}
            onChange={(e) => {
              resetPage();
              setTarget(e.target.value);
            }}
            placeholder="uuid…"
            className={fieldControlClass}
          />
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title="Error cargando audit log"
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
        <LoadingState label="Loading audit log..." rows={6} />
      ) : items.length === 0 ? (
        <EmptyState
          title={t("no_entries")}
          description="Las acciones sensibles (impersonaciones, cambios de plan, cambios de estado, signups courtesy) aparecerán aquí."
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">Fecha</th>
                  <th className="px-4 py-2.5 text-left">Acción</th>
                  <th className="px-4 py-2.5 text-left">{t("actor")}</th>
                  <th className="px-4 py-2.5 text-left">{t("target")}</th>
                  <th className="px-4 py-2.5 text-left">{t("reason")}</th>
                  <th className="px-4 py-2.5 text-left">{t("metadata")}</th>
                </tr>
              </thead>
              <tbody>
                {items.map((row) => (
                  <tr key={row.id} className="table-row">
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {formatDate(row.created_at)}
                    </td>
                    <td className="px-4 py-3">
                      <span className={actionBadge(row.action)}>
                        {row.action}
                      </span>
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-secondary)]">
                      {row.actor_id.slice(0, 8)}…
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-secondary)]">
                      {row.target_id
                        ? `${row.target_type ?? ""} ${row.target_id.slice(0, 8)}…`
                        : "—"}
                    </td>
                    <td className="px-4 py-3 text-[var(--text-secondary)]">
                      {row.reason ?? "—"}
                    </td>
                    <td className="px-4 py-3 max-w-[200px] truncate font-mono text-[10px] text-[var(--text-muted)]">
                      {formatMetadata(row.metadata)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <ul className="space-y-2 md:hidden">
            {items.map((row) => (
              <li
                key={row.id}
                className="card flex flex-col gap-2 py-3"
              >
                <div className="flex items-center justify-between">
                  <span className={actionBadge(row.action)}>{row.action}</span>
                  <span className="font-mono text-[10px] text-[var(--text-muted)]">
                    {formatDate(row.created_at)}
                  </span>
                </div>
                {row.reason && (
                  <p className="text-xs text-[var(--text-secondary)]">
                    {row.reason}
                  </p>
                )}
                <div className="flex justify-between font-mono text-[10px] text-[var(--text-muted)]">
                  <span>actor: {row.actor_id.slice(0, 8)}…</span>
                  {row.target_id && (
                    <span>
                      {row.target_type}: {row.target_id.slice(0, 8)}…
                    </span>
                  )}
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
