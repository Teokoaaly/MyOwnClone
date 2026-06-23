"use client";

import { useEffect, useMemo, useState } from "react";
import { PageHeader } from "@/components/admin/PageHeader";
import { Field, fieldControlClass } from "@/components/admin/Field";
import { FilterBar } from "@/components/admin/FilterBar";
import { useAdminFetch } from "@/components/admin/useAdminFetch";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { EmptyState } from "@/components/ui/EmptyState";
import { BarChart, ChartLegend } from "@/components/ui/BarChart";

type Capability = "llm" | "embedding" | "stt";
type Task = "chat" | "embedding" | "email_classification" | "email_draft" | "stt";

interface AIModel {
  id: string;
  tenant_id: string | null;
  name: string;
  provider: string;
  model_id: string;
  base_url: string | null;
  capabilities: string[];
  input_price_cents_per_mtok: number;
  output_price_cents_per_mtok: number;
  priority: number;
  temperature_default: number | null;
  max_tokens_default: number | null;
  max_input_tokens: number | null;
  embedding_dimensions: number | null;
  is_active: boolean;
  has_api_key: boolean;
}

interface Assignment {
  id: string;
  tenant_id: string | null;
  task: Task;
  model_id: string;
  override_params: Record<string, unknown>;
  is_active: boolean;
}

interface CostsResponse {
  series: Array<{
    day: string;
    invocations: number;
    prompt_tokens: number;
    completion_tokens: number;
  }>;
  totals: {
    invocations: number;
    prompt_tokens: number;
    completion_tokens: number;
  };
}

const TASKS: Array<{ id: Task; label: string; capability: Capability }> = [
  { id: "chat", label: "Chat", capability: "llm" },
  { id: "embedding", label: "Embeddings", capability: "embedding" },
  { id: "email_classification", label: "Email classify", capability: "llm" },
  { id: "email_draft", label: "Email draft", capability: "llm" },
  { id: "stt", label: "Speech to text", capability: "stt" },
];

const PROVIDERS = [
  "openai",
  "anthropic",
  "minimax",
  "together",
  "openai_compatible",
  "local",
];

const CAPABILITY_OPTIONS: Capability[] = ["llm", "embedding", "stt"];

const chartLegend = [
  { label: "Invocations", color: "#2563EB" },
  { label: "Prompt tokens", color: "#F97316" },
  { label: "Completion tokens", color: "#10B981" },
];

const emptyForm = {
  id: null as string | null,
  name: "",
  provider: "openai",
  model_id: "",
  api_key: "",
  base_url: "",
  capabilities: ["llm"] as Capability[],
  priority: 100,
  temperature_default: "",
  max_tokens_default: "",
  max_input_tokens: "",
  embedding_dimensions: "",
  is_active: true,
};

function taskBadge(task: Task) {
  if (task === "embedding") return "badge-violet";
  if (task === "stt") return "badge-warning";
  return "badge-active";
}

export default function AdminAIModelsPage() {
  const {
    data: models,
    loading: modelsLoading,
    error: modelsError,
    reload: reloadModels,
  } = useAdminFetch<AIModel[]>("/api/admin/ai-models");
  const {
    data: assignments,
    loading: assignmentsLoading,
    error: assignmentsError,
    reload: reloadAssignments,
  } = useAdminFetch<Assignment[]>("/api/admin/ai-models/assignments");
  const {
    data: costs,
    loading: costsLoading,
    error: costsError,
    reload: reloadCosts,
  } = useAdminFetch<CostsResponse>("/api/admin/ai-models/costs");

  const [form, setForm] = useState(emptyForm);
  const [saving, setSaving] = useState(false);
  const [playgroundTask, setPlaygroundTask] = useState<Task>("chat");
  const [playgroundModelId, setPlaygroundModelId] = useState("");
  const [playgroundPrompt, setPlaygroundPrompt] = useState("Describe the current model assignment in one short paragraph.");
  const [playgroundResult, setPlaygroundResult] = useState<string>("");
  const [playgroundMeta, setPlaygroundMeta] = useState<string>("");
  const [playgroundLoading, setPlaygroundLoading] = useState(false);
  const [pageError, setPageError] = useState<string | null>(null);
  const [actionMessage, setActionMessage] = useState<string | null>(null);

  useEffect(() => {
    if (!playgroundModelId && models?.length) {
      setPlaygroundModelId(models[0].id);
    }
  }, [models, playgroundModelId]);

  const activeAssignments = useMemo(() => {
    const byTask = new Map<Task, Assignment>();
    for (const assignment of assignments ?? []) {
      if (assignment.is_active && !byTask.has(assignment.task)) {
        byTask.set(assignment.task, assignment);
      }
    }
    return byTask;
  }, [assignments]);

  const chartData = useMemo(() => {
    return (costs?.series ?? []).map((row) => ({
      label: row.day.slice(5),
      values: [
        { label: "Invocations", value: row.invocations, color: "#2563EB" },
        { label: "Prompt", value: row.prompt_tokens, color: "#F97316" },
        { label: "Completion", value: row.completion_tokens, color: "#10B981" },
      ],
    }));
  }, [costs]);

  const visibleModels = useMemo(() => models ?? [], [models]);

  async function handleSaveModel() {
    setSaving(true);
    setPageError(null);
    setActionMessage(null);
    try {
      const payload = {
        name: form.name,
        provider: form.provider,
        model_id: form.model_id,
        api_key: form.api_key || null,
        base_url: form.base_url || null,
        capabilities: form.capabilities,
        input_price_cents_per_mtok: 0,
        output_price_cents_per_mtok: 0,
        priority: Number(form.priority) || 100,
        temperature_default: form.temperature_default === "" ? null : Number(form.temperature_default),
        max_tokens_default: form.max_tokens_default === "" ? null : Number(form.max_tokens_default),
        max_input_tokens: form.max_input_tokens === "" ? null : Number(form.max_input_tokens),
        embedding_dimensions: form.embedding_dimensions === "" ? null : Number(form.embedding_dimensions),
        is_active: form.is_active,
      };

      const response = await fetch(
        form.id ? `/api/admin/ai-models/${form.id}` : "/api/admin/ai-models",
        {
          method: form.id ? "PUT" : "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        },
      );
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.error ?? `Error ${response.status}`);
      setActionMessage(form.id ? "Model updated." : "Model created.");
      setForm(emptyForm);
      reloadModels();
    } catch (error) {
      setPageError(error instanceof Error ? error.message : "Could not save model");
    } finally {
      setSaving(false);
    }
  }

  function editModel(model: AIModel) {
    setForm({
      id: model.id,
      name: model.name,
      provider: model.provider,
      model_id: model.model_id,
      api_key: "",
      base_url: model.base_url ?? "",
      capabilities: model.capabilities.filter((value): value is Capability =>
        CAPABILITY_OPTIONS.includes(value as Capability),
      ),
      priority: model.priority,
      temperature_default: model.temperature_default?.toString() ?? "",
      max_tokens_default: model.max_tokens_default?.toString() ?? "",
      max_input_tokens: model.max_input_tokens?.toString() ?? "",
      embedding_dimensions: model.embedding_dimensions?.toString() ?? "",
      is_active: model.is_active,
    });
    setActionMessage(null);
    setPageError(null);
  }

  async function assignTask(task: Task, modelId: string) {
    setPageError(null);
    setActionMessage(null);
    try {
      const response = await fetch("/api/admin/ai-models/assignments", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          task,
          model_id: modelId,
          override_params: {},
          is_active: true,
        }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.error ?? `Error ${response.status}`);
      setActionMessage(`Assignment updated for ${task}.`);
      reloadAssignments();
    } catch (error) {
      setPageError(error instanceof Error ? error.message : "Could not update assignment");
    }
  }

  async function testConnection(modelId: string) {
    setPageError(null);
    setActionMessage(null);
    try {
      const response = await fetch("/api/admin/ai-models/test-connection", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ model_id: modelId }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.error ?? `Error ${response.status}`);
      setActionMessage(data.ok ? `Connection OK: ${data.message || "success"}` : "Connection failed.");
    } catch (error) {
      setPageError(error instanceof Error ? error.message : "Could not test connection");
    }
  }

  async function runPlayground() {
    setPlaygroundLoading(true);
    setPageError(null);
    setPlaygroundResult("");
    setPlaygroundMeta("");
    try {
      const response = await fetch("/api/admin/ai-models/playground", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model_id: playgroundModelId,
          task: playgroundTask,
          prompt: playgroundPrompt,
        }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.error ?? `Error ${response.status}`);
      setPlaygroundResult(data.text || "");
      setPlaygroundMeta(
        data.usage
          ? `${data.usage.prompt_tokens}/${data.usage.completion_tokens}/${data.usage.total_tokens} tokens`
          : data.latency_ms
            ? `${data.latency_ms} ms`
            : "No usage metadata",
      );
    } catch (error) {
      setPageError(error instanceof Error ? error.message : "Could not run playground");
    } finally {
      setPlaygroundLoading(false);
    }
  }

  if (modelsLoading && assignmentsLoading && costsLoading) {
    return <LoadingState label="Loading AI models..." rows={5} />;
  }

  if ((modelsError && !models) || (assignmentsError && !assignments)) {
    return (
      <ErrorState
        title="Could not load AI models"
        message={modelsError ?? assignmentsError ?? "Unknown error"}
        action={
          <button type="button" onClick={() => { reloadModels(); reloadAssignments(); reloadCosts(); }} className="btn-secondary text-xs">
            Try again
          </button>
        }
      />
    );
  }

  return (
    <div className="space-y-6">
      <PageHeader
        title="AI models"
        subtitle="Manage catalog entries, task routing, playground checks, and recent runtime usage."
        actions={
          <>
            <button type="button" className="btn-secondary text-xs" onClick={() => { reloadModels(); reloadAssignments(); reloadCosts(); }}>
              Refresh
            </button>
            {actionMessage && <span className="badge-active">{actionMessage}</span>}
          </>
        }
      />

      {pageError && <div className="badge-error inline-block">{pageError}</div>}

      <div className="grid grid-cols-1 gap-4 xl:grid-cols-[1.1fr_0.9fr]">
        <section className="card space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <div className="stat-label">Catalog</div>
              <div className="stat-value mt-1">{visibleModels.length}</div>
            </div>
            <button type="button" className="btn-secondary text-xs" onClick={() => setForm(emptyForm)}>
              New model
            </button>
          </div>

          {visibleModels.length === 0 ? (
            <EmptyState title="No models yet" description="Create the first runtime model to start assigning tasks." />
          ) : (
            <div className="space-y-3">
              {visibleModels.map((model) => (
                <div key={model.id} className="rounded-lg border border-[var(--border-soft)] p-3">
                  <div className="flex flex-wrap items-start justify-between gap-3">
                    <div>
                      <div className="flex items-center gap-2">
                        <h2 className="text-sm font-semibold text-[var(--text-primary)]">{model.name}</h2>
                        <span className={model.is_active ? "badge-active" : "badge-warning"}>
                          {model.is_active ? "Active" : "Inactive"}
                        </span>
                        {model.tenant_id ? null : <span className="badge-violet">Global</span>}
                      </div>
                      <p className="mt-1 font-mono text-[11px] text-[var(--text-muted)]">
                        {model.provider} · {model.model_id}
                      </p>
                      <div className="mt-2 flex flex-wrap gap-1.5">
                        {model.capabilities.map((capability) => (
                          <span key={capability} className="badge-trial">{capability}</span>
                        ))}
                      </div>
                    </div>
                    <div className="flex gap-2">
                      <button type="button" className="btn-secondary text-xs" onClick={() => editModel(model)}>
                        Edit
                      </button>
                      <button type="button" className="btn-secondary text-xs" onClick={() => testConnection(model.id)}>
                        Test
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="card space-y-4">
          <div>
            <div className="stat-label">{form.id ? "Edit model" : "Create model"}</div>
            <div className="mt-1 text-sm text-[var(--text-muted)]">
              API keys are write-only. Leave the key blank while editing to preserve the stored secret.
            </div>
          </div>

          <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
            <Field label="Name"><input className={fieldControlClass} value={form.name} onChange={(e) => setForm((s) => ({ ...s, name: e.target.value }))} /></Field>
            <Field label="Provider">
              <select className={fieldControlClass} value={form.provider} onChange={(e) => setForm((s) => ({ ...s, provider: e.target.value }))}>
                {PROVIDERS.map((provider) => <option key={provider} value={provider}>{provider}</option>)}
              </select>
            </Field>
            <Field label="Model id"><input className={fieldControlClass} value={form.model_id} onChange={(e) => setForm((s) => ({ ...s, model_id: e.target.value }))} /></Field>
            <Field label="Base URL"><input className={fieldControlClass} value={form.base_url} onChange={(e) => setForm((s) => ({ ...s, base_url: e.target.value }))} placeholder="https://..." /></Field>
            <Field label="API key">
              <input type="password" className={fieldControlClass} value={form.api_key} onChange={(e) => setForm((s) => ({ ...s, api_key: e.target.value }))} placeholder={form.id ? "leave blank to keep stored key" : "sk-..."} />
            </Field>
            <Field label="Priority"><input type="number" className={fieldControlClass} value={form.priority} onChange={(e) => setForm((s) => ({ ...s, priority: Number(e.target.value) }))} /></Field>
            <Field label="Temperature"><input type="number" step="0.1" className={fieldControlClass} value={form.temperature_default} onChange={(e) => setForm((s) => ({ ...s, temperature_default: e.target.value }))} /></Field>
            <Field label="Max output"><input type="number" className={fieldControlClass} value={form.max_tokens_default} onChange={(e) => setForm((s) => ({ ...s, max_tokens_default: e.target.value }))} /></Field>
            <Field label="Max input"><input type="number" className={fieldControlClass} value={form.max_input_tokens} onChange={(e) => setForm((s) => ({ ...s, max_input_tokens: e.target.value }))} /></Field>
            <Field label="Embedding dims"><input type="number" className={fieldControlClass} value={form.embedding_dimensions} onChange={(e) => setForm((s) => ({ ...s, embedding_dimensions: e.target.value }))} /></Field>
          </div>

          <Field label="Capabilities">
            <div className="mt-2 flex flex-wrap gap-2">
              {CAPABILITY_OPTIONS.map((capability) => {
                const checked = form.capabilities.includes(capability);
                return (
                  <label key={capability} className="flex items-center gap-2 rounded-lg border border-[var(--border-soft)] px-3 py-2 text-sm">
                    <input
                      type="checkbox"
                      checked={checked}
                      onChange={() => setForm((state) => ({
                        ...state,
                        capabilities: checked
                          ? state.capabilities.filter((value) => value !== capability)
                          : [...state.capabilities, capability],
                      }))}
                    />
                    {capability}
                  </label>
                );
              })}
              <label className="flex items-center gap-2 rounded-lg border border-[var(--border-soft)] px-3 py-2 text-sm">
                <input type="checkbox" checked={form.is_active} onChange={() => setForm((s) => ({ ...s, is_active: !s.is_active }))} />
                active
              </label>
            </div>
          </Field>

          <div className="flex gap-2">
            <button type="button" className="btn-primary text-xs disabled:opacity-50" disabled={saving || !form.name || !form.model_id || (!form.id && !form.api_key)} onClick={handleSaveModel}>
              {saving ? "Saving..." : form.id ? "Update model" : "Create model"}
            </button>
            <button type="button" className="btn-secondary text-xs" onClick={() => setForm(emptyForm)}>
              Reset
            </button>
          </div>
        </section>
      </div>

      <section className="card space-y-4">
        <div>
          <div className="stat-label">Assignments</div>
          <div className="mt-1 text-sm text-[var(--text-muted)]">
            Each task resolves to one active model. Capability mismatches are rejected by the backend.
          </div>
        </div>
        <div className="grid grid-cols-1 gap-3 lg:grid-cols-2 xl:grid-cols-3">
          {TASKS.map((task) => {
            const assigned = activeAssignments.get(task.id);
            const candidates = visibleModels.filter((model) => model.capabilities.includes(task.capability));
            return (
              <div key={task.id} className="rounded-lg border border-[var(--border-soft)] p-3">
                <div className="flex items-center justify-between gap-2">
                  <span className={taskBadge(task.id)}>{task.label}</span>
                  {assigned ? (
                    <span className="font-mono text-[11px] text-[var(--text-muted)]">
                      {visibleModels.find((model) => model.id === assigned.model_id)?.model_id ?? assigned.model_id}
                    </span>
                  ) : (
                    <span className="text-[11px] text-[var(--text-muted)]">Unassigned</span>
                  )}
                </div>
                <div className="mt-3 flex gap-2">
                  <select
                    className={fieldControlClass}
                    value={assigned?.model_id ?? ""}
                    onChange={(e) => assignTask(task.id, e.target.value)}
                  >
                    <option value="">Select model</option>
                    {candidates.map((model) => (
                      <option key={model.id} value={model.id}>
                        {model.name} · {model.model_id}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <div className="grid grid-cols-1 gap-4 xl:grid-cols-[1.05fr_0.95fr]">
        <section className="card space-y-4">
          <div>
            <div className="stat-label">Playground</div>
            <div className="mt-1 text-sm text-[var(--text-muted)]">
              Exercise the runtime stack using the current adapters and provider configuration.
            </div>
          </div>
          <FilterBar>
            <Field label="Task" fill>
              <select className={fieldControlClass} value={playgroundTask} onChange={(e) => setPlaygroundTask(e.target.value as Task)}>
                {TASKS.map((task) => <option key={task.id} value={task.id}>{task.label}</option>)}
              </select>
            </Field>
            <Field label="Model" fill>
              <select className={fieldControlClass} value={playgroundModelId} onChange={(e) => setPlaygroundModelId(e.target.value)}>
                {visibleModels.map((model) => (
                  <option key={model.id} value={model.id}>{model.name} · {model.model_id}</option>
                ))}
              </select>
            </Field>
          </FilterBar>
          <Field label="Prompt">
            <textarea className={`${fieldControlClass} min-h-[160px]`} value={playgroundPrompt} onChange={(e) => setPlaygroundPrompt(e.target.value)} />
          </Field>
          <div className="flex gap-2">
            <button type="button" className="btn-primary text-xs disabled:opacity-50" disabled={playgroundLoading || !playgroundModelId || !playgroundPrompt.trim()} onClick={runPlayground}>
              {playgroundLoading ? "Running..." : "Run prompt"}
            </button>
          </div>
          <div className="rounded-lg border border-[var(--border-soft)] bg-white/70 p-3">
            <div className="flex items-center justify-between gap-2">
              <span className="stat-label">Response</span>
              {playgroundMeta ? <span className="font-mono text-[11px] text-[var(--text-muted)]">{playgroundMeta}</span> : null}
            </div>
            <pre className="mt-2 whitespace-pre-wrap break-words text-sm text-[var(--text-primary)]">{playgroundResult || "No response yet."}</pre>
          </div>
        </section>

        <section className="card space-y-4">
          <div className="flex items-start justify-between gap-3">
            <div>
              <div className="stat-label">Recent runtime usage</div>
              <div className="mt-1 text-sm text-[var(--text-muted)]">
                Last 7 days of AI invocations from `ai_invocations`.
              </div>
            </div>
            {costsError ? <span className="badge-warning">Chart degraded</span> : null}
          </div>
          <div className="grid grid-cols-3 gap-3">
            <div className="rounded-lg border border-[var(--border-soft)] p-3">
              <div className="stat-label">Invocations</div>
              <div className="stat-value mt-1">{costs?.totals.invocations ?? 0}</div>
            </div>
            <div className="rounded-lg border border-[var(--border-soft)] p-3">
              <div className="stat-label">Prompt tokens</div>
              <div className="stat-value mt-1">{costs?.totals.prompt_tokens ?? 0}</div>
            </div>
            <div className="rounded-lg border border-[var(--border-soft)] p-3">
              <div className="stat-label">Completion tokens</div>
              <div className="stat-value mt-1">{costs?.totals.completion_tokens ?? 0}</div>
            </div>
          </div>
          {costsLoading ? (
            <LoadingState label="Loading usage..." rows={1} />
          ) : (
            <>
              <BarChart data={chartData} height={240} />
              <ChartLegend items={chartLegend} />
            </>
          )}
        </section>
      </div>
    </div>
  );
}
