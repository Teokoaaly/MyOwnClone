# 📘 Manual Completo de MyOwnClone

<p align="center">
  <strong>Plataforma SaaS multi-tenant para crear, desplegar y escalar clones digitales de IA.</strong><br />
  Desde la perspectiva del usuario final hasta la guía técnica de despliegue y operaciones.
</p>

---

## 📋 Índice

1. [Introducción](#1-introducción)
2. [Guía de Usuario](#2-guía-de-usuario)
3. [Guía Técnica](#3-guía-técnica)
4. [Guía de Despliegue](#4-guía-de-despliegue)
5. [Referencia de API](#5-referencia-de-api)
6. [Solución de Problemas](#6-solución-de-problemas)
7. [Preguntas Frecuentes](#7-preguntas-frecuentes)

---

# 1. Introducción

## 1.1 ¿Qué es MyOwnClone?

**MyOwnClone** es una plataforma SaaS que permite a creadores de contenido, educadores, coaches y negocios lanzar su propio **clon digital de IA**: un asistente conversacional entrenado con su conocimiento que puede:

- Responder preguntas en su propio tono y estilo
- Atender clientes 24/7 en modo soporte
- Asesorar sobre productos y servicios
- Gestionar su bandeja de entrada de email
- Reservar reuniones automáticamente
- Detectar qué temas no domina para aprender más

El sistema usa **RAG (Retrieval-Augmented Generation)**: en lugar de fine-tunear un modelo, el clon busca en una base de conocimiento vectorial la información más relevante y se la pasa al LLM como contexto, logrando respuestas precisas sin perder el estilo del creador.

## 1.2 ¿Para quién es?

| Rol | Beneficio principal |
|---|---|
| **Creador de contenido** | Un asistente que responde como tú 24/7 |
| **Educador / Coach** | Un tutor que enseña con tu metodología |
| **Soporte al cliente** | Automatiza respuestas sin perder calidad |
| **Ventas** | Un vendedor virtual que conoce el catálogo |
| **Desarrollador** | APIs y widget para integrar donde quieras |
| **Admin de plataforma** | Gestiona múltiples tenants desde un panel |

## 1.3 Modelo de Planes

| Plan | Conversaciones/día | Emails/mes | Fuentes | Almacenamiento | Clones | Miembros | Precio |
|---|---|---|---|---|---|---|---|
| **Trial** | 50 | 20 | 5 | 100 MB | 1 | 1 | Gratis (14 días) |
| **Basic** | 200 | 100 | 20 | 1 GB | 1 | 1 | — |
| **Pro** | 1.000 | 500 | 100 | 5 GB | 3 | 3 | — |
| **Scale** | 5.000 | 2.000 | 500 | 25 GB | 10 | 10 | — |
| **Enterprise** | 50.000 | 10.000 | 2.000 | 100 GB | 50 | 50 | — |

Al superar un límite, el clon devuelve un mensaje informativo. Los upgrades se gestionan desde el panel de facturación con Stripe.

---

# 2. Guía de Usuario

## 2.1 Primeros Pasos

### Registro

1. Ve a la [página de inicio](/) y haz clic en **"Crear cuenta"**
2. Puedes registrarte con:
   - **Email y contraseña** (registro directo)
   - **Google** (OAuth)
   - **Magic link** (te enviamos un enlace mágico a tu email)
3. Confirma tu email si usaste registro por contraseña
4. Accedes automáticamente al **Command Center** (dashboard principal)

### Onboarding

Tras el primer login, verás un banner de onboarding que te guía a través de:

1. **Configurar tu clon** — nombre, personalidad, tono
2. **Añadir fuentes** — sube tu contenido
3. **Probar el chat** — haz tu primera pregunta
4. **Ver analíticas** — monitoriza el uso

### Navegación

La interfaz se divide en:

```
┌──────────────────────────────────────────────────┐
│  MyOwnClone  [Sidebar]              [Perfil]     │
├──────────┬───────────────────────────────────────┤
│          │                                       │
│ Sidebar  │        Área principal                 │
│          │                                       │
│ Overview │                                       │
│ ─────────│                                       │
│ Search   │                                       │
│ Crawl    │                                       │
│ Extract  │                                       │
│ Research │                                       │
│ ─────────│                                       │
│ Usage    │                                       │
│ Billing  │                                       │
│ Settings │                                       │
│ ─────────│                                       │
│ ① FREE   │                                       │
│   TRIAL  │                                       │
│          │                                       │
│ [User]   │                                       │
└──────────┴───────────────────────────────────────┘
```

El sidebar se colapsa a un menú hamburguesa en móvil. El tema oscuro/claro se puede alternar desde la configuración.

## 2.2 Command Center (Overview)

El **Command Center** (`/resumen`) es la página principal del dashboard. Muestra:

- **Métrica rápida**: conversaciones totales, preguntas respondidas, gaps detectados
- **Get Started** (accesos directos):
  - API Key — configura tu clave
  - Usage — gráfico de uso últimos 30 días
  - Docs / Agent Toolkit
- **Buscador de IA**: un cuadro de texto donde puedes preguntar sobre endpoints, esquemas, workflows
- **Recent Queries**: las últimas consultas realizadas

## 2.3 Clones

### 2.3.1 Crear un Clon

Desde el panel de configuración puedes crear un clon con los siguientes parámetros:

| Parámetro | Descripción | Ejemplo |
|---|---|---|
| **Nombre** | Nombre del clon | "Asistente de María" |
| **Slug** | Identificador único para URLs | `maria-asesora` |
| **Descripción** | Qué hace tu clon | "Clon educativo sobre programación" |
| **Avatar** | URL de imagen de perfil | `https://...` |
| **Personalidad** | Cómo se comporta | "Empático, didáctico, paciente" |
| **Tono** | Estilo de comunicación | "Informal pero profesional" |
| **Idioma** | Idioma principal | `es` / `en` |
| **Modos activos** | Qué modos puede usar | pedagogía, soporte, ventas |

### 2.3.2 Modos del Clon

Cada clon puede operar en **tres modos**, cada uno con su propio prompt de sistema:

#### 📚 Modo Pedagogía
- Responde preguntas basándose en las fuentes de conocimiento
- Ideal para: cursos, libros, contenido educativo
- Prompt: "Eres un tutor experto que explica con claridad..."

#### 🛠️ Modo Soporte
- Atiende incidencias y preguntas técnicas
- Ideal para: servicio al cliente, FAQ, troubleshooting
- Prompt: "Eres un agente de soporte que resuelve problemas..."

#### 💼 Modo Ventas
- Asesora sobre productos y servicios del catálogo
- Ideal para: ecommerce, consultoría, servicios
- Prompt: "Eres un asesor de ventas que conoce el catálogo..."

### 2.3.3 Widget Embedible

Puedes incrustar tu clon en cualquier sitio web con una línea:

```html
<script src="https://tudominio.com/widget.js" data-clone="mi-clon" data-mode="support"></script>
```

Parámetros configurables:
- `data-clone` (requerido): slug del clon
- `data-mode` (opcional): `pedagogy` | `support` | `sales` (default: `pedagogy`)
- `data-theme` (opcional): `light` | `dark`
- `data-position` (opcional): `right` | `left` (default: `right`)
- `data-color` (opcional): color primario en HEX

## 2.4 Fuentes de Conocimiento

Las fuentes son el contenido que tu clon usará para responder. Se gestionan desde la sección **Biblioteca** (`/biblioteca`).

### 2.4.1 Tipos de Fuentes

| Tipo | Descripción | Método de subida |
|---|---|---|
| **PDF** | Documentos PDF | Subida de archivo |
| **YouTube** | Transcripción de vídeos | URL del vídeo |
| **Web** | Scraping de páginas web | URL |
| **Texto** | Contenido escrito manualmente | Editor de texto |
| **Entrevista** | Preguntas y respuestas | Formulario estructurado |
| **Video** | Archivos de vídeo (transcripción por Whisper) | Subida de archivo |

### 2.4.2 Estados de Procesamiento

Cada fuente pasa por un ciclo de vida:

```
uploading → processing → ready
                            └→ error (si falla)
```

- **uploading**: el archivo se está subiendo a Supabase Storage
- **processing**: se está extrayendo el texto, dividiendo en chunks y generando embeddings
- **ready**: la fuente está disponible para búsqueda semántica
- **error**: ocurrió un fallo (formato no soportado, timeout, etc.)

### 2.4.3 Silos de Conocimiento

Los silos permiten organizar las fuentes por temática. Cada fuente pertenece a un silo:

| Silo | Uso |
|---|---|
| **teach** | Contenido pedagógico |
| **support** | Base de conocimiento de soporte |
| **sales** | Catálogo de productos y ventas |

Cuando un usuario chatea en modo "soporte", el clon solo busca en fuentes del silo `support`, mejorando la precisión de las respuestas.

### 2.4.4 Proceso de Ingesta

```
Fuente (PDF, URL, texto)
    │
    ▼
Extracción de texto
    │
    ▼
Chunking (división en fragmentos de ~500 tokens)
    │
    ▼
Generación de embedding (OpenAI text-embedding-3-small)
    │
    ▼
Almacenamiento en pgvector (PostgreSQL)
    │
    ▼
¡Listo para búsqueda semántica!
```

## 2.5 Chat

### 2.5.1 Cómo Funciona

El chat es la interfaz principal de interacción con el clon. Cuando haces una pregunta:

1. Tu pregunta se envía al backend
2. Se genera un embedding de la pregunta (OpenAI)
3. Se busca en pgvector por similitud coseno (top-5 chunks, threshold > 0.75)
4. Se construye un prompt de sistema con:
   - Personalidad y tono del clon
   - Prompt de modo (pedagogía/soporte/ventas)
   - Memorias del creador
   - Chunks relevantes recuperados
5. Se genera una respuesta con el LLM (Claude o OpenAI)
6. Se calcula un **confidence score** (0.0 - 1.0)
7. Si `confidence < 0.7`, se registra un **gap de conocimiento**
8. La respuesta se envía al frontend vía **Server-Sent Events** (streaming)

### 2.5.2 Confidence Score y Gap Detection

El confidence score mide qué tan segura es la respuesta:

| Score | Significado | Acción |
|---|---|---|
| 0.9 - 1.0 | Alta confianza | Respuesta normal |
| 0.7 - 0.9 | Confianza media | Respuesta con caveat |
| 0.5 - 0.7 | Baja confianza | Se registra gap, se sugiere nueva fuente |
| < 0.5 | Muy baja | Respuesta genérica + gap registrado |

Los gaps se acumulan en `analytics_gaps` y se pueden revisar desde el panel de analíticas para saber qué contenido falta.

### 2.5.3 Streaming de Respuestas

El frontend recibe la respuesta en tiempo real mediante SSE:

```
POST /api/clone/{slug}/chat
Content-Type: application/json

{
  "message": "¿Cómo puedo empezar?",
  "silo": "teach"
}

Response (stream):
data: {"content": "Para empezar,"}
data: {"content": " puedes registrar"}
data: {"content": " tu cuenta..."}
data: {"done": true, "confidence": 0.92, "sources": [...]}
```

### 2.5.4 Mensajes y Feedback

Cada mensaje puede recibir feedback del usuario (thumbs up/down) que se almacena en la tabla `messages.feedback` para mejorar la calidad.

## 2.6 Email Inbox

### 2.6.1 Configuración

Para recibir emails, configura un webhook de **SendGrid Inbound Parse** que apunte a tu endpoint. Los emails entrantes se almacenan en la tabla `emails`.

### 2.6.2 Clasificación Automática

El sistema clasifica cada email entrante:

- **Categoría**: consulta, soporte, venta, spam
- **Urgencia**: alta, media, baja
- **Asunto**: extraído y procesado

### 2.6.3 Borradores con IA

Para cada email, el clon puede generar un borrador de respuesta automáticamente:

```
POST /api/clone/inbox/{id}/generate-draft
→ { "draft": "Estimado cliente,\n\nGracias por contactarnos..." }
```

El borrador se genera en el tono y estilo del creador, usando la información relevante del clon.

### 2.6.4 Respuesta Automática

Puedes configurar el clon para que responda automáticamente emails con alta confianza (>0.85). Los emails con baja confianza se marcan para revisión manual.

## 2.7 Reuniones

### 2.7.1 Configurar Disponibilidad

Desde `/reuniones` puedes definir tu disponibilidad semanal (días y horas). El sistema usa la tabla `availability` para gestionar los slots.

### 2.7.2 Integración con Whereby

Las videollamadas se realizan mediante **Whereby Embedded**. Cuando se reserva una reunión:

1. Se crea una sala en Whereby
2. Se envía un email de confirmación con el enlace
3. Se guarda el booking en la base de datos

### 2.7.3 Booking Público

Los visitantes pueden reservar reuniones directamente desde el widget o la página pública del clon (`/{slug}`).

## 2.8 Analíticas

### 2.8.1 Overview de Métricas

| Métrica | Descripción |
|---|---|
| **Conversaciones totales** | Número total de conversaciones |
| **Mensajes totales** | Mensajes intercambiados |
| **Preguntas respondidas** | Consultas procesadas con éxito |
| **Gaps detectados** | Preguntas con baja confianza |
| **Sesiones activas** | Conversaciones en curso |
| **Tasa de automatización** | % de respuestas automáticas exitosas |

### 2.8.2 Gap Detection

Los gaps son preguntas que el clon no pudo responder con suficiente confianza. Cada gap incluye:

- La pregunta exacta
- Número de veces que se ha preguntado
- Fecha de última aparición
- Fuente sugerida (puedes añadir contenido para cubrirlo)

### 2.8.3 Preguntas Frecuentes

El sistema registra las preguntas más frecuentes (tabla `analytics_questions`) para que puedas identificar patrones y mejorar tu contenido.

## 2.9 Facturación

### 2.9.1 Portal de Stripe

Desde `/facturacion` puedes:

- Ver tu plan actual
- Cambiar de plan (upgrade/downgrade)
- Gestionar método de pago
- Ver historial de facturas

Todo se gestiona mediante el **Stripe Customer Portal**, que se abre en una ventana segura.

### 2.9.2 Límites por Plan

Los límites se aplican en tiempo real. Cuando se supera un límite, el clon informa al usuario. Las limitaciones se resetan diaria o mensualmente según el recurso:

- **Conversaciones/día**: reset diario a las 00:00 UTC
- **Emails/mes**: reset el día de facturación
- **Almacenamiento**: acumulativo, upgrade necesario para ampliar

### 2.9.3 Período de Prueba

Los nuevos usuarios obtienen 14 días de prueba gratuita con el plan Trial. Durante este período:

- Sin límite de características
- Sin necesidad de tarjeta de crédito
- Al expirar, se requiere un plan de pago

## 2.10 Configuración

### 2.10.1 API Keys

Desde `/configuracion` puedes generar y gestionar API keys para integraciones externas. Las keys permiten:

- Acceder a la API del clon programáticamente
- Integrar el chat en aplicaciones externas
- Automatizar la subida de fuentes

### 2.10.2 Perfil de Usuario

Gestiona tu:

- Nombre y email
- Avatar
- Contraseña
- Preferencias de idioma
- Tema (oscuro/claro)

---

# 3. Guía Técnica

## 3.1 Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                     🌐 Cliente                              │
│  [Browser (Dashboard)]  [Widget externo]  [API Client]     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              🚀 Next.js 16 (Frontend App)                   │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────────┐ │
│  │ App Router  │  │ API Routes   │  │ Middleware (Proxy) │ │
│  │ (SSR/SSG)   │  │ (local DB)   │  │ → Flask backend    │ │
│  └─────────────┘  └──────────────┘  └────────────────────┘ │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Providers: SessionProvider + ThemeProvider + i18n    │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
┌──────────────┐ ┌────────┐ ┌──────────┐
│  PostgreSQL  │ │ Redis  │ │ Supabase │
│  + pgvector  │ │ (Rate  │ │ Storage  │
│  (Drizzle)   │ │ Limit) │ │ (Files)  │
└──────────────┘ └────────┘ └──────────┘
          ▲
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│              🐍 Flask 3 (Backend API)                       │
│                                                             │
│  ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌────────────┐  │
│  │ Console  │ │ Public   │ │ Auth BP   │ │ Deploy BP  │  │
│  │ Blueprint│ │ Blueprint│ │            │ │            │  │
│  └──────────┘ └──────────┘ └────────────┘ └────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Core: ModelManager, RAG Pipeline, Email Processor    │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │Anthropic │ │ OpenAI   │ │ Stripe   │
   │ Claude   │ │ Embed/   │ │ Payments │
   │ Chat     │ │ Whisper  │ │          │
   └──────────┘ └──────────┘ └──────────┘
```

### Capas del Sistema

| Capa | Tecnología | Responsabilidad |
|---|---|---|
| **Presentación** | Next.js 16 + React 19 | SSR, UI, Server/Client Components |
| **Frontend API** | Next.js API Routes | Consultas directas a DB, proxies |
| **Middleware** | Next.js Edge Middleware | Proxy inverso, detección de tenants |
| **Backend API** | Flask 3 + Gunicorn | Lógica de negocio, RAG, integraciones |
| **Base de datos** | PostgreSQL 15 + pgvector | Datos relacionales + vectores |
| **Cache** | Redis 7 (Upstash) | Rate limiting, sesiones |
| **Storage** | Supabase Storage | Archivos (PDFs, imágenes) |
| **LLM** | Anthropic Claude / OpenAI | Generación de texto, embeddings |

## 3.2 Frontend en Detalle

### 3.2.1 Estructura de Carpetas

```
MyOwnClone/src/
├── app/                               # Next.js App Router
│   ├── (dashboard)/                   # Grupo de rutas autenticadas
│   │   ├── layout.tsx                 # Layout del dashboard (sidebar + main)
│   │   ├── page.tsx                   → redirect a /resumen
│   │   ├── resumen/                   # Command Center (página principal)
│   │   ├── biblioteca/                # Gestión de fuentes
│   │   ├── cerebro/                   # Memory crawl
│   │   ├── inbox/                     # Email inbox
│   │   ├── productos/                 # Catálogo de productos
│   │   ├── analiticas/                # Analytics y métricas
│   │   ├── facturacion/               # Stripe billing
│   │   ├── configuracion/             # Settings y API keys
│   │   ├── reuniones/                 # Meetings y disponibilidad
│   │   └── registro/                  # Registro de usuarios
│   ├── (public)/                      # Rutas públicas
│   │   └── [slug]/                    # Página pública del clon
│   ├── admin/                         # Panel de administración
│   │   ├── layout.tsx                 # Layout admin con verificación de rol
│   │   ├── resumen/                   # Admin overview
│   │   ├── tenants/                   # Gestión de tenants (CRUD)
│   │   │   └── [id]/                  # Detalle de tenant
│   │   ├── audit/                     # Log de acciones sensibles
│   │   ├── impersonation/             # Impersonación de usuarios
│   │   ├── courtesy/                  # Créditos de cortesía
│   │   └── feedback/                  # Feedback de usuarios
│   ├── api/                           # API Routes
│   │   ├── auth/[...nextauth]/        # NextAuth handler
│   │   ├── clone/sources/             # CRUD de fuentes (GET, POST)
│   │   ├── bookings/                  # Booking de reuniones
│   │   ├── stt/                       # Speech-to-text (Whisper)
│   │   └── csrf/                      # CSRF token
│   ├── providers.tsx                  # SessionProvider + ThemeProvider
│   ├── layout.tsx                     # Root layout (fonts, providers)
│   └── page.tsx                       # Landing page pública
├── components/
│   ├── admin/                         # AdminShell, Pagination, FilterBar, etc.
│   ├── chat/                          # ChatPanel, MessageBubble, SiloToggle
│   ├── dashboard/                     # Sidebar, ChatOrb, StatsCard, etc.
│   └── ui/                            # Modal, Sheet, ThemeToggle, BarChart, etc.
├── lib/
│   ├── auth.ts                        # NextAuth config (providers, callbacks)
│   ├── db/
│   │   ├── index.ts                   # Drizzle client (Pool + schema)
│   │   └── schema/                    # 10 módulos de tablas
│   ├── rag/                           # Pipeline RAG (deprecado, referencia)
│   ├── stripe.ts                      # Cliente Stripe
│   ├── storage.ts                     # Supabase Storage
│   ├── email.ts                       # Resend emails
│   ├── video.ts                       # Whereby meetings
│   ├── quotas.ts                      # Límites por plan
│   ├── platform-admin.ts              # Auth helpers de admin
│   ├── nav-admin.ts                   # Navegación del admin
│   └── utils.ts                       # Utilidades (cn, formatDate, slugify, etc.)
├── middleware.ts                      # Proxy + tenant detection
└── i18n/                              # next-intl (en.json, es.json, routing)
```

### 3.2.2 Server Components vs Client Components

Por defecto, los componentes en Next.js App Router son **Server Components**. Se usa `"use client"` solo cuando es necesario:

**Server Components** (por defecto):
- `layout.tsx` (dashboard, admin, root)
- Páginas que solo renderizan datos del servidor
- Componentes sin interactividad

**Client Components** (`"use client"`):
- `ChatPanel.tsx` — estado local, streaming, eventos
- `MessageBubble.tsx` — feedback de usuario
- `Sidebar.tsx` — navegación, estado mobile
- `ThemeToggle.tsx` — cambio de tema
- `SearchCommandBar.tsx` — búsqueda interactiva
- Componentes con `useState`, `useEffect`, `useSession`

### 3.2.3 Providers

```tsx
// src/app/providers.tsx
"use client";

import { SessionProvider } from "next-auth/react";
import { ThemeProvider } from "next-themes";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>
        {children}
      </ThemeProvider>
    </SessionProvider>
  );
}
```

**SessionProvider**: Proporciona el contexto de autenticación de NextAuth v5 a todos los componentes. Usa el hook `useSession()` para acceder a la sesión.

**ThemeProvider**: Gestiona el tema oscuro/claro mediante la clase CSS `.dark` en el `<html>`. Persiste la preferencia en localStorage. No sincroniza con el sistema (`enableSystem: false`).

### 3.2.4 Internacionalización (i18n)

El sistema usa **next-intl** con soporte para español e inglés:

```tsx
// src/i18n/request.ts
export default getRequestConfig(async () => {
  // Por defecto: inglés
  // El switch de idioma se implementará en rutas futuras
  return {
    locale: "en",
    messages: (await import("./en.json")).default,
  };
});
```

Los archivos de traducción están en `src/i18n/`:
- `en.json` — Textos en inglés
- `es.json` — Textos en español
- `request.ts` — Configuración de next-intl
- `routing.ts` — Definición de rutas localizadas

La detección de idioma se hace por ruta: `/es/...` para español, `/en/...` para inglés.

### 3.2.5 Sistema de Diseño

El diseño se basa en **Tailwind CSS v4** con variables CSS personalizadas para el tema:

**Tokens de diseño** (`globals.css`):

```css
@theme inline {
  --font-sans: var(--font-dm-sans);
  --font-mono: var(--font-jetbrains-mono);

  --color-accent-warm:  #EA580C;
  --color-accent-violet: #7C3AED;
  --color-accent-pink:  #DB2777;
  --color-accent-green: #059669;
  /* ... */
}
```

**Variables de modo claro** (`:root`):

| Variable | Valor | Uso |
|---|---|---|
| `--bg-page` | `#E8E2DD` | Fondo de página (cream cálido) |
| `--bg-shell` | `#FFFFFF` | Fondo del shell principal |
| `--surface-1` | `#FFFFFF` | Superficie de tarjetas |
| `--surface-2` | `#FAFAF9` | Superficie secundaria |
| `--border-soft` | `rgba(15,23,42,0.06)` | Bordes sutiles |
| `--text-primary` | `#1C1917` | Texto principal |

**Variables de modo oscuro** (`.dark`):

| Variable | Valor | Uso |
|---|---|---|
| `--bg-page` | `#070708` | Fondo de página |
| `--bg-shell` | `#0B0B0C` | Shell principal |
| `--surface-1` | `#121213` | Superficie de tarjetas |
| `--border-soft` | `rgba(255,255,255,0.07)` | Bordes sutiles |
| `--text-primary` | `#F4F4F5` | Texto principal |

**Componentes UI reutilizables**:

| Componente | Descripción |
|---|---|
| `Modal` | Diálogo modal (Radix Dialog) |
| `Sheet` | Panel lateral deslizable (Radix Dialog) |
| `ThemeToggle` | Cambio oscuro/claro con icono |
| `SearchCommandBar` | Barra de búsqueda tipo Cmd+K |
| `BarChart` | Gráfico de barras (Recharts) |
| `EmptyState` | Estado vacío con icono y mensaje |
| `ErrorState` | Estado de error con acción de reintento |
| `LoadingState` | Estado de carga con skeleton |
| `Sidebar` | Navegación principal responsiva |
| `MobileNav` | Navegación móvil |

### 3.2.6 Tipografía

- **DM Sans** (variable): Fuente principal del sistema, pesos 400-700
- **JetBrains Mono** (variable): Fuente monoespaciada para código y números, pesos 500-700

## 3.3 Backend en Detalle

### 3.3.1 Application Factory

```python
# api/app_factory.py
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # Extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    
    # Blueprints
    app.register_blueprint(console_bp, url_prefix="/console")
    app.register_blueprint(auth_bp, url_prefix="/console/api/auth")
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(deploy_bp)
    
    # CLI commands
    app.cli.add_command(seed_demo_data)
    
    return app
```

La factory sigue el patrón de **Flask Application Factories**: permite crear múltiples instancias con diferentes configuraciones (desarrollo, testing, producción).

### 3.3.2 Blueprints

| Blueprint | Prefijo | Endpoints |
|---|---|---|
| **console** | `/console` | API autenticada del dashboard |
| **auth** | `/console/api/auth` | Login, verificación de tokens |
| **public** | (raíz) | Chat público, bookings |
| **deploy** | (raíz) | Trigger de deploy frontend |

### 3.3.3 Autenticación Backend

El backend usa **JWT** para autenticación service-to-service. Cada request del frontend al backend incluye:

```
X-API-Key: dev-api-key-for-proxy
```

La clave se valida en los endpoints protegidos mediante el decorador `login_required`. Para endpoints públicos (chat del widget), no se requiere autenticación.

### 3.3.4 Modelos SQLAlchemy

El backend gestiona tablas adicionales que el frontend no maneja directamente:

- `EmailInbound` — Emails recibidos via SendGrid
- `EmailTemplate` — Plantillas de email
- `MeetingType_` — Tipos de reuniones
- `Availability` — Disponibilidad del creador
- `Booking` — Reservas
- `CloneSilo` — Silos de conocimiento
- `Account` — Cuentas de facturación
- `Product` — Productos del creador
- `CreatorMemory` — Memorias del creador

## 3.4 Base de Datos

### 3.4.1 Esquema Drizzle ORM (Frontend)

El frontend usa **Drizzle ORM** con PostgreSQL. La conexión se define en `src/lib/db/index.ts`:

```tsx
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";
import * as schema from "./schema";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

export const db = drizzle(pool, { schema });
export { schema };
```

### 3.4.2 Tablas y Relaciones

#### `tenants`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `slug` | `text UNIQUE` | Identificador único |
| `name` | `text NOT NULL` | Nombre del tenant |
| `plan` | `enum` | `trial`, `basic`, `pro`, `scale`, `enterprise` |
| `status` | `enum` | `active`, `suspended`, `cancelled`, `trial` |
| `trial_ends_at` | `timestamp` | Fin del período trial |
| `stripe_customer_id` | `text` | ID de cliente en Stripe |
| `stripe_subscription_id` | `text` | ID de suscripción en Stripe |

#### `users`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `tenant_id` | `text FK → tenants.id` | Tenant al que pertenece |
| `name` | `text` | Nombre del usuario |
| `email` | `text UNIQUE` | Email |
| `password_hash` | `text` | Hash bcrypt de la contraseña |
| `email_verified` | `timestamp` | Cuándo se verificó el email |
| `image` | `text` | URL del avatar |
| `role` | `enum` | `owner`, `admin`, `member`, `platform_admin` |

#### `clone_configs`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `tenant_id` | `text FK → tenants.id` | Propietario |
| `name` | `text NOT NULL` | Nombre del clon |
| `slug` | `text UNIQUE` | Slug para URLs |
| `description` | `text` | Descripción |
| `avatar_url` | `text` | URL del avatar |
| `personality` | `text` | Personalidad |
| `tone` | `text` | Tono de comunicación |
| `language` | `text` | `es` / `en` |
| `custom_domain` | `text` | Dominio personalizado |
| `active_modes` | `json` | Modos activos |
| `is_active` | `boolean` | Si el clon está activo |

#### `sources`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `clone_id` | `text FK → clone_configs.id` | Clon propietario |
| `type` | `enum` | `youtube`, `pdf`, `video`, `text`, `web`, `interview` |
| `title` | `text NOT NULL` | Título de la fuente |
| `url` | `text` | URL (para YouTube/web) |
| `status` | `enum` | `uploading`, `processing`, `ready`, `error` |
| `metadata` | `json` | Metadatos (silo, etc.) |

#### `chunks`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `source_id` | `text FK → sources.id` | Fuente de origen |
| `content` | `text NOT NULL` | Contenido del chunk |
| `embedding` | `vector` | Embedding (pgvector) |
| `metadata` | `json` | Metadatos adicionales |

#### `conversations`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `clone_id` | `text FK → clone_configs.id` | Clon |
| `visitor_id` | `text` | ID del visitante |
| `mode` | `enum` | `pedagogy`, `sales`, `support` |

#### `messages`
| Columna | Tipo | Descripción |
|---|---|---|
| `id` | `text PK` | UUID |
| `conversation_id` | `text FK → conversations.id` | Conversación |
| `role` | `text` | `user` / `assistant` |
| `content` | `text NOT NULL` | Contenido del mensaje |
| `confidence` | `text` | Confidence score (decimal) |
| `sources` | `json` | Fuentes usadas para la respuesta |
| `feedback` | `text` | `up` / `down` / null |

### 3.4.3 pgvector

La extensión **pgvector** permite almacenar y buscar embeddings directamente en PostgreSQL:

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunks (
    id TEXT PRIMARY KEY,
    content TEXT NOT NULL,
    embedding vector(1536),  -- OpenAI text-embedding-3-small
    metadata JSONB
);

-- Índice para búsqueda por similitud coseno
CREATE INDEX ON chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

La búsqueda semántica se realiza con el operador `<=>` (distancia coseno):

```sql
SELECT c.id, c.content, 
       1 - (c.embedding <=> $1::vector) AS score
FROM chunks c
JOIN sources s ON s.id = c.source_id
WHERE s.clone_id = $2
  AND 1 - (c.embedding <=> $1::vector) > 0.75
ORDER BY c.embedding <=> $1::vector
LIMIT 5;
```

### 3.4.4 Nota sobre Dual ORM

El proyecto usa **dos ORMs sobre la misma base de datos PostgreSQL**:

| ORM | Framework | Tablas que gestiona |
|---|---|---|
| **Drizzle** | Next.js/TypeScript | users, tenants, clone_configs, sources, chunks, conversations, messages, emails, bookings, memories, analytics |
| **Alembic** | Flask/Python | clone_configs, email_inbound, meeting_types, bookings, cost_tracking, admin_audit_log, impersonation_tokens |

Algunas tablas se comparten entre ambos ORMs con esquemas ligeramente diferentes. Es importante mantener la sincronización entre las migraciones de Drizzle y Alembic.

## 3.5 Autenticación y Autorización

### 3.5.1 NextAuth v5

La autenticación se configura en `src/lib/auth.ts`:

```tsx
export const { handlers, auth, signIn, signOut } = NextAuth({
  session: { strategy: "jwt" },
  adapter: DrizzleAdapter(db, { /* tablas */ }),
  providers: [
    Credentials({ /* email + password */ }),
    Resend({ /* magic link */ }),
    Google({ /* OAuth */ }),
  ],
  pages: {
    signIn: "/login",
    verifyRequest: "/verificar",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.role = user.role;
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }) {
      session.user.id = token.id;
      session.user.role = token.role;
      return session;
    },
  },
});
```

### 3.5.2 Providers de Autenticación

| Provider | Método | Estado |
|---|---|---|
| **Credentials** | Email + contraseña (bcrypt) | ✅ Implementado |
| **Resend** | Magic link por email | ✅ Implementado |
| **Google** | OAuth 2.0 | ✅ Implementado |

### 3.5.3 Roles y Permisos

| Rol | Acceso | Asignado por |
|---|---|---|
| `owner` | Control total del tenant | Creador del tenant |
| `admin` | Gestión del tenant | Owner |
| `member` | Uso básico del clon | Owner/Admin |
| `platform_admin` | Panel de administración global | Variables de entorno |

### 3.5.4 Platform Admin

El admin global se autentica mediante variables de entorno:

```env
PLATFORM_ADMIN_EMAIL=admin@example.com
# Generar: node -e 'require("bcryptjs").hash(process.argv[1], 12).then(console.log)' "mi-password"
PLATFORM_ADMIN_PASSWORD_HASH=$2a$12$...
```

Si las credenciales existen en el entorno, el usuario puede hacer login como `platform_admin` y acceder al panel `/admin/*`. La verificación se hace en el layout del admin:

```tsx
// src/app/admin/layout.tsx
const session = await auth();
if (!session?.user) redirect("/login");
if (!isPlatformAdminSession(session)) redirect("/login");
```

## 3.6 Pipeline RAG

### 3.6.1 Arquitectura del Pipeline

```
                    ┌─────────────┐
                    │  Pregunta   │
                    │  del usuario│
                    └──────┬──────┘
                           ▼
┌──────────────────────────────────────────┐
│         1. Generar embedding             │
│     OpenAI text-embedding-3-small        │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│    2. Búsqueda semántica en pgvector     │
│       Similaridad coseno, top-5          │
│       Threshold: 0.75                    │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│    3. Construir prompt de sistema        │
│   - Personalidad del clon                │
│   - Prompt de modo (pedagogía/soporte)   │
│   - Memorias del creador                 │
│   - Chunks relevantes                    │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│    4. Generar respuesta (LLM)            │
│   Anthropic Claude (principal)           │
│   OpenAI GPT-4o-mini (fallback)          │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│    5. Post-procesamiento                 │
│   - Confidence scoring                   │
│   - Gap detection (confidence < 0.7)     │
│   - Logging de conversación              │
└──────────────────────────────────────────┘
```

### 3.6.2 Pipeline en Código

El pipeline está implementado en `src/lib/rag/pipeline.ts` (frontend, deprecated) y en `api/core/retrieval.py` (backend, activo):

```python
# Pseudocódigo del pipeline backend
def run_pipeline(clone_id, message, mode, history):
    # 1. Obtener configuración del clon
    clone = get_clone_config(clone_id)
    mode_config = get_mode_prompt(clone_id, mode)
    memories = get_memories(clone_id)

    # 2. Generar embedding de la pregunta
    embedding = openai.Embedding.create(
        input=message,
        model="text-embedding-3-small"
    )

    # 3. Búsqueda semántica
    chunks = search_similar(embedding, clone_id, top_k=5)

    # 4. Construir prompt
    system_prompt = f"""
    Eres {clone.name}, un asistente con personalidad {clone.personality}.
    Tono: {clone.tone}
    Modo: {mode}
    
    Contexto relevante:
    {chunks.map(c => c.content).join('\n')}
    
    Memorias:
    {memories.map(m => m.content).join('\n')}
    """

    # 5. Generar respuesta
    response = anthropic.messages.create(
        model="claude-sonnet-4-20250514",
        system=system_prompt,
        messages=[...],
        stream=True
    )

    # 6. Calcular confidence
    confidence = calculate_confidence(response, chunks)

    # 7. Detectar gaps
    if confidence < 0.7:
        register_gap(clone_id, message)

    return response, confidence
```

### 3.6.3 Chunking

El proceso de chunking divide el contenido de las fuentes en fragmentos manejables:

| Parámetro | Valor | Descripción |
|---|---|---|
| Tamaño de chunk | ~500 tokens | Fragmentos para embedding |
| Overlap | ~50 tokens | Solapamiento entre chunks |
| Estrategia | Semántico | Divide por párrafos/oraciones |

### 3.6.4 Embeddings

- **Modelo**: `text-embedding-3-small` (OpenAI)
- **Dimensiones**: 1536
- **Índice**: IVFFlat con distancia coseno
- **Threshold de búsqueda**: > 0.75 (similitud coseno)

### 3.6.5 LLM Configuration

| Parámetro | Valor | Descripción |
|---|---|---|
| Proveedor principal | Anthropic Claude | Chat, generación |
| Proveedor embeddings | OpenAI | text-embedding-3-small |
| STT | OpenAI Whisper | Speech-to-text |
| Modelo chat | `claude-sonnet-4-20250514` | Balance calidad/velocidad |
| Temperature | 0.7 | Control de creatividad |
| Max tokens | 4096 | Longitud máxima de respuesta |

## 3.7 Middleware y Proxy

### 3.7.1 Función del Middleware

El middleware (`src/middleware.ts`) actúa como **proxy inverso** entre el frontend Next.js y el backend Flask. Sus funciones son:

1. **Proxy de API**: redirige requests `/api/*` al backend Flask (`http://127.0.0.1:5001`)
2. **Detección de tenants**: identifica el tenant por subdominio
3. **Service-to-service auth**: inyecta API key en requests al backend

### 3.7.2 Mapeo de Rutas

```typescript
const ROUTE_MAP = {
  "/api/admin/overview": "/console/api/myownclone/admin/overview",
  "/api/admin/tenants": "/console/api/myownclone/admin/tenants",
  "/api/clones": "/console/api/myownclone/clones",
  "/api/plans": "/console/api/myownclone/plans",
  "/api/stripe/checkout": "/console/api/myownclone/stripe/checkout",
  "/api/inbox": "/console/api/myownclone/inbox",
  "/api/auth/login": "/console/api/auth/login",
  // ...
};
```

### 3.7.3 Detección de Tenants

```typescript
function getTenantFromHost(hostname: string): string | null {
  if (hostname === "localhost") return null;
  const parts = hostname.split(".");
  if (parts.length >= 3 && parts[1] === "replica") {
    return parts[0]; // tenant1.replica.dominio.com → "tenant1"
  }
  return null;
}
```

### 3.7.4 Service-to-Service Auth

Cada request proxy al backend incluye:

```typescript
const forwardedHeaders = {
  "Content-Type": "application/json",
  "X-API-Key": "dev-api-key-for-proxy",
};
```

## 3.8 Integraciones

### 3.8.1 Stripe

```typescript
// src/lib/stripe.ts
export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: "2025-02-24.acacia",
});

// Crear sesión de checkout
export async function createCheckoutSession(params) {
  return stripe.checkout.sessions.create({
    mode: "subscription",
    line_items: [{ price: params.priceId, quantity: 1 }],
    success_url: params.successUrl,
    cancel_url: params.cancelUrl,
    client_reference_id: params.tenantId,
    subscription_data: { trial_period_days: 14 },
  });
}

// Portal de facturación
export async function createCustomerPortalSession(params) {
  return stripe.billingPortal.sessions.create({
    customer: params.customerId,
    return_url: params.returnUrl,
  });
}
```

### 3.8.2 Resend (Email)

```typescript
// src/lib/email.ts
export async function sendEmail(params) {
  return resend.emails.send({
    from: fromEmail,
    to: params.to,
    subject: params.subject,
    html: params.html,
  });
}

// Tipos de emails:
// - Verificación de login (magic link)
// - Confirmación de booking
// - Notificaciones varias
```

### 3.8.3 SendGrid (Email Inbound)

SendGrid Inbound Parse webhook recibe los emails entrantes y los envía al backend Flask, que los procesa, clasifica y almacena en la tabla `email_inbound`.

### 3.8.4 Whereby (Videollamadas)

```typescript
// src/lib/video.ts
export async function createMeeting(params) {
  return wherebyRequest("/meetings", {
    method: "POST",
    body: JSON.stringify({
      roomMode: "normal",
      roomNamePrefix: "replica-",
      startDate: new Date().toISOString(),
      endDate: params.endDate,
    }),
  });
}
```

### 3.8.5 Supabase Storage

```typescript
// src/lib/storage.ts
export async function uploadFile(bucket, filePath, file, contentType) {
  return supabaseRequest(`/object/${bucket}/${filePath}`, {
    method: "POST",
    body: formData,
  });
}

export function getPublicUrl(bucket, filePath) {
  return `${supabaseUrl}/storage/v1/object/public/${bucket}/${filePath}`;
}
```

### 3.8.6 Upstash Redis (Rate Limiting)

Rate limiting por IP o usuario. Si Upstash no está configurado, fallback a un contador en memoria.

### 3.8.7 Sentry (Error Tracking)

Captura de errores tanto en frontend como en backend. Los errores no fatales se registran sin interrumpir la experiencia del usuario.

### 3.8.8 PostHog (Analytics de Producto)

Eventos de producto trackeados:
- Registro de usuario
- Creación de clon
- Mensajes enviados
- Gaps detectados
- Upgrades de plan

---

# 4. Guía de Despliegue

## 4.1 Requisitos de Producción

| Recurso | Especificación Mínima | Recomendada |
|---|---|---|
| **Servidor** | 2 vCPU, 4 GB RAM | 4 vCPU, 8 GB RAM |
| **Disco** | 20 GB SSD | 50 GB SSD |
| **PostgreSQL** | 15+ con pgvector | 15+ con pgvector |
| **Redis** | 7+ | 7+ |
| **Node.js** | 20 LTS | 20 LTS |
| **Python** | 3.11+ | 3.11+ |
| **Nginx** | 1.24+ | 1.24+ |

## 4.2 Despliegue con Docker

### Backend

```dockerfile
# Dockerfile (raíz del proyecto)
FROM python:3.11-slim

WORKDIR /app/api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5001
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "api.app_factory:create_app()"]
```

```yaml
# docker-compose.backend.prod.yml (en ops/)
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myownclone
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
    ports:
      - "6379:6379"

  api:
    build: .
    environment:
      DATABASE_URL: postgresql://postgres:${DB_PASSWORD}@db:5432/myownclone
      REDIS_URL: redis://:${REDIS_PASSWORD}@redis:6379/0
    depends_on:
      - db
      - redis
    ports:
      - "5001:5001"

volumes:
  pgdata:
```

### Frontend (Next.js)

```bash
# Build de producción
cd MyOwnClone
npm ci
npm run build

# Iniciar con Node.js
npm run start  # Puerto 3000

# O con PM2
pm2 start npm --name "myownclone" -- start
```

## 4.3 Frontend con Docker

```dockerfile
# Dockerfile.frontend
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["npm", "start"]
```

## 4.4 Variables de Entorno (Producción)

### Frontend

```env
# Esenciales
DATABASE_URL=postgresql://postgres:pass@prod-db:5432/myownclone
NEXTAUTH_URL=https://myownclone.com
NEXTAUTH_SECRET=<openssl rand -base64 32>
AUTH_SECRET=<mismo que arriba>
MYOWNCLONE_API_URL=http://api:5001
DEFAULT_CLONE_ID=<uuid>

# LLM
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# Stripe
STRIPE_SECRET_KEY=sk_live_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Admin
PLATFORM_ADMIN_EMAIL=admin@example.com
PLATFORM_ADMIN_PASSWORD_HASH=<bcrypt hash>
```

### Backend

```env
DB_PASSWORD=<fuerte, ≥16 chars>
REDIS_PASSWORD=<fuerte, ≥16 chars>
JWT_SECRET_KEY=<≥64 chars>
IMPERSONATION_TOKEN_PEPPER=<≥32 chars>
OPENAI_API_KEY=sk-...
STRIPE_SECRET_KEY=sk_live_...
ALLOWED_ORIGINS=https://myownclone.com,https://admin.myownclone.com
```

## 4.5 Nginx como Reverse Proxy

```nginx
server {
    listen 80;
    server_name myownclone.com *.myownclone.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name myownclone.com;

    ssl_certificate /etc/letsencrypt/live/myownclone.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myownclone.com/privkey.pem;

    # Frontend Next.js
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Backend Flask
    location /api/ {
        proxy_pass http://localhost:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 4.6 SSL con Let's Encrypt

```bash
# Instalar certbot
apt install certbot python3-certbot-nginx

# Obtener certificado
certbot --nginx -d myownclone.com -d *.myownclone.com

# Renovación automática
certbot renew --dry-run
```

## 4.7 Monitoreo

### Sentry

```typescript
// Configurar DSN en variables de entorno
NEXT_PUBLIC_SENTRY_DSN=https://...
SENTRY_ORG=myownclone
SENTRY_PROJECT=myownclone-frontend
```

### PostHog

```typescript
NEXT_PUBLIC_POSTHOG_KEY=phc_...
NEXT_PUBLIC_POSTHOG_HOST=https://app.posthog.com
```

### Logs

```bash
# Backend (Gunicorn)
journalctl -u myownclone-api -f

# Frontend (PM2)
pm2 logs myownclone

# NGINX
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## 4.8 Backup y Restore PostgreSQL

```bash
# Backup
pg_dump -U postgres myownclone > myownclone_$(date +%Y%m%d).sql

# Backup con compresión
pg_dump -U postgres myownclone | gzip > myownclone_$(date +%Y%m%d).sql.gz

# Restore
dropdb -U postgres myownclone
createdb -U postgres myownclone
gunzip -c myownclone_20260101.sql.gz | psql -U postgres myownclone

# Backup automático (cron)
0 3 * * * pg_dump -U postgres myownclone | gzip > /backups/myownclone_$(date +\%Y\%m\%d).sql.gz
```

## 4.9 Estrategia de Migraciones

### Drizzle (Frontend)

```bash
# Desarrollo: push directo del schema
npm run db:push

# Producción: generar SQL y aplicar controladamente
npm run db:generate
# Revisar el SQL generado en drizzle/
npm run db:migrate
```

### Alembic (Backend)

```bash
# Generar migración automática
flask --app app_factory db migrate -m "descripción"

# Aplicar
flask --app app_factory db upgrade

# Revertir
flask --app app_factory db downgrade
```

> ⚠️ **Importante**: Coordinar las migraciones entre Drizzle y Alembic. Ambas apuntan a la misma base de datos. Se recomienda usar un solo ORM para tablas compartidas o documentar cuidadosamente los cambios.

## 4.10 Escalado

### Vertical
- Aumentar RAM/CPU del servidor
- Optimizar consultas PostgreSQL con índices
- Aumentar `lists` en índice IVFFlat de pgvector para más precisión

### Horizontal
- Frontend: múltiples instancias de Next.js detrás de Nginx (balanceo round-robin)
- Backend: múltiples workers de Gunicorn (`--workers=4 --threads=2`)
- Base de datos: replicación de lectura (read replicas)
- Cache: Redis cluster para rate limiting distribuido

### Rate Limiting
```typescript
// Basado en Upstash Redis (o fallback in-memory)
const limiter = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(50, "1 d"), // 50 conversaciones/día
  analytics: true,
});
```

---

# 5. Referencia de API

## 5.1 Frontend API Routes

Estas rutas son servidas directamente por Next.js (sin proxy al backend):

### Autenticación

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/auth/[...nextauth]` | `*` | No | Handlers de NextAuth (login, callback, signout) |
| `/api/auth/session` | `GET` | Cookie | Obtener sesión actual |
| `/api/csrf` | `GET` | No | Obtener token CSRF |

### Fuentes (Sources)

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/clone/sources` | `GET` | Sesión | Listar fuentes del clon |
| `/api/clone/sources` | `POST` | Sesión | Crear fuente (multipart: file+metadata) |

**POST /api/clone/sources**:
```
Content-Type: multipart/form-data

Fields:
  silo: "teach" | "support" | "sales"
  type: "pdf" | "youtube" | "web" | "text" | "interview"
  content: string (para type=text)
  url: string (para type=youtube|web)
  file: File (para type=pdf)
```

### Chat

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/clone/{slug}/chat` | `POST` | No (público) | Enviar mensaje y recibir streaming |

**POST /api/clone/{slug}/chat**:
```json
{
  "message": "¿Cómo puedo empezar?",
  "silo": "teach",
  "context_id": null,
  "conversation_id": null
}
```

Response (SSE stream):
```
data: {"content": "texto parcial..."}
data: {"done": true, "confidence": 0.92, "sources": [{"chunkId": "...", "score": 0.95}]}
```

### Analytics

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/clone/analytics/overview` | `GET` | Sesión | Resumen de métricas |
| `/api/clone/inbox/list?limit=N` | `GET` | Sesión | Listar inbox |
| `/api/clone/inbox/{id}/generate-draft` | `POST` | Sesión | Generar borrador IA |

### Bookings

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/bookings` | `POST` | No | Crear reserva |
| `/api/bookings` | `GET` | Sesión | Listar reservas |

### Speech-to-Text

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/stt` | `POST` | Sesión | Convertir audio a texto (Whisper) |

### Widget

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/widget.js` | `GET` | No | Script del widget embedible |

### Deploy

| Endpoint | Método | Auth | Descripción |
|---|---|---|---|
| `/api/deploy` | `POST` | API Key | Trigger deploy frontend |

## 5.2 Backend Flask Endpoints (Proxy via Middleware)

El middleware de Next.js mapea rutas `/api/*` al backend Flask:

### Console API (Dashboard autenticado)

| Endpoint Frontend | Backend | Método | Descripción |
|---|---|---|---|
| `/api/clone/clones` | `/console/api/myownclone/clones` | `GET/POST` | CRUD clones |
| `/api/clone/analytics/overview` | `/console/api/myownclone/clones/{id}/analytics/overview` | `GET` | Overview |
| `/api/clone/analytics/questions` | `/console/api/myownclone/clones/{id}/analytics/questions` | `GET` | FAQ |
| `/api/clone/analytics/gaps` | `/console/api/myownclone/clones/{id}/analytics/gaps` | `GET` | Gaps |
| `/api/clone/memories` | `/console/api/myownclone/clones/{id}/memories` | `GET/POST` | Memorias |
| `/api/clone/plans` | `/console/api/myownclone/plans` | `GET` | Planes |
| `/api/clone/billing` | `/console/api/myownclone/stripe/billing` | `POST` | Portal billing |
| `/api/clone/stripe/checkout` | `/console/api/myownclone/stripe/checkout` | `POST` | Checkout |
| `/api/clone/inbox/list` | `/console/api/myownclone/clones/{id}/inbox` | `GET` | Inbox |
| `/api/clone/inbox/{id}` | `/console/api/myownclone/inbox/{id}` | `GET` | Email detalle |
| `/api/clone/inbox/{id}/generate-draft` | `/console/api/myownclone/inbox/{id}/generate-draft` | `POST` | Borrador |
| `/api/clone/products` | `/console/api/myownclone/clones/{id}/products` | `GET/POST` | Productos |
| `/api/clone/feedback` | `/console/api/myownclone/feedback` | `GET/POST` | Feedback |

### Admin API

| Endpoint Frontend | Backend | Método | Descripción |
|---|---|---|---|
| `/api/admin/overview` | `/console/api/myownclone/admin/overview` | `GET` | Métricas admin |
| `/api/admin/tenants` | `/console/api/myownclone/admin/tenants` | `GET` | Listar tenants |
| `/api/admin/impersonate` | `/console/api/myownclone/admin/impersonate` | `POST` | Impersonar |
| `/api/admin/courtesy-account` | `/console/api/myownclone/admin/courtesy-account` | `POST` | Créditos |

### Auth API

| Endpoint Frontend | Backend | Método | Descripción |
|---|---|---|---|
| `/api/auth/login` | `/console/api/auth/login` | `POST` | Login API |

## 5.3 Public API (Sin autenticación)

| Endpoint | Método | Descripción |
|---|---|---|
| `/api/public/{slug}/chat` | `POST` | Chat público del widget |
| `/api/public/{slug}/bookings` | `POST` | Booking público |
| `/api/public/{slug}/bookings/availability` | `GET` | Slots disponibles |

---

# 6. Solución de Problemas

## 6.1 Problemas Comunes

### Error: "Backend unavailable" (HTTP 502)

**Causa**: El middleware no puede conectar con el backend Flask.

**Solución**:
```bash
# Verificar que el backend está corriendo
curl http://localhost:5001/health

# Verificar MYOWNCLONE_API_URL en .env.local
# Debe apuntar a http://localhost:5001 en desarrollo

# Si es producción, verificar que el servicio está activo
systemctl status myownclone-api
```

### Error: "DEFAULT_CLONE_ID not configured"

**Causa**: Falta la variable de entorno `DEFAULT_CLONE_ID`.

**Solución**:
```bash
# Crear un clon primero desde el dashboard o insertar en DB
INSERT INTO clone_configs (id, tenant_id, name, slug, language, is_active)
VALUES ('tu-uuid-aqui', 'tenant-id', 'Mi Clon', 'mi-clon', 'es', true);

# Luego copiar el UUID a .env.local
echo "DEFAULT_CLONE_ID=tu-uuid-aqui" >> .env.local
```

### Error de conexión a PostgreSQL

**Causa**: Credenciales incorrectas o PostgreSQL no accesible.

**Solución**:
```bash
# Verificar conexión
psql -U postgres -h localhost -d myownclone

# Verificar DATABASE_URL en .env.local
# Formato: postgresql://user:password@host:5432/dbname

# Verificar que PostgreSQL está corriendo
docker ps | grep postgres
```

### Error en embeddings (OpenAI)

**Causa**: API key de OpenAI inválida o sin crédito.

**Solución**:
```bash
# Verificar que OPENAI_API_KEY está configurada
echo $OPENAI_API_KEY

# Testear la key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Error de migraciones Drizzle

**Causa**: Conflicto entre migraciones de Drizzle y Alembic.

**Solución**:
```bash
# Ver estado actual
npm run db:studio

# Si hay conflicto, borrar la tabla drizzle_migrations y regenerar
# O usar --force en drizzle-kit push
```

### El chat no responde o da error

**Pasos de diagnóstico**:
```bash
# 1. Verificar que el backend responde
curl http://localhost:5001/console/api/myownclone/clones

# 2. Verificar la API key de Anthropic/OpenAI
# 3. Verificar que el clon existe
# 4. Revisar logs del backend
docker logs myownclone_api --tail 50
```

## 6.2 Logs y Debugging

### Frontend
```bash
# Logs de desarrollo (terminal)
npm run dev

# Logs de producción (PM2)
pm2 logs myownclone

# Consola del navegador
# Abrir DevTools → Console para ver errores de red
```

### Backend
```bash
# Desarrollo
flask --app app_factory run --debug

# Producción (Gunicorn)
journalctl -u myownclone-api -f

# Docker
docker logs myownclone_api --tail 100
docker logs myownclone_db --tail 50
```

### Base de Datos
```sql
-- Ver conexiones activas
SELECT * FROM pg_stat_activity WHERE datname = 'myownclone';

-- Ver queries lentas
SELECT * FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;

-- Verificar extensión vector
SELECT * FROM pg_extension WHERE extname = 'vector';
```

## 6.3 Errores Frecuentes en Desarrollo

| Error | Causa | Solución |
|---|---|---|
| `Module not found: Can't resolve @/...` | Path alias no configurado | Verificar `tsconfig.json` paths |
| `bcryptjs error` | Node.js version mismatch | Usar Node.js 18+ |
| `Port 3000 already in use` | Otro proceso en el puerto | `npx kill-port 3000` |
| `pgvector: extension not found` | pgvector no instalado | `CREATE EXTENSION vector;` |
| `TypeError: Cannot read properties of null (reading 'useCallback')` | Componente sin `"use client"` | Añadir directiva al componente |

---

# 7. Preguntas Frecuentes

## 7.1 FAQ para Usuarios

### ¿Cómo entreno a mi clon?
Sube contenido (PDFs, URLs, texto) desde la sección **Biblioteca**. El clon usa ese contenido para responder preguntas. Más contenido = respuestas más precisas.

### ¿Cuánto tarda en procesarse una fuente?
Depende del tamaño: un PDF pequeño (~10 páginas) se procesa en segundos. Un vídeo de YouTube de 1 hora puede tardar 2-3 minutos.

### ¿Puedo personalizar el tono de mi clon?
Sí. Desde la configuración del clon puedes definir personalidad ("empático, técnico, divertido..."), tono ("formal, informal, profesional...") e idioma.

### ¿Qué pasa si mi clon no sabe responder?
El sistema detecta automáticamente las preguntas que tu clon no puede responder con suficiente confianza (gaps). Puedes revisarlas en Analytics y añadir contenido para cubrirlas.

### ¿Puedo usar mi propio dominio?
Sí. Los planes Pro y superiores permiten configurar un dominio personalizado para el widget y la página pública del clon.

### ¿Cómo gestiono mi suscripción?
Desde el panel de Facturación puedes cambiar de plan, actualizar método de pago y ver el historial de facturas. Todo se gestiona a través del portal seguro de Stripe.

### ¿Hay límite de mensajes?
Cada plan tiene un límite diario de conversaciones y mensual de emails. Los límites se muestran en la página de precios y en el dashboard.

## 7.2 FAQ para Desarrolladores

### ¿Cómo integro el clon en mi web?
Usa el widget embedible:
```html
<script src="https://tudominio.com/widget.js" data-clone="slug-del-clon"></script>
```

### ¿Puedo acceder a la API directamente?
Sí. Desde Configuración puedes generar API keys para acceder a los endpoints del clon programáticamente.

### ¿Qué modelos LLM usa?
- **Chat principal**: Anthropic Claude (Sonnet)
- **Embeddings**: OpenAI text-embedding-3-small
- **Speech-to-text**: OpenAI Whisper
- La selección del modelo se gestiona desde `api/core/model_manager.py`

### ¿Cómo funciona el multi-tenancy?
Cada cliente (tenant) tiene sus propios datos aislados por `tenant_id` en todas las tablas. La identificación se hace por subdominio (tenant1.myownclone.com → Tenant 1).

### ¿Dónde se almacenan los archivos?
Los archivos (PDFs, imágenes) se almacenan en **Supabase Storage**. Las URLs públicas se generan automáticamente tras la subida.

### ¿Cómo contribuir al proyecto?
Ver [CONTRIBUTING.md] — próximamente. Por ahora, haz fork del repositorio y abre un PR con tus cambios siguiendo las convenciones de código del proyecto.

### ¿Hay tests?
Sí:
- **Frontend**: Vitest + React Testing Library (`npm test`)
- **Backend**: pytest (`pytest tests/ -v`)

---

<p align="center">
  <strong>MyOwnClone</strong> — Multiply Yourself
  <br />
  <a href="../README.md">Volver al README</a>
</p>
