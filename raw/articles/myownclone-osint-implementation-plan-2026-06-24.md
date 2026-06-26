# MyOwnClone — Plan de Implementación: Replicar MyClone.is

## Fuente de Verdad
- **MyClone.is API**: https://api.myclone.is (227 endpoints, OpenAPI)
- **MyOwnClone local**: `/home/haxth3/myownclone_local/` (Flask API) + `/home/haxth3/MyOwnClone/MyOwnClone/` (Next.js)
- **Login test**: xoyigo3386@disiok.com / 2cji!6Tbhc3RLp@ (cuenta creator)

---

## Gap Analysis: MyOwnClone vs MyClone.is

### ✅ Lo que MyOwnClone YA tiene

| Feature | MyOwnClone | MyClone | Gap |
|---------|-----------|---------|-----|
| Chat streaming SSE | ✅ (`/clones/<slug>/chat`) | ✅ | Muy parejo |
| Clone/persona creation | ✅ (`CloneConfig`) | ✅ | — |
| Modos (teach/support/sales) | ✅ (`CloneSilo`) | ❌ (no tiene modos) | Ventaja MyOwnClone |
| Memories/Signatures/Templates | ✅ (`CreatorMemory`) | ❌ (no tiene esto) | Ventaja MyOwnClone |
| Knowledge library (PDF/YT/web) | ✅ (`/biblioteca`) | ✅ | — |
| Email inbound/reply | ✅ | ✅ | — |
| LLM via Dify | ✅ | ❌ (usa OpenAI directo) | — |
| Voice cloning | ❓ | ✅ (Cartesia + ElevenLabs) | MyClone gana |
| Multi-tenant | ✅ | ✅ | — |

### ❌ Lo que MyOwnClone NO tiene (prioridad alta)

#### 1. Prompt Versioning (CRÍTICO)
**MyClone tiene:**
- `persona_prompt_versions` table → cada cambio = nueva versión
- `GET /prompt/persona-prompts/{id}/history` → lista de versiones
- `POST /prompt/persona-prompts/{id}/restore/{version}` → restore
- `GET /prompt/persona-prompts/{id}/compare` → diff
- `GET /prompt/persona-prompts/{id}/timeline` → línea temporal

**MyOwnClone tiene:**
```python
class CloneModePrompt(DefaultFieldsDCMixin, TypeBase):
    clone_id: Mapped[str]
    mode: Mapped[str]           # "teach"/"support"/"sales"
    system_prompt: Mapped[str]  # UN SOLO campo, sin historial
    is_active: Mapped[bool]
```

**Gap:** No hay historial, no hay restore, no hay diff. Cada `PUT` sobrescribe sin guardar anterior.

---

#### 2. Visitor / Lead Management (ALTA)
**MyClone tiene:**
- `GET /personas/{id}/visitors` → lista de leads
- `POST /sessions/{token}/capture-lead` → captura email post-chat
- `PersonaVisitorResponse`: id, email, firstName, lastName, addedAt, lastAccessedAt
- Lead scoring system con `OutputTemplate` (sections: profile, situation, need, score, key_context, follow_up_questions)

**MyOwnClone tiene:**
- `Feedback` model en `analytics.py` (rating nada más)
- No captura de leads post-chat
- No visitor tracking

**Gap:** MyOwnClone no sabe quién visita sus clones.

---

#### 3. Workflows BETA — Conversation Flows (ALTA)
**MyClone tiene:**
- Workflow templates por industria (CPA, Tax, Insurance, Legal)
- `POST /workflows` → crear workflow
- `POST /workflows/sessions` → iniciar sesión de workflow
- `POST /workflows/sessions/{id}/answer` → responder a un paso
- `GET /workflows/{id}/analytics` → métricas
- Cada workflow tiene `objectives` (pasos con preguntas)
- `regenerate-objective` → LLM genera nuevos objetivos

**MyOwnClone tiene:**
- ❌ Nada de workflows
- Solo chat libre (sin flujo estructurado)

---

#### 4. Langfuse Integration — Prompt Observability (MEDIA)
**MyClone tiene:**
- `/langfuse/prompts/compile` → compila prompt con variables
- `/langfuse/prompts/create` → crea prompt en Langfuse
- `/langfuse/prompts/list` → lista todos
- `/langfuse/prompts/update/{name}` → actualiza
- Prompt-level metrics: latency, token usage, quality scores
- Custom evals: `llm-rag`, `llm-judge`

**MyOwnClone tiene:**
- ❌ Sin observabilidad de prompts
- Sin evaluación de calidad de respuestas
- Sin tracking de tokens por prompt

---

#### 5. Stripe Connect — Creator Monetization (MEDIA)
**MyClone tiene:**
- `POST /stripe/personas/{id}/monetization` → activar pagos
- `POST /stripe/personas/{id}/connect/onboard` → onboarding Stripe Connect
- Pricing models: one_time, subscription, one_time_duration
- Per-persona payment (creators cobran por acceso a su clone)

**MyOwnClone tiene:**
- ❌ No tiene monetización
- Solo plans de plataforma (el usuario paga, no gana)

---

#### 6. Custom Domains / Whitelabel (MEDIA)
**MyClone tiene:**
- `POST /custom-domains` → añadir dominio
- `GET /custom-domains/lookup/{domain}` → verificar DNS
- `POST /custom-domains/{id}/verify` → verificar propiedad
- Límite por tier (pro: 10, business: 10, enterprise: -1)

**MyOwnClone tiene:**
- Campo `custom_domain` en `CloneConfig` (existe, no se usa activamente)

---

#### 7. LiveKit — Real-time Voice (BAJA)
**MyClone tiene:**
- `POST /livekit/connection-details` → obtener credenciales LiveKit room
- `POST /livekit/session/{id}/heartbeat` → keepalive
- Voz real-time durante chat

**MyOwnClone tiene:**
- ❌ No tiene voz

---

## Plan de Implementación: Paso a Paso

### FASE 1: Fundacional (Semana 1-2)

#### Step 1: Prompt Versioning — Backend
**Archivos a modificar:**
1. `/home/haxth3/myownclone_local/api/api/models/clone.py`
   - Crear tabla `PersonaPromptVersion` (mirrors `CloneModePrompt` + `version_number`, `created_at`, `change_summary`)
   - Crear tabla `PersonaPromptHistory` (id, persona_id, mode, version_number, system_prompt, created_at, created_by, change_summary)

2. `/home/haxth3/myownclone_local/api/api/controllers/console/myownclone/clone.py`
   - Modificar `PUT /myownclone/clones/<clone_id>/prompts` para:
     - Guardar versión anterior en `PersonaPromptHistory` ANTES de actualizar
     - Generar `change_summary` (diff simple)
   - Crear `GET /myownclone/clones/<clone_id>/prompts/history` → lista versiones
   - Crear `POST /myownclone/clones/<clone_id>/prompts/restore/<version>` → restore
   - Crear `GET /myownclone/clones/<clone_id>/prompts/diff?v1=X&v2=Y` → diff

**API resultante:**
```bash
PUT  /myownclone/clones/{id}/prompts         # Actualiza y crea versión
GET  /myownclone/clones/{id}/prompts/history # Lista versiones
POST /myownclone/clones/{id}/prompts/restore/{version}  # Restaura versión
GET  /myownclone/clones/{id}/prompts/diff?v1=1&v2=3    # Diff entre versiones
```

---

#### Step 2: Prompt Versioning — Frontend
**Archivos a modificar:**
1. `/home/haxth3/MyOwnClone/MyOwnClone/src/app/(dashboard)/cerebro/page.tsx`
   - Añadir tab "Historial" junto a Memories/Signatures/Templates
   - Mostrar lista de versiones con fecha y summary
   - Botón "Restaurar" en cada versión
   - Vista de diff (resaltar cambios)

---

#### Step 3: Lead Capture — Backend
**Archivos a modificar:**
1. `/home/haxth3/myownclone_local/api/api/models/clone.py`
   - Crear tabla `Visitor` (id, persona_id, email, first_name, last_name, created_at, last_accessed_at)
   - Crear tabla `LeadCapture` (id, session_token, visitor_id, captured_at, source)

2. `/home/haxth3/myownclone_local/api/api/controllers/myownclone_public.py`
   - En `chat_public`, guardar `session_token` para tracking
   - Crear `POST /api/myownclone/public/clones/<slug>/capture-lead` → captura email post-chat

3. `/home/haxth3/myownclone_local/api/api/controllers/console/myownclone/clone.py`
   - Crear `GET /myownclone/clones/<clone_id>/visitors` → lista de leads
   - Crear `GET /myownclone/clones/<clone_id>/analytics/visitors` → métricas

---

#### Step 4: Lead Capture — Frontend
**Archivos a modificar:**
1. Añadir `/visitors` o usar `/analiticas` existente
2. Post-chat: mostrar popup "Ingresa tu email para continuar" (después de 3 mensajes)
3. Dashboard de visitors: tabla con email, fecha, última visita

---

### FASE 2: Crecimiento (Semana 3-4)

#### Step 5: Workflows — Data Model
**Tablas necesarias:**
```python
class WorkflowTemplate(DefaultFieldsDCMixin, TypeBase):
    # template_key, template_name, template_category, workflow_type
    # minimum_plan_tier_id, workflow_config (JSON), output_template (JSON)

class PersonaWorkflow(DefaultFieldsDCMixin, TypeBase):
    # persona_id, template_id, workflow_config (copiado del template)
    # is_customized, published_at, synced_version

class WorkflowSession(DefaultFieldsDCMixin, TypeBase):
    # workflow_id, conversation_id, status (active/completed/abandoned)
    # current_step, session_metadata (JSON)
```

#### Step 6: Workflows — API Routes
- `GET /workflow-templates` → lista templates disponibles
- `POST /workflows` → crear workflow para persona
- `POST /workflows/sessions` → iniciar sesión
- `POST /workflows/sessions/{id}/answer` → responder paso
- `GET /workflows/{id}/analytics` → métricas

#### Step 7: Workflows — Frontend
- Nueva ruta `/workflows` en dashboard
- Selector de template por industria
- UI de conversación con pasos (wizard-style)
- Tracking de progreso por sesión

---

### FASE 3: Monetización (Semana 5-6)

#### Step 8: Stripe Connect Setup
1. Registrar app en Stripe Connect
2. Añadir `stripe_account_id` a `CloneConfig`
3. Endpoints de onboarding: `POST /stripe/connect/onboard`
4. Checkout: `POST /stripe/checkout/persona-access`

---

### FASE 4: Avanzado (Semana 7+)

#### Step 9: Langfuse Integration
- Crear cuenta en Langfuse
- Instrumentar prompts con `langfuse.callback()`
- Crear prompt registry: `POST /langfuse/prompts/create`
- Dashboard de calidad de prompts

#### Step 10: Voice Cloning (Cartesia + ElevenLabs)
- Integrar APIs de voice cloning
- Endpoints ya documentados en OpenAPI de MyClone

#### Step 11: Custom Domains
- DNS verification flow
- SSL automático con Let's Encrypt
- UI en `/configuracion`

---

## Priority Matrix

| Step | Feature | Impact | Effort | Priority |
|------|---------|--------|--------|----------|
| 1 | Prompt Versioning (BE) | Alta | Media | 🔴 ALTA |
| 2 | Prompt Versioning (FE) | Alta | Media | 🔴 ALTA |
| 3 | Lead Capture (BE) | Alta | Baja | 🔴 ALTA |
| 4 | Lead Capture (FE) | Alta | Baja | 🔴 ALTA |
| 5 | Workflows (Model) | Alta | Alta | 🟡 MEDIA |
| 6 | Workflows (API) | Alta | Alta | 🟡 MEDIA |
| 7 | Workflows (FE) | Alta | Alta | 🟡 MEDIA |
| 8 | Stripe Connect | Media | Alta | 🟡 MEDIA |
| 9 | Langfuse | Media | Media | 🟢 BAJA |
| 10 | Voice Cloning | Media | Alta | 🟢 BAJA |
| 11 | Custom Domains | Media | Media | 🟢 BAJA |

---

## Notas de Implementación

### Dify como LLM (MyOwnClone) vs OpenAI directo (MyClone)
- MyOwnClone usa Dify para inferencia — los cambios de prompt deben pasar por Dify
- La compilación de prompt (rellenar variables como `{name}`, `{role}`) debe happen BEFORE sending to Dify
- MyClone usa `{{variable}}` en prompts, MyOwnClone debe soportarlo igual

### Sistema de modos MyOwnClone (único)
- MyOwnClone tiene `CloneSilo.TEACH/SUPPORT/SALES` — MyClone NO tiene esto
- El prompt versioning debe funcionar POR modo
- Mantener esta ventaja competitiva

### Auth
- MyOwnClone usa JWT vía Flask (NextAuth en frontend)
- Los nuevos endpoints deben usar `@token_required` decorator
- Ver `auth.py` en `controllers/` para patrón actual

---

## Comandos de Verificación

```bash
# Backend local
cd /home/haxth3/myownclone_local/api
python -m api.app_factory

# Frontend local
cd /home/haxth3/MyOwnClone/MyOwnClone
npm run dev

# Verificar rutas existentes
grep -r "route\|@.*route" /home/haxth3/myownclone_local/api/api/controllers/

# Verificar modelos
grep -r "class.*Base\|Mapped\[" /home/haxth3/myownclone_local/api/api/models/
```
