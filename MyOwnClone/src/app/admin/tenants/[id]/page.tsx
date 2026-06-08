"use client";

import { useEffect, useState, useCallback, useRef } from "react";
import { useRouter, useParams } from "next/navigation";
import Link from "next/link";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { StatusBadge, statusToKind } from "@/components/ui/StatusBadge";
import { ImpersonateButton } from "@/components/admin/ImpersonateButton";
import { Modal } from "@/components/ui/Modal";
import { PageHeader } from "@/components/admin/PageHeader";
import { Field, fieldControlClass } from "@/components/admin/Field";

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

const PLAN_OPTIONS = [
  { value: "trial", label: "Trial" },
  { value: "basic", label: "Básico" },
  { value: "pro", label: "Pro" },
  { value: "scale", label: "Escala" },
  { value: "enterprise", label: "Enterprise" },
];

const STATUS_OPTIONS = [
  { value: "active", label: "Active" },
  { value: "trial", label: "Trial" },
  { value: "suspended", label: "Suspended" },
  { value: "cancelled", label: "Cancelled" },
];

function formatEur(cents: number) {
  return `${(cents / 100).toFixed(2)}€`;
}

export default function AdminTenantDetailPage() {
  const router = useRouter();
  const params = useParams<{ id: string }>();
  const id = params?.id;
  const [data, setData] = useState<TenantDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // PATCH state
  const [patchOpen, setPatchOpen] = useState(false);
  const [patchPlan, setPatchPlan] = useState("");
  const [patchStatus, setPatchStatus] = useState("");
  const [patchSubmitting, setPatchSubmitting] = useState(false);
  const [patchError, setPatchError] = useState<string | null>(null);

  const cancelledRef = useRef(false);

  const fetchDetail = useCallback(async () => {
    if (!id) return;
    cancelledRef.current = false;
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`/api/admin/tenants/${id}`, {
        cache: "no-store",
      });
      if (res.status === 401 || res.status === 403) {
        router.push("/login");
        return;
      }
      if (res.status === 404) {
        throw new Error("Tenant no encontrado");
      }
      if (!res.ok) throw new Error(`Backend error ${res.status}`);
      const payload = (await res.json()) as TenantDetail;
      if (!cancelledRef.current) {
        setData(payload);
        setPatchPlan(payload.tenant.plan ?? "");
        setPatchStatus(payload.tenant.status ?? "");
      }
    } catch (err) {
      if (!cancelledRef.current) setError(err instanceof Error ? err.message : "Error");
    } finally {
      if (!cancelledRef.current) setLoading(false);
    }
  }, [id, router]);

  useEffect(() => {
    fetchDetail();
    return () => {
      cancelledRef.current = true;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [fetchDetail]);

  async function submitPatch() {
    if (!id) return;
    if (!patchPlan && !patchStatus) return;
    setPatchSubmitting(true);
    setPatchError(null);
    try {
      const body: { plan?: string; status?: string } = {};
      if (patchPlan) body.plan = patchPlan;
      if (patchStatus) body.status = patchStatus;
      const res = await fetch(`/api/admin/tenants/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      if (!res.ok) {
        const payload = await res.json().catch(() => ({}));
        throw new Error(payload.message ?? `Error ${res.status}`);
      }
      setPatchOpen(false);
      await fetchDetail();
    } catch (e) {
      setPatchError(e instanceof Error ? e.message : "Error");
    } finally {
      setPatchSubmitting(false);
    }
  }

  if (loading) {
    return <LoadingState label="Cargando tenant…" rows={4} />;
  }

  if (error || !data) {
    return (
      <ErrorState
        title="No se pudo cargar el tenant"
        message={error ?? "Sin datos"}
        action={
          <Link href="/admin/tenants" className="btn-secondary text-xs">
            ← Volver al listado
          </Link>
        }
      />
    );
  }

  const { tenant, usage, clones } = data;
  const usageRows = [
    { label: "Clones activos", value: usage.clone_count.toString() },
    { label: "Costes 30d", value: formatEur(usage.cost_cents_30d) },
    {
      label: "Tokens input 30d",
      value: usage.tokens_in_30d.toLocaleString("es-ES"),
    },
    {
      label: "Tokens output 30d",
      value: usage.tokens_out_30d.toLocaleString("es-ES"),
    },
    { label: "Preguntas 30d", value: usage.questions_30d.toLocaleString("es-ES") },
    { label: "Gaps abiertos", value: usage.gaps_open.toLocaleString("es-ES") },
  ];

  return (
    <div className="space-y-6">
      <PageHeader
        title={tenant.name}
        subtitle={
          <>
            <Link
              href="/admin/tenants"
              className="text-xs text-[var(--text-muted)] hover:text-[var(--text-primary)]"
            >
              ← Tenants
            </Link>
            <span className="mt-1 block">{tenant.slug ?? "(sin slug)"}</span>
          </>
        }
        actions={
          <>
            <StatusBadge
              kind={statusToKind(tenant.status)}
              label={tenant.status ?? "—"}
            />
            <span className="text-xs text-[var(--text-muted)]">
              Plan:{" "}
              <span className="font-medium capitalize text-[var(--text-primary)]">
                {tenant.plan ?? "—"}
              </span>
            </span>
            <button
              type="button"
              onClick={() => setPatchOpen(true)}
              className="btn-secondary text-xs"
            >
              Cambiar plan / estado
            </button>
            <ImpersonateButton tenantId={tenant.id} tenantName={tenant.name} />
          </>
        }
      />

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
                  <td className="px-4 py-3 text-[var(--text-secondary)]">
                    {c.slug}
                  </td>
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

      <Modal
        open={patchOpen}
        onClose={() => setPatchOpen(false)}
        title={`Editar ${tenant.name}`}
        size="sm"
        footer={
          <>
            <button
              type="button"
              onClick={() => setPatchOpen(false)}
              className="btn-secondary text-xs"
              disabled={patchSubmitting}
            >
              Cancelar
            </button>
            <button
              type="button"
              onClick={submitPatch}
              className="btn-primary text-xs disabled:opacity-40"
              disabled={patchSubmitting || (!patchPlan && !patchStatus)}
            >
              {patchSubmitting ? "Guardando…" : "Guardar cambios"}
            </button>
          </>
        }
      >
        <div className="space-y-3">
          <p className="text-xs text-[var(--text-muted)]">
            Esta acción queda registrada en el audit log.
          </p>
          <Field label="Plan">
            <select
              value={patchPlan}
              onChange={(e) => setPatchPlan(e.target.value)}
              className={fieldControlClass}
            >
              <option value="">(sin cambios)</option>
              {PLAN_OPTIONS.map((o) => (
                <option key={o.value} value={o.value}>
                  {o.label}
                </option>
              ))}
            </select>
          </Field>
          <Field label="Estado">
            <select
              value={patchStatus}
              onChange={(e) => setPatchStatus(e.target.value)}
              className={fieldControlClass}
            >
              <option value="">(sin cambios)</option>
              {STATUS_OPTIONS.map((o) => (
                <option key={o.value} value={o.value}>
                  {o.label}
                </option>
              ))}
            </select>
          </Field>
          {patchError && (
            <p
              role="alert"
              className="rounded-md px-2 py-1 text-xs"
              style={{
                background: "var(--surface-2)",
                color: "var(--text-primary)",
                border: "1px solid var(--color-accent-pink)",
              }}
            >
              {patchError}
            </p>
          )}
        </div>
      </Modal>
    </div>
  );
}
