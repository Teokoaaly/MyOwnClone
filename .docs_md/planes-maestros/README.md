# Planes Maestros — MyOwnClone VPS

> **Fecha**: 2026-07-02
> **Autor**: Auditoría backend en vivo (sesión de deploy + OSINT)
> **Idioma**: Español por defecto
> **Destinatario**: LLM barato (Haiku, Sonnet, GLM-4, etc.) que ejecutará los tasks

---

## Cómo usar estos planes

Cada plan es **autocontenido**. Un LLM puede tomar un plan, leerlo completo, y ejecutar sus tasks en orden sin contexto adicional. Cada task tiene:

- **ID único** (para tracking)
- **Comando exacto** o código a ejecutar
- **Criterio de verificación** (cómo saber que está hecho)
- **Rollback** (qué hacer si falla)
- **Dependencias** (qué task debe estar hecho antes)

## Reglas para el LLM ejecutor

1. **Un task a la vez.** No pidas hacer 2 tasks en paralelo sin autorización.
2. **Verifica antes de avanzar.** Cada task tiene un criterio de éxito. Si no se cumple, NO avances al siguiente.
3. **Producción con usuarios reales.** El VPS `212.227.169.99` está en producción. Cualquier mistake rompe el servicio.
4. **Acceso SSH**: `ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99`
5. **Rama de trabajo**: Los cambios de código van en `codex/backend-admin-vps-exec` (la rama compatible con la DB del VPS).
6. **Idioma**: Todos los comentarios, mensajes de commit, nombres de variables y documentación deben estar en **español** cuando sea contenido nuevo. Los nombres de variables/clases siguen en inglés (convención del código existente).
7. **Commits**: Un commit por task, con mensaje `feat/fix/chore(<scope>): <task-id> <descripción>`.
8. **Si algo rompe producción**: Rollback inmediato (cada plan tiene las instrucciones) y reportar.

---

## Índice de planes

| Plan | Foco | Tasks | Tiempo estimado | Urgencia |
|---|---|---|---|---|
| **[FASE 1](./FASE-1-ESTABILIZAR.md)** | Estabilizar backend | 8 tasks | 4-6 horas | 🔴 Crítico |
| **[FASE 2](./FASE-2-RAG-MODELO-IA.md)** | RAG + modelo IA + widget | 12 tasks | 3-5 días | 🟡 Importante |
| **[FASE 3](./FASE-3-ESCALAR.md)** | Escalar infraestructura | 7 tasks | 1-2 semanas | 🟢 Futuro |

### Orden de ejecución

```
FASE 1 (estabilizar) → FASE 2 (RAG + IA) → FASE 3 (escalar)
```

No saltar fases. Cada una depende de la anterior.

---

## Estado actual del VPS (snapshot 2026-07-02)

```
Release:     20260701150141-backend-codex-deploy (f0418c0)
Frontend:    Next.js 16.2.9, BUILD_ID rdQyAFlq
Backend:     Flask + gunicorn (2 workers) en Docker
DB:          PostgreSQL 15 + pgvector 0.8.2 (9.6 MB, 32 tablas)
Redis:       7-alpine (rate limit + cache)
Weaviate:    1.24.0 (115 KB, apenas usado)
Ollama:      mxbai-embed-large (embeddings locales)
CPU:         2 cores
RAM:         3.8 GB (2.4 disponibles)
Disco:       83 GB libres de 116 GB
```

## Acceso al VPS

```bash
# Conectar por SSH
ssh -i ~/.ssh/myownclone_vps_ed25519 root@212.227.169.99

# Layout del deploy
/opt/myownclone/
  current → releases/<release-id>     # symlink activo
  releases/                           # historial de releases
  shared/
    backend.env.production            # secrets del backend
    frontend.env.production           # secrets del frontend
  backups/                            # pg_dump diarios

# Comandos útiles
systemctl restart myownclone-frontend          # reiniciar frontend
cd /opt/myownclone/current/ops && docker compose -f docker-compose.backend.prod.yml up -d --build  # reiniciar backend
docker exec myownclone_postgres psql -U postgres -d myownclone   # entrar a la DB
```

## Rama de trabajo para cambios de código

```bash
# Rama compatible con la DB del VPS (Lineage A)
git checkout codex/backend-admin-vps-exec

# NO usar vps-fixes ni sisyphus/anti-forget-layer (Lineage B, incompatible con DB)
```

---

*Estos planes están basados en la auditoría en vivo del VPS del 2026-07-02 y el compendio OSINT de myclone.is.*
