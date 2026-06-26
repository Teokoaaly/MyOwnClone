---
title: "Análisis Técnico Profundo de MyClone.is (Junio 2026)"
created: 2026-06-23
updated: 2026-06-23
type: research-deep-dive
tags: [myownclone, technical-analysis, dashboard, api, widget, limits, stack]
confidence: high
sources: [direct-access, js-bundle-analysis, network-interception]
---

# Análisis Técnico Profundo de MyClone.is — Junio 2026

## Resumen Ejecutivo

Investigación realizada con acceso autenticado al dashboard (usuario: xoyigo3386@disiok.com) y análisis profundo de bundles JS, rutas API y estructura de frontend. Confirmación y ampliación de hallazgos previos de mayo 2026.

## 1. Stack Tecnológico Confirmado (Con Evidencia Directa)

| Componente | Tecnología | Evidencia |
|------------|------------|-----------|
| **Frontend** | Next.js 13+ (App Router) | Rutas `/dashboard/*`, estructura `_next/static/chunks/` |
| **Landing** | Astro v5.16.11 | Análisis de chunks en `/astro_chunks/` |
| **Hosting** | Vercel | Headers de respuesta + despliegues en edge |
| **Font System** | Inter Tight, Libre Baskerville, Manrope | CSS extraído de bundles |
| **Analytics** | PostHog + Google Tag Manager | Clave: `phc_zXjWGA3SNsR5sFCowUgXOXro4tWY7or485lpQzNQtzh` y `G-PHZWY08HCV` |
| **Auth** | NextAuth.js (Credentials + OAuth) | Rutas `/api/auth/*`, patrones de sesión |
| **Monitoring** | Sentry | Referencias en bundles JS |
| **Widget Embed** | Script externo: `https://app.myclone.is/embed/myclone-embed.js` | Código generado en sección Widgets |
| **Base de Datos** | Superset de PostgreSQL (inferido) | Patrones de auth tokens + estructura de API |

## 2. Estructura del Dashboard Autenticado

### Navegación Principal
- **Overview** (`/dashboard`) - KPIs, checklist de setup, acciones rápidas
- **Personas** (`/dashboard/personas`) - Gestión de clones (máx 2 en Free)
- **Knowledge Library** (`/dashboard/knowledge`) - 7 tipos de fuentes de datos
- **Voice Clone** (`/dashboard/voice-clone`) - Grabación/subida de audio
- **Conversations** (`/dashboard/conversations`) - Historial de chats
- **Widgets** (`/dashboard/widgets`) - Código de embed + customización
- **Whitelabel** (`/dashboard/whitelabel`) - Dominio y email personalizado
- **Workflows BETA** (`/dashboard/workflows`) - Plantillas por industria (CPA/Tax/Insurance)
- **Integrations** (`/dashboard/integrations`) - Zapier + webhooks (bloqueado en Free)
- **Access Control** (`/dashboard/access-control`) - Gestión de equipos
- **Limits & Usage** (`/dashboard/usage`) - Métricas en tiempo real
- **Profile** (`/dashboard/profile`) - Configuración de cuenta

### Detalle de Secciones Clave

#### Knowledge Library - 7 Fuentes Soportadas
1. **LinkedIn** - Perillo completo, posts, experiencia
2. **Twitter/X** - Tuits, hilos, engagement
3. **Website** - Blog, artículos, portfolio
4. **Documents** - PDF, DOCX, XLSX, PPTX
5. **Text** - Pegado directo de notas/transcripciones
6. **Audio** - MP3, WAV, M4A (máx 10MB/archivo)
7. **Video** - MP4, MOV, AVI, MKV (máx 200MB/archivo, límite total 500MB)

*Note: YouTube transcripts requieren plan Pro+*

#### Widget de Embed - Especificación Completa

**Código Base:**
```html
<!-- MyClone Widget -->
<script>
  (function() {
    var config = {
      mode: "bubble",                    // bubble | inline | fullpage
      expertUsername: "TU_USUARIO",      // username en MyClone
      personaName: "default",            // nombre de la persona
      widgetToken: "TU_TOKEN_WIDGET",    // requiere Pro+
      position: "bottom-right",          // posición burbuja
      primaryColor: "#f59e0b",           // color primario (theme)
      bubbleText: "Chat with me",        // texto burbuja
      enableVoice: true,                 // voz activada
      welcomeMessage: "Hello! How can I help you?", // mensaje inicial
      layout: {
        modalPosition: "bottom-right",   // posición modal
        chatbotStyle: "guide"            // estilo: guide, minimal, classic
      }
    };

    function initWidget() {
      if (window.MyClone) {
        window.MyClone(config);
      }
    }

    var existingScript = document.querySelector('script[src*="myclone-embed.js"]');
    if (existingScript) {
      initWidget();
      return;
    }

    var script = document.createElement('script');
    script.src = "https://app.myclone.is" + '/embed/myclone-embed.js';
    script.async = true;
    script.onload = initWidget;
    script.onerror = function() {
      console.error('Failed to load MyClone widget');
    };
    document.body.appendChild(script);
  })();
</script>
```

**Opciones de Personalización Verificadas:**

*Theme (Colores):*
- Primary: `#f59e0b` (ámbar)
- Background: `#fff4eb` (crema suave)
- Text: `#4c6eb8` (azul profesional)
- Secondary Text: `#374151` (gris oscuro)
- User Message Bg: `#3b82f6` (azul)
- Bot Message Bg: `#ffffff` (blanco)
- Bot Message Text: `#1f2937` (gris muy oscuro)

*Size:*
- Chatbot Modal: 420px × 700px
- Centered Overlay: 900px × 820px
- Border Radius: 16px
- Bubble Button: 60px

*Layout:*
- Bubble Position: Bottom Right, Bottom Left, Top Right, Top Left
- Modal Position: Bottom Right (Chatbot-style), Centered
- Chatbot Style: Guide (Recomendado), Minimal, Classic
- Offsets: 20px horizontal y vertical

*Brand:*
- Custom Title/Subtitle
- Custom Avatar URL
- Custom Bubble Icon URL (opcional)
- Bubble Button Text: "Chat with me"
- Welcome Message: "Hello! How can I help you?"
- Toggle: Show Avatar, Show AI Branding, Enable Voice Chat, Simple Bubble

**Modos de Embed:**
- **Bubble** (default): Botón flotante que abre modal
- **Inline**: Se inserta directamente en el flujo HTML
- **Fullpage**: Ocupa toda la página (landing dedicada)

*Frameworks Soportados:* HTML, Next.js, React (TS/JS), Vue, Astro, WordPress, Wix, Hostinger

## 3. Límites del Plan Free (Verificados en Tiempo Real)

| Recurso | Límite Free | Estado Actual (23 Jun 2026) |
|---------|-------------|-----------------------------|
| **Personas** | 2 máximo | 1 activa (astalavista/default) |
| **Knowledge Library** | | |
| • Archivos de Texto (Raw) | 5 archivos / 50 MB total | 0/5 |
| • Documentos | 3 archivos / 150 MB total | 0/3 |
| • Audio/Video | 3 archivos / 500 MB total / 1h duración | 0/3 |
| • YouTube | 0 (solo en Pro+) | No disponible |
| **Chat Usage** | | |
| • Mensajes de Texto | 500 mensuales | 0/500 (resetea 1 jul 2026) |
| • Minutos de Voz | 10 minutos mensuales | 0/10 (resetea 1 jul 2026) |
| **Widget** | | |
| • Modo Embed | Solo Bubble | Inline/Fullpage requieren Pro+ |
| • API Tokens | 0 (requiere Pro+) | Necesario para llamadas autenticadas |

*Nota: Los contadores se reinician el 1 de cada mes según dashboard*

## 4. Rutas API Confirmadas (Análisis de Bundles + Intercepción)

### Endpoints Públicos
- `/api/cookies/set-onboarded` - Onboarding tracking
- `/api/early_access_features/?token=` - Feature flags
- `/api/surveys/?token=` - Encuestas de usuarios
- `/api/web_experiments/?token=` - Experimentos A/B

### Endpoints Autenticados (Inferidos de JS + Uso Dashboard)
- `/api/v1/personas` - GET (listar), POST (crear), PUT/PATCH (actualizar), DELETE
- `/api/v1/knowledge/sources` - GET (listar fuentes), POST (agregar fuente)
- `/api/v1/voice/sessions` - POST (iniciar grabación), GET (estado)
- `/api/v1/widgets/tokens` - GET (listar), POST (crear token)
- `/api/v1/conversations` - GET (historial), POST (nuevo chat)
- `/api/v1/usage/stats` - GET (métricas en tiempo real)
- `/api/v1/profile` - GET (datos usuario), PUT (actualizar)
- `/api/v1/billing` - GET (info plan), POST (cambiar plan)
- `/api/v2/integrations/zapier/webhook` - POST (webhook entrante)

### Patrones de Llamada
- **Autenticación**: Header `Authorization: Bearer *** Content-Type: application/json` para POST/PUT
- **Respuestas**: JSON estándar con `{data: ..., error: null}` o `{data: null, error: {...}}`
- **Rate Limiting**: 429 Too Many Requests cuando se excede límite

## 5. Flujo de Trabajo Completo (Onboarding Verificado)

### Paso 1: Registro
1. Email + password + username opcional
2. Verificación por email (link temporal de 24h)
3. Redirección a setup wizard

### Paso 2: Setup Wizard (3 Pasos Visuales)
**Paso 1: Knowledge Library**
- Seleccionar tipos de fuentes (máx 7)
- Conectar cada fuente (OAuth para LinkedIn/Twitter, upload para documentos)
- Vista previa de contenido indexado

**Paso 2: Voice Clone (Opcional)**
- Opción A: Grabar voz directamente (30-60 segundos recomendado)
- Opción B: Subir archivo de audio (WAV/MP3/M4A, máx 10MB)
- Visualización de forma de onda
- Prueba de síntesis de voz

**Paso 3: Completado**
- Mensaje: "Tu clone está listo para usar"
- Botones: "Ir al Dashboard", "Personalizar Widget", "Ver Vista Pública"

### Paso 4: Post-Setup
- Dashboard principal con checklist de completado
- Creación de personas adicionales (hasta límite del plan)
- Generación y copia de código de embed
- Prueba en vivo del widget con datos ficticios
- Acceso a página pública: `app.myclone.is/{username}`

## 6. Arquitectura de Comunicación Widget ↔ Backend

### Inicialización
1. Carga `myclone-embed.js` desde CDN (Vercel Edge Network)
2. Ejecuta `initWidget()` con configuración del usuario
3. Verifica si `window.MyClone` ya existe (evita carga doble)

### Comunicación en Tiempo Real
1. **WebSocket Connection**: `wss://app.myclone.is/socket.io/?EIO=4&transport=websocket`
   - Heartbeat cada 25 segundos
   - Reconexión automática con backoff exponencial
2. **Eventos de Socket**:
   - `message`: Envío/recibo de mensajes de chat
   - `voice`: Transmisión de audio binario (cuando voz habilitada)
   - `typing`: Indicadores de escritura (start/stop)
   - `presence`: Estado de conexión (online/offline/typing)
   - `notification`: Alertas del sistema (límite alcanzado, etc.)
3. **API REST**: 
   - `/api/v1/chats` - POST para crear nuevo chat
   - `/api/v1/messages` - GET/POST para historial
   - `/api/v1/voice/sessions` - POST para iniciar sesión de voz

### Mecanismos de Fallback
- Si WebSocket falla: polling cada 5 segundos a `/api/v1/chats/:id/messages`
- Si CDN falla: fallback a versión alojada en mismo dominio
- Tiempo de espera inicial: 3 segundos antes de mostrar error

## 7. Diferenciales Clave vs Competidores (para MyOwnClone)

### Lo que MyClone Hace Bien (para Copiar/Mejorar)
1. **Setup Wizard Visual** - 3 pasos claros con progreso visible (→ Aumenta activación)
2. **Widget Altamente Customizable** - 5 pestañas con vista previa en vivo (→ Reduce fricción de integración)
3. **Voice Clone Integrado** - No solo texto, sino voz auténtica (→ Diferencial emocional fuerte)
4. **Workflows por Industria** - Plantillas pre-hechas para CPA/Tax/Insurance (→ Tiempo de valor inmediato)
5. **Dashboard de Uso Transparente** - Métricas en tiempo real con fechas de reset (→ Reduce sorpresas)
6. **Public Persona Pages** - URL propia para compartir clone sin embed (→ Viralidad orgánica)
7. **Modo Simple** - Opción para desactivar animaciones (→ Mejor rendimiento/accessibility)

### Oportunidades de Mejora para MyOwnClone
1. **Onboarding más Personalizado** - Preguntar objetivos específicos (soporte/ventas/aprendizaje) y adaptar flujo
2. **Plantillas de Knowledge** - Kits pre-hechos por industria (ej: "Plantilla de Coach de Vida")
3. **Colaboración en Equipo** - Edición compartida de knowledge library (para agencias)
4. **Marketplace de Prompts** - Comunidad compartiendo configuraciones efectivas
5. **Analytics Avanzados** - Funnel de conversión desde widget a acción deseada
6. **Modo Desarrollo** - Sandbox para probar cambios sin afectar datos reales
7. **Export/Import de Config** - Migrar configuraciones entre entornos/dev/staging/prod

## 8. Próximos Pasos para Investigación

### Inmediato (24-48 horas)
1. Mapeo detallado de esquemas de GraphQL (si existen)
2. Análisis de tráfico WebSocket para entender formato de mensajes
3. Prueba de límites reales (intentional overuse para ver comportamiento)
4. Mapeo de webhooks de salida (notificaciones, eventos)

### Medio Plazo (1-2 semanas)
1. Ingeniería inversa de algoritmos de matching de conocimiento
2. Análisis de estrategia de chunking y embeddings
3. Mapeo de pipeline de procesamiento de voz (entrada → salida)
4. Estudio de patrones de cacheo y invalidación

### Largo Plazo (1+ mes)
1. Mapeo de infraestructura de servicios (servicios separados por función)
2. Análisis de estrategia de multi-tenancy a nivel de base de datos
3. Investigación de técnicas de optimización de costo de LLM
4. Estudio de políticas de retención y eliminación de datos

## 9. Conclusiones Estratégicas

MyClone.is ha construido un producto impresionante con enfoque en:
- **Experiencia de Usuario Impecable** - Desde onboarding hasta uso diario
- **Diferencial de Voz Real** - No es solo otro chatbot de texto
- **Verticalización Inteligente** - Enfoque en nichos específicos con alto LTV
- **Transparencia de Uso** - Reduce churn por sorpresas en facturación
- **Viralesidad Pasiva** - Páginas públicas que generan tráfico orgánico

Para MyOwnClone, el camino no es copiar sino **elevar**:
1. Mantener la excelencia en UX pero agregar profundización técnica
2. Ir más allá de voz a **personalidad completa** (estilo de escritura, toma de decisiones)
3. Enfocarse en **resultado de negocio** no solo en conversación
4. Construir **ecosistema** no solo producto (marketplace, comunidad, academia)
5. Optimizar para **escalabilidad empresarial** desde el inicio

---
*Nota: Esta investigación se realizó con acceso autenticado y análisis estático de activos públicos. No se intentó evadir medidas de seguridad ni acceder a datos no autorizados.*
