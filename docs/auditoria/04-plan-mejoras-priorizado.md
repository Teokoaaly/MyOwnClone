# 04 - Plan de mejoras priorizado

| Hallazgo | Severidad | Impacto | Recomendación | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| `package-lock.json` desincronizado con `package.json` | Alta | `npm ci` falla; despliegues no son reproducibles. | Regenerar lockfile en entorno controlado, revisar diff, volver a `npm ci` en deploy. | M | P0 |
| Acceso SSH no interactivo no disponible para auditoría | Alta | No se puede cerrar inventario VPS ni verificar drift actual. | Restaurar acceso temporal con llave auditada o bastion; revocar al terminar. | S | P0 |
| Nginx productivo fue corregido manualmente | Alta | Riesgo de regresión si se reprovisiona desde config antigua. | Aplicar `ops/nginx.myownclone.conf.example` como fuente versionada y documentar reload. | S | P0 |
| Backups PostgreSQL no están automatizados/versionados | Alta | Riesgo de pérdida de datos. | Crear job `pg_dump` diario cifrado + prueba mensual de restore. | M | P1 |
| Observabilidad limitada | Alta | Incidentes tardan más en diagnosticarse. | Añadir métricas, alertas 5xx/p95, Sentry o equivalente y runbooks. | M | P1 |
| Secretos gestionados en archivos del VPS | Media | Rotación manual y mayor riesgo operativo. | Migrar a secret manager o Ansible Vault/SOPS; mantener permisos 0600 si sigue en archivo. | M | P1 |
| CI no valida deploy scripts/Nginx | Media | Drift entre repo y producción. | Añadir shellcheck, `nginx -t` en contenedor y smoke tests. | M | P2 |
| Rutas admin dependen de proxy Next + Flask service key | Media | Config incorrecta causa 401/403. | Mantener smoke autenticado y test de proxy; documentar flujo. | S | P2 |
| Doble modelo DB (`accounts` backend y `users` NextAuth legacy) | Media | Riesgo de inconsistencia de identidad. | Definir tabla canónica y migración de consolidación. | L | P2 |
| E2E con skips por datos/sesión | Media | Flujos críticos sin prueba completa. | Seed staging y test login-dashboard-chat-billing. | M | P2 |
| Manual de usuario inexistente hasta esta rama | Baja | Mayor carga de soporte. | Mantener `/docs/manual-usuario/README.md` por release. | S | P3 |

