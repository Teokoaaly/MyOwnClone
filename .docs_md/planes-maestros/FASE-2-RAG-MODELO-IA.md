# FASE 2 — RAG Pipeline + Modelo IA + Widget

> **Objetivo**: Conectar el conocimiento que suben los usuarios al chat. Añadir fallback de LLM. Crear widget embebible competitivo.
> **Tiempo estimado**: 3-5 días
> **Urgencia**: 🟡 Importante
> **Prerequisitos**: FASE 1 completada, especialmente T1.4 (embedding tipo vector)

---

## Tasks

### T2.1 — Pipeline de ingestion RAG (P0-01 del OSINT)

**Problema**: El usuario sube conocimiento (PDF, texto, URL) desde `/biblioteca/nuevo` pero ese contenido **NO llega al RAG**. El backend tiene stubs y el chat no recupera contexto.

**Estado actual** (verificado en DB):
- Tabla `sources`: 3 filas seed (status="ready")
- Tabla `chunks`: 3 filas seed
- Sin pipeline real de chunking → embedding → insert

**Solución**: Implementar pipeline completo de ingestion.

#### Arquitectura del pipeline

```
Usuario sube fuente (PDF/texto/URL)
  → POST /console/api/myownclone/sources
  → api/controllers/.../clone.py crea registro en `sources` (status=processing)
  → api/core/ingestion.py:
      1. Extraer texto (PDF → PyPDF2, URL → BeautifulSoup, texto → directo)
      2. Chunking (langchain TextSplitter o custom, 500 tokens overlap 50)
      3. Embedding (EmbeddingService.embed_texts → Ollama mxbai-embed-large)
      4. INSERT INTO chunks (source_id, content, embedding, token_count, metadata)
  → UPDATE sources SET status='ready' WHERE id=...

Chat público:
  → POST /api/clone/{slug}/chat
  → api/core/retrieval.py:
      1. Embedding del query del usuario
      2. SELECT * FROM chunks WHERE source_id IN (clone sources)
         ORDER BY embedding <=> query_embedding LIMIT 5
      3. Construir prompt con contexto recuperado
      4. LLM call (MiniMax o fallback)
```

#### Pasos

1. **Crear `api/core/ingestion.py`**:
```python
"""Pipeline de ingestion: fuente → chunks → embeddings → DB."""
import logging
from typing import Optional
from api.extensions.ext_database import db
from api.models import Chunk, Source

logger = logging.getLogger(__name__)

def ingest_source(source_id: str) -> None:
    """Procesa una fuente: extrae texto, hace chunks, embeddea y guarda."""
    source = db.session.get(Source, source_id)
    if not source:
        logger.error("Source %s no encontrada", source_id)
        return

    try:
        # 1. Extraer texto según tipo
        raw_text = _extract_text(source)
        if not raw_text.strip():
            _fail(source, "Sin contenido extraíble")
            return

        # 2. Chunking
        chunks = _split_text(raw_text, chunk_size=500, overlap=50)

        # 3. Embeddings (batch)
        from api.core.embeddings import EmbeddingService
        embedder = EmbeddingService()
        embeddings = embedder.embed_texts(chunks)

        # 4. INSERT
        for text, embedding in zip(chunks, embeddings):
            chunk = Chunk(
                source_id=source_id,
                content=text,
                embedding=embedding,
                token_count=len(text.split()),  # aproximado
                metadata={"chunk_index": chunks.index(text)},
            )
            db.session.add(chunk)

        source.status = "ready"
        db.session.commit()
        logger.info("Source %s ingerida: %d chunks", source_id, len(chunks))

    except Exception as e:
        logger.exception("Error ingiriendo source %s", source_id)
        _fail(source, str(e))


def _extract_text(source) -> str:
    """Extrae texto según el tipo de fuente."""
    if source.url:
        return _extract_from_url(source.url)
    elif source.raw_content:
        return source.raw_content
    # TODO: PDF, YouTube transcript, etc.
    return ""


def _extract_from_url(url: str) -> str:
    import requests
    from bs4 import BeautifulSoup
    resp = requests.get(url, timeout=30)
    soup = BeautifulSoup(resp.text, "html.parser")
    # Limpiar scripts, styles
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)


def _split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Divide texto en chunks solapados por número de palabras."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        if end >= len(words):
            break
        start = end - overlap
    return chunks


def _fail(source, reason: str):
    source.status = "failed"
    source.error_message = reason
    db.session.commit()
```

2. **Conectar el endpoint POST /sources** para llamar al pipeline:
```python
# En api/controllers/console/myownclone/clone.py
# Después de crear el Source:
from api.core.ingestion import ingest_source
source = Source(...)
db.session.add(source)
db.session.commit()

# Ingestion sincrónica (para fuentes pequeñas)
# TODO: async con Celery/RQ para fuentes grandes
ingest_source(str(source.id))
```

3. **Implementar retrieval real** en `api/core/retrieval.py`:
```python
"""Retrieval: encuentra chunks relevantes para un query."""
from sqlalchemy import select, text as sql_text
from api.extensions.ext_database import db
from api.models import Chunk, Source

def retrieve_context(query: str, clone_id: str, top_k: int = 5) -> list[dict]:
    """Recupera los chunks más relevantes para el query."""
    # 1. Embedding del query
    from api.core.embeddings import EmbeddingService
    embedder = EmbeddingService()
    query_embedding = embedder.embed_texts([query])[0]

    # 2. Búsqueda vectorial en chunks del clone
    # pgvector operator <=> (cosine distance)
    sources_subquery = (
        select(Source.id)
        .where(Source.clone_id == clone_id)
        .scalar_subquery()
    )
    results = db.session.execute(
        select(Chunk)
        .where(Chunk.source_id.in_(sources_subquery))
        .order_by(Chunk.embedding.cosine_distance(query_embedding))
        .limit(top_k)
    ).scalars().all()

    return [
        {"content": r.content, "score": 1.0, "metadata": r.metadata}
        for r in results
    ]
```

4. **Tests**:
```python
# tests/test_ingestion.py
def test_ingest_text_source():
    """Subir texto → chunks creados → embedding no vacío."""
    # ...
```

#### Verificación
```bash
# Subir fuente de prueba
curl -X POST http://127.0.0.1:5001/console/api/myownclone/sources \
  -H "Authorization: Bearer <token>" \
  -d '{"title":"Test","content":"Este es un texto de prueba","clone_id":"..."}'

# Verificar chunks creados
docker exec myownclone_postgres psql -U postgres -d myownclone -c \
  "SELECT count(*) FROM chunks;"

# Hacer query al chat
curl -X POST http://127.0.0.1:5001/api/myownclone/clone/<slug>/chat \
  -d '{"message":"¿Qué es MyOwnClone?"}'
# La respuesta debe incluir información del contexto
```

#### Rollback
- Revertir cambios en `clone.py` (quitar llamada a `ingest_source`)
- El chat seguirá funcionando sin RAG (como ahora)

---

### T2.2 — Fallback de LLM (OpenAI/Anthropic además de MiniMax)

**Problema**: Solo MiniMax como LLM de chat. Si la API de MiniMax cae, el chat deja de funcionar.

**Solución**: Añadir OpenAI como fallback en el catálogo IA.

#### Pasos

1. **Registrar OpenAI en el catálogo**:
```sql
INSERT INTO ai_models (id, name, provider, model_id, api_key_encrypted, is_active, input_price_cents_per_mtok, output_price_cents_per_mtok)
VALUES (
  gen_random_uuid()::varchar,
  'OpenAI GPT-4o mini',
  'openai',
  'gpt-4o-mini',
  '',  -- encriptar API key con SecretCipher
  true,
  150,  -- $1.50/MTok input
  600   -- $6.00/MTok output
);
```

2. **Crear asignación de fallback**:
```sql
INSERT INTO ai_model_assignments (task, model_id, tenant_id, priority)
VALUES ('chat_fallback', '<openai_model_id>', NULL, 200);
```

3. **Verificar que el RetryClient hace failover**:
```python
# api/core/retry_client.py debe ya soportar failover
# Verificar que al fallar MiniMax, intenta OpenAI
```

4. **Configurar API key de OpenAI** en production:
```bash
# En el VPS:
# Cifrar la API key con el CLI de crypto
docker exec myownclone_api flask --app api.app_factory generate-encrypted-key
# Actualizar el registro en ai_models
```

#### Verificación
- `SELECT * FROM ai_models WHERE provider='openai'` muestra el modelo
- Al simular fallo de MiniMax, el chat sigue funcionando con OpenAI

---

### T2.3 — Soporte de PDF en ingestion

**Problema**: El pipeline de ingestion (T2.1) solo maneja texto plano y URLs. Los PDFs no se procesan.

**Solución**: Añadir extracción de PDF con `PyPDF2`.

#### Pasos

1. **Añadir dependencia** en `api/requirements.txt`:
```
PyPDF2>=3.0.0
```

2. **Implementar extracción** en `api/core/ingestion.py`:
```python
def _extract_from_pdf(file_path: str) -> str:
    """Extrae texto de un PDF."""
    from PyPDF2 import PdfReader
    reader = PdfReader(file_path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return "\n".join(text)
```

3. **Modificar `_extract_text`** para detectar PDFs.

#### Verificación
- Subir un PDF de prueba
- Verificar chunks creados con contenido del PDF

---

### T2.4 — Soporte de YouTube (transcripciones)

**Problema**: Los usuarios quieren entrenar su clon con videos de YouTube.

**Solución**: Extraer transcripciones con `youtube-transcript-api`.

#### Pasos

1. **Añadir dependencia**:
```
youtube-transcript-api>=0.6.0
```

2. **Implementar extractor** en `api/core/ingestion.py`:
```python
def _extract_from_youtube(url: str) -> str:
    """Extrae transcripción de un video de YouTube."""
    from youtube_transcript_api import YouTubeTranscriptApi
    video_id = _extract_youtube_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry["text"] for entry in transcript])
```

#### Verificación
- Subir URL de YouTube con subtítulos
- Verificar chunks con la transcripción

---

### T2.5 — Widget embebible (como myclone.is)

**Problema**: myclone.is tiene `myclone-embed.js` que permite embeber widgets en webs externas. MyOwnClone tiene `ChatPanel mode="inline"` pero no está pulido para embed externo.

**Solución**: Crear script de embed distribuibre.

#### Arquitectura

```
Web del cliente:
  <script src="https://myownclone.com/embed/widget.js"
          data-clone="creator-slug"
          data-mode="support">
  </script>
  <div id="myownclone-widget"></div>

widget.js:
  1. Crea iframe apuntando a https://myownclone.com/embed/<slug>?mode=<mode>
  2. El iframe renderiza ChatPanel mode="inline"
  3. Comunicación vía postMessage para resize/eventos
```

#### Pasos

1. **Crear ruta `/embed/[slug]`** en Next.js que renderice SOLO el ChatPanel (sin layout completo):
```tsx
// MyOwnClone/src/app/embed/[slug]/page.tsx
export default function EmbedPage({ params }: { params: { slug: string } }) {
  return (
    <div className="embed-container">
      <ChatPanel
        mode="inline"
        cloneSlug={params.slug}
        showHeader={false}
      />
    </div>
  );
}
```

2. **Crear `public/embed/widget.js`**:
```javascript
(function() {
  const scripts = document.querySelectorAll('script[src*="widget.js"]');
  scripts.forEach(script => {
    const clone = script.dataset.clone;
    const mode = script.dataset.mode || 'support';
    const container = document.createElement('div');
    container.id = 'myownclone-widget-' + clone;
    const iframe = document.createElement('iframe');
    iframe.src = `https://myownclone.com/embed/${clone}?mode=${mode}`;
    iframe.style.width = '100%';
    iframe.style.height = '500px';
    iframe.style.border = 'none';
    iframe.style.borderRadius = '12px';
    container.appendChild(iframe);
    script.parentNode.insertBefore(container, script.nextSibling);
  });
})();
```

3. **Permitir iframe embebido** en nginx (quitar `X-Frame-Options: DENY` para rutas `/embed/`):
```nginx
location /embed/ {
    # Permitir embebido
    proxy_set_header X-Frame-Options "SAMEORIGIN";
    proxy_pass http://127.0.0.1:3000;
}
```

#### Verificación
```html
<!-- HTML de prueba -->
<script src="https://myownclone.com/embed/widget.js" data-clone="demo-clone"></script>
```
- El widget carga y funciona el chat

---

### T2.6 — Demos interactivas en landing (como myclone.is)

**Problema**: myclone.is tiene demos con personas preconfiguradas (insurance-quoter, hvac-dispatch, restaurant). MyOwnClone no tiene demos.

**Solución**: Crear 3 clones demo seed + componentes showcase.

#### Pasos

1. **Crear 3 clones demo en la DB**:
```sql
-- Asegurar que existen los clones demo
INSERT INTO clone_configs (id, clone_id, name, slug, mode, ...) VALUES
  ('demo-insurance', 'demo-insurance', 'Insurance Quoter', 'demo-insurance', 'sales', ...),
  ('demo-support', 'demo-support', 'Support Agent', 'demo-support', 'support', ...),
  ('demo-teacher', 'demo-teacher', 'Knowledge Teacher', 'demo-teacher', 'teach', ...);
```

2. **Sembrar conocimiento para cada demo**:
```sql
-- Sources + chunks para cada demo
INSERT INTO sources (...) VALUES (...);
INSERT INTO chunks (...) VALUES (...);
```

3. **Crear componente `UseCasesShowcase`** en el frontend:
```tsx
// MyOwnClone/src/components/landing/UseCasesShowcase.tsx
export function UseCasesShowcase() {
  const demos = [
    { slug: 'demo-insurance', title: 'Agente de Seguros', icon: '🛡️' },
    { slug: 'demo-support', title: 'Soporte Técnico', icon: '🔧' },
    { slug: 'demo-teacher', title: 'Profesor de IA', icon: '🎓' },
  ];
  return (
    <section className="py-20">
      <h2>Pruébalo en acción</h2>
      <div className="grid grid-cols-3 gap-6">
        {demos.map(demo => (
          <DemoCard key={demo.slug} {...demo} />
        ))}
      </div>
    </section>
  );
}
```

4. **Añadir al landing page** en `app/page.tsx`.

#### Verificación
- Landing muestra 3 demos interactivas
- Cada demo tiene un chat funcional

---

### T2.7 — Testimonios en landing

**Problema**: myclone.is tiene testimonios con fotos. MyOwnClone no tiene.

**Solución**: Crear componente `Testimonials` con datos reales (cuando haya usuarios) o placeholders honestos.

#### Pasos

1. **Crear componente**:
```tsx
// MyOwnClone/src/components/landing/Testimonials.tsx
export function Testimonials() {
  // TODO: reemplazar con testimonios reales cuando haya usuarios
  const testimonials = [
    { name: "Tu testimonio aquí", role: "Beta user", quote: "..." },
  ];
  // Renderizar marquee o grid
}
```

⚠️ **No inventar testimonios falsos.** Usar placeholders honestos hasta tener reales.

---

### T2.8 — Analytics con PostHog

**Problema**: PostHog está en env vars pero no configurado. myclone.is usa PostHog + GA4.

**Solución**: Configurar PostHog para tracking real.

#### Pasos

1. **Crear cuenta en PostHog** (gratis hasta 1M eventos/mes).
2. **Configurar env vars**:
```bash
# En frontend.env.production:
NEXT_PUBLIC_POSTHOG_HOST=https://app.posthog.com
NEXT_PUBLIC_POSTHOG_KEY=phc_xxx
```

3. **Añadir PostHog provider** en Next.js layout:
```tsx
// MyOwnClone/src/app/layout.tsx
import posthog from 'posthog-js';
import { PostHogProvider } from 'posthog-js/react';

if (typeof window !== 'undefined') {
  posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY!, {
    api_host: process.env.NEXT_PUBLIC_POSTHOG_HOST!,
  });
}
```

4. **Trackear eventos clave**: signup, chat_sent, source_uploaded, plan_selected.

#### Verificación
- PostHog dashboard muestra eventos en tiempo real

---

### T2.9 — Auth con LinkedIn (como myclone.is)

**Problema**: myclone.is ofrece login con LinkedIn. MyOwnClone solo Google + email.

**Solución**: Añadir LinkedIn OAuth provider.

#### Pasos

1. **Crear app en LinkedIn Developer** → obtener Client ID + Secret.
2. **Configurar NextAuth**:
```typescript
// MyOwnClone/src/lib/auth.ts
providers: [
  GoogleProvider({...}),
  LinkedInProvider({
    clientId: process.env.AUTH_LINKEDIN_ID,
    clientSecret: process.env.AUTH_LINKEDIN_SECRET,
  }),
]
```

3. **Añadir env vars** y botón en login/registro.

---

### T2.10 — Rate limiting real por tenant

**Problema**: El rate limiting actual usa Redis pero no está claro si se aplica por tenant o por IP.

**Solución**: Verificar y asegurar rate limiting por tenant + IP.

#### Pasos

1. **Auditar rate limiting actual**:
```bash
grep -rn "rate_limit\|RateLimit" api/core/ api/controllers/
```

2. **Asegurar que el rate limit aplica por tenant_id + IP**:
```python
# api/core/rate_limit.py
def check_rate_limit(tenant_id: str, ip: str, limit: int = 100, window: int = 3600):
    key = f"rl:{tenant_id}:{ip}"
    # Redis sliding window
```

#### Verificación
- Hacer 101 requests en 1h desde misma IP → 429

---

### T2.11 — Cost tracking en streaming (Defecto #2 del OSINT)

**Problema**: 4 backends de streaming NO llaman a `_record_llm_cost`. Los costes de IA no se registran para streaming.

**Solución**: Añadir `_record_llm_cost` en todos los paths de streaming.

#### Pasos

1. **Identificar los 4 backends streaming**:
```bash
grep -rn "stream\|yield\|SSE" api/core/model_manager.py api/controllers/
```

2. **Añadir cost tracking después de cada stream complete**:
```python
# En cada path streaming, después del último chunk:
_record_llm_cost(
    tenant_id=g.tenant_id,
    model=model_id,
    tokens_in=prompt_tokens,
    tokens_out=completion_tokens,
    cost_cents=calculate_cost(model, tokens_in, tokens_out),
)
```

#### Verificación
- `SELECT * FROM ai_invocations ORDER BY created_at DESC LIMIT 5` muestra registros de streaming

---

### T2.12 — Configuración de alertas (Sentry/PostHog)

**Problema**: Sin monitoreo de errores en producción.

**Solución**: Configurar Sentry para backend + frontend.

#### Pasos

1. **Backend (Python)**:
```bash
# requirements.txt
sentry-sdk[flask]>=2.0.0
```
```python
# app_factory.py
import sentry_sdk
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=0.1,
)
```

2. **Frontend (Next.js)**:
```bash
npm install @sentry/nextjs
```
```bash
npx @sentry/wizard@latest -i nextjs
```

---

## Resumen FASE 2

| Task | Descripción | Tiempo | Dependencias |
|---|---|---|---|
| T2.1 | Pipeline ingestion RAG | 1-2 días | FASE 1 completa |
| T2.2 | Fallback LLM OpenAI | 4h | Catálogo IA |
| T2.3 | Soporte PDF | 2h | T2.1 |
| T2.4 | Soporte YouTube | 2h | T2.1 |
| T2.5 | Widget embebible | 1 día | Chat funcional |
| T2.6 | Demos landing | 4h | T2.1 + seeds |
| T2.7 | Testimonios | 1h | Ninguna |
| T2.8 | PostHog analytics | 2h | Cuenta PostHog |
| T2.9 | LinkedIn OAuth | 2h | App LinkedIn |
| T2.10 | Rate limit por tenant | 2h | Redis |
| T2.11 | Cost tracking streaming | 3h | Model manager |
| T2.12 | Sentry alertas | 2h | Cuenta Sentry |

**Orden recomendado**: T2.1 → T2.3 → T2.4 → T2.2 → T2.11 → T2.5 → T2.6 → T2.10 → T2.8 → T2.12 → T2.9 → T2.7
