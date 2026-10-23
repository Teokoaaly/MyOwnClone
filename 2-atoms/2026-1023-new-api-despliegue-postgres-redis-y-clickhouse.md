---
id: 2026-1023-new-api-despliegue-postgres-redis-y-clickhouse
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El README define la topología de despliegue de forma explícita:

- **Quick start local**: una sola instancia Docker con **SQLite**, ligada a `127.0.0.1:3000`, con el directorio `data` montado para persistir la base entre recambios de contenedor, y un asistente de setup para crear la cuenta de administrador.
- **Producción**: el `docker-compose.yml` del repositorio arranca **New API + PostgreSQL + Redis** por defecto, e incluye ejemplos para **MySQL** y una **base de datos de logs separada en ClickHouse**.
- **Opciones de almacenamiento**: base principal **SQLite, MySQL ≥ 5.7.8 o PostgreSQL ≥ 9.6**; base de logs opcional vía `LOG_SQL_DSN` (también ClickHouse); caché **Redis opcional + caché en memoria**; plataformas de contenedor **Linux amd64 / arm64**.

## Why It Matters
Fija el **suelo de infraestructura** de este tipo de relay: SQLite en local, pero **tres servicios (app + Postgres + Redis) en producción**, más ClickHouse si se quiere separar el log de consumo. Es un dato de coste relevante porque los patrocinadores chinos de PriceAI promocionan VPS de 2 vCPU a decenas de yuanes al año para auto-hospedar un relay ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]): con este README se puede decir que el relay **más simple** (SQLite, un contenedor) cabe en un VPS de 2 vCPU, mientras que la topología de referencia no cabe en un presupuesto de 4 €/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]).
Para el vault, que ya vive en nginx sobre VPS propio ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), el patrón "app + Postgres + Redis" es exactamente lo que significa añadir un componente con estado a una infraestructura hoy stateless.
