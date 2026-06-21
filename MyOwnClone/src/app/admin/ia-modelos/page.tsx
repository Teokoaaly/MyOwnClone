"use client";

import { useMemo, useState } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { EmptyState } from "@/components/ui/EmptyState";
import { PageHeader } from "@/components/admin/PageHeader";
import { Field, fieldControlClass } from "@/components/admin/Field";
import { FilterBar } from "@/components/admin/FilterBar";
import { Pagination } from "@/components/admin/Pagination";
import { Modal } from "@/components/ui/Modal";
import { useAdminFetch } from "@/components/admin/useAdminFetch";

// ─── Types ────────────────────────────────────────────────────────────────────

interface AIModel {
  id: string;
  provider: string;
  name: string;
  model_type: string;
  capabilities: Record<string, unknown> | null;
  config: Record<string, unknown> | null;
  input_cost_per_1k: number;
  output_cost_per_1k: number;
  max_tokens: number | null;
  is_active: boolean;
  created_by: string | null;
  created_at: string | null;
  updated_at: string | null;
}

interface ModelAssignment {
  id: string;
  tenant_id: string | null;
  model_id: string;
  label: string | null;
  task: string;
  priority: number;
  is_active: boolean;
  created_by: string | null;
  created_at: string | null;
  updated_at: string | null;
}

interface BreakerState {
  key: string;
  state: string;
  failure_count: number;
  reset_in_seconds: number;
}

interface Pagination_ {
  page: number;
  limit: number;
  total: number;
  pages: number;
}

interface ModelsResponse {
  items: AIModel[];
  pagination: Pagination_;
}

interface AssignmentsResponse {
  items: { assignment: ModelAssignment; model: AIModel | null }[];
  pagination: Pagination_;
}

interface BreakerResponse {
  breakers: BreakerState[];
}

type Tab = "models" | "assignments" | "breakers";

// ─── Helpers ──────────────────────────────────────────────────────────────────

function formatDate(iso: string | null) {
  if (!iso) return "—";
  return new Date(iso).toLocaleString("es-ES", {
    dateStyle: "short",
    timeStyle: "medium",
  });
}

function formatCost(cents: number) {
  return `${(cents / 100).toFixed(4)}€`;
}

function stateBadge(state: string) {
  if (state === "closed") return "badge-active";
  if (state === "open") return "badge-error";
  if (state === "half_open") return "badge-warning";
  return "badge-trial";
}

// ─── Models Tab ────────────────────────────────────────────────────────────────

interface ModelsTabProps {
  onEdit: (model: AIModel) => void;
}

function ModelsTab({ onEdit }: ModelsTabProps) {
  const [pagination, setPagination] = useState<Pagination_>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [search, setSearch] = useState("");
  const [provider, setProvider] = useState("");
  const [modelType, setModelType] = useState("");
  const [isActive, setIsActive] = useState("");

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (search) params.set("search", search);
    if (provider) params.set("provider", provider);
    if (modelType) params.set("type", modelType);
    if (isActive) params.set("is_active", isActive);
    return params.toString();
  }, [pagination.page, pagination.limit, search, provider, modelType, isActive]);

  const { data, loading, error, reload } = useAdminFetch<ModelsResponse>(
    `/api/admin/ia-modelos/models?${queryString}`,
  );

  const items = data?.items ?? [];
  const serverPagination = data?.pagination;
  const total = serverPagination?.total ?? 0;

  function resetPage() {
    setPagination((p) => ({ ...p, page: 1 }));
  }

  return (
    <>
      <FilterBar>
        <Field label="Buscar" fill>
          <input
            type="text"
            value={search}
            onChange={(e) => {
              resetPage();
              setSearch(e.target.value);
            }}
            placeholder="provider o nombre…"
            className={fieldControlClass}
          />
        </Field>
        <Field label="Provider">
          <input
            type="text"
            value={provider}
            onChange={(e) => {
              resetPage();
              setProvider(e.target.value);
            }}
            placeholder="openai…"
            className={fieldControlClass}
          />
        </Field>
        <Field label="Tipo">
          <select
            value={modelType}
            onChange={(e) => {
              resetPage();
              setModelType(e.target.value);
            }}
            className={fieldControlClass}
          >
            <option value="">Todos</option>
            <option value="chat">chat</option>
            <option value="embedding">embedding</option>
            <option value="rerank">rerank</option>
            <option value="tts">tts</option>
            <option value="stt">stt</option>
            <option value="moderation">moderation</option>
          </select>
        </Field>
        <Field label="Activo">
          <select
            value={isActive}
            onChange={(e) => {
              resetPage();
              setIsActive(e.target.value);
            }}
            className={fieldControlClass}
          >
            <option value="">Todos</option>
            <option value="true">Sí</option>
            <option value="false">No</option>
          </select>
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title="Error cargando modelos"
          message={error}
          action={
            <button type="button" onClick={reload} className="btn-secondary text-xs">
              Reintentar
            </button>
          }
        />
      ) : loading ? (
        <LoadingState label="Cargando modelos…" rows={6} />
      ) : items.length === 0 ? (
        <EmptyState
          title="Sin modelos"
          description="No hay modelos configurados. Crea uno con el formulario superior."
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">Provider</th>
                  <th className="px-4 py-2.5 text-left">Nombre</th>
                  <th className="px-4 py-2.5 text-left">Tipo</th>
                  <th className="px-4 py-2.5 text-left">Activo</th>
                  <th className="px-4 py-2.5 text-right">Coste input/1K</th>
                  <th className="px-4 py-2.5 text-right">Coste output/1K</th>
                  <th className="px-4 py-2.5 text-left">Creado</th>
                  <th className="px-4 py-2.5 text-left"></th>
                </tr>
              </thead>
              <tbody>
                {items.map((row) => (
                  <tr key={row.id} className="table-row">
                    <td className="px-4 py-3 font-mono text-xs">{row.provider}</td>
                    <td className="px-4 py-3">{row.name}</td>
                    <td className="px-4 py-3">
                      <span className="badge-trial">{row.model_type}</span>
                    </td>
                    <td className="px-4 py-3">
                      <span className={row.is_active ? "badge-active" : "badge-error"}>
                        {row.is_active ? "Sí" : "No"}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-xs">
                      {formatCost(row.input_cost_per_1k)}
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-xs">
                      {formatCost(row.output_cost_per_1k)}
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {formatDate(row.created_at)}
                    </td>
                    <td className="px-4 py-3">
                      <button
                        type="button"
                        onClick={() => onEdit(row)}
                        className="btn-secondary text-xs"
                      >
                        Editar
                      </button>
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
                  <span className="font-mono text-xs">
                    {row.provider}/{row.name}
                  </span>
                  <span className={row.is_active ? "badge-active" : "badge-error"}>
                    {row.is_active ? "Activo" : "Inactivo"}
                  </span>
                </div>
                <div className="flex justify-between font-mono text-[10px] text-[var(--text-muted)]">
                  <span>Coste: {formatCost(row.input_cost_per_1k)} / {formatCost(row.output_cost_per_1k)}</span>
                </div>
                <button
                  type="button"
                  onClick={() => onEdit(row)}
                  className="btn-secondary text-xs self-end"
                >
                  Editar
                </button>
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
    </>
  );
}

// ─── Assignments Tab ───────────────────────────────────────────────────────────

function AssignmentsTab() {
  const [pagination, setPagination] = useState<Pagination_>({
    page: 1,
    limit: 20,
    total: 0,
    pages: 0,
  });
  const [tenantId, setTenantId] = useState("");
  const [task, setTask] = useState("");

  const queryString = useMemo(() => {
    const params = new URLSearchParams();
    params.set("page", String(pagination.page));
    params.set("limit", String(pagination.limit));
    if (tenantId) params.set("tenant_id", tenantId);
    if (task) params.set("task", task);
    return params.toString();
  }, [pagination.page, pagination.limit, tenantId, task]);

  const { data, loading, error, reload } = useAdminFetch<AssignmentsResponse>(
    `/api/admin/ia-modelos/assignments?${queryString}`,
  );

  const items = data?.items ?? [];
  const serverPagination = data?.pagination;
  const total = serverPagination?.total ?? 0;

  function resetPage() {
    setPagination((p) => ({ ...p, page: 1 }));
  }

  return (
    <>
      <FilterBar>
        <Field label="Tenant ID">
          <input
            type="text"
            value={tenantId}
            onChange={(e) => {
              resetPage();
              setTenantId(e.target.value);
            }}
            placeholder="uuid…"
            className={fieldControlClass}
          />
        </Field>
        <Field label="Task" fill>
          <select
            value={task}
            onChange={(e) => {
              resetPage();
              setTask(e.target.value);
            }}
            className={fieldControlClass}
          >
            <option value="">Todas</option>
            <option value="chat_primary">chat_primary</option>
            <option value="chat_fallback">chat_fallback</option>
            <option value="embedding">embedding</option>
            <option value="rerank">rerank</option>
            <option value="tts">tts</option>
            <option value="stt">stt</option>
            <option value="moderation">moderation</option>
          </select>
        </Field>
      </FilterBar>

      {error ? (
        <ErrorState
          title="Error cargando asignaciones"
          message={error}
          action={
            <button type="button" onClick={reload} className="btn-secondary text-xs">
              Reintentar
            </button>
          }
        />
      ) : loading ? (
        <LoadingState label="Cargando asignaciones…" rows={6} />
      ) : items.length === 0 ? (
        <EmptyState
          title="Sin asignaciones"
          description="No hay asignaciones de modelos configuradas."
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">Modelo</th>
                  <th className="px-4 py-2.5 text-left">Tenant</th>
                  <th className="px-4 py-2.5 text-left">Task</th>
                  <th className="px-4 py-2.5 text-left">Label</th>
                  <th className="px-4 py-2.5 text-right">Prioridad</th>
                  <th className="px-4 py-2.5 text-left">Activo</th>
                  <th className="px-4 py-2.5 text-left">Creado</th>
                </tr>
              </thead>
              <tbody>
                {items.map(({ assignment, model }) => (
                  <tr key={assignment.id} className="table-row">
                    <td className="px-4 py-3 font-mono text-xs">
                      {model ? `${model.provider}/${model.name}` : assignment.model_id.slice(0, 8)}
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {assignment.tenant_id ?? "— (global)"}
                    </td>
                    <td className="px-4 py-3">
                      <span className="badge-trial">{assignment.task}</span>
                    </td>
                    <td className="px-4 py-3">{assignment.label ?? "—"}</td>
                    <td className="px-4 py-3 text-right">{assignment.priority}</td>
                    <td className="px-4 py-3">
                      <span className={assignment.is_active ? "badge-active" : "badge-error"}>
                        {assignment.is_active ? "Sí" : "No"}
                      </span>
                    </td>
                    <td className="px-4 py-3 font-mono text-[11px] text-[var(--text-muted)]">
                      {formatDate(assignment.created_at)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <ul className="space-y-2 md:hidden">
            {items.map(({ assignment, model }) => (
              <li key={assignment.id} className="card flex flex-col gap-2 py-3">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs">
                    {model ? `${model.provider}/${model.name}` : assignment.model_id.slice(0, 8)}
                  </span>
                  <span className="badge-trial">{assignment.task}</span>
                </div>
                <div className="flex justify-between font-mono text-[10px] text-[var(--text-muted)]">
                  <span>Prioridad: {assignment.priority}</span>
                  <span className={assignment.is_active ? "badge-active" : "badge-error"}>
                    {assignment.is_active ? "Activo" : "Inactivo"}
                  </span>
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
    </>
  );
}

// ─── Breaker States Tab ───────────────────────────────────────────────────────

function BreakersTab() {
  const { data, loading, error, reload } = useAdminFetch<BreakerResponse>(
    "/api/admin/ia-modelos/breaker-states",
  );

  const items = data?.breakers ?? [];

  return (
    <>
      {error ? (
        <ErrorState
          title="Error cargando estados"
          message={error}
          action={
            <button type="button" onClick={reload} className="btn-secondary text-xs">
              Reintentar
            </button>
          }
        />
      ) : loading ? (
        <LoadingState label="Cargando estados…" rows={6} />
      ) : items.length === 0 ? (
        <EmptyState
          title="Sin estados"
          description="No hay circuit breakers activos."
        />
      ) : (
        <>
          <div className="card hidden overflow-hidden p-0 md:block">
            <table className="w-full text-sm">
              <thead className="table-header">
                <tr>
                  <th className="px-4 py-2.5 text-left">Key</th>
                  <th className="px-4 py-2.5 text-left">Estado</th>
                  <th className="px-4 py-2.5 text-right">Fallos</th>
                  <th className="px-4 py-2.5 text-right">Resetea en (s)</th>
                </tr>
              </thead>
              <tbody>
                {items.map((row) => (
                  <tr key={row.key} className="table-row">
                    <td className="px-4 py-3 font-mono text-xs">{row.key}</td>
                    <td className="px-4 py-3">
                      <span className={stateBadge(row.state)}>{row.state}</span>
                    </td>
                    <td className="px-4 py-3 text-right">{row.failure_count}</td>
                    <td className="px-4 py-3 text-right font-mono text-xs">
                      {row.reset_in_seconds > 0 ? `${row.reset_in_seconds.toFixed(1)}s` : "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <ul className="space-y-2 md:hidden">
            {items.map((row) => (
              <li key={row.key} className="card flex flex-col gap-2 py-3">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs">{row.key}</span>
                  <span className={stateBadge(row.state)}>{row.state}</span>
                </div>
                <div className="flex justify-between font-mono text-[10px] text-[var(--text-muted)]">
                  <span>Fallos: {row.failure_count}</span>
                  <span>
                    {row.reset_in_seconds > 0 ? `Resetea en ${row.reset_in_seconds.toFixed(1)}s` : "—"}
                  </span>
                </div>
              </li>
            ))}
          </ul>
        </>
      )}
    </>
  );
}

// ─── Create/Edit Model Modal ──────────────────────────────────────────────────

interface ModelFormData {
  provider: string;
  name: string;
  model_type: string;
  input_cost_per_1k: number;
  output_cost_per_1k: number;
  max_tokens: number | null;
  is_active: boolean;
}

interface CreateEditModalProps {
  open: boolean;
  editing: AIModel | null;
  onClose: () => void;
  onSaved: () => void;
}

function CreateEditModal({ open, editing, onClose, onSaved }: CreateEditModalProps) {
  const [form, setForm] = useState<ModelFormData>({
    provider: "",
    name: "",
    model_type: "chat",
    input_cost_per_1k: 0,
    output_cost_per_1k: 0,
    max_tokens: null,
    is_active: true,
  });
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Populate form when editing
  useMemo(() => {
    if (editing) {
      setForm({
        provider: editing.provider,
        name: editing.name,
        model_type: editing.model_type,
        input_cost_per_1k: editing.input_cost_per_1k,
        output_cost_per_1k: editing.output_cost_per_1k,
        max_tokens: editing.max_tokens,
        is_active: editing.is_active,
      });
    } else {
      setForm({
        provider: "",
        name: "",
        model_type: "chat",
        input_cost_per_1k: 0,
        output_cost_per_1k: 0,
        max_tokens: null,
        is_active: true,
      });
    }
    setError(null);
  }, [editing, open]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);

    try {
      const url = editing
        ? `/api/admin/ia-modelos/models/${editing.id}`
        : "/api/admin/ia-modelos/models";
      const method = editing ? "PUT" : "POST";

      const res = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || "Error guardando modelo");
      }

      onSaved();
      onClose();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <Modal
      open={open}
      onClose={onClose}
      title={editing ? "Editar modelo" : "Crear modelo"}
    >
      <form onSubmit={handleSubmit} className="space-y-4">
        {error && (
          <div className="rounded bg-red-500/10 p-3 text-sm text-red-400">
            {error}
          </div>
        )}

        <div className="grid grid-cols-2 gap-4">
          <Field label="Provider" required>
            <input
              type="text"
              value={form.provider}
              onChange={(e) => setForm({ ...form, provider: e.target.value })}
              placeholder="openai"
              required
              className={fieldControlClass}
            />
          </Field>
          <Field label="Nombre" required>
            <input
              type="text"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
              placeholder="gpt-4o-mini"
              required
              className={fieldControlClass}
            />
          </Field>
        </div>

        <Field label="Tipo">
          <select
            value={form.model_type}
            onChange={(e) => setForm({ ...form, model_type: e.target.value })}
            className={fieldControlClass}
          >
            <option value="chat">chat</option>
            <option value="embedding">embedding</option>
            <option value="rerank">rerank</option>
            <option value="tts">tts</option>
            <option value="stt">stt</option>
            <option value="moderation">moderation</option>
          </select>
        </Field>

        <div className="grid grid-cols-2 gap-4">
          <Field label="Coste input/1K (cents)">
            <input
              type="number"
              value={form.input_cost_per_1k}
              onChange={(e) =>
                setForm({ ...form, input_cost_per_1k: parseInt(e.target.value) || 0 })
              }
              min="0"
              className={fieldControlClass}
            />
          </Field>
          <Field label="Coste output/1K (cents)">
            <input
              type="number"
              value={form.output_cost_per_1k}
              onChange={(e) =>
                setForm({ ...form, output_cost_per_1k: parseInt(e.target.value) || 0 })
              }
              min="0"
              className={fieldControlClass}
            />
          </Field>
        </div>

        <Field label="Max tokens">
          <input
            type="number"
            value={form.max_tokens ?? ""}
            onChange={(e) =>
              setForm({ ...form, max_tokens: e.target.value ? parseInt(e.target.value) : null })
            }
            min="1"
            placeholder="sin límite"
            className={fieldControlClass}
          />
        </Field>

        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={form.is_active}
            onChange={(e) => setForm({ ...form, is_active: e.target.checked })}
            className="h-4 w-4 rounded border-[var(--border)]"
          />
          <span className="text-sm">Modelo activo</span>
        </label>

        <div className="flex justify-end gap-2 pt-2">
          <button
            type="button"
            onClick={onClose}
            className="btn-secondary"
            disabled={submitting}
          >
            Cancelar
          </button>
          <button type="submit" className="btn-primary" disabled={submitting}>
            {submitting ? "Guardando…" : editing ? "Actualizar" : "Crear"}
          </button>
        </div>
      </form>
    </Modal>
  );
}

// ─── Main Page ────────────────────────────────────────────────────────────────

export default function AdminIAModelosPage() {
  const [tab, setTab] = useState<Tab>("models");
  const [editModel, setEditModel] = useState<AIModel | null>(null);
  const [createOpen, setCreateOpen] = useState(false);

  return (
    <div className="space-y-6">
      <PageHeader
        title="Modelos IA"
        subtitle="Gestión de modelos, asignaciones y circuit breakers"
      />

      {/* Tabs */}
      <div className="flex gap-1 border-b border-[var(--border)]">
        {(["models", "assignments", "breakers"] as Tab[]).map((t) => (
          <button
            key={t}
            type="button"
            onClick={() => setTab(t)}
            className={`px-4 py-2 text-sm font-medium transition-colors ${
              tab === t
                ? "border-b-2 border-[var(--accent)] text-[var(--accent)]"
                : "text-[var(--text-muted)] hover:text-[var(--text)]"
            }`}
          >
            {t === "models" ? "Modelos" : t === "assignments" ? "Asignaciones" : "Circuit Breakers"}
          </button>
        ))}
      </div>

      {/* Create button for models tab */}
      {tab === "models" && (
        <div className="flex justify-end">
          <button
            type="button"
            onClick={() => {
              setEditModel(null);
              setCreateOpen(true);
            }}
            className="btn-primary"
          >
            + Crear modelo
          </button>
        </div>
      )}

      {/* Tab content */}
      {tab === "models" && <ModelsTab onEdit={(m) => { setEditModel(m); setCreateOpen(true); }} />}
      {tab === "assignments" && <AssignmentsTab />}
      {tab === "breakers" && <BreakersTab />}

      {/* Create/Edit Modal */}
      <CreateEditModal
        open={createOpen}
        editing={editModel}
        onClose={() => {
          setCreateOpen(false);
          setEditModel(null);
        }}
        onSaved={() => {
          // Trigger reload - the useAdminFetch will refetch automatically
        }}
      />
    </div>
  );
}
