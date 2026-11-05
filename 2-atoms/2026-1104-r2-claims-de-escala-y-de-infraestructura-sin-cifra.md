---
id: 2026-1104-r2-claims-de-escala-y-de-infraestructura-sin-cifra
type: atom
certainty: tentative
sources: [sources/2026-11-04-cloudflare-r2-storage.md]
links: ["[[2026-1031-cloudflare-r2-storage]]", "[[2026-1104-r2-tabla-de-precios-sin-cambios-en-cuarta-captura-del-slug]]", "[[2026-1102-r2-ecosistema-plataforma-que-se-vende-junto]]"]
---

## Claim
La página de producto de R2 apoya su argumento de escalabilidad en tres claims que **no llevan ninguna cifra verificable**: "Near-infinite scale — Access data from anywhere, create millions of buckets, and write as much data as you need"; "Built on systems powering 20% of the Internet, R2 runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard"; y el bloque de cierre "Predictable pricing without surprises" / "Deploy to 330+ cities instantly". El único dato numérico con forma de infraestructura es el **20%** de Internet, que se presenta sin fuente ni método.

## Why It Matters
Sirve de contraste con el resto del corpus de precios del vault, donde cada proveedor publica cifras auditables: la tabla de R2 es precisa al céntimo ([[2026-1104-r2-tabla-de-precios-sin-cambios-en-cuarta-captura-del-slug]]), pero los claims de escala que la rodean no lo son. La consecuencia práctica para el hilo de hosting barato es que **"near-infinite scale" y "millions of buckets" no son un dato de capacidad que se pueda contrastar**: el límite relevante para un producto real es si existe un mínimo, un máximo por cuenta o una cuota de requests, y la página no publica ninguno. Junto al catálogo de primitivas que Cloudflare vende junto a R2 ([[2026-1102-r2-ecosistema-plataforma-que-se-vende-junto]]), la lectura es que la página está vendiendo plataforma, no un límite de capacidad verificable.

## Nota de caveat
Se registra como `tentative`: son afirmaciones del proveedor sobre su propia infraestructura, no hechos verificados por el vault. El "20% of the Internet" es una cifra rounda y sin metodología en la captura; no debe usarse como métrica comparable.
