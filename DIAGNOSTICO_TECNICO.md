# DIAGNOSTICO_TECNICO.md — MyOwnClone
> Diagnóstico técnico consolidado — 2026-06-09 | Estado: bootstrap operativo guiado

---

## 1. RESUMEN EJECUTIVO

**MyOwnClone** es una plataforma SaaS multi-tenant para desplegar clones de IA personalizados orientados a enseñanza, soporte y ventas, con piezas de RAG, email inbound/outbound, reservas, analíticas y facturación.

A diferencia del diagnóstico inicial, el proyecto **ya no está solo en fase de auditoría**: durante esta iteración se corrigieron varios bloqueos críticos de runtime y de configuración. El estado actual es más preciso si se describe como:

- **código base parcialmente saneado**, pero
- **entorno operativo todavía no validado extremo a extremo**.

### Estado consolidado por dimensión

| Dimensión | Estado actual | Nota |
|-----------|---------------|------|
| Frontend Next.js | 🟡 70% funcional a nivel de código | Falta validación real con `.env`, DB y arranque local |
| Backend Flask | 🟠 65% funcional a nivel de código | Se corrigieron varios bloqueos críticos; falta prueba real con servicios activos |
| Base de datos | 🟠 Operable pero no consolidada | Persisten dos fuentes de verdad parciales: Drizzle y Alembic |
| Seguridad | 🟡 Aceptable con gaps claros | Login sin rate limit, tokens de impersonación sin hash, webhook sin firma |
| Tests | 🟡 Configurados pero no validados | Existen suites, falta ejecutarlas y reparar fallos reales |
| CI/CD | 🔴 No consolidado | Existe `.github/`, pero la estrategia CI no está cerrada |
| Documentación | 🟢 Mejorada | README y plan operativo ya fueron actualizados |
| Despliegue | 🟡 Parcial | Scripts existen, pero falta verificar contra el estado actual |

### Estimación actualizada para llegar a MVP local verificable
**1-3 días de trabajo enfocado**, siempre que los pasos manuales de entorno no revelen nuevas incompatibilidades graves.

### Bloqueadores reales hoy
Los principales bloqueadores ya no son únicamente bugs de código aislados, sino estos puntos:

1. Crear `api/.env` y `MyOwnClone/.env.local` con valores reales.
2. Instalar dependencias y verificar compatibilidad local.
3. Levantar PostgreSQL + Redis.
4. Habilitar `pgvector`.
5. Ejecutar migraciones Drizzle y seed mínimo.
6. Verificar arranque real de backend y frontend.
7. Tomar una decisión formal sobre la **fuente de verdad del esquema DB**.

---

## 2. STACK DETECTADO

### Frontend
| Componente | Tecnología | Versión |
|-----------|-----------|---------|
| Framework | Next.js (App Router) | 16.2.6 |
| Runtime | React | 19.2.4 |
| Lenguaje | TypeScript | ^5 |
| ORM | Drizzle ORM | ^0.38.0 |
| Driver DB | pg (node-postgres) | ^8.13.0 |
| Auth | NextAuth v5 (beta) / Auth | 5.0.0-beta.25 |
| Estilos | Tailwind CSS | ^4 |
| i18n | next-intl | ^3.24.0 |
| Temas | next-themes | ^0.4.6 |
| LLM (Anthropic) | @anthropic-ai/sdk | ^0.36.0 |
| LLM (OpenAI) | openai | ^4.72.0 |
| Rate limiting | @upstash/ratelimit | ^2.0.4 |
| Email outbound | resend | ^4.0.1 |
| Pagos | stripe | ^17.1.0 |
| Tests | Vitest + Testing Library | ^2.1.0 |

### Backend
| Componente | Tecnología | Versión |
|-----------|-----------|---------|
| Framework | Flask | >=3.0.0 |
| ORM | SQLAlchemy + Flask-SQLAlchemy | >=2.0.0 / >=3.1.0 |
| Migraciones | Flask-Migrate (Alembic) | >=4.0.0 |
| CORS | Flask-CORS | >=4.0.0 |
| API docs | flask-restx | >=1.3.0 |
| Driver DB | psycopg2-binary | >=2.9.9 |
| Cache | redis-py | >=5.0.0 |
| Vector DB | weaviate-client | >=4.4.0 |
| Validación | pydantic | >=2.5.0 |
| Auth | PyJWT + bcrypt | >=2.8.0 / >=4.1.0 |
| Pagos | stripe | >=5.0.0 |
| Servidor | gunicorn | >=21.0.0 |
| Tests | pytest | dev |

### Base de datos / Infra local
| Servicio | Tecnología | Versión / Nota |
|---------|-----------|----------------|
| Principal | PostgreSQL | 15 |
| Cache | Redis | 7-alpine |
| Vector | Weaviate | 1.24.0 (no bloqueador inicial) |
| Extensión vectorial | pgvector | Pendiente habilitar en local |
| Orquestación | Docker + docker-compose | Disponible |

---

## 3. PROBLEMAS ENCONTRADOS — ESTADO ACTUALIZADO

> Esta sección distingue entre **resueltos a nivel de código**, **pendientes manuales/operativos** y **pendientes estructurales**. El objetivo es evitar que el diagnóstico quede desfasado respecto al estado real del repo.

### ✅ CRÍTICOS YA CORREGIDOS A NIVEL DE CÓDIGO

#### C-001: Bug URI PostgreSQL — literal `***` en lugar de contraseña
**Archivo afectado:** `api/app_factory.py`
**Estado:** ✅ Corregido

**Situación anterior:**
La URI de SQLAlchemy se construía con `:***@` en lugar de usar `DB_PASSWORD`.

**Impacto anterior:**
El backend no podía conectar a PostgreSQL.

**Estado actual:**
El bug fue corregido en código. Falta validar con entorno real y credenciales válidas.

---

#### C-002: Modelos `Account` y `Tenant` eran clases Python, no modelos ORM
**Archivo afectado:** `api/models/account.py`
**Estado:** ✅ Corregido

**Situación anterior:**
`select(Tenant)` / `select(Account)` rompían por no estar mapeados en SQLAlchemy.

**Estado actual:**
Los modelos fueron reemplazados por versiones ORM reales. Falta validación funcional real contra la DB levantada.

---

#### C-003: Tablas `accounts` y `tenants` faltaban en el árbol standalone
**Área afectada:** migraciones backend
**Estado:** ✅ Corregido a nivel de migración

**Situación anterior:**
Las FKs hacia `accounts` y `tenants` podían fallar en un entorno standalone.

**Estado actual:**
La base de tablas fue añadida por migración. Falta validar `flask db upgrade` en un entorno real limpio.

---

#### C-004: Dependencia `graphon` no instalada
**Archivos afectados:** `api/controllers/myownclone_public.py`, `api/core/model_manager.py`
**Estado:** ✅ Corregido operativamente

**Situación anterior:**
Los endpoints de chat y otras piezas de IA dependían de imports no disponibles en el repo.

**Estado actual:**
Se sustituyó la dependencia problemática por un `ModelManager` funcional para proveedores reales. Queda pendiente endurecimiento posterior (`TASK-027`).

---

#### C-005: Importación rota `from api.models.model import App, Conversation, Message`
**Archivo afectado:** `api/controllers/console/myownclone/analytics.py`
**Estado:** ✅ Corregido

**Situación anterior:**
El blueprint de analytics podía romper el arranque.

**Estado actual:**
La dependencia rota fue eliminada o degradada de forma segura.

---

#### C-006: `api/migrations/env.py` con ruta absoluta Linux hardcodeada
**Archivo afectado:** `api/migrations/env.py`
**Estado:** ✅ Corregido

**Situación anterior:**
`flask db upgrade` fallaba fuera del entorno Linux/Docker esperado.

**Estado actual:**
La configuración se volvió portable. `TASK-014` queda absorbida en esta misma corrección.

---

#### C-007: Variables faltantes en `.env.example` del frontend
**Archivo afectado:** `MyOwnClone/.env.example`
**Estado:** ✅ Corregido

**Situación anterior:**
Variables de Auth/OAuth no estaban documentadas de forma consistente.

**Estado actual:**
El ejemplo fue ampliado. Sigue faltando crear el `.env.local` real.

---

#### C-008: Uso de `datetime.utcnow()` obsoleto
**Archivos afectados:** `auth.py`, `admin_platform.py`
**Estado:** ✅ Corregido

---

#### C-009: Dependencia duplicada `stripe` en backend
**Archivo afectado:** `api/requirements.txt`
**Estado:** ✅ Corregido

---

### 🚨 CRÍTICOS PENDIENTES OPERATIVOS

#### O-001: No existen todavía los `.env` locales efectivos
**Estado:** ❌ Pendiente manual

**Impacto:**
Sin `api/.env` y `MyOwnClone/.env.local`, no puede demostrarse que el stack arranca realmente.

---

#### O-002: Dependencias no verificadas en el entorno local actual
**Estado:** ❌ Pendiente manual

**Impacto:**
Aunque el código esté saneado, sigue faltando verificar que `pip install` y `npm ci` funcionen sin conflictos en el entorno real.

---

#### O-003: PostgreSQL y Redis aún no levantados en el circuito de validación
**Estado:** ❌ Pendiente manual

**Impacto:**
No hay prueba operativa de que el backend llegue a hablar con la infraestructura local.

---

#### O-004: `pgvector` no habilitado todavía
**Estado:** ❌ Pendiente manual

**Impacto:**
El esquema del frontend y la evolución del retrieval pueden romper o quedar incompletos.

---

#### O-005: Migraciones Drizzle todavía no validadas en entorno real
**Estado:** ❌ Pendiente manual

**Impacto:**
El frontend sigue sin una validación real de su esquema sobre PostgreSQL local.

---

#### O-006: Seed mínimo de datos no ejecutado/validado
**Estado:** ❌ Pendiente manual

**Impacto:**
No hay circuito fiable para probar login/dashboard/admin end-to-end.

---

#### O-007: No existe todavía smoke test real backend/frontend/end-to-end
**Estado:** ❌ Pendiente

**Impacto:**
Todavía no puede afirmarse que el producto “respira” más allá de las correcciones estáticas de código.

---

### 🔴 ALTOS PENDIENTES

#### A-001: Login sin rate limiting
**Archivo:** `api/controllers/console/auth.py`
**Estado:** ❌ Pendiente

**Impacto:**
Riesgo de fuerza bruta sin límite razonable por IP/ventana temporal.

---

#### A-002: Tokens de impersonación almacenados en texto plano
**Archivo:** `api/controllers/console/myownclone/admin_platform.py`
**Estado:** ❌ Pendiente

**Impacto:**
Compromiso directo si la base de datos es expuesta.

---

#### A-003: Webhook SendGrid sin verificación de firma
**Archivo:** `api/controllers/myownclone_public.py`
**Estado:** ❌ Pendiente

**Impacto:**
Permite POSTs fraudulentos hacia el endpoint inbound.

---

#### A-004: Modelo de chat/LLM funcional pero todavía no endurecido
**Área:** `ModelManager`
**Estado:** ❌ Pendiente parcial

**Impacto:**
Falta robustez operativa: fallback consistente, retries, observabilidad y alineación entre streaming y non-streaming.

---

### ⚠️ MEDIOS / ESTRUCTURALES PENDIENTES

#### M-001: Dualidad de esquemas DB — dos fuentes de verdad parciales
**Estado:** ❌ Pendiente estructural

**Descripción:**
Frontend y backend siguen definiendo y usando parcialmente el mismo dominio de datos desde sistemas diferentes:

- Drizzle/Next.js
- Alembic/SQLAlchemy/Flask

**Ejemplos de divergencia:**
- `clone_configs`: `personality_tone` vs `personality` + `tone`
- `bookings`: `start_time`/`end_time` vs `time`
- `creator_memory` vs `memories`

**Impacto:**
Es el principal riesgo de arquitectura a medio plazo.

---

#### M-002: `DEFAULT_CLONE_ID` hardcodeado
**Estado:** ❌ Pendiente

**Impacto:**
No encaja con un modelo SaaS multi-tenant real.

---

#### M-003: Validación de input mejorable en endpoints públicos
**Estado:** ❌ Pendiente

**Impacto:**
Hay validaciones funcionales, pero no una política suficientemente robusta para entradas sensibles como bookings/email.

---

#### M-004: Pool DB sin límites explícitos
**Estado:** ❌ Pendiente

**Impacto:**
Riesgo bajo carga si el backend comienza a recibir tráfico sostenido.

---

#### M-005: Estrategia de tests no validada en entorno actual
**Estado:** ❌ Pendiente

**Impacto:**
No se sabe todavía qué parte de la suite es realmente estable hoy.

---

### 🟢 BAJOS / MEJORAS

#### B-001: Dependencias sin lock determinista estricto
#### B-002: Comentarios de código mezclan español e inglés
#### B-003: Enum `teach` vs `pedagogy` requiere revisión funcional
#### B-004: `uuidv7()` aparenta UUIDv7 pero envuelve `uuid4()`
#### B-005: `DEPLOY_SECRET` con documentación incompleta

---

## 4. BUENAS PRÁCTICAS — ESTADO REVISADO

### Organización del código
- ✅ Estructura de blueprints Flask razonable
- ✅ Separación general controllers/models/services
- ❌ Persisten queries SQL en controladores
- ❌ La capa de servicios sigue siendo ligera/incompleta

### Variables de entorno
- ✅ `.env.example` existe en ambos lados
- ✅ Validación fail-fast en backend
- ✅ Variables faltantes principales del frontend ya documentadas
- ❌ Aún no existen los `.env` reales del entorno local

### Manejo de errores
- ✅ Hay logging y manejo básico en endpoints
- ✅ Varias roturas de imports ya fueron eliminadas
- ❌ Sigue faltando una estrategia más centralizada de manejo de errores Flask
- ❌ El streaming requiere endurecimiento y trazabilidad mejores

### Validaciones
- ✅ Tipado razonable en backend y frontend
- ❌ Falta reforzar validación/sanitización en algunos endpoints públicos

### Seguridad
- ✅ bcrypt para passwords
- ✅ checks de producción y comparaciones timing-safe presentes en partes del stack
- ❌ sin rate limiting de login
- ❌ tokens de impersonación en texto plano
- ❌ sin verificación de firma SendGrid
- ❌ faltan headers HTTP de hardening si se aspira a despliegue serio

### Testing
- ✅ Vitest configurado en frontend
- ✅ pytest configurado en backend
- ❌ no se ha validado todavía el estado real de las suites tras los cambios recientes
- ❌ sin smoke tests end-to-end automatizados

### Documentación
- ✅ `README.md` ya fue ampliado
- ✅ `MASTER_PLAN.md` y `Task.md` ya reflejan mejor el estado operativo
- ❌ sigue faltando cerrar formalmente la arquitectura DB como documento/decisión explícita

### Docker / entorno local
- ✅ `docker-compose.yml` y healthchecks existen
- ✅ hay base operativa para levantar servicios
- ❌ falta ejecutar la validación real del circuito local
- ❌ `pgvector` sigue pendiente de habilitación efectiva

### Logs y monitoreo
- ✅ logging Python presente
- ✅ hay referencias a Sentry/PostHog en configuración
- ❌ falta validar integración real de observabilidad

### Performance
- ✅ existen índices y ajustes básicos (`pool_pre_ping`, `pool_recycle`)
- ❌ faltan límites explícitos de pool
- ❌ hay riesgo de N+1 en serialización/listados

### Accesibilidad / UX
- No auditado todavía en profundidad

---

## 5. HALLAZGOS ESPECIALES

### 5.1. El proyecto sigue mostrando huellas claras del fork original
La base parece provenir de una adaptación/fork del ecosistema Dify. Eso no es un problema en sí, pero explica por qué aparecieron referencias heredadas (`graphon`, `api.models.model`, entidades del core original) que luego hubo que sanear para el modo standalone.

### 5.2. El problema principal ya no es “qué está roto”, sino “qué es fuente de verdad”
Buena parte de los bugs de arranque más visibles ya se corrigieron. El siguiente riesgo serio no es un import roto puntual, sino seguir desarrollando sin cerrar la relación entre:

- el esquema del frontend (Drizzle)
- el esquema del backend (Alembic/ORM)

### 5.3. La validación operativa real ahora es el cuello de botella
A estas alturas, más que seguir acumulando teoría, el valor está en ejecutar el siguiente bloque:

1. `.env`
2. instalaciones
3. Docker
4. `pgvector`
5. migraciones Drizzle
6. seed
7. arranque backend/frontend
8. flujo mínimo end-to-end

Hasta completar eso, el estado del proyecto sigue siendo “prometedor pero no demostrado”.

### 5.4. El enum `teach` vs `pedagogy` sigue siendo un hallazgo a revisar
La divergencia de enums entre backend y frontend continúa siendo una señal de que la capa de dominio todavía no está totalmente consolidada entre ambos lados.

---

## 6. CONCLUSIÓN PRÁCTICA

### Lo que ya puede afirmarse
- El repositorio está **más sano** que al inicio de la auditoría.
- Se resolvieron varios bloqueos críticos de runtime y configuración.
- La documentación principal fue alineada y el backlog fue reorganizado.

### Lo que todavía no puede afirmarse con honestidad
- Que el stack local completo arranca sin fricciones.
- Que frontend y backend ya conviven sin conflictos de esquema.
- Que los tests pasan.
- Que el flujo login → dashboard → admin → chat funciona extremo a extremo.

### Prioridad recomendada inmediata
1. bootstrap local real
2. smoke tests backend/frontend/end-to-end
3. decisión formal sobre fuente de verdad DB
4. seguridad básica
5. tests y CI

---

*Fin del diagnóstico técnico consolidado*