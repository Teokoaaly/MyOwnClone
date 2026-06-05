"use client";

import { useEffect, useState } from "react";
import { useRouter, useParams } from "next/navigation";
import Link from "next/link";

interface TenantDetail {
  tenant: {
    id: string;
    slug: string | null;
    name: string;
    plan: string | null;
    status: string | null;
    subscription_status: string | null;
    stripe_customer_id: string | null;
    stripe_subscription_id: string | null;
    created_at: string | null;
    updated_at: string | null;
  };
  usage: {
    clone_count: number;
    cost_cents_30d: number;
    tokens_in_30d: number;
    tokens_out_30d: number;
    questions_30d: number;
    gaps_open: number;
  };
  clones: Array<{
    id: string;
    name: string;
    slug: string;
    is_active: boolean;
    language: string | null;
    created_at: string | null;
  }>;
}

function statusBadge(status: string | null) {
  switch ((status ?? "").toLowerCase()) {
    case "active":
    case "normal":
      return "badge-active";
    case "trial":
      return "badge-trial";
    case "suspended":
      return "badge-warning";
    case "cancelled":
      return "badge-error";
    default:
      return "badge-trial";
  }
}

export default function AdminTenantDetailPage() {
  const router = useRouter();
  const params = useParams<{ id: string }>();
  const id = params?.id;
  const [data, setData] = useState<TenantDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(`/api/admin/tenants/${id}`, { cache: "no-store" })
      .then((res) => {
        if (res.status === 401) {
          router.push("/login");
          return null;
        }
        if (res.status === 404) {
          throw new Error("Tenant no encontrado");
        }
        if (!res.ok) throw new Error(`Backend error ${res.status}`);
        return res.json();
      })
      .then((payload) => {
        if (!payload || cancelled) return;
        setData(payload as TenantDetail);
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
  }, [id, router]);

  if (loading) {
    return (
      <div className="card flex h-48 items-center justify-center">
        <div className="flex gap-1">
          <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:150ms]" />
          <span className="h-2 w-2 animate-bounce rounded-full bg-[var(--color-accent-warm)] [animation-delay:300ms]" />
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="card border-red-200 bg-red-50/40">
        <p className="text-sm font-medium text-red-700">No se pudo cargar el tenant</p>
        <p className="mt-1 text-xs text-red-600">{error ?? "Sin datos"}</p>
        <Link
          href="/admin/tenants"
          className="mt-3 inline-block text-xs text-[var(--color-accent-warm)] hover:underline"
        >
          ← Volver al listado
        </Link>
      </div>
    );
  }

  const { tenant, usage, clones } = data;
  const usageRows = [
    { label: "Clones activos", value: usage.clone_count },
    { label: "Costes 30d", value: `${usage.cost_cents_30d}¢` },
    { label: "Tokens input 30d", value: usage.tokens_in_30d },
    { label: "Tokens output 30d", value: usage.tokens_out_30d },
    { label: "Preguntas 30d", value: usage.questions_30d },
    { label: "Gaps abiertos", value: usage.gaps_open },
  ];

  return (
    <div className="space-y-6">
      <header className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <Link
            href="/admin/tenants"
            className="text-xs text-[var(--text-muted)] hover:text-[var(--text-primary)]"
          >
            ← Tenants
          </Link>
          <h1 className="mt-1 text-2xl font-semibold text-[var(--text-primary)]">
            {tenant.name}
          </h1>
          <p className="mt-1 text-sm text-[var(--text-muted)]">
            {tenant.slug ?? "(sin slug)"}
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className={statusBadge(tenant.status)}>{tenant.status ?? "—"}</span>
          <span className="text-xs text-[var(--text-muted)]">
            Plan: <span className="font-medium capitalize">{tenant.plan ?? "—"}</span>
          </span>
        </div>
      </header>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <div className="card lg:col-span-2">
          <h2 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Uso últimos 30 días
          </h2>
          <div className="grid grid-cols-2 gap-4 sm:grid-cols-3">
            {usageRows.map((r) => (
              <div key={r.label}>
                <div className="stat-label">{r.label}</div>
                <div className="stat-value mt-1">{r.value}</div>
              </div>
            ))}
          </div>
        </div>

        <div className="card">
          <h2 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Datos de facturación
          </h2>
          <dl className="space-y-3 text-sm">
            <div>
              <dt className="stat-label">Subscription status</dt>
              <dd className="font-mono text-[var(--text-primary)]">
                {tenant.subscription_status ?? "—"}
              </dd>
            </div>
            <div>
              <dt className="stat-label">Stripe customer</dt>
              <dd className="break-all font-mono text-xs text-[var(--text-primary)]">
                {tenant.stripe_customer_id ?? "—"}
              </dd>
            </div>
            <div>
              <dt className="stat-label">Stripe subscription</dt>
              <dd className="break-all font-mono text-xs text-[var(--text-primary)]">
                {tenant.stripe_subscription_id ?? "—"}
              </dd>
            </div>
            <div>
              <dt className="stat-label">Creado</dt>
              <dd className="text-xs text-[var(--text-secondary)]">
                {tenant.created_at
                  ? new Date(tenant.created_at).toLocaleString("es-ES")
                  : "—"}
              </dd>
            </div>
          </dl>
        </div>
      </div>

      <div className="card overflow-hidden p-0">
        <div className="flex items-center justify-between px-4 py-3">
          <h2 className="text-sm font-semibold text-[var(--text-primary)]">
            Clones ({clones.length})
          </h2>
        </div>
        {clones.length === 0 ? (
          <div className="px-4 pb-6 text-center text-sm text-[var(--text-muted)]">
            Este tenant aún no tiene clones.
          </div>
        ) : (
          <table className="w-full text-sm">
            <thead className="table-header">
              <tr>
                <th className="px-4 py-2.5 text-left">Nombre</th>
                <th className="px-4 py-2.5 text-left">Slug</th>
                <th className="px-4 py-2.5 text-left">Idioma</th>
                <th className="px-4 py-2.5 text-left">Estado</th>
                <th className="px-4 py-2.5 text-left">Creado</th>
              </tr>
            </thead>
            <tbody>
              {clones.map((c) => (
                <tr key={c.id} className="table-row">
                  <td className="px-4 py-3 font-medium text-[var(--text-primary)]">
                    {c.name}
                  </td>
                  <td className="px-4 py-3 text-[var(--text-secondary)]">{c.slug}</td>
                  <td className="px-4 py-3 text-[var(--text-secondary)]">
                    {c.language ?? "es"}
                  </td>
                  <td className="px-4 py-3">
                    {c.is_active ? (
                      <span className="badge-active">Activo</span>
                    ) : (
                      <span className="badge-warning">Inactivo</span>
                    )}
                  </td>
                  <td className="px-4 py-3 text-xs text-[var(--text-muted)]">
                    {c.created_at
                      ? new Date(c.created_at).toLocaleDateString("es-ES")
                      : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
