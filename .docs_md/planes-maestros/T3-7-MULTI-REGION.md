# T3.7 — Multi-región / Alta disponibilidad (DOCUMENTACIÓN)

**Fecha**: 2026-07-03
**Estado**: Solo documentado. No aplica al estado actual.

## Cuándo es necesario

| SLA objetivo | Costo/mes aprox. | Cuándo |
|---|---|---|
| 99% (3.65 días/año downtime) | €10-20 | VPS actual OK |
| 99.9% (8.76 horas/año) | €80-150 | >1000 usuarios activos |
| 99.99% (52 min/año) | €300-800 | >10k usuarios activos |

**El VPS actual está en 99%+. Para 99.9%+ necesitas multi-región.**

## Arquitectura multi-región

```
                          ┌─ DNS Failover (Cloudflare o Route53) ─┐
                          │                                         │
              ┌───────────┴───────────┐                             │
              ↓                       ↓                             ↓
        VPS EU (primary)        VPS US (replica)              Health checks
        ┌─────────────┐         ┌─────────────┐
        │ App + DB    │         │ App (read)   │
        │ Primary     │ ←─────→ │ Postgres     │
        └─────────────┘  WAL    │ Streaming    │
                                └─────────────┘
```

## Componentes clave

### 1. DNS failover
- Cloudflare Load Balancer (gratis hasta 1M queries)
- O Route53 con health checks

### 2. Postgres replicación síncrona entre regiones
- **Patroni** + etcd: líder automático
- O **Postgres logical replication** con failover manual

### 3. Almacenamiento de objetos distribuido
- S3 (eu-central-1 + us-east-1) para backups cross-region
- CloudFront CDN delante de S3

### 4. Sesiones compartidas
- Redis cluster (multi-AZ)
- O JWT stateless (no requiere sesión server-side)

## Setup mínimo viable (cuando se necesite)

### Opción A: Read replicas en otra región
- Primary en EU, replica read-only en US
- Cloudflare LB: 100% a EU, fallback a US si EU caído
- Coste: +€40/mes por 1 VPS replica

### Opción B: Multi-región activo-activo
- Mismo stack en 2+ regiones
- DNS con health checks (Cloudflare)
- Postgres con logical replication bidireccional (complejo)
- Coste: +€200-400/mes

## Cuándo NO es multi-región

- **<1000 usuarios activos** — el VPS actual + backups off-site es suficiente
- **App no crítica** (downtime tolerable de horas) — un solo VPS está bien
- **Presupuesto limitado** — el dinero se gasta mejor en features que en HA

## Estado actual del proyecto

- ✅ 1 VPS (212.227.169.99) en producción
- ✅ Backups locales (cron 03:00)
- ✅ Backups off-site: work in progress (T1.1 Tarea -FASE 1)
- ❌ Multi-región
- ❌ Failover automático
- ❌ CDN global (Cloudflare en frente de nginx)

## Recomendación

**No implementar hasta tener >500 usuarios activos Y un modelo de ingresos que justifique el coste.**

El dinero ahorrado en infraestructura debería invertirse en:
- Features que retenen usuarios
- Marketing para conseguir más usuarios
- Soporte al cliente

HA viene cuando el producto crece, no antes.