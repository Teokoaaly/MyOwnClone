# Plan: Admin Backend — Monitor & Control Panels (M14)

> **For Hermes:** Execute task-by-task via terminal/workers. No deploy until Phase 4 verified.

**Goal:** Añadir 4 paneles de control al admin `/admin/ia-modelos`: balanceador, embeddings, costes por modelo, y backfill trigger. Todo documentado en `.sisyphus/evidence/`.

**Architecture:** Backend Flask-RESTX (endpoints nuevos en `ai_models.py` + utilidad en `model_registry.py`). Frontend Next.js (secciones nuevas dentro de `/admin/ia-modelos/page.tsx` + 1 página nueva). Sin migraciones DB (usa tablas existentes).

**Tech Stack:** Python 3.11+, Flask-RESTX, SQLAlchemy, Next.js 16, TypeScript, Tailwind CSS

---

## §0 — Auditoría previa

```
Archivos a modificar:
  api/controllers/console/myownclone/ai_models.py     ← 4 endpoints nuevos
  api/core/model_registry.py                          ← método dump_status()
  api/core/embeddings.py                              ← método stats()
  MyOwnClone/src/app/admin/ia-modelos/page.tsx        ← 3 secciones/tabs nuevas
  MyOwnClone/src/app/admin/ia-modelos/balanceador/page.tsx  ← NUEVA: panel dedicado
  MyOwnClone/src/app/admin/ia-modelos/embeddings/page.tsx   ← NUEVA: panel dedicado
  MyOwnClone/src/lib/nav-admin.ts                     ← añadir enlaces sidebar

Archivos NUEVOS:
  api/tests/test_admin_ai_models_panels.py            ← tests backend
  .sisyphus/evidence/task-M14-admin-panels.md         ← documentación
```

---

## Fase 1 — Backend: Endpoints de estado

### Task 1: Model Registry status endpoint

**Objetivo:** API que devuelva el estado del balanceador: qué modelo está activo por cada task, TTL, cache hits.

**Files:**
- Modify: `api/core/model_registry.py` (añadir `dump_status()`)
- Modify: `api/controllers/console/myownclone/ai_models.py` (añadir endpoint)
- Create: `api/tests/test_admin_ai_models_panels.py`

**Endpoint:** `GET /console/api/myownclone/ai-models/registry-status`
**Response:**
```json
{
  "ttl_seconds": 60,
  "cache_size": 2,
  "tasks": [
    {"task": "chat", "provider": "openai", "model_id": "gpt-4o-mini", "source": "db_assignment", "cache_hit": true},
    {"task": "embedding", "provider": "openai", "model_id": "text-embedding-3-small", "source": "db_assignment", "cache_hit": false}
  ]
}
```

**Step 1:** Añadir `dump_status()` a `ModelRegistry` en `api/core/model_registry.py`:
```python
def dump_status(self) -> dict:
    items = []
    for task in AITask:
        entry = self._get(task, None)  # None tenant for global
        items.append({
            "task": task.value,
            "provider": entry.provider if entry else None,
            "model_id": entry.model_id if entry else None,
            "source": entry.source if entry else "unresolved",
            "cache_hit": self._cache.get(task) is not None if entry else False,
        })
    return {"ttl_seconds": self.ttl_seconds, "cache_size": len(self._cache), "tasks": items}
```

**Step 2:** Añadir endpoint `RegistryStatusApi` en `ai_models.py`:
```python
@console_ns.route("/myownclone/ai-models/registry-status")
class RegistryStatusApi(Resource):
    @login_required
    def get(self):
        reg = ModelRegistry()
        return reg.dump_status(), 200
```

**Step 3:** Test: `test_registry_status_endpoint` — llama `GET /console/api/myownclone/ai-models/registry-status` y verifica 200, keys esperadas.

---

### Task 2: Embedding status endpoint

**Objetivo:** API que devuelva constantes de embedding (_MAX_EMBED_TEXTS, EMBEDDING_BATCH_SIZE) + contador reciente de llamadas.

**Endpoint:** `GET /console/api/myownclone/ai-models/embedding-status`

**Step 1:** Añadir `dump_embedding_status()` en `runtime.py`:
```python
def dump_embedding_status() -> dict:
    return {
        "max_embed_texts": _MAX_EMBED_TEXTS,
        "embedding_dimensions": 1536,
        "client_batch_size": 64,
    }
```

**Step 2:** Añadir endpoint en `ai_models.py`:
```python
@console_ns.route("/myownclone/ai-models/embedding-status")
class EmbeddingStatusApi(Resource):
    @login_required
    def get(self):
        from api.controllers.console.myownclone.runtime import dump_embedding_status
        return dump_embedding_status(), 200
```

**Step 3:** Test: `test_embedding_status_endpoint`.

---

### Task 3: Cost details endpoint (per-model breakdown)

**Objetivo:** Extender el endpoint de costes actual para incluir desglose por modelo.

**Endpoint:** `GET /console/api/myownclone/ai-models/costs` (extender respuesta existente)

**Step 1:** En el método `get()` de `AIModelCostsApi`, añadir campo `by_model`:
```python
by_model = {}
stmt = select(AIInvocation).where(AIInvocation.created_at >= since.replace(tzinfo=None))
if tenant_id:
    stmt = stmt.where(AIInvocation.tenant_id == tenant_id)
rows = db.session.execute(stmt.order_by(AIInvocation.created_at.asc())).scalars().all()
for row in rows:
    key = f"{row.model_id or 'unknown'}"
    entry = by_model.setdefault(key, {"model_id": key, "invocations": 0, "prompt_tokens": 0, "completion_tokens": 0})
    entry["invocations"] += 1
    entry["prompt_tokens"] += row.prompt_tokens or 0
    entry["completion_tokens"] += row.completion_tokens or 0

return {
    "series": list(daily.values()),
    "totals": totals,
    "by_model": list(by_model.values()),
}, 200
```

**Step 2:** Test: `test_cost_by_model_breakdown`.

---

### Task 4: AI Backfill trigger endpoint

**Objetivo:** POST endpoint que ejecute el backfill desde la UI admin.

**Endpoint:** `POST /console/api/myownclone/ai-models/backfill`

**Step 1:** Añadir endpoint en `ai_models.py`:
```python
@console_ns.route("/myownclone/ai-models/backfill")
class AIModelBackfillApi(Resource):
    @login_required
    def post(self):
        from api.commands.ai_backfill import run_backfill
        report = run_backfill(dry_run=False)
        return report, 200
```

**Step 2:** Test: `test_backfill_endpoint`.

---

## Fase 2 — Frontend: Nuevos paneles en el admin

### Task 5: Registry Status panel (dentro de ia-modelos)

**Objetivo:** Sección colapsable en `/admin/ia-modelos` que muestre estado del balanceador.

**File:** `MyOwnClone/src/app/admin/ia-modelos/page.tsx`

**Step 1:** Añadir hook `useAdminFetch` para registry-status:
```tsx
const { data: registryStatus } = useAdminFetch<RegistryStatusResponse>("/api/admin/ai-models/registry-status");
```

**Step 2:** Añadir tipo `RegistryStatusResponse`:
```tsx
interface RegistryStatusResponse {
  ttl_seconds: number;
  cache_size: number;
  tasks: Array<{
    task: string;
    provider: string | null;
    model_id: string | null;
    source: string;
    cache_hit: boolean;
  }>;
}
```

**Step 3:** Renderizar sección después del playground existente:
```tsx
<section className="card space-y-4">
  <div className="stat-label">Model Registry · Balancer</div>
  <div className="text-xs text-[var(--text-muted)]">TTL: {registryStatus?.ttl_seconds}s · Cache entries: {registryStatus?.cache_size}</div>
  {registryStatus?.tasks.map(t => (
    <div key={t.task} className="flex justify-between text-sm">
      <span className="badge-active">{t.task}</span>
      <span className="font-mono text-[11px]">{t.provider} / {t.model_id}</span>
      <span className={t.cache_hit ? "badge-active" : "badge-warning"}>{t.source}</span>
    </div>
  ))}
</section>
```

---

### Task 6: Embedding Status panel (dentro de ia-modelos)

**Objetivo:** Sección que muestre constantes de embedding.

**Step 1:** Hook + tipo:
```tsx
interface EmbeddingStatus {
  max_embed_texts: number;
  embedding_dimensions: number;
  client_batch_size: number;
}
const { data: embeddingStatus } = useAdminFetch<EmbeddingStatus>("/api/admin/ai-models/embedding-status");
```

**Step 2:** Renderizar:
```tsx
<section className="card space-y-4">
  <div className="stat-label">Embedding Configuration</div>
  <div className="grid grid-cols-3 gap-4 text-sm">
    <div>MAX texts: <span className="font-mono">{embeddingStatus?.max_embed_texts}</span></div>
    <div>Dimensions: <span className="font-mono">{embeddingStatus?.embedding_dimensions}</span></div>
    <div>Client batch: <span className="font-mono">{embeddingStatus?.client_batch_size}</span></div>
  </div>
</section>
```

---

### Task 7: Cost By Model panel (dentro de ia-modelos)

**Objetivo:** Tabla de costes por modelo debajo del gráfico de barras existente.

**Step 1:** Añadir `by_model` al tipo `CostsResponse`:
```tsx
interface CostsResponse {
  series: Array<...>;
  totals: {...};
  by_model: Array<{model_id: string; invocations: number; prompt_tokens: number; completion_tokens: number}>;
}
```

**Step 2:** Renderizar tabla debajo del `<BarChart>`:
```tsx
{(costs?.by_model?.length ?? 0) > 0 && (
  <div className="mt-4">
    <div className="stat-label mb-2">By model</div>
    <table className="w-full text-xs">
      <thead><tr><th>Model</th><th>Calls</th><th>Prompt</th><th>Completion</th></tr></thead>
      <tbody>
        {costs.by_model.map(m => (
          <tr key={m.model_id}>
            <td className="font-mono">{m.model_id}</td>
            <td>{m.invocations}</td>
            <td>{m.prompt_tokens}</td>
            <td>{m.completion_tokens}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
)}
```

---

### Task 8: Backfill Trigger button

**Objetivo:** Botón en ia-modelos que ejecute el backfill y muestre resultado.

**Step 1:** Añadir estado y handler:
```tsx
const [backfillResult, setBackfillResult] = useState<string | null>(null);
const [backfilling, setBackfilling] = useState(false);

async function runBackfill() {
  setBackfilling(true);
  const res = await fetch("/api/admin/ai-models/backfill", { method: "POST" });
  const data = await res.json();
  setBackfillResult(JSON.stringify(data, null, 2));
  setBackfilling(false);
  reloadModels();
  reloadAssignments();
}
```

**Step 2:** Botón en el header de la página:
```tsx
<button type="button" className="btn-secondary text-xs" disabled={backfilling} onClick={runBackfill}>
  {backfilling ? "Backfilling..." : "Backfill from env"}
</button>
```

**Step 3:** Mostrar resultado si existe:
```tsx
{backfillResult && (
  <pre className="mt-2 text-[11px] font-mono bg-[var(--bg-card)] p-3 rounded max-h-40 overflow-auto">{backfillResult}</pre>
)}
```

---

### Task 9: Navigation — Añadir "Registry" y "Embeddings" al sidebar

**Objetivo:** Enlaces en el sidebar admin para navegación rápida.

**File:** `MyOwnClone/src/lib/nav-admin.ts`

Añadir después de "AI models":
```tsx
{
  href: "/admin/ia-modelos/balanceador",
  label: "Registry",
  iconKey: "cerebro",
  tooltip: "Model balancer status",
  section: "platform",
},
{
  href: "/admin/ia-modelos/embeddings",
  label: "Embeddings",
  iconKey: "cerebro",
  tooltip: "Embedding config",
  section: "platform",
},
```

---

## Fase 3 — Tests y verificación

### Task 10: Ejecutar tests backend

```bash
cd api
python3 -m pytest api/tests/test_admin_ai_models_panels.py -v
# Expected: 4 tests pass
```

### Task 11: TypeScript check frontend

```bash
cd MyOwnClone
npx tsc --noEmit
# Expected: no errors
```

### Task 12: Build y smoke test

```bash
cd MyOwnClone
npm run build
# Expected: success, 0 errors
curl http://127.0.0.1:3000/admin/ia-modelos  # 307 (auth)
```

---

## Fase 4 — Documentación y deploy

### Task 13: Escribir evidence M14

**File:** `.sisyphus/evidence/task-M14-admin-panels.md`

Secciones: Context, Changes (endpoints + frontend), Verification (comandos y resultados), Open risks.

### Task 14: Commit y push

```bash
git add -A
git commit -m "feat(admin): M14 — balanceador, embeddings, costes por modelo, backfill UI"
git push origin audit/sisyphus-vps-integration
```

### Task 15: Actualizar progress.json

Marcar M14 como `done` con SHA del commit.

---

## Riesgos

- **API del VPS puede caer:** hacer deploy tras verificar tests localmente
- **Weaviate reinicia:** si el container está restarting, necesitará `docker compose up -d`
- **i18n:** las labels nuevas van en inglés; el usuario puede pedir traducción a español después

---

## Orden de ejecución

Fase 1 (backend) → Fase 2 (frontend) → Fase 3 (tests) → Fase 4 (docs + push)

Cada fase es dependiente de la anterior. Dentro de cada fase, las tareas son secuenciales.
