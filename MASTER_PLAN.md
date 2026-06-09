# MASTER_PLAN.md — MyOwnClone
> Actualizado: 2026-06-09 | Estado: bootstrap operativo guiado
> Stack: Next.js 16 (App Router) + Flask 3 + PostgreSQL + Redis + Weaviate/pgvector

---

## RESUMEN EJECUTIVO

**MyOwnClone** es una plataforma SaaS multi-tenant para desplegar clones de IA orientados a enseñanza, soporte y ventas. El proyecto combina:

- **Frontend:** Next.js 16 + Drizzle ORM + NextAuth/Auth
- **Backend:** Flask + SQLAlchemy + Flask-Migrate/Alembic
- **Infra local:** PostgreSQL + Redis
- **IA:** proveedores LLM configurables vía `ModelManager`
- **Búsqueda semántica:** hoy con señales mixtas entre Weaviate y pgvector

### Estado real actual
El proyecto ya no está solo en fase de diagnóstico: **varios bloqueos críticos de runtime fueron corregidos**, pero todavía faltan los pasos manuales que demuestran que el sistema arranca de verdad extremo a extremo.

### Progreso ya consolidado
Las siguientes correcciones ya se consideran implementadas y verificadas a nivel de código:

- **TASK-001** — Fix del bug crítico en la URI de PostgreSQL en `api/app_factory.py`
- **TASK-002** — Eliminación de `stripe` duplicado en `api/requirements.txt`
- **TASK-006** — Corrección portable de `api/migrations/env.py`
- **TASK-007** — Creación de tablas base `accounts` y `tenants`
- **TASK-011** — Sustitución de stubs `Account` / `Tenant` por modelos SQLAlchemy reales
- **TASK-012** — Eliminación del import roto `api.models.model`
- **TASK-013** — Sustitución práctica de la dependencia problemática `graphon` mediante un `ModelManager` funcional
- **TASK-015** — Variables faltantes añadidas a `MyOwnClone/.env.example`
- **TASK-019** — Reemplazo de `datetime.utcnow()` por `datetime.now(timezone.utc)`
- **TASK-025** — README ampliado con instalación, comandos y arquitectura

### Bloqueadores actuales
Los bloqueadores principales ya no son tanto fallos de código aislados, sino **habilitar y validar el entorno operativo real**:

1. Falta crear los archivos `.env` locales con valores reales.
2. Falta instalar dependencias en el entorno actual.
3. Falta levantar PostgreSQL y Redis.
4. Falta habilitar `pgvector` para el esquema del frontend.
5. Falta ejecutar migraciones frontend y seed mínimo.
6. Falta verificar arranque real de backend y frontend.
7. Sigue abierta la decisión arquitectónica sobre la **fuente de verdad del esquema DB**: Drizzle vs Alembic.

### Riesgo estructural principal
El mayor riesgo de medio plazo no es un bug puntual, sino la coexistencia de:

- **Drizzle/Next.js** como sistema de esquema del frontend
- **Alembic/Flask** como sistema de esquema del backend

Ambos apuntan a la misma base de datos, con tablas duplicadas o semiduplicadas (`clone_configs`, `bookings`, `analytics_*`, `products`, etc.) y diferencias de naming/columnas. Antes de seguir ampliando funcionalidad de negocio, esta decisión debe formalizarse.

---

## ESTADO GENERAL POR ÁREA

### Frontend (Next.js)
- Estado estimado: **70% funcional a nivel de código**.
- Fortalezas: estructura limpia, base UI moderna, esquema Drizzle definido, README ya actualizado.
- Bloqueos actuales: variables de entorno reales, migraciones Drizzle pendientes, smoke test real del arranque y del login/dashboard.

### Backend (Flask)
- Estado estimado: **65% funcional a nivel de código**.
- Fortalezas: varios bloqueos críticos ya corregidos (`DB URI`, imports, modelos ORM base, `ModelManager`).
- Bloqueos actuales: validación real con PostgreSQL/Redis, seed mínimo, endurecimiento de endpoints y seguridad.

### Base de datos
- Estado estimado: **operable pero todavía no consolidada**.
- Positivo: ya existen correcciones sobre migraciones y tablas base del backend.
- Riesgo: la dualidad Drizzle/Alembic sigue sin resolverse de forma arquitectónica.

---

## DECISIONES Y ACLARACIONES IMPORTANTES

### 1. Sobre `down_revision = None`
Se elimina la interpretación anterior de que esto fuese necesariamente un hueco defectuoso. Si la primera migración standalone del proyecto actúa como raíz del historial, entonces `down_revision = None` **es correcto** y no debe presentarse como bug por sí mismo.

### 2. Sobre `TASK-014`
`TASK-014` queda **absorbida por `TASK-006`**, ya que ambas describían esencialmente el mismo arreglo de portabilidad en `api/migrations/env.py`.

### 3. Sobre `TASK-007` vs `TASK-011`
Se consideran tareas **relacionadas pero distintas**:

- **TASK-007:** creación de tablas base y migración raíz necesaria.
- **TASK-011:** integración runtime mediante modelos ORM reales `Account` y `Tenant`.

### 4. Sobre `TASK-013` vs `TASK-027`
No deben entenderse como duplicadas exactas:

- **TASK-013:** dejar operativo el runtime sustituyendo la dependencia problemática y habilitando un `ModelManager` funcional.
- **TASK-027:** endurecer esa capa con fallback robusto, retries, observabilidad y consistencia streaming/non-streaming.

---

## OBJETIVO INMEDIATO

Dejar el proyecto en un estado mínimo verificable:

- PostgreSQL y Redis levantados
- Migraciones backend aplicadas
- Migraciones frontend aplicadas
- Backend arranca en puerto 5001
- Frontend arranca en `http://localhost:3000`
- Login admin funciona
- Dashboard/admin overview responde
- Chat público responde con el LLM configurado

---

## PLAN CONSOLIDADO POR FASES

---

## FASE 1 — BOOTSTRAP LOCAL OBLIGATORIO

### TASK-003
**Título:** Crear `api/.env` y `MyOwnClone/.env.local` locales  
**Prioridad:** Crítica  
**Tipo:** devops/manual

**Objetivo:**
Crear los archivos de entorno locales con los secretos y valores mínimos necesarios para arrancar backend y frontend.

**Incluye:**
- Backend: `DB_PASSWORD`, `REDIS_PASSWORD`, `JWT_SECRET_KEY`, `IMPERSONATION_TOKEN_PEPPER`, `FLASK_ENV`, claves LLM si aplican.
- Frontend: `DATABASE_URL`, `NEXTAUTH_SECRET`/`AUTH_SECRET`, `NEXTAUTH_URL`, URL del backend y variables OAuth si se usan.

**Criterio de aceptación:**
- Backend deja de fallar por variables obligatorias faltantes.
- Frontend puede resolver su configuración base en desarrollo.

---

### TASK-004
**Título:** Instalar dependencias del backend y frontend  
**Prioridad:** Crítica  
**Tipo:** devops/manual

**Objetivo:**
Validar que el proyecto se instala correctamente en el entorno actual.

**Criterio de aceptación:**
- `pip install -r requirements.txt` y `pip install -r requirements-dev.txt` completan sin errores bloqueantes.
- `npm ci` completa sin errores críticos.

---

### TASK-005
**Título:** Levantar servicios Docker: PostgreSQL + Redis  
**Prioridad:** Crítica  
**Tipo:** devops/manual

**Objetivo:**
Levantar los servicios mínimos necesarios para validar el stack local.

**Criterio de aceptación:**
- PostgreSQL healthy
- Redis healthy
- Conexión local al servicio de base de datos funcional

> Nota: Weaviate no se considera bloqueador de arranque inicial si el objetivo es validar bootstrap y flujos básicos.

---

### TASK-009
**Título:** Instalar/habilitar extensión `pgvector` en PostgreSQL  
**Prioridad:** Alta  
**Tipo:** devops/manual

**Objetivo:**
Permitir que el esquema del frontend y las futuras piezas de retrieval puedan usar columnas vectoriales.

**Criterio de aceptación:**
```sql
SELECT * FROM pg_extension WHERE extname = 'vector';
```
retorna al menos una fila.

---

### TASK-008
**Título:** Ejecutar migraciones Drizzle del frontend  
**Prioridad:** Crítica  
**Tipo:** devops/manual

**Objetivo:**
Aplicar o sincronizar el esquema gestionado por Drizzle en la base de datos local.

**Criterio de aceptación:**
- `npm run db:generate` y/o `npm run db:push` / `npm run db:migrate` completan sin errores bloqueantes.
- Las tablas esperadas por el frontend quedan accesibles.

---

### TASK-010
**Título:** Sembrar datos iniciales: planes + admin  
**Prioridad:** Alta  
**Tipo:** devops/manual

**Objetivo:**
Crear datos mínimos para probar login y panel admin.

**Criterio de aceptación:**
- Los planes existen.
- Existe un usuario o configuración admin con la que probar autenticación y dashboard.

---

## FASE 2 — CORRECCIONES CRÍTICAS YA IMPLEMENTADAS

### TASK-001
**Título:** Corregir bug crítico en URI de PostgreSQL en `api/app_factory.py`  
**Estado:** ✅ Completada

### TASK-002
**Título:** Eliminar dependencia duplicada `stripe` en `requirements.txt`  
**Estado:** ✅ Completada

### TASK-006
**Título:** Corregir `api/migrations/env.py` para path portable y compatibilidad local  
**Estado:** ✅ Completada

### TASK-007
**Título:** Crear tablas base `accounts` y `tenants`  
**Estado:** ✅ Completada

### TASK-011
**Título:** Reemplazar modelos stub `Account` y `Tenant` por modelos SQLAlchemy reales  
**Estado:** ✅ Completada

### TASK-012
**Título:** Corregir importación rota `from api.models.model import App, Conversation, Message`  
**Estado:** ✅ Completada

### TASK-013
**Título:** Sustituir dependencia problemática `graphon.model_runtime` y habilitar `ModelManager` funcional  
**Estado:** ✅ Completada

### TASK-015
**Título:** Añadir variables faltantes a `.env.example` del frontend  
**Estado:** ✅ Completada

### TASK-019
**Título:** Sustituir `datetime.utcnow()` por `datetime.now(timezone.utc)`  
**Estado:** ✅ Completada

### TASK-025
**Título:** Actualizar `README.md` con instrucciones completas  
**Estado:** ✅ Completada

---

## FASE 3 — VERIFICACIÓN FUNCIONAL MÍNIMA

### TASK-034
**Título:** Verificar arranque real del backend  
**Prioridad:** Crítica  
**Tipo:** smoke test

**Objetivo:**
Validar que `flask --app app_factory run` arranca correctamente con el entorno local ya preparado.

**Criterio de aceptación:**
- El backend arranca sin `ImportError`, errores de DB ni excepciones tempranas de configuración.
- Los blueprints principales cargan correctamente.

---

### TASK-035
**Título:** Verificar arranque real del frontend  
**Prioridad:** Crítica  
**Tipo:** smoke test

**Objetivo:**
Validar que `npm run dev` arranca correctamente con el entorno local ya preparado.

**Criterio de aceptación:**
- La aplicación responde en `http://localhost:3000`.
- Login y dashboard renderizan sin fallos básicos de configuración.

---

### TASK-036
**Título:** Validar flujo mínimo end-to-end  
**Prioridad:** Crítica  
**Tipo:** smoke test

**Objetivo:**
Probar el primer circuito funcional completo.

**Flujo mínimo:**
1. login admin
2. acceso a dashboard
3. acceso a admin overview
4. prueba de chat público con clone válido

**Criterio de aceptación:**
- El sistema demuestra vida operativa más allá de compilación y migraciones.

---

## FASE 4 — ARQUITECTURA Y COHERENCIA DE BASE DE DATOS

### TASK-023
**Título:** Documentar y resolver la dualidad Drizzle vs Alembic  
**Prioridad:** Crítica  
**Tipo:** refactor/docs

**Objetivo:**
Definir formalmente la fuente de verdad del esquema de base de datos y cómo se coordinarán frontend y backend.

**Decisión pendiente:**
- Opción A: Alembic como fuente de verdad
- Opción B: Drizzle como fuente de verdad
- Opción C: modelo híbrido explícito con límites claros

**Recomendación actual para el MVP:**
Tomar una decisión explícita antes de seguir ampliando tablas de negocio. El coste de seguir sin resolverlo es creciente.

**Criterio de aceptación:**
- Existe una decisión documentada.
- Se sabe qué tablas viven dónde y cuál es la estrategia de evolución.

---

### TASK-024
**Título:** Corregir discrepancias críticas de esquema  
**Prioridad:** Alta  
**Tipo:** bugfix

**Casos identificados:**
- `bookings`
- `analytics_gaps`
- `creator_memory` vs `memories`

**Criterio de aceptación:**
- No hay incompatibilidades bloqueantes entre el esquema esperado por frontend y backend en las tablas críticas seleccionadas.

---

## FASE 5 — SEGURIDAD

### TASK-017
**Título:** Añadir rate limiting al endpoint de login  
**Prioridad:** Alta  
**Tipo:** security

**Criterio de aceptación:**
- El 6º intento fallido desde la misma IP dentro de la ventana configurada retorna `429`.

---

### TASK-020
**Título:** Hashear tokens de impersonación con SHA-256 + PEPPER  
**Prioridad:** Alta  
**Tipo:** security

**Criterio de aceptación:**
- Los tokens almacenados dejan de persistirse en texto plano.

---

### TASK-018
**Título:** Verificar firma webhook SendGrid en `/inbound-email`  
**Prioridad:** Media  
**Tipo:** security

**Criterio de aceptación:**
- El endpoint rechaza peticiones no firmadas o inválidas.

---

## FASE 6 — TESTS Y ESTABILIZACIÓN

### TASK-021
**Título:** Ejecutar y corregir tests del frontend  
**Prioridad:** Alta  
**Tipo:** testing

**Criterio de aceptación:**
- `npm test` pasa sin errores críticos.

---

### TASK-022
**Título:** Ejecutar y corregir tests del backend  
**Prioridad:** Alta  
**Tipo:** testing

**Criterio de aceptación:**
- `pytest` pasa al menos sobre la suite actualmente soportada por el entorno local configurado.

---

### TASK-026
**Título:** Crear CI básica con lint + test + build  
**Prioridad:** Media  
**Tipo:** devops

**Criterio de aceptación:**
- Existen workflows reproducibles para frontend y backend.

---

## FASE 7 — EVOLUCIÓN DE ARQUITECTURA Y PRODUCTO

### TASK-027
**Título:** Endurecer `ModelManager`  
**Prioridad:** Alta  
**Tipo:** feature/refactor

**Objetivo:**
Ampliar la implementación actual con:
- fallback robusto
- retries
- observabilidad
- consistencia entre streaming y non-streaming

---

### TASK-028
**Título:** Implementar retrieval RAG con pgvector  
**Prioridad:** Alta  
**Tipo:** feature

**Objetivo:**
Alinear la estrategia de retrieval con la decisión arquitectónica final de base de datos/vector store.

---

### TASK-029
**Título:** Mover `DEFAULT_CLONE_ID` a resolución dinámica por tenant  
**Prioridad:** Media  
**Tipo:** refactor

**Objetivo:**
Eliminar una dependencia global impropia de un SaaS multi-tenant.

---

## FASE 8 — FRONTEND Y UX

### TASK-030
**Título:** Verificar configuración Next.js 16  
**Prioridad:** Media  
**Tipo:** bugfix

### TASK-031
**Título:** Revisar accesibilidad básica  
**Prioridad:** Baja  
**Tipo:** refactor

---

## FASE 9 — DESPLIEGUE Y OPERACIÓN

### TASK-016
**Título:** Verificar existencia y correctitud de `alembic.ini`  
**Prioridad:** Alta  
**Tipo:** devops

### TASK-032
**Título:** Verificar scripts VPS `ops/deploy-backend.sh` y `ops/deploy-frontend.sh`  
**Prioridad:** Media  
**Tipo:** devops

### TASK-033
**Título:** Completar `docker-compose.prod.yml` consolidado  
**Prioridad:** Media  
**Tipo:** devops

---

## ROADMAP DE IMPLEMENTACIÓN PRIORITARIO ACTUALIZADO

| Orden | TASK | Descripción | Prioridad |
|-------|------|-------------|-----------|
| 1 | TASK-003 | Crear `.env` locales | Crítica |
| 2 | TASK-004 | Instalar dependencias | Crítica |
| 3 | TASK-005 | Levantar PostgreSQL + Redis | Crítica |
| 4 | TASK-009 | Habilitar `pgvector` | Alta |
| 5 | TASK-008 | Ejecutar migraciones Drizzle | Crítica |
| 6 | TASK-010 | Sembrar datos iniciales | Alta |
| 7 | TASK-034 | Verificar arranque del backend | Crítica |
| 8 | TASK-035 | Verificar arranque del frontend | Crítica |
| 9 | TASK-036 | Validar flujo end-to-end mínimo | Crítica |
| 10 | TASK-023 | Resolver fuente de verdad DB | Crítica |
| 11 | TASK-024 | Corregir discrepancias críticas de esquema | Alta |
| 12 | TASK-017 | Rate limiting en login | Alta |
| 13 | TASK-020 | Hash seguro de tokens de impersonación | Alta |
| 14 | TASK-018 | Verificación de firma SendGrid | Media |
| 15 | TASK-021 | Tests frontend | Alta |
| 16 | TASK-022 | Tests backend | Alta |
| 17 | TASK-026 | CI básica | Media |
| 18 | TASK-027 | Endurecer `ModelManager` | Alta |
| 19 | TASK-028 | RAG con pgvector | Alta |
| 20 | TASK-029 | `DEFAULT_CLONE_ID` dinámico | Media |

---

## MÉTRICA DE ESTADO CONSOLIDADA

| Categoría | Total | Completadas | Pendientes |
|-----------|-------|-------------|------------|
| 🚨 Críticas | 12 | 4 | **8** |
| 🔴 Altas | 13 | 3 | **10** |
| ⚠️ Medias | 8 | 2 | **6** |
| 🟢 Bajas | 2 | 1 | **1** |
| **TOTAL** | **35** | **10** | **25** |

> Nota: el total activo pasa a **35** porque `TASK-014` se absorbe en `TASK-006`, y se añaden `TASK-034`, `TASK-035` y `TASK-036` para reflejar los smoke tests operativos pendientes.

---

## CRITERIO FINAL DE ÉXITO

El proyecto se considerará listo para una base MVP estable cuando:

- `docker-compose up -d` levanta PostgreSQL + Redis sin errores
- `flask --app app_factory db upgrade` ejecuta migraciones sin errores
- `npm run db:push` / `npm run db:migrate` sincroniza el esquema frontend sin errores
- `flask --app app_factory run` arranca backend en puerto 5001
- `npm run dev` arranca frontend en `http://localhost:3000`
- Login admin funciona
- Dashboard/admin responde
- El chat público responde usando el proveedor LLM configurado
- `npm test` pasa en frontend
- `pytest` pasa en backend dentro del alcance soportado
- `npm run build` compila sin errores críticos
- `npx tsc --noEmit` termina sin errores de tipo
- Existe decisión explícita sobre la fuente de verdad del esquema DB

---

## REGISTRO DE CAMBIOS DEL PLAN

| Fecha | TASK | Cambio | Resultado |
|-------|------|--------|-----------|
| 2026-06-09 | — | Análisis inicial y diagnóstico | Plan creado |
| 2026-06-09 | TASK-001 | Fix URI PostgreSQL `***` → `DB_PASSWORD` real en `app_factory.py` | ✅ Corregido |
| 2026-06-09 | TASK-002 | Eliminado `stripe` duplicado en `requirements.txt` | ✅ Corregido |
| 2026-06-09 | TASK-006 | Fix `migrations/env.py` path Linux `/app/api` → ruta portable | ✅ Corregido |
| 2026-06-09 | TASK-007 | Nueva migración base para `tenants` + `accounts` | ✅ Creada |
| 2026-06-09 | TASK-011 | Modelos `Account` y `Tenant` reescritos como SQLAlchemy ORM reales | ✅ Corregido |
| 2026-06-09 | TASK-012 | Eliminado import roto de `App/Conversation/Message` del analytics | ✅ Corregido |
| 2026-06-09 | TASK-013 | `ModelManager` funcional implementado para proveedores reales | ✅ Implementado |
| 2026-06-09 | TASK-015 | Variables Google OAuth + AUTH_SECRET + Upstash añadidas a `.env.example` | ✅ Corregido |
| 2026-06-09 | TASK-019 | `datetime.utcnow()` → `datetime.now(timezone.utc)` | ✅ Corregido |
| 2026-06-09 | TASK-025 | README.md completo con instalación, comandos y arquitectura | ✅ Creado |
| 2026-06-09 | — | Consolidación del roadmap y alineación con `Task.md` | ✅ Actualizado |

---

## REFERENCIA OPERATIVA

El archivo **`Task.md`** debe considerarse el tablero operativo vivo.  
Este **`MASTER_PLAN.md`** actúa como documento de contexto, priorización y dirección arquitectónica.