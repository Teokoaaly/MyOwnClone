"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

interface AdminTenant {
  id: string;
  slug: string | null;
  name: string;
  plan: string | null;
  status: string | null;
  subscription_status: string | null;
  clone_count: number;
  monthly_cost_cents: number;
  created_at: string | null;
  updated_at: string | null;
}

interface Pagination {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

const PLAN_OPTIONS = [
  { value: "", label: "Todos los planes" },
  { value: "trial", label: "Trial" },
  { value: "basic", label: "Básico" },
  { value: "pro", label: "Pro" },
  { value: "scale", label: "Escala" },
  { value: "enterprise", label: "Enterprise" },
];

const STATUS_OPTIONS = [
  { value: "", label: "Todos los estados" },
  { value: "active", label: "Active" },
  { value: "trial", label: "Trial" },
  { value: "suspended", label: "Suspended" },
  { value: "cancelled", label: "Cancelled" },
];

function statusBadge(status: string | null) {
  switch ((status ?? "").toLowerCase()) {
    case "active":
    case "normal":
      return "badge-active";
    case "trial":
      return "badge-trial";
    case "suspended":
    case "warning":
      return "badge-warning";
    case "cancelled":
    case "error":
      return "badge-error";
    default:
      return "badge-trial";
  }
}

export default function AdminTenantsPage() {
  const router = useRouter();
  const [tenants, setTenants] = useState<AdminTenant[]>([]);
  const [pagination, setPagination] = useState<Pagination>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [plan, setPlan] = useState("");
  const [status, setStatus] = useState("");
  const [error, setError] = useState<string | null>(null);

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (search) params.set("search", search);
    if (plan) params.set("plan", plan);
    if (status) params.set("status", status);
    return params.toString();
  }, [pagination.page, pagination.limit, search, plan, status]);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(`/api/admin/tenants?${queryString}`, { cache: "no-store" })
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
        setTenants(data.items ?? []);
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

  function changePage(p: number) {
    setPagination((prev) => ({ ...prev, page: p }));
  }

  return (
    <div className="space-y-6">
      <header className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
            Tenants
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            {pagination.total} cuentas en la plataforma
          </p>
        </div>
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
            placeholder="Nombre o slug…"
            className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
          />
        </div>
        <div>
          <label className="stat-label">Plan</label>
          <select
            value={plan}
            onChange={(e) => {
              setPagination((p) => ({ ...p, page: 1 }));
              setPlan(e.target.value);
            }}
            className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
          >
            {PLAN_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label className="stat-label">Estado</label>
          <select
            value={status}
            onChange={(e) => {
              setPagination((p) => ({ ...p, page: 1 }));
              setStatus(e.target.value);
            }}
            className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
          >
            {STATUS_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {error ? (
        <div className="card border-red-200 bg-red-50/40">
          <p className="text-sm font-medium text-red-700">Error cargando tenants</p>
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
      ) : tenants.length === 0 ? (
        <div className="card text-center text-sm text-[var(--text-muted)]">
          No se encontraron tenants con esos filtros.
        </div>
      ) : (
        <div className="card overflow-hidden p-0">
          <table className="w-full text-sm">
            <thead className="table-header">
              <tr>
                <th className="px-4 py-2.5 text-left">Tenant</th>
                <th className="px-4 py-2.5 text-left">Plan</th>
                <th className="px-4 py-2.5 text-left">Estado</th>
                <th className="px-4 py-2.5 text-right">Clones</th>
                <th className="px-4 py-2.5 text-right">Costes 30d</th>
                <th className="px-4 py-2.5 text-left">Creado</th>
              </tr>
            </thead>
            <tbody>
              {tenants.map((t) => (
                <tr key={t.id} className="table-row">
                  <td className="px-4 py-3">
                    <Link
                      href={`/admin/tenants/${t.id}`}
                      className="font-medium text-[var(--text-primary)] hover:text-[var(--color-accent-warm)]"
                    >
                      {t.name}
                    </Link>
                    {t.slug && (
                      <div className="text-xs text-[var(--text-muted)]">
                        {t.slug}
                      </div>
                    )}
                  </td>
                  <td className="px-4 py-3 text-[var(--text-secondary)] capitalize">
                    {t.plan ?? "—"}
                  </td>
                  <td className="px-4 py-3">
                    <span className={statusBadge(t.status)}>
                      {t.status ?? "—"}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-right font-mono text-[var(--text-primary)]">
                    {t.clone_count}
                  </td>
                  <td className="px-4 py-3 text-right font-mono text-[var(--text-primary)]">
                    {t.monthly_cost_cents}¢
                  </td>
                  <td className="px-4 py-3 text-xs text-[var(--text-muted)]">
                    {t.created_at
                      ? new Date(t.created_at).toLocaleDateString("es-ES")
                      : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {pagination.pages > 1 && (
        <div className="flex items-center justify-between text-xs text-[var(--text-muted)]">
          <span>
            Página {pagination.page} de {pagination.pages}
          </span>
          <div className="flex gap-2">
            <button
              type="button"
              disabled={pagination.page <= 1}
              onClick={() => changePage(pagination.page - 1)}
              className="btn-secondary text-xs disabled:opacity-40"
            >
              ← Anterior
            </button>
            <button
              type="button"
              disabled={pagination.page >= pagination.pages}
              onClick={() => changePage(pagination.page + 1)}
              className="btn-secondary text-xs disabled:opacity-40"
            >
              Siguiente →
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
