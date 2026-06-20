"use client";

import { useMemo, useState, useCallback } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { EmptyState } from "@/components/ui/EmptyState";
import { StatusBadge, statusToKind } from "@/components/ui/StatusBadge";
import { CourtesyButton } from "@/components/admin/CourtesyButton";
import { PageHeader } from "@/components/admin/PageHeader";
import { Field, fieldControlClass } from "@/components/admin/Field";
import { FilterBar } from "@/components/admin/FilterBar";
import { Pagination } from "@/components/admin/Pagination";
import { Modal } from "@/components/ui/Modal";
import { useAdminFetch } from "@/components/admin/useAdminFetch";
import { Link } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

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

interface Pagination_ {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

interface TenantsResponse {
  items: AdminTenant[];
  pagination: Pagination_;
}

const PLAN_OPTIONS = [
  { value: "", label: "Todos los planes" },
  { value: "free", label: "Free Plan" },
  { value: "pro", label: "Pro Plan" },
  { value: "enterprise", label: "Enterprise" },
];

const STATUS_OPTIONS = [
  { value: "", label: "Todos los estados" },
  { value: "active", label: "Active" },
  { value: "trial", label: "Trial" },
  { value: "suspended", label: "Suspended" },
  { value: "cancelled", label: "Cancelled" },
];

function formatEur(cents: number) {
  return `${(cents / 100).toFixed(2)}€`;
}

export default function AdminTenantsPage() {
  const t = useTranslations("admin");
  const [pagination, setPagination] = useState<Pagination_>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [search, setSearch] = useState("");
  const [plan, setPlan] = useState("");
  const [status, setStatus] = useState("");

  // Create tenant modal state
  const [createOpen, setCreateOpen] = useState(false);
  const [createName, setCreateName] = useState("");
  const [createSlug, setCreateSlug] = useState("");
  const [createPlan, setCreatePlan] = useState("trial");
  const [createStatus, setCreateStatus] = useState("trial");
  const [createSubmitting, setCreateSubmitting] = useState(false);
  const [createError, setCreateError] = useState<string | null>(null);

  const slugify = (text: string) =>
    text
      .toLowerCase()
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "");

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (search) params.set("search", search);
    if (plan) params.set("plan", plan);
    if (status) params.set("status", status);
    return params.toString();
  }, [pagination.page, pagination.limit, search, plan, status]);

  const { data, loading, error, reload } = useAdminFetch<TenantsResponse>(
    `/api/admin/tenants?${queryString}`,
  );

  const tenants = data?.items ?? [];
  const serverPagination = data?.pagination;
  const total = serverPagination?.total ?? 0;

  function resetPage() {
    setPagination((p) => ({ ...p, page: 1 }));
  }

  const handleCreateNameChange = useCallback(
    (value: string) => {
      setCreateName(value);
      setCreateSlug(slugify(value));
    },
    [],
  );

  async function submitCreateTenant() {
    if (!createName.trim() || !createSlug.trim()) return;
    setCreateSubmitting(true);
    setCreateError(null);
    try {
      const res = await fetch("/api/admin/tenants", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: createName.trim(),
          slug: createSlug.trim(),
          plan: createPlan,
          status: createStatus,
        }),
      });
      if (!res.ok) {
        const payload = await res.json().catch(() => ({}));
        throw new Error(payload.error ?? `Error ${res.status}`);
      }
      setCreateOpen(false);
      setCreateName("");
      setCreateSlug("");
      setCreatePlan("trial");
      setCreateStatus("trial");
      reload();
    } catch (e) {
      setCreateError(e instanceof Error ? e.message : "Error creating tenant");
    } finally {
      setCreateSubmitting(false);
    }
  }

  return (
    <div className="space-y-6">
      <PageHeader
        title={t("tenants.title")}
        subtitle={`${total} accounts in the platform`}
        actions={
          <>
            <button
              type="button"
              onClick={() => setCreateOpen(true)}
              className="btn-primary text-xs"
            >
              + New tenant
            </button>
            <CourtesyButton onCreated={reload} />
          </>
        }
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
            placeholder={t("tenants.searchPlaceholder")}
            className={fieldControlClass}
          />
        </Field>
        <Field label="Plan">
          <select
            value={plan}
            onChange={(e) => {
              resetPage();
              setPlan(e.target.value);
            }}
            className={fieldControlClass}
          >
            {PLAN_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </Field>
        <Field label="Status">
          <select
            value={status}
            onChange={(e) => {
              resetPage();
              setStatus(e.target.value);
            }}
            className={fieldControlClass}
          >
            {STATUS_OPTIONS.map((o) => (
              <option key={o.value} value={o.value}>
                {o.label}
              </option>
            ))}
          </select>
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title={t("tenants.errorTitle")}
          message={error}
          action={
            <button
              type="button"
              onClick={reload}
              className="btn-secondary text-xs"
            >
              Try again
            </button>
          }
        />
      ) : loading ? (
        <LoadingState label="Loading tenants..." rows={6} />
      ) : tenants.length === 0 ? (
        <EmptyState
          title={t("no_tenants")}
          description={
            search || plan || status
              ? "No tenants matched those filters."
              : "There are no tenants in the platform yet. Create the first one with the button above."
          }
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">{t("common.tenant")}</th>
                  <th className="px-4 py-2.5 text-left">{t("plan")}</th>
                  <th className="px-4 py-2.5 text-left">{t("status")}</th>
                  <th className="px-4 py-2.5 text-right">{t("common.clones")}</th>
                  <th className="px-4 py-2.5 text-right">{t("common.costs30d")}</th>
                  <th className="px-4 py-2.5 text-left">{t("tenantDetail.created")}</th>
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
                      <StatusBadge
                        kind={statusToKind(t.status)}
                        label={t.status ?? "—"}
                      />
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-[var(--text-primary)]">
                      {t.clone_count}
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-[var(--text-primary)]">
                      {formatEur(t.monthly_cost_cents)}
                    </td>
                    <td className="px-4 py-3 text-xs text-[var(--text-muted)]">
                      {t.created_at
                        ? new Date(t.created_at).toLocaleDateString("en-US")
                        : "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <ul className="space-y-2 md:hidden">
            {tenants.map((t) => (
              <li key={t.id} className="card flex flex-col gap-2 py-3">
                <Link
                  href={`/admin/tenants/${t.id}`}
                  className="font-medium text-[var(--text-primary)] hover:text-[var(--color-accent-warm)]"
                >
                  {t.name}
                </Link>
                {t.slug && (
                  <p className="text-xs text-[var(--text-muted)]">{t.slug}</p>
                )}
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <StatusBadge
                    kind={statusToKind(t.status)}
                    label={t.status ?? "—"}
                  />
                  <span className="text-xs text-[var(--text-secondary)] capitalize">
                    {t.plan ?? "—"}
                  </span>
                </div>
                <div className="flex justify-between text-[10px] text-[var(--text-muted)] font-mono">
                  <span>{t.clone_count} clones</span>
                  <span>{formatEur(t.monthly_cost_cents)} / 30d</span>
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
          layout="spread"
          onPrev={() =>
            setPagination((p) => ({ ...p, page: Math.max(1, p.page - 1) }))
          }
          onNext={() =>
            setPagination((p) => ({ ...p, page: p.page + 1 }))
          }
        />
      )}

      {/* ── Create Tenant Modal ── */}
      <Modal
        open={createOpen}
        onClose={() => setCreateOpen(false)}
        title={t("tenants.createTitle")}
        size="sm"
        footer={
          <>
            <button
              type="button"
              onClick={() => setCreateOpen(false)}
              className="btn-secondary text-xs"
              disabled={createSubmitting}
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={submitCreateTenant}
              className="btn-primary text-xs disabled:opacity-40"
              disabled={createSubmitting || !createName.trim() || !createSlug.trim()}
            >
              {createSubmitting ? "Creating..." : "Create tenant"}
            </button>
          </>
        }
      >
        <div className="space-y-3">
          <Field label="Tenant name">
            <input
              type="text"
              value={createName}
              onChange={(e) => handleCreateNameChange(e.target.value)}
              placeholder={t("tenants.namePlaceholder")}
              className={fieldControlClass}
              autoFocus
            />
          </Field>
          <Field label="Slug">
            <input
              type="text"
              value={createSlug}
              onChange={(e) => setCreateSlug(e.target.value)}
              placeholder={t("tenants.slugPlaceholder")}
              className={fieldControlClass}
            />
            <p className="mt-1 text-[10px] text-[var(--text-muted)]">
              Auto-generated from the name. You can edit it.
            </p>
          </Field>
          <Field label="Plan">
            <select
              value={createPlan}
              onChange={(e) => setCreatePlan(e.target.value)}
              className={fieldControlClass}
            >
              <option value="trial">{t("common.trial")}</option>
              <option value="basic">{t("basic")}</option>
              <option value="pro">{t("pro")}</option>
              <option value="scale">{t("scale")}</option>
              <option value="enterprise">{t("enterprise")}</option>
            </select>
          </Field>
          <Field label="Status">
            <select
              value={createStatus}
              onChange={(e) => setCreateStatus(e.target.value)}
              className={fieldControlClass}
            >
              <option value="trial">{t("common.trial")}</option>
              <option value="active">{t("active")}</option>
              <option value="suspended">{t("common.suspended")}</option>
              <option value="cancelled">{t("cancelled")}</option>
            </select>
          </Field>
          {createError && (
            <p
              role="alert"
              className="rounded-md px-2 py-1 text-xs"
              style={{
                background: "var(--surface-2)",
                color: "var(--text-primary)",
                border: "1px solid var(--color-accent-pink)",
              }}
            >
              {createError}
            </p>
          )}
        </div>
      </Modal>
    </div>
  );
}
