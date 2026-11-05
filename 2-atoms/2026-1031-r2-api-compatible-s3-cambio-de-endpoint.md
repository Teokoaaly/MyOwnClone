---
id: 2026-1031-r2-api-compatible-s3-cambio-de-endpoint
type: atom
certainty: solid
sources: [sources/2026-10-31-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-1031-backblaze-b2-storage-pricing]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Cloudflare R2 expone una API compatible con S3, de modo que se migra cambiando el endpoint (https://{your-account-id}.r2.cloudflarestorage.com) y conservando las herramientas, SDKs y pipelines existentes; el ejemplo oficial usa boto3 con endpoint_url, aws_access_key_id y aws_secret_access_key.

## Why It Matters
La compatibilidad S3 convierte R2 en un drop-in replacement y hace que la migración no dependa de reescribir código de aplicación, lo que es decisivo en un stack como el de MyOwnClone (Flask + Next.js) donde los artefactos de los clones se sirven desde object storage con SDKs estándar. Consecuencia económica: al poder mover el storage entre proveedores sin tocar la aplicación, el coste de almacenamiento pasa a ser una variable de negociación continua, no un compromiso de arquitectura — se puede comparar R2 ($0.015/GB-month, ver [[2026-1031-cloudflare-r2-storage]]) con B2 ($6.95/TB/mes, ver [[2026-1031-backblaze-b2-storage-pricing]]) y con S3 manteniendo el mismo código. Refuerza la lectura de [[2026-1022-costes-por-categoria-tenant]]: la infraestructura es reemplazable y por tanto el coste dominante del producto es el asiento, no el almacenamiento.
