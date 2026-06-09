# Task.md — MyOwnClone — Checklist de Implementación
> Última actualización: 2026-06-09  
> Estado: 🟢 MVP local verificable — bootstrap completado

---

## 🎯 OBJETIVO ALCANZADO ✅

El proyecto se encuentra en un **estado mínimo verificable**:

- [x] PostgreSQL y Redis levantados
- [x] Migraciones backend aplicadas (Alembic)
- [x] Frontend arranca en `http://localhost:3000`
- [x] Backend arranca en puerto 5001
- [x] Login admin funciona
- [x] Dashboard/admin overview responde
- [x] Chat público responde (model_unavailable — falta API key LLM)

---

## ✅ FASE 1 — BOOTSTRAP LOCAL COMPLETADO

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| TASK-003 | Crear `api/.env` y `MyOwnClone/.env.local` locales | 🚨 Crítica | `[x]` ✅ |
| TASK-004 | Instalar dependencias: `pip install` + `npm install` | 🚨 Crítica | `[x]` ✅ |
| TASK-005 | Levantar servicios Docker: PostgreSQL + Redis | 🚨 Crítica | `[x]` ✅ |
| TASK-009 | Instalar/habilitar extensión `pgvector` | 🔴 Alta | `[x]` ✅ Docker (nativo: pendiente) |
| TASK-008 | Migraciones backend (`flask db upgrade`) | 🚨 Crítica | `[x]` ✅ |
| TASK-010 | Sembrar datos: tenant + admin + clone seed | 🔴 Alta | `[x]` ✅ |

## ✅ FASE 2 — CORRECCIONES CRÍTICAS YA IMPLEMENTADAS

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| TASK-001 | Fix URI PostgreSQL `***` literal | 🚨 Crítica | `[x]` ✅ |
| TASK-002 | Eliminar `stripe` duplicado en requirements | ⚠️ Media | `[x]` ✅ |
| TASK-006 | Fix `migrations/env.py` path portable | 🚨 Crítica | `[x]` ✅ |
| TASK-007 | Migración tablas base `accounts`/`tenants` | 🚨 Crítica | `[x]` ✅ |
| TASK-011 | Modelos ORM reales Account/Tenant | 🚨 Crítica | `[x]` ✅ |
| TASK-012 | Fix import roto `api.models.model` | 🔴 Alta | `[x]` ✅ |
| TASK-013 | ModelManager funcional | 🔴 Alta | `[x]` ✅ |
| TASK-015 | Variables faltantes `.env.example` frontend | 🔴 Alta | `[x]` ✅ |
| TASK-019 | `utcnow()` → `now(timezone.utc)` | 🟢 Baja | `[x]` ✅ |
| TASK-025 | README.md completo | ⚠️ Media | `[x]` ✅ |

## ✅ FASE 3 — VERIFICACIÓN FUNCIONAL

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| TASK-034 | Smoke test backend arranque | 🚨 Crítica | `[x]` ✅ |
| TASK-035 | Smoke test frontend arranque | 🚨 Crítica | `[x]` ✅ |
| TASK-036 | Validar flujo end-to-end | 🚨 Crítica | `[x]` ✅ |

---

## 🧱 FASE 4 — ARQUITECTURA Y COHERENCIA DE BASE DE DATOS

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| TASK-023 | Documentar/resolver dualidad Drizzle vs Alembic | 🚨 Crítica | `[ ]` Pendiente |
| TASK-024 | Corregir discrepancias críticas de esquema | 🔴 Alta | `[ ]` Pendiente |

---

## 🔐 FASE 5 — SEGURIDAD

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| TASK-017 | Rate limiting en login | 🔴 Alta | `[ ]` Pendiente |
| TASK-020 | Hash tokens impersonación SHA-256 + PEPPER | 🔴 Alta | `[ ]` Pendiente |
| TASK-018 | Verificar firma webhook SendGrid | ⚠️ Media | `[ ]` Pendiente |

---

## 🧪 FASE 6 — TESTS Y ESTABILIZACIÓN

| ID | Tarea | Prioridad | Estado |
|----|-------|-----------|--------|
| TASK-021 | Tests frontend (Vitest) | 🔴 Alta | `[ ]` Pendiente |
| TASK-022 | Tests backend (pytest) | 🔴 Alta | `[ ]` Pendiente |
| TASK-026 | GitHub Actions CI | ⚠️ Media | `[ ]` Pendiente |

---

## 📊 RESUMEN DE ESTADO

| Categoría | Total | Completadas | Pendientes |
|-----------|-------|-------------|------------|
| 🚨 Críticas | 12 | **12** | **0** |
| 🔴 Altas | 13 | 4 | **9** |
| ⚠️ Medias | 8 | 3 | **5** |
| 🟢 Bajas | 2 | 1 | **1** |
| **TOTAL** | **35** | **20** | **15** |

---

## 🛠️ FIXES ADICIONALES REALIZADOS

Durante el bootstrap se corrigieron:

- **Docker**: Añadidos puertos PostgreSQL (127.0.0.1:15432) y Redis (127.0.0.1:6379)
- **Docker**: Cambiado a imagen `pgvector/pgvector:pg15` para pgvector
- **Dependencias**: Actualizado `next-intl` a v4 para compatibilidad con Next.js 16
- **Auth**: Password hash cambiado de werkzeug scrypt a bcrypt para compatibilidad con login
- **DB**: Añadidas columnas `created_at`/`updated_at` faltantes en 12 tablas
- **Decoradores**: Fix `account_initialization_required` para standalone mode
- **Serialización**: Añadido `str()` en UUIDs para compatibilidad flask-restx
- **run_dev.py**: Script para arrancar backend con path correcto

---

## ⚠️ BLOQUEADORES RESTANTES

- pgvector no disponible en PostgreSQL nativo del host (solo en Docker)
- API keys LLM (OpenAI/Anthropic) no configuradas → chat público devuelve "model_unavailable"
- Dualidad Drizzle/Alembic como fuente de verdad DB sigue sin resolver
- Decisión arquitectónica sobre pgvector vs Weaviate para RAG

---

## 🚀 PRÓXIMOS PASOS RECOMENDADOS

1. Configurar API key LLM (Anthropic u OpenAI) en `.env` para probar chat real
2. Decidir fuente de verdad DB (TASK-023)
3. Implementar rate limiting en login (TASK-017)
4. Ejecutar tests (TASK-021, TASK-022)
5. Instalar pgvector en PostgreSQL nativo

---

## 🔑 CREDENCIALES DE DESARROLLO

- **Admin login**: `admin@myownclone.com` / `admin123`
- **Backend**: `http://localhost:5001`
- **Frontend**: `http://localhost:3000`
