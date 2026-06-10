# 🎯 Plan Maestro: Alinear el Dashboard con el Propósito Real del Producto

> **Problema**: El Command Center del dashboard habla de "build or query", "endpoints, schema design"
> y redirige a una búsqueda textual, cuando el producto REAL es un clon de IA
> que conversa con tus archivos y conocimiento.

---

## 📋 Diagnóstico Actual

### Sección "What do you want to build or query?" (`/resumen`)

| Elemento | Texto actual | Problema |
|---|---|---|
| **Título** | "What do you want to build or query?" | Suena a herramienta de desarrollo, no a clon de IA |
| **Placeholder** | "Ask about endpoints, schema design, or workflow orchestration..." | Habla de schemas y endpoints, no del contenido del usuario |
| **Botón lightning** | "Find the fastest way to launch my AI clone workflow." | Enfocado en "launch workflow", no en conversar |
| **Botón templates** | "Create a workflow that ingests content, answers customer questions, and flags gaps." | Demasiado técnico/genérico |
| **Ejemplos recent query** | "Extract product data from nike.com", "Create extraction schema for blog articles", "Research latest AI compliance regulations" | Suena a web scraping, no a clon de IA |
| **Al enviar** | Redirige a `/biblioteca?query=...` | No es un chat real, es un buscador textual |

### Contraste con la realidad del producto

| Realidad | El dashboard dice |
|---|---|
| El usuario crea un **clon de IA** entrenado con su contenido | "build or query" — parece un API explorer |
| El clon **responde preguntas** basándose en fuentes (PDFs, web, YouTube) | "endpoints, schema design" — suena a documentación técnica |
| El usuario **chatea** con su clon desde el widget o el panel | Redirige a biblioteca (búsqueda textual) |
| El valor es **conversar con tu conocimiento** | Los ejemplos hablan de extraer datos de Nike |

---

## 🗺️ Plan de Corrección por Fases

### Fase 1: Solo textos del Command Center (más impactante, mínimo esfuerzo)

Cambiar los strings en `resumen/page.tsx` para que reflejen el propósito real.

#### 1.1 Título
```
❌ "What do you want to build or query?"
✅ "What would you like to ask your clone?"
```

#### 1.2 Placeholder del textarea
```
❌ "Ask about endpoints, schema design, or workflow orchestration..."
✅ "Ask anything. Your clone will answer from your knowledge base..."
```

#### 1.3 Texto de los botones de ejemplo
```
❌ lightning → "Find the fastest way to launch my AI clone workflow."
✅ lightning → "Explain this concept as if I were a beginner."

❌ templates → "Create a workflow that ingests content, answers questions..."
✅ templates → "Summarize the key ideas from my latest uploads."
```

#### 1.4 Ejemplos de "Your Recent Query"
```
❌ "Extract product data from nike.com..."
❌ "Create extraction schema for blog articles..."
❌ "Research latest AI compliance regulations..."

✅ "What are the main topics covered in my uploaded PDFs?"
✅ "Explain this concept in simple terms for a customer."
✅ "What questions have my users asked that I couldn't answer?"
```

#### 1.5 Acción al enviar
```
❌ router.push(`/biblioteca?query=${encodeURIComponent(trimmed)}`)
✅ router.push(`/inbox?query=${encodeURIComponent(trimmed)}`) o al chat real
```

### Fase 2: Revisar el resto del dashboard

| Ubicación | Texto actual | Debería |
|---|---|---|
| **Get Started > API Key** | "Get started in 5 min" | OK, configuración necesaria |
| **Get Started > Usage** | "Past 30 Days" | OK |
| **Get Started > Docs** | "Docs" → enlace a biblioteca | Confuso. "Library" o "Knowledge Base" |
| **Get Started > Agent Toolkit** | "Agent Toolkit" → enlace a cerebro | ¿Qué es "Agent Toolkit" para el usuario? |
| **Sidebar nav labels** | "Search", "Crawl", "Extract", "Research" | Suenan a herramientas de scraping, no a un clon |

### Fase 3: Sidebar — Renombrar secciones para el usuario real

| Actual | Propuesto | Motivo |
|---|---|---|
| **Search** (Biblioteca) | **Knowledge** | Es donde están las fuentes del clon |
| **Crawl** (Cerebro) | **Memories** | Son las memorias del creador |
| **Extract** (Inbox) | **Inbox** | Es el email, no "extract" |
| **Research** (Productos) | **Products** | Es el catálogo de productos |
| **Usage** (Analíticas) | **Analytics** | "Usage" suena a consumo técnico |
| **API Keys** (Configuración) | **Settings** | Más claro |

### Fase 4: Landing page — Revisar mensajes clave

| Actual | Problema | Propuesto |
|---|---|---|
| "Create an AI clone **that works like you**" | "works like you" es ambiguo | "Create an AI clone **trained on your content**" |
| "Train a clone with your content. Answer questions, reply to emails, and book meetings 24/7..." | OK, esto está bien | — |
| "Start free" / "Watch demo" | OK | — |

---

## 📊 Priorización por Impacto/Esfuerzo

| Tarea | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|
| 1.1 Cambiar título del Command Center | 🔥 Alto | 🟢 1 línea | **P0** |
| 1.2 Cambiar placeholder | 🔥 Alto | 🟢 1 línea | **P0** |
| 1.3 Cambiar botones de ejemplo | 🔥 Alto | 🟢 3 líneas | **P0** |
| 1.4 Cambiar ejemplos de "Recent Query" | 🔥 Alto | 🟢 3 líneas | **P0** |
| 1.5 Cambiar acción al enviar | 🔥 Alto | 🟢 1 línea | **P0** |
| 2. Revisar Get Started cards | 📗 Medio | 🟡 4 líneas | **P1** |
| 3. Sidebar re-naming | 📗 Medio | 🟡 1 archivo | **P1** |
| 4. Landing page tweaks | 📘 Bajo | 🟢 2 líneas | **P2** |

---

## 🧠 Notas Técnicas

### El chat real no existe desde el dashboard

Actualmente el textarea redirige a `/biblioteca?query=...` que es una página de búsqueda.
Para que **realmente** el usuario converse con su clon desde el Command Center,
habría que:

```
Opción A (fácil): Redirigir al chat público del clon → /{slug}
Opción B (media): Redirigir al inbox → /inbox?query=...
Opción C (compleja): Integrar el ChatPanel dentro del Command Center
```

La **Opción A** es la más rápida y la que más sentido tiene:
el usuario escribe → se abre el chat con su clon → respuesta real con IA.

### El sidebar ya tiene labels hardcodeadas

Las labels del sidebar están en `dashboard/layout.tsx` como strings planos.
Se pueden cambiar en ese mismo archivo sin tocar el componente Sidebar.

---

## ✅ Resumen Ejecutivo

```
Fase 1 (hoy):   Cambiar textos del Command Center → 7 líneas de código
Fase 2 (hoy):   Revisar Get Started + sidebar → 1 archivo
Fase 3 (próximo): Redirigir al chat real en vez de a biblioteca
Fase 4 (futuro): Landing page

Prioridad: Fase 1 es la que más impacta al usuario final.
El cambio clave es pasar de "build or query / endpoints" a
"ask your clone / your knowledge base".
```

---

<p align="center">
  <strong>MyOwnClone</strong> —Align the message with the product.
</p>
